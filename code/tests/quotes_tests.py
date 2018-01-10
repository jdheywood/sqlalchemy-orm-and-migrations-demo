# -*- coding: utf-8 -*-
# pylint: skip-file
import unittest
import datetime
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from code import models


class QuotesTestCase(unittest.TestCase):
    def setUp(self):
        connection_uri = "postgresql://vagrant:vagrant@localhost:5432/demo"
        self.engine = create_engine(connection_uri)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def test_number_of_quotes(self):
        quote_count = self.session.query(models.Quote).count()
        self.assertEqual(quote_count, 5)


    def tearDown(self):
        self.session.close()
  