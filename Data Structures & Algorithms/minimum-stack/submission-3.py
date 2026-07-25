class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minval = val
        else:
            self.stack.append(val - self.minval)
            if val < self.minval:
                self.minval = val

    def pop(self) -> None:
        if self.stack:
            tmp = self.stack.pop()
            val = tmp + self.minval
            if tmp < 0:
                self.minval -= tmp 

    def top(self) -> int:
        tmp = self.stack[-1]
        if tmp > 0:
            val = tmp + self.minval
        else:
            val = self.minval
        return val

    def getMin(self) -> int:
        return self.minval
        
