import sqlite3

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('../Database.db') as db:
    c = db.cursor()

# Create Tables
# -- User Table for Clerks
# ---- UserID, Name, Password
c.execute('CREATE TABLE IF NOT EXISTS user (UserID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Password TEXT NOT NULL);')

# -- Person Table for General Public
# ---- NIC, Name, Email, Password, Phone, Address, ImageID
c.execute('CREATE TABLE IF NOT EXISTS person (NIC TEXT NOT NULL PRIMARY KEY, Name TEXT NOT NULL, Email TEXT NOT NULL, Password TEXT NOT NULL, Phone TEXT NOT NULL, Address TEXT NOT NULL, ImageID TEXT NOT NULL);')


db.commit()
db.close()
