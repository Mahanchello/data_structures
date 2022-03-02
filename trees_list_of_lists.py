"""
         a
        /  \
       b    c
      / \   |
     d   e  f    
"""
# implementation of the above tree
myTree = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]] # list of lists representation
# print('root:', myTree[0])
# print('left subtree:', myTree[1])
# print('right subtreeL', myTree[2])

def BinaryTree(r):
    return[r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])   
    return root

def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, t, []])
    else:
        root.insert(2, [newBranch, [], []])  
    return root    

def getRootValue(root):
    return root[0]

def setRootValue(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


r = BinaryTree(3)
insertLeft(r, 4)
insertRight(r, 5)
insertLeft(r, 8)
insertRight(r, 10)
l = getLeftChild(r)
print(l)
setRootValue(l, 9)
print(r)
insertLeft(l, 11)
print(r)
print(getRightChild(getRightChild(r)))





