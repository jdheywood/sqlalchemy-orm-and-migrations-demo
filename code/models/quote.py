# -*- coding: utf-8 -*-
from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    TIMESTAMP,
)

from .base import Base


__all__ = ['Quote']


class Quote(Base):
    __tablename__ = 'quote'

    id = Column(String, primary_key=True)

    who = Column(String)
    what = Column(String)
    
    def __repr__(self):
        return "<Quote id='{}' who={} what={}".format(
            self.id, self.who, self.what)
