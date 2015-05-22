#queue class and its functions
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.isEmpty():
           return self.items.pop()
        else:
           return "queue is empty"

    def size(self):        
        return len(self.items)

    def minQueue(self, itemLst):
        minQ = sys.maxint
        for i in range(len(itemLst)):
            if i < minQ:
                minQ = i
                self.enqueue(i)
            else:
                temp = self.dequeue()
                self.enqueue(minQ)

    

q = Queue()
print q.isEmpty()
q.enqueue(5)
q.enqueue(7)
q.enqueue(9)
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.size()


