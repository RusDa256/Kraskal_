import time

parent = []

def make_set(vertex):
    for i in range(vertex):
        parent.append(i)

def find_set(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find_set(parent[vertex])
    return parent[vertex]

def union_set(ver1, ver2):
    parent[ver1] = parent[ver2]

def kraskal(graph):
    mst = []
    graph.sort()
    make_set(graph_ver)

    for i in graph:
        w, v1, v2 = i
        v1Rep = find_set(v1)
        v2Rep = find_set(v2)
        if v1Rep != v2Rep:
            mst.append(i)
            union_set(v1Rep, v2Rep)
    return sorted(mst)

def print_mst(mst):
    for i in mst:
        print("Edge between (", i[1], ",", i[2], ") Weight: ", i[0])

if __name__ == "__main__":

    graph_list = []
    graph_ver = 6
    graph_list.append([2, 0, 1])
    graph_list.append([3, 0, 2])
    graph_list.append([1, 2, 3])
    graph_list.append([3, 1, 3])
    graph_list.append([2, 0, 3])
    graph_list.append([4, 2, 4])
    graph_list.append([5, 3, 4])
    graph_list.append([2, 1, 5])
    graph_list.append([4, 3, 5])
    graph_list.append([5, 0, 4])

    start_time = time.time()
    for i in range(1000):
        mst = kraskal(graph_list)
    end_time = time.time()

    print((end_time - start_time)/1000)
    print_mst(mst)