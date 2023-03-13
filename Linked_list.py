# class Node:
#     def __init__(self, datanode) -> None:
#         self.datanode = datanode
#         self.nextnode = None


# class SlinkedList:
#     def __init__(self) -> None:
#         self.headnode = None

#     def listprint(self):
#         printnode = self.headnode
#         while printnode is not None:
#             print(printnode.datanode)
#             printnode = printnode.nextnode

#     def at_the_beg(self, Newdata):
#         newNode = Node(Newdata)

#         newNode.nextnode = self.headnode
#         self.headnode = newNode

#     def at_the_end(self, newdata):
#         NewNode = Node(newdata)
#         if self.headnode is None:
#             self.headnode = NewNode
#             return
#         last = self.headnode
#         while last.nextnode:
#             last = last.nextnode
#         last.nextnode = NewNode

#     def Inbtw(self, middle_node, newdata):
#         if middle_node is None:
#             print(" the mentioned node is absent")
#             return
#         newNode = Node(newdata)
#         newNode.nextnode = middle_node.nextnode
#         middle_node.nextnode = newNode


# list = SlinkedList()
# list.headnode = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
# e4 = Node("Fri")

# list.headnode.nextnode = e2
# e2.nextnode = e3
# e3.nextnode = e4

# list.at_the_beg("Start")
# list.Inbtw(list.headnode.nextnode, "middle")
# list.at_the_end("end")
# list.listprint()


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Link_kardo_listko:
    def __init__(self) -> None:
        self.head = None

    def add_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def add_after_Node(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("ni hai idhar")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def print_ll(self):
        if self.head == None:
            print("khuch ni hai agge chalo")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next


linkedlist = Link_kardo_listko()
linkedlist.head = Node(50)
e2 = Node(60)
e3 = Node(70)
e4 = Node(80)

linkedlist.head.next = e2
e2.next = e3
e3.next = e4

linkedlist.add_end(200)
linkedlist.add_after_Node(150, 50)
linkedlist.add_beg(100)
linkedlist.print_ll()
