USE DbMysql07;

CREATE TABLE Categories (
    category_id int AUTO_INCREMENT,
    category_name varchar(50), 
    PRIMARY KEY (category_id)
);

CREATE TABLE Songs (
    song_id int AUTO_INCREMENT,
    song_name varchar(100),
    likes int,
    dislikes int,
    PRIMARY KEY (song_id)
);

CREATE TABLE Artists (
    artist_id int AUTO_INCREMENT,
    artist_name varchar(50), 
    PRIMARY KEY (artist_id)
);

CREATE TABLE Lyrics (
    song_id int,
    lyrics varchar(5000), 
    FOREIGN KEY (song_id) REFERENCES Songs(song_id)
);

CREATE TABLE SongToCategory (
    song_id int,
    category_id int, 
    FOREIGN KEY (song_id) REFERENCES Songs(song_id),
	FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE SongToArtist (
    song_id int,
    artist_id int, 
    FOREIGN KEY (song_id) REFERENCES Songs(song_id),
	FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);

CREATE TABLE Comments (
    song_id int,
    comment_text varchar(2000) NOT NULL, 
    author varchar(50) NOT NULL,
    likes int,
    dislikes int,
    FOREIGN KEY (song_id) REFERENCES Songs(song_id)
);

CREATE TABLE CommentWordsPerSong (
    song_id int,
    word varchar(20) NOT NULL, 
    comment_word_count int NOT NULL,
    FOREIGN KEY (song_id) REFERENCES Songs(song_id)
);

CREATE TABLE WordsPerSong (
    song_id int,
    word varchar(20) NOT NULL, 
    word_count int,
    FOREIGN KEY (song_id) REFERENCES Songs(song_id)
);