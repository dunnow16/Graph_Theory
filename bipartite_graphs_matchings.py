import copy

"""
    Owen Dunn, MTH 325, 4/19/18, Project: 
    
    This project implements a number of functions related to .
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
    
    :param _list: a list
    :return: a set
"""


def make_set(_list):
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
    binary method  is used. The size of a set determines how many 
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


def power(_list):
    power_set = []  # always contains at least the null set

    # produce the set to use to produce the power set
    _set = make_set(_list)

    set_size = len(_set)  # used for binary solution

    # Using binary logic, each element is represented by a 1 or 0 if it
    # is in a subset of the powerset. Ex: 111 for {a, b, c} is subset
    # {a, b, c}
    # There are thus 2^n or 2 ** n (python code) or 1 << setSize total
    # subsets in the power set.
    # A left bit shift doubles the possibilities each time.
    for i in range(1 << set_size):
        if i == 0:
            tmp = []
            power_set.append(tmp)
            continue  # go to next i value or subset
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
    # line from: 6/15/17
    # https://stackoverflow.com/questions/4735704/ordering-a-list-of-lists-by-lists-len
    # sorts by sum of whole list if same size
    power_set = sorted(power_set, key=len)

    return power_set


"""
    Partite Sets method: 
    
    This method returns the partite sets of a bipartite graph.
    :param graph: a bipartite graph (dictionary type)
    :return: the two partite sets of the graph (as lists)
"""


def partite_sets(graph):
    # The partite sets are initialized.
    set1 = []
    set2 = []
    # A list of two sets: one for each partite set.
    sets = []
    vertices = list(graph.keys())

    if len(graph) == 0:  # check for empty graph
        return []
    if len(graph) == 1:
        return []

    # Add the first vertex to the first set.
    set1.append(vertices[0])
    # Check which partite set all remaining vertices belong to.
    # Using the assumption that the graph is bipartite:
    # This is done by checking if a vertex is adjacent to any vertices
    # in the first set. If the vertex is adjacent to a vertex in the
    # first set, it is appended to the second set. Adjacent vertices in
    # a bipartite graph cannot be part of the same partite set.
    # for v in vertices[1:]:  # second through last vertex
    #     for i in range(len(vertices)):
    #         if v in graph.get(vertices[i], []):
    #             set2.append(v)
    #             break  # check next vertex
    #     else:  # runs if break not reached in for loop
    #         set1.append(v)

    # For all the vertices, check if any of its neighbors or adjacent
    # vertices are in one of the two sets. If one neightbors of the
    # vertex is in a set, place the vertex in the other partite set.
    # Adjacent vertices can not be in the same partite set or else both
    # endpoints of an edge would be in the same partite set, which is
    # against definition of a bipartite graph.
    for v in vertices:
        neighbors = graph[v]
        for n in neighbors:
            if v not in set1:
                if n in set1:
                    set2.append(v)
                    break
            if v not in set2:
                if n in set2:
                    set1.append(v)
                    break

    # Return two lists or append to one list?
    return set1, set2
    # sets.append(set1)
    # sets.append(set2)
    #return sets


"""
Boolean Bipartite Check method:

This method checks is a graph is bipartite. 
:param graph: a graph that may or may not be bipartite
:return: Boolean: True if the graph is bipartite
"""


def is_bipartite(graph):
    # set1 = []  # vertex set 1
    # set2 = []  # vertex set 2
    vertices = list(graph.keys())
    q = copy.deepcopy(vertices)  # queue of all vertices
    colors = {vertices[0]: 0}  # 0 or 1 used (2 colors)

    if len(graph) <= 1:
        return True
    # set1.append(vertices[0])
    # Using coloring logic, with color 1 within set 1 and color 2 within
    # set 2, first add the first key/vertex to set 1. Then add all of
    # the neighbors of the vertex to set 2. Then iteratively go to the
    # neighbors and put all of the neighbors in the other set. If it is
    # found that this can't be done while maintaining only two colors or
    # having two bipartite sets, then the graph is not bipartite.
    # Go until all vertices have been colored or it is found a bipartite
    # graph is not possible.
    # Initialize vertex to check neighbors and index.
    i = 0
    v = vertices[0]  # color already initialized to 0
    #for v in vertices:
    #while len(colors) != len(graph):
    while not len(q) == 0:
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
                        print(colors)
                        return False
            q.remove(v)

        # Loop and repeat over all the vertices as needed.
        i = (i + 1) % len(vertices)
        v = vertices[i]
        print(q)

    print(colors)
    return True


"""
Boolean Perfect Matching method: 

This method determines if a bipartite graph (assumed) has a perfect
matching. True is returned if the graph has a perfect matching.
:param graph: a bipartite graph (assumed to be)
:return: Boolean: True if has a perfect matching
"""


def is_perfect(graph):


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
    print()

    print('test is_bipartite(graph)')
    print(is_bipartite({"A": ["B", "C"], "B": ["A"], "C": ["A"]}))
    print(is_bipartite({"A": ["B", "C"], "B": ["A", "C"],
                        "C": ["A", "B"]}))
    print()

    print('test is_perfect(graph)')
