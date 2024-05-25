n = int(input("input number: "))
f = 1
n1 = n
while (n > 1):
    f*=n
    n-= 1
print(f"{n1}! = {f}")