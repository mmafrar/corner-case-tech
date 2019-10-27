class Config:
    def __init__(self):
        return self


class DatabaseConfig(Config):
    HOST = "localhost"
    USERNAME = "admin"
    PASSWORD = "admin"
    DATABASE = "food_menu_voting_app"
