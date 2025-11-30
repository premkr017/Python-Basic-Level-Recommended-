a=1
b=2
c=a+b
print(c)
print("Hello, World!")
for i in range(5):
    print(i)
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
if c > 2:
    print("c is greater than 2")
while a < 5:
    print(a)
    a += 1
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
import math
print(math.sqrt(16))
with open("output.txt", "w") as f:
    f.write("This is a test file.\n")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
person = Person("Ritik Kumar", 20)
print(person.introduce())