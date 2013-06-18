#Project 1

sum = 0

for i in range(0, 1000):
    if (div_by(i, 3)):
        sum = sum + i
    elif (div_by(i, 5)):
        sum = sum + i
print(sum)

#div_by: int int -> bool
def div_by(x, multiple):
    if (x % multiple == 0):
        return true
    else:
        return false
