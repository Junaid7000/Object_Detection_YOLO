''''
    This script is used to Darknet model form the config file.
'''


import torch
import torch.nn



''''
    This class is used to initialize model from the cfg file 
    & create a modules list which finally builds a yolo architecture.

    Input:  
            cfg_file(string)        : location of cfg file.

    Output:
            detection (torch.tensor): ooutput from the YOLOv3  
'''

class Darknet(nn.modules):

    def __init__(self, cfg_file):
        super(Darknet, self).__init__()

        self.blocks = cfg_to_dict(cfg_file)
        self.net_info, self.module_list = create_module(self.blocks)


    def  forward(self, img):

        #write logic for forward pass.

        pass

    
    #used to load weights form given location.
    def load_weights(self, weights_file):

        pass

        










































if __name__ == '__main__':
    from cfg_to_dict import cfg_to_dict
    from create_modules import create_module
    
else:
    from utils.cfg_to_dict import cfg_to_dict
    from create_modules import create_module
    