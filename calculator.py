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
            result=first_number+second_number
        elif operator =="-":
            result=first_number-second_number
        elif operator =="*":
            result=first_number*second_number
        elif operator =="**":
            result=first_number**second_number
        else:
            result=first_number/second_number
        
        print(result)
        
    #error in choosing wrong operator
    else:
        print("Operator is wrong! Please try again")
    


