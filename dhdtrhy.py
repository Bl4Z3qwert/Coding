# import array as arr
# array_num = arr.array('i',[  2,3,1,5,4,7,6,8,4,2,1,3 ])
# print('Original array: ' + str(array_num))
# print('Number of occurances of repited numbers: ' + str(array_num))
# array_num.reverse()
# print('Reverse order of numbers')
# print(str(array_num))

class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print('The price of this computer is {}'.format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice=price
        
        
        
        
        
        
                
c= Computer()
c.sell()
c.__maxprice=1000
c.sell()
c.setmaxprice(15000)
c.sell        