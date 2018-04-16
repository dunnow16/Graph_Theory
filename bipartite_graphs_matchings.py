import copy

"""
    Owen Dunn, MTH 325, 4/19/18, Project 1: Bipartite Graphs and 
    Matchings 

    This project implements a number of functions related to bipartite
    graphs.
"""

print("Owen Dunn, MTH 325, 4/19/18")
print("Project 1: Bipartite Graphs and Matchings")

"""
    Set Producer function: Used with power() function.

    This function accepts a list. A set is made from the list and 
    returned. This function creates a set by only adding an element if 
    it is not a repeat. As each element is checked from a list, the set 
    in progress is checked if it already contains the element. If an 
    element is already in the set, the next element of the list is 
    considered until every list element has been checked.
    The set is actually a list data type in Python.

    :param _list: a list
    :return: a set
"""


def make_set(_list=[]):
    # I used underscores "_" before list and set variables to not
    # confuse/shadow with Python keywords.
    # first check if passed list any elements
    if len(_list) == 0:
        return []  # null set

    # make a new set to store elements
    _set = []

    # no repeats and unordered
    # check for repeats: don't add repeats to the set
    _set.append(_list[0])  # always add first element
    # go through each element of list and only add in not in set already
    # analyze second element to last element of list
    for e in _list[1:len(_list)]:
        if e not in _set:
            _set.append(e)

    return _set


'''
    Power Set Function:

    This function produces a power set from a list. First, the list is
    converted into a set. This set is then used to make its power set, 
    which contains all the subsets of the set. To find the power set, a 
    binary method is used. The size of a set determines how many 
    possible subsets it can have.

    For example, a set of 3 such as {1,3,5} has 2^3 = 8 possible 
    subsets. These subsets include the null set and every element of the 
    set, as well as everything in between. Thinking of the 2^(set size) 
    possible subsets in terms of binary representation allows you to 
    check if bits are 1 or 0, indicating if elements are contained 
    within the set. All 2^n possible subsets are found by noting that 
    for 3 elements, for example, the 8 possible subsets can be found by 
    using bit operators to see which of the 3 bits are 1. All bits that 
    are found to be one, for each 8, are added to a subset. The subset
    is added to the powerset once all bits are checked, before moving to 
    the next subset of 8. This logic carries for any set size. As the 
    count goes from 0 to 2^n - 1, the first subset is all 0's (null set) 
    and the final subset is all ones (ex: 2^3 - 1 = 7 = b111). Again, 
    bitwise operators are then used to find which elements should be 
    included in the subset (see comments for more detail).

    Several sources used, such as: 6/15/17
    http://www.geeksforgeeks.org/finding-all-subsets-of-a-given-set-in-java/

    :param _list: a list 
    :return: a power set of the list parameter
'''


def power(_list=[]):
    power_set = []  # always contains at least the null set

    # produce the set to use to produce the power set
    _set = make_set(_list)

    set_size = len(_set)  # used for binary solution

    # Using binary logic, each element is represented by a 1 or 0 if it
    # is in a subset of the power set. Ex: 111 for {a, b, c} is subset
    # {a, b, c}
    # There are thus 2^n or 2 ** n (python code) or (1 << setSize) total
    # subsets in the power set.
    # A left bit shift doubles the possibilities each time.
    for i in range(1 << set_size):
        if i == 0:  # add the null set
            tmp = []
            power_set.append(tmp)
        else:
            tmp = []
            j = 1  # used to check if a bit is 1 for all bits
            # 'pos' is used to index element of the set: each time the
            # bit is shifted, the next possible index or set element is
            # in the subset when the if conditional is met
            pos = 0  # used to index elements of set (position)
            while j < (1 << set_size):
                if (j & i) > 0:
                    tmp.append(_set[pos])
                # shift the bit to check if next element is in subset
                j = j << 1
                pos += 1
            power_set.append(tmp)

    # Sort the power set to be in the familiar logical order as if done
    # by a human.
    power_set = sorted(power_set, key=len)

    return power_set


"""
    Partite Sets method: 

    This method returns the partite sets of a bipartite graph.
    :param graph: a bipartite graph (dictionary type)
    :return: the two partite sets of the graph (as lists)
"""


def partite_sets(graph={}):
    # The partite sets are initialized.
    set1 = list()
    set2 = list()
    vertices = list(graph.keys())
    q = copy.deepcopy(vertices)  # queue of vertices

    if len(graph) == 0:  # check for empty graph
        return list(), list()
    if len(graph) == 1:
        return list(graph.keys()), list()

    # For all the vertices, check if any of its neighbors or adjacent
    # vertices are in one of the two sets. If one neightbors of the
    # vertex is in a set, place the vertex in the other partite set.
    # Adjacent vertices can not be in the same partite set or else both
    # endpoints of an edge would be in the same partite set, which is
    # against definition of a bipartite graph.
    i = 0            # initial index of vertices
    v = vertices[0]  # the initial vertex
    set1.append(v)   # add the first vertex to the first partite set
    q.remove(v)      # remove the first vertex from the queue
    while len(q) > 0:  # Run until found a place for all vertices.
        neighbors = graph[v]  # adjacent vertices of vertex v
        # Don't waste time if already found partite set for vertex.
        if v in q:  # if vertex is in the queue
            for n in neighbors:
                if n in set1:
                    set2.append(v)
                    q.remove(v)
                    break
                elif n in set2:
                    set1.append(v)
                    q.remove(v)
                    break

        # cycle and re-try vertices as needed
        i = (i + 1) % len(vertices)
        v = vertices[i]

    return set1, set2  # returns tuples (can't be changed)


"""
Boolean Bipartite Check method:

This method checks if a graph is bipartite. 
:param graph: a graph that may or may not be bipartite
:return: True if the graph is bipartite
"""


def is_bipartite(graph={}):
    vertices = list(graph.keys())  # vertices of the graph
    q = copy.deepcopy(vertices)    # queue of all vertices
    colors = {vertices[0]: 0}      # 0 or 1 used (2 colors)

    if len(graph) <= 1:
        return True

    # Using coloring logic, assign colors to vertices. First assign
    # color 1 to the initial vertex. Then iteratively go to the
    # neighbors and give them all the other color if they have not been
    # assigned a color. If it is found that this can't be done while
    # maintaining only two colors or having two bipartite sets, then the
    # graph is not bipartite. Go until all vertices have been colored or
    # it is found a bipartite graph is not possible.
    # Initialize vertex to check neighbors and index.
    i = 0              # initial index
    v = vertices[0]    # color already initialized to 0
    while len(q) > 0:  # go until the queue has been emptied
        neighbors = graph[v]  # neighbors of vertex v
        if v in colors and v in q:
            for n in neighbors:  # Color all neighbors the other color.
                if n not in colors:
                    if colors[v] == 0:
                        colors[n] = 1  # adds new key to dictionary
                    elif colors[v] == 1:
                        colors[n] = 0
                else:
                    # Does a neighbor have same color?
                    if colors[v] == colors[n]:
                        #print(colors)
                        return False
            q.remove(v)  # remove vertex v from the queue

        # Loop and repeat over all the vertices as needed.
        i = (i + 1) % len(vertices)
        v = vertices[i]
        #print(q)

    #print(colors)
    # No adjacent vertices were found to have the same color, so the
    # graph is therefore bipartite.
    return True


"""
Boolean Perfect Matching method: 

This method determines if a bipartite graph (assumed) has a perfect
matching. True is returned if the graph has a perfect matching.
Hall's Theorem is used. 
:param graph: a bipartite graph (assumed to be)
:return: True if graph has a perfect matching
"""


def is_perfect(graph):
    # Get the partite sets of the bipartite graph.
    X, Y = partite_sets(graph)

    # Halls Theorem:
    # Check the size of the neighborhood for each subset of each partite
    # set. The size of the union of neighborhoods should be greater than
    # or equal to the size of the subset for each subset of the partite
    # sets.
    # Find all subsets (power set) of each partite set.
    A = power(X)
    B = power(Y)
    # print(X)
    # print(A)
    # print(Y)
    # print(B)

    n = []                  # union of neighborhoods of a subset
    for s in A:             # for all subsets of partite set X
        for v in s:         # for all vertices in the subset
            tmp = graph[v]  # neighbors of vertex v
            for t in tmp:   # for all neighbors of vertex v
                # if union of neighbors doesn't contain vertex
                if t not in n:
                    n.append(t)  # add to union of neighbors
        # if size of union of neighborhoods is less than size of subset
        if len(n) < len(s):
            return False
        n = []  # reset the union of neighborhoods

    for s in B:  # for all subsets of partite set Y
        for v in s:  # for all vertices in the subset
            tmp = graph[v]  # neighbors of vertex v
            for t in tmp:
                if t not in n:
                    n.append(t)
        # if size of union of neighborhoods is less than size of subset
        if len(n) < len(s):
            return False
        n = []  # reset the union of neighborhoods

    # Size of union of neighborhoods for all subsets of partite sets
    # found to be at least as large as the subset itself.
    return True


"""
Test all the functions from the project.
"""

if __name__ == "__main__":
    """
    Test all the functions from the project.
    """
    print('test power(list)')
    print(power([1, 3, 5]))
    print(power([1, 1, 1]))
    print(power([0, 1, 2, 3, 4]))
    print(power(["A", "B"]))
    print(power(["A", "B", "C"]))
    print()

    print('test partite_sets(graph)')
    print(partite_sets({"A": ["B", "C"], "B": ["A"], "C": ["A"]}))
    print(partite_sets({"A": ["B", "C"], "B": ["A", "D"],
                        "C": ["A", "D"], "D": ["B", "C"]}))
    print(partite_sets({'A': ['B', 'F'], 'B': ['A', 'C'],
                        'C': ['B', 'D'], 'D': ['C', 'E'],
                        'E': ['D', 'F'], 'F': ['A', 'E']}))
    print()

    print('test is_bipartite(graph)')
    print(is_bipartite({"A": ["B", "C"], "B": ["A"], "C": ["A"]}))  # T
    print(is_bipartite({"A": ["B", "C"], "B": ["A", "C"],
                        "C": ["A", "B"]}))  # F
    print(is_bipartite({"A": ["B", "C"], "B": ["A", "D"],
                        "C": ["A", "D"], "D": ["B", "C"]}))  # T
    print(is_bipartite({'A': ['B', 'F'], 'B': ['A', 'C'],
                        'C': ['B', 'D'], 'D': ['C', 'E'],
                        'E': ['D', 'F'], 'F': ['A', 'E']}))  # T
    print()

    print('test is_perfect(graph)')
    print(is_perfect({'A': ['B', 'C'], 'B': ['A', 'D'],
                      'C': ['A', 'D'], 'D': ['B', 'C']}))  # T
    print(is_perfect({'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}))  # F
    print(is_perfect({'A': ['B', 'F'], 'B': ['A', 'C'],
                      'C': ['B', 'D'], 'D': ['C', 'E'],
                      'E': ['D', 'F'], 'F': ['A', 'E']}))  # T
    print(is_perfect({'A': ['E', 'F'], 'B': ['D', 'E'], 'C': ['D', 'F'],
                      'D': ['B', 'C'], 'E': ['A', 'B'],
                      'F': ['A', 'C']}))  # T
    print()
