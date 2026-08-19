class MinStack:

    def __init__(self):
        self.stack = []
        self.stack2 = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack2 or val <= self.stack2[-1]:
            self.stack2.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.stack2[-1]:
            self.stack2.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack2[-1]
        
