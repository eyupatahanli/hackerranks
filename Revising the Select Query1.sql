--Query all columns for all American cities in the CITY table with populations larger than 100000.
--The CountryCode for America is USA.
--The CITY table is described as follows:

SELECT *
FROM CITY
WHERE CountryCode = 'USA' AND Population > 100000;