from transformers import pipeline
from PIL import Image

print("Loading SafeVersion AI...")

classifier = pipeline(
    "image-classification",
    model="Falconsai/nsfw_image_detection"
)

print("AI loaded!")


def detect_image(image_path):
    """
    Analyze an image and return SafeVersion result.
    """

    image = Image.open(image_path)

    results = classifier(image)

    nsfw_score = 0

    for result in results:
        label = result["label"]
        score = result["score"] * 100

        print(f"{label}: {score:.2f}%")

        if label.lower() == "nsfw":
            nsfw_score = score

    if nsfw_score >= 70:
        return {
            "status": "UNSAFE CONTENT",
            "confidence": nsfw_score,
            "action": "BLOCK"
        }

    else:
        return {
            "status": "SAFE CONTENT",
            "confidence": 100 - nsfw_score,
            "action": "ALLOW"
        }