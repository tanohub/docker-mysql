#!/usr/bin/env python3

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


from faker import Faker
import pymysql
import random

MYSQL_DATABASE_HOST="localhost"
MYSQL_DATABASE_PORT=3306
MYSQL_DATABASE_USER="root"
MYSQL_DATABASE_PASSWORD="Password123"
MYSQL_DATABASE_NAME="DB02"
MYSQL_DATABASE_TABLE_NAME="db02tab01"

conn = pymysql.connect(host=MYSQL_DATABASE_HOST,port=MYSQL_DATABASE_PORT, user=MYSQL_DATABASE_USER, password=MYSQL_DATABASE_PASSWORD, db=MYSQL_DATABASE_NAME)
cur = conn.cursor()

fake = Faker()

# Fake Domain ex: X domains with random users ( between 0 and rows_max )
domains=1
rows_max=1500

for domain_curr in range(domains) :
	domain=fake.domain_name()
	for i in range(random.randrange(rows_max)):
		user=fake.first_name()
		password=fake.password(length=12)
		cur.execute('insert into ' + MYSQL_DATABASE_TABLE_NAME + ' (user,domain,password) VALUES (%s,%s,%s)', (user,domain,password));
		conn.commit()
	print('- Created domain \t' + domain + '\t\t with: ' + str(i+1) + ' mailboxes ')

# Fake Person ex: create 10000 fake humans )
#for i in range(10000):
#	print('insert num: ' + str(i))
#	name=fake.first_name()
#	surname=fake.last_name()
#	email=fake.email()
#	birth=fake.date()
#	cur.execute('insert into ' + MYSQL_DATABASE_TABLE_NAME + ' (name,surname,email,birth) VALUES (%s,%s,%s,%s)', (name,surname,email,birth));
#	conn.commit()
