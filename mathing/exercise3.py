# Devision function

def devision(x,y):
    if x <= 0:
        return 0
    elif y <= 0:
        return 0
    else:
        devide = x/y;
        return devide;

num1 = int(input("Enter the first Number :"))
num2 = int(input("Enter the second Number :"))

result = devision(num1,num2)

print (result)

