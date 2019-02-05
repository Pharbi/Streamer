from os.path import join, dirname
from dotenv import load_dotenv
import os

class Config():

    """
        Intializing python env variables as Config object
    """

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    def __init__(self):
        self.cli_id = os.getenv('CLI_ID')
        self.cli_secret = os.getenv('CLI_SECRET')
        self.redirect_uri = os.getenv('REDIRECT_URI')
