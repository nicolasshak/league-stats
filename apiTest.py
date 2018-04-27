import sys, requests, time, json
from riotwatcher import RiotWatcher
from terminaltables import AsciiTable

KEY_PATH = 'json/key.txt'
CHAMPIONS_PATH = 'json/champions.json'
REGION = 'na1'

def getKey():
	with open(KEY_PATH) as file_object:
		key = file_object.readline()
	return key

def getChampions():
	return json.load(open(CHAMPIONS_PATH))

if len(sys.argv) == 1:
	print('Missing summoner name. Correct usage is: python apiTest.py [SummonerName]')
	exit()

Riot = RiotWatcher(getKey())
champions = getChampions()

summoner = Riot.summoner.by_name(REGION, sys.argv[1])
print summoner['name']

matches = Riot.match.matchlist_by_account_recent(REGION, summoner['accountId'])

data = [['Lane', 'Champion', 'Queue']]

for match in matches['matches']:
	data.append([match['lane'], champions[str(match['champion'])], str(match['queue'])])

table = AsciiTable(data)
print table.table