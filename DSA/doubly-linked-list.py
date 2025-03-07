class DoublyNode:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.val)

head = tail = DoublyNode(1)
print(tail)

#display the values of doubly linked list 
def display(head):
    current = head
    elements = []
    while current:
        elements.append(str(current.val))
        current = current.next
    print("<->".join(elements))
display(head)     

#Insert at the beginning - O(1)
def insert_at_beginning(head,tail,val):
    newNode = DoublyNode(val,next=head)
    head.prev = newNode
    return newNode,tail
head,tail = insert_at_beginning(head,tail,3)
display(head)

#Insert at end - O(1)
def insert_at_end(head,tail,val):
    newNode = DoublyNode(val,prev=tail)
    tail.next = newNode
    return head,newNode
head,tail = insert_at_end(head,tail,7)
display(head)
       