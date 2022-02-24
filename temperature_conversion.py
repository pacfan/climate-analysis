"""
A module for converting temperature in Fahrenheit to Celsius and Kelvin.

Functions:
	fahr_to_cels - returns the temperature in Celcius from Fahrenheit
	fahr_to_kelv - returns the temperature in Kelvin from Fahrenheit 
	...
"""

def fahr_to_cels(fahr):
	"""
        Convert temperature in Fahrenheit to Celsius
	
	:param fahr: float
	:returns: cels, float   	
	"""

	cels = (fahr + 32) * (5 / 9)
	return cels

def fahr_to_kelv(fahr):
    	"""
	Convert temperature in Fahrenheit to Kelvin
    
	:param fahr: fahr
	:returns: kelv, float
	"""

	cels = fahr_to_cels(fahr)
    	kelv = cels + 273.15
   	return kelv
