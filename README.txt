Implementation of YOLO v3 from scratch using Pytorch

Directory Structure
	-	---- config	(contains configuration of YOLO v3).
			
		---- utils	(contains utils for training of object detector from scratch).
			|
			|----- cfg_to_dict.py 		(this script is used to converet all config to a neural network).
			|----- create_modules.py 	(this script is used to create PyTorch modules from the cfg list).
			|----- nn_utils.py 		(this script contains helper class from the PyTorch nn module).
			|----- load_weights.py 		(this script is used to load weights to the Yolo v3 model).
			|----- darknet.py 		(this is actual script which is used to to create a model from the cfg file).
			

	