from transformers import pipeline
from PIL import Image

print("Loading SafeVersion AI...")

classifier = pipeline(
    "image-classification",
    model="Falconsai/nsfw_image_detection"
)

print("AI loaded!")

image_path = input("Enter image path: ")

image = Image.open(image_path)

results = classifier(image)

print("\nSafeVersion Analysis")
print("--------------------")

for result in results:
    label = result["label"]
    score = result["score"] * 100

    print(f"{label}: {score:.2f}%")

# SafeVersion decision
nsfw_score = 0

for result in results:
    if result["label"].lower() == "nsfw":
        nsfw_score = result["score"] * 100

print("\n========================")
print("     SAFEVERSION")
print("========================")

if nsfw_score >= 70:
    print("🔴 UNSAFE CONTENT")
    print(f"Confidence: {nsfw_score:.2f}%")
    print("Action: BLOCK")
else:
    print("🟢 SAFE CONTENT")
    print(f"Confidence: {100 - nsfw_score:.2f}%")
    print("Action: ALLOW")