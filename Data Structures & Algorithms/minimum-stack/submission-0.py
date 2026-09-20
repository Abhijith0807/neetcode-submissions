class MinStack:

    def __init__(self):
        self.stackvals=deque()
        self.topv=-1

    def push(self, val: int) -> None:
        self.stackvals.append(val)
        self.topv+=1
        

    def pop(self) -> None:
        self.stackvals.pop()        
        self.topv-=1
    def top(self) -> int:
        return(self.stackvals[self.topv])

    def getMin(self) -> int:
        return(min(self.stackvals))
        
