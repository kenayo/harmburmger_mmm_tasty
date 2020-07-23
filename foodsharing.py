import vk_api
import requests
import json
import re
import logging
from sqlalchemy import MetaData, Table, create_engine, Column, Integer, String
from sqlalchemy.dialects.postgresql import insert



logging.basicConfig(
	level=logging.INFO,
	format='%(name)s %(levelname)s %(asctime)s    '
			'%(message)s',
	datefmt='%I:%M:%S',
	handlers=[
        logging.FileHandler("foodsharing.log"),
        # logging.StreamHandler()
    ]
)
log = logging.getLogger()


def authorization():
	login, password = '+7___', '___'
	vk_session = vk_api.VkApi(login, password)
	try:
		vk_session.auth(token_only = False)
	except vk_api.AuthError as error_msg:
		print(error_msg)
	vk = vk_session.get_api()
	log.info("Vk session has been started login %s", login)
	return vk

def getinformation(vk):
	foodsharingroupID = '-109125816'
	group = vk.wall.get(owner_id=foodsharingroupID, count=2)
	write_json(group)
	return group["items"][1]["text"]


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
	geodata = requests.get(requestwithaddress)
	return geodata

def write_db(vkmessage):
	metadata = MetaData()
	domains = Table(
		'products',
		metadata,
		Column('id', Integer, primary_key=True),
		Column('product', String),
		Column('all_message', String)
	)

	engine = create_engine('postgresql://foodsharing_user:___@192.168.56.102/foodsharing_db')
	with engine.begin() as conn:
		query = domains.insert().values([
			{'product': 'test', 'all_message': vkmessage}
		]).returning(*domains.columns)

		data = conn.execute(query).fetchall()


def main():

	vk = authorization()
	text = getinformation(vk)
	write_db(text)
	address = addressparser(text)
	geodata(address)



if __name__ == '__main__':
	main()

"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

class Post(DeclarativeBase):
    __tablename__ = 'foodsharing_db'

    id = Column(Integer, primary_key=True)
    name = Column('product', String)
    url = Column('all_message', String)

    def __repr__(self):
        return "".format(self.code)
        """