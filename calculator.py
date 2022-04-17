#added to function
def addiction(x,y):
    result=x+y
    print(result)
    
def extraction(x,y):
    result=x-y
    print(result)
    
def multiplication(x,y):
    result=0
    for i in range(0, y):
        #print(x)
        result=x+result
    print(result)
    
def division(x,y):
    result=x/y
    print(result)
    
def power(x,y):
    result=1
    for i in range(0, y, 1):
        result=x*result
    print(result)

#added to return to start in case of error.
while True:
    #We asked the user to enter a number.
    first_number=int(input("First Number: "))   
    second_number=int(input("Second Number: "))
    
    #We asked the user to enter an operator
    operator=input("Operator (+,-,/,*,**): ")


    #check is the operator is correct or not
    if operator == "+" or operator == "-"or operator =="*" or operator =="/" or operator =="**" :
        if operator == "+":
            addiction(first_number,second_number)
        elif operator =="-":
            extraction(first_number,second_number)
        elif operator =="*":
            multiplication(first_number,second_number)
        elif operator =="**":
            power(first_number,second_number)
        else:
            division(first_number,second_number)
    #error in choosing wrong operator
    else:
        print("Operator is wrong! Please try again")
    


