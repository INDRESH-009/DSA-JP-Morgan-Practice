# SINGLY LINKED LIST 
from curses import flash
from xml.dom.minidom import Element


class singlyNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
Head = singlyNode(1)
A = singlyNode(2)
B = singlyNode(3)
C = singlyNode(4)

Head.next = A
A.next = B
B.next = C

print(Head)

#Traverse the list- O(n)
current = Head
while current:
    print(current)
    current = current.next

#Display a linked list - O(n)
def display(head):
    current = head
    elements = []
    while current:
        elements.append(str(current.val))
        current = current.next
    print('->'.join(elements))
display(Head)

# Search for a node value - O(n)
def search(head,value):
    current = head
    while current:
        if current.val==value:
            return True
        current = current.next
    return False
print(search(Head,9))