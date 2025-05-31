from decouple import config


class Config:

    PRODUCTION: bool = config("PRODUCTION", cast=bool)
    DB_NAME: str = config("DB_NAME", cast=str)
    DB_USER: str = config("DB_USER", cast=str)
    DB_PASSWORD: str = config("DB_PASSWORD", cast=str)
    DB_HOST: str = config("DB_HOST", cast=str)
    DB_PORT: int = config("DB_PORT", cast=int)

config = Config()