#!/usr/bin/python3
# 
# SPDX-License-Identifier: MIT
#
######################################
#
# Copyright 2022 John 'Warthog9' Hawley
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

######################################

import serial
from datetime import datetime
import json
from pprint import pprint

import paho.mqtt.client as mqtt
import logging
import socket
import sys

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

mqtt_username = config['config']['mqtt_username']
mqtt_password = config['config']['mqtt_password']
mqtt_host = config['config']['mqtt_host']
# config file format:
# [config]
# mqtt_username = <username>
# mqtt_password = <password>
# mqtt_host = <host>

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

def mqtt_connect(client, userdata, flags, rc):
    """Callback for MQTT connects."""

    logging.info("MQTT connected: " + mqtt.connack_string(rc))
    if rc != 0:
        logging.error("Could not connect. Error: " + str(rc))
    else:
        logging.info("Subscribing to: " + args.rtl_topic)
        client.subscribe(args.rtl_topic)


def mqtt_disconnect(client, userdata, rc):
    """Callback for MQTT disconnects."""
    logging.info("MQTT disconnected: " + mqtt.connack_string(rc))

def getHassDevice():
    global hostname
    return '"device": { "manufacturer": "Banggood AQI", "identifiers": "banggood-aqi-'+ str(hostname) +'", "name": "banggood-'+ str(hostname) +'", "model": "1" }'

hostname = socket.gethostname()

mqttc = mqtt.Client("{}".format( hostname ))
mqttc.username_pw_set( mqtt_username, mqtt_password )
try:
    mqttc.connect( mqtt_host, 1883 )
except:
    print("Failed to connect")
    sys.exit()

# publish the config sections for HASS
# cpm2.5 - Chinese Particles per Million < 2.5 micron
# cpm1.0 - Chinese Particles per Million < 1.0 micron
# cpm10  - Chinese Particles per Million < 10 micron
# apm2.5 - American Particles per Million < 2.5 micron
# apm1.0 - American Particles per Million < 1.0 micron
# apm10  - American Particles per Million < 10 micron
# aqi    - Calculated AQI
# t      - Temperature Celsius
# r      - Relative Humidity %
#
mqttc.publish(
                "homeassistant/sensor/{}/cpm25/config".format( hostname ),
                '{ '\
                + '"name": "cpm2.5", '\
                + '"device_class": "pm25", '\
                + '"unit_of_measurement": "µg/m³" ,'\
                + '"value_template": "{{ value|float }}", '\
                + '"state_class": "measurement", '\
                + '"state_topic": "homeassistant/sensor/'+ hostname +'/cpm25/state", '\
                + '"unique_id": "aqi-'+ hostname +'-cpm25", '\
                + getHassDevice() \
                + ' }'
            )  # publish
mqttc.publish(
                "homeassistant/sensor/{}/cpm1/config".format( hostname ),
                '{ '\
                + '"name": "cpm1.0", '\
                + '"device_class": "pm1", '\
                + '"unit_of_measurement": "µg/m³" ,'\
                + '"value_template": "{{ value|float }}", '\
                + '"state_class": "measurement", '\
                + '"state_topic": "homeassistant/sensor/'+ hostname +'/cpm1/state", '\
                + '"unique_id": "aqi-'+ hostname +'-cpm1", '\
                + getHassDevice() \
                + ' }'
            )  # publish
mqttc.publish(
                "homeassistant/sensor/{}/cpm10/config".format( hostname ),
                '{ '\
                + '"name": "cpm10", '\
                + '"device_class": "pm10", '\
                + '"unit_of_measurement": "µg/m³" ,'\
                + '"value_template": "{{ value|float }}", '\
                + '"state_class": "measurement", '\
                + '"state_topic": "homeassistant/sensor/'+ hostname +'/cpm10/state", '\
                + '"unique_id": "aqi-'+ hostname +'-cpm10", '\
                + getHassDevice() \
                + ' }'
            )  # publish
mqttc.publish(
                "homeassistant/sensor/{}/apm25/config".format( hostname ),
                '{ '\
                + '"name": "apm2.5", '\
                + '"device_class": "pm25", '\
                + '"unit_of_measurement": "µg/m³" ,'\
                + '"value_template": "{{ value|float }}", '\
                + '"state_class": "measurement", '\
                + '"state_topic": "homeassistant/sensor/'+ hostname +'/apm25/state", '\
                + '"unique_id": "aqi-'+ hostname +'-apm25", '\
                + getHassDevice() \
                + ' }'
            )  # publish
mqttc.publish(
                "homeassistant/sensor/{}/apm1/config".format( hostname ),
                '{ '\
                + '"name": "apm1.0", '\
                + '"device_class": "pm1", '\
                + '"unit_of_measurement": "µg/m³" ,'\
                + '"value_template": "{{ value|float }}", '\
                + '"state_class": "measurement", '\
                + '"state_topic": "homeassistant/sensor/'+ hostname +'/apm1/state", '\
                + '"unique_id": "aqi-'+ hostname +'-apm1", '\
                + getHassDevice() \
                + ' }'
            )  # publish
mqttc.publish(
                "homeassistant/sensor/{}/apm10/config".format( hostname ),
                '{ '\
                + '"name": "apm10", '\
                + '"device_class": "pm10", '\
                + '"unit_of_measurement": "µg/m³" ,'\
                + '"value_template": "{{ value|float }}", '\
                + '"state_class": "measurement", '\
                + '"state_topic": "homeassistant/sensor/'+ hostname +'/apm10/state", '\
                + '"unique_id": "aqi-'+ hostname +'-apm10", '\
                + getHassDevice() \
                + ' }'
            )  # publish
mqttc.publish(
                "homeassistant/sensor/{}/aqi/config".format( hostname ),
                '{ '\
                + '"name": "aqi", '\
                + '"device_class": "aqi", '\
                + '"value_template": "{{ value|float }}", '\
                + '"state_class": "measurement", '\
                + '"state_topic": "homeassistant/sensor/'+ hostname +'/aqi/state", '\
                + '"unique_id": "aqi-'+ hostname +'-aqi", '\
                + getHassDevice() \
                + ' }'
            )  # publish
mqttc.publish(
                "homeassistant/sensor/{}/temperature/config".format( hostname ),
                '{ '\
                + '"name": "temperature", '\
                + '"device_class": "temperature", '\
                + '"unit_of_measurement": "°C" ,'\
                + '"value_template": "{{ value|float }}", '\
                + '"state_class": "measurement", '\
                + '"state_topic": "homeassistant/sensor/'+ hostname +'/temperature/state", '\
                + '"unique_id": "aqi-'+ hostname +'-temperature", '\
                + getHassDevice() \
                + ' }'
            )  # publish
mqttc.publish(
                "homeassistant/sensor/{}/humidity/config".format( hostname ),
                '{ '\
                + '"name": "humidity", '\
                + '"device_class": "temperature", '\
                + '"unit_of_measurement": "%" ,'\
                + '"value_template": "{{ value|float }}", '\
                + '"state_class": "measurement", '\
                + '"state_topic": "homeassistant/sensor/'+ hostname +'/humidity/state", '\
                + '"unique_id": "aqi-'+ hostname +'-humidity", '\
                + getHassDevice() \
                + ' }'
            )  # publish

ser = serial.Serial(
        '/dev/ttyUSB0',
        115200
        )  # open serial port
print(ser.name)         # check which port was really used

now = datetime.now()
str_now = now.strftime("%y-%m-%d %H:%M:%S")

print( "str_now: {}".format( str_now ) )

ser.write(
        bytes(
            "{\"fun\":\"03\",\"clock\":\""+ str_now +"\"}}",
            "UTF-8"
            )
        )

ser.write(b"{\"fun\":\"05\",\"flag\":\"1\"}")     # write a string

found_start = False
data = ""

while True:
    c = ser.read().decode("utf-8")
    #print( c )
    if c == "{":
        found_start = True
        data = ""
    if found_start:
        data += c
    if c == "}":
        found_start = False
        isValidJSON = validateJSON( data )
        if isValidJSON:
            jdata = json.loads( data )
            if jdata['res'] == "4":
                #{"res":"4","y":"2022","m":"09","d":"11","h":"22","min":"30","sec":"16","cpm2.5":"0001","cpm1.0":"0001","cpm10":"0001","apm2.5":"0001","apm1.0":"0001","apm10":"0001","aqi":"001","t":"20.6","r":"52"}
                # res    - what type of response is this
                # y      - full year
                # m      - full month
                # d      - full day
                # h      - full hour
                # min    - full minute
                # sec    - full second
                # cpm2.5 - Chinese Particles per Million < 2.5 micron
                # cpm1.0 - Chinese Particles per Million < 1.0 micron
                # cpm10  - Chinese Particles per Million < 10 micron
                # apm2.5 - American Particles per Million < 2.5 micron
                # apm1.0 - American Particles per Million < 1.0 micron
                # apm10  - American Particles per Million < 10 micron
                # aqi    - Calculated AQI
                # t      - Temperature Celsius
                # r      - Relative Humidity %
                #
                mqttc.publish(
                        "aqi/{}/cpm25".format(hostname),
                        jdata['cpm2.5']
                        )
                mqttc.publish(
                        "homeassistant/sensor/{}/cpm25/state".format(hostname),
                        int(jdata['cpm2.5'])
                        )
                mqttc.publish(
                        "aqi/{}/cpm1".format(hostname),
                        int(jdata['cpm1.0'])
                        )
                mqttc.publish(
                        "homeassistant/sensor/{}/cpm1/state".format(hostname),
                        int(jdata['cpm1.0'])
                        )
                mqttc.publish(
                        "aqi/{}/cpm10".format(hostname),
                        int(jdata['cpm10'])
                        )
                mqttc.publish(
                        "homeassistant/sensor/{}/cpm10/state".format(hostname),
                        int(jdata['cpm10'])
                        )
                mqttc.publish(
                        "aqi/{}/apm25".format(hostname),
                        int(jdata['apm2.5'])
                        )
                mqttc.publish(
                        "homeassistant/sensor/{}/apm25/state".format(hostname),
                        int(jdata['apm2.5'])
                        )
                mqttc.publish(
                        "aqi/{}/apm1".format(hostname),
                        int(jdata['apm1.0'])
                        )
                mqttc.publish(
                        "homeassistant/sensor/{}/apm1/state".format(hostname),
                        int(jdata['apm1.0'])
                        )
                mqttc.publish(
                        "aqi/{}/apm10".format(hostname),
                        int(jdata['apm10'])
                        )
                mqttc.publish(
                        "homeassistant/sensor/{}/apm10/state".format(hostname),
                        int(jdata['apm10'])
                        )
                mqttc.publish(
                        "aqi/{}/aqi".format(hostname),
                        int(jdata['aqi'])
                        )
                mqttc.publish(
                        "homeassistant/sensor/{}/aqi/state".format(hostname),
                        int(jdata['aqi'])
                        )
                mqttc.publish(
                        "aqi/{}/temperature".format(hostname),
                        float(jdata['t'])
                        )
                mqttc.publish(
                        "homeassistant/sensor/{}/temperature/state".format(hostname),
                        float(jdata['t'])
                        )
                mqttc.publish(
                        "aqi/{}/humidity".format(hostname),
                        float(jdata['r'])
                        )
                mqttc.publish(
                        "homeassistant/sensor/{}/humidity/state".format(hostname),
                        float(jdata['r'])
                        )

ser.close()             # close port
