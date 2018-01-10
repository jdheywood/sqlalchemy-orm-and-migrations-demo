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


def remove_plumbus(session):
    session.query(models.Plumbus).delete()
    session.commit()


if __name__ == '__main__':
    print('Start...')
    engine_main = _get_engine()
    session_main = _get_session(engine_main)

    print('Removing materials data')
    remove_plumbus(session_main)

    session_main.close()

    print('Fin.')
