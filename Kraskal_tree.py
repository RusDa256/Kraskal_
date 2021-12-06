import time

def kraskal_tree(edges=[[0, 8, 5, 0, 0],
                    [8, 0 ,9 , 11, 0],
                    [5, 9, 0, 15, 10],
                    [0, 11, 15, 0, 7],
                    [0, 0, 10, 7, 0]]):

    w_edges = []
    name_edges = []

    for x in range(len(edges)):
        for y in range(len(edges[x])):
            if edges[x][y]:
                w_edges.append(edges[x][y])
                name_edges.append([x, y])

    def partition(w, names, low, high):
        pivot = w[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while w[i] < pivot:
                i += 1

            j -= 1
            while w[j] > pivot:
                j -= 1

            if i >= j:
                return j

            w[i], w[j] = w[j], w[i]
            names[i], names[j] = names[j], names[i]

    def quick_sort(w, names):  
        def _quick_sort(_w, names, low, high):
            if low < high:
                split_index = partition(_w, names, low, high)
                _quick_sort(_w, names, low, split_index)
                _quick_sort(_w, names, split_index + 1, high)

        _quick_sort(w, names, 0, len(w) - 1)

    quick_sort(w_edges, name_edges)

    parent = []
    mst = []

    for x in range(len(edges)):
        parent.append(str(x))

    for x in range(len(w_edges)):
        i = j = -1
        for y in range(len(parent)):
            if str(name_edges[x][0]) in parent[y]:
                i = y
            if str(name_edges[x][1]) in parent[y]:
                j = y

        if i != j:
            mst.append([name_edges[x], w_edges[x]])
            parent[i] += parent[j]
            parent.pop(j)
    
    return mst

def print_mst(mst):
    for i in mst:
        print("Edge between (", i[0][0], ",", i[0][1], ") Weight: ", i[1])


if __name__ == "__main__":

    n = 5
    graph = []

    for x in range(n):
        graph.append(input())

    for x in range(len(graph)):
        s = graph[x].split()
        graph[x] = []
        for y in s:
            graph[x].append(int(y)) 

    print_mst(kraskal_tree(graph))
    
    # start_time = time.time()
    # for i in range(1000):
    #     kraskal_tree(graph)
    # end_time = time.time()
    # print((end_time - start_time)/1000)

"""

0 3 2 1 1
3 0 5 0 4
2 5 0 3 7
1 0 3 0 2
1 4 7 2 0
__________

0 2 4 0 3 0
2 0 5 3 5 4
4 5 0 3 2 0
0 3 3 0 3 1
3 5 2 3 0 3
0 4 0 1 3 0
"""
