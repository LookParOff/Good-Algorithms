def arr_to_str(arr):
    return " ".join(list(map(str, arr)))


def TopoSort(lst_of_nei):
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


count_of_all_v = int(input())

lst_of_nei = [[] for _ in range(count_of_all_v)]
while True:
    try:
        edge = input().split()
        edge = list(map(int, edge))
        lst_of_nei[edge[0]].append(edge[1])
    except:
        break

for id, el in enumerate(lst_of_nei):
    lst_of_nei[id] = sorted(el)
print(lst_of_nei)
res = TopoSort(lst_of_nei)

print(arr_to_str(res))
