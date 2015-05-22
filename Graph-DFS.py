graph = {'G': set(['A','D','F']),
         'A': set(['B','D','G']),\
         'B': set(['A','E']),\
         'E': set(['B','F']),\
         'C' : set(['F']),\
         'D' : set(['A','G']),\
         'F': set(['G','C','E'])}

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
       vertex = stack.pop()       
       if not vertex in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

print "first method: ",dfs(graph, 'G')


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for a in graph[start]:
        if a not in visited:
          dfs(graph,a,visited)
    return visited

print "second method:", dfs(graph, 'G')

# without yield
def pathToGoal(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex]-set(path):
            if next == goal:
                temp =  path + [next]
                pathToGoal(graph,next,goal)
                print temp                                
            else:
                stack.append((next, path + [next]))

#pathToGoal(graph, 'A', 'F')

# with yield
def pathToGoalYield(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex,path) = stack.pop()
        if next in graph[vertex] - path:
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path +[next]))

#with reference arg
def pathToGoalReference(graph, start, goal, path=None):
    if path == None:
        path = [start]
    if start == goal:
        return path
    for next in graph[start] - set(path):
        print pathToGoalReference(graph, next, goal, path + [next])

#print pathToGoalReference(graph,'A','F')
#print 
            
    
