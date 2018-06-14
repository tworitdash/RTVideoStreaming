#!/usr/bin/env python
import os
#from geopy.geocoders import Nominatim, GoogleV3
#from geopy.exc import GeocoderTimedOut
#import serial
import time 
import asyncio
import websockets
#import pynmea2
#from pynmea2 import ChecksumError
#from pynmea2 import ParseError

#ser =serial.Serial("/dev/tty.usbserial", 9600, timeout=1)

async def hello():
	async with websockets.connect('ws://localhost:8765') as websocket:
		while True:
			data = await concurrent()
			await websocket.send(str(data))
			print("> {}".format(data))
			greeting = await websocket.recv()
			print("< {}".format(data))
#def set_proxy():
#    proxy_addr = 'http://localhost:3128'
#    os.environ['http_proxy'] = proxy_addr
#    os.environ['https_proxy'] = proxy_addr

#def unset_proxy():
#    os.environ.pop('http_proxy')
#   os.environ.pop('https_proxy')

#async def retrieve():
	#data = ser.readline().decode()
	#data_to_be_sent = await concurrent()
	#return(data_to_be_sent)

async def concurrent():

    #ADD your pyshark code here and return something from this function! 


	


asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()
