'''Write a Python program that will demonstrate the use of raise keyword.'''

def dem():
    while True:
        try:
            age=int(input("Enter a age:"))
            if age >= 18:
                print(f"{age} you are eligible for voting.")
                return age
            else:
                raise ValueError("You are not eligible for voting.")
                
        except ValueError as e:
            print(e)

a = dem()
print(a)