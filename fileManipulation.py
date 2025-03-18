import pandas as pd

myDataSet = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

myVar = pd.DataFrame(myDataSet)

myDataSet2 = {
    "cars": ["Toyota", "Honda", "Nissan"],
    "passings": [4, 6, 3]
}
myVar2 = pd.DataFrame(myDataSet2)
#Concat the two dataframes
myVar3 = pd.concat([myVar, myVar2], ignore_index=True)
print(myVar3)

myDataSet3 = {
    "rating": [4, 5, 6]
}
myVar4 = pd.DataFrame(myDataSet3)

#Concat the two dataframes
myVar5 = pd.concat([myVar3, myVar4], axis=1)    
print(myVar5)