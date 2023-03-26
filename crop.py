import os
import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np


import subprocess
import sys
import time
from PIL import Image



def crop():
    img = Image.open("image.jpg") #process the image 
    
    if img.height > 300 or img.width > 300: #get the height and width of the image
        output_size = (900, 900) #crop the image to the output size
        img.thumbnail(output_size) 
        ext = ['.jpeg', '.png', '.jpg'] #create list of extensions to save as 
        for extension in ext: #loop over the list 
            img.save(f"image_resize{extension}")

crop()
