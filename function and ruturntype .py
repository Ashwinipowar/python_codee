marks= [3,5,6,"sara", True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])


# print(marks[-3]) # negative indexing
# print(marks[len(marks)-3])# positive indexing
# print(marks[5-3])# positive index
# print(marks[-3])

# if "sara" in marks:
#     print("yes")
# else:
#     print("no")

# here is we have the sara as sting in the marks but
# let we see 6 number as string whta give the ans


# if "6" in marks:
#     print("yes")
# else:
#     print("no")


# same thing appies for the string
# if "sa" in "sara":
#       print("yes")
# else:
#     print("no")

# slicing
# print(marks)
# print(marks[1:-1])
# print(marks[1:4])



# jump index
# marks1 = [2,4,5,6,7,8,"sara","diya",34,55,] # for the defining the marks needs give some place before and after of the =
# print(marks1)
# print(marks1[1:8])
# print(marks1[1:8:2]) # here it will perform the jump operation



# # negative indexing 
# print(marks1[-8:-1:2])
# print(marks1[10-8:10-1:2]) # converted into the positive indexing by total number of member present(without indexing number) minus of negative indexing



# list comprehension
# lst = [i*i for i in range (4)]
# print(lst)


lst = [i*i for i in range (10)]
print(lst)
lst=[i*i for i  in range (10) if i%2==0]
print(lst)
