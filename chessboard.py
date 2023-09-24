numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)


sliced_elements = numbers[:2]
numbers.extend(sliced_elements)

print("Updated name list:", numbers)


def name_to_octal(name):
        octal_representation = ""

        for char in name:
                octal_representation += oct(ord(char))[2:]

        return octal_representation


my_name = "Vaibhav Bhardwaj"
octal_name = name_to_octal(my_name)
print("Octal representation of Vaibhav Bardwaj name:", octal_name)
print(u"\u20B9")


def draw_chessboard(size):
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                print("\u25A0", end=" ")  # Black square
            else:
                print("\u25A1", end=" ")  # White square
        print()

# Specify the size of the chessboard (8x8)
chessboard_size = 8

draw_chessboard(chessboard_size)


