# A class to define an AVL tree DS with LL

# data   : 27-09-2023
# Written by: JAM 

class TrieNode(object):
    # Define tree node object
    def __init__(self: object):
        self.children = {}
        self.endOfString = False

class Trie(object):
    def __init__(self: object):
        self.rootNode = TrieNode()

    def insertString(self: object, string: str):
        currNode = self.rootNode
        for i in string:
            node = currNode.children.get(i)
            if node is None:
                node = TrieNode()
                currNode.children.update({i:node})
            currNode = node
        currNode.endOfString = True
        return True
    
    def searchString(self: object, string: str):
        currNode = self.rootNode
        for i in string:
            node = currNode.children.get(i)
            if node is None:
                return False
            currNode = node
        if currNode.endOfString == True:
            return True
        else:
            return False
        
def deleteString(rootNode: object, string: str, index: int): # index is where to start the deletion of the words from
    char = string[index]
    currNode = rootNode.children.get(char)
    deletion = False
    # if the string is a prefix to another string
    if len(currNode.children) > 1:
        deleteString(currNode, string, index + 1)
        return False
    # at last char of word but string is prefix to another string so just remove endOf String
    if index == len(string) - 1:
        if len(currNode.children) >= 1:
            currNode.endOfString = False
            return False
        # if node not dependent on other strings remove node
        else:
            rootNode.children.pop(char)
            return True
    # Another string remaing is a prefix of this string
    if currNode.endOfString is True:
        deleteString(currNode, string, index + 1)
        return False
    # string nodes has no dependencies on other strings
    deletion = deleteString(currNode, string, index + 1)
    if deletion is True:
        rootNode.children.pop(char)
        return True
    else:
        return False


newTrie = Trie()
print(newTrie.insertString("App"))
print(newTrie.insertString("Apple"))
print(newTrie.searchString("App"))
print(newTrie.searchString("Ap"))
# deleteString(newTrie.rootNode, "App", 0)
# print(newTrie.searchString("App"))
print(newTrie.rootNode.children.get("A").children)
print(len(newTrie.rootNode.children))