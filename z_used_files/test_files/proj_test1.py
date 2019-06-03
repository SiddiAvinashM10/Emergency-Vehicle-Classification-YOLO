import sys
import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt

#%config InlineBackend.figure_format = 'svg'
#%%
options  = {
        'model': 'cfg/yolo.cfg',
        'load':'bin/yolo.weights',
        'threshold' : 0.3,
        'gpu' : 1.0
        }

tfnet = TFNet(options)