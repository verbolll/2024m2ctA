# afterFindAandC.py
# 找出所有时间组合的误差后选出误差最小的组合
import csv

def findAandC(filename):
    with open(filename, 'r', encoding='gb2312') as file:
        csv_reader = csv.reader(file)
        
        min_value = float('inf')
        min_row = None
        
        for row in csv_reader:
            value = float(row[2])
            
            if value < min_value:
                min_value = value
                min_row = row

    final = min_row[-1]
    final = final.replace("[", "")
    final = final.replace("]", "")
    data = [x for x in final.split(' ') if x != '']
    print(data)

    if min_row:
        print("最小值:", min_value)
        print("最优解:", min_row[-1])
        print('经度' + str(float(data[0]) / 97.304 + 110.241))
        print('纬度' + str(float(data[1]) / 111.263 + 27.204))
        print('高度' + str(float(data[2])))
        print('时间' + str(float(data[3]) / 0.34))
    else:
        print("未找到最小值")
    return min_row[0]