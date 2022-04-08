# mymidipad  

Some python that allows easy config and use of midi pads with multiple functionalities.  
THIS IS NOT WORKING YET. IT IS STILL IN DEVELOPMENT. WILL HAVE A FIRST WORKING VERSION IN A FEW DAYS

---
## Dependencies  

Depend on the modules you might like to run.  
In any case:  
> pip install pygame, pyautogui, requests

If you want to use the obs module:  
> pip install simpleobsws  

## How to run

Just download the project and execute the __main__.py file like this:  
> $ cd *path to where the project was put*
> $ python mymidipad  

---
## Config file

You can modify the config file to make your pad do what you want.  
If you aren't sure how your pad works, just run a config file without any actions and look at what the program displays when you press a button.  
* **default_midi_input** allows you to define a default midi device. If you don't set any, the program will ask you to choose among all the inputs it sees.  
* **Actions_on_start** contains all actions that will be executed automatically when the program starts.  
* **Actions_on_event** contains all actions that can be executed when using the pad.  
* **modules_to_import** contains strings for each module you might want to import and run.  
    * **"obs"** will allow you to use an obs websocket  
        * **OBSserver_urls** urls to the obs websockets. For example: ["ws://127.0.0.1:4455", "ws://127.0.0.1:4456"]
        * **OBSserver_password** passwords to the obs websockets.  

### Actions

Each action has a standard model:
```
{
  "action":"action_name",
  "args":(arg1, arg2),
  "kwargs":{key1:val1, key2:val2}
}
```  

### Actions_on_event

The keys of this dict are tuples, corresponding to the first values of the midi data. You can define any number of values, 1 or 100, maybe even 0 if you want it to be triggered no matter the event. Every time a midi event happens, the program will check if the first values of the event correspond to the key and trigger it if they are the same.  
The value corresponding to this key is a dict containing three optional keys:  
* "ActionsGeneral" maps to a list of actions that will be executed.
* "ActionOnValue" maps to a dict with two keys:
    * "value" maps to a tuple containing 2 values. The actions will be executed only if the two values are the same.
    * "actions" maps to a list of actions to be executed.
* "ActionsIfInRange" maps to a dict with two keys:
    * "value" maps to a tuple containing 3 values. The actions will be executed only if the first value is greater or equal to the second one and strictly lesser than the third one.
    * "actions" maps to a list of actions to be executed.

### Filtering

A possible action is the **set_variable** action, which defines a variable that can be used somewhere else in the config.  
From then on, instead of setting a value, you can set "?varname", which will be replaced by the value specified. You can change a variable by re-setting it.
Additionally, you can take a value of the midi data, starting from index 0. For example, "?2" will take the 3rd value of the midi data.  
Finally, you can use the midi_timestamp with "?timestamp"  

---

## Actions

[link to list of actions](actions.md)
  
