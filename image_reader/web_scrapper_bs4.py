from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests, image_info, csv, os

os.remove('data.csv')

IMG_FOLDER = 'images/'

url = 'https://www.bomjesus.rj.gov.br/site/ver_noticias-10#content'
html = urlopen(url)

bs = BeautifulSoup(html, 'lxml')


flag = True
index = 1
while flag:
	aux = 'content_page_' + str(index)
	content_page = bs.find('div', id=aux)

	for div in content_page.find_all('div', recursive=False):
		div_interno = div.find('div', recursive=False)
		link = div_interno.find('a')

		if 'BOLETIM CORONAVÍRUS (COVID -19)' in link['title']:
			try:
				url_noticia = 'https://www.bomjesus.rj.gov.br/site/' + link['href']
				html_noticia = urlopen(url_noticia)
				bs_noticia = BeautifulSoup(html_noticia, 'lxml')

				imagens_div = bs_noticia.find('div', {'class': 'jcarousel'})

				info = None
				for img in imagens_div.find_all('img'):
					try:
						image_url = 'https://www.bomjesus.rj.gov.br/site/' + img['src']
						resource = urlopen(image_url)
						output = open(IMG_FOLDER + 'temp.png','wb')
						output.write(resource.read())
						output.close()

						info = image_info.get()
						break
					except:
						None

				print(info)

				if info is not None:
					file = open('data.csv', mode='a')
					csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
					csv_writer.writerow(info)
					file.close()
					
			except:
				print('error')

	index += 1