
class Move:
	#Consts
	DOWN	= [1, 0]
	RIGHT	= [0, 1]
	UP		= [-1, 0]
	LEFT	= [0, -1]


	def getJSON(self):
		"""
		Transforms the object to a JSON to send it to the web service
		Returns:
			a string
		"""
		return ''

	def __init__(self):
		"""
		Constructor
		"""
		self.row = 0
		self.column = 0
		self.direction = Move.DOWN
		self.score = 0
		self.word = ''
		self.lettersUsed = ''
		self.valid = False
