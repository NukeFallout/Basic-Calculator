#this is the code for a basic calculator
#ask user for their 1st and 2nd  number

num1 = float(input("Enter a number: "))
num2 = float(input('Enter another number: '))

operator = input("Enter the operator you would like to use: * , / , + or - : ")

if operator == "*":
    mul = num1 * num2
    print(f"{num1} * {num2} = {mul}")
elif operator == "/":
    div = num1 / num2
    print(f"{num1} / {num2} = {div}")
elif operator == "+":
    add = num1 + num2
    print(f"{num1} + {num2} = {add}")
elif operator == "-":
    sub = num1 - num2
    print(f"{num1} - {num2} = {sub}")
else:
    print("Invalid Operator")

   


       

    

