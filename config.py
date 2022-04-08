default_midi_input = 1

modules_to_import = ["obs"]

OBSserver_urls = ["ws://127.0.0.1:4455"]
OBSserver_passwords = ["password"]

Actions_on_start = [
	{
		"action":"obs_set_profile",
		"args":("?obs1",),
		"kwargs":{
			"profileName":"Untitled"
		}
	},
	{
		"action":"obs_set_scene_collection",
		"args":("?obs1",),
		"kwargs":{
			"sceneCollectionName":"Untitled"
		}
	}
]

Actions_on_event = {
	(999,999) : {
		"ActionsGeneral":[],
		"ActionsOnValue":[
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
	},
	tuple() : {"ActionsGeneral":[{"action":"test","args":tuple(),"kwargs":{}}]},
	(154,8) : {
		"ActionsGeneral":[
			{
				"action":"obs_set_scene_preview",
				"args":("?obs1",),
				"kwargs":{"sceneName":"Scene Display 1"}
			}
		]
	},
	(154,9) : {
		"ActionsGeneral":[
			{
				"action":"obs_set_scene_preview",
				"args":("?obs1",),
				"kwargs":{"sceneName":"Scene Display 2"}
			}
		]
	},
	(154,10) : {
		"ActionsGeneral":[
			{
				"action":"obs_set_scene_preview",
				"args":("?obs1",),
				"kwargs":{"sceneName":"Scene Display 3"}
			}
		]
	},
	(154,16) : {
		"ActionsGeneral":[
			{
				"action":"obs_studio_mode_transition",
				"args":("?obs1",),
				"kwargs":{}
			}
		]
	},
	(154,22) : {
		"ActionsGeneral":[
			{
				"action":"obs_toggle_stream",
				"args":("?obs1",),
				"kwargs":{}
			}
		]
	},
	(154,23) : {
		"ActionsGeneral":[
			{
				"action":"obs_toggle_record",
				"args":("?obs1",),
				"kwargs":{}
			}
		]
	},
	(186,9) : {
		"ActionsGeneral":[
			{
				"action":"obs_set_transition_duration",
				"args":("?obs1",),
				"kwargs":{"transitionDuration":"?2"}
			}
		],
		"ActionsOnValue":[
			{
				"value":("?2",0),
				"actions":[
					{
						"action":"obs_set_transition",
						"args":("?obs1",),
						"kwargs":{"transitionName":"Cut"}
					}
				]
			}
		],
		"ActionsIfInRange":[
			{
				"value":("?2",1,128),
				"actions":[
					{
						"action":"obs_set_transition",
						"args":("?obs1",),
						"kwargs":{"transitionName":"Fade"}
					}
				]
			}
		]
	}
}