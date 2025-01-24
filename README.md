# Chatting Application Based on UDP Socket Programming

A Python-based chat application utilizing **UDP Socket Programming** with a **Tkinter GUI** for real-time communication between a server and multiple clients. It supports lightweight messaging, multi-client connections, threading for non-blocking I/O, and message broadcasting.

## Features
- **UDP Protocol** for fast, lightweight communication.
- **Multi-client Support** for simultaneous messaging.
- **Graphical User Interface (GUI)** built with `Tkinter`.
- **Threaded Operations** to maintain a responsive interface.
- **Message Broadcasting** by the server to all connected clients.

## Requirements
- Python 3.6 or later
- Required libraries:
  - `socket`
  - `threading`
  - `tkinter`

## How to Use
### Running the Server
1. Run `server.py`.
2. The server GUI will open, displaying message logs and providing an input box for messages.

### Running the Client
1. Run `client.py`.
2. Enter a unique port number for the client connection.
3. The client GUI will open, allowing messages to be sent and received.

## How It Works
1. The server listens for client messages and broadcasts responses to all connected clients.
2. Each client sends messages to the server and receives broadcasts.
3. Threading ensures smooth GUI operation without blocking network tasks.

## Testing Scenarios
1. **Single Client Interaction**:
   - A client sends a message to the server, and the server replies.
2. **Multiple Client Interaction**:
   - Multiple clients connect, send messages, and receive broadcasts.

## File Structure
- `server.py`: Manages server operations, client connections, and message broadcasting.
- `client.py`: Handles client connections, sending messages, and receiving broadcasts.

## References
- [GeeksforGeeks: UDP Client-Server using CONNECT](https://www.geeksforgeeks.org/udp-client-server-using-connect-c-implementation/)
- Hamonangan Situmorang, Diktat Kuliah Pemrograman Berorientasi Objek, Edunex ITB.
