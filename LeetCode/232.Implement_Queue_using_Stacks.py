class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.org_stack = []
        self.rev_stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.org_stack.append(x)
        
        # Move from rev to org
        n = 0
        while self.rev_stack:
            self.org_stack.append(self.rev_stack.pop())
            n += 1
        
        # Move from org to rev
        self.rev_stack.append(x)
        for i in range(n):
            self.rev_stack.append(self.org_stack.pop())        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        res = self.rev_stack.pop()
        
        # Move from org to rev
        n = 0
        while self.org_stack:
            self.rev_stack.append(self.org_stack.pop())
            n += 1
            
        # Move from rev to org
        self.rev_stack.pop()
        for i in range(n-1):
            self.org_stack.append(self.rev_stack.pop())
        
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.rev_stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.org_stack:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()