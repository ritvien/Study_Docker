from flask import Flask, request, jsonify
from ultralytics import YOLO
import torch

app = Flask(__name__)

# Load YOLOv8 model
model = YOLO("models/yolov8n.pt")  

@app.route("/")
def home():
    return "Hello, YOLO!"

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    image = request.files["image"]
    results = model(image)

    detections = []
    for result in results:
        for box in result.boxes:
            detections.append({
                "class": int(box.cls),
                "confidence": float(box.conf),
                "bbox": box.xyxy.tolist()[0]
            })
    
    return jsonify({"detections": detections})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
