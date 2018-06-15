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

        if node.left != None:  ### 1 Prioritize going all the way left first (to reach the smallest number)
            if not node.left.recorded: ### 1 If left has never been touched before, call a recursive call to keep going left
                self.ascending_process(node.left, ordered)

                if not node.recorded: ### 5 after you cannot go left anymore AND can't go right, the recursive loop will start unraveling and eventually
                                        ### hit code after the above recursive call, adding each step as we unravel
                    ordered.append(node.value)
                    node.recorded = True

            if node.right != None: ### 6 after fully unravelling and going as far left as you can on a node, go 1 step to the right and try the whole thing again
                                    ### starting at step 1 
                self.ascending_process(node.right, ordered)

        else: ### 2 Once you have reached the smallest number, record it and try going right just 1 step
            if not node.recorded:
                ordered.append(node.value)
                node.recorded = True


            if node.right != None: ### 3 Trying to go right just 1 step, to then try and go all the way left again
                self.ascending_process(node.right, ordered)

            else: ### 4 If you can't go right or left, add the number and do not call another recursion so the recursive loop begins to unfold

                if not node.recorded:
                    ordered.append(node.value)
                    node.recorded = True

    def _reset(self, node):

        if node.left != None:
            self._reset(node.left)

            node.recorded = False

            if node.right != None:
                self._reset(node.right)

        else:
            node.recorded = False

            if node.right != None:
                self._reset(node.right)

            else:
                node.recorded = False



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

    def reset(self):
        self._reset(self.head)

    def __str__(self):
        self.reset()
        ascend = self.ascending(self.head)
        return str(ascend)


if __name__ == "__main__":
    for iter in range(50):
        digits = [round(random.random() * 100, 0) for _ in range(15)]
        t = Tree(Node(1.0))
        t.fill(digits)

        test = t.ascending(t.head)

        for digit in digits:
            if digit not in test:
                print('error')
                print(digits)
                print(test)
    print(t)


class Human(object):
    def __init__(self):
        pass