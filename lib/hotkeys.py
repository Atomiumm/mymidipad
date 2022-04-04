import pyautogui

def click(*args, **kwargs):
	try:
		if "interval" not in kwargs:
			kwargs["interval"] = 0.1
		pyautogui.click(**kwargs)
		return {
			"success":True,
			"data":{
				"clicks": kwargs["clicks"] if "clicks" in kwargs.keys() else 1,
				"pos": pyautogui.position(),
				"interval":kwargs["interval"],
				"button": kwargs["button"] if "button" in kwargs.keys() else "left"
			}
		}
	except Exception as e:
		return {
			"success":False,
			"data":{
				"exception":str(e),
				"kwargs":kwargs
			}
		}

def hotkeys(keys, *args, **kwargs):
	try:
		if "interval" not in kwargs:
			kwargs["interval"] = 0.01
		pyautogui.hotkey(*keys, **kwargs)
		return {
			"success":True,
			"data":{
				"keys": keys,
				"interval":kwargs["interval"]
			}
		}
	except Exception as e:
		return {
			"success":False,
			"data":{
				"exception":str(e),
				"keys":keys,
				"kwargs":kwargs
			}
		}