class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
head = Node(10)
second = Node(20)
third = Node(30)
head.next = second
second.prev = head
second.next = third
third.prev = second
temp = head
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next
print("None")
