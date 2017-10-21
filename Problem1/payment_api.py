# Use this mock API as-is for charging an amount.
# No code in this file should be changed.

import random


class Error(Exception):
  """Base exception class."""


class ChargeFailedError(Error):
  """Raised when a charge fails for whatever reason. Who knows? Not me."""
  

def Charge(amount):
  """Attempts to charge an amount.

  Args:
    amount: Float USD amount to be charged.

  Returns:
    Float USD amount if charge attempt succeeded.

  Raises:
    ChargeFailedError: Raised if charge attempt fails.
  """
  if random.randint(0, 3):
    raise ChargeFailedError('Charge attempt failed.')

  return amount




