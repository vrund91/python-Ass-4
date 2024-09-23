'''Write a Python program that will ask the user to input age of a person and generates an 
exception if user enters non-numeric data and display the proper message'''

def display():
    try:
        age=int(input("Enter your age:"))
        print("your age is:",age)
        return age
    
    except ValueError:
        print("Error:please enter a valid numeric age.")

result=display()
print("your age is:",result)