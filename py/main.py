import sys
from Dictionary import Dictionary
from Board import Board

if __name__ == '__main__':
	path = "../Resources/esOptimized.txt"
	dct = Dictionary()
	end = False
	dct.loadJSONFromPath(path)

	if (len(sys.argv) == 1):
		print 'System ready\n\n'
		end = False
		while not end:
			word = raw_input('Word to check ')
			print "The word \"" + word + "\" is " + "correct" if dct.checkWord(word) else "not correct"
			if word == 'bye':
				end = True
				print "See you soon!"
	else:
		word = sys.argv[1]
		if word == 'run':
			board = Board()
			board.setTestData()
			move = board.findBestMove(dct, "hlo")
			if move == None:
				print "There are no moves :S"
			else:
				#print [x.__dict__ for x in move] 
				print "The best solution is ", move.__dict__
		else:
			print "The word \"" + word + "\" is " + "correct" if dct.checkWord(word) else "not correct"
