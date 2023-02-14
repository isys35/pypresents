SELECT Company, COUNT(*) AS ModelsCount
FROM Products
GROUP BY Company
HAVING COUNT(*) > 1;