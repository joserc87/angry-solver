

from ServerSession import ServerSession
import json

class User:
	"""
	An AngryWords user (login user or opponent)
	"""

	def __init__(self):
		"""
		Constructor
		"""
		self.ID = -1
		self.username = ''
		self.email = ''
		self.has_pass = False
		self.language = ''
		self.coins = 0
		self.description = ''
		self.online_status = ''
		self.gender = ''
		self.phone = ''
		self.zip_code = ''
		self.photo_url = ''
		self.allow_og_posts = False
		self.fb_show_name = False
		self.fb_show_picture = False
		self.facebook_id = ''
		self.facebook_name = ''
		self.twitter_name = ''
		self.is_app_user = False
		self.session = None

	def parseJSON(self, dct):
		"""
		Parse a JSON object (dictionary) and stores the data
		"""
		if 'id'				in dct: self.ID				= dct['id']
		if 'username'		in dct: self.username		= dct['username']
		if 'email'			in dct: self.email			= dct['email']
		if 'has_pass'		in dct: self.has_pass		= dct['has_pass']
		if 'language'		in dct: self.language		= dct['language']
		if 'coins'			in dct: self.coins			= dct['coins']
		if 'description'	in dct: self.description	= dct['description']
		if 'online_status'	in dct: self.online_status	= dct['online_status']
		if 'gender'			in dct: self.gender			= dct['gender']
		if 'phone'			in dct: self.phone			= dct['phone']
		if 'zip_code'		in dct: self.zip_code		= dct['zip_code']
		if 'photo_url'		in dct: self.photo_url		= dct['photo_url']
		if 'allow_og_posts'	in dct: self.allow_og_posts	= dct['allow_og_posts']
		if 'fb_show_name'	in dct: self.fb_show_name	= dct['fb_show_name']
		if 'fb_show_picture'in dct: self.fb_show_picture= dct['fb_show_picture']
		if 'facebook_id'	in dct: self.facebook_id	= dct['facebook_id']
		if 'facebook_name'	in dct: self.facebook_name	= dct['facebook_name']
		if 'twitter_name'	in dct: self.twitter_name	= dct['twitter_name']
		if 'is_app_user'	in dct: self.is_app_user	= dct['is_app_user']
		if 'session'		in dct: self.session		= ServerSession(dct['session'])
		#if '__type__' in obj and obj['__type__'] == 'ServerSession':

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

if __name__ == "__main__":
	#jsonString = '{"id": 3459640, "allow_og_posts": true, "coins": 40, "email": "joserc87@gmail.com", "facebook_id": "1299086492", "facebook_name": "Jos\u00e9 Ram\u00f3n Cano Yribarren", "fb_show_name": true, "fb_show_picture": true, "has_pass": true, "is_app_user": true, "language": "ES", "session": {"attributes": {}, "expiration_time": "08/21/2014 15:29:59 EST", "sample": "b965a", "session": "b965ac64be529d281716f73f59431d6473605d65"}, "username": "joserc87"}'
	jsonString = '{"username": "joserc87", "has_pass": true, "description": "", "online_status": "ONLINE", "fb_show_picture": true, "gender": "male", "coins": 40, "fb_show_name": true, "email": "joserc87@gmail.com", "phone": "", "allow_og_posts": true, "facebook_name": "Jos\u00e9 Ram\u00f3n Cano Yribarren", "facebook_id": "1299086492", "twitter_name": "", "is_app_user": true, "zip_code": "", "id": 3459640, "photo_url": ""}'
	dct = json.loads(jsonString)
	response = LoginResponse()
	response.parseJSON(dct)
	#response = json.loads(jsonString, object_hook=asLoginResponse)
	print response.__dict__

# Example data:
#{
#    "allow_og_posts": true,
#    "coins": 40,
#    "email": "joserc87@gmail.com",
#    "facebook_id": "1299086492",
#    "facebook_name": "Jos\u00e9 Ram\u00f3n Cano Yribarren",
#    "fb_show_name": true,
#    "fb_show_picture": true,
#    "has_pass": true,
#    "id": 3459640,
#    "is_app_user": true,
#    "language": "ES",
#    "session": {
#        "attributes": {},
#        "expiration_time": "08/21/2014 15:29:59 EST",
#        "sample": "b965a",
#        "session": "b965ac64be529d281716f73f59431d6473605d65"
#    },
#    "username": "joserc87"
#}

#OR

#{
#  'username': 'joserc87',
#  'has_pass': True,
#  'description': '',
#  'online_status': 'ONLINE',
#  'fb_show_picture': True,
#  'gender': 'male',
#  'coins': 40,
#  'fb_show_name': True,
#  'email': 'joserc87@gmail.com',
#  'phone': '',
#  'allow_og_posts': True,
#  'facebook_name': 'jos\xe9 ram\xf3n cano yribarren',
#  'facebook_id': '1299086492',
#  'twitter_name': '',
#  'is_app_user': True,
#  'zip_code': '',
#  'id': 3459640,
#  'photo_url': ''
#}

