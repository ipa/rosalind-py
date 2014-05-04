

def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n):
    if n == 0:
        return 0
    else:
        fibo_numbers = list()
        # add fibo numbers from 0 to 2
        fibo_numbers.append(0)
        fibo_numbers.append(1)
        fibo_numbers.append(1)
        for count in range(3, n+1):
            x = fibo_numbers[count-1] + fibo_numbers[count-2]
            fibo_numbers.append(x)

        return fibo_numbers[len(fibo_numbers)-1]

num = int(input("Fibonacci number of: "))

result = fib2(num)
print(result)