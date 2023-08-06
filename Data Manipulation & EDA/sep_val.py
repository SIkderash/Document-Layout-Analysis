import os
from rotate import change_label, rotate_image
import cv2
import random
from tqdm import tqdm

TRAIN_IMG_DIR = 'datasets/badlad/heq/images/train'
TRAIN_LABEL_DIR = 'datasets/badlad/heq/labels/train'
VAL_IMG_DIR = 'datasets/badlad/heq/images/val'
VAL_LABEL_DIR = 'datasets/badlad/heq/labels/val'


for imgname in tqdm(os.listdir(TRAIN_IMG_DIR)):
    labname = imgname[:-4]+'.txt'
    r = random.randint(0, 99)
    if r<20:
        os.rename(os.path.join(TRAIN_IMG_DIR, imgname), os.path.join(VAL_IMG_DIR, imgname))
        os.rename(os.path.join(TRAIN_LABEL_DIR, labname), os.path.join(VAL_LABEL_DIR, labname))