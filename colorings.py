import copy

"""
    Owen Dunn, MTH 325, 4/19/18, Project: 

    This project implements a number of functions related to .
"""

print("Owen Dunn, MTH 325, 4/19/18")
print("Project 2: Colorings")

"""

"""


def is_proper(graph, color):
    vertices = list(graph.keys())

    # If the difference of the sets is not null, there is not a color
    # for each vertex.
    if set(color.keys()) - set(vertices) != set():
        print('Error: There must be a color for each vertex.')
        return

    for v in vertices:
        v_color = color[v]
        neighbors = graph[v]
        # Check if any of the vertex neighbors have the same color.
        for n in neighbors:
            if v_color == color[n]:
                return False

    # All adjacent vertex colors found to be different.
    return True


"""
Three Color:

This method takes a graph as input and returns all possible three color
vertex colorings. 
:param graph: a graph
:return: all possible dictionaries of vertex colorings
"""


def three_color(graph):
    




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

