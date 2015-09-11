def factorize(n):
    
    factorlist = []
    while n > 1:
        k = 2
        while k <= n:
            if n%k == 0:
                factorlist = factorlist + [k]
                n = n/k
                break
            else:
                k = k + 1
    return factorlist


def fib(n):
    first = second = 1
    print first
    print second
    counter = 2
    while counter < n:
        next = first + second
        first = second
        second = next
        counter = counter + 1

        print counter, ':', next, "factors are", factorize(next)

    
fib(100)
        