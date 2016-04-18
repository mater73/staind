from Configuration import Configuration
from sqlalchemy.orm import load_only
import config

class Base:

    def __init__(self):
        try:
            configuration = Configuration()
            self.session = configuration.getConfig()
            print 'hello'
        except Exception as ex:
            print ex
