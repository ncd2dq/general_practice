import random

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.recorded = False

    def __str__(self):
        return str(self.value)


class Tree(object):
    def __init__(self, head_node):
        self.head = head_node

    def place_node(self, num, node):

        if num > node.value:
            if node.right == None:
                node.right = Node(num)
            else:
                self.place_node(num, node.right)

        if num < node.value:
            if node.left == None:
                node.left = Node(num)
            else:
                self.place_node(num, node.left) 

    def ascending_process(self, node, ordered):

        if node.left != None:
            if not node.left.recorded:
                self.ascending_process(node.left, ordered)

                if not node.recorded:
                    ordered.append(node.value)
                    node.recorded = True
            if node.left.recorded and node.right != None:
                self.ascending_process(node.right, ordered)

        else: # Can't go left anymore
            if not node.recorded:
                ordered.append(node.value)
                node.recorded = True


            if node.right != None:
                self.ascending_process(node.right, ordered)

            else: # can't go left AND can't go right

                if not node.recorded:
                    ordered.append(node.value)
                    node.recorded = True

    #
    # Public Functions
    #

    def fill(self, number_list):
        for num in number_list:
            self.place_node(num, self.head)

    def ascending(self, node):
        ordered = []

        self.ascending_process(node, ordered)

        return ordered



for iter in range(50):
    digits = [round(random.random() * 100, 0) for _ in range(5000)]
    t = Tree(Node(1.0))
    t.fill(digits)

    test = t.ascending(t.head)

    for digit in digits:
        if digit not in test:
            print('error')
            print(digits)
            print(test)
print('done')

#print("Ordered: ", t.ascending(t.head))
#print("Original:", digits)