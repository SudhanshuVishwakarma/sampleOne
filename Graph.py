# # # # Adj matix
# # def add_node(v):
# #     global node_count
# #     if v in nodes:
# #         print(v, "is already present in the graph")
# #     else:
# #         node_count = node_count + 1
# #         nodes.append(v)
# #         for n in graph:
# #             n.append(0)
# #         temp = []
# #         for i in range(node_count):
# #             temp.append(0)
# #         graph.append(temp)


# # # undirected un-weighted
# # def add_edge(v1, v2):
# #     if v1 not in nodes:
# #         print(v1, "not present")
# #     elif v2 not in nodes:
# #         print(v2, "not present")
# #     else:
# #         index1 = nodes.index(v1)
# #         index2 = nodes.index(v2)
# #         graph[index1][index2] = 1
# #         graph[index2][index1] = 1


# # # directed weighted
# # def add_edge(v1, v2, cost):
# #     if v1 not in nodes:
# #         print(v1, " is not present")
# #     elif v2 not in nodes:
# #         print(v2, "is not present")
# #     else:
# #         index1 = nodes.index(v1)
# #         index2 = nodes.index(v2)
# #         graph[index1][index2] = cost
# #         # graph[index2][index1] = cost


# # def delete_edge(v1, v2):
# #     if v1 not in nodes:
# #         print(v1, " is not present")
# #     elif v2 not in nodes:
# #         print(v2, "is not present")
# #     else:
# #         index1 = nodes.index(v1)
# #         index2 = nodes.index(v2)
# #         graph[index1][index2] = 0
# #         # graph[index2][index1] = cost


# # def delete_node(v):
# #     global node_count
# #     if v not in nodes:
# #         print(v, "not present")
# #     else:
# #         index1 = nodes.index(v)
# #         node_count = node_count - 1
# #         nodes.remove(v)
# #         graph.pop(index1)
# #         for i in graph:
# #             i.pop(index1)


# # def print_graph():
# #     for i in range(node_count):
# #         for j in range(node_count):
# #             print(format(graph[i][j], "<3"), end=" ")
# #         print()


# # nodes = []
# # graph = []
# # node_count = 0
# # add_node("A")
# # add_node("D")
# # add_node("C")

# # add_edge("A", "C", 10)
# # add_edge("A", "D", 5)
# # add_edge("D", "C", 3)
# # delete_edge("D", "C")
# # delete_node("A")
# # delete_node("F")
# # print(nodes)
# # print(graph)
# # print_graph()


# # Adj list use to dictonary
# def add_node(v):
#     if v in graph:
#         print(v, " is alredy present in the graph")
#     else:
#         graph[v] = []


# # undirected un-weighted
# # def add_edge(v1, v2):
# #     if v1 not in graph:
# #         print(v1, "not present")
# #     elif v2 not in graph:
# #         print(v2, "not present")
# #     else:
# #         list1 = [v1]
# #         # for directed gp comment the next line
# #         list2 = [v2]

# #         graph[v1].append(list2)
# #         # for directed gp comment the next line
# #         graph[v2].append(list1)


# # directed weighted
# def add_edge(v1, v2, cost):
#     if v1 not in graph:
#         print(v1, "not present")
#     elif v2 not in graph:
#         print(v2, "not present")
#     else:
#         list1 = [v2, cost]
#         # for directed gp comment the next line
#         list2 = [v1, cost]

#         graph[v1].append(list1)
#         # for directed gp comment the next line
#         graph[v2].append(list2)


# # def delete_node(v):
# #     if v not in graph:
# #         print(v, "not present")
# #     else:
# #         graph.pop(v)
# #         for i in graph:
# #             list1 = graph[i]
# #             if v in list1:
# #                 list1.remove(v)


# def delete_node(v):
#     if v not in graph:
#         print(v, "not present")
#     else:
#         graph.pop(v)
#         for i in graph:
#             list1 = graph[i]
#             for j in list1:
#                 if v == j[0]:
#                     list1.remove(j)
#                     break


# def delete_edge(v1, v2, cost):
#     if v1 not in graph:
#         print(v1, "not present")
#     elif v2 not in graph:
#         print(v2, "not present")
#     else:
#         temp = [v1, cost]
#         temp1 = [v2, cost]
#         if temp1 in graph[v1]:
#             graph[v1].remove(temp1)
#             # For directed comment the next line
#             graph[v2].remove(temp)
#         else:
#             print("their so such edge present")


# graph = {}
# add_node("A")
# add_node("B")
# add_node("C")

# add_edge("A", "B", 2)
# add_edge("B", "C", 5)
# add_edge("C", "A", 8)

# delete_edge("A", "B", 1)

# # delete_node("B")

# print(graph)

# traversal operation
# DFS - depth frist search

# consider starting node as current node and visit that node
# visit the un-visited hsn code of the current node and make that mode as current note
# Follow Step 2 until we reach dead end
# If unvisited nodes are present in the graph then backtrack take recent visited mode as current node repeat Step 2

# DFS
# adj list reprensentation
# Recursion


# def DFS(Starting_Node, visited, graph):
#     # visit starting node ->A
#     # serach adj node A
#     # unvisited adj node of A(B)
#     # serach of adj node of B
#     # Unvisited adj node of B ..... contiue
#     if Starting_Node not in visited:
#         if Starting_Node not in graph:
#             print("node is not present in graph")
#             return
#         print(Starting_Node)
#         visited.add(node)
#         for i in graph[Starting_Node]:
#             # Recursion
#             DFS(i, visited, graph)


# visited = set()


def DFSiterattive(node, graph):
    visited = set()
    if node not in graph:
        print("Node is not present in the graph")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


DFSiterattive("A", graph)
