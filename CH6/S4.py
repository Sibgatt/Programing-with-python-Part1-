#you can sum 1 to 50 all together by this line of code
reasult = 0
num = 1

for _ in range(50):
    reasult = reasult + num
    num = num + 1


print(reasult)


#you can also put num on range to sum one after another digit upto 50
reasult = 0

for num in range(51):  # starting from 0 num will continue adding 1 on every step
    reasult = reasult + num


print(reasult)


#you can also put the whole loop argument on one single condition
reasult = 0

for num in range(51):
    reasult += num

print(reasult)