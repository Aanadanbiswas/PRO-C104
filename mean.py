import csv

with open(r'details.csv',newline='') as f:
    data_reader = csv.reader(f)
    AllData = list(data_reader)

AllData.pop(0)

weight_data = []

for i in range(len(AllData)):
    Weight_Value = AllData[i][2]
    weight_data.append(float(Weight_Value))

total = 0

for x in weight_data:
    total += x

n = len(weight_data)

mean = total/n

print('Mean of the weight is: ',mean)