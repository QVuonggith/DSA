class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def list_to_linked(values):
    head = tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head
def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
def selection_sort_linked_list(head):
    result_head = result_tail = None
    while head:
        min_node = head
        min_prev = None
        prev, curr = head, head.next
        while curr:
            if curr.val < min_node.val:
                min_node = curr
                min_prev = prev
            prev, curr = curr, curr.next
        if min_node is head:
            head = head.next
        else:
            min_prev.next = min_node.next
        min_node.next = None

        if result_head is None:
            result_head = result_tail = min_node
        else:
            result_tail.next = min_node
            result_tail = min_node
    return result_head
if __name__ == "__main__":
    head = list_to_linked([3, 1, 2])
    sorted_head = selection_sort_linked_list(head)
    print(linked_to_list(sorted_head))  
