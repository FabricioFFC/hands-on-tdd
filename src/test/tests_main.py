#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from main import app as my_app
import json
from mock import patch, MagicMock
from test_helpers.database_faker import DatabaseHelper

class TestMain(unittest.TestCase):

    def setUp(self):
        DatabaseHelper.clean_db()
        self.app = my_app.test_client()

    @patch('commands.get_customer_luck_numbers.DatabaseHelper', DatabaseHelper)
    def test_returns_pincode(self):
        # given
        data = {'cpf': '35818079805', 'pincode': '1q2w3e4r5t'}
        # when
        res = self.app.post('/receber_numero_da_sorte', data=data)
        # then
        self.assertEqual(res.status_code, 201)
        self.assertIn(data['pincode'], str(res.data))

    @patch('commands.get_customer_luck_numbers.DatabaseHelper', DatabaseHelper)
    def test_returns_error_when_pincode_already_exists(self):
        # given
        data = {'cpf': '35818079805', 'pincode': '1q2w3e4r5t'}
        expected_error = 'Pincode existe'
        # when
        self.app.post('/receber_numero_da_sorte', data=data)
        res = self.app.post('/receber_numero_da_sorte', data=data)
        data = json.loads(res.data)
        # then
        self.assertEqual(res.status_code, 400)
        self.assertEqual(expected_error, data['error'])

if __name__ == '__main__':
    unittest.main()
