cities1= {"tokiyo", "madrid", "berlin", "delhi"}
cities2 = {"tokiyo", "seoul", "kabul", "madrid"}


cities3 = cities1.union(cities2)
print(cities3) # combination of both


cities4 =cities1.intersection(cities2)
cities5 =cities1.update(cities2)# add the values which are preesent in the set2 in set1





cities6 =cities1.intersection_update(cities2) 
print(cities6)
#intersection_update() in Python
#The intersection_update() method in Python is used with sets to update the original set by 
# keeping only the elements that are common (intersection) between the original set and one or more specified sets

#Key Differences from intersection()
#intersection() returns a new set without modifying the original set.
#intersection_update() modifies the original set in place.

#When to Use intersection_update()?
#When you want to update a set without creating a new set.
#When working with large sets, since it is more memory-efficient than intersection()
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set1.intersection_update(set2)
print(set1)  # Output: {3, 4, 5}




set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {4, 5, 6, 7, 8}

set1.intersection_update(set2, set3)
print(set1)  # Output: {4, 5}




# In Python, intersection refers to finding common elements between two or more sets.
#  It is commonly used with sets to return elements that exist in all given sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1 & set2
print(result)  # Output: {3, 4}




set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.intersection(set2)
print(result)  # Output: {3, 4}





cities7=cities1.symmetric_difference(cities2) # common hai vo nikal dete hai aur jo uncommon hai vo print hoga
print(cities7)
# wo sari values jo common nahi hai
#The symmetric difference between two sets returns elements that are
#  in either of the sets but not in both. In other words, it removes common elements and keeps only the unique ones.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 2, 5, 6}





#disjoint set meaning is that no comman element there
#The isdisjoint() method checks whether two sets have no common elements.
#It returns True if the sets have no elements in common.
#It returns False if there is at least one common element

#agar ik bhi common hoga to vo false print karega
#aur no common then true will be print 
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.isdisjoint(set2))  # Output: False




#issuperset
#issuperset() in Python
# The issuperset() method checks if a set contains all elements of another set.
# It returns True if the first set includes all elements of the second set.
# It returns False otherwise
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}
print(set1.issuperset(set2))  # Output: True


set1 = {1, 2, 3, 4, 5}
set2 = {2, 6}
print(set1.issuperset(set2))  # Output: False
# even if only one is not present in the base set then it will not the superset of another


set1 = {1, 2, 3}
set2 = set()  # Empty set
print(set1.issuperset(set2))  # Output: True
# rare case

#issubset just opposite like the issuperset
set1 = {2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # Output: True

set1 = {2, 6}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # Output: False

set1 = set()  # Empty set
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True

#add
#only add one item
set = {1, 2, 3, 4, 5}
set.add("ash")
print(set)

#update ----when you want to add more than one
set2 = {1, 2, 3, 4, 5}
sets = {1, 2, 3}
set2.update(sets)
print(set2)
# it update but value wont repeat


set2 = {1, 2, 3, 4, 5}
sets = {6,77,88}
set2.update(sets)
print(set2)
# here values are getting update

#remove 
name={"ash", "siya", "toto","nande"}
name.remove("nande")
print(name)

# name={"ash", "siya", "toto","nande"}
# name.remove("seojun")
# print(name)


#here gives the error if there is not having
# this value but in the discard doesnt give error
#means the if the iteam is does not have in set and we still wabts to remove
#then remove will give you the error 
# but the discard is not show the eror


#discard
name={"ash", "siya", "toto","nande"}
name.discard("seojun")
print(name)

#what if when we wannas to delete the entire items of the set
# but not the set only items
#hoiw????????????????
#we use the clear method
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

