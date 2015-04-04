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


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def printList(self):
        current = self.head
        ctr = 0
        while current <> None:
            ctr += 1
            print "Element at position %s is: %s"%(ctr,current.getData())
            current = current.getNext()

        #return
    
    def size(self):
        current = self.head
        count = 0
        while current <> None:
            count += 1
            current = current.getNext()

        return count
        
    def middleElt(self):
        ctr = 1
        slow = self.head
        fast = self.head
        while fast <> None and fast.getNext() <> None:
            slow = slow.getNext()
            fast = fast.getNext().getNext()
            ctr += 1
            
        return slow.getData()
    
    def search(self,item):
        current = self.head
        found = False
        while current <> None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        found = False
        previous = None
        removed = False
        while not found and current <> None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if found:
          if previous == None:
            self.head = current.getNext()
            
          else:
            previous.setNext(current.getNext())
          removed = True
           
        
        return removed

    def index(self,item):
        current = self.head
        found = False
        counter = 0
        while not found and current <> None:
            counter += 1
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        if not found:
            counter = 0
            
        return counter

    def pop(self):
       current = self.head
       previous = None
       while current.getNext() <> None:
           previous = current
           current = current.getNext()

       previous.setNext(None)

    def insertAtHead(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def insertAtTail(self,item):
        temp = Node(item)
        current = self.head
        prev = None
        while current.getNext() <> None:
            prev = current
            current = current.getNext()
        
        temp.setNext(None)
        current.setNext(temp)

    def revList(self):
        prev = None
        curr = self.head
        while curr <> None:
            nxt = curr.getNext()
            curr.setNext(prev)
            prev = curr
            curr = nxt
              
        self.head = prev
        while prev <> None:
            print prev.getData()
            prev = prev.getNext()
        return
   
            
myList = UnorderedList()
myList.add(31)
myList.add(24)
myList.add(16)
myList.add(30)
##myList.add(35)
##myList.add(60)
##myList.add(55)
print myList.middleElt()
myList.printList()
myList.revList()
#print myList.remove(24)
#print myList.size()
#print myList.index(31)
#myList.pop()
##print myList.size()
##print myList.index(31)
##print myList.index(24)
##print myList.index(16)
#myList.insertAtTail(55)
#print myList.isCircular()
