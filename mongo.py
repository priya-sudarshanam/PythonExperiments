def makeDict(txtFile):
     data = []
     with open(txtFile, 'rb') as f:
         x = f.readline().split(",")
         ctr = 0
         for line in f:
             fields = line.split(",")
             entry = {}
             if ctr == 3:
                 break

             data = [{entry[x[i].strip()] : value.strip() for i,value in enumerate(fields)}]
          #   data.append(entry)
             ctr += 1
     print data
makeDict("MongoDBUdacity.txt")
