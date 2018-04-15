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
    dicts = list()  # dictionary to store all dictionaries to return
    vertices = list(graph.keys())
    num_unique = 3**len(vertices)  # number of unique 3 color colorings
    num_v = len(vertices)  # number of unique vertices in the graph

    # Convert decimal to ternary number for all possible number of
    # colorings. Then add one to each value in the number to get the
    # colors for each vertex.
    for n in range(num_unique):
        nums = []  # list of remainders
        num = n    # number used to calculate ternary number
        if n == 0:
            nums.append(0)
        while num > 0:
            # divide by 3 and save result and remainder
            #n, r = divmod(n, 3)  # built-in method
            r = num % 3
            num = int(num / 3)
            nums.append(r)  # save all remainders
        # The reverse of the remainders is the ternary number.
        start = 0
        end = len(nums) - 1
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start = start + 1
            end = end - 1
        # Make sure the list is the same size for all.
        while len(nums) < num_v:
            nums.insert(0, 0)  # pad zeroes
        #print(nums)
        # Add one to each color.
        for i in range(len(nums)):
            nums[i] += 1
        print(nums)
        # Assign each value of the found number to the corresponding
        # vertex.
        tmp = dict()
        for i in range(num_v):
            v = vertices[i]  # vertex key
            value = nums[i]  # mapped vertex value for color
            tmp[v] = value   # add key/value pair
        dicts.append(tmp)  # add tmp dictionary to all dictionaries
        print(n)
        print(dicts[n])

    # for n in range(len(dicts)):
    #     print(dicts[n])

    # ??? returning in a list okay ???
    return dicts  # returned in a list


"""
Is Three Color:

This method takes a graph and determines whether the chromatic number is
at most three.
:param graph: a graph
:return: Boolean True if chromatic number is at most three
"""


def is_three_color(graph):



    return False

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

