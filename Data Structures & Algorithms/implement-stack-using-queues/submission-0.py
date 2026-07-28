class MyStack:

    def __init__(self):
        self.content = []
        self.size = 0

    def push(self, x: int) -> None:
        self.content.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.size <= 0:
            return None
        tmp = []
        for i in range(self.size - 1):
            e = self.content.pop(0)
            tmp.append(e)
        x = self.content.pop(0)
        self.content = tmp
        self.size -= 1
        return x

    def top(self) -> int:
        x = self.pop()
        self.push(x)
        return x

    def empty(self) -> bool:
        return True if self.size <= 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()