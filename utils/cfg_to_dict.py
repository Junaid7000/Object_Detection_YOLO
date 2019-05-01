''''
    Author: 
    
    Date:

    Project: Object detection using py-Torch.
    
    This file is used to read ./config/yolov3.cfg to a and then convert this config file to dictionary.

    Dictionary should contain key as a type of fuction and value as value.

    e.g.  {'layer': 'convolutional', 'batch_normalize': '1', 'filters': '32', 'size': '3', 'stride': '1', 'pad': '1', 'activation': 'leaky'}

    Then append this dictonary to a list.
    
''' 


''''
    This funtion should convert config file to dictionary

    Input:  cfg_file (string):      Address of the config file.
    Output: config_list(list):      list containing configurations.
''' 

def cfg_to_dict(cfg_file):

    pass