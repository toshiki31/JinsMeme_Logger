#!/usr/bin/env python3
# reference: https://xp-cloud.jp/blog/2020/09/15/7564/
# pip install git+https://github.com/Pithikos/python-websocket-server

from websocket_server import WebsocketServer
import time
import json
import pprint

def start():
    # Connection event
    def new_client(client, server):
        print('New client {}:{} has joined.'.format(client['address'][0], client['address'][1]))
 
    # Disconnection event
    def client_left(client, server):
        print('Client {}:{} has left.'.format(client['address'][0], client['address'][1]))
 
    # Message receive event
    def message_received(client, server, message):
        # print(message)
        d = json.loads(message)
        # pprint.pprint(d, width=40)
	# currentData
        accX = d.get('accX')
        accY = d.get('accY')
        accZ = d.get('accZ')
        blinkSpeed = d.get('blinkSpeed')
        blinkStrength = d.get('blinkStrength')
        eyeMoveDown = d.get('eyeMoveDown')
        eyeMoveLeft = d.get('eyeMoveLeft')
        eyeMoveRight = d.get('eyeMoveRight')
        eyeMoveUp = d.get('eyeMoveUp')
        fitError = d.get('fitError')
        noiseStatus = d.get('noiseStatus')
        pitch = d.get('pitch')
        powerLeft = d.get('powerLeft')
        roll = d.get('roll')
        sequenceNumber = d.get('sequenceNumber')
        walking = d.get('walking')
        yaw = d.get('yaw')
        
        # debug
        print('accX:', accX, 'accY:', accY, 'accZ:', accZ)
        print('blinkSpeed:', blinkSpeed, 'blinkStrength:', blinkStrength)
        print('eyeMoveDown:', eyeMoveDown, 'eyeMoveLeft:', eyeMoveLeft, 'eyeMoveRight:', eyeMoveRight, 'eyeMoveLeft:', eyeMoveLeft, 'eyeMoveUp', eyeMoveUp)
        print('fitError:', fitError, 'noiseStatus:', noiseStatus)
        print('pitch:', pitch, 'roll:', roll, 'yaw:', yaw) 
        print('powerLeft:', powerLeft, 'sequenceNumber:', sequenceNumber, 'walking:', walking)

    # 5001番ポートでサーバーを立ち上げる
    server = WebsocketServer(port=5001, host='172.16.4.31')
    # イベントで使うメソッドの設定
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    # 実行
    server.run_forever()
 
if __name__ == "__main__":
    start()