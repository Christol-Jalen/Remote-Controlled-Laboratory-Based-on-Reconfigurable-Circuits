def _init(): #initialise
	global _global_dict
	_global_dict = {}

def set_value(key, value):
	#define a global variable
	_global_dict[key] = value 

def get_value(key):
	#get a global variable
	try:
		return _global_dict[key]
	except:
		print("fail to get the value")
