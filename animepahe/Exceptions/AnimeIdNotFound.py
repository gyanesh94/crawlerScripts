class AnimeIdNotFound(Exception):
    """Exception raised when anime ID not found.
    """

    def __init__(self, url=""):
        super(AnimeIdNotFound, self).__init__(f"Anime ID not found url: {url}")
