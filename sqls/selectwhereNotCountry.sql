SELECT * 
FROM Customers
WHERE NOT Country = 'USA'
AND NOT Country = 'Germany'
;

-- Number of Records: 67