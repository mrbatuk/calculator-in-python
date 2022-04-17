#added to return to start in case of error.
while True:
    #We asked the user to enter a number.
    first_number=int(input("First Number: "))   
    second_number=int(input("Second Number: "))
    
    #We asked the user to enter an operator
    operator=input("Operator (+,-,/,*,**): ")
    result=1
    result2=0
    #check is the operator is correct or not
    if operator == "+" or operator == "-"or operator =="*" or operator =="/" or operator =="**" :
        if operator == "+":
            result=first_number+second_number
            print(result)
        elif operator =="-":
            result=first_number-second_number
            print(result)
        elif operator =="*":
            for x in range(0, second_number):
                result2=first_number+result2
            print(result2)
        elif operator =="**":
            for x in range(0, second_number, 1):
                result=first_number*result
            print(result)
        else:
            result=first_number/second_number
        

        
    #error in choosing wrong operator
    else:
        print("Operator is wrong! Please try again")
    


