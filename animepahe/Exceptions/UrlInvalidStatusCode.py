class UrlInvalidStatusCode(Exception):
    """Exception raised when anime ID not found.
    """

    def __init__(self, url="", status_code=""):
        super(UrlInvalidStatusCode, self).__init__(f"Url: {url}\nStatus code: {status_code}")
