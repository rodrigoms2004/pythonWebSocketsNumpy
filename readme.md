## Python Websockets and numpy

The example sends via websocket the matrix below to a server.
Pickle  methods *loads* and *dumps* are used to serialize numpy array through the socket.


```
[[ 1  1  1]
 [ 0  2  5]
 [ 2  5 -1]]
```

and receives its inverse

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