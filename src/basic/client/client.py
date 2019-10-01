#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import numpy as np
from pickle import dumps, loads

matrix = np.array([[1,1,1],[0,2,5],[2,5,-1]]) 

async def sendMatrix():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        
        buffer_matrix = dumps(matrix)

        await websocket.send(buffer_matrix)
        print("Sending matrix:\n", matrix)

        buffer_inverse = await websocket.recv()
        inverse = loads(buffer_inverse)
        print("Receiving its inverse:\n", inverse)

asyncio.get_event_loop().run_until_complete(sendMatrix())