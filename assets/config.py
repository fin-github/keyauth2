class Config:
    def __init__(self):
        from json import loads as load
        self.raw = open("configs/config.json", 'r').read()
        self.config = load(self.raw)
    def get(self, key: str):
        return self.config[key]

conf = Config()