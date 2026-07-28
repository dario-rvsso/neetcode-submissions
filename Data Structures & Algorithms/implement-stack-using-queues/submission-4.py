class MyStack:

    def __init__(self):
        self.content = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.content.append(x)
        self.size += 1
        if self.size > 1:
            self.content.rotate()

    def pop(self) -> int:
        if self.size <= 0:
            return None
        self.size -= 1
        return self.content.popleft()

    def top(self) -> int:
        x = self.content[0]
        #x = self.pop()
        #self.push(x)
        return x

    def empty(self) -> bool:
        return True if self.size <= 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()