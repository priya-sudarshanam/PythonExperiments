#stack class and its functions
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

#balancing of paranthesis
##def paranChecking(paranString):
##     s = Stack()   
##     balanced = True
##     opening = ["(","[","{"]
##     matching = ["()","[]","{}"]
##  #   output = "balanced"
##   #  index = 0
##    # while index < len(paranString):
##     for i in paranString:
##      # curr = paranString[index]
##       if i in opening:
##           s.push(i)                                 
##       else:
##           if s.isEmpty() or (s.pop()+i not in matching):
##               balanced = False
####            else:
####               x = s.pop()               
####               if x+curr not in matching:                   
####                   balanced = False
####                   return
##                   
###       index += 1
##     return "unbalanced" if not (balanced and s.isEmpty()) else "balanced"

##s = Stack()
##print s.isEmpty()
##s.push(4)
##s.push(6)
##s.push(8)
##print s.isEmpty()
##print s.pop()
##print s.peek()
##print s.size()

##print paranChecking("(())") # balanced
##print paranChecking("(()") #unbalanced
##print paranChecking("(())]") #unbalanced
##print paranChecking("{(())}") #balanced
##print paranChecking("") #balanced
##print paranChecking(" ") #unbalanced
##print paranChecking("[(())}") #unbalanced
##print paranChecking("{(}())") #unbalanced
##print paranChecking("{()](())") #unbalanced


def decToBinary(n):
    s = Stack()
    q=0
    div = 2
    even = [0,2,4,6,8]
    m= n
    a = ""
    x = ""
    k = "-0b"
    if n == 0:
      print 0    
    else:
      if n <0:
        n = abs(n)
      while  not n/div == q:        
        if int(str(n)[-1]) in even:
            s.push(0)
        else:
            s.push(1)
        q = n/div 
        n = q       
    while not s.isEmpty():
        x += str(s.pop())
        
    if m < 0:
       a = k + x + "\n"
    else:
       a = x +"\n"
    return a

print decToBinary(0)
print decToBinary(-42)
print decToBinary(233)

        
