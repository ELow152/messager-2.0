import socket
import threading
import time
import json

# Function to handle receiving messages
def receive_messages(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            if data:
                message = data.decode()
                print(f"\nReceived: {message} from {addr}")
            else:
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

# Function to send broadcast messages to find servers
def discover_servers(sock):
    broadcast_message = json.dumps({'action': 'DISCOVER', 'ip': sock.getsockname()[0], 'port': sock.getsockname()[1]}).encode()
    sock.sendto(broadcast_message, ('<broadcast>', 55555))  # Broadcast on the network
    print("Broadcasting for servers...")
    time.sleep(2)  # Wait for a while to listen for responses

# Function to handle sending messages
def send_messages(sock):
    while True:
        message = input("You: ")
        # Sending to connected address (client)
        destination = input("Send to (IP:PORT) or 'b' for broadcast: ")
        if destination == 'b':
            broadcast_message = message.encode()

            sock.sendto(broadcast_message, ('<broadcast>', 55555))
        else:
            try:
                ip, port = destination.split(':')
                sock.sendto(message.encode(), (ip, int(port)))
            except Exception as e:
                print(f"Invalid destination: {e}")

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcast
    sock.bind(('', 55555))  # Bind to the port

    # Start a thread to receive messages
    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    # Announce server presence
    print(f"Server initialized at {sock.getsockname()[0]}:{sock.getsockname()[1]}")
    
    # Discover servers
    discover_servers(sock)

    print("You can start sending messages now.")
    # Handle sending messages
    send_messages(sock)

if __name__ == "__main__":
    main()
