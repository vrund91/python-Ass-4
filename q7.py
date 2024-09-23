'''Write a Python program that asks the user to input a number and if number is negative 
generates a value error. '''

try:
    number=float(input("Enter a number:"))
    if number <= 0:
        raise ValueError("The number cann't be negative")
    print("you entered a valid number:",number)

except ValueError as e:
    print(e)