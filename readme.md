## Python Websockets and numpy

This example a matrix to a server using Websocket, the server replies with the inverse matrix.

Pickle  methods *loads* and *dumps* are used to serialize numpy array through the socket.

The Matrix:
```
[[ 1  1  1]
 [ 0  2  5]
 [ 2  5 -1]]
```

and its inverse:
```
[[ 1.28571429 -0.28571429 -0.14285714]
 [-0.47619048  0.14285714  0.23809524]
 [ 0.19047619  0.14285714 -0.0952381 ]]
```


### Requirements and installation

Install websockets, numpy

```
pip install websockets numpy
```

### Run 

Running server, it will listen to port TCP 8765

```
python src/basic/server/server.py
```

Then run the client

```
python src/basic/client/client.py 
```

#### Results: 

Server side

```
Receiving matrix:
 [[ 1  1  1]
 [ 0  2  5]
 [ 2  5 -1]]
Sending inverse:
 [[ 1.28571429 -0.28571429 -0.14285714]
 [-0.47619048  0.14285714  0.23809524]
 [ 0.19047619  0.14285714 -0.0952381 ]]
```

Client side 

```
Sending matrix:
 [[ 1  1  1]
 [ 0  2  5]
 [ 2  5 -1]]
Receiving its inverse:
 [[ 1.28571429 -0.28571429 -0.14285714]
 [-0.47619048  0.14285714  0.23809524]
 [ 0.19047619  0.14285714 -0.0952381 ]]
```

### References

[Websockets Getting started](https://websockets.readthedocs.io/en/stable/intro.html)

[Inverse Matrix with Numpy](https://www.tutorialspoint.com/numpy/numpy_inv.htm)

[serialize numpy array with pickle](https://stackoverflow.com/questions/26377023/send-a-multidimensional-numpy-array-over-a-socket/26379564#26379564)

### Copyright

Free use!