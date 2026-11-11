class Node:
    def __init__(self, tables, left=None, right=None, leftKey=None, rightKey=None):
        self.tables = tables
        self.left = left
        self.right = right
        self.leftKey = leftKey
        self.rightKey = rightKey

    @property
    def isTable(self):
        return self.left is None
