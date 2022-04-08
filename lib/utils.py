from time import sleep as timesleep

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

def sleep(*args, **kwargs):
	try:
		timesleep(args[0])
		return {
			"success":True,
			"data":{
				"sleeptime": args[0]
			}
		}
	except Exception as e:
		return {
			"success":False,
			"data":{
				"exception": str(e),
				"args": args
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