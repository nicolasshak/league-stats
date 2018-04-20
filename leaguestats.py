import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Game():
	
	def __init__(self, result, champion):
		# false indicates loss, true idicates win
		self.result = result;
		self.champion = champion;

	def tostring(self):
		print(self.champion + ' : ' + str(self.result));

class Champion():

	def __init__(self, name):
		self.name = name;
		self.wins = 0;
		self.losses = 0;

	def add_win(self):
		wins += 1;

	def add_loss(self):
		losses += 1;

	def calc_winrate(self):
		return float(self.wins)/float(self.wins + self.losses);

	def tostring(self):
		print(self.name + ': ' + str(self.calc_winrate));

NUM_GAMES = 30;
if len(sys.argv) > 1:
	NUM_GAMES = int(sys.argv[1]);

driver = webdriver.Chrome();
driver.get("https://matchhistory.na.leagueoflegends.com/en/#match-history/NA1/207127188");
try: 
	wait = WebDriverWait(driver, 10)
	wait.until(
		EC.presence_of_element_located((By.CSS_SELECTOR, '.game-summary'))
	);

	while True:
		driver.execute_script('window.scrollBy(0, 1000)');	
		elems = driver.find_elements_by_class_name('game-summary');
		if len(elems) >= NUM_GAMES:
			break;

	games = [];
	for elem in elems:
		if 'defeat' not in elem.find_element_by_class_name('result-marker').get_attribute('class'):
			result = True;
		else:
			result = False;
		champ = elem.find_element_by_class_name('champion-nameplate-name').find_element_by_class_name('binding').text;
		games.append(Game(result, champ));

	champions_played = [];
	for game in games:
		champion_found = False;
		for champion_played in champions_played:
			if champion_played.name == game.champion:
				champion_found = True;
				if game.result:
					champion_played.add_win();
				else:
					champion_played.add_loss();
			if not champion_found:
				champions_played.append(Champion(game.champion));
				if game.result:
					champion_played.add_win();
				else:
					champion_played.add_loss();

	for champ in champions_played:
		tostring(champ);

finally:
	driver.close();

