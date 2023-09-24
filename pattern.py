def pattern(number):
    for num in range(0, number):
        for i in range(num):
            print(i, end=" ")
        print(" ")




number = int(input("How long do you want the pattern? "))
pattern(number)
