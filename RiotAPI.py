import requests

KEY_PATH = 'key.txt'
DOMAIN = 'https://na1.api.riotgames.com/lol/'

#API endpoints
CHAMPION_MASTERY = 'champion-mastery/v3/champion-masteries/by-summoner/'
SUMMONER_BY_NAME =  'summoner/v3/summoners/by-name/'
MATCHLIST = 'match/v3/matchlists/by-account/'
MATCH_BY_ID = 'match/v3/matches/'
CHAMPION_BY_ID = 'static-data/v3/champions/'

def getKey():
	with open(KEY_PATH) as file_object:
		key = file_object.readline()
	return key

class RiotAPI:

	# Constructors
	def __init__(self):
		self.API_KEY = '?api_key=' + getKey()

	# Helpers
	def makeURL(self, api, arg):
		return DOMAIN + api + arg + self.API_KEY

	# Champion Mastery
	def getChampionMasteries(self, summoner_id):
		return requests.get(makeURL(CHAMPION_MASTERY, summoner_id))

	def getChampionMastery(self, summoner_id, champion_id):
		return requests.get(makeURL(CHAMPION_MASTERY, summoner_id + 'by-champion/' + champion))

	def getMasteryScore(self, summoner_id, champion_id):

	# Champion
	def getChampions(self):

	def getChampion(self, champion_id):
		return requests.get(makeURL(CHAMPION_BY_ID, str(champion_id)))

	# League
	def getChallengerLeague(self, queue):

	def getLeague(self, league_id):

	def getMasterLeague(self, queue):

	def getLeaguePositions(self, summoner_id):

	# LoL Static Data


	# LoL Status
	# Match
	def getMatch(match_id):
		return requests.get(makeURL(MATCH_BY_ID, match_id))

	def getAllMatches(summoner_id):
		return requests.get(makeURL(MATCHLIST, str(summoner_id)))

	def getRecentMatches(summoner_id):
		return requests.get(makeURL(MATCHLIST, str(summoner_id)) + '/recent'))

	# Spectator
	# Summoner
	def getSummonerByName(self, summoner_name):
		return requests.get(self.makeURL(SUMMONER_BY_NAME, summoner_name))

	# Third Party Code
	# Tournament Stub
	# Tournament
