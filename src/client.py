import socket
import threading
from tkinter import *
from tkinter import scrolledtext

def receive_message():
    while True:
        try:
            # Perubahan di sini: menggunakan recvfrom untuk UDP
            message, _ = client.recvfrom(1024)
            message = message.decode('utf-8')
            chat_log.insert(END, "Server: " + message + "\n")
        except Exception as e:
            print("Error receiving message: ", e)
            break

def send_message():
    message = entry_message.get()
    chat_log.insert(END, "Client: " + message + "\n")
    client.sendto(message.encode('utf-8'), server_address)
    entry_message.delete(0, END)


# Initialize client socket
server_address = ('127.0.0.1', 12345) 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('127.0.0.1', int(input("enter port: "))))

window = Tk()
window.title("Client")

chat_log = scrolledtext.ScrolledText(window, width=50, height=10)
chat_log.grid(column=0, row=0, padx=10, pady=10)

entry_message = Entry(window, width=40)
entry_message.grid(column=0, row=1, padx=10, pady=10)

send_button = Button(window, text="Kirim", command=send_message)
send_button.grid(column=0, row=2, padx=10, pady=10)

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

window.mainloop()