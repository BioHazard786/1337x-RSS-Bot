from .__init__ import *


def fetch_torrent_info(link):
    t_info = dict()
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            torrent_link = soup.select_one(
                'ul.dropdown-menu').select_one('li').select_one('a')['href']
        except:
            torrent_link = link

        t_info['torrent_link'] = torrent_link
        title = soup.find('title').text[9:-16]
        t_info['title'] = title
        torrent_meta_info = soup.select('ul.list')[1].select('li')
        for info in torrent_meta_info:
            t_info[info.select_one('strong').text.strip()] = info.select_one(
                'span').text.strip()

        return t_info
    else:
        return None
