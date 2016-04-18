import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Schemas import Base

class Configuration:

    config =  None

    def __init__(self):
        self.config = config.config


    def getConfig(self):
        try:
            self.engine = create_engine(
                    'mysql://'+self.config.get('user') + ':'
                    + self.config.get('password') + '@'
                    + self.config.get('host') + '/'
                    + self.config.get('schema'),
                    pool_recycle = 3600,
                    pool_size = -1,
                    max_overflow = 100)

            Base.metadata.bind = self.engine
            self.DBSession = sessionmaker(bind=self.engine)
            return self.DBSession()
        except Exception as ex:
            print ex
