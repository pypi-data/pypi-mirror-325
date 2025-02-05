import cv2
import os
from skimage.metrics import structural_similarity as ssim


class VisualAssertion:
    def __init__(self, threshold=0.9):
        self.threshold = threshold
        self.report_dir = "report/image"

    def resize_to_smallest(self, image1, image2):
        height1, width1 = image1.shape[:2]
        height2, width2 = image2.shape[:2]
        new_height = min(height1, height2)
        new_width = min(width1, width2)
        image1_resized = image1[:new_height, :new_width]
        image2_resized = image2[:new_height, :new_width]
        return image1_resized, image2_resized

    def compare_images(self, image1_path, image2_path):
        image1 = cv2.imread(image1_path)
        image2 = cv2.imread(image2_path)
        
        image1, image2 = self.resize_to_smallest(image1, image2)
        
        gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        score, diff = ssim(gray_image1, gray_image2, full=True)
        return score, diff

    def save_diff_image_with_boxes(self, image1_path, image2_path, diff_filename="diff.png"):
        if not diff_filename.lower().endswith(".png"):
            diff_filename += ".png"
        
        diff_path = os.path.join(self.report_dir, diff_filename)
        score, diff = self.compare_images(image1_path, image2_path)
        diff = (diff * 255).astype("uint8")

        _, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        image1 = cv2.imread(image1_path)
        image2 = cv2.imread(image2_path)
        image1, image2 = self.resize_to_smallest(image1, image2)

        marked_image = image1.copy()

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(marked_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1.5
        font_color = (0, 255, 0)
        font_thickness = 1

        cv2.putText(
            image1,
            "Expected Image",
            (10, image1.shape[0] - 10),
            font,
            font_scale,
            font_color,
            font_thickness,
            cv2.LINE_AA,
        )

        cv2.putText(
            image2,
            "Actual Image",
            (10, image2.shape[0] - 10),
            font,
            font_scale,
            font_color,
            font_thickness,
            cv2.LINE_AA,
        )

        cv2.putText(
            marked_image,
            "Diff Image",
            (10, marked_image.shape[0] - 10),
            font,
            font_scale,
            font_color,
            font_thickness,
            cv2.LINE_AA,
        )

        border_color = (0, 0, 0)
        border_thickness = 5

        image1_with_border = cv2.copyMakeBorder(
            image1,
            border_thickness,
            0,
            border_thickness,
            0,
            cv2.BORDER_CONSTANT,
            value=border_color,
        )
        image2_with_border = cv2.copyMakeBorder(
            image2,
            border_thickness,
            0,
            border_thickness,
            0,
            cv2.BORDER_CONSTANT,
            value=border_color,
        )
        marked_image_with_border = cv2.copyMakeBorder(
            marked_image,
            border_thickness,
            0,
            border_thickness,
            0,
            cv2.BORDER_CONSTANT,
            value=border_color,
        )

        combined = cv2.vconcat(
            [image1_with_border, image2_with_border, marked_image_with_border]
        )

        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

        cv2.imwrite(diff_path, combined)

        return score, diff_path

    def assert_images(self, image1_path, image2_path, diff_filename="diff.png"):
        score, diff_path = self.save_diff_image_with_boxes(image1_path, image2_path, diff_filename)
        print(f"SSIM between {image1_path} and {image2_path}: {score:.4f}")
        print(f"Diff image saved at: {diff_path}")
        assert score >= self.threshold, f"Images '{image1_path}' and '{image2_path}' are not similar enough (SSIM: {score:.4f}, threshold: {self.threshold})."
