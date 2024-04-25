import uvicorn
from fastapi import FastAPI

from core.config import settings
from core.database import create_tables


class GameBuddyApp:
    """ Объект, управляющий жизненным циклом приложения """
    fastapi_app: FastAPI

    def __init__(self):
        self._build_fastapi()
        self.setup()

    def _build_fastapi(self):
        self.fastapi_app = FastAPI(
            title="GameBuddy", 
            description="A simple API for GameBuddy",
            version=settings.app.APP_VERSION
        )

    def setup(self):
        pass
        # create_tables()

    def run(self, debug_mode=False):
        """ 
        ### Описание
        Запускает сервер, который будет принимать запросы на API.

        ### Параметры:
            - `debug_mode: Bool` 
                - `True` - передает в `uvicorn.run` строку пути к экземпляру приложения
                - `False` - передает в `uvicorn.run` сам экземпляр приложения, что гарантирует выключение `reload`,
                  даже если `reload=True` (так работает uvicorn).
        """
        instance: FastAPI | str = "core.application:gamebuddy_app.fastapi_app" if debug_mode else self.fastapi_app

        uvicorn.run(
            instance,
            host=settings.uvicorn.HOST,
            port=settings.uvicorn.PORT,
            log_level=settings.uvicorn.LOG_LEVEL,
            reload=debug_mode,
        )

    def shutdown(self):
        """ А тут закрывать коннекты к БД напрмер """
        pass


gamebuddy_app = GameBuddyApp()
