'''

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

#41ms
class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, val):
        self.stack.append(val)
            
        if len(self.minStack) == 0 or val <=self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        
            
        if self.stack[-1]== self.minStack[-1]:
            self.minStack.pop()
            
        self.stack.pop()
        
        

    def top(self):
        return self.stack[-1]
       
        

    def getMin(self):
        return self.minStack[-1]
            
        
        
#bet time 25ms
class MinStack(object):

    def __init__(self):
        self.stk1 = []
        self.stk2 = []
        self.min = 99999999999
        self.mincnt = 0


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stk1.append(val)
        if val < self.min:
            self.min = val
            self.mincnt = 1
        elif val == self.min:
            self.mincnt += 1


    def pop(self):
        """
        :rtype: None
        """
        val = self.stk1.pop()
        if val == self.min:
            self.mincnt -= 1
        if self.mincnt == 0:
            self.min = 99999999999
            while(len(self.stk1) > 0):
                val1 = self.stk1.pop()
                if val1 < self.min:
                    self.min = val1
                    self.mincnt = 1
                elif val == self.min:
                    self.mincnt += 1
                self.stk2.append(val1)
            while(len(self.stk2) > 0):
                val1 = self.stk2.pop()
                self.stk1.append(val1)


    def top(self):
        """
        :rtype: int
        """
        return self.stk1[len(self.stk1)-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        




#best pace complexity 16600kb
class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
