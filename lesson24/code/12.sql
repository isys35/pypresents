BEGIN;
--
-- Create model Book
--
CREATE TABLE "books_book" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
		"name" varchar(100) NOT NULL,
		"description" text NULL,
		"price" real NULL,
		"published" datetime NOT NULL
);
CREATE INDEX "books_book_published_58fde1b5" ON "books_book" ("published");
COMMIT;