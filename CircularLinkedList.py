class Node:
    def __init__(self,initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,newNext):
        self.next = newNext


class CircularList:
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(self.head)

    def add(self,item):
        temp = Node(item)
        if self.head is None:
            temp.setNext(self.head)
            self.head.setNext(temp)
        else:
            current = self.head
            while current.getNext() <> self.head:
                  current = current.getNext()

            current.setNext(temp)
            temp.setNext(self.head)
            
    def addAfterHead(self,item):
        temp = Node(item)
        prev = self.head
        current = self.head.getNext()
        prev.setNext(temp)
        temp.setNext(current)

    def getCenterElt(self):
        slow = self.head
        fast = self.head
        ctr = 0
        while fast.getNext() <> self.head or fast.getNext().getNext() <> self.head:
            ctr += 1
            slow = slow.getNext()
            fast = fast.getNext().getNext()

        centerStr = "Middle of the list is: %s and index position is: %s"\
                    %(slow.getData(),ctr)
        
        return centerStr

    def printList(self):
        current = self.head.getNext()
        ctr = 0        
        while current <> self.head:            
            ctr += 1
            print "Element at position %s is: %s"%(ctr,current.getData())
            current = current.getNext()

        printStr = "size of the list is: ", ctr
        
        return printStr

    def index(self, item):
        current = self.head.getNext()
        ctr = 0
        found = False
        while not found and current <> self.head:
            ctr += 1
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        if not found:
            ctr = -1

        if ctr > 0:
            return "found and index is: {0}", ctr
        else:
            return "not found"

    def removeHead(self):
        current = self.head.getNext()
        prev = self.head.getNext()
        while current.getNext() <> self.head:
            current = current.getNext()

        self.head = prev
        current.setNext(self.head)
 
    def pop(self):
        current = self.head.getNext()
        prev = None
        while current.next <> self.head:
            prev = current
            current = current.getNext()

        prev.setNext(self.head)
        
    def isCircular(self):
        circular = False
        slow = self.head
        fast = slow.getNext()
        while fast.getNext() <> None:
          if (fast == slow or fast.getNext() == slow):
                circular = True
                break
          else:
                slow = slow.getNext()
                fast = fast.getNext().getNext()
                
        return circular        
        
myList = CircularList()
myList.add(16)
myList.add(31)
myList.add(64)
myList.add(34)
print myList.printList()
myList.addAfterHead(17)
#print myList.pop()
#print myList.index(34)
#print myList.pop()
#print myList.removeHead()
print myList.printList()
print myList.getCenterElt()
print myList.isCircular()
