-- Write a script that displays the number of records with id = 89 in the table "first_table" of the database
-- cat count_records.sql | mysql -hlocalhost -uroot database_name | tail -1
SELECT COUNT(*) FROM first_table WHERE ID=89;
