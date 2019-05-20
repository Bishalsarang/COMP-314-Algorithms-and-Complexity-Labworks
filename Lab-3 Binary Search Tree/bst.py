# Author: Bishal Sarang
# Implementation of BST using doubly linked list


# TODO: 1. Implement Delete
# TODO: 2. Unit test
# TODO: 3. Iterative Approach
class Node:
	"""
	Node class
	Args:
        key(int): unique key 
        value(Gen): value corresponding to the key
        left(Node): left Node
        right(Node): right Node
        parent(Node): parent Node 
	"""
	def __init__(self, key, value):
		"""
		Constructor for Node Class
		Args:
			key(int): unique key
			value(Gen): corresponding value
		"""
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		
	def __repr__(self):
		"""
		Overload printing function
		"""
		return '({},"{}")'.format(self.key, self.value)
	
	def __eq__(self, node1):
		return self.key == node1.key 
		
	def has_left_child(self):
		return self.left is not None
	
	def has_right_child(self):
		return self.right is not None
		
	def insert(self, key, value):
		"""
		Insert (key, value) into correct place of BST
		Args:
			key(int): unique key
			value(Gen): corresponding value
		Returns:
			Boolean Value if (key, value) has been inserted properly or not
		"""
		
		# If the key already exists in BST
		# Do  not insert
		if self.key == key:
			return False
		# If key to be inserted is less than parent key
		# Inser into left subtree
		elif self.key > key:
			# If left subtree exists try to insert (key, value) recursively
			if self.has_left_child():
				self.left.insert(key, value)
			# Else make a new left node
			# Set parent to the current node
			self.left = Node(key, value)
			self.left.parent = self
			return True
		# If key to be inserted is greater than current node key
		# Insert into right subtree
		else:
			# If right subtree exists try to insert (key, value) recursively
			if self.has_right_child():
				self.right.insert(key, value)
			# Else make a new right node
			# Set parent to the current node
			self.right = Node(key, value)
			self.right.parent = self
			return True
	
	def find(self, key):
		"""
		find if key exists
		Args:
			key(int): key to be searched
		Returns:
			Boolean Value if a key is found or  not
		"""
		# If searched key is found
		# Print (key, value)
		# return True
		if self.key == key:
			return self
		# Search left subtree if there is any
		elif self.key > key:
			if self.has_left_child():
				return self.left.find(key)
			return None
		# Search right subtree if there is any
		else:
			if self.has_right_child():
				return self.right.find(key)
			return None
			
	def largest_key(self):
		"""
		Find largest key
		Args:
			None
		Returns:
			Largest Key
		"""
		if self.has_right_child():
			return self.right.largest_key()
		return self.key
	
	def smallest_key(self):
		"""
		Find smallest key
		Args:
			None
		Returns:
			Smallest Key
		"""
		if self.has_left_child():
			return self.left.smallest_key()
		return self.key
	
	
	def preorder(self):
		"""
		Preorder traversal for current node
		Args:
			None
		Return:
			None
		"""
		if self is not None:
			print(self, end = " => ")
			
			if self.has_left_child():
				self.left.preorder()
			if self.has_right_child():
				self.right.preorder()
	
	def postorder(self):
		"""
		Post order traversal for current node
		Args:
			None
		Returns:
			None
		"""
		if self is not None:
			if self.has_left_child():
				self.left.postorder()
			if self.has_right_child():
				self.right.postorder()
			print(self, end = " => ")
	
	def inorder(self):
		"""
		Inorder traversal of current node
		"""
		if self is not None:
			if self.has_left_child():
				self.left.postorder()
			print(self, end = " => ")
			if self.has_right_child():
				self.right.postorder()
	
	def deletenode(self, key):
		found_node = self.find(key)
		
		# If node is in the BST
		if found_node is not None:
			if not found_node.has_left_child() and not found_node.has_right_child():
				if found_node.parent.has_right_child():
					if found_node.parent.right == found_node:
						found_node.parent.right = None
				else:
					found_node.parent.left = None
				
			return True
		return False
			
class BST:
	"""
	Binary Search Tree Class
	"""
	def __init__(self):
		"""
		Args:
			None
		Returns:
			None
		"""
		self.root = None
		self.size = 0
	
	def __repr__(self):
		"""
		Overload printing of BST objects
		"""
		return "Root Node is {}.\nTotal Nodes of BST is {}".format(self.root.key, self.size)
		
		
	def insert(self, key, value):
		"""
		inserts (key, value) into BST
		Args:
			key, value
		"""
		# If BST is not empty
		# Insert (key, value) into root Node
		if self.root is not None:
			self.size += self.root.insert(key, value)
		# If BST is empty i.e no root
		# Create a new root 
		else:
			self.root = Node(key, value)
			self.size += 1
			return True

	def find(self, key):
		# If BST is not empty
		# FInd the key
		if self.root is  not None:
			return self.root.find(key)
		# Else not found
		return None
			
	def largest_key(self):
		if self.root is not None:
			return self.root.largest_key()
	
	def smallest_key(self):
		if self.root is not None:
			return self.root.smallest_key()
	
	def preorder(self):
		print("Pre Order Traversal is ")
		self.root.preorder()
		print("")
		
	def postorder(self):
		print("Post Order Traverasal is ")
		self.root.postorder()
		print("")
		
	def inorder(self):
		print("In Order traversal is")
		self.root.inorder()
		print("")
		
	def deletenode(self, key):
		if self.root is not None:
			if self.root.key == key:
				self.root = None
				self.size -= 1
				return True
			if self.find(key) is None:
				return False
			if self.root.deletenode(key):
				self.size -= 1
			
	
	
			
			
if __name__ == "__main__":
	bt = BST()
	bt.insert(5, "e")
	bt.insert(6, "f")
	print(bt.root == bt.root)
	print(bt.size)
	print(bt.deletenode(6))
	print(bt.size)
	"""
	print(bt.root)
	bt.preorder()
	bt.inorder()
	bt.postorder()
	print(bt)
	bt.deletenode(5)
	print(bt.root)
	"""
