import socket

# Crear un socket
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dirección del servidor y el puerto
host = 'localhost'
puerto = 12345

# Conectar al servidor
cliente_socket.connect((host, puerto))

# Enviar un mensaje al servidor
mensaje = "¡Hola, servidor!"
cliente_socket.sendall(mensaje.encode())

# Recibir la respuesta del servidor
respuesta = cliente_socket.recv(1024)
print("Respuesta del servidor:", respuesta.decode())

# Cerrar la conexión
cliente_socket.close()
