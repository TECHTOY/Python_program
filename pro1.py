#!/usr/bin/python3
a = 10
b = 2.10
c = a%b

print("c")
print("Hello Python", c)
print(type(c))

# Data Types: int, float, string, boolean, long, complex etc.
# 
x = 3
z = 3+4j
print(x + z)
print(f"Values are {x} {z}")

my_name = 'Python'
print(my_name,type(my_name))

my_value = True
my_value_1 = False

print(my_value, my_value_1)

# TYPE CASTING & CONVERSION
# Any data type can be converted into boolean.
# bool(any_data_type)= True or False
# x="2.1.3.5" (string)

x = 25
print(x,type(x))
y=str(x)
print(y,type(y))
z=bool(x)
print(z,type(z))

#============================================================#

#Simple addition cal
v =eval(input("Enter a value: "))
u =eval(input("Enter a value: "))
result= v + u
print(f"The addition of {v} and {u} is: {result}")
print(type(result))




