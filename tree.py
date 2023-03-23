# Binary serach tree
# key/data
# left child
# right child

# Implementation
class BST:
    def __init__(self, key) -> None:
        self.key = key
        self.lchild = None
        self.rchild = None

    # Insertion
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    # traversal
    def pre_order(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key, end=" ")

    def In_order(self):
        if self.lchild:
            self.lchild.In_order()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.In_order()

    # delection
    def delete(self, data, curr):
        # if tree is mpt
        if self.key is None:
            print("Tree is empty")
            return
        # find the node
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print("Given is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("Given is not present in the tree")
        else:
            # caese := 0 child ; 1 child ; 2 child
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = temp
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = temp
                return
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr)
        return self

    def Min_key(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("Node with the smallest key", current.key)

    def Max_key(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Node with the maximum key", current.key)

    # seraching
    def search(self, data):
        if self.key == data:
            print("Node is Found")
            return
        if data < self.key:
            # 1. left s.t empty 2. left s.t contain 1 or more node
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree")


# count
def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)


root = BST(30)
list1 = [20, 4, 30, 56, 4, 1, 5, 6]
for i in list1:
    root.insert(i)
# root.search(6)

print("Number of nodes", count(root))

# if count(root) > 1:
#     root.delete(30, root.key)
# else:
#     print("can not perform delete opearation")

root.Min_key()
root.Max_key()

print(" Pre-order:")
root.pre_order()
print("\n Post-order:")
root.post_order()
print("\n In-order:")
root.In_order()

# print(root.key)
# print(root.lchild)
# print(root.rchild)

# root.lchild = BST(5)
# print(root.lchild.key)
# print(root.lchild.lchild)
# print(root.lchild.rchild)

# root.rchild = BST(15)
# print(root.rchild.key)
# print(root.rchild.lchild)
# print(root.rchild.rchild)

# import heapq

# list1 = [(11, "Riya"), (2, "siya"), (3, "giya")]
# heapq.heapify(list1)
# for i in range(len(list1)):
#     print(heapq.heappop(list1))
