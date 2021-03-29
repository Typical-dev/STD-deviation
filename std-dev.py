import csv
with open("class1.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data.pop(0)

def mean(data1):
    total_marks = 0
    total_entries = len(data1)
    for marks in data1:
        total_marks += float(marks[1])
    mean = total_marks/total_entries
    return(mean)


squared_list = []
mean_data = mean(data)
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)
sum = 0
for i in squared_list:
    sum = sum + i
result = sum/(len(data) - 1)
STD = math.sqrt(result)
print(STD)