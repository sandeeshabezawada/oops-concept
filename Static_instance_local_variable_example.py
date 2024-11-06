#static variable example
'''class Lego:
    #
    width = 5  # static variable
    height = 5  # static variable

    def __init__(self, length, colour):
        self.length = length  # instance variable
        self.colour = colour
        print('Block of ' + colour + ' colour is manufactured.')


block1 = Lego(10, 'Red')
block2 = Lego(5, 'Blue')'''

#instance variables exampleclass
'''class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create first object
s1 = Student("sandy", 32)

# access instance variable
print('Object 1')
print('Name:', s1.name)
print('Age:', s1.age)

# create second object
s2= Student("siva", 42)

# access instance variable
print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)'''

#local variable example
class local:
    def my_function(self):
        x=10
        y=20 # Local variable
        return x+y

obj=local()
print(obj.my_function())
