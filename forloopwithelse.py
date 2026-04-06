for i in range (5):
    print(i)

else:
    print("sorry no i")

#it goes zero to 4 nad then it stop bcz of hving n-1

#here it goes to the end nad then goes to the else statment 
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
else:
    print("Loop completed without break.")


#when the break statment applied this loop stop there
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
    if num == 3:
        break
else:
    print("Loop completed without break.")


#example
i=0
while i<7:
    print(i)
    i=i+1

else:
    print("sorry no i")

for x in range(5):
    print("iteration no {}in loop ")

else :
    print("else block in loop")
print("out of loop")
