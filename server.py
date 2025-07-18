import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9999))

server.listen()

client, addr = server.accept()

state = False

while not state:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        state = True
    print(msg)
    client.send(input("Message: ").encode('utf-8')

client.close()
server.close()
