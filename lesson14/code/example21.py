class XMLHttpService(Connection):
    xhr = XMLHttpRequest()

    def request(self, url: str, options:dict):
        self.xhr.open()
        self.xhr.send()