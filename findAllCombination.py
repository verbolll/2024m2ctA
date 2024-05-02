from itertools import product
import numpy as np

def find_all(B, C, D, E, F, G):
    name = str(len(B) + 1) + '.csv'
    nametime = str(len(B) + 1) + 'time.csv'
    A = [100.767, 164.229, 214.85, 270.065]
    all_combinations = list(product(B, C, D, E, F, G))

    with open(name, 'w', encoding='utf-8') as fp:
        for combination in all_combinations:
            templist = list(combination)
            templist.insert(0, A[-len(B)])
            np_list = np.array(templist)
            templist = (np_list*0.34).tolist()
            templist.insert(0, None)
            fp.write(str(templist))
            fp.write('\n')

    with open(nametime, 'w', encoding='utf-8') as fp:
        for combination in all_combinations:
            templist = list(combination)
            templist.insert(0, A[-len(B)])
            np_list = np.array(templist)
            templist = (np_list).tolist()
            templist.insert(0, None)
            fp.write(str(templist))
            fp.write('\n')
    return name