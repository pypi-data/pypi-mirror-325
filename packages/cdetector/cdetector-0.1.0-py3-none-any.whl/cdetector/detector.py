import cv2
import os
from ultralytics import YOLO
from .util import get_car

class Detector:
    def __init__(self):
        self.coco_model = YOLO(os.path.join(os.path.dirname(__file__), '../models/yolov8n.pt'))
        self.license_plate_detector = YOLO(os.path.join(os.path.dirname(__file__), '../models/license_plate_detector.pt'))

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
