USE DbMysql07;

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
    PRIMARY KEY (artistID)
);

CREATE TABLE Lyrics (
    songID int,
    lyrics varchar(5000), 
    FOREIGN KEY (songID) REFERENCES Songs(songID)
);

CREATE TABLE ArtistToCategory (
    artistID int,
    categoryID int, 
    FOREIGN KEY (artistID) REFERENCES Artists(artistID),
	FOREIGN KEY (categoryID) REFERENCES Categories(categoryID)
);

CREATE TABLE SongToArtist (
    songID int,
    artistID int, 
    FOREIGN KEY (songID) REFERENCES Songs(songID),
	FOREIGN KEY (artistID) REFERENCES Artists(artistID)
);


CREATE TABLE SongToCategory (
    songID int,
    categoryID int,
    FOREIGN KEY (songID) REFERENCES Songs(songID),
	FOREIGN KEY (categoryID) REFERENCES Categories(categoryID)
);


CREATE TABLE Videos (
    videoID char(11) UNIQUE,
    songID int,
    publishedAt DATE NOT NULL,
    title varchar(100) NOT NULL,
    viewCount BIGINT NOT NULL,
    likeCount int NOT NULL,
    dislikeCount int NOT NULL,
    favoriteCount int,
    commentCount int NOT NULL,
    PRIMARY KEY (videoID),
    FOREIGN KEY (songID) REFERENCES Songs(songID)
);

CREATE TABLE Comments (
    commentID varchar(30) UNIQUE,
    videoID char(11),
    author varchar(50) NOT NULL,
    commentText TEXT(2000) NOT NULL,
    publishedAt DATE NOT NULL,
    viewerRating int,
    likeCount int NOT NULL,
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