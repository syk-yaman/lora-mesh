from network import LoRa
import socket, time, pycom
red=0x7f0000; orange=0xff5100; yellow=0x7f5100; green=0x007f00; cyan=0x007f7f; blue=0x00007f; magenta=0x7f007f; off=0x000000; white=0x7f7f7f

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False); lora.sf(12); pycom.heartbeat(False)
pycom.rgbled(green)

while 1:
    if s.recv(64)==b'Ping': 
      print(lora.stats())
      pycom.rgbled(red)
      time.sleep(1)
      pycom.rgbled(green)
    else: time.sleep(1)