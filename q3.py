'''Write a Python program that will ask the user to input one integer value and if user inputs 
non-numeric data than it generates Value Error and display proper message till user inputs 
numeric data.'''

def display():
    while True:
       try:
        a=int(input("Enter a number:"))
        print("You enterd value:",a)
        return a
       
       except ValueError:
          print("Error:please enter numeric data")

result=display()
print(result)