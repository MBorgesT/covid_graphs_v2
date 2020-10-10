from lxml import html
import requests

page = requests.get('https://www.bomjesus.rj.gov.br/site/ver_noticias-10#content')
tree = html.fromstring(page.content)

flag = True
page = 1

xpath = '/html/body/div[7]/div[1]/div[1]/div[' + str(page) + ']/div[' + str(1) + ']/div/h3/a'

link = tree.xpath(xpath)
print(link)

'''
while flag:
	for post in range(1, 11):
		xpath = '/html/body/div[7]/div[1]/div[1]/div[' + str(page) + ']/div[' + str(post) + ']/div/h3/a'

		link = tree.xpath(xpath)
		print(link)
'''