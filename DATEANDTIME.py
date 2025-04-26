import datetime
import calendar
import random
import time
x=datetime.datetime.now()
print(x)
yy=2000
mon=4
print(calendar.month(yy,mon))
def getrandomdate(startdate,enddate):
    print('Printing random between ' ,startdate , 'and' , enddate)
    randomGenarator = random.random()
    dateFormart= '%m/%d/%Y'
    startTime= time.mktime(time.strptime(startdate,dateFormart))
    endTime= time.mktime(time.strptime(startdate,dateFormart))
    randomTime=startTime  +randomGenarator*(endTime-startTime)
    randomdate=time.strftime(dateFormart,time.localtime(randomTime))
    return randomdate
print('random Date =', getrandomdate ('4/26/2024' , '4/26/2025'))


months = list(calendar.month_name)
for month in months:
    print(month)