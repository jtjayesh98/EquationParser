
def searchNextNode(node, problemTree):
    if node.children_list == []:
        return node
    childHeuristic = []
    for currNode, heuristic in problemTree.heur:
        if currNode == node:
            childHeuristic = heuristic
    nodeChildren = node.children_list
    maxHeur = 0
    for i in childHeuristic:
        if i >= maxHeur:
            maxHeur = i
    return nodeChildren[childHeuristic.index(maxHeur)]
    

def searchTree(problemTree):
    node = problemTree.root
    while node.children_list != []:
        node = searchNextNode(node, problemTree)
    return node