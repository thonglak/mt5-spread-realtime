import socket
import threading
import time
import random

# สร้างลิสต์เพื่อเก็บ client sockets ที่เชื่อมต่อ
clients = []

def client_handler(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message.decode('utf-8') == 'ready':
                print("Client is ready")
                
            if message.decode('utf-8') == 'close_profit':
                print("command close_profit")
                for client in clients:
                    client.sendall("close_profit".encode('utf-8'))
                    
            if message.decode('utf-8') == 'close':
                print("command close all")
                for client in clients:
                    client.sendall("close".encode('utf-8'))
                    
            
                    
            if message.decode('utf-8') == 'start':
                print("command start")
                for client in clients:
                    client.sendall("start".encode('utf-8'))
                    
            if message.decode('utf-8') == 'buy':
                print("command buy")
                for client in clients:
                    client.sendall("buy".encode('utf-8'))
                    
            if message.decode('utf-8') == 'sell':
                print("command sell")
                for client in clients:
                    client.sendall("sell".encode('utf-8'))
                    
            if message.decode('utf-8') == 'run':
                print("command run")
                for client in clients:
                    client.sendall("run".encode('utf-8'))
                
                
                    
        except:
            clients.remove(client_socket)
            client_socket.close()
            break






def broadcast_start_command():
    for client in clients:
        client.sendall("start".encode('utf-8'))

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 6789))
    server_socket.listen()

    print("Server listening for connections...")
    while True:
        client_socket, _ = server_socket.accept()
        clients.append(client_socket)
        threading.Thread(target=client_handler, args=(client_socket,)).start()

        # ตัวอย่าง: สั่งให้ทุก clients เริ่มทำงานเมื่อมี 3 clients เชื่อมต่อ
        #if len(clients) == 3:
            #broadcast_start_command()

if __name__ == "__main__":
    server()