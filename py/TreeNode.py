
class TreeNode:
	"""
	A node in the character tree. It simply contains a letter and
	two pointers: one for the next sibling and the first child (plus other data for optimization)
	"""

	def __init__ (self, val = u''):
		"""
		Constructor
		"""
		self.value = val
		self.ending = u''
		self.child = None
		self.sibling = None
		self.isAWord = False #This boolean indicates if the node represents a word. This is necesary due that not only the leaf nodes can be a word.

	def loadJSON(self, dct):
		"""
		Loads a JSON object
		"""
		self.value = dct['value']
		self.ending = dct['ending']
		self.isAWord = dct['isAWord']
		if dct['child'] != None:
			self.child = TreeNode()
			self.child.loadJSON(dct['child'])

		if dct['sibling'] != None:
			self.sibling = TreeNode()
			self.sibling.loadJSON(dct['sibling'])
	
	def __createNewNodeFromString (self, s):
		"""
		Create a TreeNode
		Args:
			s (str): The input string
		Returns:
			a new TreeNode object representing the string s.
			The value of the new node will be s[0] and the ending will be s[1:]
		"""
		node = TreeNode()
		node.value = s[0]
		node.ending = s[1:]
		return node


	def addChild(self, c):
		"""
		Adds a child node. The method assumes that there is no child yet with the same value.
		Args:
			c (TreeNode): The node to add
		"""
		# First of all, if there is an ending (we don't have child yet), remove the ending and create a child based on that ending.
		if len(self.ending) > 0:
			endingCopy = self.ending
			self.ending = u''
			self.addChild(self.__createNewNodeFromString (endingCopy))

		if self.child == None:	# If there is no child, add c as the only child
			self.child = c
		else:					# If there are childs, add c as the last child
			node = self.child
			while node.sibling != None:
				node = node.sibling
			node.sibling = c

#	def addChildFromString(self, s):
#		"""
#		Initialize the node from a string s
#		Args:
#			s (str): The string to add
#		"""
#		if child == None:				# If there are no childs, easy
#			if len(self.ending) == 0:	# There is no ending ->
#				self.value = s[0]
#				self.ending = s[1:]
#			else:
#				node = self.__createNewNodeFromString(self.ending)
#				self.addChild(node)
#				self.addChildFromString(s)
#		else:
#			node = self.getChildFromChar(s[0])
#			if node == None:
#				node = self.__createNewNodeFromString(s)
#				self.addChild(node)
#			else:
#				node.addChildFromString(s[1:])


	def addString(self, s):
		"""
		Setup the node tree to "hold" the string s
		Args:
			s (str): The string that will be contained in the node
		"""
		if self.value == None:			#If the node is empty (Root node)
			self.value = s [0]
			self.ending = s[1:]

		elif self.value == s[0]:		# If the value is the same, add as a child.
			# First of all, if there is an ending (we don't have child yet), remove the ending and create a child based on that ending.
			if len(self.ending) > 0:
				endCopy = self.ending
				self.ending = ''
				self.isAWord = False	# As there is no ending anymore, this node won't represent a full word, but its son
				self.addChild(self.__createNewNodeFromString(endCopy))


			if len(s) <= 1:				# S is only one char. End
				self.isAWord = True
			else:
				substr = s[1:]

				if self.child == None:
					ch = self.__createNewNodeFromString(substr)
					ch.isAWord = True
					self.addChild(ch)
				else:
					self.child.addString(substr)

		elif self.sibling != None:		# s[0] != value -> Check on siblings
			self.sibling.addString (s)
		else:							# There are no siblings -> Create the first one
			self.sibling = self.__createNewNodeFromString(s)
			self.sibling.isAWord = True



	def getChildFromChar(self, c):
		"""
		Look up for the child with value c, or None if there is no such a child
		Args:
			c (str): The character to look up
		Returns:
			a TreeNode with value == c if found, or None otherwise
		"""
		node = self.child
		while node != None and node.value != c:
			node = node.sibling
		return node

	def checkString(self, s):
		"""
		Check if the string is valid, i.e. if value == s[0] and getChildFromChar(s[1]).checkString(s[1:])
		Args:
			s (str): The string to check
		Returns:
			True if s matches in the Tree, or False otherwise
		"""
		# Empty strings?
		if s == None:
			return False
		if len(s) == 0:
			return True
		if len(s) == 1:
			if s [0] == self.value:
				return self.isAWord

		# If it is a real string, if value is correct, check vertically, otherwise horizontally:
		if s[0] != self.value:		# We don't have that value	-> Check siblings
			return self.sibling != None and self.sibling.checkString(s)
		else:						# We may have it!
			if self.child == None:	# But we don't have childs	-> Check ending
				return self.ending == s[1:]
			else:					# And we have childs		-> Check recursively
				return self.child.checkString(s[1:])


	def toString(self, depth):
		"""
		String representation of the node.
		Returns:
			a string
		"""
		string = self.value
		if len(self.ending) != 0:
			string += '(' + self.ending + ')'
		if self.child != None:
			string += self.child.toString(depth+1)
		if self.sibling != None:
			string += '\n'
			for _ in range(depth):
				string += ' '
			self.sibling.toString(depth)
		return string

	def findWordsInPattern(self, pattern, letters, word):
		"""
		Find all the possible words, starting for this node, that matches the board pattern, and that has a prefix (word).
		Args:
			pattern (str): The pattern to match. Must be a chain of [a-z] + ' '
			letters (str): The available letters to use
			word (str): The word that we have build so far. Any new word will be 'word + str'
		Returns:
			A list of strings with all the valid words found in the pattern
		"""
		# ALGORITHM
		# -- CASE the node is child and we found a word
		# If child==NULL
		#   If pattern.length == 0
		#     words += word
		#   Return
		# -- CASE the position is fixed:
		# If pattern [0] != " "
		#   If pattern [0] == value
		#     If value IN letters
		#       call son, with pattern++ and letters -= value
		#     Else
		#       Return
		#   Else
		#     call sibling with same pattern and letters
		# Else --- Case the position is free
		#   If value IN letters
		#     call children
		#   call sibling
		#   
		#
		# Check if "value" is in letters (and pattern [0]==" ") OR if pattern [0]==value
		# Otherwise, go to sibling.
		words = []
		if self.value == ' ':
			words = self.child.findWordsInPattern(pattern, letters, word)
		elif len(pattern) == 0:		# Is the end, check if there is a child
			return []
		else:
			if pattern [0] == self.value:	# The next letter is value -> Recursion
				# Quick check: if it is a word by itself, add it in words
				if self.isAWord or self.child == None:
					if len (pattern) == 1 or pattern [1] == ' ': # Check that the word can be cut here
						words.append(word + self.value + self.ending)
				if self.child != None:	# If we have a child
					words.extend(self.child.findWordsInPattern(pattern[1:], letters, word + self.value))
				else:
					return[]
			elif pattern [0] == ' ':	# The next letter is an empty cell. We have to write "value"
				# Check if value is in "letters"
				pos = letters.find(self.value)
				if pos >= 0:
					# Quick check: if it is a word by itself, add it in words
					if self.isAWord or self.child == None:
						if len (pattern) == 1 or pattern [1] == ' ': # Check that the word can be cut here
							words.append(word + self.value + self.ending)
					# Remove value from letters
					lettersWithoutVal = letters[:pos] + letters[pos+1:] 
					# Call child with pattern[1:], letters-value, etc
					if self.child != None:
						words.extend(self.child.findWordsInPattern(pattern[1:], lettersWithoutVal, word + self.value))
				# Call siblings
				if self.sibling != None:
					words.extend(self.sibling.findWordsInPattern(pattern, letters, word))
			else:						# It is not empty, but pattern != value
				# Call siblings
				if self.sibling != None:
					words.extend(self.sibling.findWordsInPattern(pattern, letters, word))
		return words
