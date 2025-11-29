# Python Program to create a simple calculator


# 3 step to build calculator program
# 1. Functions for operation
# 2. User input
# 3. Print result

# step 1: Create Function 
# Function to add two numbers
def add(num1,num2):
    return num1 + num2

# Function to Substract two numbers
def sub(num1,num2):
    return num1 - num2

# Function to Multiplication two numbers
def mul(num1,num2):
    return num1 * num2

# Function to Divide two numbers
def div(num1,num2):
    return num1 / num2

# Function to Average two numbers
def Avg(num1,num2):
    return (num1 + num2)/2

# Step 2: User Input

print("Please slect a operation:\n " \
     "1. Addition\n" \
        "2. Substraction\n" \
            "3. Multiply\n" \
                "4. Divide\n" \
                    "5. Average\n")

select = int(input("Select a operation from 1,2,3,4,5: "))

number1= int(input("Enter First Number: "))
number2= int(input("Enter Second Number: "))

# Step 3: Print the result
if select == 1:
    print(number1, "+" , number2, "=", \
        add(number1,number2))

elif select == 2:
    print(number1, "-" , number2, "=", \
        sub(number1,number2))

elif select == 3:
    print(number1, "*" , number2, "=", \
        mul(number1,number2))

elif select == 4:
    print(number1, "/" , number2, "=", \
        div(number1,number2))

elif select == 5:
    print("(", number1, "+" , numrber2,")","/2", "=", \
        Avg (number1,number2))

else:
    ("Invalid operation please select again!")
