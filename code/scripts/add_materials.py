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


def add_schleem(session):
    schleem = models.Schleem(
        id=uuid.uuid4(),
        height=123,
        width=456,
        harvested_at=datetime.datetime.utcnow(),
        batch='098-qwerty'
    )
    session.add(schleem)
    session.commit()


def add_dinglepops(session):
    for i in range(1, 6, 1):
        dinglepop = models.Dinglepop(
            id=uuid.uuid4(),
            origin="Universe #{}".format((i * 23) + i),
            weight=5*i
        )
        session.add(dinglepop)

    session.commit()

def add_fleeb(session):
    fleeb = models.Fleeb(
        id=uuid.uuid4(),
        organic=False,
        picked_on=datetime.datetime.utcnow()
    )
    session.add(fleeb)
    session.commit()


def add_chumbles(session):
    for i in range(1, 4, 1):
        chumble = models.Chumble(
            id=uuid.uuid4(),
            length=((i * 17) + 4),
            diameter=((i * 9) + 2 * (i-1))
        )
        session.add(chumble)

    session.commit()


if __name__ == '__main__':
    print('Start...')
    engine_main = _get_engine()
    session_main = _get_session(engine_main)

    print('Adding materials data')
    add_schleem(session_main)
    add_dinglepops(session_main)
    add_fleeb(session_main)
    add_chumbles(session_main)

    session_main.close()

    print('Fin.')
