class Dog:
    species = "Canis Familiaris"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Beagle")
dog2 = Dog("Max", "Labrador")

for dog in [dog1, dog2]:
    print(f"{dog.name} is a {dog.breed} of species {Dog.species}")
