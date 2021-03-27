import os
import sys
import subprocess
import cv2
import numpy as np

from color_grey_conversion import color_to_grey
from test import run

IMG_FOLDER = os.path.join(os.path.dirname(__file__), "dataset/val_img")
INST_FOLDER = os.path.join(os.path.dirname(__file__), "dataset/val_inst")
LABEL_FOLDER = os.path.join(os.path.dirname(__file__), "dataset/val_label")

def copy_file(old="avon.png", new="avon.png"):
    command_string = "cp " + old + " " + new
    subprocess.check_output(command_string.split(" "))


def genInstanceAndLabelMap(greyscale_fname, color_file):
    # label folder
    label_map_file = LABEL_FOLDER + "/" + greyscale_fname
    color_to_grey.convert_rgb_image_to_greyscale(color_file, label_map_file)

    instance_map_file = INST_FOLDER + "/" + greyscale_fname
    copy_file(label_map_file, instance_map_file)

    image_file = IMG_FOLDER + "/" + greyscale_fname
    copy_file(label_map_file, image_file)
    

if __name__ == "__main__":
    color_in_loc  = 'img' + "/" + "color.png"
    img_color_in = cv2.imread(color_in_loc)
    img_color_in = cv2.resize(img_color_in, dsize=(256,256))

    greyscale_fname = "greyscale.png"

    genInstanceAndLabelMap(greyscale_fname, color_in_loc)

    # TODO: we should create a new API to have greyscale_fname as input and
    # now input of run() is implicitly stored in greyscale_fname folders.
    synthesized_img_loc = run()

    img_synthesized = cv2.imread(synthesized_img_loc)

    stack_horizontal = np.hstack((img_color_in, img_synthesized))
    cv2.imshow('result', stack_horizontal)
    cv2.waitKey(0)