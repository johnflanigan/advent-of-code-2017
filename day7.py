import re


class Node(object):
    def __init__(self, key, weight, childrenKeys):
        self.key = key
        self.weight = weight
        self.childrenKeys = childrenKeys
        self.childrenRefs = []
        self.childrenCopies = None
        self.processed = False
        self.parent = None


def recursiveCircus():
    f = open("day7_input.txt", "r")
    nodes = []
    for line in f:
        m = re.match(r"(\w+) \((\d+)\)(?: -> )?(.*)", line)
        nodes.append(Node(m.group(1), int(m.group(2)), m.group(3).split(', ')))
    # probably a better way to do this...
    for node in nodes:
        if node.childrenKeys != ['']:
            for childKey in node.childrenKeys:
                for current in nodes:
                    if current.key == childKey:
                        current.parent = node
                        node.childrenRefs.append(current)
    for node in nodes:
        node.childrenCopies = list(node.childrenRefs)
    for i in range(0, len(nodes)):
        for node in nodes:
            if node.childrenCopies == [] and not node.processed and node.parent != None:
                node.parent.weight += node.weight
                node.parent.childrenCopies.remove(node)
                node.processed = True
    unbalancedNodes = []
    for node in nodes:
        if node.childrenRefs != []:
            weights = []
            for child in node.childrenRefs:
                weights.append(child.weight)
            modeWeight = max(weights, key=weights.count)
            for child in node.childrenRefs:
                if child.weight != modeWeight:
                    unbalancedNodes.append((child, modeWeight))
    lightest = unbalancedNodes[0]
    for node in unbalancedNodes:
        if node[0].weight < lightest[0].weight:
            lightest = node
    lightestNode = lightest[0]
    modeWeight = lightest[1]
    for child in lightestNode.childrenRefs:
        modeWeight -= child.weight
    return modeWeight


print recursiveCircus()
