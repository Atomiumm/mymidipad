default_midi_input = 1

modules_to_import = ["obs"]

OBSserver_url = "ws://127.0.0.1:4444"
OBSserver_password = "password"

Actions_on_start = [
	{
		"action":"set_variable",
		"args":(),
		"kwargs":{
			"name":"test",
			"val":0.1234
		}
	},
	{
		"action":"hotkeys_hotkeys",
		"args":(("a","b"),),
		"kwargs":{"interval":"?test"}
	},
	{
		"action":"hotkeys_click",
		"args":(),
		"kwargs":{
			"x":1000,
			"y":1000,
			"clicks":1,
			"button":"right",
			"interval":"?test"
		}
	}
]

Actions_on_event = {
	(144,0) : {
		"ActionsGeneral":[],
		"ActionOnValue":[
			{
				"value":("?2",127),
				"actions":[]
			}
		],
		"ActionsIfInRange":[
			{
				"value":("?2",20,50),
				"actions":[]
			}
		]
	}
}