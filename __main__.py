#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
os.system("cls")
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from config import *
if "obs" in modules_to_import:
	from lib.obs import obsws
from functionmap import functions
from lib.utils import VARIABLES
import pygame.midi as midi
from time import sleep

def connect_midi_pad(midi_input = default_midi_input):
	midi.init()
	while True:
		try:
			midi_pad = midi.Input(int(midi_input), 1024)
			print(f"Connected to midi device {midi_input}")
			return midi_pad
		except Exception as e:
			print(f"Connection to midi device {midi_input} failed. Error: {e}")
			print("Choose a device (num)")
			for i in range(midi.get_count()):
				info = midi.get_device_info(i)
				print(i, info)
			midi_input = input("->")

def filter(midi_data, timestamp, obj):
	if type(obj) == str:
		if obj.startswith("?"):
			try:
				if obj == "?timestamp":
					return timestamp
				if obj[1:].isdigit():
					return midi_data[int(obj[1:])]
				if obj.startswith("?obs"):
					return obsws[int(obj[4:])-1]
				if obj[1:] in VARIABLES:
					return VARIABLES[obj[1:]]
			except:
				pass
		return obj
	elif type(obj) == dict:
		newobj = {}
		for k,v in obj.items():
			newobj[filter(midi_data, timestamp, k)] = filter(midi_data, timestamp, v)
		return newobj
	elif type(obj) == list or type(obj) == tuple:
		newobj = []
		for v in obj:
			newobj.append(filter(midi_data, timestamp, v))
		return type(obj)(newobj)
	return obj

def execute_action(action):
	print("executing:", action)
	try:
		print(functions[action["action"]](*action["args"], **action["kwargs"]))
	except Exception as e:
		print(f"couldn't execute: {e}")
		
def midi_pad_poll(midi_pad):
	while True:
		while midi_pad.poll():
			midi_data, timestamp = tuple(midi_pad.read(1)[0])
			sleep(0.1)
			while midi_pad.poll():
				midi_data, timestamp = tuple(midi_pad.read(1)[0])
			print(midi_data, timestamp)
			for i in range(len(midi_data)):
				if tuple(midi_data[:i]) in Actions_on_event:
					to_execute = filter(midi_data, timestamp, Actions_on_event[tuple(midi_data[:i])])
					if "ActionsGeneral" in to_execute:
						for action in to_execute["ActionsGeneral"]:
							execute_action(action)
					if "ActionsOnValue" in to_execute:
						for valuecheck in to_execute["ActionsOnValue"]:
							if valuecheck["value"][0] == valuecheck["value"][1]:
								for action in valuecheck["actions"]:
									execute_action(action)
					if "ActionsIfInRange" in to_execute:
						for valuecheck in to_execute["ActionsIfInRange"]:
							if valuecheck["value"][0] >= valuecheck["value"][1] and valuecheck["value"][0] < valuecheck["value"][2]:
								for action in valuecheck["actions"]:
									execute_action(action)





if __name__ == "__main__":
	midi_pad = connect_midi_pad()
	for action in Actions_on_start:
		execute_action(filter([], 0, action))
	midi_pad_poll(midi_pad)
