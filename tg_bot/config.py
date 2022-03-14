from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1584582613  # my telegram ID
    OWNER_USERNAME = "KING"  # my telegram username
    API_KEY = "your bot api key"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [236390091, 334255172,  755569473,  1584582613, 1269645128]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
