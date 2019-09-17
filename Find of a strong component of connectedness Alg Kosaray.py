def arr_to_str(arr):
    return " ".join(list(map(str, arr)))


def DFS_loop(lst_of_nei):
    tout = [0 for _ in range(len(lst_of_nei))]
    marks = [0 for _ in range(len(lst_of_nei))]
    for v in range(len(lst_of_nei)):
        if marks[v] == 0:
            DFS_rec(v, lst_of_nei, marks, tout)

    for i in range(len(tout)):
        tout[i] -= 1
    return tout


def DFS_rec(ver, lst_of_nei, marks, tout):
    marks[ver] = 1

    for nei in lst_of_nei[ver]:
        if marks[nei] == 0:
            DFS_rec(nei, lst_of_nei, marks, tout)

    tout[ver] = max(tout) + 1


def ReturnComponent(ver, lst_of_nei, marks, comp):
    marks[ver] = 1
    comp.append(ver)
    for nei in lst_of_nei[ver]:
        if marks[nei] == 0:
            ReturnComponent(nei, lst_of_nei, marks, comp)

    return comp


def transpose_graph(lst_of_nei):
    """
    >>> transpose_graph([[1], []])
    [[], [0]]

    >>> transpose_graph([[1], [2], [0]])
    [[2], [0], [1]]

    >>> transpose_graph([[1, 2, 3], [], [], []])
    [[], [0], [0], [0]]
    """
    new_lst_of_nei = [[] for _ in range(len(lst_of_nei))]
    for ind, neis in enumerate(lst_of_nei):
        for nei in neis:
            new_lst_of_nei[nei].append(ind)
    return new_lst_of_nei


def vertex_of_start(tout, marks):
    max_el = tout[0]
    ver_to_ret = -1
    for ver, el in enumerate(tout):
        if el >= max_el and marks[ver] == 0:
            max_el = el
            ver_to_ret = ver

    return ver_to_ret


def Kosaray(lst_of_nei):
    components = []
    tout = DFS_loop(lst_of_nei)
    lst_of_nei = transpose_graph(lst_of_nei)

    marks = [0 for _ in range(len(lst_of_nei))]

    for _ in range(len(lst_of_nei)):
        ver = vertex_of_start(tout, marks)
        comp = []
        if ver != -1:
            comp = ReturnComponent(ver, lst_of_nei, marks, comp)
            components.append(comp)
        else:
            break
    return components


# count_of_all_v = int(input())
# lst_of_nei = [[] for _ in range(count_of_all_v)]
# inv_lst_of_nei = [[] for _ in range(count_of_all_v)]
# while True:
#     try:
#         edge = input().split()
#         edge = list(map(int, edge))
#         lst_of_nei[edge[0]].append(edge[1])
#         inv_lst_of_nei[edge[1]].append(edge[0])
#     except:
#         break

lst_of_nei = [[], [], [3], [1, 4], [0, 2]]
res = Kosaray(lst_of_nei)

for el in res:
    print(el, end=" ")
