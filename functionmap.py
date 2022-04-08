import lib
#add requests
#add obs mediainputs
#add spotify

functions = {
	"obs_call_request": lib.obs.obs_call_request,
	"obs_set_profile": lib.obs.obs_set_profile,
	"obs_set_scene_collection": lib.obs.obs_set_scene_collection,
	"obs_set_scene_program": lib.obs.obs_set_scene_program,
	"obs_set_scene_preview": lib.obs.obs_set_scene_preview,
	"obs_set_transition": lib.obs.obs_set_transition,
	"obs_set_transition_duration": lib.obs.obs_set_transition_duration,
	"obs_toggle_virtual_cam": lib.obs.obs_toggle_virtual_cam,
	"obs_start_virtual_cam": lib.obs.obs_start_virtual_cam,
	"obs_stop_virtual_cam": lib.obs.obs_stop_virtual_cam,
	"obs_toggle_stream": lib.obs.obs_toggle_stream,
	"obs_start_stream": lib.obs.obs_start_stream,
	"obs_stop_stream": lib.obs.obs_stop_stream,
	"obs_toggle_record": lib.obs.obs_toggle_record,
	"obs_start_record": lib.obs.obs_start_record,
	"obs_stop_record": lib.obs.obs_stop_record,
	"obs_toggle_record_pause": lib.obs.obs_toggle_record_pause,
	"obs_pause_record": lib.obs.obs_pause_record,
	"obs_resume_record": lib.obs.obs_resume_record,
	#"obs_studio_mode_on": lib.obs.obs_studio_mode_on,
	#"obs_studio_mode_off": lib.obs.obs_studio_mode_off,
	#"obs_studio_mode_toggle": lib.obs.obs_studio_mode_toggle,
	"obs_studio_mode_transition": lib.obs.obs_studio_mode_transition,

	"hotkeys_click": lib.hotkeys.click,
	"hotkeys_hotkeys": lib.hotkeys.hotkeys,
	"set_variable": lib.utils.set_variable,
	"sleep": lib.utils.sleep,
	"test": lib.utils.test
}