# Here I am going to compare integer variable value to string variable value

def myFunction(myInteger, myString):
    myString = int(myString)
    if myInteger > myString:
        Result = True

    elif myInteger < myString:
        Result = False

    else:
        Result = "Bothe are equals"

    return Result
    
myResult = myFunction(12, '15')

print(myResult)
        