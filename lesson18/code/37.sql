SELECT Company, COUNT(*) AS ModelsCount
FROM Products
WHERE Price > 30000
GROUP BY Company
ORDER BY ModelsCount DESC;