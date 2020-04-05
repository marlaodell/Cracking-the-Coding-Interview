class Node():
	def __init__(self, val = None):
		self.val = val

	def __str__(self):
		return str(self.val)

	def __eq__(self, other):
		return self.val == other.val

class BinaryTreeNode(Node):
	def __init__(self, val = None, left = None, right = None):
		Node.__init__(self, val)
		self.left = left
		self.right = right
		# self.left_subtree_size = 0

class ParentBinaryTreeNode(BinaryTreeNode):
	def __init__(self, val = None, left = None, right = None, parent = None):
		BinaryTreeNode.__init__(self, val, left, right)
		self.parent = parent

class KeyBinaryTreeNode(BinaryTreeNode):
	def __init__(self, key = None, val = None, left = None, right = None):
		BinaryTreeNode.__init__(self, val, left, right)
		self.key = key


class BinarySearchTree():

    def __init__(self, root = None):
        self.root = root

    def put(self, vals):
        for val in vals:
            self.root = self._put(val, self.root)
        return self.root

    def _put(self, val, root):
        if root is None:
            return BinaryTreeNode(val)
        if val < root.val:
            root.left = self._put(val, root.left)
        elif val > root.val:
            root.right = self._put(val, root.right)
        return root

class KeyBinarySearchTree(BinarySearchTree):
    
    def put(self, key_vals):
        for key, val in key_vals:
            self.root = self._put(key, val, self.root)
        return self.root

    def _put(self, key, val, root):
        if root is None:
            return KeyBinaryTreeNode(key, val)
        if val < root.val:
            root.left = self._put(key, val, root.left)
        elif val > root.val:
            root.right = self._put(key, val, root.right)
        return root

class ParentBinarySearchTree(BinarySearchTree):

    def _put(self, val, root):
        if root is None:
            return ParentBinaryTreeNode(val)
        if val < root.val:
            temp = self._put(val, root.left)
            root.left = temp
            temp.parent = root
        elif val > root.val:
            temp = self._put(val, root.right)
            root.right = temp
            temp.parent = root
        return root

			