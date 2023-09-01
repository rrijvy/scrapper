class Proxy:
    def __init__(self, proxy: str) -> None:
        self.ip: str = proxy.split(":")[0]
        self.port: str = proxy.split(":")[1]
        self.isActive: bool = False
