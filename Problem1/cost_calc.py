"""Library to calculate costs and issue charge."""
# TODO comments require action.
# Other files of interest: models.py, cost_calc_test.py
from models import Dog, Customer

# Cost per pound by recipe.
RECIPE_COST_PER_POUND = {
  'pork': 1.25,
  'chicken': 1.49,
}

# Calories per pound by recipe.
CALORIES_PER_POUND = {
  'pork': 500,
  'chicken': 590,
}

# Number meals per delivery cadence. Assumes 2 meals per day.
# Weekly means a week of food in one delivery.
# Monthly means 4 weeks of food in one delivery.
DELIVERY_CADENCE_MEALS = {
  'weekly': 14,
  'monthly': 56
}

# Labor cost in USD to package a single meal.
LABOR_COST_PER_MEAL = 0.12

# Conversion from kilograms to pounds.
KILOGRAMS_IN_A_POUND = 0.453592


def GetCaloriesPerMeal(dog):
  """Calculates the calories per meal required.

  Args:
    dog: Dog instance.

  Returns:
    Integer calories required per meal for the dog.
  """
  # Formula for calories per meal is:
  # 29 * (dog weight * KILOGRAMS_IN_A_POUND)**0.8
  # TODO: TO BE IMPLEMENTED
  calories = int(29 * dog.weight * KILOGRAMS_IN_A_POUND ** 0.8)
  return calories

def GetShippingCost(package_weight):
  """Calculates shipping cost.
  Args:
    package_weight: Float lbs package weight.

  Returns:
    Float USD shipping cost.
  """
  # Assume base shipping cost of $10.
  # Add $1.5 cost for every 5 lbs up to 30 lbs.
  # If package is over 30 lbs, add $2.60 cost for every 10 lbs beyond 30 lbs.
  # Weight should always be rounded up to the next shipping cost price point.
  # For example, an 11 lb package should be considered 15 lbs for shipping cost.
  # TODO: TO BE IMPLEMENTED
  if not package_weight: return 0
  price = 0
  # Add $1.5 cost for every 5 lbs up to 30 lbs.
  if package_weight <= 30: 
    if package_weight % 5: 
      package_weight = (package_weight // 5 + 1) * 5
    price = 10 + 1.5 * package_weight / 5.0
  # If package is over 30 lbs, add $2.60 cost for every 10 lbs beyond 30 lbs.
  else:
    if package_weight % 10: 
      package_weight = (package_weight // 10 + 1) * 10
    price = 10 + 1.5 * 30 / 5.0 + 2.6 * (package_weight - 30) / 10.0
  return price


def GetTotalCost(customer):
  """Calculates total cost for a single delivery.

  Args:
    customer: models.Customer instance with a delivery cadence and dogs set.

  Returns:
    Float USD cost for a delivery of dog food.
  """
  # Total cost should be the sum of costs for food + labor + shipping
  # based on the customer's delivery cadence and dog(s) properties.
  # TODO: TO BE IMPLEMENTED
  foodCost, laborCost, shippingCost = 0, 0, 0
  recipeCostForAllDogs, foodWeightForAllDogs = 0, 0
  if customer.delivery_cadence not in DELIVERY_CADENCE_MEALS:
    raise Exception('unknown delivery cadence {}'.format(customer.delivery_cadence))
  numberOfMealsPerDeliveryCadence = DELIVERY_CADENCE_MEALS.get(customer.delivery_cadence, 0)

  dogs = customer.ListDogs()
  for dog in dogs: 
    dogRecipe = dog.recipe 
    if dogRecipe not in CALORIES_PER_POUND:
      raise Exception('unknown recipe type {} for CALORIES_PER_POUND'.format(dogRecipe))
    if dogRecipe not in RECIPE_COST_PER_POUND:
      raise Exception('unknown recipe type {} for RECIPE_COST_PER_POUND'.format(dogRecipe))
    # calories per meal based on dogs weight
    caloriesPerMeal = GetCaloriesPerMeal(dog)
    # food weight based on calories per meal
    foodWeight = float(caloriesPerMeal) / CALORIES_PER_POUND.get(dogRecipe, 0)
    # recipe cost based on food weight 
    recipeCost = foodWeight * RECIPE_COST_PER_POUND.get(dogRecipe, 0)
    recipeCostForAllDogs += recipeCost 
    foodWeightForAllDogs += foodWeight
  
  foodCost = recipeCostForAllDogs * numberOfMealsPerDeliveryCadence
  laborCost = LABOR_COST_PER_MEAL * numberOfMealsPerDeliveryCadence * len(dogs)
  shippingCost = GetShippingCost(foodWeightForAllDogs * numberOfMealsPerDeliveryCadence)

  totalCost = foodCost + laborCost + shippingCost
  #rounding to 2 decimals 
  totalCost = round(totalCost,2)
  return totalCost 
