-- Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server.
echo "SHOW GRANTS FOR 'user_0d_1'@'localhost'" | mysql -hlocalhost -uroot
echo "SHOW GRANTS FOR 'user_0d_2'@'localhost'" | mysql -hlocalhost -uroot
