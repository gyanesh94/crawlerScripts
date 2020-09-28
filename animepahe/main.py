from Anime import Anime
from config import CURRENT_DOWNLOAD
from Episode import Episode
from Exceptions.AnimeIdNotFound import AnimeIdNotFound
from helper_functions import episode_list_url, extract_text, get_src, list_empty, parse_html, print_object, print_text

import json
import re


class Download:
    def __init__(self, current_anime: Anime):
        self.current_anime: Anime = current_anime

    def dowload_anime_page(self):
        self.src = get_src(self.current_anime.anime_url)

    def get_anime_id(self):
        result = re.findall(r'/api\?m=release&id=([\d]+)&', self.src)
        if list_empty(result):
            raise AnimeIdNotFound(self.current_anime.anime_url)
        self.current_anime.anime_id = result[0]
    
    def get_anime_summary(self):
        soup = parse_html(self.src)
        div = soup.find("div", {"class": "anime-synopsis"})
        if div is None:
            return
        self.current_anime.summary = extract_text(div)

    def get_episode_urls(self):
        page = 1
        episode_api_url = episode_list_url(self.current_anime.anime_id, page)
        while True:
            src = get_src(episode_api_url)
            data = json.loads(src)
            episode_data: list = data.get("data", [])
            for index in range(0, len(episode_data)):
                episode = Episode()
                episode.parse_from_dict(episode_data[index])
                if episode.id == -1 or not len(episode.session):
                    print_text(f"**** Warn: Anime: {self.current_anime.anime_name}, episode not found. API: {episode_api_url}, index: {index}")
                else:
                    self.current_anime.episode_list.append(episode)
            if data.get("next_page_url", None) is None or page >= data.get("last_page", 0):
                return
            episode_api_url = episode_list_url(self.current_anime.anime_id, (page := page + 1))



def main():
    f = Download(CURRENT_DOWNLOAD)
    f.dowload_anime_page()
    f.get_anime_id()
    f.get_anime_summary()
    f.get_episode_urls()


if __name__ == "__main__":
    main()
