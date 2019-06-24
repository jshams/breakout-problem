def find_middle(ll):
    even = ll.size % 2 == 0
    node = ll.head
    if even:
        for i in range(ll.size // 2 + 1):
            if i == ll.size / 2 - 1:
                return node.data, node.next.data
            node = node.next
    else:
        for i in range(ll.size // 2 + 2):
            if i == ll.size // 2:
                return node.data
            node = node.next


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self, items=None):
        self.head = None
        self.tail = None
        self.size = 0
        if items is not None:
            for item in items:
                self.append(item)

    def items(self):
        items = []
        node = self.head 
        while node is not None: 
            items.append(node.data) 
            node = node.next
        return items

    def is_empty(self):
        return self.head is None

    def length(self):
        return self.size

    def append(self, item):
        new_node = Node(item)
        old_tail = self.tail
        self.tail = new_node
        if old_tail is not None:
            old_tail.next = new_node
        if self.head is None:
            self.head = new_node
        self.size += 1

ll = LinkedList([1,2,3,4,5,6,7,8])
print(find_middle(ll))