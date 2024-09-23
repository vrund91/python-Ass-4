'''Write a Python program that will ask the user to input positive numeric number and if user 
inputs any other data then it generates appropriate exception and message.'''

def appropriate():
    while True:
        try:
            number=float(input("Enter positive number:"))
            if number <= 0:
                raise ValueError("The number must be positive")
            return number
        
        except ValueError as e:
            print(e)

a = appropriate()
print(a)