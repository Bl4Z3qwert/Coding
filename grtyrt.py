class Reverser:
    def reverse_words(self, sentence):
        return ' '.join(sentence.split()[::-1])

text = Reverser()
print(text.reverse_words("hello world this is cool"))





class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

class Bus(Vehicle):
    def fare(self):
        return self.seating_capacity * 100  # Assume 100 per seat

my_bus = Bus(50)
print("Total Bus Fare:", my_bus.fare())





