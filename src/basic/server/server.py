#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import numpy as np
from pickle import dumps, loads

async def inverseMatrix(websocket, path):

    buffer_matrix = await websocket.recv()
    matrix = loads(buffer_matrix)
    print("Receiving matrix:\n", matrix)

    inverse = np.linalg.inv(matrix)

    buffer_inverse = dumps(inverse)
    await websocket.send(buffer_inverse)
    print("Sending inverse:\n", inverse)

start_server = websockets.serve(inverseMatrix, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()