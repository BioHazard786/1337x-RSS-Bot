from .__init__ import *


def fetch_torrents(user):
    response = requests.get(Torrent_User.GetLink(user))
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        torrents_title = soup.select('td.coll-1.name')
        torrents = []
        for torrent in torrents_title:
            try:
                torrent_link = 'https://1337x.to' + \
                    torrent.findChildren()[2]["href"]
            except:
                continue
            torrents.append(torrent_link)

        return torrents
    else:
        return None
