# Actions

## General

### "test"

Will just print the given args and kwargs out
```
{
  "action":"test",
  "args:(),
  "kwargs:{}
}
```

### "set_variable"

Will add a variable
```
{
  "action":"set_variable",
  "args":(),
  "kwargs":{
    "name":"varname",
    "val":0.1234
  }
}
```

### "sleep"

Will wait
```
{
  "action":"sleep",
  "args":(3,),      #nb of seconds
  "kwargs":{}
}
```

### "hotkeys_click"

Will do a mouseclick
```
{
  "action":"hotkeys_click",
  "args":(),
  "kwargs":{
    "x":1000,         #optional but needs y if present
    "y":1000,         #optional but needs x if present
    "clicks":1,       #optional
    "button":"left",  #optional
    "interval":"0.1"  #optional
  }
}
```

### "hotkeys_hotkeys"

Presses keyboard keys
```
{
  "action":"hotkeys_hotkeys",
  "args":(("a","b"),),    #only one arg, which is a tuple containing the keys to press
  "kwargs":{
    "interval":0.1        #optional
  }
}
```
  

## OBS

Every obs request requires the first argument in args to be a filter to the websocket to use. The format is "?obsX" where X is the number of the socket in the config, starting with 1.

### "obs_call_request"

Calls a request from [obs-websocket](https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#requests)
```
{
  "action":"obs_call_request",
  "args":("?obsX","requestname"),
  "kwargs":{
    "key1": val1        #arguments defined by the request
  }
}
```

### "obs_set_profile"

Sets the obs profile
```
{
  "action":"obs_set_profile",
  "args":("?obsX",),
  "kwargs":{
    "profileName": profileName
  }
}
```

### "obs_set_scene_collection"

Sets the obs scene collection
```
{
  "action":"obs_set_scene_collection",
  "args":("?obsX",),
  "kwargs":{
    "sceneCollectionName": sceneCollectionName
  }
}
```

### "obs_set_scene_program"

Sets the obs scene currently active
```
{
  "action":"obs_set_scene_program",
  "args":("?obsX",),
  "kwargs":{
    "sceneName": sceneName
  }
}
```
  
### "obs_set_scene_preview"

Sets the obs scene currently in preview when in studio mode
```
{
  "action":"obs_set_scene_preview",
  "args":("?obsX",),
  "kwargs":{
    "sceneName": sceneName
  }
}
```
  
### "obs_set_transition"

Sets the transition to use when change the active scene
```
{
  "action":"obs_set_transition",
  "args":("?obsX",),
  "kwargs":{
    "transitionName": transitionName
  }
}
```

### "obs_set_transition_duration"

Sets the transition duration
```
{
  "action":"obs_set_transition_duration",
  "args":("?obsX",),
  "kwargs":{
    "transitionDuration": transitionDuration
  }
}
```

### "obs_toggle_virtual_cam"

Toggles the virtual cam on/off
```
{
  "action":"obs_toggle_virtual_cam",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_start_virtual_cam"

Starts the virtual cam
```
{
  "action":"obs_start_virtual_cam",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_stop_virtual_cam"

Stops the virtual cam
```
{
  "action":"obs_stop_virtual_cam",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_toggle_stream"

Toggles the stream on/off
```
{
  "action":"obs_toggle_stream",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_start_stream"

Starts the stream
```
{
  "action":"obs_start_stream",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_stop_stream"

Stops the stream
```
{
  "action":"obs_stop_stream",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_toggle_record"

Toggles the record on/off
```
{
  "action":"obs_toggle_record",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_start_record"

Starts the record
```
{
  "action":"obs_start_record",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_stop_record"

Stops the record
```
{
  "action":"obs_stop_record",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_toggle_record_pause"

Toggles the record play/pause
```
{
  "action":"obs_toggle_record_pause",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_pause_record"

Pauses the record
```
{
  "action":"obs_pause_record",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_resume_record"

Resumes the record
```
{
  "action":"obs_resume_record",
  "args":("?obsX",),
  "kwargs":{}
}
```

### "obs_studio_mode_transition"

Triggers the transition of preview to program when in studio mode
```
{
  "action":"obs_studio_mode_transition",
  "args":("?obsX",),
  "kwargs":{}
}
```
