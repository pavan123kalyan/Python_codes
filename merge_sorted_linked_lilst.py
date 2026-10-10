class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = [1, 2, 4]
list2 = [1, 3, 4]

dummy1 = ListNode()
cur1 = dummy1

for i in list1:
    cur1.next = ListNode(i)
    cur1 = cur1.next

dummy2 = ListNode()
cur2 = dummy2

for i in list2:
    cur2.next = ListNode(i)
    cur2 = cur2.next

list1 = dummy1.next
list2 = dummy2.next

p = ListNode()
cur = p

while list1 and list2:
    if list1.val <= list2.val:
        cur.next = list1
        list1 = list1.next
    else:
        cur.next = list2
        list2 = list2.next

    cur = cur.next

if list1:
    cur.next = list1
else:
    cur.next = list2

ans = p.next

while ans:
    print(ans.val, end=" ")
    ans = ans.next