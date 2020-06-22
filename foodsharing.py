# import vk
import requests
import json

# ACCESS_TOKEN = 'a2ad71b9a36ae1748f12a9b3bff7b580f415d8ea3504c95c9fc70c5d28c49bc2fb6d097fbf20b167f3111'
# VERSION = '5.110'



def write_json(data):
	with open('post.json','w') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)


def main():
	DOMAIN = 'sharingfood'
	response = requests.get('https://api.vk.com/method/wall.get', params={'domain': DOMAIN})
	write_json(response.json())



if __name__ == '__main__':
	main()


# ?&access_token=ACCESS_TOKEN&v=VERSION

# session = vk.Session(access_token='tocken')

# gruop = vk.wall.get(owner_id=newstr, count=depth)
# u = JSON.dumps(gruop)