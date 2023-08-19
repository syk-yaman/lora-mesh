import pycom
import time
from mqtt import MQTTClient
# from mqtt import MQTTClient_lib as MQTTClient
from network import WLAN
import machine
import time
from _pymesh_config import PymeshConfig
from _pymesh import Pymesh
import config

from machine import I2C

def sub_cb(topic, msg):
   print(msg)

def send_mqtt_message():
    while not wlan.isconnected():  
        machine.idle()
    print("Connected to WiFi\n")

    client = MQTTClient(config.MQTT_ID, config.MQTT_BROKER,user= config.MQTT_USER, password= config.MQTT_PASSWORD, port= config.MQTT_PORT, keepalive=30, ssl=False, ssl_params={})

    client.set_callback(sub_cb)

    time.sleep(5)
    client.connect()
    client.subscribe(topic="yaman/feeds/test")
    print("Recieved from mesh")
    client.publish(topic="yaman/feeds/test", msg="Recieved")

def new_message_cb(rcv_ip, rcv_port, rcv_data):
    send_mqtt_message()
    ''' callback triggered when a new packet arrived '''
    print('Incoming %d bytes from %s (port %d):' %
            (len(rcv_data), rcv_ip, rcv_port))
    print(rcv_data)

    # user code to be inserted, to send packet to the designated Mesh-external interface
    for _ in range(3):
        pycom.rgbled(0x888888)
        time.sleep(.2)
        pycom.rgbled(0)
        time.sleep(.1)
    return

def ReadLightSensor():
    i2c = I2C(0)
    i2c = I2C(0, I2C.MASTER) 
    i2c.init(I2C.MASTER, baudrate=20000)
    lightI2C = i2c.readfrom_mem(0x23, 0x10, 2)
    lightConverted = lightI2C[0] << 8 | lightI2C[1]
    lightValue = lightConverted / 1.2
    i2c.deinit() 
    return lightValue


pycom.heartbeat(False)

# read config file, or set default values
pymesh_config = PymeshConfig.read_config()
pymesh = Pymesh(pymesh_config, new_message_cb)
#initialize Pymesh

# mac = pymesh.mac()
# if mac > 10:
#     pymesh.end_device(True)
# elif mac == 5:
#     pymesh.leader_priority(255)

while not pymesh.is_connected():
    print(pymesh.status_str())
    time.sleep(3)

# send message to the Node having MAC address 5
pymesh.send_mess(5, "Hello World")

# def new_br_message_cb(rcv_ip, rcv_port, rcv_data, dest_ip, dest_port):
#     ''' callback triggered when a new packet arrived for the current Border Router,
#     having destination an IP which is external from Mesh '''
#     print('Incoming %d bytes from %s (port %d), to external IPv6 %s (port %d)' %
#             (len(rcv_data), rcv_ip, rcv_port, dest_ip, dest_port))
#     print(rcv_data)

#     # user code to be inserted, to send packet to the designated Mesh-external interface
#     # ...
#     return

# add current node as Border Router, with a priority and a message handler callback
# pymesh.br_set(PymeshConfig.BR_PRIORITY_NORM, new_br_message_cb)

# remove Border Router function from current node
# pymesh.br_remove()

# send data for Mesh-external, basically to the BR
# ip = "1:2:3::4"
# port = 5555
# pymesh.send_mess_external(ip, port, "Hello World")

print("done Pymesh init, CLI is started, h - help/command list, stop - CLI will be stopped")
#pymesh.cli_start()

# while True:
#     time.sleep(3)


wlan = WLAN(mode=WLAN.STA)
wlan.connect(config.WIFI_SSID, auth=(WLAN.WPA2, config.WIFI_PASSWORD), timeout=5000)

while not wlan.isconnected():  
    machine.idle()
print("Connected to WiFi\n")

client = MQTTClient(config.MQTT_ID, config.MQTT_BROKER,user= config.MQTT_USER, password= config.MQTT_PASSWORD, port= config.MQTT_PORT, keepalive=30, ssl=False, ssl_params={})

client.set_callback(sub_cb)

time.sleep(10)
client.connect()
client.subscribe(topic="yaman/feeds/test")


while True:
    print("Sending ON")
    client.publish(topic="yaman/feeds/test", msg="ON")
    time.sleep(1)
    print("Sending OFF")
    client.publish(topic="yaman/feeds/test", msg="OFF")
    client.check_msg()

    time.sleep(1)