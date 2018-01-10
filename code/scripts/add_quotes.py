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


def add_quote(session, who, what):
    session.add(models.Quote(
        id=uuid.uuid4(),
        who=who,
        what=what
    ))
    
    session.commit()


if __name__ == '__main__':
    print('Start...')
    engine_main = _get_engine()
    session_main = _get_session(engine_main)

    print('Adding quotes data')
    add_quote(session_main, 'Morty', "Nobody exists on purpose. Nobody belongs anywhere. We're all going to die. Come watch TV.")
    add_quote(session_main, 'Rick', "Weddings are basically funerals with cake.")
    add_quote(session_main, 'Mr Meeseeks', "Existence is pain to a Meeseeks Jerry.")
    add_quote(session_main, 'Snuffles', "Do not call me that! Snuffles was my slave name, you can call me snowball because my fur is pretty and white.")
    add_quote(session_main, 'Bird Person', 'Morty, do you know what "wubba lubba dub dub" means?')

    session_main.close()

    print('Fin.')
