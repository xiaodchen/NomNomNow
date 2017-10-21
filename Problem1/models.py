"""Data models to represent customers and dogs."""
# TODO comments require action.


class Dog(object):
  """Class representing a single dog."""

  def __init__(self, recipe, weight):
    """Initialization values for a dog.

    Args:
      recipe: String recipe.
      weight: Interger pounds current weight of the dog.
    """
    self.recipe = recipe
    self.weight = int(weight)


class Customer(object):
  """Class representing a customer."""

  def __init__(self, delivery_cadence):
    """Initializes a customer with a delivery_cadence and empty list of dogs.

    Args:
      delivery_cadence: String "weekly" or "monthly" delivery cadence.
    """
    self.delivery_cadence = delivery_cadence
    self._dogs = []

  def AddDog(self, dog):
    """Adds a dog to the customer.

    Args:
      dog: Instance of a Dog.
    """
    # TODO: TO BE IMPLEMENTED
    self._dogs.append(dog)

  def ListDogs(self):
    """Gets a list of all dogs belonging to the customer.

    Returns:
      List of customer's dog instances.
    """
    # TODO: TO BE IMPLEMENTED
    return self._dogs
