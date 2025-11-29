-- Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server.
mysql -uroot -e "SHOW GRANTS FOR 'user_0d_1'@'localhost'"
mysql -uroot -e "SHOW GRANTS FOR 'user_0d_2'@'localhost'"
