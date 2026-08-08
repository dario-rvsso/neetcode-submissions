class Node:
    def __init__(self, key = None, val = None, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.fullness = 0
        self.cache = {}
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, self.head, None)
        self.head.next = self.tail
 
    def get(self, key: int) -> int:
        rc = -1
        if key in self.cache:
            curr = self.cache[key]
            rc = curr.val
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.head.next.prev = curr
            curr.next = self.head.next
            self.head.next = curr
            curr.prev = self.head 
        return rc         

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value, self.head, self.head.next)
            self.head.next.prev = node
            self.head.next = node
            self.fullness += 1
            if self.fullness > self.capacity:
                curr = self.tail.prev
                curr.prev.next = self.tail
                self.tail.prev = curr.prev
                curr.prev = None
                curr.next = None
                self.cache.pop(curr.key, None)
                self.fullness -= 1
            self.cache[key] = node
        else:
            node = self.cache[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
