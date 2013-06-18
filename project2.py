#Project 2

#fib: int -> void
def fib(limit):
    num1 = 0
    num2 = 1
    num3 = 0
    fibSum = 0
    while True:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        if (num3 >= limit):
            break
        if (num3 % 2 == 0):
            fibSum = fibSum + num3
    print(fibSum)
