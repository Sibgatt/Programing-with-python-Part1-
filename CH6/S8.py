#You can print the numbers from 1 to 100 which are -- by 5 and also find their sum
reasult = 0 
for num in range(100):
    if num %5 ==0:
        print(num)
        reasult += num

print("Sum is" , reasult)# it will show 950 as answer but the right answer is 1050 . actually you used 100 as range so the loop isn't reading 100 as a number here ..so you can use 101 as range to solve the problem



#you can also write the code more easier way
reasult = 0
for num in range(5,101,5):
    print(num)
    reasult += num

print("Sum is", reasult)