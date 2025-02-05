from fastapi import FastAPI

from nephyx.core.settings import nephyxSettings


class nephyxApi(FastAPI):
    def __init__(self, settings_cls: type[nephyxSettings] = nephyxSettings):
        super().__init__()
        self.settings = settings_cls()
