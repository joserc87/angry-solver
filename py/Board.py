# -*- coding: utf-8 -*-
from Dictionary import Dictionary
from Move import Move

# See: http://fbpedia.com/cuantas-letras-tiene-apalabrados-angry-words.html
# Score: http://www.palabras-apalabrados.info/trucos
class Board:
	BOARD_HEIGHT = 15
	BOARD_WIDTH = 15
	EMPTY = u' '

	wordMultipliers = [int(c) for c in \
										"113111111111311" + \
										"111112111211111" + \
										"311111111111113" + \
										"111111121111111" + \
										"111111111111111" + \
										"121111111111121" + \
										"111111111111111" + \
										"111211111112111" + \
										"111111111111111" + \
										"121111111111121" + \
										"111111111111111" + \
										"111111121111111" + \
										"311111111111113" + \
										"111112111211111" + \
										"113111111111311" ]

	letterMultipliers = [int(c) for c in \
										"111131111131111" + \
										"131111111111131" + \
										"112111313111211" + \
										"111311111113111" + \
										"311111212111113" + \
										"111113111311111" + \
										"113121111121311" + \
										"111111111111111" + \
										"113121111121311" + \
										"111113111311111" + \
										"311111212111113" + \
										"111311111113111" + \
										"112111313111211" + \
										"131111111111131" + \
										"111131111131111" ]

	# This is for spanish
	scorePerLetter = {
		u'a' : 1,
		u'b' : 3,
		u'c' : 3,
		u'd' : 2,
		u'e' : 1,
		u'f' : 4,
		u'g' : 2,
		u'h' : 4,
		u'i' : 1,
		u'j' : 8,
		u'k' : 0,
		u'l' : 1,
		u'm' : 3,
		u'n' : 1,
		u'ñ' : 8,
		u'o' : 1,
		u'p' : 3,
		u'q' : 5,
		u'r' : 1,
		u's' : 1,
		u't' : 1,
		u'u' : 1,
		u'v' : 4,
		u'w' : 0,
		u'x' : 8,
		u'y' : 4,
		u'z' : 10
	}
	numLettersPerMatch = {
		u'a' : 12,
		u'b' : 2,
		u'c' : 4,
		u'd' : 5,
		u'e' : 12,
		u'f' : 1,
		u'g' : 2,
		u'h' : 2,
		u'i' : 6,
		u'j' : 1,
		u'k' : 0,
		u'l' : 4,
		u'm' : 2,
		u'n' : 5,
		u'ñ' : 1,
		u'o' : 9,
		u'p' : 2,
		u'q' : 1,
		u'r' : 5,
		u's' : 6,
		u't' : 4,
		u'u' : 5,
		u'v' : 1,
		u'w' : 0,
		u'x' : 1,
		u'y' : 1,
		u'z' : 1
	}

	def __init__(self):
		"""
		Constructor
		"""
		self.multipliers = None
		self.BOARD_HEIGHT = Board.BOARD_HEIGHT
		self.BOARD_WIDTH = Board.BOARD_WIDTH
		self.tiles = [' ' for _ in range(self.BOARD_WIDTH * self.BOARD_HEIGHT)]

		
		# TODO: Change multipliers
		#self.multipliers = [1 for _ in range (self.BOARD_WIDTH * self.BOARD_HEIGHT)]


	def setTestData(self):
		# For testing porpuses
		self.tiles = [c for c in u"               " + \
						u"               " + \
						u"       afeo    " + \
						u"       c       " + \
						u"       r       " + \
						u"    ujier      " + \
						u"       c       " + \
						u"       i       " + \
						u"       o       " + \
						u"               " + \
						u"               " + \
						u"               " + \
						u"               " + \
						u"               " + \
						u"               " ]


	def getTile(self, row, col):
		"""
		Getter to access the content of the board
		Args:
			row (int): The row of the tile to retrieve
			col (int): The column of the tile to retrieve
		Returns:
			The tile at (row, col)
		"""
		assert(self.validPos(row, col))
		return self.tiles[row*15 + col]

	def getLetterMultiplier(self, row, col):
		"""
		Getter to access the multipliers
		Args:
			row (int): The row of the multiplier to retrieve
			col (int): The column of the multiplier to retrieve
		Returns:
			The multiplier at (row, col)
		"""
		assert(self.validPos(row, col))
		return self.letterMultipliers[row*15 + col] if self.getTile(row, col) == Board.EMPTY else 1

	def getWordMultiplier(self, row, col):
		"""
		Getter to access the multipliers
		Args:
			row (int): The row of the multiplier to retrieve
			col (int): The column of the multiplier to retrieve
		Returns:
			The multiplier at (row, col)
		"""
		assert(self.validPos(row, col))
		return self.wordMultipliers[row*15 + col] if self.getTile(row, col) == Board.EMPTY else 1

	def getScoreForLetter(self, letter):
		"""
		The score for each letter [a-z], without any kind of multipliers
		Args:
			letter (str): A single char (a-z)
		Returns:
			a number
		"""
		return Board.scorePerLetter[letter]

	def setTile(self, row, col, val):
		"""
		Setter to change the content of the board
		Args:
			row (int): The row of the tile to change
			col (int): The column of the tile to change
			val (str): The new value of the tile
		"""
		assert(self.validPos(row, col))
		self.tiles[row*15+col] = val

	def initFromTileString(self, tilestring):
		"""
		Initialize the object (tiles) from a string
		Args:
			tilestring (str): A string with the format "C1|P1,C2|P2,...,CN|PN" where C1..N are just characters, the value of the tile, and P1..N are the position (int [0..15*15-1])
		"""
		moves = [x.split('|') for x in tilestring.split(',')]
		for move in moves:
			val = move[0]
			pos = int(move[1])
			if pos >= 0 and pos < self.BOARD_WIDTH * self.BOARD_HEIGHT:
				self.tiles[pos] = val

	def toString(self):
		"""
		String representation of the object
		Returns:
			A string
		"""
		string = ''
		i = 0
		for tile in self.tiles:
			string = string + '| ' + tile + ' '
			if i % Board.BOARD_WIDTH == 0:
				string = string + '\n'
			i += 1
		return string

	def findBestMove(self, dictionary, letters):
		"""
		Find the best move in the board using the available letters
		Args:
			dct (dict): The dictionary to use to find the words
			letters (str): The available letters
		Returns:
			A list of moves
		"""
		# For each position
		bestMove = None
		moves = []
		for i in range(self.BOARD_HEIGHT):
			for j in range(self.BOARD_WIDTH):
				# For each direction
				for direction in [Move.DOWN, Move.RIGHT]: # LEFT and UP are not allowed
					#moves[len(moves):] = self.findAllMovesIn(i, j, direction, letters, dictionary)
					moves = self.findAllMovesIn(i, j, direction, letters, dictionary)
					for move in moves:					# Take only the best move
						bestMove = self.maxMove(bestMove, move)
		return bestMove

	def findAllMovesIn(self, row, col, direction, letters, dictionary):
		"""
		Find all the possible words in the current board
		starting in the position (row, column) with the available letters and cointained in the dictionary
		Args:
			row (int): The row of the position where the words will start
			col (int): The column of the position where the words will start
			direction ([x,y]): The direction of the word. Must be one between Move.UP, Move.DOWN, Move.LEFT or Move.RIGHT
			letters (str): The available letters to build the word
			dictionary (Dictionary): The dictionary where the words must be
		Returns:
			a list of Move with the possible moves (words)
		"""
		moves = []
		# First of all, check that there can be a valid move at this position, just to speed things up
		if not self.checkNeighbours(row, col, direction, len(letters)):
			return moves
		# Otherwise, if possible, lets start searching
		# First, take the row/column from the board, as a string
		boardString = self.getStringFromBoard (row, col, direction)
		# Find a word that fits in the string
		# This is the main method of the algorithm
		words = dictionary.findWordsInPattern (boardString, letters)
		# Once we have the solutions, lets create the moves
		for word in words:
			move = Move()
			word = word.strip()
			move.valid = True
			move.row = row;
			move.column = col;
			move.direction = direction;
			move.score = self.calcScore (row, col, direction, word);
			move.lettersUsed = self.getLettersUsed (word, boardString);
			move.word = word
			if len(move.lettersUsed) > 0 and len(move.lettersUsed) < len(move.word):
				moves.append(move)
		return moves

	def getStringFromBoard(self, row, col, direction):
		"""
		Gets the string contained in the board starting at the position (row, col) and going in the direction "direction" 
		It will contain also the spaces util the end of the board
		Args:
			row (int): The position row where the word starts
			col (int): The position column where the word starts
			direction ([dx, dy]): One of the following Move.UP, Move.DOWN, Move.LEFT or Move.RIGHT
		Returns:
			a string with the content of the board at that position. Can contain EMPTY tiles
		"""
		di = direction[0]
		dj = direction[1]
		end = False
		i = row
		j = col
		boardString = ''
		while not end:
			# Check if finish
			if not self.validPos(i, j):
				end = True
			else:
				# Add the character to the string
				boardString = boardString + self.getTile(i, j)
				# Go forward
				i+=di
				j+=dj
		return boardString
	def getBeginingOfWordAt(self, row, col, direction):
		di = direction[0]
		dj = direction[1]
		end = False
		i = row
		j = col
		boardString = ''
		while not end:
			# Check if finish
			if not self.validPos(i+di, j+dj) or self.tiles(i, j) == Board.EMPTY:
				end = True
			else:
				# Go forward
				i+=di
				j+=dj
		return [i, j]

	def getWordAtPos(self, row, col, direction):
		"""
		Retrieves the word (without spaces) that lays on the position (row, col).
		The word can actually start before or after (row, col)
		Args:
			row (int): The row part of the position P, where P contains a letter of the word
			col (int): The column part of the position P, where P contains a letter of the word
			direction ([dx, dy]): The direction in wich the word is written. The algorithm will only check that direction
		Returns:
			a string, without spaces, with length 0 if the position is empty, 1 if there is no word at the position or >1 if there is a word
		"""
		assert(self.validPos(row, col))
		di = direction[0]
		dj = direction[1]
		if self.getTile(row, col) == Board.EMPTY:
			return ''
		
		start = self.getBeginingOfWordAt(row, col, [-di, -dj])
		end = self.getBeginingOfWordAt(row, col, [di, dj])

		end = False
		i = row
		j = col
		boardString = ''
		while not end:
			# Check if finish
			if self.validPos(i, j):
				end = True
			else:
				# Add the character to the string
				boardString = boardString + self.getTile(i, j)
				# Go forward
				i+=di
				j+=dj
		return boardString	

	def calcScore(self, row, col, direction, word):
		"""
		Retrieves the score based on the word, the position (multipliers) and derivated words.
		Args:
			row (int): The row where the word starts
			col (int): The column where the word starts
			direction ([di, dj]): The direction of the word. Must be Move.UP, Move.DOWN, Move.RIGHT or Move.LEFT
			word (str): The word
		Returns:
			The score of that word in the board, as an integer
		"""
		score = 0
		di = direction[0]
		dj = direction[1]
		end = False
		i = row
		j = col
		wordMultiplier = 1
		cnt = 0
		while not end:
			# Check if finish
			if self.validPos(i, j) or cnt >= len(word):
				end = True
			else:
				# Add the character to the string
				wordMultiplier *= self.getWordMultiplier(i, j) 
				score += self.getScoreForLetter(word[cnt]) * self.getLetterMultiplier(i, j)
				# Go forward
				i+=di
				j+=dj
			cnt += 1
		return score * wordMultiplier

	def validPos(self, row, col):
		"""
		Check if the position (row, col) is inside the boundaries
		Args:
			row (int): The row where the word starts
			col (int): The column where the word starts
		Returns:
			True if row >= 0 and row < self.BOARD_HEIGHT and col >= 0 and col < self.BOARD_WIDTH
		"""
		if row >= 0 and row < self.BOARD_HEIGHT and col >= 0 and col < self.BOARD_WIDTH:
			return True
		else:
			return False


	def checkNeighbours(self, row, col, direction, length):
		"""
		Check if a word with a certain length can be written in the pos (row, col)
		If there is no other word in the neighbourhood, we can't write it (unless it is the first one)
		Args:
			row (int): The row where the word starts
			col (int): The column where the word starts
			direction ([di, dj]): The direction of the word. Must be Move.UP, Move.DOWN, Move.RIGHT or Move.LEFT
			length (int): The length of the word
		Returns:
			True if there is a tile "length" tiles away from (row, col) in that direction. False otherwise
		"""
		di = direction[0]
		dj = direction[1]
		i = row
		j = col
		cnt = 0
		while self.validPos(i, j) and cnt < length:
			if self.getTile(i, j) != Board.EMPTY:
				return True
			if self.validPos(i + dj, j + di) and self.getTile(i + dj, j + di) != Board.EMPTY:
				return True
			if self.validPos(i - dj, j - di) and self.getTile(i - dj, j - di) != Board.EMPTY:
				return True
			i += di
			j += dj
			cnt += 1
		return False

	def maxMove(self, move1, move2):
		"""
		Return the best of the 2 moves.
		Args:
			move1 (Move): The first move
			move2 (Move): The second move
		Returns:
			move2 if move1 is not valid or move2.score > move1.score, or else move1
		"""
		if move2 == None or (move1 != None and not move2.valid):
			return move1
		elif move1 == None or not move1.valid or move2.score > move1.score:
			return move2
		else:
			return move1

	def getLettersUsed(self, word, pattern):
		"""
		Get the letters in word that are not in pattern
		Args:
			word (str): The word (e.g. "python")
			pattern (str): The pattern used to create the word (e.g. "  tho ")
		Returns:
			the letters in word that are not the same in pattern (e.g. "pyn")
		"""
		letters = ''
		# To calc the letters used, substract the pattern from the word
		for i in range(len(word)):
			if pattern[i] == Board.EMPTY:
				letters += word[i]
		return letters



if __name__ == '__main__':
	tiles = 'A|156,R|187,E|126,N|141,E|112,O|142,O|172,L|157,D|113,I|114,D|115,O|116,C|111'
	vec = [x.split('|') for x in tiles.split(',')]
	board = Board()
	board.initFromTileString(tiles)
	print board.toString()
