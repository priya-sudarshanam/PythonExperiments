import re

def uniqChar(d):
    duplicate = False
    s = [False] * 26
    for i in range(len(d)):
        if d[i] in s:
            duplicate = True
            return ("Duplicate: "+ str(duplicate))
        s[i] = d[i]
        
def revStr(s):
    rev = ""
    c = '\0'
    for i in s:
        rev = i + rev
    return c+rev

def anagram(a,b):
    dicta = {i:a.count(i) for i in a}
    dictb = {i:b.count(i) for i in b}
    isAnagram = False
    matched = len(set(dicta.items()) ^ set(dictb.items())) == 0
    if matched:
        isAnagram = True
    return isAnagram

def replaceSpace(d):
    return re.sub(r'\s','%20',d)

def isSubstring(a,b):
    return b in a

def isRotation(a,b):
    indexFirst = a.index(b[0])
    fullString = a+a
    return isSubstring(fullString,b)

def removeDuplicates(d):
    m = list(d)
    i = 0
    n = len(m)
    while i < n:
        if m[i] in m[:i]:
          del m[i]
          n -= 1
        else:
          i += 1
    return m

print removeDuplicates("ashacomaashacoma")
          
        


    
#print isRotation("waterbottlewaterbottle","erbottlewat")
#print replaceSpace("h e l l o")
