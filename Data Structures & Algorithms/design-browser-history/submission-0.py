class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(None, None, None)
        self.home = Node(homepage, self.head, None)
        self.tail = Node(None, self.home, None)
        self.head.next = self.home
        self.home.next = self.tail
        self.size_prev = 0
        self.size_next = 0

    def visit(self, url: str) -> None:
        newpage = Node(url, self.home, self.tail)
        self.home.next.prev = None
        self.home.next = newpage
        self.tail.prev = newpage
        self.home = newpage
        self.size_prev += 1
        self.size_next = 0
        
    def back(self, steps: int) -> str:
        if steps > self.size_prev:
            steps = self.size_prev
        curr = self.home
        for i in range(steps):
            curr = curr.prev
        self.size_prev = self.size_prev - steps
        self.size_next = self.size_next + steps
        self.home = curr
        return curr.val

    def forward(self, steps: int) -> str:
        if steps > self.size_next:
            steps = self.size_next
        curr = self.home
        for i in range(steps):
            curr = curr.next
        self.size_prev = self.size_prev + steps
        self.size_next = self.size_next - steps
        self.home = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)