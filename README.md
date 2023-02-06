# Gogoanime 
Unofficial python wrapper for Gogoanime API
## Important

<p align="center"><a href="https://discord.otakatsu.studio"> <img src="https://img.shields.io/badge/Discord%20Server-pink?style=for-the-badge" width="220" height="38.45"/></a></p>
<p align="center"><a href="https://telegram.otakatsu.studio"> <img src="https://img.shields.io/badge/Telegram%20Channel-pink?style=for-the-badge" width="220" height="38.45"/></a></p>


## Installation
```$ pip install gogoanime```

## Usage
### 1. Importing the Library
```from gogoanime import get_search_results, get_anime_details, get_anime_episode, get_anime_popular, get_anime_newseason, get_anime_recent```
### 2. Searching manga
```anime_search = get_search_results(query="Naruto", page=1)```
###
#### Anime Search Result
```
[{'title': 'Naruto', 'image': 'https://gogocdn.net/images/anime/N/naruto.jpg', 'id': 'naruto'},
 {'title': 'Naruto (Dub)', 'image': 'https://gogocdn.net/cover/naruto-dub.png', 'id': 'naruto-dub'},
 {'title': 'Naruto Shippuden', 'image': 'https://gogocdn.net/images/anime/naruto_shippuden.jpg', 'id': 'naruto-shippuden'},
 {'title': 'Naruto Shippuden (Dub)', 'image': 'https://gogocdn.net/cover/naruto-shippuuden-dub.png', 'id': 'naruto-shippuuden-dub'},
 {'title': 'Boruto: Naruto the Movie', 'image': 'https://gogocdn.net/images/upload/175815.jpg', 'id': 'boruto-naruto-the-movie'},
 {'title': 'Naruto Shippuden Movie 1', 'image': 'https://gogocdn.net/images/anime/N/Naruto-Shippuuden-Movie-1.jpg', 'id': 'naruto-shippuuden-movie-1'},
 {'title': 'Boruto: Naruto the Movie (Dub)', 'image': 'https://gogocdn.net/cover/boruto-naruto-the-movie-dub.png', 'id': 'boruto-naruto-the-movie-dub'},
 {'title': 'Boruto: Naruto Next Generations', 'image': 'https://gogocdn.net/cover/boruto-naruto-next-generations.png', 'id': 'boruto-naruto-next-generations'},
 {'title': 'Naruto: Shippuuden Movie 1 (Dub)', 'image': 'https://gogocdn.net/cover/naruto-shippuuden-movie-1-dub.png', 'id': 'naruto-shippuuden-movie-1-dub'},
 {'title': 'Naruto Shippuden Movie 5 Special', 'image': 'https://gogocdn.net/images/004.jpg', 'id': 'naruto-shippuden-movie-5-special'},
 {'title': 'The Last: Naruto the Movie (Dub)', 'image': 'https://gogocdn.net/cover/the-last-naruto-the-movie-dub.png', 'id': 'the-last-naruto-the-movie-dub'},
 {'title': 'Naruto Shippuden Movie 2: Kizuna', 'image': 'https://gogocdn.net/images/anime/N/Naruto-Shippuuden-Movie-2.jpg', 'id': 'naruto-shippuuden-movie-2-kizuna'},
 {'title': 'Naruto Shippuden Movie 7: The Last', 'image': 'https://gogocdn.net/images/upload/67631.jpg', 'id': 'naruto-shippuuden-movie-7-the-last'},
 {'title': 'Naruto Shippuden: Sunny Side Battle', 'image': 'https://gogocdn.net/images/Naruto Shippuuden.jpg', 'id': 'naruto-shippuuden-sunny-side-battle'},
 {'title': 'Boruto: Naruto Next Generations (Dub)', 'image': 'https://gogocdn.net/cover/boruto-naruto-next-generations-dub.png', 'id': 'boruto-naruto-next-generations-dub'},
 {'title': 'Naruto Shippuden Movie 5: Blood Prison', 'image': 'https://gogocdn.net/images/anime/N/Naruto-Shippuuden-Movie-5.jpg', 'id': 'naruto-shippuuden-movie-5-blood-prison'},
 {'title': 'Naruto Shippuden Movie 6: Road to Ninja', 'image': 'https://gogocdn.net/images/anime/N/Naruto-Shippuuden-Movie-6.jpg', 'id': 'naruto-shippuuden-movie-6-road-to-ninja'},
 {'title': 'Naruto Shippuden Movie 4: The Lost Tower', 'image': 'https://gogocdn.net/images/anime/N/Naruto-Shippuuden-Movie-4.jpg', 'id': 'naruto-shippuuden-movie-4-the-lost-tower'},
 {'title': 'Naruto: Shippuuden Movie 2 - Kizuna (Dub)', 'image': 'https://gogocdn.net/cover/naruto-shippuuden-movie-2-kizuna-dub.png', 'id': 'naruto-shippuuden-movie-2-kizuna-dub'},
 {'title': 'Naruto: Akaki Yotsuba no Clover wo Sagase', 'image': 'https://gogocdn.net/cover/naruto-akaki-yotsuba-no-clover-wo-sagase.png', 'id': 'naruto-akaki-yotsuba-no-clover-wo-sagase'}]
```
###
#### Getting the title of anime search results:
```
for k in anime_search:
    print(k.get('title'))
```
###
#### This will print the following:
```
Naruto
Naruto (Dub)
Naruto Shippuden
Naruto Shippuden (Dub)
Boruto: Naruto the Movie
Naruto Shippuden Movie 1
Boruto: Naruto the Movie (Dub)
Boruto: Naruto Next Generations
Naruto: Shippuuden Movie 1 (Dub)
Naruto Shippuden Movie 5 Special
The Last: Naruto the Movie (Dub)
Naruto Shippuden Movie 2: Kizuna
Naruto Shippuden Movie 7: The Last
Naruto Shippuden: Sunny Side Battle
Boruto: Naruto Next Generations (Dub)
Naruto Shippuden Movie 5: Blood Prison
Naruto Shippuden Movie 6: Road to Ninja
Naruto Shippuden Movie 4: The Lost Tower
Naruto: Shippuuden Movie 2 - Kizuna (Dub)
Naruto: Akaki Yotsuba no Clover wo Sagase
```
### 3. Anime Details
```anime_details = get_anime_details(id="naruto")```
###
#### Anime Details Result
```
[{'title': 'Naruto',
'release': '2002', 
'other_names': 'Other name: ナルト', 
'type': 'TV Series', 
'status': 'Completed', 
'genre': "['Action', 'Comedy', 'Martial Arts', 'Shounen', 'Super Power']", 
'total_episode': '220', 
'image': 'https://gogocdn.net/images/anime/N/naruto.jpg', 
'description': ' In a world of mystical and powerful enemies lurk in every nation, a legendary Nine-Tailed Demon Fox attacked the ninja village Konoha, killing many innocent people. In response of a desperate measure from the people, the leader of the village – the Fourth Hokage – sacrificed his life to defeat the demon fox. By sacrificing his own life, he sealed the demon fox into a very young boy named, Naruto Uzumaki. Naruto has lost his parents during the attack. He grew up in the village and was mistreated badly by everyone in town.\r\n\r\nWith his loud mouth and careless attitude, he is determined to become the greatest ninja, hokage, in his village. Along with friends, and hope, Naruto trains to become a better ninja than expected.'}]
```
###
#### Specific Result of Anime Detail
```
title = manga_details.get('title')
print(title)
```

### 4. Anime Episode
```anime_episode = get_anime_episode(email="pranavajay712@gmail.com", password="otakatsu123", id="naruto", episode=1)```
###
#### Anime Episode Result
```
[{'quality': '360p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDURASDGHUSRFSJGYfdsffsderFStewthsfSFtrftesdfUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuMzYwcC5tcDQ/dG9rZW49RndJSmZBWVhLcTJfTXZheTUxWkRnZyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDY0MHgzNjAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'},
 {'quality': '480p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDURASDGHUSRFSJGYfdsffsderFStewthsfSFtrftesdfUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuNDgwcC5tcDQ/dG9rZW49YVJBMDNZTmU0c2RBLURlNldDM0FxdyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDg1NHg0ODAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'},
 {'quality': '720p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyURASDGHUSRFSJGYfdsffsderFStewthsfSFtrfteAdeqwrwedffryretgsdFrsftrsvfsfsrsdf9jZG54MDUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuNzIwcC5tcDQ/dG9rZW49a2VNYjRRTUxkbTlWdWdyUEk1RnJGdyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDEyODB4NzIwLWdvZ29hbmltZSluYXJ1dG8tZXBpc29kZS0xLm1wNA=='},
 {'quality': '1080p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDAawehyfcghysfdsDGDYdgdsfsdfwstdgdsgtertUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuMTA4MHAubXA0P3Rva2VuPWdENmhCcWNMN0ljV244cWxBQXk1WkEmZXhwaXJlcz0xNjc1NjYzOTc4JmlkPTI1MDU0JnRpdGxlPSgxOTIweDEwODAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'}][{'quality': '360p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDURASDGHUSRFSJGYfdsffsderFStewthsfSFtrftesdfUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuMzYwcC5tcDQ/dG9rZW49RndJSmZBWVhLcTJfTXZheTUxWkRnZyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDY0MHgzNjAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'}, {'quality': '480p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDURASDGHUSRFSJGYfdsffsderFStewthsfSFtrftesdfUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuNDgwcC5tcDQ/dG9rZW49YVJBMDNZTmU0c2RBLURlNldDM0FxdyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDg1NHg0ODAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'}, {'quality': '720p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyURASDGHUSRFSJGYfdsffsderFStewthsfSFtrfteAdeqwrwedffryretgsdFrsftrsvfsfsrsdf9jZG54MDUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuNzIwcC5tcDQ/dG9rZW49a2VNYjRRTUxkbTlWdWdyUEk1RnJGdyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDEyODB4NzIwLWdvZ29hbmltZSluYXJ1dG8tZXBpc29kZS0xLm1wNA=='}, {'quality': '1080p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDAawehyfcghysfdsDGDYdgdsfsdfwstdgdsgtertUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuMTA4MHAubXA0P3Rva2VuPWdENmhCcWNMN0ljV244cWxBQXk1WkEmZXhwaXJlcz0xNjc1NjYzOTc4JmlkPTI1MDU0JnRpdGxlPSgxOTIweDEwODAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'}][{'quality': '360p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDURASDGHUSRFSJGYfdsffsderFStewthsfSFtrftesdfUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuMzYwcC5tcDQ/dG9rZW49RndJSmZBWVhLcTJfTXZheTUxWkRnZyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDY0MHgzNjAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'}, {'quality': '480p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDURASDGHUSRFSJGYfdsffsderFStewthsfSFtrftesdfUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuNDgwcC5tcDQ/dG9rZW49YVJBMDNZTmU0c2RBLURlNldDM0FxdyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDg1NHg0ODAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'}, {'quality': '720p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyURASDGHUSRFSJGYfdsffsderFStewthsfSFtrfteAdeqwrwedffryretgsdFrsftrsvfsfsrsdf9jZG54MDUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuNzIwcC5tcDQ/dG9rZW49a2VNYjRRTUxkbTlWdWdyUEk1RnJGdyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDEyODB4NzIwLWdvZ29hbmltZSluYXJ1dG8tZXBpc29kZS0xLm1wNA=='}, {'quality': '1080p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDAawehyfcghysfdsDGDYdgdsfsdfwstdgdsgtertUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuMTA4MHAubXA0P3Rva2VuPWdENmhCcWNMN0ljV244cWxBQXk1WkEmZXhwaXJlcz0xNjc1NjYzOTc4JmlkPTI1MDU0JnRpdGxlPSgxOTIweDEwODAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'}][{'quality': '360p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDURASDGHUSRFSJGYfdsffsderFStewthsfSFtrftesdfUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuMzYwcC5tcDQ/dG9rZW49RndJSmZBWVhLcTJfTXZheTUxWkRnZyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDY0MHgzNjAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'}, {'quality': '480p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDURASDGHUSRFSJGYfdsffsderFStewthsfSFtrftesdfUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuNDgwcC5tcDQ/dG9rZW49YVJBMDNZTmU0c2RBLURlNldDM0FxdyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDg1NHg0ODAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'}, {'quality': '720p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyURASDGHUSRFSJGYfdsffsderFStewthsfSFtrfteAdeqwrwedffryretgsdFrsftrsvfsfsrsdf9jZG54MDUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuNzIwcC5tcDQ/dG9rZW49a2VNYjRRTUxkbTlWdWdyUEk1RnJGdyZleHBpcmVzPTE2NzU2NjM5NzgmaWQ9MjUwNTQmdGl0bGU9KDEyODB4NzIwLWdvZ29hbmltZSluYXJ1dG8tZXBpc29kZS0xLm1wNA=='}, {'quality': '1080p', 'link': 'https://gogodownload.net/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9jZG54MDAawehyfcghysfdsDGDYdgdsfsdfwstdgdsgtertUuYW5pY2FjaGUubmV0L3VzZXIxMzQyLzYxOWI4MzJhZjhmMTZhODhjYTEzOTdjMmQ0YjJjODQ2L0VQLjEudjEuMTA4MHAubXA0P3Rva2VuPWdENmhCcWNMN0ljV244cWxBQXk1WkEmZXhwaXJlcz0xNjc1NjYzOTc4JmlkPTI1MDU0JnRpdGxlPSgxOTIweDEwODAtZ29nb2FuaW1lKW5hcnV0by1lcGlzb2RlLTEubXA0'}]
```
###

### 5. Anime - Popular, Newseason, Recent 
```anime_popular = get_anime_popular(page=1)
   anime_newseason = get_anime_newseason(page=1)
   anime_recent_sub = get_anime_recent(type=1, page=1)
   anime_recent_dub = get_anime_recent(type=2, page=1)
```
###
### Anime Popular
```
[{'title': 'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka IV: Fuka Shou - Yakusai-hen', 'image': 'https://gogocdn.net/cover/dungeon-ni-deai-wo-motomeru-no-wa-machigatteiru-darou-ka-iv-fuka-shou-yakusai-hen.png', 'id': 'dungeon-ni-deai-wo-motomeru-no-wa-machigatteiru-darou-ka-iv-fuka-shou-yakusai-hen'},
 {'title': 'Boruto: Naruto Next Generations', 'image': 'https://gogocdn.net/cover/boruto-naruto-next-generations.png', 'id': 'boruto-naruto-next-generations'},
 {'title': 'NieR:Automata Ver1.1a', 'image': 'https://gogocdn.net/cover/nierautomata-ver1-1a-1672331611.png', 'id': 'nierautomata-ver1-1a'},
 {'title': 'Spy Kyoushitsu', 'image': 'https://gogocdn.net/cover/spy-kyoushitsu-1672332673.png', 'id': 'spy-kyoushitsu'},
 {'title': 'Tomo-chan wa Onnanoko!', 'image': 'https://gogocdn.net/cover/tomo-chan-wa-onnanoko-1672333039.png', 'id': 'tomo-chan-wa-onnanoko'},
 {'title': 'Detective Conan', 'image': 'https://gogocdn.net/cover/detective-conan.png', 'id': 'detective-conan'},
 {'title': 'One Piece', 'image': 'https://gogocdn.net/images/anime/One-piece.jpg', 'id': 'one-piece'},
 {'title': 'Boku no Hero Academia 6th Season', 'image': 'https://gogocdn.net/cover/boku-no-hero-academia-6th-season-1664387814.png', 'id': 'boku-no-hero-academia-6th-season'},
 {'title': 'Ijiranaide, Nagatoro-san 2nd Attack', 'image': 'https://gogocdn.net/cover/ijiranaide-nagatoro-san-2nd-attack-1672330313.png', 'id': 'ijiranaide-nagatoro-san-2nd-attack'},
 {'title': 'Vinland Saga Season 2', 'image': 'https://gogocdn.net/cover/vinland-saga-season-2-1672333695.png', 'id': 'vinland-saga-season-2'},
 {'title': 'Fumetsu no Anata e 2nd Season', 'image': 'https://gogocdn.net/cover/fumetsu-no-anata-e-2nd-season-1662695170.png', 'id': 'fumetsu-no-anata-e-2nd-season'},
 {'title': 'Bungou Stray Dogs 4th Season', 'image': 'https://gogocdn.net/cover/bungou-stray-dogs-4th-season.png', 'id': 'bungou-stray-dogs-4th-season'},
 {'title': 'Tokyo Revengers: Seiya Kessen-hen', 'image': 'https://gogocdn.net/cover/tokyo-revengers-seiya-kessen-hen-1672332928.png', 'id': 'tokyo-revengers-seiya-kessen-hen'},
 {'title': 'Blue Lock', 'image': 'https://gogocdn.net/cover/blue-lock-1664387634.png', 'id': 'blue-lock'}, {'title': 'Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e Kayou II', 'image': 'https://gogocdn.net/cover/maou-gakuin-no-futekigousha-shijou-saikyou-no-maou-no-shiso-tensei-shite-shison-tachi-no-gakkou-e-kayou-2nd-season-part-2-1672331388.png', 'id': 'maou-gakuin-no-futekigousha-shijou-saikyou-no-maou-no-shiso-tensei-shite-shison-tachi-no-gakkou-e-kayou-2nd-season-part-2'},
 {'title': 'Kage no Jitsuryokusha ni Naritakute!', 'image': 'https://gogocdn.net/cover/kage-no-jitsuryokusha-ni-naritakute-1664388804.png', 'id': 'kage-no-jitsuryokusha-ni-naritakute'}, {'title': 'Mairimashita! Iruma-kun 3rd Season', 'image': 'https://gogocdn.net/cover/mairimashita-iruma-kun-3rd-season.png', 'id': 'mairimashita-iruma-kun-3rd-season'},
 {'title': 'Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2', 'image': 'https://gogocdn.net/cover/itai-no-wa-iya-nano-de-bougyoryoku-ni-kyokufuri-shitai-to-omoimasu-ii-1671337143.png', 'id': 'itai-no-wa-iya-nano-de-bougyoryoku-ni-kyokufuri-shitai-to-omoimasu-ii'},
 {'title': 'Kyokou Suiri Season 2', 'image': 'https://gogocdn.net/cover/kyokou-suiri-2nd-season-1672331068.png', 'id': 'kyokou-suiri-2nd-season'},
 {'title': 'Horimiya', 'image': 'https://gogocdn.net/cover/horimiya.png', 'id': 'horimiya'}]
```
###
### Anime Newseason 
```
[{'title': 'Hikari no Ou', 'image': 'https://gogocdn.net/cover/hikari-no-ou-1672330046.png', 'id': 'hikari-no-ou'},
 {'title': 'Ooyukiumi no Kaina', 'image': 'https://gogocdn.net/cover/ooyukiumi-no-kaina-1672332008.png', 'id': 'ooyukiumi-no-kaina'},
 {'title': 'Tondemo Skill de Isekai Hourou Meshi', 'image': 'https://gogocdn.net/cover/tondemo-skill-de-isekai-hourou-meshi-1672333091.png', 'id': 'tondemo-skill-de-isekai-hourou-meshi'},
 {'title': 'Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2', 'image': 'https://gogocdn.net/cover/itai-no-wa-iya-nano-de-bougyoryoku-ni-kyokufuri-shitai-to-omoimasu-ii-1671337143.png', 'id': 'itai-no-wa-iya-nano-de-bougyoryoku-ni-kyokufuri-shitai-to-omoimasu-ii'},
 {'title': 'Kubo-san wa Mob wo Yurusanai', 'image': 'https://gogocdn.net/cover/kubo-san-wa-mob-wo-yurusanai-1670555914.png', 'id': 'kubo-san-wa-mob-wo-yurusanai'}]
```
###
### Anime Recent Sub
```
[{'title': 'Gekitou! Crush Gear Turbo', 'image': 'https://gogocdn.net/cover/gekitou-crush-gear-turbo.png', 'id': 'gekitou-crush-gear-turbo', 'episode_id': 'gekitou-crush-gear-turbo-episode-22', 'episodenum': ' 22'}, 
 {'title': 'Cap Kakumei Bottleman DX', 'image': 'https://gogocdn.net/cover/cap-kakumei-bottleman-dx.png', 'id': 'cap-kakumei-bottleman-dx', 'episode_id': 'cap-kakumei-bottleman-dx-episode-44', 'episodenum': ' 44'}, {'title': 'Mou Ippon!', 'image': 'https://gogocdn.net/cover/mou-ippon-1672331529.png', 'id': 'mou-ippon', 'episode_id': 'mou-ippon-episode-5', 'episodenum': ' 5'}, 
 {'title': 'D4DJ All Mix', 'image': 'https://gogocdn.net/cover/d4dj-all-mix-1672329322.png', 'id': 'd4dj-all-mix', 'episode_id': 'd4dj-all-mix-episode-5', 'episodenum': ' 5'},
 {'title': 'IDOLiSH7: Third Beat! Part 2', 'image': 'https://gogocdn.net/cover/idolish7-third-beat-part-2.png', 'id': 'idolish7-third-beat-part-2', 'episode_id': 'idolish7-third-beat-part-2-episode-14', 'episodenum': ' 14'},
 {'title': 'Punirunes', 'image': 'https://gogocdn.net/cover/punirunes.png', 'id': 'punirunes', 'episode_id': 'punirunes-episode-18', 'episodenum': ' 18'}]
```
###
### Anime Recent Dub
```
[{'title': 'Kidou Senshi Gundam: Suisei no Majo (Dub)', 'image': 'https://gogocdn.net/cover/kidou-senshi-gundam-suisei-no-majo-dub.png', 'id': 'kidou-senshi-gundam-suisei-no-majo-dub', 'episode_id': 'kidou-senshi-gundam-suisei-no-majo-dub-episode-1', 'episodenum': ' 1'},
 {'title': 'Zoku Natsume Yuujinchou (Dub)', 'image': 'https://gogocdn.net/cover/zoku-natsume-yuujinchou-dub.png', 'id': 'zoku-natsume-yuujinchou-dub', 'episode_id': 'zoku-natsume-yuujinchou-dub-episode-12', 'episodenum': ' 12'},
 {'title': 'Pokemon (2019) (Dub)', 'image': 'https://gogocdn.net/cover/pokemon-2019-dub.png', 'id': 'pokemon-2019-dub', 'episode_id': 'pokemon-2019-dub-episode-121', 'episodenum': ' 121'},
 {'title': 'Utawarerumono: Futari no Hakuoro (Dub)', 'image': 'https://gogocdn.net/cover/utawarerumono-futari-no-hakuoro-dub.png', 'id': 'utawarerumono-futari-no-hakuoro-dub', 'episode_id': 'utawarerumono-futari-no-hakuoro-dub-episode-5', 'episodenum': ' 5'},
 {'title': 'Mairimashita! Iruma-kun 3rd Season (Dub)', 'image': 'https://gogocdn.net/cover/mairimashita-iruma-kun-3rd-season-dub.png', 'id': 'mairimashita-iruma-kun-3rd-season-dub', 'episode_id': 'mairimashita-iruma-kun-3rd-season-dub-episode-14', 'episodenum': ' 14'}]
```
###


