import numpy as np
import q4findLocal
import q4plot

boom1 = np.array([100.767, 112.22, 188.02, 258.985, 118.443, 266.871, 163.024])
boom2 = np.array([164.229, 169.362, 156.936, 141.409, 86.216, 166.27, 103.738])
boom3 = np.array([214.85, 92.453, 75.56, 196.517, 78.6, 175.482, 210.306])
boom4 = np.array([270.065, 196.583, 110.696, 94.653, 126.669, 67.274, 206.789])

X = [None, 0, 52.73877, 50.69538, 0.97304, 27.53703, 21.9907, -18.87698]
Y = [None, 0, 28.03828, 64.6438, 91.34692, 45.95162, 97.57765, 35.27037]
Z = [None, 0.824, 0.727, 0.742, 0.85, 0.786, 0.678, 0.575]

mean = 0
std_dev = 0.5

def boomAddError(boomName, csvname):
    for i in range(1000):
        error = np.random.normal(mean, std_dev, size=len(boomName))
        boom_with_error = boom1 + error
        boom_with_error = (boom_with_error*0.34).tolist()
        boom_with_error.insert(0, None)
        filename = csvname + '.csv'
        q4findLocal.find_local(X, Y, Z, L=boom_with_error, filename=filename, ifprint=False)
    return filename
q4plot.pltN(boomAddError(boom1, 'boom1'), 'x', 'boom1', 0.05)
