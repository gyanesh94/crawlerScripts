class Episode:
    def __init__(self):
        self.name = ""
        self.session = ""
        self.id = ""
        self.index = ""

    def parse_from_dict(self, data):
        self.name = data.get("title", "")
        self.session = data.get("session", "")
        self.id = data.get("id", -1)
        self.index = data.get("episode", -1)

    def __str__(self):
        s = "Episode("
        if self.name:
            s += f"Name: {self.name}, "
        if self.index != -1:
            s += f"Index: {self.index}, "
        if self.id != -1:
            s += f"ID: {self.id}, "
        if self.session:
            s += f"Session: {self.session}"
        s += ")"
        return s
