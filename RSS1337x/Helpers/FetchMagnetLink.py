from .__init__ import *


def fetch_magnet_link(link):
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            magnet_link = soup.select_one(
                'ul.dropdown-menu').select('li')[-1].select_one('a')['href']
        except:
            return None

        title = soup.find('title').text[9:-16]
        return {
            "title": title,
            "link": magnet_link.strip()
        }
    else:
        return None
