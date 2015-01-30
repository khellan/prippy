import os
import string

from os import path
from sys import argv

BLUE_IDX  = 0
GREEN_IDX = 1
RED_IDX   = 2
THRESHOLD = 1.5

if __name__ == "__main__":
    src_dir = argv[1]
    for filename in os.listdir(src_dir):
        basename = path.splitext(path.basename(filename))[0]
        with open(src_dir + '/' + filename, 'r') as file:
            values = string.split(file.read(), ',')
            if int(values[BLUE_IDX]) > THRESHOLD * int(values[GREEN_IDX]) and int(values[BLUE_IDX]) > THRESHOLD * int(values[RED_IDX]):
                color = 'blue'
            elif int(values[GREEN_IDX]) > THRESHOLD * int(values[BLUE_IDX]) and int(values[GREEN_IDX]) > THRESHOLD * int(values[RED_IDX]):
                color = 'green'
            elif int(values[RED_IDX]) > THRESHOLD * int(values[BLUE_IDX]) and int(values[RED_IDX]) > THRESHOLD * int(values[GREEN_IDX]):
                color = 'red'
            else:
                color = 'none'
            print basename + ',' + color
