SELECT Company, ProductCount, COUNT(*) AS ModelsCount
FROM Products
GROUP BY Company, ProductCount;