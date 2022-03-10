from oper import *

class Node:
    def __init__(self, data):
        self.data = data
        self.no_children = 0 
        self.children_list = []
        self.depth = 0
        self.visited = False
        self.hVisited = False
    def addChild(self, childNode):
       self.no_children = self.no_children + 1
       self.children_list.append(childNode)
       childNode.changeDepth(self.depth + 1)
    def changeDepth(self, depth):
        self.depth = depth
    def changeVisited(self):
        self.visited = True
    def changeHVisited(self):
        self.hVisited = True

class Tree:
    def __init__(self, rootNode):
        rootNode.changeDepth(0)
        self.root = rootNode
        self.depth = 0
        self.Nodes = [rootNode]
        self.heur = []
    def addNode(self, parentNode, childNode):
        parentNode.addChild(childNode)
        if childNode.depth > self.depth:
            self.depth = childNode.depth
        self.Nodes.append(childNode)
    def printChildren(self, node):
        for i in node.children_list:
            print(i.data)

class Heuristics:
    def __init__(self, tree):
        self.heuristic = []    
        tree.heur = self.heuristic
    def addHeuristic(self, data):
        if data != None:
            self.heuristic.append(data)

def addChild(problemTree, parentNode, childNode):
    problemTree.addNode(parentNode, childNode)


