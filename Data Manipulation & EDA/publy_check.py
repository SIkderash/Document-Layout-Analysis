import os
from ultralytics import YOLO
import wandb



wandb.init(mode="disabled")
model = YOLO("/media/abhijit/New Volume/dls2/code/runs/segment/train34/weights/publy.pt")

print(help(model))