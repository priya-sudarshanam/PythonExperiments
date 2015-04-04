class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BTree:
    def __init__(self):
        self.root = None
        
    def addNode(self,data):
        return Node(data)

    def insert(self, root, data):
        if root:
           if data <= root.data:
                root.left = self.insert(root.left, data)
           else:
                root.right = self.insert(root.right, data)
           return root
        else:
           return self.addNode(data)
     
    def lookup(self, root, target, parent=None):
        found = False
        if root:
          if target == root.data:
              found = True
          elif target < root.data:
             return self.lookup(root.left, target, root)
          else:
             return self.lookup(root.right, target,root)
        else:
          found = False

        if parent:
            return found,parent,parent.data,target
        elif not root or not parent:
            return found,None,None,target
        
    def getMin(self,root):
        if root:
          while root.left:
              root = root.left
              
        return root.data

    def getMax(self,root):
        if root:
          while root.right:
              root = root.right
              
        return root.data

    def treeHeight(self,root):
        if root == None:
          return 0
        else:
            l = self.treeHeight(root.left)
            r = self.treeHeight(root.right)
            return max(l,r) + 1
    
    def childrenCount(self, root,node):
        cnt = 0
        f,p,pdata,d = self.lookup(root,node)
        if f:
          if d == root.data:
            if root.left:
                  cnt += 1
            if root.right:
                  cnt += 1
          elif node < root.data:
            return self.childrenCount(root.left, node)
          else:
            return self.childrenCount(root.right, node)
        else:
            cnt = -1
        
        return cnt

    def inOrder(self,root):
        if root:
          self.inOrder(root.left)
          print root.data,
          self.inOrder(root.right)

    def postOrder(self,root):
        if root:
          self.postOrder(root.left)
          self.postOrder(root.right)
          print root.data,

    def preOrder(self,root):
        if root:
          print root.data,
          self.preOrder(root.left)
          self.preOrder(root.right)          

    def revOrder(self,root):
        if root:
          self.revOrder(root.right)
          print root.data,
          self.revOrder(root.left)

    def size(self,root):
        if root:
            return (self.size(root.left) + 1 + self.size(root.right))
        else:
            return 0

    def convertArray(self,root):
        if not root:
          return []
        return [root.data] + self.convertArray(root.left) + self.convertArray(root.right)

    def returnPreAndSuc(self,root,node):
            #way 1
            if root and self.lookup(root,node):
                l = sorted(self.convertArray(root))
                m = l.index(node)
                predeccesor = l[m-1]
                successor = l[m+1]
            return "Predecessor and Successor: %s, %s"%(predeccesor,successor)

            #way 2
         #   if root:
                
               
    def compareTrees(self,root1,root2):
        # way 1
##        r1 = self.convertArray(root1)
##        r2 = self.convertArray(root2)
##        treeSame = False
##        if root1 and root2 and (root1 == root2):
##          treeEqual = [i for i, j in zip(r1, r2) if i <> j]
##        
##        if not treeEqual:
##           treeSame = True
##        return treeSame
        
        #way 2
        treeEqual = False
        if not root1 and root2:
            return "missing roots: ",treeEqual
            return            
        else:
            if root1.data <> root2.data:
              return "roots are unequal: ",treeEqual
              return
            else:
              while root1.left and root2.left:
                if root1.left.data <> root2.left.data:
                    return "left side of tree unequal: ",treeEqual 
                    return
                return self.compareTrees(root1.left,root2.left)
                                                        
              while root1.right and root2.right:
                if root1.right.data <> root2.right.data:
                    return "right side of tree unequal: ",treeEqual
                    break
                return self.compareTrees(root1.right,root2.right)
            
        treeEqual = True           
        return treeEqual         

    def deleteNode(self,root,node):
        if root:
            f,p,pdata,t = self.lookup(root,node)
            if f:
              if self.childrenCount(root,t) == 0:
                 if p.right is t:
                    p.right = None
                 else:
                    p.left = None
              elif self.childrenCount(root,t) == 1:
                   if p.right.data is t:
                       if p.right.right:
                         p.right = p.right.right
                       elif p.right.left:
                         p.right = p.right.left                      
                   else:
                      if p.left.right:
                        p.left = p.left.right
                      else:
                         p.left = p.left.left
              else:
                  successor = p.right
                  while successor.left:
                      p = successor
                      successor = successor.left
                  p.data = successor.data
                  if p.left == successor:
                      p.left = successor.right
                  else:
                      p.right = successor.right                     

                
if __name__ == "__main__":
    bTree = BTree()
    root = bTree.addNode(8)
    root1 = bTree.addNode(8)
    for i in range(0, 8):
        data = int(raw_input("insert the node value for tree1 %d: " % i))
        bTree.insert(root, data)
    print
##    for i in range(0, 4):
##        data = int(raw_input("insert the node value for tree2 %d: " % i))
##        bTree.insert(root1, data)
##    print    

##    data = int(raw_input("insert a value to find: "))
##    f,p,t = bTree.lookup(root, data,None)
##    if f:
##       print "parent,target: %s,%d" %(p,t)
##    else:
##       print "not found"

    print "Minimum of the tree is: ", bTree.getMin(root)
    print "Maximum of the tree is: ", bTree.getMax(root)
    print "Height of the Tree is: ", bTree.treeHeight(root)
    #cdata = int(raw_input("insert node to find children: "))
    #ctr = bTree.childrenCount(root,cdata)
    #print ctr
    #if ctr >= 0:
     #   print "Number of children for node: %s is : %s " %(cdata,ctr)
    #else:
     #   print "Node %s has no children" %(cdata)    


    print "Inorder Traversal: \n", bTree.inOrder(root)
    print "Preorder Traversal: \n", bTree.preOrder(root)
    print "Postorder Traversal: \n", bTree.postOrder(root)
    print "Reverse Order: \n", bTree.revOrder(root)
    print "\nSize of the tree is: ", bTree.size(root)
   # bTree.compareTrees(root,root1)
    node = int(raw_input("insert the node for deleting : "))    
    #print bTree.returnPreAndSuc(root,node)
    bTree.deleteNode(root,node)
    print "Inorder Traversal: \n", bTree.inOrder(root)
               
