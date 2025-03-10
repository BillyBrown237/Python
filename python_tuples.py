# used to store different data strucutres
# can also be defines without the parentheses

my_tuple = (1 , "strings" , 4.5, True)
print(my_tuple[1])
print(my_tuple.count('strings')) # returns a number of times an element appears in a tuple
print(my_tuple.index(4.5)) # returns the index of the element in the tuple
 
 # looping through a tuple
for x in my_tuple:
    print(x)
# tuple values are immutable , they cannot be changed

# my_tuple[5] = 1 returns an exception