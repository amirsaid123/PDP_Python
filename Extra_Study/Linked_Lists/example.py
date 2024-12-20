

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, val):
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = Node(val)

    def print(self):
        tmp = self.head.next
        while tmp:
            print(f"{tmp.val} -->", end=" ")
            tmp = tmp.next

    def insert(self, new_val, pos):
        tmp = self.head
        next_pos = 1
        while tmp.next:
            if next_pos == pos:
                new_node = Node(new_val)
                new_node.next = tmp.next
                tmp.next = new_node
                break
            tmp = tmp.next
            next_pos += 1
        else:
            tmp.next = Node(new_val)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]




linked_list = LinkedList()
for i in numbers:
    linked_list.append(i)

linked_list.print()
linked_list.insert(100, 5)
print()
linked_list.print()













# n1 = Node(1)
# n2 = Node(25)
# n3 = Node(56)
# n4 = Node(90)
# n5 = Node(3)
#
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
#







