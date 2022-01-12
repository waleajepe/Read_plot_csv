""" 
A module that reads a csv file and plotting a pie chart using a csv, matplotlib and np module
"""
from matplotlib import pyplot as plt
import numpy as np
import csv

# Using the "with" keyword as it closes the file after reading through the data
with open("random_nums.csv", "r") as file:
    reader = csv.reader(file)
    reading = list(reader)

integer_list = []
for list_value in reading[1:]:
    for value in list_value:
        integer_list.append(int(value))

data = np.array(integer_list)
fig = plt.figure(figsize=(10, 7))
plt.pie(x=data)
plt.show()
