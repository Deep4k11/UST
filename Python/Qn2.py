lim = int(input("Enter the limit"))
n1, n2 = 0,1
next_num=0
print('Fibonacci Sequence btwn 1 to 20')
while next_num < lim:

    print(n2)
    next_num = n1 + n2

     #update values
    n1 = n2
    n2 = next_num
