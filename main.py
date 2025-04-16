import socket

# ✅ In-memory store (acts like Redis)
store = {}

def main():
    print("Redis server starting on port 6379...")

    server_socket = socket.create_server(("localhost", 6379))
    connection, _ = server_socket.accept()
    print("Client connected!")

    buffer = b""

    while True:
        chunk = connection.recv(1024)
        if not chunk:
            print("❌ Client disconnected.")
            break

        buffer += chunk

        if b"\r\n" not in buffer:
            continue  # Wait until full command is received

        # Split and process full command
        data = buffer.strip()
        buffer = b""  # reset buffer after reading

        print(f"📥 Full command: {data}")

        parts = data.split()

        if len(parts) == 1 and parts[0].upper() == b"PING":
            connection.sendall(b"+PONG\r\n")

        elif len(parts) == 3 and parts[0].upper() == b"SET":
            key = parts[1].decode()
            value = parts[2].decode()
            store[key] = value
            print(f"📝 Stored: {key} = {value}")
            connection.sendall(b"+OK\r\n")

        else:
            connection.sendall(b"-ERR unknown command\r\n")


if __name__ == "__main__":
    main()
