
import os
import csv
import pandas as pd
import math

label_path = os.path.join(os.getcwd(), 'labels')

print(label_path)

final_list=[]
data_list = []

for file in os.listdir(label_path):
    
    file_new = file
    data_list=[]
    if file.endswith(".txt") and file!="classes.txt":
        filename = os.path.join(label_path, file)
        # print(filename)
        with open(filename, 'r') as file:
                line = file.readline()
                line_new = line.split(' ')
                print(file_new)
                data_list.append(file_new)
                data_list.append(int(line_new[0]))
                data_list.append(float(line_new[3]))
                data_list.append(float(line_new[4]))
                data_list.append(float(line_new[3])*float(line_new[4]))
                data_list.append(math.hypot(float(line_new[3]), float(line_new[4])))
                # print(filename)
                # print(data_list)
                final_list.append(data_list)

with open('output.csv', mode='w', newline='') as csv_file:

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Filename', 'Class', 'Width', 'Length', 'Area', 'diagonal'])
    csv_writer.writerows(final_list)

print("Done")

df = pd.read_csv('output.csv')

value_map = {15: 'drone', 16: 'aeroplane', 17: 'bird', 18:'kite'}

df['Class'] = df['Class'].map(value_map)
df.to_csv('output.csv', index=False)
print("Done with csv")
