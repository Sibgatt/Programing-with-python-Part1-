n1 = int(input('n1 = '))
n2 = int(input('n2 = '))
n3 = int(input('n3 = '))

if n1>n2:
    max_n=n1
else:
    max_n = n2
if max_n < n3 :
    max_n = n3

print(max_n)