# tree = {0:[2],
#         1:[3,4],
#         2:[6,7]}
# tree = []{5:[3,7],
#           3:[]}

# tree=[]
# print(type(tree))
# while True:
#     number = int(input("Enter number to add to list:- "))
#     tree.append(number)
#     if number == -1:
#         break
#
# print(tree)


class tree:
    def __init__(self, number):
        self.number = number
        self.left = None
        self.right = None

    def insert(self, number):
        if self.number is not None:
            if number < self.number:
                if self.left is None:
                    self.left = tree(number)
                else:
                    self.left.insert(number)
            elif number > self.number:
                if self.right is None:
                    self.right = tree(number)
                else:
                    self.right.insert(number)
        else:
            self.number = number

            # Print the tree////

    def print_tree(self):
            if self.left:
                self.left.print_tree()
            print(self.number),
            if self.right:
                self.right.print_tree()


root = int(input("Enter root node"))
root = tree(root)
while True:
    number = int(input("Add Number into the tree:- "))
    root.insert(number)
    if number == -1:
        break

root.print_tree()
