def dijkstra(count_of_vert, start_vert, matrix):
    valid = [True] * count_of_vert
    weight = [1000000] * count_of_vert
    weight[start_vert] = 0
    print(weight)
    for i in range(count_of_vert):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(count_of_vert):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight


print(dijkstra(2, 1, [[1, 0], [10, 1]]))