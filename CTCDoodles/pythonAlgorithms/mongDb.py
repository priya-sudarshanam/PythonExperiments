from collections import defaultdict
def makeDict(txtFile):
     firstLine = True
     header = []
     d = {}
     lines = []
     m = []
     total = []
     with open(txtFile, 'r') as f:
         x = f.readlines()[0]
         for i in x.strip().split(","):
             header.append(i)
     with open(txtFile, 'r') as f:
         next(f)
         for i in f:
             lines.append(i.strip())
     for i in lines:
          m.append(i.rstrip().split(","))

     for i,j,k in zip(header,range(6),m):
          print k[0].split(",")
    #     total.append((header[j],k[0][j]))
     
     #print 
       
##     with open(txtFile, 'r') as f:
##     #    next(f)
##         for line,j in zip(f,range(6)):
##              elements = line.rstrip().split(",")
##             # print header
##              lines.append(dict(zip(header[j], elements[j])))
##     print lines
  #           lines.append(line.strip().split)
   #  for i in lines:
    #      print i.split(",")
   #  for i,j in zip(lines,range(6)):
          
         #  for i in range(6):
          #      if not header[i] in d:
       
               
         #  d #{header[i]: line.strip().split(",")[i] for line in f for i in range(6)}
               #   d[header[i]] = line.strip().split(",")[i]
               # else:
       #           d[header[i]] = (line.strip().split(",")[i])
     #print d             
    # for k,v in d.iteritems():
     #    print k,v
 
makeDict("MongoDBUdacity.txt")
