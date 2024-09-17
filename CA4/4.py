def topological_sort(graph):
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    n = len(graph)
    visited = [False] * n
    stack = []

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return stack[::-1]

def find_sorted_arrangement(n, a, edges):
    graph = [[] for k in range(0,n)]
    for i in range(n):
        for j in range(n):
            if edges[i][j] == 1:
                graph[i].append(j)

    from collections import defaultdict, deque

    def bfs(start):
        component = []
        visited.add(start)
        queue = deque([start])
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighborNode in graph[node]:
                if neighborNode not in visited:
                    queue.append(neighborNode)
                    visited.add(neighborNode)
        return component

    visited = set()
    components = []
    for i in range(n):
        if i not in visited:
            components.append(bfs(i))
            
    result = [5] * n
    for component in components:
        indices = sorted(component)
        values = sorted(a[i] for i in indices)
        for i in range(len(indices)):
            idx = indices[i]
            value = values[i]
            result[idx] = value

    return result

n = int(input())
a = list(map(int, input().split()))
edges = []
for l in range(n):
    row = list(map(int, input()))
    edges.append(row)

result = find_sorted_arrangement(n, a, edges)
print(*result)



