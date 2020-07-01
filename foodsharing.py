import vk_api
import requests
import json


def authorization():
	login, password = '+7_______', '_______'
	vk_session = vk_api.VkApi(login, password)
	try:
		vk_session.auth(token_only = False)
	except vk_api.AuthError as error_msg:
		print(error_msg)
	vk = vk_session.get_api()
	return vk

def getinformation(vk):
	foodsharingroup = '-109125816'
	gruop = vk.wall.get(owner_id=foodsharingroup, count=2)
	write_json(gruop)
	# tools = vk_api.VkTools(vk_session)
	# DOMAIN = 'sharingfood'
	# wall = tools.get_all('wall.get', 5, {'domain': DOMAIN})
	# write_json(wall.json())




def write_json(data):
	with open('information_from_group.json','w', encoding='utf-8') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)


def main():
	vk = authorization()
	getinformation(vk)
	# response = requests.get('https://api.vk.com/method/wall.get', params={'domain': DOMAIN})
	# write_json(response.json())



if __name__ == '__main__':
	main()
