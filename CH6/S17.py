terminate = False
while True:
    num1 = int(input('Please enter a number :'))
    num2 = int(input('Please enter a number :'))

    while True :
        operation = input("Please enter sub/add or quit to exit :")
        if operation == 'quit':
            break
        if operation == "add":
            print("Reasult is :",num1+num2)
        if operation == 'sub':
            print("Reasult is :",num1-num2)
        if operation not in ['add','sub']:
            print('Unknown operation..')
            break
    break