class student:
    grade =6
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def details(self):
        print(f'my name is {self.name} im {self.age} im in grade {self.grade} ')
obj = student('ken', 13)
obj2 = student('der', 12) 
obj.details()
obj2.details()           
    
    
