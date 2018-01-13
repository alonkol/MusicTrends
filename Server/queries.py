
CATEGORIES = "SELECT categoryID as id, categoryName as name FROM Categories;"

TOP_SONG_LIKES = "SELECT songName, likeCount " \
                    "FROM songs, videos " \
                    "WHERE songs.songID = videos.songID " \
                    "ORDER BY likeCount DESC " \
                    "LIMIT %s;"

TOP_SONG_LIKES_PER_CATEGORY = "SELECT songName, likeCount " \
            "FROM songs, videos, categories, SongToCategory " \
            "WHERE songs.songID = videos.songID " \
            "AND SongToCategory.songID = songs.songID " \
            "AND SongToCategory.categoryID = categories.categoryID " \
            "AND categories.categoryName = %s " \
            "ORDER BY likeCount DESC " \
            "LIMIT %s;"

TOP_SONG_DISLIKES = "SELECT songName, dislikeCount " \
            "FROM songs, videos " \
            "WHERE songs.songID = videos.songID " \
            "ORDER BY dislikeCount DESC " \
            "LIMIT %s;"

TOP_SONG_DISLIKES_PER_CATEGORY = "SELECT songName, dislikeCount " \
            "FROM songs, videos, categories, SongToCategory " \
            "WHERE songs.songID = videos.songID " \
            "AND SongToCategory.songID = songs.songID " \
            "AND SongToCategory.categoryID = categories.categoryID " \
            "AND categories.categoryName = %s " \
            "ORDER BY dislikeCount DESC " \
            "LIMIT %s;"

TOP_SONG_VIEWS = "SELECT songName, viewCount " \
            "FROM songs, videos " \
            "WHERE songs.songID = videos.songID " \
            "ORDER BY viewCount DESC " \
            "LIMIT %s;"

TOP_SONG_VIEWS_PER_CATEGORY = "SELECT songName, viewCount " \
            "FROM songs, videos, categories, SongToCategory " \
            "WHERE songs.songID = videos.songID " \
            "AND SongToCategory.songID = songs.songID " \
            "AND SongToCategory.categoryID = categories.categoryID " \
            "AND categories.categoryName = %s " \
            "ORDER BY viewCount DESC " \
            "LIMIT %s;"

BOTTOM_SONG_VIEWS = "SELECT songName, viewCount " \
            "FROM songs, videos " \
            "WHERE songs.songID = videos.songID " \
            "ORDER BY viewCount ASC " \
            "LIMIT %s;"

BOTTOM_SONG_VIEWS_PER_CATEGORY = "SELECT songName, viewCount " \
            "FROM songs, videos, categories, SongToCategory " \
            "WHERE songs.songID = videos.songID " \
            "AND SongToCategory.songID = songs.songID " \
            "AND SongToCategory.categoryID = categories.categoryID " \
            "AND categories.categoryName = %s " \
            "ORDER BY viewCount ASC " \
            "LIMIT %s;"

TOP_WORDS = "SELECT word, SUM(wordCount) AS count " \
                "FROM WordsPerSong " \
                "GROUP BY word " \
                "ORDER BY count DESC " \
                "LIMIT %s;"

TOP_WORDS_PER_CATEGORY = "SELECT word, SUM(wordCount) AS count " \
            "FROM WordsPerSong, categories, SongToCategory " \
            "WHERE WordsPerSong.songID = SongToCategory.songID " \
            "AND SongToCategory.categoryID = categories.categoryID " \
            "AND categories.categoryName = %s " \
            "GROUP BY word " \
            "ORDER BY count DESC " \
            "LIMIT %s;"

BOTTOM_WORDS = "SELECT word, SUM(wordCount) AS count " \
            "FROM WordsPerSong " \
            "GROUP BY word " \
            "ORDER BY count ASC " \
            "LIMIT %s;"

BOTTOM_WORDS_PER_CATEGORY = "SELECT word, SUM(wordCount) AS count " \
            "FROM WordsPerSong, categories, SongToCategory " \
            "WHERE WordsPerSong.songID = SongToCategory.songID " \
            "AND categories.categoryID = SongToCategory.categoryID " \
            "AND categories.categoryName = %s " \
            "GROUP BY word " \
            "ORDER BY count ASC " \
            "LIMIT %s;"

TOP_SOPHISTICATED = "SELECT songName, score " \
            "FROM " \
            "(" \
                "SELECT songID, (POW(COUNT(WordsPerSong.word),2)/SUM(wordCount))*AVG(uniqueness) AS score " \
                "FROM " \
                "(" \
                    "SELECT word, 1/SUM(wordCount) AS uniqueness " \
                    "FROM WordsPerSong " \
                    "GROUP BY word " \
                ") AS wordUniqueness, WordsPerSong  " \
                "WHERE wordUniqueness.word = WordsPerSong.word " \
                "GROUP BY WordsPerSong.songID " \
            ") AS a, songs " \
            "WHERE songs.songID = a.songID " \
            "ORDER BY score DESC " \
            "LIMIT %s;"

TOP_SOPHISTICATED_PER_CATEGORY = "SELECT songName, score " \
            "FROM " \
            "(" \
                "SELECT WordsPerSong.songID, (POW(COUNT(WordsPerSong.word),2)/SUM(wordCount))*AVG(uniqueness) AS score " \
                "FROM " \
                "(" \
                    "SELECT word, 1/SUM(wordCount) AS uniqueness " \
                    "FROM WordsPerSong " \
                    "GROUP BY word " \
                ") AS wordUniqueness, WordsPerSong, categories, SongToCategory " \
                "WHERE wordUniqueness.word = WordsPerSong.word " \
                "AND categories.categoryName = %s " \
                "AND SongToCategory.categoryID = categories.categoryID " \
                "AND SongToCategory.songID = WordsPerSong.songID " \
                "GROUP BY WordsPerSong.songID " \
            ") AS a, songs " \
            "WHERE songs.songID = a.songID " \
            "ORDER BY score DESC " \
            "LIMIT %s;"

BOTTOM_SOPHISTICATED = "SELECT songName, score " \
            "FROM " \
            "(" \
                "SELECT songID, (POW(COUNT(WordsPerSong.word),2)/SUM(wordCount))*AVG(uniqueness) AS score " \
                "FROM " \
                "(" \
                    "SELECT word, 1/SUM(wordCount) AS uniqueness " \
                    "FROM WordsPerSong " \
                    "GROUP BY word " \
                ") AS wordUniqueness, WordsPerSong  " \
                "WHERE wordUniqueness.word = WordsPerSong.word " \
                "GROUP BY WordsPerSong.songID" \
            ") AS a, songs " \
            "WHERE songs.songID = a.songID " \
            "ORDER BY score ASC " \
            "LIMIT %s;"

BOTTOM_SOPHISTICATED_PER_CATEGORY = "SELECT songName, score " \
            "FROM " \
            "(" \
                "SELECT songID, (POW(COUNT(WordsPerSong.word),2)/SUM(wordCount))*AVG(uniqueness) AS score " \
                "FROM " \
                "(" \
                    "SELECT word, 1/SUM(wordCount) AS uniqueness " \
                    "FROM WordsPerSong" \
                    "GROUP BY word " \
                ") AS wordUniqueness, WordsPerSong, categories, SongToCategory " \
                "WHERE wordUniqueness.word = WordsPerSong.word " \
                "AND categories.categoryName = %s " \
                "AND SongToCategory.categoryID = categories.categoryID " \
                "AND SongToCategory.songID = WordsPerSong.songID " \
                "GROUP BY WordsPerSong.songID " \
            ") AS a, songs " \
            "WHERE songs.songID = a.songID " \
            "ORDER BY score ASC " \
            "LIMIT %s;"

ARTISTS = "SELECT artistID, artistName FROM Artists WHERE active=1;"

SONGS_FOR_ARTISTS = "SELECT Songs.songID, Songs.songName FROM SongToArtist, Songs " \
                    "WHERE artistID = %s " \
                    "and Songs.songID = SongToArtist.songID;"

BLACKLIST_ARTIST = "UPDATE Artists SET active=0 WHERE artistID=%s;"

LYRICS = "SELECT lyrics FROM Lyrics WHERE songID = %s;"

DELETE_FROM_WORDS_PER_SONG = "DELETE FROM WordsPerSong WHERE songID = %s;"

FIND_ARTIST_ID = "SELECT artistID FROM Artists WHERE artistName = %s;"

FIND_LYRICS = "SELECT lyrics FROM Lyrics WHERE songID = %s;"

UPDATE_LYRICS = "UPDATE Lyrics SET lyrics = %s WHERE songID = %s;"

FIND_SONG_ID = "SELECT Songs.songID " \
                "FROM Songs, SongToArtist, Artists " \
                "WHERE songName = %s AND " \
                "ArtistName = %s AND " \
                "Artists.artistID = SongToArtist.artistID AND " \
                "Songs.songID = SongToArtist.songID;"


ARTISTS_FOR_CATEGORIES = "SELECT Artists.artistID, Artists.artistName FROM Artists, ArtistToCategory " \
                         "Where Artists.artistID = ArtistToCategory.artistID AND " \
                         "ArtistToCategory.categoryID = %s"


FIND_VIDEO_ID_BY_SONG_ID = "SELECT videoID From Videos WHERE songID = %s"

UPDATE_VIDEOS_DATA = "UPDATE Videos SET viewCount = %s, likeCount = %s, dislikeCount = %s, favoriteCount = %s, " \
                     "commentCount = %s WHERE videoID = %s"
