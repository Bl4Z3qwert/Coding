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

class Tesla:
    def fuel_type(self):
        return "Tesla uses electricity"

    def max_speed(self):
        return "Tesla's max speed is 220 km/h"

# Polymorphism in action
def vehicle_details(vehicle):
    print(vehicle.fuel_type())
    print(vehicle.max_speed())
    print("--------")

# Testing all vehicles
for car in [BMW(), Ferrari(), Tesla()]:
    vehicle_details(car)
