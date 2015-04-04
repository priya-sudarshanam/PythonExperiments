import os, traceback, math
from collections import defaultdict, deque

def isTriangle(a,b,c):
    if ((a > (b + c)) or (b > (a + c)) or (c > (a + b))):
        print "Triangle No"
    else:
        print "Triangle Yes"


def fibonacci(n):
    if n < 0 or not isinstance(n, int):
        print "cannot give fibonacci of negative or float"
        os._exit(0) 
    
    if n == 0:
     return 0
    elif n == 1:
     return 1
    else:
      return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n < 0 or not isinstance(n, int):
        print "cannot give factorial of negative or float"
        os._exit(0)

    if n == 0:
      return 1
    else:
      return n * factorial(n-1)


def mult(n,m):
    if m == 0:
      return 1
    else:
      return n * mult(n,m-1)

def factors(n):
    l = []
    if n == 0 or n < 0:
      print "no factors of negative or zero"
      os._exit(0)    
    for i in range(1,int(math.ceil(n/2))+1):
        if (n % i) == 0:
            l.append(i)
    l.append(n)
    return l


def isSqrt(n):
    xn = 1
    xn1 = (xn + (n/xn))/2
    while abs(xn1-xn) > 1:
        xn = xn1
        xn1 = (xn + (n/xn))/2

    while xn1 * xn1 > n:
        xn1 -= 1
    return xn1

#reverse a string
def revStr(s):
##    m=''  
##    for i in range(len(s)-1,-1,-1):
##       m += ''.join(s[i])
##    return m
##    
  rev=""
  for i in s:
    rev=i+rev
  return rev

#check if palindrome
def isPalindrome(s):
    i = 0
    j = len(str(s))-1
    k = math.ceil(len(str(s))/2)
    while i < k and j > k:
        if str(s)[i] != str(s)[j]:
          return "not a palindrome"
          break
        i += 1
        j -= 1
    return "is palindrome"

#capitalize letters given list/list of lists
def capT(s):
    x = []
    for i in s:
        if isinstance(i,list):
           x.append(capT(i))
        else:
            if isinstance(i,str):
              m = i.capitalize()
            else:
              m = i
            x.append(m)
            
    return x

#check if two words are anagrams 
def isAnagram(a,b):
   dictA = {i: a.count(i) for i in a}
   dictB = {i: b.count(i) for i in b}
   isAnagram = False
   matched = len(set(dictA.items()) ^ set(dictB.items())) == 0
   if matched:
       isAnagram = True
   return isAnagram == True

#read words from a file
#create a dictionary of anagrams
def fileAnagrams(fa):
    anagList =[]
    anagList1 = []
    anagDict = defaultdict(list)
    with open(fa,'r') as f:
        for i in f.readlines():
          anagList.append(i.rstrip())
          
    for i in range(len(anagList)-1):
        for j in range(i+1,len(anagList)-1):
           if isAnagram(anagList[i], anagList[j]):
              anagDict[anagList[i]].append(anagList[j])
              anagList1.append(anagList[j])
        anagList = filter(lambda x: x not in anagList1, anagList)        
    return anagDict
        
#print fileAnagrams("fileAnags.txt")   
#check if a list is sorted
def isSorted(s):
    i = 0
    j = len(s)
    k = math.ceil(len(s)/2)
    if len(s) > 2:
        while i <= k  and j >= k :
            if i == 0:
                if not s[i] < s[i+1]:
                    return "not sorted"
                    break
            elif j == -1:
                if not s[j] > s[j-1]:
                    return "not sorted"
                    break
            else:
                if not s[i-1] < s[i] < s[i+1] or \
                    not s[j-1] < s[j] < s[j+1]:
                    return "not sorted"
                    break
            i += 1
            j -= 1
        return "sorted"
    if len(s) == 2:
        if not s[0] < s[1]:
            return "not sorted"
            return

    return "sorted"

def cumulativeTotal(l):
    m = []
    i = 0
    if isinstance(l, list):
       for i in range(len(l)):
         if i == 0:
             m.append(l[0])
         else:
             m.append(m[i-1] + l[i])
                     
    return m

def cumulativeProduct(l):
  m = []
  i = 0
  if isinstance(l, list):
     for i in range(len(l)):
       if i == 0:
           m.append(l[0])
       else:
           m.append(m[i-1] * l[i])
                     
  return m

def removeDup(l):
    dups = defaultdict(int)
    for i in l:
        dups[i] += 1

    return [k for k, v in dups.iteritems() if v > 1]     

def islenSorted(l):
    isSorted = False
    for j in range(len(l) - 1):
         if len(l[j]) > len(l[j+1]):
          return isSorted
          break
    isSorted = True
    
    return isSorted
    
def sortList(l):
    for i in range(len(l)-1):
        if len(l[i]) > len(l[i+1]):
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
   
    if not islenSorted(l):        
        sortList(l)

    return l


def revFile(fa):
    lineFile = []
    rev = ""
    with open(fa,'r') as f:
      for i in f.readlines():
        rev = i+"\n"+rev
    return rev

#print revFile('fileRevData.txt')

def triplets(n):
    l = [(i,j,i+j) for i in range(1,n+1) for j in range(1,n+1) if \
         (i+j) <= n ]
    return [l[i] for i in range(len(l)-1) if l[i][i] <> l[i+1][i+1]]
           
    
def convert(text):
    return "".join(str(ord(char)) for char in text)

#print convert('python')
#print convert('jython')

##class A:
##    def f(self):
##        return self.g()
##
##    def g(self):
##        return 'A'
##
##class B(A):
##    def g(self):
##        return 'B'
##
##a = A()
##b = B()
#print b.g()

##try:
##    print "a"
###    raise Exception("doom")
##except:
##    print "b"
##else:
##    print "c"
##finally:
##    print "d"


##def f():
##    try:
##        print "a"
##        return
##    except:
##        print "b"
##    else:
##        print "c"
##    finally:
##        print "d"

def perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
                
##a=perms('ab')
##for i in a:
##    print i

def expF(x,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return expF(x*x, n/2)
    else:
        return x * expF(x,n-1)

def flatList(l, result=[]):
    for x in l:
        if isinstance(x,list):
           flatList(x,result)
        else:
           result.append(x)
    return result

def flatDict(d,result={}):
  m = {}
  ki =""
  for k,v in d.items():
      if isinstance(v,dict):
          for i,j in v.items():
             # ki = '%s.%s'%(k,i)
              m['%s.%s'%(k,i)] = j
          flatDict(m,result)
      else:
           result[k] = v
  #result = sorted(result,key=lambda key: result[key])
  return result

#print flatDict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})

def unflatDict(m):
  n = defaultdict(list)
  x = {}
  l = []
  for k,v in m.items():
      if len(k) > 1:
          n[k.split('.')[0]].append({k.split('.')[1]:v} )         
      else:
          n[k] = v
  return n

#print unflatDict({'a': 1, 'c': 4, 'b.x': 2,'b.y': 3})
       
def treemap(f,l):
    result = []
    for x in l:
        if isinstance(x,list):
           result.append(treemap(f,x))
        else:
           result.append(f(x))
    return result

#mult = lambda m: m*m
#print treemap(mult,[1, 2,[3, 4, [5]]])

##rev=""
##  for i in s:
##    rev=i+rev
##  return rev

def treeReverse(l):
    result = []
    for x in l:
        if isinstance(x,list):
           result.append(treeReverse(x))
        else:
           result[0] = x
    return result

#print treeReverse([[1, 2], [3, [4, 5]], 6])

def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in xrange(coin, amount + 1):
           ways[j] += ways[j - coin]
                       
    return ways
 
#print changes(100, [1,5])

def permu(xs):
    if xs:
      r , h = [],[]
      for x in xs:
        if x not in h:
          ts = xs[:];ts.remove(x)          
          for p in permu(ts):
             r.append([x]+p)          
          h.append(x)
          
      return r
    else:
      return [[]]

#print permu([1,2,3])

## l = [0 for i in range(amt+1)]
##    jd=[]
##    l[0] = 0
##    for i in range(1,amt+1):
##        temp = float('inf')
##        ctemp = float('inf')
##        for j in [c for c in d if  i >= c]:
##            temp = min(l[i-j],temp)
##        
##        l[i] = temp + 1
##    
    
def coinChange(amt,d):
    l = [0 for i in range(amt+1)]
    xl = [0 for i in range(amt+1)]
    l[0] = 0
    first, second = 0,0
    for i in range(1,amt+1):
        temp = float('inf')
        for j in (c for c in d if i >= c):
            temp = min(l[i-j],temp)
            if (l[i-j] == temp):
                xl[i] = j
            l[i] = temp + 1
    for i in xl:
        first = xl[amt]
        second = xl[first]
        
    print "Minimum Number of coins to get change: ",l[amt]
    print "\n The denominations are : (a) %d (b) %d " %(first,second)
    
coinChange(6,[1,3,4])


