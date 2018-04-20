import requests

DOMAIN = 'https://na1.api.riotgames.com/'
SUMMONER_BY_NAME =  'lol/summoner/v3/summoners/by-name/'
MATCHLIST = 'lol/match/v3/matchlists/by-account/'
MATCH_BY_ID = '/lol/match/v3/matches/'
CHAMPION_BY_ID = '/lol/static-data/v3/champions/'
API_KEY = '?api_key=RGAPI-dbe0b535-8e03-4bf8-9108-409fd55c048a'

def makeURL(api, arg):
	return DOMAIN + api + arg + API_KEY

def makeOtherURL(api, arg, aug):
	return DOMAIN + api + arg + aug + API_KEY

def getSummonerByName(summoner_name):
	return requests.get(makeURL(SUMMONER_BY_NAME, summoner_name))

def getAllMatches(summoner_id):
	return requests.get(makeURL(MATCHLIST, str(summoner_id)))

def getRecentMatches(summoner_id):
	return requests.get(makeOtherURL(MATCHLIST, str(summoner_id), '/recent'))

def getMatch(match_id):
	return requests.get(makeURL(MATCH_BY_ID, match_id))

def getChampion(champion_id):
	return requests.get(makeURL(CHAMPION_BY_ID, str(champion_id)))
