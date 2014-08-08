import json
from Game import Game

class PlayerStatus:

	def __init__(self):
		"""
		Constructor
		"""
		self.notification_id = ''
		self.last_chat_activity = ''
		self.tournaments = []
		self.coins = 0
		self.games = []
		self.available_languages = []
		self.time = ''
		self.unread_conversations = 0
		self.total = 0
		self.celebrity_tournaments = []

	def parseJSON(self, dct):
		"""
		Initialize the object with the content of a JSON
		Args:
			dct (dict): A dictionary like object with the data
		"""
		if 'notification_id'		in dct: self.notification_id		= dct['notification_id']
		if 'last_chat_activity'		in dct: self.last_chat_activity		= dct['last_chat_activity']
		if 'tournaments'			in dct: self.tournaments			= dct['tournaments']			# We don't care about tournaments
		if 'celebrity_tournaments'	in dct: self.celebrity_tournaments	= dct['celebrity_tournaments']	# Nor celebrity_tournamentes
		if 'coins'					in dct: self.coins					= dct['coins']
		if 'available_languages'	in dct: self.available_languages	= dct['available_languages']
		if 'time'					in dct: self.time					= dct['time']
		if 'unread_conversations'	in dct: self.unread_conversations	= dct['unread_conversations']
		if 'total'					in dct: self.total					= dct['total']
		if 'list'					in dct:
			self.games = []
			for item in dct['list']:
				game = Game()
				game.parseJSON(item)
				self.games.append(game)

# Unit test
if __name__ == '__main__':
	jsonString = '{"notification_id": "", "last_chat_activity": "05/21/2014 08:39:29 EST", "tournaments": [], "coins": 40, "list": [{"my_message_alerts": 0, "id": 473619906, "nudge": true, "remaining_tiles": 70, "coins": 40, "my_turn": false, "type": "NORMAL", "opponent": {"username": "kik2004", "fb_show_picture": true, "is_app_user": true, "allow_og_posts": true, "fb_show_name": true, "facebook_name": "Carmelo Saez Martin", "facebook_id": "1776940109", "id": 13583749 }, "my_rack_tiles": "R,U,L,Y,E,A,S", "board_tiles": "A|156,R|187,E|126,N|141,E|112,O|142,O|172,L|157,D|113,I|114,D|115,O|116,C|111", "turns_passed": 0, "last_turn": {"play_date": "07/22/2014 16:25:29 EST", "type": "PLACE_TILE", "turn_points": 12, "words": "AL,OLOR,NO", "played_tiles": "142,157,172,187"}, "my_score": 32, "chat_enable": true, "lang_distribution": "f:4,g:2,d:2,e:1,b:3,c:3,a:1,n:1,o:1,l:1,m:3,j:8,h:4,-:0,i:1,v:4,u:1,t:1,s:1,r:1,q:5,p:3,z:10,y:4,\\\\xf1:8,x:8", "language": "ES", "created": "07/22/2014 15:31:39 EST", "expiration_date": "07/29/2014 16:25:29 EST", "opponent_score": 7, "game_status": "ACTIVE", "extras": [{"usage": "PER_TURN", "cost": 6, "name": "STOCK_PILE", "used": false }, {"usage": "PER_GAME", "cost": 12, "name": "VALIDATOR", "used": false }, {"usage": "ALWAYS", "cost": 2, "name": "WORD_DEFINITION", "used": false } ], "removed_by_opponent": false, "dictionary_version": "1285030781", "turns_played": 3 } ], "available_languages": ["ES", "EN", "FR", "IT", "CA", "PT-BR", "DE", "GA", "RU", "EU", "PT", "EN-UK", "NW", "SV", "NL", "DA"], "time": "07/24/2014 14:08:35 EST", "unread_conversations": 0, "total": 1, "celebrity_tournaments": [] }'
	dct = json.loads(jsonString)
	response = PlayerStatus()
	response.parseJSON(dct)
	#response = json.loads(jsonString, object_hook=asLoginResponse)
	print response.__dict__
#{
#  'notification_id': '',
#  'last_chat_activity': '05/21/2014 08:39:29 EST',
#  'tournaments': [
#    
#  ],
#  'coins': 40,
#  'list': [
#    {
#      'my_message_alerts': 0,
#      'id': 473619906,
#      'nudge': True,
#      'remaining_tiles': 70,
#      'coins': 40,
#      'my_turn': False,
#      'type': 'NORMAL',
#      'opponent': {
#        'username': 'kik2004',
#        'fb_show_picture': True,
#        'is_app_user': True,
#        'allow_og_posts': True,
#        'fb_show_name': True,
#        'facebook_name': 'Carmelo Saez Martin',
#        'facebook_id': '1776940109',
#        'id': 13583749
#      },
#      'my_rack_tiles': 'R,U,L,Y,E,A,S',
#      'board_tiles': 'A|156,R|187,E|126,N|141,E|112,O|142,O|172,L|157,D|113,I|114,D|115,O|116,C|111',
#      'turns_passed': 0,
#      'last_turn': {
#        'play_date': '07/22/2014 16:25:29 EST',
#        'type': 'PLACE_TILE',
#        'turn_points': 12,
#        'words': 'AL,OLOR,NO',
#        'played_tiles': '142,157,172,187'
#      },
#      'my_score': 32,
#      'chat_enable': True,
#      'lang_distribution': 'f:4,g:2,d:2,e:1,b:3,c:3,a:1,n:1,o:1,l:1,m:3,j:8,h:4,-:0,i:1,v:4,u:1,t:1,s:1,r:1,q:5,p:3,z:10,y:4,\xf1:8,x:8',
#      'language': 'ES',
#      'created': '07/22/2014 15:31:39 EST',
#      'expiration_date': '07/29/2014 16:25:29 EST',
#      'opponent_score': 7,
#      'game_status': 'ACTIVE',
#      'extras': [
#        {
#          'usage': 'PER_TURN',
#          'cost': 6,
#          'name': 'STOCK_PILE',
#          'used': False
#        },
#        {
#          'usage': 'PER_GAME',
#          'cost': 12,
#          'name': 'VALIDATOR',
#          'used': False
#        },
#        {
#          'usage': 'ALWAYS',
#          'cost': 2,
#          'name': 'WORD_DEFINITION',
#          'used': False
#        }
#      ],
#      'removed_by_opponent': False,
#      'dictionary_version': '1285030781',
#      'turns_played': 3
#    }
#  ],
#  'available_languages': [
#    'ES',
#    'EN',
#    'FR',
#    'IT',
#    'CA',
#    'PT-BR',
#    'DE',
#    'GA',
#    'RU',
#    'EU',
#    'PT',
#    'EN-UK',
#    'NW',
#    'SV',
#    'NL',
#    'DA'
#  ],
#  'time': '07/24/2014 14:08:35 EST',
#  'unread_conversations': 0,
#  'total': 1,
#  'celebrity_tournaments': [
#    
#  ]
#}