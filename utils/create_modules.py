''''
    This sscript will convert dictionary from cfg_to_dict.py to a PyTorch module for the blocks represented
    in yolov3.cfg file.

    Use nn.Sequential to create a sequential model from the given config_list.

'''

import torch
import torch.nn as nn

#use nn_utils.py for helper functions.

''''
    This function will take config_list as a input convert those list to a sequential.

    Input:  config_list (list) : list cotaining all config
    Output: 
            module_list(nn.Modulelist)  : list containing list of all PyTorch module.
            net_info(list)     : list containing information of all modules
            
'''

def create_module(config_list):


    pass
























if __name__ == '__main__':
    from cfg_to_dict import cfg_to_dict
    from nn_utils import EmptyLayer, DetectionLayer

else:
    from utils.cfg_to_dict import cfg_to_dict
    from utils.nn_utils import EmptyLayer, DetectionLayer