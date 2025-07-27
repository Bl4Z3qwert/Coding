import pandas as pd
myDataset={
    'cars':['Bmw', 'Audi', 'Mercedes'],
    'passings':[4, 5, 4],
}
myvar=pd.DataFrame(myDataset)
print(myvar)



b=[2, 4, 6, 8,]
var=pd.Series(b)
print(var)

vr=pd.Series(b, index=['x', 'y', 'z', 'w'])
print(vr)




calories = {'day1': 420, 'day2': 380, 'day3': 390}
dat=pd.Series(calories)
print(dat)
data={
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}
data=pd.DataFrame(data,index= ['day1', 'day2', 'day3'])
print(data)
df=pd.read_csv