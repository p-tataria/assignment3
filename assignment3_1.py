def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

a=(int(input("Enter a non negative number:")))
if a < 0:
    print("Not valid")
else:
    print("The factorial of",a,"is:",factorial(a))
    
