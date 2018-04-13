import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

NUM_GAMES = 30;
if len(sys.argv) > 1:
	NUM_GAMES = int(sys.argv[1]);
	print(sys.argv[1]);

driver = webdriver.Chrome();
driver.get("https://matchhistory.na.leagueoflegends.com/en/#match-history/NA1/210976050");
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
	win = 0;
	loss = 0;
	champ = '';
	result = '';
	for elem in elems:
		result = 'loss';
		if 'defeat' not in elem.find_element_by_class_name('result-marker').get_attribute('class'):
			result = 'win';
			win += 1;
		else:
			loss += 1;
		champ = elem.find_element_by_class_name('champion-nameplate-name').find_element_by_class_name('binding').text;
		#print(champ + ' : ' + result);
	print('wins: ' + str(win) + ', losses: ' + str(loss) +  ', winrate: ' + str(float(win)/float(loss + win)));
finally:
	driver.close();
