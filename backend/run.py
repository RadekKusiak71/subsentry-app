import uvicorn
from decouple import config

if __name__ == "__main__":

    PRODUCTION: bool = config("PRODUCTION", cast=bool)

    if PRODUCTION:
        uvicorn.run(
            app = "src.main:app",
            host = "0.0.0.0",
            port = 80,
            reload = False
        )
    else:
        uvicorn.run(
            app = "src.main:app",
            host = "0.0.0.0",
            port = 80,
            reload = True
        )