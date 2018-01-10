# -*- coding: utf-8 -*-
# pylint: skip-file
import unittest
import datetime
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from code import models


class ProductsTestCase(unittest.TestCase):
    def setUp(self):
        connection_uri = "postgresql://vagrant:vagrant@localhost:5432/demo"
        self.engine = create_engine(connection_uri)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def test_smooth_dinglepop_with_schleem(self):
        dinglepop = self.session.query(models.Dinglepop).first()
        self.assertIsNotNone(dinglepop)

        schleem = self.session.query(models.Schleem).filter_by(height=123, width=456).one_or_none()
        self.assertIsNotNone(schleem)

    def test_repurpose_schleem_for_later_batch(self):
        schleem = self.session.query(models.Schleem).filter_by(height=123, width=456).one_or_none()
        self.assertIsNotNone(schleem)

        schleem.batch = '123-zxcvb'
        self.session.commit()

    def test_rub_dinglepop_with_fleeb(self):
        dinglepop = self.session.query(models.Dinglepop).first()
        self.assertIsNotNone(dinglepop)

        fleeb = self.session.query(models.Fleeb).first()
        self.assertIsNotNone(fleeb)

    def test_cut_the_fleeb(self):
        fleeb = self.session.query(models.Fleeb).first()
        self.assertIsNotNone(fleeb)

    def test_rub_the_chumbles(self):
        chumble = self.session.query(models.Chumble)\
            .filter(models.Chumble.length == 21)\
            .filter(models.Chumble.diameter == 9)\
            .one()

        self.assertIsNotNone(chumble)

    def test_the_plumbus(self):
        plumbus = self.session.query(models.Plumbus).first()

        schleem = self.session.query(models.Schleem).filter_by(id=plumbus.schleem_id)
        self.assertIsNotNone(schleem)

        dinglepop = self.session.query(models.Dinglepop).filter_by(id=plumbus.dinglepop_id)
        self.assertIsNotNone(dinglepop)

        fleeb = self.session.query(models.Fleeb).filter_by(id=plumbus.fleeb_id)
        self.assertIsNotNone(fleeb)
        
        chumble = self.session.query(models.Chumble).filter_by(id=plumbus.chumble_id)
        self.assertIsNotNone(chumble)


    def tearDown(self):
        self.session.close()
  