from decouple import config


class Config:

    PRODUCTION: bool = config("PRODUCTION", cast=bool)


config = Config()