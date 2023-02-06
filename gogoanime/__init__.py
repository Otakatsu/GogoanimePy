from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

def gogo_auth(email, password):
    s = requests.session()
    animelink = "https://gogoanime.tel/login.html"
    response = s.get(animelink)
    response_html = response.text
    soup = BeautifulSoup(response_html, "html.parser")
    source_url = soup.select('meta[name="csrf-token"]')
    token = source_url[0].attrs["content"]


    data = f"email={email}&password={password}&_csrf={token}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; vivo 1916) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
        "authority": "gogo-cdn.com",
        "referer": f"https://gogoanime.tel/",
        "content-type": "application/x-www-form-urlencoded",
    }
    s.headers = headers
    

    r = s.post(animelink, data=data, headers=headers)

    if r.status_code == 200:
        return s.cookies.get_dict().get("auth")

def get_search_results(query, page = 0):
        animelink = f"https://gogoanime.tel/search.html?keyword={query}&page={page}"
        response = requests.get(animelink)
        response_html = response.text
        soup = BeautifulSoup(response_html, 'lxml')
        source_url = soup.find('div', 'last_episodes').find('ul', 'items').find_all("li")
        res_search_list = []
        for links in source_url:
            a = links.find('a')
            title = a["title"]
            img = links.find('img')['src']
                
            url = a['href']
            r = url.split('/')[2]

            res_search_list.append({"title": f"{title}", "image": f"{img}", "id": f"{r}"})
                
        if res_search_list == []:
            return {"status":"204", "reason":"No search results found for the query"}
        return res_search_list
        
def get_anime_newseason(page = 0):
        animelink = f"https://gogoanime.tel/new-season.html?page={page}"
        response = requests.get(animelink)
        response_html = response.text
        soup = BeautifulSoup(response_html, 'html.parser')
        source_url = soup.find('div', 'last_episodes').find('ul', 'items').find_all('li')
        res_newseason_list = []
        for links in source_url:
            a = links.find('a')
            title = links.find('p', 'name').text
            img = links.find('img')['src']
                
            id = a['href']
            
            r = id.replace('/category/', '')
                
            res_newseason_list.append({"title": f"{title}", "image": f"{img}", "id": f"{r}"})
                
        if res_newseason_list == []:
            return {"status":"204", "reason":"Wrong Page Id"}
        return res_newseason_list
        


def get_anime_popular(page = 0):
        animelink = f"https://gogoanime.tel/popular.html?page={page}"
        response = requests.get(animelink)
        response_html = response.text
        soup = BeautifulSoup(response_html, 'html.parser')
        source_url = soup.find('div', 'last_episodes').find('ul', 'items').find_all('li')
        res_newseason_list = []
        for links in source_url:
            a = links.find('a')
            title = links.find('p', 'name').text
            img = links.find('img')['src']
                
            id = a['href']
            
            r = id.replace('/category/', '')
                
            res_newseason_list.append({"title": f"{title}", "image": f"{img}", "id": f"{r}"})
              
        if res_newseason_list == []:
            return {"status":"204", "reason":"Wrong Page Id"}
        return res_newseason_list
        




def get_anime_recent(type = 1, page = 0):
        animelink = f"https://ajax.gogo-load.com/ajax/page-recent-release.html?page={page}&type={type}"
        response = requests.get(animelink)
        response_html = response.text
        soup = BeautifulSoup(response_html, 'html.parser')
        source_url = soup.find('ul','items').find_all('li')
        res_recent_list = []
        for links in source_url:
            a = links.find('a')
            title = links.find('p','name').text
            img = links.img['src']
            episode = links.find('p','episode').text
            id = a['href']
            
            r = id.replace('/', '')
            r2 = episode.replace('Episode', '')
            r3 = r.split('-episode-')[0]
            res_recent_list.append({"title": f"{title}", "image": f"{img}", "id": f"{r3}", "episode_id": f"{r}", "episodenum": f"{r2}"})
                
        if res_recent_list == []:
            return {"status":"204", "reason":"Wrong Page Id"}
        return res_recent_list
        



def get_anime_details(id):  
        animelink = f"https://gogoanime.tel/category/{id}"
        response = requests.get(animelink)
        plainText = response.text
        soup = BeautifulSoup(plainText, "lxml")
        source_url = soup.find("div", {"class": "anime_info_body_bg"}).img
        img = source_url.get('src')
        res_detail_list = []
        title = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
        dic = soup.find_all('p', {"class": "type"})
        psummary = dic[1]
        p = psummary.get_text().split(':')
        p.remove(p[0])
        sums = ""
        summary = sums.join(p)
        type = dic[0].a['title']
        genre = dic[2].find_all('a')  # .find_all('title')
        genres = []
        for x in genre:
            genres.append(x.get('title'))
        releaser = dic[3].get_text()
        releases = releaser.split(" ")
        release = releases[1]
        status = dic[4].a.get_text()
        other_names = dic[5].get_text()
        ep = soup.find(id="episode_page")
        Ep = ep.find_all("li")[-1].a
        totalep = int(Ep.get("ep_end"))
        res_detail_list.append({"title": f"{title}", "release": f"{release}", "other_names": f"{other_names}",
                             "type": f"{type}", "status": f"{status}", "genre": f"{genres}",
                             "total_episode": f"{totalep}", "image": f"{img}", "description": f"{summary}"})
                          
        if res_detail_list == []:
                return {"status":"204", "reason":"Wrong Anime Id"}
        return res_detail_list


def get_anime_episode(email, password, id, episode):
    auth_gogo = gogo_auth(email=email, password=password)


    if not auth_gogo:
        text = "invalid e-mail and password"
        return text
  
    
    if auth_gogo:
        res_episode_list = []
        animelink = requests.get(f"https://gogoanime.tel/{id}-episode-{episode}", cookies=dict(auth=auth_gogo))      
        soup = BeautifulSoup(animelink.content, "html.parser")
        source_url = soup.find("div", {'class': 'cf-download'}).findAll('a')
        for links in source_url:
            url = links['href']
            qualitys = links.text.strip().split('x')[1]
                                                  
            if qualitys == "360":
                link = url
                quality = "360p"
                                           
            elif qualitys == "480":
                link = url
                quality = "480p"
            elif qualitys == "720":
                link = url
                quality = "720p" 
            elif qualitys == "1080":
                link = url
                quality = "1080p" 
            res_episode_list.append({"quality": f"{quality}", "link": f"{link}"})
        if res_episode_list == []:
            return {"status":"204", "reason":"Wrong Anime Id And Episode"}
        return res_episode_list
                
            
             








                
