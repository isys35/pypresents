SELECT Company, COUNT(*) AS Models, SUM(ProductCount) AS Units
FROM Products
WHERE Price * ProductCount > 80000
GROUP BY Company
HAVING SUM(ProductCount) > 2
ORDER BY Units DESC;