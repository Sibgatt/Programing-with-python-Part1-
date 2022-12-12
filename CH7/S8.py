#you can also put a list lin a functiom.
def add_numbers(numbers):
    result=0
    for number in numbers:
        result += number
    return result

a = add_numbers([1,2,30,4,5,9])
print(a)