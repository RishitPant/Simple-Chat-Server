import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12321

server.bind(('127.0.0.1', port))
server.listen()

client_names = []
clients = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client.index(client)
            clients.remove(client)
            client.close()
            name = client_names[index]
            broadcast(f"{client_name} left the chat!".encode('ascii'))
            client_names.remove(name)
            break


def recieve():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")
        
        client.send('NICK'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        client_names.append(name)
        client_names.append(client)

        print(f"Name of the client is {name}")
        broadcast(f"{name} joined the chat!".encode("ascii"))
        client.send("Connected to the Noob Coder's Server!".encode("ascii"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("SERVER STARTED...")
recieve()
