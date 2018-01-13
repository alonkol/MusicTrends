
CATEGORIES = "SELECT categoryID as id, categoryName as name FROM Categories;"

TOP_SONG_LIKES = "SELECT songName, likeCount " \
                    "FROM songs, videos " \
                    "WHERE songs.songID = videos.songID " \
                    "ORDER BY likeCount DESC " \
                    "LIMIT %s;"

TOP_SONG_LIKES_PER_CATEGORY = "SELECT songName, likeCount " \
            "FROM songs, videos, SongToCategory " \
            "WHERE songs.songID = videos.songID " \
            "AND SongToCategory.songID = songs.songID " \
            "AND SongToCategory.categoryID = %s " \
            "ORDER BY likeCount DESC " \
            "LIMIT %s;"

TOP_SONG_DISLIKES = "SELECT songName, dislikeCount " \
            "FROM songs, videos " \
            "WHERE songs.songID = videos.songID " \
            "ORDER BY dislikeCount DESC " \
            "LIMIT %s;"

TOP_SONG_DISLIKES_PER_CATEGORY = "SELECT songName, dislikeCount " \
            "FROM songs, videos, SongToCategory " \
            "WHERE songs.songID = videos.songID " \
            "AND SongToCategory.songID = songs.songID " \
            "AND SongToCategory.categoryID = %s " \
            "ORDER BY dislikeCount DESC " \
            "LIMIT %s;"

TOP_SONG_VIEWS = "SELECT songName, viewCount " \
            "FROM songs, videos " \
            "WHERE songs.songID = videos.songID " \
            "ORDER BY viewCount DESC " \
            "LIMIT %s;"

TOP_SONG_VIEWS_PER_CATEGORY = "SELECT songName, viewCount " \
            "FROM songs, videos, SongToCategory " \
            "WHERE songs.songID = videos.songID " \
            "AND SongToCategory.songID = songs.songID " \
            "AND SongToCategory.categoryID = %s " \
            "ORDER BY viewCount DESC " \
            "LIMIT %s;"

BOTTOM_SONG_VIEWS = "SELECT songName, viewCount " \
            "FROM songs, videos " \
            "WHERE songs.songID = videos.songID " \
            "ORDER BY viewCount ASC " \
            "LIMIT %s;"

BOTTOM_SONG_VIEWS_PER_CATEGORY = "SELECT songName, viewCount " \
            "FROM songs, videos, SongToCategory " \
            "WHERE songs.songID = videos.songID " \
            "AND SongToCategory.songID = songs.songID " \
            "AND SongToCategory.categoryID = %s " \
            "ORDER BY viewCount ASC " \
            "LIMIT %s;"

TOP_WORDS = "SELECT word, SUM(wordCount) AS count " \
                "FROM WordsPerSong " \
                "GROUP BY word " \
                "ORDER BY count DESC " \
                "LIMIT %s;"

TOP_WORDS_PER_CATEGORY = "SELECT word, SUM(wordCount) AS count " \
            "FROM WordsPerSong, SongToCategory " \
            "WHERE WordsPerSong.songID = SongToCategory.songID " \
            "AND SongToCategory.categoryID = %s " \
            "GROUP BY word " \
            "ORDER BY count DESC " \
            "LIMIT %s;"

BOTTOM_WORDS = "SELECT word, SUM(wordCount) AS count " \
            "FROM WordsPerSong " \
            "GROUP BY word " \
            "ORDER BY count ASC " \
            "LIMIT %s;"

BOTTOM_WORDS_PER_CATEGORY = "SELECT word, SUM(wordCount) AS count " \
            "FROM WordsPerSong, SongToCategory " \
            "WHERE WordsPerSong.songID = SongToCategory.songID " \
            "AND SongToCategory.categoryID = %s " \
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
                ") AS wordUniqueness, WordsPerSong, SongToCategory " \
                "WHERE wordUniqueness.word = WordsPerSong.word " \
                "AND SongToCategory.categoryID = %s " \
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
                ") AS wordUniqueness, WordsPerSong, SongToCategory " \
                "WHERE wordUniqueness.word = WordsPerSong.word " \
                "AND SongToCategory.categoryID = %s " \
                "AND SongToCategory.songID = WordsPerSong.songID " \
                "GROUP BY WordsPerSong.songID " \
            ") AS a, songs " \
            "WHERE songs.songID = a.songID " \
            "ORDER BY score ASC " \
            "LIMIT %s;"


TOP_SOPHISTICATED_SONG_DISCUSSIONS = ""

TOP_SOPHISTICATED_SONG_DISCUSSIONS_PER_CATEGORY = ""

TOP_GROUPIES = ""

TOP_GROUPIES_PER_CATEGORY = ""

TOP_HEAD_EATERS = "SELECT artists.artistName, AVG(wordCount) AS avgWordCount " \
                "FROM artists, songtoartist, " \
                "(" \
                    "SELECT songID, SUM(wordCount) AS wordCount " \
                    "FROM wordspersong " \
                    "GROUP BY songID " \
                ") AS totalWordsPerSong " \
                "WHERE songtoartist.artistID = artists.artistID " \
                "AND songtoartist.songID = totalWordsPerSong.songID " \
                "GROUP BY songtoartist.artistID, artists.artistName " \
                "ORDER BY avgWordCount DESC " \
                "LIMIT %s;"

TOP_HEAD_EATERS_PER_CATEGORY = "SELECT artists.artistName, AVG(wordCount) AS avgWordCount " \
                "FROM artists, songtoartist, " \
                "(" \
                    "SELECT wordspersong.songID, SUM(wordCount) AS wordCount " \
                    "FROM wordspersong, songtocategory " \
                    "WHERE wordspersong.songID = songtocategory.songID " \
                    "AND songtocategory.categoryID = %s " \
                    "GROUP BY wordspersong.songID " \
                ") AS totalWordsPerSong " \
                "WHERE songtoartist.artistID = artists.artistID " \
                "AND songtoartist.songID = totalWordsPerSong.songID " \
                "GROUP BY songtoartist.artistID, artists.artistName " \
                "ORDER BY avgWordCount DESC " \
                "LIMIT %s;"


TOP_ARTIST_TEXT_COUPLES = ""

TOP_ARTIST_TEXT_COUPLES_PER_CATEGORY = ""

TOP_DAYS_COMMENTS = "SELECT DAYNAME(comments.publishedAt) AS day " \
                    "FROM comments, videos " \
                    "WHERE comments.videoID = videos.videoID " \
                    "GROUP BY day " \
                    "ORDER BY COUNT(*) DESC " \
                    "LIMIT %s;"


TOP_DAYS_COMMENTS_PER_CATEGORY = "SELECT DAYNAME(comments.publishedAt) AS day " \
                                 "FROM comments, videos, songToCategory " \
                                 "WHERE comments.videoID = videos.videoID " \
                                 "AND videos.songID = songToCategory.songID " \
                                 "AND songToCategory.categoryID = %s " \
                                 "GROUP BY day " \
                                 "ORDER BY COUNT(*) DESC " \
                                 "LIMIT %s;"

TOP_CONTROVERSIAL_ARTISTS = "SELECT artists.artistName, AVG(scores.score) AS score " \
                             "FROM artists, songtoartist, " \
                             "(" \
                                "SELECT songID, dislikeCount/likeCount AS score " \
                                "FROM videos " \
                             ") AS scores " \
                             "WHERE songtoartist.artistID = artists.artistID " \
                             "AND songtoartist.songID = scores.songID " \
                             "GROUP BY artists.artistID, artists.artistName " \
                             "ORDER BY score DESC " \
                             "LIMIT %s;"

TOP_CONTROVERSIAL_ARTISTS_PER_CATEGORY = "SELECT artists.artistName, AVG(scores.score) AS score " \
                                         "FROM artists, songtoartist, " \
                                         "(" \
                                            "SELECT songID, dislikeCount/likeCount AS score " \
                                            "FROM videos, songtocategory " \
                                            "WHERE songtocategory.categoryID = %s " \
                                            "AND songtocategory.songID = videos.songID " \
                                         ") AS scores " \
                                         "WHERE songtoartist.artistID = artists.artistID " \
                                         "AND songtoartist.songID = scores.songID " \
                                         "GROUP BY artists.artistID, artists.artistName " \
                                         "ORDER BY score DESC " \
                                         "LIMIT %s;"

# ADMIN PAGE QUERIES

ARTISTS = "SELECT artistID, artistName FROM Artists WHERE active=1;"

SONGS_FOR_ARTISTS = "SELECT Songs.songID, Songs.songName FROM SongToArtist, Songs " \
                    "WHERE artistID = %s " \
                    "and Songs.songID = SongToArtist.songID;"

BLACKLIST_ARTIST = "UPDATE Artists SET active=0 WHERE artistID=%s;"

LYRICS = "SELECT lyrics FROM Lyrics WHERE songID = %s;"

DELETE_FROM_WORDS_PER_SONG = "DELETE FROM WordsPerSong WHERE songID = %s;"

FIND_ARTIST_NAME = "SELECT artistName FROM Artists WHERE artistID = %s;"

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
