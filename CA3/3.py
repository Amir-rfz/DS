class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.leftChild = None
        self.rightChild = None


n = int(input())
nodes = []
children = []
for i in range(n):
    value, left, right = map(int, input().split())
    nodes.append(Node(i, value))
    children.append((left, right))

for i in range(n):
    if (children[i][0] != -1):
        nodes[i].leftChild = nodes[children[i][0] - 1]
    if (children[i][1] != -1):
        nodes[i].rightChild = nodes[children[i][1] - 1]


def showAllNode(node):
    if node is None:
        return []
    result = []
    result.append(node)
    if (node.leftChild is not None):
        result.extend(showAllNode(node.leftChild))
    if (node.rightChild is not None):
        result.extend(showAllNode(node.rightChild))
    return result


problematic_nodes = set()
count = 0
for node in nodes:
    allLeftNodes = showAllNode(node.leftChild)
    allRightNodes = showAllNode(node.rightChild)
    for leftNode in allLeftNodes:
        if leftNode.data > node.data:
            problematic_nodes.add(leftNode.id)
    for rightNode in allRightNodes:
        if rightNode.data < node.data:
            problematic_nodes.add(rightNode.id)

print(len(problematic_nodes))
