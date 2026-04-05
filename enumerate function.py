marks = [12, 34, 56, 78, 98, 54, 545]


# index = 0 
# for mark in marks:
#     print(mark)
# if (index ==3 ):
#     print("harry , awsome!")
# index =+ 1


for index , mark in enumerate (marks, start=2): # it starts the indexing from the 2 position by the using if the enumerate
    print(mark)
    if (index == 3):
        print("harry, awesome")




# In Python, enumerate() is a built-in function used to loop over 
# something while keeping track of the index (position) of the current item
#syntax
# enumerate(iterable, start=0)
# iterable: any iterable object like a list, tuple, string, etc.

# start: the index you want to start counting from (default is 0)


# without enumerate

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 cherry


# with enumwrate

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# 1 apple
# 2 banana
# 3 cherry
