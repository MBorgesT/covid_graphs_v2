
import pytesseract, cv2, re
import numpy as np
from datetime import datetime

FOLDER = 'images/'

def get():
	kernel = np.ones((2,1),np.uint8)

	img = cv2.imread(FOLDER + 'temp.png')
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,45,5)
	#img = cv2.dilate(img, kernel, iterations = 1)
	#img = cv2.GaussianBlur(img, (1,1), sigmaX=1, sigmaY=1, borderType = cv2.BORDER_DEFAULT)
	#img = cv2.blur(img,(3,3))

	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
	img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

	img_data = img[110:158, 485:715]
	img_confirmados = img[285:336, 668:746]
	img_monitorados = img[356:420, 668:746]
	img_casos_curados = img[438:492, 668:746]
	img_obitos_investigacao = img[510:570, 668:746]
	img_obitos_confirmados = img[590:650, 668:746]


	'''
	cv2.imshow("cropped", img_obitos_investigacao)
	cv2.waitKey(0)
	'''

	'''
	print(repr(pytesseract.image_to_string(img_data)))
	print(repr(pytesseract.image_to_string(img_confirmados)))
	print(repr(pytesseract.image_to_string(img_monitorados)))
	print(repr(pytesseract.image_to_string(img_casos_curados)))
	print(repr(pytesseract.image_to_string(img_obitos_investigacao)))
	print(repr(pytesseract.image_to_string(img_obitos_confirmados)))
	'''

	config = '--psm 7 --oem 3 -c tessedit_char_whitelist=.0123456789'

	str_data = pytesseract.image_to_string(img_data, config=config)[:10]
	str_confirmados = pytesseract.image_to_string(img_confirmados, config=config).split('\n')[0]
	str_monitorados = pytesseract.image_to_string(img_monitorados, config=config).split('\n')[0]
	str_casos_curados = pytesseract.image_to_string(img_casos_curados, config=config).split('\n')[0]
	str_obitos_investigacao = pytesseract.image_to_string(img_obitos_investigacao, config=config).split('\n')[0]
	str_obitos_confirmados = pytesseract.image_to_string(img_obitos_confirmados, config=config).split('\n')[0]

	info = [
		str_data,
		int(str_confirmados),
		int(str_monitorados),
		int(str_casos_curados),
		int(str_obitos_investigacao),
		int(str_obitos_confirmados)
	]

	return info


def __main__():
	print(get())