def func1():
     try:
        l =[1,5,6,7 ]
        i=int (input ("enter the index:"))
        print(l[i]) 
        return 1   
     except:
         print ("some erroe occured")
         return 0
     

     finally :
         print("i am always executed")
# print("i am always executed")# if only this will be there then even if the error is occured there will not having the print statment

x= func1()
print(x)
      

      # the meaning of finally is that it execute always
#       The finally block in Python is used to ensure that certain code runs 
#       no matter what—even if something goes wrong (an error happens) or everything works fine.

#      try:
#     # Code that might cause an error
# except:
#     # Code that runs if there's an error
# finally:
#     # Code that always runs



# 🔹 Why use it?
# Because sometimes you need to clean up, like:

# Closing a file

# Disconnecting from a database

# Releasing memory or resources

# Logging out a user

# Stopping a program safely






# example




# try:
#     file = open("data.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("The file was not found.")
# finally:
#     file.close()
#     print("File is closed.")
