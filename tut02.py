
# function defination
def sum(a,b):
    return a + b

# function calling
print(sum(10,20))




"""
Loops two types :
- while
- for

Other important things:
1. break 
2. continue
3. pass (use when you want to left anything bodyless, means if python you can't left left empty loops, conditionals, function etc. so to make things empty and no error come for that use pass keyword. In is because of indentation)
"""

number = 0
while number <= 10 :
    print(number,end=", ")
    number+=1

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
print()

for el in range(3,5) :
    print(el, end=", ")

# 3, 4, 
print()

print(list(range(1,50,2)))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]