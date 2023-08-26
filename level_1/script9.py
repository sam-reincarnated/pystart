mixed_case = "MIXedcases"

print("Original:", mixed_case)
print("Upper:", mixed_case.upper())
print("Lower:", mixed_case.lower())
print("Capitalize:", mixed_case.capitalize())

spider = "Spider Man"
pieces = spider.split()
print(pieces, len(pieces))

IP = "127.0.0.1"
octets = IP.split(".")
print(len(octets))

counter = 1
for octet in octets:
    print("Octet", counter, " is ", octet)
    counter +=1
