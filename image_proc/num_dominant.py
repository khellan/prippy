import os
import string

from os import path
from sys import argv

BLACK_IDX  = 0
BLUE_IDX   = 1
LIME_IDX   = 2
BROWN_IDX  = 3
RED_IDX    = 4
PURPLE_IDX = 5
ORANGE_IDX = 6
YELLOW_IDX = 7
GREY_IDX   = 8
PINK_IDX   = 9
WHITE_IDX  = 10

THRESHOLD = 1.5

if __name__ == "__main__":
    src_dir = argv[1]
    for filename in os.listdir(src_dir):
        basename = path.splitext(path.basename(filename))[0]
        with open(src_dir + '/' + filename, 'r') as file:
            line = file.read()
            #print basename + ">" + line
            values = [int(v) for v in string.split(line, ',')]
            max_value = max(values)
            threshold = max_value / THRESHOLD
            print basename + ',', sum([1 for x in values if x > threshold])
