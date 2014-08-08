import requests
import json
from urllib import urlencode
from LoginResponse import LoginResponse 
from PlayerStatus import PlayerStatus

class WebServiceHelper:

	# The default server
	SERVER = "https://api.apalabrados.com/api/"

	def __init__(self):
		""" Constructor """
		self.session = requests.Session()
		self.server = WebServiceHelper.SERVER
		self.session = None
		self.user = None
	def getLoginURL(self):
		""" Builds the URL to login a user in the system: https://api.apalabrados.com/api/login """
		return self.server + "login"

	def getGamesURL(self, userID):
		""" Builds the URL to retrieve the list of games: https://api.apalabrados.com/api/users/[UserID]/games """
		return self.server + "users/" + str(userID) + "/games"


	def login(self, email, password, language="es"):
		"""
		Calls https://api.apalabrados.com/api/login with username+password and stores the User info and session (+ extra cookie)
		Returns True if the login was successful
		"""
		try:
			data = json.dumps({"email" : email, "password" : password, "language" : language})
			headers = {"content-type" : "application/json"}
			# POST
			response = self.session.post(self.getLoginURL(), data=data, headers=headers)
			if response.status_code == requests.codes.ok:
				self.user = LoginResponse()
				self.user.parseJSON(response.json())
				return True
			else:
				return False
		except requests.ConnectionError:
			return False
		except:
			print "Unexpected error"
			raise
		return False

	def getGames(self):
		""" Calls https://api.apalabrados.com/api/users/[UserID]/games and returns the list of current games """
		try:
			headers = {"content-type" : "application/json"}
			if self.user != None:
				# GET
				response = self.session.get(self.getGamesURL(self.user.ID), headers=headers)
				if response.status_code == requests.codes.ok:
					playerStatus = PlayerStatus()
					playerStatus.parseJSON(response.json())
					return playerStatus
				else:
					return None
			else:
				print "User not logged in"
				return None

		except requests.ConnectionError:
			return None
		except:
			print "Unexpected error"
			raise
		return None

if __name__ == "__main__":
	server = WebServiceHelper()
	if server.login("joserc87@gmail.com", "casco51141"):
		print "Loged in!"
		print "UserID = ", server.user.ID
		playerStatus = server.getGames()
		if playerStatus != None:
			print "Board:"
			print playerStatus.games[0].board.toString()
	else:
		print "There was a problem logging in"


