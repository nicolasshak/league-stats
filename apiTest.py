import argparse, json, requests, sys, time
from riotwatcher import RiotWatcher
from terminaltables import AsciiTable

KEY_PATH = 'key.txt'
CHAMPIONS_PATH = 'json/champions.json'
QUEUES_PATH = 'json/queues.json'
REGION = 'na1'

def getKey():
	with open(KEY_PATH) as file_object:
		key = file_object.readline()
	return key

def isValidMatch(args, match):
	if args.byChampion == None or champions[str(match['champion'])] == args.byChampion[0]:
		if not args.byRanked or (args.byRanked and (match['queue'] == 420 or match['queue'] == 440)):
			return True
	return False

def main():
	if len(sys.argv) == 1:
		print('Missing summoner name. Correct usage is: python apiTest.py [SummonerName]')
		exit()

	parser = argparse.ArgumentParser(description = 'calculate winrate')
	parser.add_argument('summonerName', help='summoner name for lookup', type = str)
	parser.add_argument('-A', dest = 'getAllMatches', help = 'get all available matches', action = 'store_true')
	parser.add_argument('-r', dest = 'rankedOnly', help = 'filter to ranked games only', action = 'store_true')
	parser.add_argument('-c', dest = 'byChampion', nargs = 1, help = 'filter by champion', action = 'store')
	parser.add_argument('-q', dest = 'byQueue', help = 'filter by queue', action = 'store_true')
	parser.add_argument('-v', dest = 'verbose', help = 'filter by champion', action = 'store_true')

	args = parser.parse_args()

	Riot = RiotWatcher(getKey())
	champions = json.load(open(CHAMPIONS_PATH))
	queues = json.load(open(QUEUES_PATH))

	summoner = Riot.summoner.by_name(REGION, sys.argv[1])
	print summoner['name']

	if args.getAllMatches:
		matches = Riot.match.matchlist_by_account(REGION, summoner['accountId'])
	else:
		matches = Riot.match.matchlist_by_account_recent(REGION, summoner['accountId'])

	games = [['Lane', 'Champion', 'Queue', 'Win']]
	winrate = [['Wins', 'Losses', 'Winrate']]
	wins = 0;
	losses = 0;

	for match in matches['matches']:
		if isValidMatch(args, match):

			matchDto = Riot.match.by_id(REGION, match['gameId'])
			participantId = -1
			for participant in matchDto['participantIdentities']:
				if participant['player']['summonerName'] == summoner['name']:
					participantId = participant['participantId']
			win = False
			for participant in matchDto['participants']:
				if participant['participantId'] == participantId:
					win =  participant['stats']['win']

			if win:
				wins = wins + 1
			else:
				losses = losses + 1

			games.append([
				match['lane'], 
				champions[str(match['champion'])], 
				queues[str(match['queue'])],
				str(win)
				])

	table_games = AsciiTable(games)
	print table_games.table

	if args.verbose:
		print();

	winrate.append([str(wins), str(losses), float(wins)/float(wins + losses)])
	table_winrate = AsciiTable(winrate)
	print table_winrate.table

if __name__ == '__main__':
	main()