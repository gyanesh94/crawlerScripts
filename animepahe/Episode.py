class DowloadLink:
    def __init__(self):
        self.resolution = ""
        self.audio = ""
        self.disc = ""
        self.kwik = ""
        self.kwik_shst = ""
        self.kwik_adfly = ""
    
    def parse_from_dict(self, resolution: str, data: dict):
        self.resolution = resolution
        self.audio = data.get("audio", "")
        self.disc = data.get("disc", "")
        self.kwik = data.get("kwik", "").replace("kwik.cx/e/", "kwik.cx/f/")
        self.kwik_shst = data.get("kwik_shst", "")
        self.kwik_adfly = data.get("kwik_adfly", "")

    def __repr__(self):
        return str(self)

    def __str__(self):
        l = []

        if self.resolution:
            l.append(f"Resolution: {self.resolution}")
        if self.audio:
            l.append(f"audio: {self.audio}")
        if self.disc:
            l.append(f"ID: {self.disc}")
        if self.kwik:
            l.append(f"kwik: {self.kwik}")
        if self.kwik_shst:
            l.append(f"kwik_shst: {self.kwik_shst}")
        if self.kwik_adfly:
            l.append(f"kwik_adfly: {self.kwik_adfly}")

        s = f"DowloadLink({', '.join(l)})"
        return s


class Episode:
    def __init__(self):
        self.name = ""
        self.session = ""
        self.id = ""
        self.index = ""
        self.download_detail = []

    def parse_from_dict(self, data):
        self.name = data.get("title", "")
        self.session = data.get("session", "")
        self.id = data.get("id", -1)
        self.index = data.get("episode", -1)
    
    def add_download_links(self, download_links_list: list):
        download_links: dict
        for download_links in download_links_list:
            resolution: str
            download_link: dict
            for resolution, download_link in download_links.items():
                dowloadLink = DowloadLink()
                dowloadLink.parse_from_dict(resolution, download_link)
                self.download_detail.append(dowloadLink)

    def set_name(self, name):
        if not self.name:
            self.name = name

    def __repr__(self):
        return str(self)

    def __str__(self):
        l = []

        if self.name:
            l.append(f"Name: {self.name}")
        if self.index != -1:
            l.append(f"Index: {self.index}")
        if self.id != -1:
            l.append(f"ID: {self.id}")
        if self.session:
            l.append(f"Session: {self.session}")
        if self.download_detail:
            l.append(f"download_detail: {self.download_detail}")

        s = f"Episode({', '.join(l)})"
        return s
