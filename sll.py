#SLL stands for Singly Linked List, which is a data structure that consists of nodes where each node contains data and a reference to the next node in the list. The last node in the list points to None, indicating the end of the list. Below is an implementation of a singly linked list in Python.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(10)
second = Node(20)
third = Node(30)
head.next = second
second.next = third
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

#Insertion at the end of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(20)
second = Node(30)

head.next = second

new_node = Node(10)
new_node.next = head
head = new_node

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

#Insertion at the end of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
second = Node(20)

head.next = second

new_node = Node(30)

temp = head
while temp.next:
    temp = temp.next

temp.next = new_node

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

#Insertion at a specific position in the linked list
#Suppose we want to insert 25 after 20:
#    10 -> 20 -> 30    result: 10 -> 20 -> 25 -> 30

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third

new_node = Node(25)

new_node.next = second.next
second.next = new_node

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

#Deletion of node from beginning of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(10)
second = Node(20)
third = Node(30)
head.next = second
second.next = third
head = head.next
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

#Deletion of node from end of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(10)
second = Node(20)
third = Node(30)
head.next = second
second.next = third
temp = head
while temp.next.next:
    temp = temp.next
temp.next = None
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")