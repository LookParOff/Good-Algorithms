def arr_to_str(arr):
    return " ".join(list(map(str, arr)))


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, el):
        self.queue.append(el)

    def get(self):
        return self.queue.pop(0)

    def empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return " ".join(list(map(str, self.queue)))


def delete_ver_from_graph(graph, vertex, degrees):
    for el in sorted(graph[vertex]):
        degrees[el] -= 1
        if degrees[el] == 0:
            v_with_deg_0.put(el)


count_of_all_v = int(input())

degrees_of_v = [0 for _ in range(count_of_all_v)]
lst_of_nei = [[] for _ in range(count_of_all_v)]

while True:
    try:
        edge = input().split()
        edge = list(map(int, edge))
        lst_of_nei[edge[0]].append(edge[1])
        degrees_of_v[edge[1]] += 1

    except EOFError:
        break

v_with_deg_0 = Queue()

for ind, el in enumerate(degrees_of_v):
    if el == 0:
        v_with_deg_0.put(ind)

to_print = []
cycle = False

for i in range(count_of_all_v):
    if v_with_deg_0.empty():
        cycle = True
        break
    print(arr_to_str(degrees_of_v))
    print(v_with_deg_0)
    v = v_with_deg_0.get()
    delete_ver_from_graph(lst_of_nei, v, degrees_of_v)
    to_print.append(v)

if not cycle:
    print(arr_to_str(to_print[::-1]))
else:
    print(None)
