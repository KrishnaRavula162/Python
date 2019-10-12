x = int(input("Enter a Number : "))
is_prime = True
y = 2
while y < x:
    if (x % y == 0):
        is_prime = False
        break
    y = y + 1

if is_prime == True:
    print(x, "is prime")
else:
    print(x, "is composite")