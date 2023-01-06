from faker import Faker
import pymysql

MYSQL_DATABASE_HOST="localhost"
MYSQL_DATABASE_PORT=3306
MYSQL_DATABASE_USER="root"
MYSQL_DATABASE_PASSWORD="Password123"
MYSQL_DATABASE_NAME="DB01"
MYSQL_DATABASE_TABLE_NAME="db01tab01"

conn = pymysql.connect(host=MYSQL_DATABASE_HOST,port=MYSQL_DATABASE_PORT, user=MYSQL_DATABASE_USER, password=MYSQL_DATABASE_PASSWORD, db=MYSQL_DATABASE_NAME)
cur = conn.cursor()

fake = Faker()

for i in range(10000):
	print('insert num: ' + str(i))
	name=fake.first_name()
	surname=fake.last_name()
	email=fake.email()
	birth=fake.date()
	cur.execute('insert into ' + MYSQL_DATABASE_TABLE_NAME + ' (name,surname,email,birth) VALUES (%s,%s,%s,%s)', (name,surname,email,birth));
	conn.commit()
