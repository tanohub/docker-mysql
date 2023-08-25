#!/usr/bin/env python3

from faker import Faker
import pymysql
import random
import argparse
 
p = argparse.ArgumentParser(description='add fake records to DB: account or info')
p.add_argument('db', type=str, metavar='<db>')
p.add_argument('domains', type=int, metavar='<domains>')
p.add_argument('max_users', type=int, metavar='<max_users>')
args = p.parse_args()

domains=args.domains
max_users=args.max_users

MYSQL_DATABASE_HOST="localhost"
MYSQL_DATABASE_PORT=3306
MYSQL_DATABASE_USER="root"
MYSQL_DATABASE_PASSWORD="Password123"

#https://faker.readthedocs.io/en/stable/providers.html
# ex :
# "NAME": fake.first_name()
# "SURNAME": fake.last_name()
# "PHONE": fake.phone_number()
# "EMAIL": fake.email()
# "ADDRESS": fake.address()
# "POSTAL_CODE": fake.postcode()
# "REGION": fake.state()
# "COUNTRY": fake.country()
# "WORD": fake.word()
# "TEXT": fake.text()
# "NUMBER": fake.random_number()
# "CURRENCY_CODE": fake.currency_code()
# "ALPHA_NUMERIC": fake.bothify(text='??##?#?##?')
# "UUID": fake.uuid4()
# "UUID_WITHOUT_HYPHEN": str(fake.uuid4()).replace("-", "")
# "DATE": fake.date()
# "DATE_TIME": fake.date_time()
# "BOOLEAN": fake.boolean()
# "UNIQUE_ID": fake.unique.bothify(text='##########')

# accounts DB
if (args.db =='account'):
	MYSQL_DATABASE_NAME="users_account"
	MYSQL_DATABASE_TABLE_NAME="accounts"

	conn = pymysql.connect(host=MYSQL_DATABASE_HOST,port=MYSQL_DATABASE_PORT, user=MYSQL_DATABASE_USER, password=MYSQL_DATABASE_PASSWORD, db=MYSQL_DATABASE_NAME)
	cur = conn.cursor()

	fake = Faker()

	# Fake Domain ex: create X domains with random users ( between 0 and max_users )
	for domain_curr in range(domains) :
		domain=fake.domain_name()
		for i in range(random.randrange(max_users)):
			user=fake.first_name()
			password=fake.password(length=12)
			cur.execute('insert into ' + MYSQL_DATABASE_TABLE_NAME + ' (user,domain,password) VALUES (%s,%s,%s)', (user,domain,password));
			conn.commit()
		print('- Created domain \t' + domain + '\t\t with: ' + str(i+1) + ' mailboxes ')


# users DB
elif (args.db =='info'):
	MYSQL_DATABASE_NAME="users_info"
	MYSQL_DATABASE_TABLE_NAME="infos"

	conn = pymysql.connect(host=MYSQL_DATABASE_HOST,port=MYSQL_DATABASE_PORT, user=MYSQL_DATABASE_USER, password=MYSQL_DATABASE_PASSWORD, db=MYSQL_DATABASE_NAME)
	cur = conn.cursor()

	fake = Faker()

	# Fake Person ex: create max_users fake humans )
	for i in range(max_users):
		name=fake.first_name()
		surname=fake.last_name()
		email=fake.email()
		birth=fake.date()
		cur.execute('insert into ' + MYSQL_DATABASE_TABLE_NAME + ' (name,surname,email,birth) VALUES (%s,%s,%s,%s)', (name,surname,email,birth));
		conn.commit()
		print('inserted: ' + str(i+1) + ' - ' + name + ' ' + surname)
