
import time
#Performing Operations
def operations(number_1,number_2,operation):
    if operation == 1:
        return number_1 + number_2
    elif operation == 2:
        return number_1 - number_2
    elif operation == 3:
        return number_1 * number_2
    elif operation == 4:
        try:
           return number_1 / number_2
        except ZeroDivisionError:
            return "Error!Division by Zero"
    elif operation == 5:
        return number_1**number_2

print("Welcome To Mini Calculator !".center(100))   

while True:
    
    #Entering input values 
    try:
        number_1=float(input("\nEnter the first number: "))
        number_2=float(input("Enter the second number: "))
    #Handling value errors
    except ValueError:
        print("Error!!Enter the numeric values")
        continue
 
#Displaying the list of operations
    while True:
        print("\nList of Operations\n",
    "1.Addition\n",
    "2.Subtraction\n",
    "3.Multiplication\n",
    "4.Division\n",
    "5.Power")
   
        try:
            operation = int(input("Enter Your Choice (1/2/3/4/5) "))
            if operation not in (1, 2, 3, 4, 5):
                print("Invalid choice. Please select a valid operation.")
                continue
        except ValueError:
            print("Error!!Enter a choice")
            continue
        time.sleep(0.5)
        break
    

    result=operations(number_1,number_2,operation)
    print(f"Result is {result}")
    repeat=input("\nWould you like to perform another operation?(Yes/No) ").strip().lower()
    if repeat=="no":
        print("\nThank you for using Mini Calculator")
        break



    


    



    
