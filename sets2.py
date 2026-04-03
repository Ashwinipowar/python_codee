 # sets in python ,ore or less work in the same way as sets in math. 
# we can perform operation like union and intersection on the sets just in math.


# union and updates 
# the union and update methon prints all the items that are present in the two sets .
# the union method returns a new set whereas update method  add item into the existing set feom another set


#intersection 
# the intersection means that the value which in the both sets



cities1= {"tokiyo", "madrid", "berlin", "delhi"}
cities2 = {"tokiyo", "seoul", "kabul", "madrid"}
cities3 = cities1.union(cities2)
print(cities3)

cities4 =cities1.intersection(cities2)
cities5 =cities1.update(cities2)
#cities will be update ....add the items in thecities which are preset in the cities 


cities6 =cities1.intersection_update(cities2)
#update the first one set 


#symmetry difference and symmetry difference update
cities7=cities1.symmetric_difference(cities2)