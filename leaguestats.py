from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome();
driver.get("https://matchhistory.na.leagueoflegends.com/en/#match-history/NA1/210976050");
try: 
	wait = WebDriverWait(driver, 10)
	elems = wait.until(
		EC.presence_of_element_located((By.CSS_SELECTOR, ".game-summary"))
	);
	print(elems.get_attribute('innerHTML'));
finally:
	driver.close();
