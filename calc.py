def addition(a,b):
    return(a+b)

def subtract(a,b):
    return a-b

def multiply(a,b):
    return(a*b)

def divide(a,b):
    if a==0 and b==0 :
        raise ValueError("undefined")
    elif b==0:
        raise ValueError("we cannot divide")
    return a/b
#a=int(input("Enetr a:"))
#b=int(input("enter b:"))
#addition(a,b)
#subtract(a,b)
#multiply(a,b)
#divide(a,b)
