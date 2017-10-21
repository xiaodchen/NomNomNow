 # Assume a total cost is now calculated and we want to charge the amount. 
 # A mock charge API is provided by payment_api.py. 
 # However, the charge attempt may sometimes fail when the API is called.

import payment_api

def ChargeWithRetries(amount, maxRetryAttempts, paymentApi=None): 

	"""
	Write a new function called ChargeWithRetries that accepts an amount to charge and max retry attempts as parameters. 
	This new function should call payment_api.Charge and, if necessary, retry up to the max retry attempts.

	"""
	for n in range(maxRetryAttempts): 
		try:  
			paymentApi = paymentApi or payment_api.Charge
			return paymentApi(amount)
		except: 
			print 'Failed {0}th time.'.format(n)  
	raise Exception('Exceeded the number of tries: {0}'.format(maxRetryAttempts))
 
