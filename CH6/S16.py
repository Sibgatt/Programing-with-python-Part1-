# You can use break to get out of a loop..
while True:
    n=int(input("Please enter the number(0 to exit) :"))
    if n==0:
        break

    print('Square of',n,'is',n*n)





# you can also use this program on even and odd numbers ...
while True:
    n = int(input("Please enter a positive number(0 to exit) :"))
    if n < 0:
        print('We only allow positive number . Please try again.')
        continue
    if n == 0:
        break
    print('Square of',n,'is',n*n)