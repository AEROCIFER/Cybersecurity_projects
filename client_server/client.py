import socket

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8888))

try:
    while True:
        message = input("You: ")
        if message.lower() == 'quit':
            client_socket.send("quit".encode())
            break

        
        encrypted_message = caesar_cipher(message, 3)
        client_socket.send(encrypted_message.encode())

        data = client_socket.recv(1024).decode()
        if data.lower() == 'quit':
            print("Server ended the chat.")
            break

        decrypted_message = caesar_cipher(data, -3)
        print(f"Server: {decrypted_message}")

finally:
    client_socket.close()
