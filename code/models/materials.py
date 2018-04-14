# -*- coding: utf-8 -*-
from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    TIMESTAMP,
)

from .base import Base


__all__ = ['Schleem', 'Dinglepop', 'Fleeb', 'Chumble']


class Schleem(Base):
    __tablename__ = 'schleem'

    id = Column(String, primary_key=True)

    height = Column(Integer)
    width = Column(Integer)
    
    harvested_at = Column(TIMESTAMP)
    batch = Column(String)

    def __repr__(self):
        return "<Schleem id='{}' harvested_at={}".format(
            self.id, self.harvested_at)


class Dinglepop(Base):
    __tablename__ = 'dinglepop'

    id = Column(String, primary_key=True)

    origin = Column(String)
    weight = Column(Integer)

    def __repr__(self):
        return "<Dinglepop id='{}' origin={}".format(
            self.id, self.origin)


class Fleeb(Base):
    __tablename__ = 'fleeb'

    id = Column(String, primary_key=True)

    organic = Column(Boolean, default=True)
    picked_on = Column(TIMESTAMP)

    def __repr__(self):
        return "<Fleeb id='{}' picked_on={}".format(
            self.id, self.picked_on)


class Chumble(Base):
    __tablename__ = 'chumble'

    id = Column(String, primary_key=True)

    length = Column(Integer)
    diameter = Column(Integer)

    def __repr__(self):
        return "<Chumble id='{}' diameter={}".format(
            self.id, self.diameter)
