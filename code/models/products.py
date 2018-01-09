# -*- coding: utf-8 -*-
from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    TIMESTAMP,
)

from .base import Base


__all__ = ['Plumbus']


class Plumbus(Base):
    __tablename__ = 'plumbus'

    id = Column(String, primary_key=True)

    schleem_id = Column(String, ForeignKey('schleem.id'))
    dinglepop_id = Column(String, ForeignKey('dinglepop.id'))
    fleeb_id = Column(String, ForeignKey('fleeb.id'))
    chumble_id = Column(String, ForeignKey('chumble.id'))
    
    manufactured_on = Column(TIMESTAMP)

    def __repr__(self):
        return "<Plumbus id='{}' manufactured_on={}".format(
            self.id, self.manufactured_on)
