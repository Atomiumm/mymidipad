from config import OBSserver_urls, OBSserver_passwords
import simpleobsws
import asyncio
#https://github.com/obsproject/obs-websocket/blob/4.x-current/docs/generated/protocol.md
#https://github.com/IRLToolkit/simpleobsws
loop = asyncio.get_event_loop()
obsws = []
for i in range(len(OBSserver_urls)):
	obsws.append(simpleobsws.WebSocketClient(url=OBSserver_urls[i], password=OBSserver_passwords[i]))
	print("Connecting to obs websocket: ", end="", flush=True)
	print(loop.run_until_complete(obsws[i].connect()))
	print("Waiting until identified to obs websocket: ", end="", flush=True)
	print(loop.run_until_complete(obsws[i].wait_until_identified(timeout = 30)))

def obs_call_request(obsws, request, *args, **kwargs):
	r = loop.run_until_complete(obsws.call(simpleobsws.Request(request, kwargs)))
	if not r.requestStatus.result:
		return {
			"success":False,
			"data":{
				"exception": r.requestStatus.comment,
				"kwargs": kwargs
			}
		}
	return {
		"success":True,
		"data":{
			"data": r.responseData,
			"kwargs": kwargs
		}
	}

def obs_set_profile(obsws, *args, **kwargs):
	if "profileName" not in kwargs:
		return {
			"success":False,
			"data":{
				"exception": "profileName not in kwargs",
				"kwargs": kwargs
			}
		}
	return obs_call_request(obsws, "SetCurrentProfile", **kwargs)	

def obs_set_scene_collection(obsws, *args, **kwargs):
	if "sceneCollectionName" not in kwargs:
		return {
			"success":False,
			"data":{
				"exception": "sceneCollectionName not in kwargs",
				"kwargs": kwargs
			}
		}
	return obs_call_request(obsws, "SetCurrentSceneCollection", **kwargs)

def obs_set_scene_program(obsws, *args, **kwargs):
	if "sceneName" not in kwargs:
		return {
			"success":False,
			"data":{
				"exception": "sceneName not in kwargs",
				"kwargs": kwargs
			}
		}
	return obs_call_request(obsws, "SetCurrentProgramScene", **kwargs)

def obs_set_scene_preview(obsws, *args, **kwargs):
	if "sceneName" not in kwargs:
		return {
			"success":False,
			"data":{
				"exception": "sceneName not in kwargs",
				"kwargs": kwargs
			}
		}
	return obs_call_request(obsws, "SetCurrentPreviewScene", **kwargs)

def obs_set_transition(obsws, *args, **kwargs):
	if "transitionName" not in kwargs:
		return {
			"success":False,
			"data":{
				"exception": "transitionName not in kwargs",
				"kwargs": kwargs
			}
		}
	return obs_call_request(obsws, "SetCurrentSceneTransition", **kwargs)

def obs_set_transition_duration(obsws, *args, **kwargs):
	if "transitionDuration" not in kwargs:
		return {
			"success":False,
			"data":{
				"exception": "transitionDuration not in kwargs",
				"kwargs": kwargs
			}
		}
	return obs_call_request(obsws, "SetCurrentSceneTransitionDuration", **kwargs)

def obs_toggle_virtual_cam(obsws, *args, **kwargs):
	return obs_call_request(obsws, "ToggleVirtualCam")

def obs_start_virtual_cam(obsws, *args, **kwargs):
	return obs_call_request(obsws, "StartVirtualCam")

def obs_stop_virtual_cam(obsws, *args, **kwargs):
	return obs_call_request(obsws, "StopVirtualCam")

def obs_toggle_stream(obsws, *args, **kwargs):
	return obs_call_request(obsws, "ToggleStream")

def obs_start_stream(obsws, *args, **kwargs):
	return obs_call_request(obsws, "StartStream")

def obs_stop_stream(obsws, *args, **kwargs):
	return obs_call_request(obsws, "StopStream")

def obs_toggle_record(obsws, *args, **kwargs):
	return obs_call_request(obsws, "ToggleRecord")

def obs_start_record(obsws, *args, **kwargs):
	return obs_call_request(obsws, "StartRecord")

def obs_stop_record(obsws, *args, **kwargs):
	return obs_call_request(obsws, "StopRecord")

def obs_toggle_record_pause(obsws, *args, **kwargs):
	return obs_call_request(obsws, "ToggleRecordPause")

def obs_pause_record(obsws, *args, **kwargs):
	return obs_call_request(obsws, "PauseRecord")

def obs_resume_record(obsws, *args, **kwargs):
	return obs_call_request(obsws, "ResumeRecord")

def obs_studio_mode_on(obsws, *args, **kwargs):
	return obs_call_request(obsws, "SetStudioModeEnabled", {"studioModeEnabled":True})

def obs_studio_mode_off(obsws, *args, **kwargs):
	return obs_call_request(obsws, "SetStudioModeEnabled", {"studioModeEnabled":False})

def obs_studio_mode_toggle(obsws, *args, **kwargs):
	r = loop.run_until_complete(obsws.call(simpleobsws.Request("GetStudioModeEnabled")))
	if not r.requestStatus.result:
		return {
			"success":False,
			"data":{
				"exception": f"couldn't get studio mode info, {r.requestStatus.comment}"
			}
		}
	return obs_studio_mode_off(obsws) if r.responseData["studioModeEnabled"] else obs_studio_mode_on(obsws)

def obs_studio_mode_transition(obsws, *args, **kwargs):
	return obs_call_request(obsws, "TriggerStudioModeTransition")
