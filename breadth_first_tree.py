class Tree:
    def __init__(self):
        self.b_tree = dict()

    def insert(self, parent, value):
        if parent not in self.b_tree:
            print(f"Parent node {parent} does not exist.")
            return

        self.b_tree[parent].append(value)
        self.b_tree[value] = []

    def show(self):
        print(self.b_tree)

# Create a tree instance
my_tree = Tree()

# Take input for the root value
root_value = int(input("Enter root number: "))
my_tree.b_tree[root_value] = []

while True:
    parent_value = int(input("Enter parent node value: "))
    child_value = int(input("Enter child node value: "))
    my_tree.insert(parent_value, child_value)
    my_tree.show()
