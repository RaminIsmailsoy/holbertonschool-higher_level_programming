-- Write a script that creates a table called first_table in the current database in your MySQL server.
-- first_table description: id INT, name VARCHAR(256). The database name will be passed as an argument
-- cat new_table_name.sql | mysql -hlocalhost -uroot database_name
-- If the table first_table already exists, your script should not fail
CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));
