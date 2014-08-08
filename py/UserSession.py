import json


class UserSession:

	def  __init__(self, dct):
		"""
		Constructor.
		Args:
			dct (dict): A dictionnary containing the data to initialize the object
		"""
		self.attributes = None
		self.expiration_time = ""
		self.sample = ""
		self.session = ""
		self.parseJSON(dct)

	def parseJSON(self, dct):
		"""
		Init the object with the content of a dictionary
		"""
		if 'attributes' in dct: self.attributes = dct['attributes']
		if 'expiration_time' in dct: self.expiration_time = dct['expiration_time']
		if 'sample' in dct: self.sample = dct['sample']
		if 'session' in dct: self.session = dct['session']

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

# Example data
#	"session": {
#        "attributes": {},
#        "expiration_time": "08/21/2014 15:29:59 EST",
#        "sample": "b965a",
#        "session": "b965ac64be529d281716f73f59431d6473605d65"
#    },