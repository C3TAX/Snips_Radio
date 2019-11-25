#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import io
import websockets
from websocket import create_connection

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, configparser.Error) as e:
        return dict()


def msg_play(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    
    subprocess.call("mpc clear", shell=True)
    subprocess.call("mpc load " + conf['secret']['radio_playlist'], shell=True))
    subprocess.call("mpc play", shell=True)
    result_sentence =  "Radio an "

    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, result_sentence)


def msg_stop (hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)

    subprocess.call("mpc stop", shell=True)
    result_sentence =  "Radio aus "

    current_session_id = intentMessage.session_id
    hermes.publish_end_session (current_session_id, result_sentence)
    
if  __name__  ==  " __main__ " :
    mqtt_opts = MqttOptions ()
    mit Hermes ( mqtt_options = mqtt_opts) als h:
        h.subscribe_intent("cetax:play", msg_play)
        h.subscribe_intent("cetax:play", msg_stop)
        h.start()
