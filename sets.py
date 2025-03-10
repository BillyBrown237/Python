set_a ={1 , 2, 3, 4 , 5} # sets don't allow duplicate values
print(set_a) 

set_a.add(6) # adds the value 6 to the set

set_a.remove(2) # remove the number 2 from the set , 

set_a.discard(2) #dicards the number 2 from the set

set_b = {4,5,6,7,8}

# math operators in sets

set_a.union(set_b) # joins the two sets a and b minus the duplicate values
set_a | set_b # does the same thing as using .union

set_a.intersection(set_b) # produces the elements similar to set a and b
set_a & set_b # does the same thing as .intersection

set_a.difference(set_b) # produces all the elements only in "a" and not "b" can also be represented using the "-" symbol

set_a.symmetric_difference(set_b) # produces all the elements present in set a or b but not in both sets , can also be represented using the "^" symbol

#attempting to print an indexed element from a set produces an error because sets are not ordered