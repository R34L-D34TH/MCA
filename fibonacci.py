def fibonacci_recursive(number):
    if number <= 0:
        print("in 0")
        return []
    elif number == 1:
        print("in 1")
        return [0]
    elif number == 2:d
        print("in 2")
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(number - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

number = int(input("Enter the number of terms:- "))

fib_series = fibonacci_recursive(number)
print("Fibonacci Series:", fib_series)
