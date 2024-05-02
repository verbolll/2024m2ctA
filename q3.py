import findAllCombination
import findLocal
import afterFindAandC
import csv
from itertools import islice

B = [92.453, 112.22, 169.362, 196.583]
C = [75.560, 110.696, 156.936, 188.02]
D = [94.653, 141.409, 196.517,258.985]
E = [78.600, 86.216, 118.443, 126.669]
F = [67.274, 166.270, 175.482, 266.871]
G = [103.738, 163.024, 206.789, 210.306]

X = [None, 0, 52.73877, 50.69538, 0.97304, 27.53703, 21.9907, -18.87698]
Y = [None, 0, 28.03828, 64.6438, 91.34692, 45.95162, 97.57765, 35.27037]
Z = [None, 0.824, 0.727, 0.742, 0.85, 0.786, 0.678, 0.575]

for i in range(3):
    name = findAllCombination.find_all(B, C, D, E, F, G)
    findLocal.find_local(X, Y, Z, file=name, x0=[0, 0, 13, 0], ifprint=False)
    line = afterFindAandC.findAandC('localData.csv')
    with open(str(len(B) + 1) + 'time.csv', 'r', encoding='utf-8') as file:
        mycsv = csv.reader(file)
        for i, row in enumerate(mycsv):
            if i == int(line):
                tagrow = row
                break
        tagrow = [(s.strip("[] '")) for s in tagrow if s.strip("[] '")]
        tagrow.pop(0)
        tagrow = [float(num) for num in tagrow]
        tagrow.pop(0)
        file.close()
    for i in range(len([B, C, D, E, F, G])):
        [B, C, D, E, F, G][i].remove(tagrow[i])