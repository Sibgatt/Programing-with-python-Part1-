#you can find the largest number in a list using for loop
numbers = [6,1,0,3,9,2,5,8]
max_n = numbers[0]
for n in numbers:# the condition is in numbers list as for its used in for loop
    if n > max_n:
        max_n = n

print(max_n)