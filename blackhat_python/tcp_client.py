import socket

target_host = '127.0.0.1'
target_port = 9999

# target_host = 'www.google.com'
# target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

client.send(b"Hello")
# client.send(b"GET / HTTP/1.1\nHost: google.com\n\n")

response = client.recv(4096)
print(response.decode())
client.close()
