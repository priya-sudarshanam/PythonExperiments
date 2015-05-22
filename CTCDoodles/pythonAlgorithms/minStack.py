#stack class and its functions
import sys
class Stack:
    def __init__(self):
        self.items = []
        self.min = []

    def isEmpty():
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        if not self.min or item <= self.minStack():
            self.min.append(item)         
        
    def pop(self):
        if not self.isEmpty():
           return self.items.pop()

    def minStack(self):
       return self.min[-1]
                

s = Stack()
s.push(4)
s.push(6)
s.push(8)
print s.minStack()




        
