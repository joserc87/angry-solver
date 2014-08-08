import sys
from Dictionary import Dictionary
from Board import Board

if __name__ == '__main__':
	path = "../Resources/spanish.txt"
	dct = Dictionary()
	end = False
	dct.loadFromPath(path)
	jsonString = dct.toJSON()
	f = open("../Resources/esOptimized.txt", 'w')
	f.write(jsonString)
	f.close()

