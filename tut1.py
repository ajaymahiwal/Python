print("Hello World !")

value = input("enter something you want to :")
print(value)
print(type(value)) # str

# python only have reference types, not any kind of primitives data types
# so when you write num = 50 then a object is created in which 50 is stored and that variable is pointing to that reference address, not storing that value 50 inside itself alike java and c++ etc

intValue = 10
floatValue = 34.3
stringValue = "ajay mahiwal"
booleanValue = True
Age = None


# Operators

print(10+10)
print(2**5)

print(True and False)
print(True or False)
print(not True)

# type casting 

num = float("10.5")


# String (immutable)

name = "ajaymahiwal"
print(name)
print(len(name)) # 11

# string slicing
print(name[0:]) # ajaymahiwal
print(name[:5]) # ajaym
print(name[3:5])# ym
print(name[-len(name):-3]) # ajaymahi
print(name[-3]) # w

# print(name[2:len(name):0]) //error slice step cannot be zero
print(name[2:len(name):2]) # amhwl

# name[0] = 'A'     #error : 'str' object does not support item assignment
print(name)

# List (mutable)

classmates = ["sonu","pankaj","rahul","yuvraj"]
sonu = ["from Haryana",21,8.8,+910000000000]
print(sonu)

randomData = ["hello","india","coding",5000000,"fa",5,7,8.2,"okay","hii"]

print(randomData[2:5]) #['from Haryana', 21, 8.8, 910000000000]
print(randomData[-2]) #okay
print(randomData[-2:]) #['okay', 'hii']

# randomData[10] = "last" # error: list assignment index out of range

print(randomData)


# Tuple (immutable)

data0 = ("ajay") # str  <class 'str'>
data1 = () #empty tuple hai ye   <class 'tuple'>
data = ("ajay",) #tuple <class 'tuple'>

print(type(data0))
print(type(data1))


tupData = ("ajay",4.5)

print(tupData[0]) 

# tupData[0] = "fsadfhj" # TypeError: 'tuple' object does not support item assignment

print(tupData)