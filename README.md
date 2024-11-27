# Overview

I created a small networking program for this project.
It is a server that can respond to a variety of requests from a client.
It responds with random jokes, quotes, or fortunes depending on the request.

To start the server:
```
python src/server.py
```

To start the client:
```
python src/client.py
```

I wrote this to learn about how networking works at a basic level.

[Software Demo Video](https://youtu.be/rURwORSJYF8)

# Network Communication

I used a client-server architecture for this project.
The server responds to TCP requests over port 2023.

Messages take a simple format.
A request can be sent with the format `REQUEST <type>`.
Each request should end with a newline (LF) to indicate that the message is over.

The server response is simply a single line of text.
It too ends with a newline (LF) to indicate the end of the message.

| Message Type   | Description                          |
| ---            | ---                                  |
| `BANNER`       | Returns a welcome message            |
| `GOODBYE`      | Returns a goodbye message            |
| `JOKE`         | Returns a random joke                |
| `FORTUNE`      | Returns a random fortune             |
| `QUOTE`        | Returns a random inspirational quote |

# Development Environment

I used standard python 3 for this project.
I only used standard libraries for this (socket and random).

# Useful Websites

* [Python Socket Documentation](https://docs.python.org/3/library/socket.html)
* [GeeksforGeeks](https://www.geeksforgeeks.org/socket-programming-python/)

# Future Work

* Add more jokes, fortunes, and quotes
* Add other request types
* Allow clients to post messages to a central message board
