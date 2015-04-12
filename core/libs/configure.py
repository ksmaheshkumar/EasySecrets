#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

# CONFIGURATION FILE STUFF

import os
import ConfigParser


# In house default config
config = {}
config["proxymode"] = "False" #os.path.dirname(__file__) + '/core/config/.es.config' #Folder where config information will be kept.
# Go to this path to remove wanted items.
config_file_path = os.path.dirname(__file__) + '/core/config/.es.config'
config_section = "PROXY"

# Read the configuration file and discard the items the user wants.
def read_config(config_file_path, config_dict):
  configparser = ConfigParser.RawConfigParser()
  configparser.read(config_file_path)
  for key, previous_value in config_dict.items():
    if configparser.has_option(config_section, key):
      new_value = configparser.get(config_section, key).decode('utf-8')
      if type(previous_value) in (list, bool):
        new_value = json.loads(new_value)
      config_dict[key] = new_value

# Save any new items to the config file
def save_config(config_file_path, config_dict):
  configparser = ConfigParser.RawConfigParser()
  configparser.add_section(config_section)
  for key, value in config_dict.items():
    if type(value) in (list, bool):
      value = json.dumps(value)
    configparser.set(config_section, key, value.encode('utf-8'))

  config_file_folder = os.path.dirname(config_file_path)
  if not os.path.exists(config_file_folder) :
    os.makedirs(config_file_folder)
  with open(config_file_path, 'w') as configfile:
    configparser.write(configfile)

# Instantiation of config file.
read_config(config_file_path, config)
save_config(config_file_path, config)
