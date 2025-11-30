-- Write a script that inserts a new row in the table "first_table"
-- New row: id = 89,  name = Best School,  The database name will be passed as an argument
-- cat insert_value.sql | mysql -hlocalhost -uroot database_name
INSERT INTO first_table(id, name) VALUES(89, "Best School");
