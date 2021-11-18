import csv

with open(r'details.csv',newline='') as f:
    data_reader = csv.reader(f)
    AllData = list(data_reader)

AllData.pop(0)

weight_data = []

for i in range(len(AllData)):
    weight_value = AllData[i][2]
    weight_data.append(weight_value)

weight_data.sort()

n = len(weight_data)

if n % 2==0:
    median_1 = float(weight_data[n//2])
    median_2 = float(weight_data[n//2-1])
    median = (median_1 + median_2)/2

else:
    median = float(weight_data[n//2])

print('The median of weight is: ',median)