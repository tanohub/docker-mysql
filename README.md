# docker-mysql

At first run, mysql container executes any .sql file in ./provision/mysql/init as temporary root, then restart 

# Tools

```
./tools/generateDummyDataSql/quickinsert.py -h
usage: quickinsert.py [-h] <db> <domains> <max_users>

add fake records to DB: account or info

positional arguments:
  <db>
  <domains>
  <max_users>

options:
  -h, --help   show this help message and exit


db : can be "account" ( DB.table: users_account.accounts ) or "info" ( DB.table: users_info.infos)
domains: domain to create ( use only DB.table: users_account.accounts )
max_users: max_users to create 

ex:
./quickinsert.py account 5 60
- Created domain        kim.com          with: 43 mailboxes 
- Created domain        newman.net               with: 47 mailboxes 
- Created domain        duran-perkins.com                with: 24 mailboxes 
- Created domain        burton.com               with: 17 mailboxes 
- Created domain        perez.info               with: 26 mailboxes 

./quickinsert.py info 5 60
inserted: 1 - Alexander Edwards
...
inserted: 60 - Devin James
```


# Services :
| Service   | Note |
| :---      | :--- |
| http://localhost:8081 | adminer ( root : Password123 ) |
| | |
| tcp://localhost:3306 | mysql |
