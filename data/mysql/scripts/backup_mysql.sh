#!/bin/sh
 
# Create Backup storage directory
backupfolder="/backup/mysql"
if [ ! -d "${backupfolder}" ]; then
	mkdir -p ${backupfolder}
fi
 
# Number of days to store the backup
keep_day=7

mysql_host="localhost"
mysql_username="root"
mysql_password="Password123"

echo "--- START mysql Backup : $(date +%Y_%m-%d_%H-%M)"
echo " "
mysql --user=${mysql_username} --password=${mysql_password} -N -e 'show databases' | while read dbname
do
        sqlfile="$backupfolder/$dbname-$(date +%Y-%m-%d_%H-%M).sql.gz" 

        echo "- START DB Backup - $dbname : $(date +%Y_%m-%d_%H-%M)"
 
        # https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html
	mysqldump \
                --user=${mysql_username} \
                --password=${mysql_password} \
		--host=${mysql_host} \
		--force \
		--events \
		--complete-insert \
		--routines \
		--triggers \
		--single-transaction \
		"$dbname" | gzip > ${sqlfile}
	echo "- END DB Backup - $dbname : $(date +%Y_%m-%d_%H-%M)"
        echo " "
done
 
# Delete old backups 
echo "--- Deleting old backups"
find $backupfolder -mtime +$keep_day -delete
 
echo "--- END mysql Backup : $(date +%Y_%m-%d_%H-%M)"
