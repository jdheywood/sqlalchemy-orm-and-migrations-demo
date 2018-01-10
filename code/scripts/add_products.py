# -*- coding: utf-8 -*-
import uuid
import os
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import models


def _get_engine(isolation_level=None):
    connection_uri = "postgresql://vagrant:vagrant@localhost:5432/demo"
    if isolation_level:
        return create_engine(connection_uri, isolation_level=isolation_level)

    return create_engine(connection_uri)


def _get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


def create_plumbus(session):
    schleem = session.query(models.Schleem).first()
    dinglepop = session.query(models.Dinglepop).filter_by(origin='Universe #72').one_or_none()
    fleeb = session.query(models.Fleeb).first()
    chumble = session.query(models.Chumble).first()

    plumbus = models.Plumbus(
        id=uuid.uuid4(),
        schleem_id=schleem.id,
        dinglepop_id=dinglepop.id,
        fleeb_id=fleeb.id,
        chumble_id=chumble.id,
        manufactured_on=datetime.datetime.utcnow()
    )
    session.add(plumbus)
    session.commit()


if __name__ == '__main__':
    print('Start...')
    engine_main = _get_engine()
    session_main = _get_session(engine_main)

    print('Creating a Plumbus')
    create_plumbus(session_main)

    session_main.close()

    print('Fin.')
