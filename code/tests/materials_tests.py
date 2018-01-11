# -*- coding: utf-8 -*-
# pylint: skip-file
import unittest
import datetime
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from code import models


class MaterialsTestCase(unittest.TestCase):
    def setUp(self):
        connection_uri = "postgresql://vagrant:vagrant@localhost:5432/demo"
        self.engine = create_engine(connection_uri)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def test_querying_schleems(self):
        schleems = self.session.query(models.Schleem).all()
        self.assertGreater(len(schleems), 0)

    def test_deleting_a_dinglepop(self):
        dinglepops_initial_count = self.session.query(models.Dinglepop).count()
        self.assertGreater(dinglepops_initial_count, 0)

        dinglepop = self.session.query(models.Dinglepop).filter_by(origin='Universe #48').one_or_none()
        self.assertIsNotNone(dinglepop)

        self.session.delete(dinglepop)

        dinglepops_new_count = self.session.query(models.Dinglepop).count()
        self.assertEqual((dinglepops_initial_count - 1), dinglepops_new_count)

        # Note that without committing the session these changes are not persisted to our database
        # self.session.commit()

    def test_adding_a_chumble(self):
        chumble_count = self.session.query(models.Chumble).count()
        self.assertGreater(chumble_count, 0)

        self.session.add(models.Chumble(
            id=uuid4(),
            length=123,
            diameter=99
        ))

        new_chumble_count = self.session.query(models.Chumble).count()
        self.assertGreater(new_chumble_count, chumble_count)

        # This time let's commit the session, so we can see the effect on the underlying database
        self.session.commit()

    def test_updating_the_fleeb(self):
        fleeb = self.session.query(models.Fleeb).one_or_none()

        fleeb.organic = True

        # Apply the update, sqlalchemy has generated this from the change to the record we just made
        self.session.commit() 

    def test_requesting_one_record_when_many_exist_raises_an_exception(self):
        with self.assertRaises(Exception):
            chumble = self.session.query(models.Chumble).one_or_none()

    def test_one_or_none_exception_message(self):
        try:
            chumble = self.session.query(models.Chumble).one_or_none()
            self.assertFail()

        except Exception as ex:
            self.assertEqual(str(ex), 'Multiple rows were found for one_or_none()')
  
    def test_executing_sql(self):
        sql = "SELECT * FROM dinglepop"

        # without fetching the data we will have a ResultProxy that can be accessed via 'yield per' (helps with data at scale)
        # watchout for empty sets of data when doing this though as error messages are vague in these instances
        dinglepops = self.session.execute(sql).fetchall()

        self.assertGreater(len(dinglepops), 0)

    def test_scalar(self):
        sql = "SELECT COUNT(*) FROM dinglepop"

        dinglepop_count = self.session.scalar(sql)

        self.assertGreater(dinglepop_count, 0)


    def tearDown(self):
        self.session.close()
  