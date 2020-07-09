import vk_api
import requests
import json
import re


def authorization():
	login, password = '+7___', '___'
	vk_session = vk_api.VkApi(login, password)
	try:
		vk_session.auth(token_only = False)
	except vk_api.AuthError as error_msg:
		print(error_msg)
	vk = vk_session.get_api()
	return vk

def getinformation(vk):
	foodsharingroupID = '-109125816'
	gruop = vk.wall.get(owner_id=foodsharingroupID, count=2)
	write_json(gruop)
	return gruop["items"][1]["text"]


def write_json(data):
	with open('information_from_group.json','w', encoding='utf-8') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)

# def read_json(data):
# 	with open('information_from_group.json','w', encoding='utf-8') as file:
# 		json.dump(data, file, indent=2, ensure_ascii=False)

def addressparser(text):
	addresspatterns = ['^м.\s*[а-яА-Я]', '^ул.\s*[а-яА-Я]',
					'^пл.\s*[а-яА-Я]', '^Набережная\s[а-яА-Я]'
					]
	address = []
	for pattern in addresspatterns:
		address.extend(re.findall(pattern,text))
		write_json(address)
		return address

def timeparser():
	pass

def geodata(address):
	APIkey = '42604df8-0cd1-40c9-ad47-8a62f88fbfb1'
	addressforrequest = '+'.join(address)
	requestwithaddress = 'https://geocode-maps.yandex.ru/1.x/?apikey=' + APIkey + '&geocode=' + addressforrequest
	# print(requestwithaddress)
	geodata = requests.get(requestwithaddress)
	# print(geodata)
	return geodata






def main():
	vk = authorization()
	text = getinformation(vk)
	address = addressparser(text)
	geodata(address)




if __name__ == '__main__':
	main()
