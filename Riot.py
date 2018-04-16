import requests

DOMAIN = 'https://na1.api.riotgames.com/'
SUMMONER_BY_NAME =  'lol/summoner/v3/summoners/by-name/'
MATCHLIST = 'lol/match/v3/matchlists/by-account/'
CHAMPION_BY_ID = '/lol/static-data/v3/champions/'
API_KEY = '?api_key=RGAPI-6fc58367-b9c7-40dc-93bd-a7d81e53e218'

def makeURL(api, arg):
	return DOMAIN + api + arg + API_KEY

def makeOtherURL(api, arg, aug):
	return DOMAIN + api + arg + aug + API_KEY

def getSummonerByName(summoner_name):
	return requests.get(makeURL(SUMMONER_BY_NAME, summoner_name)).json()

def getAllMatches(summoner_id):
	return requests.get(makeURL(MATCHLIST, str(summoner_id))).json()

def getRecentMatches(summoner_id):
	return requests.get(makeOtherURL(MATCHLIST, str(summoner_id), '/recent')).json()

def getChampion(champion_id):
	return requests.get(makeURL(CHAMPION_BY_ID, str(champion_id))).json()
