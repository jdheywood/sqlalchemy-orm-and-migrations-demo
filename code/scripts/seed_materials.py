# -*- coding: utf-8 -*-
import uuid
import os
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text

import models


def _get_engine(conn_id, isolation_level=None):
    connection_uri = "postgresql://vagrant:vagrant@localhost:5432/demo"
    if isolation_level:
        return create_engine(connection_uri, isolation_level=isolation_level)

    return create_engine(connection_uri)


def _get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


def seed_materials(session):
    # Add example models here
    schleem = models.Schleem(
        id=uuid.uuid4(),
        height=123,
        width=456,
        harvested_at=datetime.datetime.utcnow(),
        batch='098-qwerty'
    )

    session.add(schleem)

    session.commit()


if __name__ == '__main__':
    print('Start...')
    engine_main = _get_engine("demo")
    session_main = _get_session(engine_main)

    print('Seeding materials data')
    seed_materials(session_main)

    session_main.close()

    print('Fin.')
