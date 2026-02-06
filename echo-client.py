import socket

HOST = "10.90.14.78"  # Замените на IP сервера
PORT = 13337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Устанавливаем таймаут для сокета
    s.settimeout(5.0)
    
    # Получаем приветственное сообщение от сервера
    try:
        welcome_msg = s.recv(1024)
        print(welcome_msg.decode('utf-8'), end='')
    except socket.timeout:
        print("No welcome message received")
    
    while True:
        try:
            # Пользователь вводит сообщение
            user_input = input("You: ")
            
            # Отправляем сообщение серверу
            s.sendall(user_input.encode('utf-8'))
            
            # Получаем ответ от сервера
            data = s.recv(1024)
            if data:
                print(f"Server: {data.decode('utf-8')}", end='')
            else:
                print("Server disconnected")
                break
            
            # Если пользователь ввел "exit", выходим
            if user_input.lower() == "exit":
                break
                
        except socket.timeout:
            print("Connection timeout")
            break
        except ConnectionResetError:
            print("Server disconnected")
            break
        except KeyboardInterrupt:
            print("\nInterrupted by user")
            s.sendall(b"exit")
            break

print("Disconnected from server")