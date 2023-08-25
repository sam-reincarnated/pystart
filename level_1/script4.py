value_1 = 1000
value_2 = 1000

# id outputs the reference / location where the variable is pointing

print("location of value_1 is ", id(value_1))
print("location of value_2 is ", id(value_2))


value_2 = 1001
print("current location of value_2 is ", id(value_2))
