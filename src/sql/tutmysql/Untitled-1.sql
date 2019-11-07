-- DROP TABLE pet;
-- CREATE TABLE pet (
--     name VARCHAR(20),
--     owner VARCHAR(20),
--     species VARCHAR(20),
--     sex CHAR(1),
--     birth DATE,
--     death DATE
-- );

-- LOAD DATA LOCAL 
-- INFILE '/home/percy/Projects/Tutorials/PythonTutorial/src/sql/tutmysql/pet.txt' 
-- INTO TABLE pet FIELDS TERMINATED BY ' ';

-- SELECT * FROM pet;

-- INSERT INTO pet VALUES 
-- ('Puffball','Diane','hamster','f','1999-03-30',NULL);

-- HELP 'CREATE TABLE';

-- SELECT name, birth, CURDATE(), TIMESTAMPDIFF(YEAR, birth, CURDATE()) AS age
-- from pet ORDER BY age;

-- SELECT name, birth FROM pet 
-- WHERE MONTH(birth) = MONTH(DATE_ADD(CURDATE(), INTERVAL 2 MONTH));

-- SELECT '2018-10-32' + INTERVAL 1 DAY;

-- SELECT owner, COUNT(*) FROM pet GROUP BY owner;

-- CREATE TABLE event (
--     name VARCHAR(20),
--     date DATE,
--     type VARCHAR(15),
--     remark VARCHAR(255)
-- );

-- LOAD DATA LOCAL
-- INFILE '/home/percy/Projects/Tutorials/PythonTutorial/src/sql/tutmysql/event.txt'
-- INTO TABLE event;

-- SELECT * FROM event;

-- SELECT *
-- FROM pet INNER JOIN event ON pet.name = event.name
-- WHERE event.type = 'litter';

-- SELECT p1.name as n1, p2.name as n2
-- FROM pet as p1 INNER JOIN pet as p2;
-- WHERE event.type = 'litter';

-- SELECT e1.name as n1, e2.name as n2
-- FROM event AS e1 INNER JOIN event as e2;

-- CREATE TABLE shop (
--     article INT(4) UNSIGNED ZEROFILL DEFAULT '0000' NOT NULL,
--     dealer CHAR(20) DEFAULT '' NOT NULL,
--     price DOUBLE(16, 2) DEFAULT '0.00' NOT NULL,
--     PRIMARY KEY(article, dealer)
-- );
-- INSERT INTO shop VALUES
-- (1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),
-- (3,'C',1.69),(3,'D',1.25),(4,'D',19.95);

show create table shop;