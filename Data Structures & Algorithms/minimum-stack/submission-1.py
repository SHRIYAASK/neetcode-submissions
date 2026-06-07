class MinStack:

    def __init__(self):
        self.MinStack=[]
        
    def push(self, val: int) -> None:
        self.MinStack.append(val)
    def pop(self) -> None:
        if not bool(MinStack):
            return -1
        return self.MinStack.pop()
    def top(self) -> int:
        return self.MinStack[-1]
    def getMin(self) -> int:
        return min(self.MinStack)
    

        
