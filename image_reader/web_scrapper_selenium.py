from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://www.bomjesus.rj.gov.br/site/ver_noticias-10#content')


flag = True
while flag:
	page = 1

	for i in range(1,11):
		print(i)
		link = None
		img = None

		xpath = '/html/body/div[7]/div[1]/div[1]/div[' + str(page) + ']/div[' + str(i) + ']/div/h3/a'
		print(xpath)
		while True:
			try:
				link = driver.find_element(By.XPATH, xpath)
				break
			except:
				None

		print(link.get_attribute('title'))
		if 'BOLETIM CORONAVÍRUS' in link.get_attribute('title'):
			link.click()




