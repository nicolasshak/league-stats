import Riot, sys, requests

if len(sys.argv) == 1:
	print('Missing summoner name. Correct usage is: python apiTest.py [SummonerName]')

summoner_name = sys.argv[1];
summoner = Riot.getSummonerByName(summoner_name)
summonerId = summoner[u'accountId']

recent_matches = Riot.getRecentMatches(summonerId)

print Riot.getChampion(recent_matches[u'matches'][0][u'champion'])[u'name']