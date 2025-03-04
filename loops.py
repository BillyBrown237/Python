import time
# for loop and while loop

# str = 'Looping'

# for item in str:
#     print(item)

# testing the for loop
# everything you need to loop towards an n number better to use range
favorite_fruits = ['apple', 'banana', 'orange', 'grape', 'mango']

# for fruit in range(10):
#     print("Looping...",fruit)

# for fruit in favorite_fruits:
#     print("Looping...",fruit)

# while loop
# count = 0
# while count < len(favorite_fruits):
#     print("Looping...", favorite_fruits[count])
#     count += 1


# Nested Loops

# start_time = time.time()
# for i in range(100):
#     #inner loop
#     for j in range(100):
#        print(0, end=" ")
#     print() #new line

# print(round(time.time() - start_time, 5), "Seconds")

#### Exercise
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
count = 0 
# 1. Print all the numbers in the list 
for idx,  i in enumerate(num_list):
  count += 1
#   print(i)
  # add a contion that looks for all numbers greater than 45 and print only those numbers
  if(i > 45):
    print("Over 45",i)
  elif(i == 36):
     print("Number found at position:", idx)
     break
  else:
      print("Under 45",i)
  

  print("Total numbers in the list:", count)

  a = isinstance(str , "aa")
  print(a)