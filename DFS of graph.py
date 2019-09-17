# Обход графа в глубину
nv = int(input())  # number of vertices
ne = int(input())  # number of edges
# list of lists of neighbors
e = [[] for _ in range(nv + 1)]
# создание списка смежности
for _ in range(ne):
    # read edge from u to v
    u, v = map(int, input().split())
    # save edge to list
    e[u] += [v]
    # e[v] += [u]  Для неор графов разкоментить


def DFS(number_of_ver, lst_of_nei):
    start = 0

    stack = []
    white = 0  # 0 - white, not visited, not added to queue
    gray = 1  # 1 - gray, added to queue
    black = 2  # 2 - black, visited
    status = [white for _ in range(number_of_ver + 1)]

    # add start vertex
    stack += [start]
    status[start] = gray
    idx = 0
    while len(stack) != 0:
        # pop current vertex from queue
        vertex = stack[-1]
        stack.pop(-1)
        print(stack, vertex)
        status[vertex] = black
        idx += 1  # increase current vertex counter
        # ... here place your useful workload
        for neighbor in lst_of_nei[vertex]:
            if status[neighbor] is white:
                # add neighbor to queue if neighbor is white
                stack += [neighbor]
                status[neighbor] = gray

    print(stack)
