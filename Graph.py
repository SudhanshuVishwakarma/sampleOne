# # # Adj matix
# def add_node(v):
#     global node_count
#     if v in nodes:
#         print(v, "is already present in the graph")
#     else:
#         node_count = node_count + 1
#         nodes.append(v)
#         for n in graph:
#             n.append(0)
#         temp = []
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)


# # undirected un-weighted
# def add_edge(v1, v2):
#     if v1 not in nodes:
#         print(v1, "not present")
#     elif v2 not in nodes:
#         print(v2, "not present")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = 1
#         graph[index2][index1] = 1


# # directed weighted
# def add_edge(v1, v2, cost):
#     if v1 not in nodes:
#         print(v1, " is not present")
#     elif v2 not in nodes:
#         print(v2, "is not present")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = cost
#         # graph[index2][index1] = cost


# def delete_edge(v1, v2):
#     if v1 not in nodes:
#         print(v1, " is not present")
#     elif v2 not in nodes:
#         print(v2, "is not present")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = 0
#         # graph[index2][index1] = cost


# def delete_node(v):
#     global node_count
#     if v not in nodes:
#         print(v, "not present")
#     else:
#         index1 = nodes.index(v)
#         node_count = node_count - 1
#         nodes.remove(v)
#         graph.pop(index1)
#         for i in graph:
#             i.pop(index1)


# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(format(graph[i][j], "<3"), end=" ")
#         print()


# nodes = []
# graph = []
# node_count = 0
# add_node("A")
# add_node("D")
# add_node("C")

# add_edge("A", "C", 10)
# add_edge("A", "D", 5)
# add_edge("D", "C", 3)
# delete_edge("D", "C")
# delete_node("A")
# delete_node("F")
# print(nodes)
# print(graph)
# print_graph()


# Adj list use to dictonary
def add_node(v):
    if v in graph:
        print(v, " is alredy present in the graph")
    else:
        graph[v] = []


# undirected un-weighted
def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "not present")
    elif v2 not in graph:
        print(v2, "not present")
    else:
        list1 = [v1, cost]
        # for directed gp comment the next line
        list2 = [v2, cost]

        graph[v1].append(list1)
        # for directed gp comment the next line
        graph[v2].append(list2)


def delete_node(v):
    if v not in graph:
        print(v, "not present")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)


graph = {}
add_node("A")
add_node("B")
add_node("C")


add_edge("A", "B", 10)
add_edge("A", "C", 5)


delete_node("B")

print(graph)
