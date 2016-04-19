from Configuration import Configuration
from sqlalchemy.orm import load_only
import config
from Schemas import TaHotelReview1
from sqlalchemy import func

class Base:

    def __init__(self):
        try:
            configuration = Configuration()
            self.session = configuration.getConfig()
            print 'hello'
	    maxHotelId = self.session.query(func.max(TaHotelReview1.id)).first()
	    print maxHotelId
        except Exception as ex:
            print ex


obj = Base()
