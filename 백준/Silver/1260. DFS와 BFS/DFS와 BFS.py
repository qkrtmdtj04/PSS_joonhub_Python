from collections import deque
N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1,N+1):
    graph[i].sort()



graph_check1 = [0 for _ in range(N+1)]
graph_check2 = [0 for _ in range(N+1)]

def DFS(v):
    graph_check1[v] = 1
    print(v,end=" ")
    for i in graph[v]:
         if graph_check1[i] == 0:
              DFS(i)

def BFS(v):
    q = deque([v])
    graph_check2[v] = 1
    while q:
         vv = q.popleft()
         print(vv, end=" ")
         for i in graph[vv]:
            if graph_check2[i] == 0:
                q.append(i)
                graph_check2[i] = 1
         
         
DFS(V)
print()
BFS(V)
