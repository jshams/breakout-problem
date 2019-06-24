def find_middle(ll):
    even = ll.size % 2 == 0
    node = ll.head
    if even:
        for i in range(ll.size // 2 + 1):
            if i == ll.size / 2:
                return node.data, node.next.data
            node = node.next
    else:
        for i in range(ll.size // 2 + 2):
            if i == ll.size // 2 + 1:
                return node.data
            node = node.next
