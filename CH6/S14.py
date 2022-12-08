#when you use a while loop you need to use a spacific argument ..
i = 0
while i < 5 :
    print(i)
    i += 1

print("____")
#you can als use while loop to print numbers backwords..

_ = 5
while _ >= 0:
    _ -=1
    print(_) #the loop will print -1 though you spacified the argument to print untill the numbers are equal to 0.actually for the (>=) sign , the loop goes on cause it thinks that there must be more numbers that will come in this condition and when it finds -1 it doesnt find any more condition to work with and stops