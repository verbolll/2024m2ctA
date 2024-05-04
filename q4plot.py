# q4plot.py
# 添加随机误差后坐标与时间分布
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pltN(file, colname, boomname, step):
    temp = 0
    name = ['x', 'y', 'z', 't']
    col = name.index(colname)
    for i in [col]:
        df = pd.read_csv(file)
        if name[col] == 't':
            y_values = df.iloc[:, i] / (-0.34)
        else:
            y_values = df.iloc[:, i] 
        y_values_sorted = y_values.sort_values()
        min_value = y_values_sorted.min()
        interval_counts = {}
        for value in y_values_sorted:
            interval = int((value - min_value) / step)
            if interval not in interval_counts:
                interval_counts[interval] = 1
            else:
                interval_counts[interval] += 1
        interval_starts = []
        interval_ends = []
        counts = []
        for interval, count in interval_counts.items():
            interval_start = min_value + interval * step
            interval_end = interval_start + step
            interval_starts.append(interval_start)
            interval_ends.append(interval_end)
            counts.append(count)
        plt.bar(interval_starts, counts, width=step, align='edge', edgecolor='red')
        plt.xlabel(name[col])
        plt.title(boomname)
        plt.show()
        temp = temp + 1