import torch
from PIL import Image
from transformers import OwlViTProcessor, OwlViTForObjectDetection
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class OWLVit:
    """
    OWL-ViT object detection model with default queries including COCO classes.
    """

    def __init__(self, queries=None):
        """
        Initialize the OWL-ViT model with default or user-provided queries.

        Args:
            queries (list, optional): List of object queries (e.g., ["a cat", "a dog"]).
                                       If None, defaults to COCO classes as queries.
        """
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = OwlViTForObjectDetection.from_pretrained(
            "google/owlvit-base-patch32"
        ).to(self.device)
        self.processor = OwlViTProcessor.from_pretrained("google/owlvit-base-patch32")

        # Default COCO class queries
        self.coco_classes = [
            "a person",
            "a bicycle",
            "a car",
            "a motorcycle",
            "an airplane",
            "a bus",
            "a train",
            "a truck",
            "a boat",
            "a traffic light",
            "a fire hydrant",
            "a stop sign",
            "a parking meter",
            "a bench",
            "a bird",
            "a cat",
            "a dog",
            "a horse",
            "a sheep",
            "a cow",
            "an elephant",
            "a bear",
            "a zebra",
            "a giraffe",
            "a backpack",
            "an umbrella",
            "a handbag",
            "a tie",
            "a suitcase",
            "a frisbee",
            "skis",
            "a snowboard",
            "a sports ball",
            "a kite",
            "a baseball bat",
            "a baseball glove",
            "a skateboard",
            "a surfboard",
            "a tennis racket",
            "a bottle",
            "a wine glass",
            "a cup",
            "a fork",
            "a knife",
            "a spoon",
            "a bowl",
            "a banana",
            "an apple",
            "a sandwich",
            "an orange",
            "broccoli",
            "a carrot",
            "a hot dog",
            "a pizza",
            "a donut",
            "a cake",
            "a chair",
            "a couch",
            "a potted plant",
            "a bed",
            "a dining table",
            "a toilet",
            "a TV",
            "a laptop",
            "a mouse",
            "a remote",
            "a keyboard",
            "a cell phone",
            "a microwave",
            "an oven",
            "a toaster",
            "a sink",
            "a refrigerator",
            "a book",
            "a clock",
            "a vase",
            "a scissors",
            "a teddy bear",
            "a hair drier",
            "a toothbrush",
        ]

        # Use default COCO classes unless custom queries are provided
        self.queries = queries if queries else self.coco_classes

    def detect_objects(self, image_path):
        """
        Detect objects in an image using default or custom queries.

        Args:
            image_path (str): Path to the input image.

        Returns:
            dict: A dictionary containing the input image, bounding boxes, scores, and labels.
        """
        # Load and preprocess the image
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(
            images=image, text=self.queries, return_tensors="pt"
        ).to(self.device)

        # Perform inference
        with torch.no_grad():
            outputs = self.model(**inputs)

        # Post-process outputs
        target_sizes = torch.tensor([image.size[::-1]]).to(self.device)
        results = self.processor.post_process_object_detection(
            outputs=outputs, threshold=0.1, target_sizes=target_sizes
        )[0]

        # Prepare packed results
        packed_results = {
            "image": image,
            "boxes": results["boxes"].cpu().tolist(),  # Convert to list
            "scores": results["scores"].cpu().tolist(),  # Convert to list
            "labels": [self.queries[label] for label in results["labels"].cpu().tolist()],
        }

        return packed_results


    def visualize_results(self, packed_results):
        """
        Visualize detected objects in an image.

        Args:
            packed_results (dict): Packed results containing the image, bounding boxes, scores, and labels.
        """
        image = packed_results["image"]
        boxes = packed_results["boxes"]
        scores = packed_results["scores"]
        labels = packed_results["labels"]

        plt.figure(figsize=(10, 10))
        plt.imshow(image)
        ax = plt.gca()

        for box, score, label in zip(boxes, scores, labels):
            xmin, ymin, xmax, ymax = [round(coord, 2) for coord in box]

            # Draw bounding box
            rect = patches.Rectangle(
                (xmin, ymin),
                xmax - xmin,
                ymax - ymin,
                linewidth=2,
                edgecolor="red",
                facecolor="none",
            )
            ax.add_patch(rect)

            # Draw label and confidence score
            ax.text(
                xmin,
                ymin - 5,
                f"{label}: {score:.2f}",
                fontsize=12,
                color="white",
                bbox=dict(facecolor="red", alpha=0.5, edgecolor="none"),
            )

        plt.axis("off")
        plt.show()
