#Steps
"""
Takes in an excel file
Creates a dataframe
Pivots on certain row names and column names and values.
  Can choose which aggregate function to be applied(sum/len/mean etc) from numpy
intersection of data frames
union of dataframes
difference between dataframes
"""
import pandas as pd
import numpy as np


data=pd.read_excel('C:\\Users\\karthik\\Desktop\\Data Science\\sample.xlsx')

data2=data[['Org Theater','Project Number','Hours Entered','Product Family']] #Applyingng the filter externally for pivotting the dataframes


pdata=pd.pivot_table(data2,index=['Org Theater','Product Family'],values=['Hours Entered'],aggfunc={'Hours Entered':np.sum})


print(pdata)
first=data2[:40]    #0 to 40 rows

second=data2[15:45]  #15 to 45 rows

def intersect(a,b):
    intersection=pd.merge(a,b,how='inner') #Intersection of two dataframes

def union(a,b)
union=pd.merge(first,second,how='outer') #Union of two differenct dataframes

diff=first[~first.isin(second).all(1)] #Difference between two dataframes

print(diff)

