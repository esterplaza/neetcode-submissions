class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            if val < self.minstack[-1]:
                self.minstack.append(val)
        

    def pop(self) -> None:
        x = self.stack.pop()
        if x in self.minstack and x not in self.stack:
            self.minstack.remove(x)
        return x
        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.minstack[-1]

        
