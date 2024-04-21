def sum(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b) :
    return a * b

def division(a,b) :
    return a / b





# main

print("calculator application.")

print("Which Operation You Want To Do:")
print("Enter 1 for Sum")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")

response = int(input("Enter Your Response: "))

first = float(input("Enter First Number: "))
second = float(input("Enter Second Number: "))

if response == 1 :
    print(f"result : {sum(first,second)}")
elif response == 2 :
    print(f"result : {subtraction(first,second)}")
elif response == 3 :
    print(f"result : {multiplication(first,second)}")
elif response == 4 :
    print(f"result : {division(first,second)}")
else :
    print(f"You entered {response}, which is not vaild response.")






