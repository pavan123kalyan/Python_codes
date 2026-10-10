#unweighted graph
# 4 4
# 1 2
# 1 3
# 2 4
# 3 4
# The first line contains two integers n and e, where n is the number of vertices in the graph and e is the number of edges. The next e lines contain two integers u and v, representing an edge between vertices u and v.

n, e = map(int, input().split())
graph = [[] for i in range(n + 1)]
print(graph)
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
print(graph)

#weighted graph
# 4 4
# 1 2 5
# 1 3 2
# 2 4 7
# 3 4 1
n, e = map(int, input().split())
graph = [[] for i in range(n + 1)]
print(graph)
for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
print(graph)
#[[], [(2, 5), (3, 2)], [(1, 5), (4, 7)], [(1, 2), (4, 1)], [(2, 7), (3, 1)]]