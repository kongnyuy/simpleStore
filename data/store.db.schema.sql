BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Basket" (
	"id"	INTEGER,
	"user_id"	INTEGER,
	"article_id"	INTEGER,
	"session_id"	TEXT,
	"isAvail"	INTEGER DEFAULT 1,
	"date_added"	TEXT
);
CREATE TABLE IF NOT EXISTS "Inventory" (
	"article_id"	INTEGER,
	"qauntity"	INTEGER
);
CREATE TABLE IF NOT EXISTS "Artice_kind" (
	"id"	INTEGER NOT NULL,
	"label"	TEXT NOT NULL,
	"description"	TEXT,
	UNIQUE("label"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Categories" (
	"id"	INTEGER NOT NULL,
	"label"	TEXT NOT NULL,
	"description"	TEXT,
	UNIQUE("label"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Articles" (
	"id"	INTEGER,
	"name"	TEXT,
	"cost"	NUMERIC NOT NULL,
	"model"	TEXT,
	"maker"	TEXT,
	"category"	INTEGER NOT NULL,
	"sub_category"	INTEGER,
	"quantity"	INTEGER NOT NULL DEFAULT 0,
	"images"	TEXT,
	UNIQUE("model","maker"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;
