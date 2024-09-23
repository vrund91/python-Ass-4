'''Write a Python program that will ask the user to input 2 integer values, if user enter second 
value as zero than it generates the appropriate exception and display the message.'''

def display():
    while True:
      try:
          a=int(input("Enter a numerator:"))
          b=int(input("Enter a denominator:"))

          if b == 0:
            raise ZeroDivisionError("Error:The denominator cannot be zero")
        
          else:
            result=a/b
            print("The result is: ",result)
            return result

      except Exception as e:
       print(e)

Result=display()
print(Result)
    
        