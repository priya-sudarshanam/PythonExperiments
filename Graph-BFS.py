graph = {'A': set(['B','D','G']),\
         'B': set(['E','A']),\
         'C' : set(['F']),\
         'D' : set(['A','G']),\
         'E': set(['B','F']),\
         'F': set(['E','C','G']),\
         'G': set(['A','D','F'])}

def bfs(graph, start):
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
    #    print vertex
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited))
    return visited


#print bfs(graph, 'G')

def pathToGoalYield(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
          if next == goal:
              yield path + [next]
          else:
              queue.append((next, path + [next]))


def pathToGoalRef(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start]-set(path):
        yield pathToGoalRef(graph,next,goal,path +[next])

#print list(pathToGoalRef(graph,'G','C'))
  

def shortestPath(graph,start,goal):
    try:
        return next(pathToGoalYield(graph,start,goal))
    except StopIteration:
        return None

print shortestPath(graph,'C','B')

    
#print list(pathToGoalYield(graph, 'A', 'E'))


