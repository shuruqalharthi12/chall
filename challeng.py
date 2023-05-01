n=int(input("enter number of lines:"))
for i in range (0,n):
    for j in range (0,i+1):
        print('* ', end="")
    print ()
for i in range (n,-1,-1):
    for j in range (0,i+1):
        print('* ', end="")
    print ()