class MinStack:

    def __init__(self):
        self.stack=deque()
        self.topelem=-1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.topelem+=1

    def pop(self) -> None:
        x=self.stack.pop()
        self.topelem-=1

    def top(self) -> int:
        return(self.stack[self.topelem])

    def getMin(self) -> int:
        return(min(self.stack))
