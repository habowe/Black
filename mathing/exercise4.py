# Fabanacci 

def fibanacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x > 2:
        return fibanacci(x-1) + fibanacci(x-2)
    
x = int(input("Enter Number to check :"))

#result = fibanacci(num,  bool(num))

#print (result)

for x in range(1,11):
     if (fibanacci(x) == True):
        print (x , "is a Fibonacci Number ")
     else:
        print (x , "is a not Fibonacci Number ")

    

