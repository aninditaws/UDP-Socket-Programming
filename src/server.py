import socket
import threading
from tkinter import *
from tkinter import scrolledtext

def start_server():
    while True:
        message, address = server.recvfrom(1024)
        message = message.decode('utf-8')
        clients.add(address)
        chat_log.insert(END, f"Client {address}: {message}\n")

        
        

def send_message():
    message = entry_message.get()
    chat_log.insert(END, "Server: " + message + "\n")
    for client in clients:
        server.sendto(message.encode('utf-8'), client)
    entry_message.delete(0, END)



server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 12345))

clients = set() 

window = Tk()
window.title("Server")

chat_log = scrolledtext.ScrolledText(window, width=50, height=10)
chat_log.grid(column=0, row=0, padx=10, pady=10)

entry_message = Entry(window, width=40)
entry_message.grid(column=0, row=1, padx=10, pady=10)

send_button = Button(window, text="Kirim", command=send_message)
send_button.grid(column=0, row=2, padx=10, pady=10)

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

window.mainloop()
