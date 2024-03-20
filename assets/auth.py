class Auth:
    class AuthConfig:
        def __init__(self) -> None:
            from json import loads as load
            from assets.config import conf
            self.raw: str = open(
                conf.get("keys_file")
            ).read()
            
            self.config: dict = load(self.raw)
            self.keys: list[str] = self.config.keys()
    def __init__(self):
        self.AuthC = self.AuthConfig()
         
    def check_key(self, key: str, user_id: int):
        if not key in self.AuthC.keys: return False
        # if made to this point: key is available
        return self.AuthC.config[key] == user_id # if the keys userid matches the passed in user_id


if __name__ == "__main__":
    A = Auth()
    print(A.check_key(
        key=input("Key> "),
        user_id=int(input("UserID> "))
    ))