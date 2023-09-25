# A class to define a tree DS

# Date   : 25-09-2023
# Written by: JAM

class TreeNode(object):
    def __init__(self: object, data: any, children:list = []):
        self.data = data
        self.children = children

    def __str__(self: object, level: int = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self: object, TreeNode: object):
        self.children.append(TreeNode)

tree = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot  = TreeNode("Hot", [])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode("Tea", [])
coffee  = TreeNode("Coffee", [])
fanta = TreeNode("Fanta", [])
cola  = TreeNode("Cola", [])
cold.addChild(fanta)
cold.addChild(cola)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)