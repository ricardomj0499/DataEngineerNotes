import socket

# Crear un socket
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuración de la IP y el puerto donde escuchará el servidor
host = 'localhost'  # Dirección local
puerto = 12345      # Puerto de escucha

# Vincular el socket al host y al puerto
servidor_socket.bind((host, puerto))

# Escuchar conexiones entrantes (máximo 5 conexiones a la vez)
servidor_socket.listen(5)

print(f"Servidor escuchando en {host}:{puerto}...")

# Aceptar conexiones de los clientes
cliente_socket, direccion_cliente = servidor_socket.accept()

print(f"Conexión establecida con: {direccion_cliente}")

# Recibir un mensaje del cliente
mensaje = cliente_socket.recv(1024)  # Lee hasta 1024 bytes
print("Mensaje recibido:", mensaje.decode())

# Enviar respuesta al cliente
cliente_socket.sendall("Hola, cliente. Mensaje recibido.".encode())

# Cerrar la conexión
cliente_socket.close()
