import socket

def main():
    print("🚀 Redis server starting on port 6379...")

    server_socket = socket.create_server(("localhost", 6379))
    connection, _ = server_socket.accept()
    print("✅ Client connected!")

    while True:
        data = connection.recv(1024)

        if not data:
            print("❌ Client disconnected.")
            break

        print(f"📥 Received from client: {data}")

        if b"PING" in data:
            connection.sendall(b"+PONG\r\n")
        else:
            connection.sendall(b"-ERR unknown command\r\n")

if __name__ == "__main__":
    main()
