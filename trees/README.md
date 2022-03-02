# Trees 

**Tree** is a type of graph. When we talk about a tree we are referring to a graph structure that is rooted, meaning it has a root node or top node of the structure. Root node has child nodes. The structure is directed, because edges point downwards of the tree. Tree structure is acyclic. Each child node can have only one parent node. The tree is no allowed to be disconnected. 

The most common type of tree is **binary tree**. Binary tree is a normal tree, where each node has at at most two child nodes.  

**Ternary tree** when each node has at most three child nodes. 

**K-ary trees** are trees where each node has at most k nodes. 

**Binary search tree** or **BST** is a special type of a tree where every node satisfies a special **BST** property. 
**Min/max heaps** is a special type of the three where each node satisfies min or max heap property. 
**Tries** is a tree type data structure that typically stores characters in a string. 
**Balanced tree** is a tree that mantains O(log n) time complexity for the one path/sub-tree traversal. It's when we have more or less same amount of branches on the left and on the right from the root node. 

**Node** - is fundamental part of the tree. It can have a name called "key". A node cam also have an additional information that can be called *payload*.  
**Edge** - connects two nodes to show that there is a relasinship between them. Every node (except the root) is connected by exactly one incoming edge fron another node. Each node may have several outgoing edges. 
**Root** - the root of the tree is the only node in the tree that has no incoming edges. 
**Path** is ordered list of nodes that are connected by edges. 
**Subtree** is set of nodes and edges consisted of a parent and all the descendants of that parent. 
**Level** - the level of the node is the number of edges on the path from root node to n.
**Height** is equal to the maximum level of any node in the tree. 
Every path that starts from the top of the tree till the bottom of tree is called **branch**. 
Bottom nodes are called **leaf** nodes. 
Every tree has levels of the nodes. 
**Full binary tree** - it's a tree where leaf nodes have no children or a node has two children. If a node has children, it should be two children all the time, node can not have only one child to call the tree **full tree**. 
Example of  full tree:
```
    *
  /   \
 *     *
      / \
     *   *
    / \
   *   *
```

The tree is **complete** where every single level of the tree is filled up except the final level that may or may not be filled up. But if the final level has nodes, they should be filled up from left to right. So at the final level we can't have branch wihout a node. (The main thing is nodes filled up from left ro right). 
Example of complete tree:
```
        *
      /   \
     *     *
    / \   / \
   *   * *   *
  / \
 *   *
``` 

The tree is **full** if every node in the tree has either no children nodes or k-children nodes. 
**Perfect tree** is a tree where all the leaf nodes has the same depth (same amount of the number of levels).
Example of the perfect binary tree:
```
            *
       /        \
      *          *
    /  \       /   \ 
   *    *     *     *
  / \  / \   / \   / \
 *  * *   * *   *  *  *
```
Operations and complexity: 
- storing a tree: O(N) space complexity 
- traversing through the entire tree: O(n) time complexity 
- traversing a tree going one path (sub-tree) instead of two paths: O(log n) time complexity for balanced trees only 

There are three ways to **depth first traverse binary tree**: 
Prefix tells us when we will visit the node. 
- **Pre**order - **n**lr (first we visit node, then left subtree, then right subtree) 
- **In**order - l**n**r (first we visit left subtree, then node, then right subtree)
- **Post**order - lr**n** (first we visit left subtree, then right subtree, then node)

**Type of trees representation:**
- list of lists(Example: ['a', ['b', [], []], ['c', [], []]]) [Implementation](trees_list_of_lists.py)
