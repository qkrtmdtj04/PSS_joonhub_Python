N = int(input() )
M = int(input() )
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1,N+1):
    graph[i].sort()



graph_check1 = [0 for _ in range(N+1)]

def DFS(v):
    graph_check1[v] = 1
    for i in graph[v]:
         if graph_check1[i] == 0:
              DFS(i)
                  
                  
         
DFS(1)
print(graph_check1.count(1)-1)