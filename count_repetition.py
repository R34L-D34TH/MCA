def count_repetition(number):
    digits = dict()
    value = 0
    for index in range(0, len(number)):
        if number[index] in digits.keys():
            value = digits[number[index]]
            value += 1
            digits.update({number[index]: value})
        else:
            value = 1
            digits.update({number[index]: value})
    return digits


number = str(input("Enter a number:- "))
digits = count_repetition(number)
print(digits)
