# -*- coding: utf-8 -*-
# pylint: skip-file
import unittest
import datetime
from uuid import uuid4
from code import models


class MaterialsTestCase(unittest.TestCase):
    def test_querying_schleems(self):

        shcleem = models.Schleem

        expected_value = None

        actual_value = None

        self.assertEqual(actual_value, expected_value)
