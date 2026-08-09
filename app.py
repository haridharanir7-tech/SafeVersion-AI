from flask import Flask, render_template, request,jsonify
from ai.content_dectector import detect_image
import os

app = Flask(__name__)

UPLOAD_FOLDER = "ai/test_images"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "No image selected"}), 400

    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(image_path)

    result = detect_image(image_path)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)