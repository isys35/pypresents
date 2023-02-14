CREATE TABLE "Products"
(
    "Id" SERIAL PRIMARY KEY,
    "ProductName" VARCHAR(30) NOT NULL,
    "Company" VARCHAR(20) NOT NULL,
    "ProductCount" INT DEFAULT 0,
    "Price" NUMERIC NOT NULL,
    "IsDiscounted" BOOL
);