class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        #Checking if value is duplicate
        if data == self.data:
            return
        if data < self.data:
            #checking if not leaf node
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
            #add data in left subtree
        else:
            #add data in right subtree
            #checking if not leaf node
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        #visit left tree first
        if self.left:
            elements += self.left.in_order_traversal()
        #visit base node
        elements.append(self.data)
        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        # visit left tree first
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        if self.left:
            elements += self.left.post_order_traversal()
        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_side = self.left.calculate_sum() if self.left else 0
        right_side = self.right.calculate_sum() if self.right else 0
        return self.data + left_side + right_side

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_value = self.left.find_max()
            self.data = max_value
            self.right = self.right.delete(max_value)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [12,6,3,89,21,34,6,3]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal()) # This will return the list in a sorted order
    #numbers_tree.delete(89)
    numbers_tree.delete(6)
    print(numbers_tree.in_order_traversal())

    #print(numbers_tree.post_order_traversal())
    #print(numbers_tree.find_min())
    #print(numbers_tree.find_max())
    #print(numbers_tree.calculate_sum())




