class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (self.minval == None) or (val < self.minval):
            self.minval = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minval:
            try:
                self.minval = min(self.stack)
            except ValueError:
                self.minval = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval
        
