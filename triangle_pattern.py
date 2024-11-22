
row=int(input("Enter number of rows:"))
for i in range(row):
    for j in range (i+1):
        print("*",end=" ")
    print("")

row=int(input("enter number of rows:"))
for i in range (row):
    for j in range (row-i):
         print("*",end=" ")
    print("")
row=int(input("Enter number of rows:"))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print("")

row=int(input("Enter number of rows:"))
for i in range(row, 0,-1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print("")

