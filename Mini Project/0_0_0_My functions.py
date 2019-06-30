import random
import numpy as np


#check duplicates in a list and remove them from it
def check_duplicates (list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return (new_list)