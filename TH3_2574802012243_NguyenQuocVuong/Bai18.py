class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort_linked_list(head):
    if not head:
        return None
    
    current_i = head
    while current_i:
        current_j = head
        while current_j and current_j.next:
            if current_j.data > current_j.next.data:
                current_j.data, current_j.next.data = current_j.next.data, current_j.data
            current_j = current_j.next
        current_i = current_i.next
    return head

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else " -> null\n")
        curr = curr.next

head = Node(1)
head.next = Node(3)
head.next.next = Node(2)

sorted_head = bubble_sort_linked_list(head)
print_list(sorted_head) 