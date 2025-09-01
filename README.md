# Music-Track-Database-with-SQLite
This project builds a small music track database using SQLite. It processes data from a tracks.csv file, organizes it into relational tables (Artists, Albums, Genres, Tracks), and allows you to run queries to explore the relationships between them.

Features
1. Creates 4 relational tables:
     Artist (artist details) 
     Album (albums linked to artists) 
     Genre (track genres) 
     Track (songs with metadata) 

2. Reads track information from tracks.csv.
3. Avoids duplicate entries using INSERT OR IGNORE.
4. Joins across multiple tables to show meaningful relationships.
5. Outputs sample results such as track title, artist, album, and genre.

🛠️ Requirements
1. Python 3.x
2. SQLite (built-in with Python)
3. pandas (optional, imported but not required in this script)

📂 Usage
1. Clone the repository: 
git clone https://github.com/your-username/music-track-database.git 
cd music-track-database

2. Place your dataset file as tracks.csv in the same directory.

3. Example row format: 
TrackTitle, ArtistName, AlbumTitle , Rating, Count , Length, Genre

4. Run the script:
python tracks.py

5. Example output (first 3 results ordered by Artist name):

SongTitle1  ArtistName1 
SongTitle2  ArtistName2 
SongTitle3  ArtistName3 

Database Schema 
Artist(id, name) 
Genre(id, name) 
Album(id, artist_id, title) 
Track(id, title, album_id, genre_id, len, rating, count) 

Learning Context
1. This project is based on exercises from the Python for Everybody (PY4E) course by Dr. Charles Severance. It’s designed to practice:
2. Relational databases
3. Joins and foreign keys
4. Data normalization
5. Handling CSV data with Python + SQLite
