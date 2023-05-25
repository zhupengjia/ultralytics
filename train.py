#!/usr/bin/env python3

from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n-pose.yaml")  # build a new model from scratch
model = YOLO("yolov8n-pose.pt")

import ipdb
ipdb.set_trace()

# Use the model
model.train(data="coco8-pose.yaml", epochs=3)  # train the model