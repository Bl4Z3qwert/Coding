def student(name):
    print("my name is ", name)
student('horla')

def is_synonym(letterd):
    letterd = letterd.replace(" ","")
    return letterd==letterd[::-1]
    
word='dad'
print(is_synonym(word))

def fruit(type):
    print("this fruit is", type)
fruit('ripe')