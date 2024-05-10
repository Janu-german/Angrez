#how to convert column data into list for regression analysis
#https://www.geeksforgeeks.org/python-read-csv-columns-into-list/
from pandas import *
import pandas as pd   #loading data
import seaborn as sns  #data Analysis
import matplotlib.pyplot as plt
import numpy as num
from scipy import stats

# reading CSV file
data = read_csv("Exercise.csv")
# # converting column data to list
# Age = data['Age'].tolist()
# print(Age)
#================================+++++++++++++============================++++++++++++++++




# X = num.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)

# print(X)

#====================================================================================================
#take data from csv file column print it ,1)its in column form , 2)then it to list and 3)then convert that list to column form
Agecolumn =data['Age']
print(Agecolumn)
# Agecolumntolist =data['Age'].tolist()
#print(Agecolumntolist)
# Agecolumntolisttocolumn = num.array([Agecolumntolist]).reshape(-1,1)
# print(Agecolumntolisttocolumn)
#conclusion , some how i sucessfully did this above exercise but i am still unaware of usage & difference of above.

