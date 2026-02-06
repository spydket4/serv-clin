import socket
import time

HOST = "0.0.0.0"
PORT = 13337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        
        # Отправляем приветственное сообщение клиенту
        conn.sendall(b"Welcome to echo server! Type 'exit' to quit.\n")
        
        counter = 1
        while True:
            try:
                # Получаем данные от клиента
                data = conn.recv(1024)
                if not data:
                    break
                    
                client_msg = data.decode('utf-8').strip()
                print(f"Received: {client_msg}")
                
                # Если клиент отправил "exit", завершаем соединение
                if client_msg.lower() == "exit":
                    conn.sendall(b"Goodbye!\n")
                    break
                
                # Эхо-ответ клиенту
                response = f"Echo [{counter}]: {client_msg}\n"
                conn.sendall(response.encode('utf-8'))
                
                counter += 1
                
            except (ConnectionResetError, ConnectionAbortedError):
                print("Connection lost")
                break
            except socket.timeout:
                # Таймаут приема, продолжаем цикл
                continue

print("Connection closed")