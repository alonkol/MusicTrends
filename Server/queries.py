
CATEGORIES = "SELECT categoryID as id, categoryName as name FROM Categories;"

TOP_SONG_LIKES = "SELECT songName, likeCount " \
                    "FROM songs, videos " \
                    "WHERE songs.songID = videos.songID " \
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
                "SELECT SongToCategory.songID, (POW(COUNT(WordsPerSong.word),2)/SUM(wordCount))*AVG(uniqueness) AS score " \
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

TOP_SOPHISTICATED_SONG_DISCUSSIONS = "SELECT songName, score " \
            "FROM " \
            "(" \
                "SELECT videoID, (POW(COUNT(commentWordsPerVideo.word),2)/SUM(commentWordCount))*AVG(uniqueness) AS score " \
                "FROM " \
                "(" \
				    "SELECT word, 1/SUM(commentWordCount) AS uniqueness " \
                    "FROM commentWordsPerVideo " \
                    "GROUP BY word " \
                ") AS wordUniqueness, commentWordsPerVideo " \
                "WHERE wordUniqueness.word = commentWordsPerVideo.word " \
                "GROUP BY commentWordsPerVideo.videoID " \
            ") AS a, songs, videos " \
            "WHERE songs.songID = videos.songID " \
            "AND videos.videoID = a.videoID " \
            "ORDER BY score DESC " \
            "LIMIT %s;"

TOP_SOPHISTICATED_SONG_DISCUSSIONS_PER_CATEGORY = "SELECT songName, score " \
            "FROM " \
            "(" \
                "SELECT videos.videoID, (POW(COUNT(commentWordsPerVideo.word),2)/SUM(commentWordCount))*AVG(uniqueness) AS score " \
                "FROM " \
                "(" \
				    "SELECT word, 1/SUM(commentWordCount) AS uniqueness " \
                    "FROM commentWordsPerVideo " \
                    "GROUP BY word " \
                ") AS wordUniqueness, commentWordsPerVideo, SongToCategory, videos " \
                "WHERE wordUniqueness.word = commentWordsPerVideo.word " \
                 "AND SongToCategory.categoryID = %s " \
                 "AND SongToCategory.songID = videos.songID " \
                 "AND videos.videoID = commentWordsPerVideo.videoID " \
                 "GROUP BY commentWordsPerVideo.videoID " \
            ") AS a, songs, videos " \
            "WHERE songs.songID = videos.songID " \
            "AND videos.videoID = a.videoID " \
            "ORDER BY score DESC " \
            "LIMIT %s;"

TOP_GROUPIES = "SELECT CONCAT(author, ' (', artistName, ')' ), COUNT(*) AS count  " \
                "FROM artists, " \
                "(" \
                    "SELECT author, songToArtist.artistID, videos.videoID " \
                    "FROM comments, songToArtist, videos " \
                    "WHERE comments.videoID = videos.videoID " \
                    "AND videos.songID = songToArtist.songID " \
                    "GROUP BY songToArtist.artistID, videos.videoID, author " \
                ") AS authorComments " \
                "WHERE artists.artistID = authorComments.artistID " \
                "GROUP BY author, artists.artistID " \
                "ORDER BY count DESC " \
                "LIMIT %s;" \

TOP_GROUPIES_PER_CATEGORY = "SELECT CONCAT(author, ' (', artistName, ')' ), COUNT(*) AS count " \
                "FROM artists, " \
                "(" \
                    "SELECT author, songToArtist.artistID, videos.videoID " \
                    "FROM comments, songToArtist, videos, songToCategory " \
                    "WHERE comments.videoID = videos.videoID " \
                    "AND videos.songID = songToArtist.songID " \
                    "AND songToCategory.songID = videos.songID " \
                    "AND songToCategory.categoryID = %s " \
                    "GROUP BY songToArtist.artistID, videos.videoID, author " \
                ") AS authorComments " \
                "WHERE artists.artistID = authorComments.artistID " \
                "GROUP BY author, artists.artistID " \
                "ORDER BY count DESC " \
                "LIMIT %s;" \

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


TOP_ARTIST_TEXT_COUPLES = "SELECT CONCAT(artist1, ' ~ ', artist2) AS couple, delta " \
                            " FROM " \
                            "(" \
                                "SELECT wc1.artistName AS artist1, wc2.artistName AS artist2, AVG(ABS(wc1.wordCount - wc2.wordCount)) AS delta " \
                                "FROM artistsWordCount AS wc1, artistsWordCount AS wc2 " \
                                "WHERE wc1.word = wc2.word " \
                                "GROUP BY wc1.artistID, wc2.artistID, wc1.artistName, wc2.artistName " \
                                "HAVING wc1.artistName < wc2.artistName " \
                            ") AS artistDeltas " \
                            "ORDER BY delta ASC " \
                            "LIMIT %s;" \

TOP_ARTIST_TEXT_COUPLES_PER_CATEGORY = "SELECT CONCAT(artist1, ' ~ ', artist2) AS couple, delta " \
                            " FROM " \
                            "(" \
                                "SELECT wc1.artistName AS artist1, wc2.artistName AS artist2, AVG(ABS(wc1.wordCount - wc2.wordCount)) AS delta " \
                                "FROM artistsWordCount AS wc1, artistsWordCount AS wc2 " \
                                "WHERE wc1.word = wc2.word " \
                                "AND wc1.categoryID = wc2.categoryID " \
                                "AND wc1.categoryID = %s " \
                                "GROUP BY wc1.artistID, wc2.artistID, wc1.artistName, wc2.artistName " \
                                "HAVING wc1.artistName < wc2.artistName " \
                            ") AS artistDeltas " \
                            "ORDER BY delta ASC " \
                            "LIMIT %s;"

TOP_DAYS_COMMENTS = "SELECT DAYNAME(comments.publishedAt) AS day, COUNT(*) AS count " \
                    "FROM comments, videos " \
                    "WHERE comments.videoID = videos.videoID " \
                    "GROUP BY day " \
                    "ORDER BY count DESC " \
                    "LIMIT %s;"


TOP_DAYS_COMMENTS_PER_CATEGORY = "SELECT DAYNAME(comments.publishedAt) AS day, COUNT(*) AS count " \
                                 "FROM comments, videos, songToCategory " \
                                 "WHERE comments.videoID = videos.videoID " \
                                 "AND videos.songID = songToCategory.songID " \
                                 "AND songToCategory.categoryID = %s " \
                                 "GROUP BY day " \
                                 "ORDER BY count DESC " \
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
                                            "SELECT SongToCategory.songID, dislikeCount/likeCount AS score " \
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

UPDATE_VIDEOS_DATA = "UPDATE Videos SET viewCount = %s, likeCount = %s, dislikeCount = %s WHERE videoID = %s"

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