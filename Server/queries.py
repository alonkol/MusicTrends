
CATEGORIES = "SELECT categoryID as id, categoryName as name FROM Categories;"

TOP_SONG_LIKES = "SELECT songName, likeCount " \
                    "FROM Songs, Videos " \
                    "WHERE Songs.songID = Videos.songID " \
                    "ORDER BY likeCount DESC " \
                    "LIMIT %s;"

TOP_SONG_LIKES_PER_CATEGORY = "SELECT songName, likeCount " \
            "FROM Songs, Videos, SongToCategory " \
            "WHERE Songs.songID = Videos.songID " \
            "AND SongToCategory.songID = Songs.songID " \
            "AND SongToCategory.categoryID = %s " \
            "ORDER BY likeCount DESC " \
            "LIMIT %s;"

TOP_SONG_DISLIKES = "SELECT songName, dislikeCount " \
            "FROM Songs, Videos " \
            "WHERE Songs.songID = Videos.songID " \
            "ORDER BY dislikeCount DESC " \
            "LIMIT %s;"

TOP_SONG_DISLIKES_PER_CATEGORY = "SELECT songName, dislikeCount " \
            "FROM Songs, Videos, SongToCategory " \
            "WHERE Songs.songID = Videos.songID " \
            "AND SongToCategory.songID = Songs.songID " \
            "AND SongToCategory.categoryID = %s " \
            "ORDER BY dislikeCount DESC " \
            "LIMIT %s;"

TOP_SONG_VIEWS = "SELECT songName, viewCount " \
            "FROM Songs, Videos " \
            "WHERE Songs.songID = Videos.songID " \
            "ORDER BY viewCount DESC " \
            "LIMIT %s;"

TOP_SONG_VIEWS_PER_CATEGORY = "SELECT songName, viewCount " \
            "FROM Songs, Videos, SongToCategory " \
            "WHERE Songs.songID = Videos.songID " \
            "AND SongToCategory.songID = Songs.songID " \
            "AND SongToCategory.categoryID = %s " \
            "ORDER BY viewCount DESC " \
            "LIMIT %s;"

BOTTOM_SONG_VIEWS = "SELECT songName, viewCount " \
            "FROM Songs, Videos " \
            "WHERE Songs.songID = Videos.songID " \
            "ORDER BY viewCount ASC " \
            "LIMIT %s;"

BOTTOM_SONG_VIEWS_PER_CATEGORY = "SELECT songName, viewCount " \
            "FROM Songs, Videos, SongToCategory " \
            "WHERE Songs.songID = Videos.songID " \
            "AND SongToCategory.songID = Songs.songID " \
            "AND SongToCategory.categoryID = %s " \
            "ORDER BY viewCount ASC " \
            "LIMIT %s;"

TOP_WORDS = "SELECT CONCAT(UCASE(LEFT(word, 1)), SUBSTRING(word, 2)), " \
                "SUM(wordCount) AS count " \
                "FROM WordsPerSong " \
                "GROUP BY word " \
                "ORDER BY count DESC " \
                "LIMIT %s;"

TOP_WORDS_PER_CATEGORY = "SELECT CONCAT(UCASE(LEFT(word, 1)), SUBSTRING(word, 2)), " \
            "SUM(wordCount) AS count " \
            "FROM WordsPerSong, SongToCategory " \
            "WHERE WordsPerSong.songID = SongToCategory.songID " \
            "AND SongToCategory.categoryID = %s " \
            "GROUP BY word " \
            "ORDER BY count DESC " \
            "LIMIT %s;"

BOTTOM_WORDS = "SELECT CONCAT(UCASE(LEFT(word, 1)), SUBSTRING(word, 2)), " \
            "SUM(wordCount) AS count " \
            "FROM WordsPerSong " \
            "GROUP BY word " \
            "ORDER BY count ASC " \
            "LIMIT %s;"

BOTTOM_WORDS_PER_CATEGORY = "SELECT CONCAT(UCASE(LEFT(word, 1)), SUBSTRING(word, 2)), " \
            "SUM(wordCount) AS count " \
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
                    "GROUP BY word" \
                ") AS wordUniqueness, WordsPerSong " \
                "WHERE wordUniqueness.word = WordsPerSong.word " \
                "GROUP BY WordsPerSong.songID " \
            ") AS A, Songs " \
            "WHERE Songs.songID = A.songID " \
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
            ") AS a, Songs " \
            "WHERE Songs.songID = a.songID " \
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
            ") AS a, Songs " \
            "WHERE Songs.songID = a.songID " \
            "ORDER BY score ASC " \
            "LIMIT %s;"

BOTTOM_SOPHISTICATED_PER_CATEGORY = "SELECT songName, score " \
            "FROM " \
            "(" \
                "SELECT SongToCategory.songID, (POW(COUNT(WordsPerSong.word),2)/SUM(wordCount))*AVG(uniqueness) AS score " \
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
            ") AS a, Songs " \
            "WHERE Songs.songID = a.songID " \
            "ORDER BY score ASC " \
            "LIMIT %s;"

TOP_SOPHISTICATED_SONG_DISCUSSIONS = "SELECT songName, score " \
            "FROM " \
            "(" \
                "SELECT videoID, (POW(COUNT(CommentWordsPerVideo.word),2)/SUM(commentWordCount))*AVG(uniqueness) AS score " \
                "FROM " \
                "(" \
				    "SELECT word, 1/SUM(commentWordCount) AS uniqueness " \
                    "FROM CommentWordsPerVideo " \
                    "GROUP BY word " \
                ") AS wordUniqueness, CommentWordsPerVideo " \
                "WHERE wordUniqueness.word = CommentWordsPerVideo.word " \
                "GROUP BY CommentWordsPerVideo.videoID " \
            ") AS a, Songs, Videos " \
            "WHERE Songs.songID = Videos.songID " \
            "AND Videos.videoID = a.videoID " \
            "ORDER BY score DESC " \
            "LIMIT %s;"

TOP_SOPHISTICATED_SONG_DISCUSSIONS_PER_CATEGORY = "SELECT songName, score " \
            "FROM " \
            "(" \
                "SELECT Videos.videoID, (POW(COUNT(CommentWordsPerVideo.word),2)/SUM(commentWordCount))*AVG(uniqueness) AS score " \
                "FROM " \
                "(" \
				    "SELECT word, 1/SUM(commentWordCount) AS uniqueness " \
                    "FROM CommentWordsPerVideo " \
                    "GROUP BY word " \
                ") AS wordUniqueness, CommentWordsPerVideo, SongToCategory, Videos " \
                "WHERE wordUniqueness.word = CommentWordsPerVideo.word " \
                 "AND SongToCategory.categoryID = %s " \
                 "AND SongToCategory.songID = Videos.songID " \
                 "AND Videos.videoID = CommentWordsPerVideo.videoID " \
                 "GROUP BY CommentWordsPerVideo.videoID " \
            ") AS a, Songs, Videos " \
            "WHERE Songs.songID = Videos.songID " \
            "AND Videos.videoID = a.videoID " \
            "ORDER BY score DESC " \
            "LIMIT %s;"

TOP_GROUPIES = "SELECT CONCAT(author, ' (', artistName, ')' ), COUNT(*) AS count  " \
                "FROM Artists, " \
                "(" \
                    "SELECT author, SongToArtist.artistID, Videos.videoID " \
                    "FROM Comments, SongToArtist, Videos " \
                    "WHERE Comments.videoID = Videos.videoID " \
                    "AND Videos.songID = SongToArtist.songID " \
                    "GROUP BY SongToArtist.artistID, Videos.videoID, author " \
                ") AS authorComments " \
                "WHERE Artists.artistID = authorComments.artistID " \
                "GROUP BY author, Artists.artistID " \
                "ORDER BY count DESC " \
                "LIMIT %s;" \

TOP_GROUPIES_PER_CATEGORY = "SELECT CONCAT(author, ' (', artistName, ')' ), COUNT(*) AS count " \
                "FROM Artists, " \
                "(" \
                    "SELECT author, SongToArtist.artistID, Videos.videoID " \
                    "FROM Comments, SongToArtist, Videos, SongToCategory " \
                    "WHERE Comments.videoID = Videos.videoID " \
                    "AND Videos.songID = SongToArtist.songID " \
                    "AND SongToCategory.songID = Videos.songID " \
                    "AND SongToCategory.categoryID = %s " \
                    "GROUP BY SongToArtist.artistID, Videos.videoID, author " \
                ") AS authorComments " \
                "WHERE Artists.artistID = authorComments.artistID " \
                "GROUP BY author, Artists.artistID " \
                "ORDER BY count DESC " \
                "LIMIT %s;" \

TOP_HEAD_EATERS = "SELECT Artists.artistName, AVG(wordCount) AS avgWordCount " \
                "FROM Artists, SongToArtist, " \
                "(" \
                    "SELECT songID, SUM(wordCount) AS wordCount " \
                    "FROM WordsPerSong " \
                    "GROUP BY songID " \
                ") AS totalWordsPerSong " \
                "WHERE SongToArtist.artistID = Artists.artistID " \
                "AND SongToArtist.songID = totalWordsPerSong.songID " \
                "GROUP BY SongToArtist.artistID, Artists.artistName " \
                "ORDER BY avgWordCount DESC " \
                "LIMIT %s;"

TOP_HEAD_EATERS_PER_CATEGORY = "SELECT Artists.artistName, AVG(wordCount) AS avgWordCount " \
                "FROM Artists, SongToArtist, " \
                "(" \
                    "SELECT WordsPerSong.songID, SUM(wordCount) AS wordCount " \
                    "FROM WordsPerSong, SongToCategory " \
                    "WHERE WordsPerSong.songID = SongToCategory.songID " \
                    "AND SongToCategory.categoryID = %s " \
                    "GROUP BY WordsPerSong.songID " \
                ") AS totalWordsPerSong " \
                "WHERE SongToArtist.artistID = Artists.artistID " \
                "AND SongToArtist.songID = totalWordsPerSong.songID " \
                "GROUP BY SongToArtist.artistID, Artists.artistName " \
                "ORDER BY avgWordCount DESC " \
                "LIMIT %s;"


TOP_VIRAL_SONGS = "SELECT songName From Songs," \
                  "(SELECT songID, Videos.videoID, commentCount * avg_like_per_comment as rating From Videos, " \
                  "(SELECT videoID, AVG(likeCount) as avg_like_per_comment FROM Comments GROUP BY videoID) As A " \
                  "WHERE A.videoID = Videos.videoID " \
                  "ORDER BY rating) As likesInComments " \
                  "WHERE Songs.songID = likesInComments.songID " \
                  "Limit %s;"

TOP_VIRAL_SONGS_PER_CATEGORY = "SELECT songName From Songs, SongToCategory," \
                                "(SELECT songID, Videos.videoID, commentCount * avg_like_per_comment as rating From Videos, " \
                                "(SELECT videoID, AVG(likeCount) as avg_like_per_comment FROM Comments GROUP BY videoID) As A " \
                                "WHERE A.videoID = Videos.videoID " \
                                "ORDER BY rating) As likesInComments " \
                                "WHERE Songs.songID = likesInComments.songID AND Songs.songID = SongToCategory.songID " \
                                "AND SongToCategory.categoryID = %s Limit %s;"

TOP_DAYS_COMMENTS = "SELECT DAYNAME(Comments.publishedAt) AS day, COUNT(*) AS count " \
                    "FROM Comments, Videos " \
                    "WHERE Comments.videoID = Videos.videoID " \
                    "GROUP BY day " \
                    "ORDER BY count DESC " \
                    "LIMIT %s;"


TOP_DAYS_COMMENTS_PER_CATEGORY = "SELECT DAYNAME(Comments.publishedAt) AS day, COUNT(*) AS count " \
                                 "FROM Comments, Videos, SongToCategory " \
                                 "WHERE Comments.videoID = Videos.videoID " \
                                 "AND Videos.songID = SongToCategory.songID " \
                                 "AND SongToCategory.categoryID = %s " \
                                 "GROUP BY day " \
                                 "ORDER BY count DESC " \
                                 "LIMIT %s;"

TOP_CONTROVERSIAL_ARTISTS = "SELECT Artists.artistName, AVG(scores.score) AS score " \
                             "FROM Artists, SongToArtist, " \
                             "(" \
                                "SELECT songID, dislikeCount/likeCount AS score " \
                                "FROM Videos " \
                             ") AS scores " \
                             "WHERE SongToArtist.artistID = Artists.artistID " \
                             "AND SongToArtist.songID = scores.songID " \
                             "GROUP BY Artists.artistID, Artists.artistName " \
                             "ORDER BY score DESC " \
                             "LIMIT %s;"

TOP_CONTROVERSIAL_ARTISTS_PER_CATEGORY = "SELECT Artists.artistName, AVG(scores.score) AS score " \
                                         "FROM Artists, SongToArtist, " \
                                         "(" \
                                            "SELECT SongToCategory.songID, dislikeCount/likeCount AS score " \
                                            "FROM Videos, SongToCategory " \
                                            "WHERE SongToCategory.categoryID = %s " \
                                            "AND SongToCategory.songID = Videos.songID " \
                                         ") AS scores " \
                                         "WHERE SongToArtist.artistID = Artists.artistID " \
                                         "AND SongToArtist.songID = scores.songID " \
                                         "GROUP BY Artists.artistID, Artists.artistName " \
                                         "ORDER BY score DESC " \
                                         "LIMIT %s;"

# ADMIN PAGE QUERIES

ARTISTS = "SELECT artistID, artistName FROM Artists WHERE active=1;"

SONGS_FOR_ARTISTS = "SELECT Songs.songID, Songs.songName FROM SongToArtist, Songs " \
                    "WHERE artistID = %s " \
                    "and Songs.songID = SongToArtist.songID;"

BLACKLIST_ARTIST = "UPDATE Artists SET active=0 WHERE artistID=%s;"

FIND_ARTIST_NAME = "SELECT artistName FROM Artists WHERE artistID = %s;"

FIND_LYRICS = "SELECT lyrics FROM Lyrics WHERE songID = %s;"

UPDATE_LYRICS = "UPDATE Lyrics SET lyrics = %s WHERE songID = %s;"

UPDATE_LYRICS_MY_ISAM = "UPDATE Lyrics_MyISAM SET lyrics = %s WHERE songID = %s;"


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

UPDATE_VIDEOS_DATA = "UPDATE Videos SET viewCount = %s, likeCount = %s, dislikeCount = %s, commentCount = %s, " \
                     "WHERE videoID = %s"

FIND_FIVE_MATCHING_SONG_NAMES = "SELECT songName " \
                                "FROM " \
                                "Songs, (SELECT songID, MATCH (lyrics) AGAINST (%s IN BOOLEAN MODE) " \
                                "as score FROM Lyrics_MyISAM ORDER BY score DESC LIMIT 5) as BestMatches " \
                                "WHERE BestMatches.songID = Songs.songID;"

VIDEOS_FOR_SONGS = "SELECT videoID FROM Videos WHERE songID IN (%s)"


REMOVE_VIDEO_FROM_COMMENT_WORDS = "DELETE FROM CommentWordsPerVideo WHERE videoID = %s; "
REMOVE_VIDEO_FROM_COMMENTS = "DELETE FROM Comments WHERE videoID = %s; "
REMOVE_VIDEO_FROM_VIDEOS = "DELETE FROM Videos WHERE videoID = %s "

REMOVE_SONG_FROM_SONGS = "DELETE FROM Songs WHERE songID = %s "
REMOVE_SONG_FROM_SONGS_TO_CATEGORY = "DELETE FROM SongToCategory WHERE songID = %s "
REMOVE_SONG_FROM_SONGS_TO_ARTIST = "DELETE FROM SongToArtist WHERE songID = %s "
REMOVE_SONG_FROM_LYRICS = "DELETE FROM Lyrics WHERE songID = %s "
REMOVE_SONG_FROM_LYRICS_MyISAM = "DELETE FROM Lyrics_MyISAM WHERE songID = %s "
REMOVE_SONG_FROM_WORDS_PER_SONG = "DELETE FROM WordsPerSong WHERE songID = %s "

REMOVE_ARTIST_FROM_ARTIST_TO_CATEGORY = "DELETE FROM ArtistToCategory WHERE artistID = %s "
REMOVE_ARTIST_FROM_ARTISTS = "DELETE FROM Artists WHERE artistID = %s "