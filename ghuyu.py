class Vechile:
    def __init__(self,name,max_speed):
        self.name=name
        self.mileage=max_speed
        
    def  car_mileage(self):
        print(f'the car name is {self.name} and it has a mileage of {self.mileage}')
        
        
class Bus(Vechile):
    def __init__(self,color, name, max_speed):
        self.color=color  
        super().__init__(name,max_speed)   
school_bus=Bus('blue','street Volvo', 12)
school_bus.car_mileage(nujh)            
    