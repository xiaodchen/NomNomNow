"""Unit tests for charge api logic."""

import unittest
from mock import Mock # Note: need to pip install mock at python 2.7
import charge_with_retries_api

class TestChargeAPI(unittest.TestCase):
	def setUp(self):
		self.retryAmount = 3
		self.amount = 50

	def testAlwaysException(self):
		mock = Mock(side_effect=Exception('foo'))
		with self.assertRaises(Exception):
			charge_with_retries_api.ChargeWithRetries(self.amount, self.retryAmount, mock)

	def testFailedThreeTimes(self):
		mock = Mock()
		mock.side_effect = [Exception('foo'), Exception('foo'), Exception('foo'), 5]
		with self.assertRaises(Exception):
			charge_with_retries_api.ChargeWithRetries(self.amount, self.retryAmount, mock)

	def testFailedTwice(self):
		mock = Mock()
		mock.side_effect = [Exception('foo'), Exception('foo'), 5, 6]
		self.assertEqual(5, charge_with_retries_api.ChargeWithRetries(self.amount, self.retryAmount, mock))

	def testFailedOnce(self):
		mock = Mock()
		mock.side_effect = [Exception('foo'), 6, 5, 3]
		self.assertEqual(6, charge_with_retries_api.ChargeWithRetries(self.amount, self.retryAmount, mock))

	def testNoFail(self):
		mock = Mock()
		mock.side_effect = [6, 4, Exception('foo')]
		self.assertEqual(6, charge_with_retries_api.ChargeWithRetries(self.amount, self.retryAmount, mock))

if __name__ == '__main__':
  unittest.main()
