#Project 2

#fib: int -> void
def fib(exceed):
    fibCount1 = 0
    fibCount2 = 1
    fibCount3 = 0
    fibSum = 0
    i = 0
    while i < exceed:
        fibCount3 = fibCount1 + fibCount2
        fibCount1 = fibCount2
        fibCount2 = fibCount3
        if (fibCount3 % 2 == 0):
            fibSum = fibSum + fibCount3
        i = i + 1
    print(fibSum)