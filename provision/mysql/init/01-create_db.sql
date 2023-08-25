-- create databases
-- users_account : sample user,domain,password
-- users_info : sample name,surname,email,birth
CREATE DATABASE IF NOT EXISTS `users_account`;
CREATE DATABASE IF NOT EXISTS `users_info`;

-- create DBs user and grant rights
CREATE USER 'ua_rw_user01'@'%' IDENTIFIED BY 'Password123';
GRANT ALL PRIVILEGES ON users_account.* TO 'ua_rw_user01'@'%';

CREATE USER 'ui_rw_user01'@'%' IDENTIFIED BY 'Password123';
GRANT ALL PRIVILEGES ON users_info.* TO 'ui_rw_user01'@'%';

-- create reader user for both DB
CREATE USER 'ro_user01'@'%' IDENTIFIED BY 'Password123';
GRANT SELECT ON users_account.* TO 'ro_user01'@'%';
GRANT SELECT ON users_info.* TO 'ro_user01'@'%';

USE users_account;
CREATE TABLE accounts (
    user varchar(255),
    domain varchar(255),
    password varchar(255)
);

USE users_info;
CREATE TABLE infos (
    name varchar(255),
    surname varchar(255),
    email varchar(255),
    birth date
);
