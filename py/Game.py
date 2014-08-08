import json
from User import User
from Board import Board


class Game:

	

	def __init__(self):
		self.ID = 0 # The GameID
		self.my_message_alerts = 0
		self.nudge = False
		self.coins = 0
		self.my_turn = False
		self.type = ''
		self.opponent = None #User()
		self.my_rack_tiles = []	# List of available tiles
		self.remaining_tiles = 0 # Tiles to come
		self.board = Board()
		self.turns_played = 0
		self.turns_passed = 0
		self.last_turn = None
		self.my_score = 0
		self.opponent_score = 0
		self.chat_enable = False
		self.lang_distribution = '' # Whatever this is
		self.language = ''
		self.dictionary_version = ''
		self.created = ''
		self.expiration_date = ''
		self.game_status = ''
		self.extras = []
		self.removed_by_opponent = False


	def parseJSON(self, dct):
		if 'id'					in dct: self.ID					= dct['id']
		if 'my_message_alerts'	in dct: self.my_message_alerts	= dct['my_message_alerts']
		if 'nudge'				in dct: self.nudge				= dct['nudge']
		if 'coins'				in dct: self.coins				= dct['coins']
		if 'my_turn'			in dct: self.my_turn			= dct['my_turn']
		if 'type'				in dct: self.type				= dct['type']
		if 'remaining_tiles'	in dct: self.remaining_tiles	= dct['remaining_tiles']
		if 'turns_played'		in dct: self.turns_played		= dct['turns_played']
		if 'turns_passed'		in dct: self.turns_passed		= dct['turns_passed']
		if 'my_score'			in dct: self.my_score			= dct['my_score']
		if 'opponent_score'		in dct: self.opponent_score		= dct['opponent_score']
		if 'chat_enable'		in dct: self.chat_enable		= dct['chat_enable']
		if 'lang_distribution'	in dct: self.lang_distribution	= dct['lang_distribution']
		if 'language'			in dct: self.language			= dct['language']
		if 'dictionary_version'	in dct: self.dictionary_version	= dct['dictionary_version']
		if 'created'			in dct: self.created			= dct['created']
		if 'expiration_date'	in dct: self.expiration_date	= dct['expiration_date']
		if 'game_status'		in dct: self.game_status		= dct['game_status']
		if 'extras'				in dct: self.extras				= dct['extras'] # Right now we don't care about the extras, so we will add it as an object
		if 'removed_by_opponent'in dct: self.removed_by_opponent= dct['removed_by_opponent']

		# The opponent is just a User
		if 'opponent'			in dct:
			self.opponent = User()
			self.opponent.parseJSON(dct['opponent'])

		# The last played turn
		if 'last_turn'			in dct:
			self.last_turn = Turn()
			self.last_turn.parseJSON(dct['last_turn'])

		# For the available tiles, transform from string to list
		if 'my_rack_tiles'		in dct:	
			my_rack_tiles = [x.strip() for x in dct['my_rack_tiles'].split(',')]

		# Parse the board
		if 'board_tiles'		in dct:
			board_tiles = dct['board_tiles'] # In the format 'A|156,R|187,E|126,N|141,E|112,O|142,O|172,L|157,D|113,I|114,D|115,O|116,C|111',
			self.board = Board()
			self.board.initFromTileString(board_tiles)


class Turn:

	def __init__(self):
		# Initialization here
		self.play_date = ''
		self.turn_type = ''
		self.turn_points = 0
		self.words = []
		self.played_tiles = []

	def parseJSON(self, dct):
		if 'play_date'		in dct: self.play_date		= dct['play_date']
		if 'type'			in dct: self.turn_type		= dct['type']
		if 'turn_points'	in dct: self.turn_points	= dct['turn_points']
		if 'words'			in dct: self.words			= [(x.strip()) for x in dct['words'].split(',')]
		if 'played_tiles'	in dct: self.played_tiles	= [int(x.strip()) for x in dct['played_tiles'].split(',')]

if __name__ == '__main__':
	jsonString = '{"my_message_alerts": 0, "id": 473619906, "nudge": true, "remaining_tiles": 70, "coins": 40, "my_turn": false, "type": "NORMAL", "opponent": {"username": "kik2004", "fb_show_picture": true, "is_app_user": true, "allow_og_posts": true, "fb_show_name": true, "facebook_name": "Carmelo Saez Martin", "facebook_id": "1776940109", "id": 13583749 }, "my_rack_tiles": "R,U,L,Y,E,A,S", "board_tiles": "A|156,R|187,E|126,N|141,E|112,O|142,O|172,L|157,D|113,I|114,D|115,O|116,C|111", "turns_passed": 0, "last_turn": {"play_date": "07/22/2014 16:25:29 EST", "type": "PLACE_TILE", "turn_points": 12, "words": "AL,OLOR,NO", "played_tiles": "142,157,172,187"}, "my_score": 32, "chat_enable": true, "lang_distribution": "f:4,g:2,d:2,e:1,b:3,c:3,a:1,n:1,o:1,l:1,m:3,j:8,h:4,-:0,i:1,v:4,u:1,t:1,s:1,r:1,q:5,p:3,z:10,y:4,\\\\xf1:8,x:8", "language": "ES", "created": "07/22/2014 15:31:39 EST", "expiration_date": "07/29/2014 16:25:29 EST", "opponent_score": 7, "game_status": "ACTIVE", "extras": [{"usage": "PER_TURN", "cost": 6, "name": "STOCK_PILE", "used": false }, {"usage": "PER_GAME", "cost": 12, "name": "VALIDATOR", "used": false }, {"usage": "ALWAYS", "cost": 2, "name": "WORD_DEFINITION", "used": false } ], "removed_by_opponent": false, "dictionary_version": "1285030781", "turns_played": 3 }'
	dct = json.loads(jsonString)
	response = Game()
	response.parseJSON(dct)
	#response = json.loads(jsonString, object_hook=asLoginResponse)
	print response.__dict__

# Example data JSON
#{
#  'my_message_alerts': 0,
#  'id': 473619906,
#  'nudge': True,
#  'remaining_tiles': 70,
#  'coins': 40,
#  'my_turn': False,
#  'type': 'NORMAL',
#  'opponent': {
#    'username': 'kik2004',
#    'fb_show_picture': True,
#    'is_app_user': True,
#    'allow_og_posts': True,
#    'fb_show_name': True,
#    'facebook_name': 'Carmelo Saez Martin',
#    'facebook_id': '1776940109',
#    'id': 13583749
#  },
#  'my_rack_tiles': 'R,U,L,Y,E,A,S',
#  'board_tiles': 'A|156,R|187,E|126,N|141,E|112,O|142,O|172,L|157,D|113,I|114,D|115,O|116,C|111',
#  'turns_passed': 0,
#  'last_turn': {
#    'play_date': '07/22/2014 16:25:29 EST',
#    'type': 'PLACE_TILE',
#    'turn_points': 12,
#    'words': 'AL,OLOR,NO',
#    'played_tiles': '142,157,172,187'
#  },
#  'my_score': 32,
#  'chat_enable': True,
#  'lang_distribution': 'f:4,g:2,d:2,e:1,b:3,c:3,a:1,n:1,o:1,l:1,m:3,j:8,h:4,-:0,i:1,v:4,u:1,t:1,s:1,r:1,q:5,p:3,z:10,y:4,\xf1:8,x:8',
#  'language': 'ES',
#  'created': '07/22/2014 15:31:39 EST',
#  'expiration_date': '07/29/2014 16:25:29 EST',
#  'opponent_score': 7,
#  'game_status': 'ACTIVE',
#  'extras': [
#    {
#      'usage': 'PER_TURN',
#      'cost': 6,
#      'name': 'STOCK_PILE',
#      'used': False
#    },
#    {
#      'usage': 'PER_GAME',
#      'cost': 12,
#      'name': 'VALIDATOR',
#      'used': False
#    },
#    {
#      'usage': 'ALWAYS',
#      'cost': 2,
#      'name': 'WORD_DEFINITION',
#      'used': False
#    }
#  ],
#  'removed_by_opponent': False,
#  'dictionary_version': '1285030781',
#  'turns_played': 3
#}