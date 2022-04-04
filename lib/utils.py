
VARIABLES = {}

def set_variable(*args, name = None, val = None, **kwargs):
	try:
		VARIABLES[name] = val
		return {
			"success":True,
			"data":{
				"name": name,
				"val": val
			}
		}
	except Exception as e:
		return {
			"success":False,
			"data":{
				"exception": str(e),
				"name": name,
				"val": val
			}
		}

def test(*args, **kwargs):
	return {
		"success":True,
		"data":{
			"args": args,
			"kwargs": kwargs
		}
	}