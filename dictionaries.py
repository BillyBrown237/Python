# 
sample_dict = {1:'Coffee' , 2:'Tea', 3:'Juice'}

print(sample_dict[1])

my_d = {1:'Test', 'Name': 'Jim'}
print(type(my_d))
my_d[2] = 'Test 2'
my_d[1] = 'Not a Test'
# doesn't allow duplicate keys and updates the key with the latest value

for key, value  in my_d.items():
    print(str(key) + " : " + value)
