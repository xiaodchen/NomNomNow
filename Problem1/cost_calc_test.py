"""Unit tests for cost calc logic."""

import unittest
import cost_calc
import models

class TestCostCalc(unittest.TestCase):

	def testDeliveryCadence(self):	
		self.assertEquals(cost_calc.DELIVERY_CADENCE_MEALS['weekly'], 14)
		self.assertEquals(
			cost_calc.DELIVERY_CADENCE_MEALS['monthly'],
			cost_calc.DELIVERY_CADENCE_MEALS['weekly'] * 4)

	def testCaloriesPerMeal(self): 
		dog = models.Dog("Test Recipe", 30)
		self.assertEquals(cost_calc.GetCaloriesPerMeal(dog), 462)

	def testGetShippingCost(self):
		# assuming package_weight is float input
		# assuming 0 package_weight would return 0 

		#0 -> 5 lbs cost = 10 + 5/5 * 1.5 = 11.5
		self.assertEquals(cost_calc.GetShippingCost(0), 0)
		#0.5 -> 5 lbs cost = 10 + 5/5 * 1.5 = 11.5
		self.assertEquals(cost_calc.GetShippingCost(0.5), 11.5)		
		#4 -> 5 lbs cost = 10 + 5/5 * 1.5 = 11.5
		self.assertEquals(cost_calc.GetShippingCost(4), 11.5)
		#4.5 -> 5 lbs cost = 10 + 5/5 * 1.5 = 11.5
		self.assertEquals(cost_calc.GetShippingCost(4.5), 11.5)
		#9.5 -> 10 lbs cost = 10 + 10/5 * 1.5 = 13
		self.assertEquals(cost_calc.GetShippingCost(9.5), 13)
		#10 -> 10 lbs cost = 10 + 10/5 * 1.5 = 13
		self.assertEquals(cost_calc.GetShippingCost(10), 13)
		#10.1 -> 15 lbs cost = 10 + 15/5 * 1.5 = 14.5
		self.assertEquals(cost_calc.GetShippingCost(10.1), 14.5)
		#27 -> 30 lbs cost = 10 + 30/5 * 1.5 = 19
		self.assertEquals(cost_calc.GetShippingCost(27), 19)
		#30 -> 30 lbs cost = 10 + 30/5 * 1.5 = 19
		self.assertEquals(cost_calc.GetShippingCost(30), 19)
		#35 -> 40 lbs cost = 10 + 30/5 * 1.5 + 10/10 * 2.6 = 21.6
		self.assertEquals(cost_calc.GetShippingCost(35), 21.6)
		#41.111111 -> 50 lbs cost = 10 + 30/5 * 1.5 + 20/10 * 2.6 = 24.2
		self.assertEquals(cost_calc.GetShippingCost(41.111111), 24.2)
		#100 -> 100 lbs cost = 10 + 30/5 * 1.5 + 70/10 * 2.6 = 37.2
		self.assertEquals(cost_calc.GetShippingCost(100), 37.2)
		#1000000005 -> 1000000010 lbs cost = 10 + 30/5 * 1.5 + (1000000010-30)/10 * 2.6 = 37.2
		self.assertEquals(cost_calc.GetShippingCost(1000000005), 260000013.8)

	def testGetTotalCost(self):
		dog1 = models.Dog("chicken", 30)
		dog2 = models.Dog("pork", 126.555)
		customer = models.Customer('weekly')
		customer.AddDog(dog1)
		customer.AddDog(dog2)
		# dog1: chicken, 30 lbs dog weight, weekly 
		# 			int(29 * 30 * 0.453592 ** 0.8) / 590 * 1.49 * 14 = 16.3344
		# dog2: pork, 126 lbs dog weight, weekly
		# 			int(29 * 126 * 0.453592 ** 0.8) / 500 * 1.25 * 14 = 67.9467
		# totalcost: 84.269 + 0.12 * 14 * 2 + 29.4 = 117.03
		self.assertEquals(cost_calc.GetTotalCost(customer), 117.03)
		dog1 = models.Dog("chicken", 32)
		dog2 = models.Dog("pork", 50)
		customer = models.Customer('monthly')
		customer.AddDog(dog1)
		customer.AddDog(dog2)
		# dog1: chicken, 32 lbs dog weight, weekly 
		# 			int(29 * 32 * 0.453592 ** 0.8) / float(590) * 1.49 * 56
		# dog2: pork, 50 lbs dog weight, weekly
		# 			int(29 * 50 * 0.453592 ** 0.8) / float(500) * 1.25 * 56
		# totalcost:  177.522 + 0.12 * 56 * 2 + 47.6 = 238.56
		self.assertEquals(cost_calc.GetTotalCost(customer), 238.56)

	def testUnknownRecipes(self):
		dog1 = models.Dog("Beef", 30)
		dog2 = models.Dog("Unknown", 126.555)
		customer = models.Customer('weekly')
		customer.AddDog(dog1)
		customer.AddDog(dog2)
		with self.assertRaises(Exception):
			self.assertEquals(cost_calc.GetTotalCost(customer), 117.03)

	def testUnknownDeliveryCadence(self):
		dog1 = models.Dog("chicken", 32)
		dog2 = models.Dog("pork", 50)
		customer = models.Customer('foo')
		customer.AddDog(dog1)
		customer.AddDog(dog2)
		with self.assertRaises(Exception):
			self.assertEquals(cost_calc.GetTotalCost(customer), 117.03)

if __name__ == '__main__':
  unittest.main()
