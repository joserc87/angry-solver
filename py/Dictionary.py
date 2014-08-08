# -*- coding: utf-8 -*-
from TreeNode import TreeNode
import json
import unicodedata
import codecs

def strip_accents(s):
	return u''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def removeAccent(v):
	"""
	v is an unicode character
	"""
	if v == u'á':
		return u'a'
	elif v == u'é':
		return u'é'
	elif v == u'í':
		return u'í'
	elif v == u'ó':
		return u'ó'
	elif v == u'ú':
		return u'ú'
	else:
		return v


def removeAccentsInString(s):
	return u''.join(removeAccent(c) for c in s)

class Dictionary:
	"""
	A word dictionary saved as a Tree
	"""

	def __init__(self):
		"""
		Default constructor
		"""
		self.root = TreeNode()


	def loadFromPath(self, path):
		"""
		Load a dictionary from a file
		Args:
			path (str): the path to the file to read
		Rises:
			IOException: If the file can't be opened
		"""
		self.root = TreeNode(' ');
		node = TreeNode()
		f = codecs.open(path, 'r', 'utf-8')
		for line in f:
			line = removeAccentsInString(line)
			node.addString(line.rstrip())
		f.close()
		self.root.addChild(node)

	def loadJSONFromPath(self, path):
		"""
		Load a dictionary from a JSON file
		Args:
			path (str): the path to the file to read
		Rises:
			IOException: If the file can't be opened
		"""
		self.root = TreeNode(' ');
		content = codecs.open(path, 'r', 'utf-8').read()
		data = json.loads(content)
		self.root = TreeNode()
		self.root.loadJSON(data)

	def checkWord(self, word):
		"""
		Check a word in the dictionary
		Args:
			word (str): The word to check
		Returns:
			True if the word exists in the dictionary. False otherwise
		"""
		return self.root.checkString(u' ' + word);

	def printTree(self):
		"""
		Prints the tree to the standard output
		"""
		print 'Tree:'
		print self.root.toString(0)
		print '\n'

	def toJSON(self):
		"""
		Saves the whole dictionary as a JSON object
		"""
		return json.dumps(self.root, default=lambda o: o.__dict__)

	def findWordsInPattern (self, pattern, letters):
		"""
		Find all the words from the dictionary that matches the pattern
		Args:
			pattern (str): The pattern where the word should fit in. It must be a mix of [a-z] + ' '
			letters (str): The available letters to form the word ([a-z] + *, where the * represents the wildcard)
		Returns:
			A list of strings with all the words found 
		"""
		words = []
		letters = ' ' + letters
		words = self.root.findWordsInPattern(pattern, letters, u'')
		return words;


