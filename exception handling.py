# ashwini
# if you give the space before the print statment of these tlast two lines 
# then you will get ghe one by one number nad print statment inthe outp






#  a= input("Enter the number :")
# print(f"multiplication table of {a} is: ")

# for i in range (1,11):
#     print(f"{int(a)} x {i} = {int(a)*i}")

# print("some imp lines of code")
# print("end of the code")




#ECXEPTION HANDLING
# a= input("Enter the number :")
# print(f"multiplication table of {a} is: ")
 
# try:
#   for i in range (1,11):
#     print(f"{int(a)} x {i} = {int(a)*i}")

# except:

#      print("exception type of error occures")

# print("some imp lines of code")
# print("end of the code")


# this output we get-------Enter the number :ashwini
# multiplication table of ashwini is: 
# exception type of error occures
# some imp lines of code
# end of the code


# In Python, an exception is an error that occurs during the execution of a program.
# When Python encounters an error, it raises an exception,
# which can interrupt the normal flow of the program.


# Exception Name	Description
# ZeroDivisionError	---Raised when a number is divided by zero.
# TypeError	----Raised when an operation is applied to an object of inappropriate type.
# ValueError---	Raised when a function receives the correct type but inappropriate value.
# IndexError----	Raised when a list index is out of range.
# KeyError	-----Raised when a dictionary key is not found.
# FileNotFoundError	--Raised when a file or directory is requested but doesn't exist.
# ImportError	---Raised when an imported module cannot be found.


try:
   num= int(input("enter an integer"))
   a=[6,3]
   print(a[num])
except ValueError:
   print("number entered is not an integer")

except IndexError:
   print("index error")

