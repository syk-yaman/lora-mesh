import pycom
import time
from mqtt import MQTTClient
# from mqtt import MQTTClient_lib as MQTTClient
from network import WLAN
import machine
import time
from _pymesh_config import PymeshConfig
from _pymesh import Pymesh


def sub_cb(topic, msg):
   print(msg)

def new_message_cb(rcv_ip, rcv_port, rcv_data):
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
wlan.connect("#########", auth=(WLAN.WPA2, "########"), timeout=5000)

while not wlan.isconnected():  
    machine.idle()
print("Connected to WiFi\n")

client = MQTTClient("Node-3", "#################",user=None, password=None, port=9001, keepalive=30, ssl=False, ssl_params={})

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