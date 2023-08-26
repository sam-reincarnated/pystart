print("===============Operations on INT===============")

str_operations = dir(int)

for operation in str_operations:
    if operation[0:2] != "__" :
        print(operation)

print("===============Operations on STR===============")

str_operations = dir(str)

for operation in str_operations:
    if operation[0:2] != "__" :
        print(operation)
print("===============Operations on BOOL ===============")

str_operations = dir(bool)

for operation in str_operations:
    if operation[0:2] != "__" :
        print(operation)

