#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from mock import patch, MagicMock
from commands.get_customer_luck_numbers import GetCustomerLuckNumbersCommand
from test_helpers.database_faker import DatabaseHelper
class TestGetCustomerLuckNumbersCommand(unittest.TestCase):
    def test_return_invalid_cpf_when_cpf_is_invalid(self):
        # given
        invalid_cpf = '111'
        pincode = '1a2s3d4f5g'
        expected_error = 'CPF inválido'
        # when
        result = GetCustomerLuckNumbersCommand.call(invalid_cpf, pincode)
        # then
        self.assertEqual(result['error'], expected_error)
    def test_return_invalid_pincode_when_pincode_is_invalid(self):
        # given
        cpf = '35818079805'
        invalid_pincode = '1a2s3d4f5'
        expected_error = 'Pincode inválido'
        # when
        result = GetCustomerLuckNumbersCommand.call(cpf, invalid_pincode)
        # then
        self.assertEqual(result['error'], expected_error)
    @patch('commands.get_customer_luck_numbers.DatabaseHelper', DatabaseHelper)
    def test_return_pincode_when_cpf_and_pincode_are_valid(self):
        # given
        cpf = '35818079805'
        pincode = '1a2s3d4f5g'
        # when
        saved_pincode = GetCustomerLuckNumbersCommand.call(cpf, pincode)
        # then
        self.assertEqual(saved_pincode, pincode)

if __name__ == '__main__':
    unittest.main()
