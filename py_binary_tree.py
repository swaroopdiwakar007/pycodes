class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def search(self, target):
        if self.data == target:
            print("found the data")
            return self
        elif self.left and self.data > target:
            return self.left.search(target)
        elif self.right and self.data < target:
            return self.right.search(target)
        else:
            print("Not found")

    def tr_pre_order(self): # top to bottom traverse -- first parent -- then left child -- then right child
        print(self.data, end=' ')
        if self.left:
            self.left.tr_pre_order()
        if self.right:
            self.right.tr_pre_order()

    def tr_in_order(self): # bottom to top traverse -- first left child -- then parent -- then right child
        if self.left:
            self.left.tr_in_order()
        print(self.data, end=' ')
        if self.right:
            self.right.tr_in_order()

    def tr_post_order(self): # bottom to top traverse -- first left child -- then right child -- then parent
        if self.left:
            self.left.tr_post_order()
        if self.right:
            self.right.tr_post_order()
        print(self.data, end = ' ')

    def height(self, h = 0): # get height of tree
        leftHeight = self.left.height(h + 1) if self.left else h
        rightHeight = self.right.height(h + 1) if self.right else h
        return max(leftHeight, rightHeight)

    def get_node_at_depth(self, depth, nodes = []):
        if depth == 0:
            nodes.append(self.data)
            return nodes      
        if self.left:
            self.left.get_node_at_depth(depth - 1, nodes)
        if self.right:
            self.right.get_node_at_depth(depth - 1, nodes)
        return nodes

class Tree:
    def __init__(self, root, name = ''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def tr_pre_order(self):
        self.root.tr_pre_order()

    def tr_in_order(self):
        self.root.tr_in_order()

    def tr_post_order(self):
        self.root.tr_post_order()

    def height(self):
        return self.root.height()

    def get_node_at_depth(self, depth):
        return self.root.get_node_at_depth(depth)

node = Node(10)
node.left = Node(5)
node.right = Node(15)
node.left.left = Node(0)
node.left.right = Node(7)
node.right.left = Node(12)
node.right.right = Node(20)

# print(node.right.data)

mytree = Tree(node, 'Name_of_tree')

# print(mytree.root.data)

# print(mytree.root.right.data)
# print(mytree.name)

# mytree.tr_pre_order()
# print()
# mytree.tr_in_order()
# print()
# mytree.tr_post_order()

# print(mytree.height())

print(mytree.get_node_at_depth(2))
