import sqlite3
import pandas as pd

conn = sqlite3.connect('track.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')

cur.execute('CREATE TABLE Artist (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE)')
cur.execute('CREATE TABLE Genre (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name TEXT UNIQUE)')
cur.execute('CREATE TABLE Album (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,artist_id  INTEGER,title   TEXT UNIQUE)')
cur.execute('CREATE TABLE Track (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,title TEXT  UNIQUE,album_id  INTEGER,genre_id  INTEGER,len INTEGER, rating INTEGER, count INTEGER);')

fname = open('tracks.csv')

for line in fname:
    line = line.rstrip()
    pieces = line.split(',')

    track = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    rating = pieces[3]
    count = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?,? )''', ( album,artist_id, ) )
    cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Track (title,album_id, genre_id,len,rating,count) 
        VALUES ( ?,?,?,?,?,? )''', ( track ,album_id , genre_id ,length ,rating,count, ) )

conn.commit()

sqlquery = 'SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.ID and Track.album_id = Album.id AND Album.artist_id = Artist.id ORDER BY Artist.name LIMIT 3'

for line in cur.execute(sqlquery):
    print(str(line[0]), line[1])

cur.close()
conn.close()
