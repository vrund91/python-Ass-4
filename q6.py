'''Write a Python program that demonstrate the use of finally and else clause in exception. '''

try:
    numerator=float(input("Enter the numerator:"))
    denominator=float(input("Enter the Denominator:"))
    result = numerator / denominator
except ZeroDivisionError:
    print("Can't Devide by zero.")
except ValueError:
    print("please enter valid numeric value")
else:
    print("The result is:",numerator/denominator)
finally:
    print("Execution of the division operation is complete")