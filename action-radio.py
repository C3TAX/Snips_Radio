# ! / usr / bin / env python3
# - * - Kodierung: utf-8 - * -

import configparser
aus hermes_python.hermes importiere Hermes
aus hermes_python.ffi.utils importieren Sie MqttOptions
aus hermes_python.ontology importieren  *
io importieren
import subprocess

CONFIGURATION_ENCODING_FORMAT  =  " utf-8 "
CONFIG_INI  =  " config.ini "

Klasse  SnipsConfigParser ( configparser . SafeConfigParser ):
    def  to_dict ( self ):
        return {section: {option_name: option für option_name, option in  self .items (section)} für section in  self .sections ()}


def  read_configuration_file ( configuration_file ):
    versuche :
        mit io.open (configuration_file, encoding = CONFIGURATION_ENCODING_FORMAT ) als f:
            conf_parser = SnipsConfigParser ()
            conf_parser.readfp (f)
            return conf_parser.to_dict ()
    außer ( IOError , configparser.Error) als e:
        return  dict ()
        
 
     subprocess.call("mpc clear", shell=True)
    subprocess.call("mpc load " + conf['secret']['radio_playlist'], shell=True)

    subprocess.call("mpc play", shell=True)

def msg_play ( hermes , intentMessage ):
    conf = read_configuration_file ( CONFIG_INI )

    subprocess.call("mpc clear", shell=True)
    subprocess.call("mpc load " + conf['secret']['radio_playlist'], shell=True))

    subprocess.call("mpc play", shell=True)
    result_sentence =  "Radio an "

    current_session_id = intentMessage.session_id
    hermes.publish_end_session (current_session_id, result_sentence)

if  __name__  ==  " __main__ " :
    mqtt_opts = MqttOptions ()
    mit Hermes ( mqtt_options = mqtt_opts) als h:
        h.subscribe_intent ( "cetax:play" , msg_play)
        h.start ()
