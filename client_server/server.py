import socket

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) - shift) % 26 + ord(base))
        else:
            result += char
    return result

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 8888))
server_socket.listen(1)
print("Server listening on port 8888...")

client_socket, addr = server_socket.accept()
print(f"Connected by {addr}")

try:
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            print("Client disconnected.")
            break
        
        decrypted = caesar_cipher(data, 3)
        print(f"Client says (decrypted): {decrypted}")
        
        response = input("Reply (plain text, or 'quit' to exit): ")
        if response.lower() == 'quit':
            client_socket.send("quit".encode())
            break
        
        # Encrypt before sending
        encrypted_response = caesar_cipher(response, -3)  # encrypt by shifting forward 3, so reverse shift is -3 here
        client_socket.send(encrypted_response.encode())

finally:
    client_socket.close()
    server_socket.close()
