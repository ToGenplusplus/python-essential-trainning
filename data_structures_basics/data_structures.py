# list methods
print("list actions\n")
my_list = []
my_list.append(1) # adds to the list
print(my_list)
my_list.insert(0,33) # inserts element at specified index
print(my_list)
my_list.insert(0,22)
print(my_list)
copy_of_my_list = my_list.copy() #returns a shallow copy of list
print(copy_of_my_list)
print(my_list.count(1)) #returns the number of occurenes of the value passed in
my_list.extend([9,8,7,8,9]) # adds all elements of an iterable to the end of the list
print(my_list)
my_list.remove(8)   # removes the first matching element based on the argument passed in from the list
print(my_list)
item_at_index_2 = my_list.pop(2) # removes and returns the item and the specified index
print(my_list)
print(item_at_index_2)
my_list.clear() # removes all elements in list
print(my_list)



print("set actions\n")
# set methods
my_set = {1, 2, 3}
my_set.add(4) #adds an element to the set
print(my_set)
value = my_set.pop() # removes and returns a random element from the set
print(value)
my_set.update([5,6,7]) # update the set with the union of itself and the elements passed in
print(my_set)
my_set.discard(3) # removes an element from a set if the element exists
print(my_set)
intersect = my_set.intersection({7,8,9}) # returns the elements that are shared by both sets
print(intersect)
my_set.difference({2, 3, 4}) # returns the elements in my_set that are not in the iterable passed in
print(my_set)

print("tuple actions\n")
# tuple methods 
my_tuple = (1,2,3)
print(my_tuple.index(3)) # returns the first position in the tuple of the value 

print("dict actions\n")
#dict methods
my_dict = {'hello' : 'world', 'boolean': True}
print(my_dict.get('hello', 'default world')) # returns the value for key if present else default value passed in 
new_dict = my_dict.fromkeys(['first', 'second', 'third'], False)
print(new_dict)
print(my_dict.items()) # returns a set like object containing the dictionarys items

# shared methods between the above data structures
# .index() # returns the index of the specified element in the structure (list, tuple)