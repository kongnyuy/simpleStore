BEGIN TRANSACTION;
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
	"kind"	INTEGER,
	"quantity"	INTEGER NOT NULL DEFAULT 0,
	"images"	TEXT,
	UNIQUE("model","maker"),
	CONSTRAINT "cat_art_FK" FOREIGN KEY("category") REFERENCES "Categories"("id") ON UPDATE CASCADE ON DELETE RESTRICT,
	CONSTRAINT "kind_art_FK" FOREIGN KEY("kind") REFERENCES "Artice_kind"("id") ON UPDATE CASCADE ON DELETE RESTRICT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Inventory" (
	"article_id"	INTEGER,
	"qauntity"	INTEGER,
	UNIQUE("article_id"),
	CONSTRAINT "inv_art_FK" FOREIGN KEY("article_id") REFERENCES "Articles"("id") ON UPDATE CASCADE ON DELETE RESTRICT
);
CREATE TABLE IF NOT EXISTS "Users" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Sessions" (
	"id"	INTEGER NOT NULL,
	"user_id"	INTEGER NOT NULL,
	"start_time"	INTEGER NOT NULL,
	"end_time"	INTEGER NOT NULL,
	UNIQUE("user_id","start_time","end_time"),
	CONSTRAINT "user_session_FK" FOREIGN KEY("user_id") REFERENCES "Users"("id") ON UPDATE CASCADE ON DELETE RESTRICT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Baskets" (
	"id"	INTEGER NOT NULL,
	"user_id"	INTEGER,
	"article_id"	INTEGER,
	"session_id"	INTEGER,
	"isAvail"	INTEGER DEFAULT 1,
	"date_added"	TEXT,
	CONSTRAINT "session_basket_FK" FOREIGN KEY("session_id") REFERENCES "Sessions"("id") ON UPDATE CASCADE ON DELETE RESTRICT,
	CONSTRAINT "art_basket_FK" FOREIGN KEY("article_id") REFERENCES "Articles"("id") ON UPDATE CASCADE ON DELETE RESTRICT,
	CONSTRAINT "user_basket_FK" FOREIGN KEY("user_id") REFERENCES "Users"("id") ON UPDATE CASCADE ON DELETE RESTRICT,
	PRIMARY KEY("user_id","session_id","date_added")
);
COMMIT;
