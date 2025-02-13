import cv2
import os
import requests
from ultralytics import YOLO
from .util import get_car

class Detector:
    def __init__(self):
        # Ensure models directory exists
        models_dir = os.path.join(os.path.dirname(__file__), '../models')
        os.makedirs(models_dir, exist_ok=True)

        # Paths to model files
        self.yolo_model_path = os.path.join(models_dir, 'yolov8n.pt')
        self.license_plate_model_path = os.path.join(models_dir, 'license_plate_detector.pt')

        # Download license_plate_detector.pt if not present
        if not os.path.exists(self.license_plate_model_path):
            print("Downloading license_plate_detector.pt...")
            url = "https://github.com/mahdihuseine/object.detector/raw/main/object/detector/models/license_plate_detector.pt"
            response = requests.get(url)
            if response.status_code == 200:
                with open(self.license_plate_model_path, 'wb') as f:
                    f.write(response.content)
                print("Downloaded license_plate_detector.pt successfully.")
            else:
                raise Exception("Failed to download license_plate_detector.pt")

        self.coco_model = YOLO(self.yolo_model_path)
        self.license_plate_detector = YOLO(self.license_plate_model_path)

    def detect(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Invalid image path provided.")
        
        vehicles = [2, 3, 5, 7]
        results_vehicle = self.coco_model(image)[0]
        
        vehicle_detections = [detection[:5] for detection in results_vehicle.boxes.data.tolist() if int(detection[5]) in vehicles]
        results_lp = self.license_plate_detector(image)[0]

        plate_detections = []
        for detection in results_lp.boxes.data.tolist():
            plate_detections.append(detection[:4])

        return vehicle_detections, plate_detections
