class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertion_sort_linked_list(head):
    sorted_head = None
    current = head
    
    while current is not None:
        next_node = current.next
        if sorted_head is None or sorted_head.data >= current.data:
            current.next = sorted_head
            sorted_head = current
        else:
            search = sorted_head
            while search.next is not None and search.next.data < current.data:
                search = search.next
            current.next = search.next
            search.next = current
        current = next_node
        
    return sorted_head

head = Node(3)
head.next = Node(1)
head.next.next = Node(2)

sorted_head = insertion_sort_linked_list(head)

curr = sorted_head
while curr:
    print(curr.data, end="->")
    curr = curr.next
print("null")