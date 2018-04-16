import copy

"""
    Owen Dunn, MTH 325, 4/19/18, Project 2: Colorings

    This project implements a number of functions related to coloring.
"""

print("Owen Dunn, MTH 325, 4/19/18")
print("Project 2: Colorings")

"""
Is Proper:

This method determines whether or not the labeling is a proper vertex
coloring of the given graph.
:param graph: a graph
:param color: a corresponding vertex coloring of the graph
:return: Return True if found to be a proper vertex coloring
"""


def is_proper(graph={}, color={}):
    vertices = list(graph.keys())

    # If the difference of the sets is not null, there is not a color
    # for each vertex.
    if set(color.keys()) - set(vertices) != set():
        print('Error: There must be a color for each vertex.')
        return
    if len(graph) == 0 or len(color) == 0:
        print('You must provide a graph and coloring.')
    if len(graph) == 1:  # a single vertex is proper if it has a color
        return True

    for v in vertices:  # for all vertices in the graph
        v_color = color[v]    # the vertex's color
        neighbors = graph[v]  # the neighbors of the vertex
        # Check if any of the vertex neighbors have the same color.
        for n in neighbors:
            if v_color == color[n]:
                return False

    # All adjacent vertex colors found to be different.
    return True


"""
Three Color:

This method takes a graph as input and returns all possible three color
vertex-colorings (not necessarily proper) of that graph. 
:param graph: a graph
:return: all possible dictionaries of vertex colorings in a list
"""


def three_color(graph={}):
    dicts = list()  # dictionary to store all dictionaries to return
    vertices = list(graph.keys())  # vertices of the graph
    num_unique = 3**len(vertices)  # number of unique 3 color colorings
    num_v = len(vertices)  # number of unique vertices in the graph

    if len(graph) == 0:
        print('You must provide a graph.')

    # Convert decimal to ternary number for all possible number of
    # colorings. Then add one to each value/digit in the number to get
    # the colors for each vertex.
    for n in range(num_unique):
        nums = list()  # list of remainders
        num = n        # number used to calculate ternary number
        if n == 0:
            nums.append(0)
        while num > 0:
            # divide by 3 and save result and remainder
            r = num % 3         # remainder
            num = int(num / 3)  # truncate to integer
            nums.append(r)      # save all remainders
        # The reverse of the remainders is the ternary number.
        # Reverse the order of the remainder list.
        start = 0
        end = len(nums) - 1
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start = start + 1
            end = end - 1
        # Make sure the list is the same size for all numbers.
        while len(nums) < num_v:
            nums.insert(0, 0)  # pad zeroes
        #print(nums)
        # Add one to each color (starts at 1, not 0).
        for i in range(len(nums)):
            nums[i] = nums[i] + 1
        #print(nums)
        # Assign each value of the found number to the corresponding
        # vertex for color assignment.
        tmp = dict()
        for i in range(num_v):
            v = vertices[i]  # vertex key
            value = nums[i]  # mapped vertex value for color
            tmp[v] = value   # add key/value pair to dictionary
        dicts.append(tmp)    # add tmp dictionary to dictionaries list
        #print(n)
        #print(dicts[n])

    # for n in range(len(dicts)):
    #     print(dicts[n])

    return dicts  # returned in a list


"""
Is Three Color:

This method takes a graph and determines whether the chromatic number is
at most three.
:param graph: a graph
:return: True if chromatic number is at most three
"""


def is_three_color(graph={}):
    # Get a list of all possible 3 color vertex-colorings dictionaries
    # for the graph.
    dicts = three_color(graph)

    if len(graph) == 0:
        print('You must provide a graph.')
        return

    # Check if any of the possible 3 color vertex-colorings is a proper
    # vertex coloring for the graph.
    for d in dicts:
        if is_proper(graph, d):
            return True

    # No proper 3 color vertex-coloring found for the graph.
    return False


"""
Is Proper Edge:

This method determines if the edge labeling of a graph is a proper
edge-coloring.
:param graph: a weighted graph (has all edges labeled) 
:return: True if the graph is a proper edge-coloring 
"""


def is_proper_edge(graph={}):
    vertices = list(graph.keys())  # all graph vertices
    colors = list(graph.values())  # all edge colorings
    #print(vertices)
    #print(colors)

    if len(graph) == 0:
        print('You must provide a weighted graph.')
        return
    if len(graph) == 1:
        return True  # a single edge with a color is proper

    for i in range(len(vertices)):  # Go for each vertex.
        v = vertices[i]    # a vertex to consider its edges
        edges = colors[i]  # edges of vertex v
        for j in range(len(edges)):  # Go for each edge.
            tmp = edges[j]     # one of the edges
            v_adj = tmp[0]     # adjacent vertex to v
            color_v = tmp[1]   # color value of edge
            # Check the graph for the adjacent vertex's edges.
            edges_adj = graph[v_adj]
            # Check if any edges of the adjacent vertex have the same
            # color (incident edges of same color).
            for k in range(len(edges_adj)):
                tmp = edges_adj[k]
                if tmp[0] != v:  # if not the same edge
                    # If two incident edges have the same color.
                    if color_v == tmp[1]:
                        return False

    # No incident edges were found to have the same color.
    return True


"""
Greedy:

This method takes a graph and an ordering of vertices (of the graph) and
returns the proper vertex-coloring produced by the greedy algorithm.
:param graph: a graph
:param order: an ordering of vertices of the graph
:return: a proper vertex coloring
"""


def greedy(graph={}, order={}):
    color = dict()  # the coloring dictionary for all vertices

    if len(order) == 0:
        print('You must provide an ordering of vertices.')
        return {}
    if len(graph) == 0:
        print('You must provide a graph.')
        return {}
    if set(graph.keys()) - set(order) != set():
        print('You must provide an ordering of all vertices.')
        return {}
    if len(order) == 1:
        return {order[0]: 1}

    # Assign colors to each vertex in the order in sequence.
    # First assign the first vertex of the order color 1.
    color[order[0]] = 1
    # Assign colors to the rest of the vertices.
    for v in order[1:]:
        neighbors = graph[v]  # neighbors of vertex v
        # Check color for all neighbors of vertex v.
        n_colors = list()  # list of neighbor colors
        for n in neighbors:
            if n in color:
                n_colors.append(color[n])
        if len(n_colors) == 0:  # if no neighbors have a color assigned
            color[v] = 1
        else:
            colored = False  # True when color assigned for given vertex
            # color to assign to vertex v if not given to a neighbor
            c = 1
            while not colored:
                if c not in n_colors:
                    color[v] = c
                    colored = True
                c = c + 1  # try the next color

    # Return the completed proper vertex coloring sorted by letter.
    return dict(sorted(color.items()))


if __name__ == "__main__":
    """
    Test all the functions from the project.
    """
    print('test is_proper(graph, color)')
    print(is_proper({'A': ['B', 'C'], 'B': ['A', 'C'],
                     'C': ['A', 'B']},
                    {'A': 1, 'B': 2, 'C': 3}))  # T
    print(is_proper({'A': ['B', 'C'], 'B': ['A', 'C'],
                     'C': ['A', 'B']},
                    {'A': 1, 'B': 1, 'C': 3}))  # F
    print()
    print('test three_color(graph)')
    print(three_color({'A': ['B'], 'B': ['A']}))
    print()
    print('test is_three_color(graph)')
    print(is_three_color({'A': ['B', 'C'], 'B': ['A', 'C'],
                          'C': ['A', 'B']}))  # T
    print(is_three_color({'A': ['B', 'C', 'D'], 'B': ['A', 'C', 'D'],
                          'C': ['A', 'B', 'D'], 'D': ['A', 'B', 'C']}))
    # F
    print()
    print('test is_proper_edge(graph)')
    print(is_proper_edge({'A': [['B', 1], ['C', 2]],
                          'B': [['A', 1], ['C', 3]],
                          'C': [['A', 2], ['B', 3]]}))  # T
    print(is_proper_edge({'A': [['B', 1], ['C', 2]],
                          'B': [['A', 1], ['C', 2]],
                          'C': [['A', 2], ['B', 2]]}))  # F
    print()
    print('test greedy(graph, order)')
    print(greedy({'A': ['B', 'C'], 'B': ['A'], 'C': ['A']},
                 ['A', 'B', 'C']))
    print(greedy({'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D'],
                  'D': ['C']}, ['A', 'D', 'B', 'C']))
