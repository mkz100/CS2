# Python module to execute
# import file_two
from file_two import function_three # to use a function from another module, it need to be explicitly imported

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
   function_three()
else:
   print("File one executed when imported")