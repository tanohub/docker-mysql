# create databases
CREATE DATABASE IF NOT EXISTS `DB01`;
CREATE DATABASE IF NOT EXISTS `DB02`;

# create DB01 user and grant rights
CREATE USER 'db01user01'@'%' IDENTIFIED BY 'Password123';
GRANT ALL PRIVILEGES ON DB01.* TO 'db01user01'@'%';

# create DB02 user and grant rights
CREATE USER 'db02user01'@'%' IDENTIFIED BY 'Password123';
GRANT ALL PRIVILEGES ON DB02.* TO 'db02user01'@'%';
