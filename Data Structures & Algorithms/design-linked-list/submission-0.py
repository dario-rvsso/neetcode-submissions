class MyLinkedList:

    class Node:
        def __init__(self, val=None, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next
        def getVal(self):
            return self.val
        def setVal(self, val):
            self.val = val
        def setNext(self, next):
            self.next = next
        def setPrev(self, prev):
            self.prev = prev

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.size = 0
        self.head.setNext(self.tail)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head.next
        for i in range(index):
            curr = curr.next
        tmp = curr.getVal()
        return tmp if tmp != None else -1 

    def addAtHead(self, val: int) -> None:
        newhead = self.Node(val, self.head, self.head.next)
        self.head.next.setPrev(newhead)
        self.head.next = newhead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newtail = self.Node(val, self.tail.prev, self.tail)
        self.tail.prev.setNext(newtail)
        self.tail.prev = newtail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0 
        curr = self.head
        for i in range(index):
            curr = curr.next
        newnode = self.Node(val, curr, curr.next)
        curr.next.setPrev(newnode)
        curr.setNext(newnode)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head.next
        for i in range(index):
            curr = curr.next
        curr.prev.setNext(curr.next)
        curr.next.setPrev(curr.prev)
        curr.setPrev(None)
        curr.setNext(None)
        curr.setVal(None)
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)