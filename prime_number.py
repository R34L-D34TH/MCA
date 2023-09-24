def prime_number(number):
    factor = 0
    for i in range(1, number + 1):
        if number % i == 0:
            factor += 1

    if factor > 2:
        print("Number is not prime")
    else:
        print("Number is prime")


while True:
    number = int(input("Enter a number:- "))
    prime_number(number)