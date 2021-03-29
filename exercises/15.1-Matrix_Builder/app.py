#Import random
import random

#Create the function below:
list1 = []
list2 = []
def matrixBuilder(item):
    for i in range(0,item,1):
        list1.append(1)
    for j in range(0,item,1):
        list2.append(list1)
    print(list2)
matrixBuilder(2)

