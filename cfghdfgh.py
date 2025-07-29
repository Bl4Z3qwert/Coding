class BMW:
    def fuel_type(self):
        return "BMW uses petrol"

    def max_speed(self):
        return "BMW's max speed is 250 km/h"

class Ferrari:
    def fuel_type(self):
        return "Ferrari uses high-octane petrol"

    def max_speed(self):
        return "Ferrari's max speed is 330 km/h"

# Polymorphism in action
def vehicle_details(vehicle):
    print(vehicle.fuel_type())
    print(vehicle.max_speed())
    print("--------")

# Creating objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Passing different objects to the same function
vehicle_details(bmw_car)
vehicle_details(ferrari_car)
