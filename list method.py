l = [11,45,1,2,4,6,1,1]
print(l)

l.append(7) # it add
print(l)

l.sort()# assending order
print(l)

l.sort(reverse=True) # reversred assending order
print(l)

l.reverse() # reverse make it
print(l)

print(l.index(1))# show the index number of thar perticular member

print(l.count(1)) # how many 1 are  present in the list

m= l.copy()
m[0]=0
print(m) # it will place in the position of the 0th index

# but we use the insert 
l.insert(1, 899)
print(l) # at the position of the 1 we insert the 899 

# when we wanna concatinate we use two ways
m=[1,222,333,444,555]
l.extend(m)
print(l) # it will add at the end or extended


# and the second way is that make a diff list
k= l+m
print(k) # for the need to give #to the 30 and 31 line number

