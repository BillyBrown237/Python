# Args and Kwargs  (kwyword Args) , arguments and keyword arguments
#*args allow n arguments to be used in a function call

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(2,3,4,56,6,7))

# Kwargs

def bill_sum(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    print(sum)