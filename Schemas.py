# coding: utf-8
from sqlalchemy import Column, Enum, Float, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class TaHotelReview1(Base):
    __tablename__ = 'ta_hotel_review1'

    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, nullable=False)
    partner_hotel_id = Column(Integer)
    match_verdict = Column(Enum(u'MATCH', u'UNSURE', u'NOT_EXISTS'))
    partner_review_id = Column(Integer)
    language = Column(String(8))
    published_date = Column(String(256))
    rating = Column(Float, nullable=False)
    helpful_votes = Column(Integer)
    rating_image_url = Column(Text)
    review_url = Column(Text)
    trip_type = Column(String(256))
    travel_date = Column(String(256))
    review_text = Column(Text)
    reviewer_name = Column(String(256))
    reviewer_location_name = Column(String(256))
    reviewer_location_id = Column(Integer)
    review_title = Column(Text)
    owner_response = Column(Text)
    subratings = Column(Text)
