import Riot, sys, requests, time

if len(sys.argv) == 1:
	print('Missing summoner name. Correct usage is: python apiTest.py [SummonerName]')
	exit()

summoner_name = sys.argv[1];
summoner = Riot.getSummonerByName(summoner_name)
summonerId = summoner.json()[u'accountId']

recent_matches = Riot.getRecentMatches(summonerId).json()
for match in recent_matches['matches']:
	print Riot.getChampion(match['champion']).headers
	time.sleep(1);