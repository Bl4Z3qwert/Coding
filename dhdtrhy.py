# import array as arr
# array_num = arr.array('i',[  2,3,1,5,4,7,6,8,4,2,1,3 ])
# print('Original array: ' + str(array_num))
# print('Number of occurances of repited numbers: ' + str(array_num))
# array_num.reverse()
# print('Reverse order of numbers')
# print(str(array_num))

# class Computer:
#     def __init__(self):
#         self.__maxprice=900
#     def sell(self):
#         print('The price of this computer is {}'.format(self.__maxprice))
#     def setmaxprice(self,price):
#         self.__maxprice=price
        
        
        
        
        
        
                
# c= Computer()
# c.sell()
# c.__maxprice=1000
# c.sell()
# c.setmaxprice(15000)
# c.sell        

class square:
    def __init__(self,side):
        self.side=side
        
    def area(self):
        print('the area of square is ', self.side **2)
        
class circle:
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        print('The area of a circle is', self.radius**2)  
        
Square= square(50)   
Circle= circle(30)     
# Square.area()
# Circle.area() 

for shape in(Square,Circle):
    shape.area()
    
    


from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        print('This is the parent class of animals') 
        
        
class human(Animal):
    def move(self):
        print('I can talk and walk on two legs')     


class snake(Animal):
    def move():
        print('I can slither')
        
        
r= human()
r.move()        

              
            
        
        