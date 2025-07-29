import math

def trig_values(angle):
    radians = math.radians(angle)
    return {
        "sin": round(math.sin(radians), 2),
        "cos": round(math.cos(radians), 2),
        "tan": round(math.tan(radians), 2)
    }

angle = float(input("Enter angle in degrees: "))
values = trig_values(angle)
print("sin:", values["sin"])
print("cos:", values["cos"])
print("tan:", values["tan"])
