#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 16:11
# @Author  : eason.han
# @Email   : hanclong@hotmail.com
# @File    : websocket_scrapy.py
# @Software: PyCharm
import asyncio
import json
import logging
import random
from datetime import datetime
import websockets
import random_string
import load_mainpage
import asyncio
import websockets
import websocket
from aiowebsocket.converses import AioWebSocket
content = ['pid-7805:', 'pid-7802:', 'pid-7800:', 'pid-7806:', 'pid-7808:', 'pid-7801:', 'pid-7803:',
                   'pid-7810:', 'pid-7804:', 'pid-7809:', 'pid-7812:', 'pid-7811:', 'pid-7813:', 'pid-7807:',
                   'pid-7814:', 'pid-40820:', 'pid-28930:', 'pid-179:', 'pid-178:', 'pid-1175152:', 'pid-1175153:',
                   'pid-8827:', 'pid-6408:', 'pid-6369:', 'pid-243:', 'pid-267:', 'pid-7888:', 'pid-284:', 'pid-352:',
                   'pidTechSumm-6408:', 'pidTechSumm-6369:', 'pidTechSumm-243:', 'pidTechSumm-267:',
                   'pidTechSumm-7888:', 'pidTechSumm-284:', 'pidTechSumm-352:', 'isOpenExch-54:', 'isOpenExch-21:',
                   'isOpenExch-20:', 'isOpenPair-1175152:', 'isOpenPair-1175153:', 'isOpenPair-8827:', 'domain-6:']
def start(url):
    ws = websocket.create_connection(url,timeout=10)
    content = "{\"_event\":\"bulk-subscribe\",\"tzID\":28,\"message\":\"pid-6408:%%pid-6369:%%pid-243:%%pid-267:%%pid-7888:%%pid-284:%%pid-352:%%pidTechSumm-6408:%%pidTechSumm-6369:%%pidTechSumm-243:%%pidTechSumm-267:%%pidTechSumm-7888:%%pidTechSumm-284:%%pidTechSumm-352:%%pid-7805:%%pid-7802:%%pid-7800:%%pid-7806:%%pid-7808:%%pid-7801:%%pid-7803:%%pid-7810:%%pid-7804:%%pid-7809:%%pid-7812:%%pid-7811:%%pid-7813:%%pid-7807:%%pid-7814:%%pid-40820:%%pid-28930:%%pid-179:%%pid-178:%%pid-1175152:%%pid-1175153:%%pid-8827:%%isOpenExch-54:%%isOpenExch-21:%%isOpenExch-20:%%isOpenPair-1175152:%%isOpenPair-1175153:%%isOpenPair-8827:%%domain-6:\"}"
    ws.send(content)
    ws.send("{\"_event\":\"UID\",\"UID\":0}")
    while True:
        recv = ws.recv()
        print(recv)
        if recv =="o":
            ws.send(json.dumps(content))
            ws.send("{\"_event\":\"UID\",\"UID\":0}")

async def startup(uri):
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    }
    async with websockets.connect(uri, extra_headers=headers) as websocket:
        content = ['pid-7805:', 'pid-7802:', 'pid-7800:', 'pid-7806:', 'pid-7808:', 'pid-7801:', 'pid-7803:',
                   'pid-7810:', 'pid-7804:', 'pid-7809:', 'pid-7812:', 'pid-7811:', 'pid-7813:', 'pid-7807:',
                   'pid-7814:', 'pid-40820:', 'pid-28930:', 'pid-179:', 'pid-178:', 'pid-1175152:', 'pid-1175153:',
                   'pid-8827:', 'pid-6408:', 'pid-6369:', 'pid-243:', 'pid-267:', 'pid-7888:', 'pid-284:', 'pid-352:',
                   'pidTechSumm-6408:', 'pidTechSumm-6369:', 'pidTechSumm-243:', 'pidTechSumm-267:',
                   'pidTechSumm-7888:', 'pidTechSumm-284:', 'pidTechSumm-352:', 'isOpenExch-54:', 'isOpenExch-21:',
                   'isOpenExch-20:', 'isOpenPair-1175152:', 'isOpenPair-1175153:', 'isOpenPair-8827:', 'domain-6:']
        await websocket.send(json.dumps(content))
        while True:
            recv = await websocket.recv_data_frame()
            print(recv)
            if recv == "o":
                await websocket.send(json.dumps(content))


uri = f"wss://{load_mainpage.get_netloc()}/echo/{int(random.random() * 1000)}/{random_string.random_str()}/websocket"
start(uri)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(startup(uri))

