#Project 1

#div_by: int int -> bool
def div_by(x, multiple):
    if (x % multiple == 0):
        return true
    else:
        return false

#printSum: int int int -> void
def printSum(last, div1, div2):
    sum = 0
    for i in range(0, last):
        if (div_by(i, div1)):
            sum = sum + i
        elif (div_by(i, div2)):
            sum = sum + i
    print(sum)