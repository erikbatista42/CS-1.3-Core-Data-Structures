
#!python

# import custom_queue 
import custom_queue

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        if self.left is None and self.right is None:
            return True
        else:
            return False


    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        if self.left is not None or self.right is not None:
            return True
        else:
            return False


    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best and worst case running time: Best => O(1) if tree is really small like a couple of nodes that we need to traverse to find height. 
        Worst => O(n) because it depends how many nodes they are in to traverse"""
        left_height = 0
        right_height = 0

        if self.left is not None:
            left_height = 1 + self.left.height()
        if self.right is not None:
            right_height = 1 + self.right.height()

        # max returns the largest num between the two arguments
        return max(left_height, right_height)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best and worst case running time: Best => O(1) if tree is really small like a couple of nodes that we need to traverse to find height. 
        Worst => O(n) because it depends how many nodes they are in to traverse"""
        return self.root.height() # calculate height here

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_iterative(item)
        if node is not None:
            return node.data
        else:
            return None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: O(1)  If parent is found quickly when traversing
        TODO: Worst case running time: O(n) because we have to find the parent. So n is the number of time we have to search to find parent """
        # Handle the case where the tree is empty
        if self.is_empty():
            # Create a new root node
            self.root = BinaryTreeNode(item)
            # Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_iterative(item)
        # Check if the given item should be inserted left of parent node
        if parent.data > item:
            # Create a new node and set the parent's left child
            parent.left = BinaryTreeNode(item)
        # Check if the given item should be inserted right of parent node
        elif parent.data < item:
            # Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)
        # Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: O(1) if the node we find is very early like the first few nodes
        Worst case running time: O(n) because we have to traverse the nodes/ tree to find the node"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if node.data == item:
                # Return the found node
                return node
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Descend to the node's left child
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Descend to the node's right child
                node = node.right
        return None # Not found

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: O(1) if the node we find is very early like the first few nodes
        Worst case running time: O(n) because we have to traverse the nodes/ tree to find the node"""
        

        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        elif item == node.data:
            # Return the found node
            return node
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            return _find_node_recursive(self, item, node = node.left)
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            # TODO: Recursively descend to the node's right child, if it exists
            return _find_node_recursive(self, item, node = node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case running time: O(1) if there are only a few nodes in the tree to traverse to find parent
        Worst case running time: O(n) Since we have to go traverse num of nodes in tree"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None # previous node
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent # found
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            return parent
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            if node.left is not None:
                node = node.left
            return self._find_parent_node_recursive(self, item, node, parent=node)  # Hint: Remember to update the parent parameter
        # TODO: Check if the given item is greater than the node's data
        elif node.right is not None:
            # TODO: Recursively descend to the node's right child, if it exists
            node = node.right
            return self._find_parent_node_recursive(self, item, node, parent=node)  # Hint: Remember to update the parent parameter


    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) n is the number of visits we have to make
        Memory usage: O(n) stack size when function is invoking itself"""
        # Traverse left subtree, if it exists
        if node.left is not None:
            print("left", node.data)
            self._traverse_in_order_recursive(node.left, visit)
        visit(node.data)
        if node.right is not None:
            print("right", node.data)
            self._traverse_in_order_recursive(node.right, visit)


    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) n is the number of visits we have to make
        Memory usage: O(n) stack size when function is invoking itself"""
        # Visit this node's data with given function
        visit(node.data)
        if node.left:
            self._traverse_pre_order_recursive(node.left, visit)

        if node.right:
            self._traverse_pre_order_recursive(node.right, visit)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) n is the number of visits we have to make
        Memory usage: O(n) stack size when function is invoking itself"""
        # Traverse left subtree, if it exists
        if node.left:
            self._traverse_post_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        if node.right:
            self._traverse_post_order_recursive(node.right, visit)
        # Visit this node's data with given function
        visit(node.data)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) while loop ends depending on the number of visits it has to make
        Memory usage: O(n) n is the size of the queue"""
        # Create queue to store nodes not yet traversed in level-order
        queue = custom_queue.LinkedQueue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while not queue.is_empty():
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left:
                queue.enqueue(node.left)
            # Enqueue this node's right child, if it exists
            if node.right:
                queue.enqueue(node.right)

if __name__ == "__main__":
    # test_binary_search_tree()
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    # print('items: {}'.format(items))

    tree = BinarySearchTree()

    for item in items:
        tree.insert(item)

    print('Traversing items:')
    print('items in-order: {}'.format(tree.items_level_order()))
    # nodes = ["A","B","C"]
    # tree = BinarySearchTree()

    # for data in nodes:
    #     tree.insert(data)
    
    # result = tree.search("C")   

    # root_node = BinaryTreeNode("A")
    # left_node_1 = BinaryTreeNode("B")
    # left_node_2 = BinaryTreeNode("C")
    # right_node_1 = BinaryTreeNode("D")
    # right_node_2 = BinaryTreeNode("E")
    # right_node_3 = BinaryTreeNode("F")


    # root_node.left = left_node_1
    # left_node_1.left = left_node_2
    # left_node_1.right = right_node_1
    # right_node_1.right = right_node_2
    # right_node_2.right = right_node_3
    # print("items in tree =>", tree)
    # print(tree.items_in_order())

# def test_binary_search_tree():
#     # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    # items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
#     print('items: {}'.format(items))

    # tree = BinarySearchTree()
#     print('tree: {}'.format(tree))
#     print('root: {}'.format(tree.root))

#     print('\nInserting items:')
    # for item in items:
    #     tree.insert(item)
#         print('insert({}), size: {}'.format(item, tree.size))
#     print('root: {}'.format(tree.root))

#     print('\nSearching for items:')
#     for item in items:
#         result = tree.search(item)
#         print('search({}): {}'.format(item, result))
#     item = 123
#     result = tree.search(item)
#     print('search({}): {}'.format(item, result))

    # print('\nTraversing items:')
#     print('items in-order:    {}'.format(tree.items_in_order()))
#     print('items pre-order:   {}'.format(tree.items_pre_order()))
#     print('items post-order:  {}'.format(tree.items_post_order()))
    # print('items level-order: {}'.format(tree.items_level_order()))



