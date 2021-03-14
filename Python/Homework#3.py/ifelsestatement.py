# This is my third homework

'''The current work is 
about if statment used in a functions'''


# My first Function

def passMark(Tutorial, Test, Exam):
    if (Tutorial >= 17 and Test >= 15 and Exam >= 15):
        passExam = "Excellent ! You Passed !!!"
    
    elif(Tutorial <= 15 and Test > 15 and Exam > 15):
        passExam = "Good! You Passed !!!"

    else:
        passExam = "Ops, You Failled !!!"
    
    return passExam

Result = passMark(12, 17, 16)
print(Result)



