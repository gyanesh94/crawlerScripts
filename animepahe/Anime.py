from helper_functions import get_anime_url_path

class Anime:
    def __init__(self, anime_name="", anime_url=""):
        self.anime_name = anime_name
        self.anime_url = anime_url
        self.episode_list = []
        self.summary = ""
        self.anime_id = ""
        self.anime_path = get_anime_url_path(anime_url)
