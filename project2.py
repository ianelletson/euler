#Project 2

#fib: int -> void
def fib(limit):
    num1 = 0
    num2 = 1
    num3 = 0
    for i in range(0,10):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num2)
