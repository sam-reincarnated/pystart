# string as a sequence

string = "This is the string we will be using"

# let's print the first character of the string

print(string[0])

# let's print the 10th character of the string
print(string[9])

# let's print the last character of the string
print(string[-1])


# finding Nemo
new_string = "I don't know where Nemo is at!"

print(new_string.index("Nemo"))

# now lets slice "Nemo"

nemo = "Nemo"

print("Nemo sliced", nemo[1:3])


print("Nemo sliced", nemo[:3])


print("Nemo sliced", nemo[1:])


# this is special 

# stepping [first:last:stepsize]
print(string[0:-1:2])

