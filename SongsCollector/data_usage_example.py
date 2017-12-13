>>> import json

>>> with open('data.json', 'r') as data:
	js_data = json.load(data)

	
>>> # Genres
>>> for i in js_data['items']:
	print i['genre']

	
Pop Music
Electronic Music
Hip Hop Music
Rock Music
House Music
Alternative Rock
Classical Music
Deep House
Electronic Dance Music
Trance Music
Latin American Music
Reggae
Trap Music
Pop Rock
Middle Eastern Music
Soul Music
Psychedelic Trance
Heavy Metal Music
Jazz
Indie Music
New-Age Music
Arabic Music
Contemporary R&amp;B
Electro House
Asian Music
Dancehall
Rhythm &amp; Blues
>>> # songs
>>> js_data['items'][0].keys()
[u'nextPageToken', u'kind', u'items', u'etag', u'genre', u'pageInfo']
>>> js_data['items'][0]['items'][0].keys()
[u'snippet', u'contentDetails', u'kind', u'etag', u'id']

>>> js_data['items'][0]['items'][0]['snippet'].keys()
[u'channelId', u'description', u'title', u'resourceId', u'playlistId', u'publishedAt', u'channelTitle', u'position', u'thumbnails']
>>> js_data['items'][0]['items'][0]['snippet']['title']
u'Camila Cabello - Havana ft. Young Thug'