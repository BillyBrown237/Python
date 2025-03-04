# and operator checks for a condition to be true
# or checks if only one of the conditions is true
# not , returns a false if the result is true and vice versa

# Example 1
print(2 + 2)
print(2 - 2)
print(35 / 5) # division always returns a float
print(2 * 2)
print(2 ** 2) # exponentiation
print(2 % 2) # modulo operator, returns the remainder of the division
print(2 // 2) # floor division, returns the integer part of the division

# Example 2 Logical operators
a = True
b = False

if a or b:
    print("Both are true")

if not(a) or not(b):
    print('All true')