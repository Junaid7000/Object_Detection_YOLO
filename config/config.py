def parse_cfg(cfgfile):

    """

    Takes a configuration file

    

    Returns a list of blocks. Each blocks describes a block in the neural

    network to be built. Block is represented as a dictionary in the list

    

    """

    file = open(cfgfile, 'r')

    lines = file.read().split('\n')     #store the lines in a list

    lines = [x for x in lines if len(x) > 0] #get read of the empty lines 

    lines = [x for x in lines if x[0] != '#']  

    lines = [x.rstrip().lstrip() for x in lines]



    

    block = {}

    blocks = []

    

    for line in lines:

        if line[0] == "[":               #This marks the start of a new block

            if len(block) != 0:

                blocks.append(block)

                block = {}

            block["type"] = line[1:-1].rstrip()

        else:

            key,value = line.split("=")

            block[key.rstrip()] = value.lstrip()

    blocks.append(block)
    
    print(blocks)
    print('\n\n'.join([repr(x) for x in blocks]))





if __name__ == "__main__":
    parse_cfg("./yolov3.cfg")