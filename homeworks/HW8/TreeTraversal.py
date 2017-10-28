import warnings

# The BinaryNode class for nodes in the BinaryTree
class BinaryNode:
    
    def __init__(self, val):
        self.val = val
        self.p = None
        self.left = None
        self.right = None
    
    def __repr__(self):
        return "BinaryNode({})".format(self.val)
    
    def count_child(self): # count the number of children of this node
        if self.left == None and self.right == None:
            return 0
        elif self.left != None and self.right != None:
            return 2
        else:
            return 1

# The BinaryTree class
class BinaryTree:
    
    def __init__(self):
        self.root = None
    
    def __repr__(self):
        return "BinaryTree()"
    
    # The height of the BinaryTree
    def __len__(self):
        return self.maxDepth(self.root)
    
    # The height of the BinaryTree
    def maxDepth(self, root): 
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
    
    
    # Insert
    def insert(self, val):
        bi_node = BinaryNode(val) # create a new BinaryNode for the value to be inserted
        
        if self.root == None: # if the tree is empty, we just need to insert it at root
            self.root = bi_node
            return
        
        current_node = self.root # walk thru the tree to find the right position to insert
        while current_node != None:
            current_p = current_node
            if val > current_node.val:
                current_node = current_node.right
            else:
                current_node = current_node.left
        
        if val > current_p.val: 
            current_p.right = bi_node # is a right child
        else:
            current_p.left = bi_node # is a left child
        bi_node.p = current_p # set parent
    
    def inOrderWalk(self, node, ordered_nodes):
        if node != None:
            self.inOrderWalk(node.left, ordered_nodes)
            ordered_nodes.append(node.val)
            self.inOrderWalk(node.right, ordered_nodes)
            return ordered_nodes
    
    def preOrderWalk(self, node, ordered_nodes):
        if node != None:
            ordered_nodes.append(node.val)
            self.preOrderWalk(node.left, ordered_nodes)
            self.preOrderWalk(node.right, ordered_nodes)
            return ordered_nodes
    
    def postOrderWalk(self, node, ordered_nodes):
        if node != None:
            self.postOrderWalk(node.left, ordered_nodes)
            self.postOrderWalk(node.right, ordered_nodes)
            ordered_nodes.append(node.val)
            return ordered_nodes
    
    # Delete the nodes with 'None' as value
    def clearNoneNodes(self, node):
        if node != None:
            if node.val == 'None':
                if node == node.p.right:
                    node.p.right = None
                else:
                    node.p.left = None
            self.clearNoneNodes(node.left)
            self.clearNoneNodes(node.right)
    
    # GetValues: calling getValuesNode(self.root, 0, depth, values)
    def getValues(self, depth):
        values = []
        self.getValuesNode(self.root, 0, depth, values)
        self.clearNoneNodes(self.root)
        return values
    
    # GetValues from the subtree rooted at node, store in values
    def getValuesNode(self, node, current_depth, depth, values):
        if node != None:
            if current_depth == depth:
                values.append(node.val)
            else:
                if node.left == None:
                    none_node = BinaryNode('None')
                    none_node.p = node
                    node.left = none_node
                if node.right == None:
                    none_node = BinaryNode('None')
                    none_node.p = node
                    node.right = none_node
                self.getValuesNode(node.left, current_depth+1, depth, values)
                self.getValuesNode(node.right, current_depth+1, depth, values)
    
    # Return the right-most node from the subtree rooted at node
    def tree_max(self, node): 
        while node.right != None:
            node = node.right
        return node

    # Replace the subtree rooted at u with the subtree rooted at v
    def transplant(self, u, v): 
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p
    
    # Search for the value=key thru the subtree rooted at node
    def search(self, node, key):
        while node != None and key != node.val:
            if key > node.val:
                node = node.right
            else:
                node = node.left
        return node
    
    # Remove
    def remove(self, val):
        rm_node = self.search(self.root, val)
        if rm_node == None: # invalid remove node
            warnings.warn('The value to be removed does not has a node associated.')
            return
        if rm_node.left == None:
            self.transplant(rm_node, rm_node.right)
        elif rm_node.right == None:
            self.transplant(rm_node, rm_node.left)
        else:
            left_max = self.tree_max(rm_node.left)
            if left_max.p != rm_node:
                self.transplant(left_max, left_max.left)
                left_max.left = rm_node.left
                left_max.left.p = left_max
            self.transplant(rm_node, left_max)
            left_max.right = rm_node.right
            left_max.right.p = left_max


from enum import Enum

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal:
    
    # DFSTraversal Constructor
    def __init__(self, tree, traversalType):
        if traversalType == DFSTraversalTypes.INORDER:
            self.ordered_nodes = tree.inOrderWalk(tree.root, list())
        elif traversalType == DFSTraversalTypes.PREORDER:
            self.ordered_nodes = tree.preOrderWalk(tree.root, list())
        elif traversalType == DFSTraversalTypes.POSTORDER:
            self.ordered_nodes = tree.postOrderWalk(tree.root, list())
        else:
            raise TypeError('TraversalType Wrong: must be DFSTraversalTypes.INORDER/PREORDER/POSTORDER')
        # set attributes
        self.tree = tree 
        self.type = traversalType
        self.index = 0
    
    # Change Traversal Type
    def changeTraversalType(self, traversalType):
        if self.type == traversalType: # nothing changed
            return
        else:
            if traversalType == DFSTraversalTypes.INORDER: # change to INORDER
                self.ordered_nodes = self.tree.inOrderWalk(self.tree.root, list())
            elif traversalType == DFSTraversalTypes.PREORDER: # change to PREORDER
                self.ordered_nodes = self.tree.preOrderWalk(self.tree.root, list())
            elif traversalType == DFSTraversalTypes.POSTORDER: # change to POSTORDER
                self.ordered_nodes = self.tree.postOrderWalk(self.tree.root, list())
            else:
                raise TypeError('TraversalType Wrong: must be DFSTraversalTypes.INORDER/PREORDER/POSTORDER')
            print('Changed traversalType to be {}'.format(traversalType))
            self.type = traversalType
            self.index = 0
    
    # Initialize the iterator
    def __iter__(self):
        return self
    
    # Called by __iter__ to get the next value
    def __next__(self):
        try:
            node = self.ordered_nodes[self.index] 
        except IndexError:
            raise StopIteration() 
        self.index += 1
        return node 
            
            
    