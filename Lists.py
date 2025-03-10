list1 = [1,2,3,4,5]

list2 = ['A','B','C','D','E']

list3 = ['Hello', 1 , True , 40.22]

list4 = [1, [2,3,4],5]

### to print an entire list
print(*list1)
### to print values separated by something
print(*list1, sep=",")
### to add an element
#using insert takes the element to insert and the index where to insert
list1.insert(len(list1),6)
print(list1)
#using append
list1.append(7)
print(list1)
#using extend
list1.extend([8,9,10])
print(list1)

### to remove from the list
#using pop , speicify the index 
list1.pop(4)
print(list1)
#using del keyword also takes index
del list1[4]
print(list1)


### iteration through a list

for x in list1:
    print(x)