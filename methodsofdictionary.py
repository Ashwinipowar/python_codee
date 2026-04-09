#METHODS OF DICTIONARY
# 1.update
# 2.clear
# 3.pop 
# 4.popitem
# 5.del


ep1 ={122:45, 123:54, 243:56, 456:65}
ep2 ={222:67 , 566:90}
 
# ep1.update(ep2)# fill the all values in the ep1
# print(ep1)

# ep1.clear()
# print(ep1)#only {} will be there not having the error


# ep1.remove()# it shows then error
# print(ep1)

# ep1.pop(122)#only that key value pair will delet
# print(ep1)

# ep1.popitem() # last key value pair will delet
# print(ep1)

# empt={}
# print(empt)

del ep1[243]
print(ep1)# only deleted the 243 key value pair