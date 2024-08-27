"WAP to find the greatest of 3 numbers entered by the user."

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

if(a>b and a>c):
    print(a,"is greater than",b,"and",c)
elif(b>a and b>c):
    print(b,"is greater than",a,"and",c)
else:
    print(c,"is greater than",a,"and",b)