'''
    This class contains helper classes for intializing object detection model.

'''

import torch
import torch.nn as nn



''''
    This is just a empty class used for for Shortcut & Route layers from YOLO v3 config.
    This is used to create a empty nn layer
'''

class EmptyLayer(nn.Module):

    def __init__(self):
        super(EmptyLayer, self).__init__()







''''
    This is used to create a detection layer class.
'''

class DetectionLayer(nn.Module):

    def __init__(self, anchors):
        super(DetectionLayer, self).__init__()
        self.anchors = anchors