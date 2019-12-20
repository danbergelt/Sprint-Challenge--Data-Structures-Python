class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
      # If inserting we must already have a tree/root
      # If value is < root go left, make a new tree/node if empty, otherwise keep going(recursion)
      # If greater than or equal to then go right, make a new tree/node if empty, otherwise keep going(recursion)
        if self.value == None:
            self.value = value
            return self.value
        elif value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
      # If target == self.value, return it
      # go left or right based on smaller or bigger
        if self.value == target:
            return self.value
        elif target < self.value:
            if self.left == target:
                return self.left
            elif self.left == None:
                return None
            else:
                return self.left.contains(target)
        else:
            if self.right == target:
                return self.right
            elif self.right == None:
                return None
            else:
                return self.right.contains(target)