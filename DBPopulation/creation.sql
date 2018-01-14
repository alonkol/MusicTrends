CREATE TABLE Categories (
    categoryID int AUTO_INCREMENT,
    categoryName varchar(50), 
    PRIMARY KEY (categoryID)
);

CREATE TABLE Songs (
    songID int AUTO_INCREMENT,
    songName varchar(250),
    PRIMARY KEY (songID)
);

CREATE TABLE Artists (
    artistID int AUTO_INCREMENT,
    artistName varchar(250),
    active tinyint(1) DEFAULT 1,
    PRIMARY KEY (artistID)
);

CREATE TABLE Lyrics (
    songID int,
    lyrics TEXT(5000),
    PRIMARY KEY (songID),
    FOREIGN KEY (songID) REFERENCES Songs(songID)
);

CREATE TABLE Lyrics_MyISAM (
    songID int,
    lyrics TEXT(5000),
    PRIMARY KEY (songID),
    FOREIGN KEY (songID) REFERENCES Songs(songID)
) ENGINE = MyISAM;

ALTER TABLE Lyrics_MyISAM ADD FULLTEXT (lyrics);

CREATE TABLE ArtistToCategory (
    artistID int,
    categoryID int,
    PRIMARY KEY (artistID, categoryID),
    FOREIGN KEY (artistID) REFERENCES Artists(artistID),
	FOREIGN KEY (categoryID) REFERENCES Categories(categoryID)
);

CREATE TABLE SongToArtist (
    songID int,
    artistID int,
    PRIMARY KEY (songID, artistID),
    FOREIGN KEY (songID) REFERENCES Songs(songID),
	FOREIGN KEY (artistID) REFERENCES Artists(artistID)
);


CREATE TABLE SongToCategory (
    songID int,
    categoryID int,
    PRIMARY KEY (songID, categoryID),
    FOREIGN KEY (songID) REFERENCES Songs(songID),
	FOREIGN KEY (categoryID) REFERENCES Categories(categoryID)
);


CREATE TABLE Videos (
    videoID char(11),
    songID int,
    publishedAt DATE NOT NULL,
    title varchar(500) NOT NULL,
    viewCount bigint NOT NULL,
    likeCount int NOT NULL,
    dislikeCount int NOT NULL,
    PRIMARY KEY (videoID),
    FOREIGN KEY (songID) REFERENCES Songs(songID)
);

CREATE TABLE Comments (
    commentID varchar(30),
    videoID char(11),
    author varchar(200) NOT NULL,
    commentText TEXT(2000) NOT NULL,
    publishedAt DATE NOT NULL,
    PRIMARY KEY (commentID),
    FOREIGN KEY (videoID) REFERENCES Videos(videoID)
);

CREATE TABLE CommentWordsPerVideo (
    videoID char(11),
    word varchar(20) NOT NULL, 
    commentWordCount int NOT NULL,
    FOREIGN KEY (videoID) REFERENCES Videos(videoID)
);

CREATE TABLE WordsPerSong (
    songID int,
    word varchar(20) NOT NULL, 
    wordCount int NOT NULL,
    FOREIGN KEY (songID) REFERENCES Songs(songID)
);

CREATE VIEW ArtistsWordCount AS
SELECT Artists.artistName, Artists.artistID, word, sum(wordCount), ArtistToCategory.categoryID
FROM WordsPerSong, SongToArtist, Artists, ArtistToCategory
WHERE WordsPerSong.songID = SongToArtist.songID
AND SongToArtist.artistID = Artists.artistID
AND ArtistToCategory.artistID = Artists.artistID
GROUP BY word, Artists.artistID, Artists.artistName, categoryID;

CREATE UNIQUE INDEX SongIdInVideos ON Videos(songID);

---TODO consider adding these
---CREATE INDEX WordInSongs ON WordsPerSong (word);
---CREATE INDEX WordInComments ON CommentWordsPerVideo (commentWordCount);