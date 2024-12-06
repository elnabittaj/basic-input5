def gcd(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return gcd(num2,num1%num2)
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
custom=gcd(num1,num2)
print(custom)