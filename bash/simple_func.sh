#!/bin/bash
# indica al sistema que este script debe ejecutarse con el intérprete de Bash si no seria bash ipsweep.sh

# --- Ejemplo simple de variables y funciones en Bash ---
# echo "Hola, cual es tu nombre?"
# read name
# echo "Hola $name, como estas?"

# --- look for active devices in a network ---

echo $(date) | cut -d ' ' -f 4 # Hora actual, para saber tiempo de ejecución

# Verificar si el usuario proporcionó un argumento
if [ -z "$1" ]; then # -z verifica si la longitud de la cadena es cero
    echo "Oops! You forgot an IP Address"
    echo "Syntax: ./ipsweep.sh 192.168.7"
else
    # Iterar sobre los posibles hosts en la subred
    for ip in $(seq 1 254); do 
        ping -c 1 "$1.$ip" | grep '64 bytes' | cut -d ' ' -f 4 | tr -d ':' & 
    done
    wait  # Esperar a que terminen todos los procesos en segundo plano
fi

echo $(date) | cut -d ' ' -f 4 # hora de terminacion del proceso

<<COMMENT

ejemplo del for con localhost

- ping -c 1 localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.016 ms

--- localhost ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.016/0.016/0.016/0.000 ms


- ping -c 1 192.168.7.118 | grep 64
64 bytes from 192.168.7.118: icmp_seq=1 ttl=64 time=0.012 ms


- ping -c 1 192.168.7.118 | grep 64 | cut -d " " -f 4 
192.168.7.118:


- ping -c 1 192.168.7.118 | grep 64 | cut -d " " -f 4 | tr -d ':'
192.168.7.118


y "&" ejecuta el proceso en segundo plano permitiendo concurrencia

con concurrencia >
19:46:12 - 19:46:02 > 10 seg

sin >
19:59:13 - 19:46:34 Alrededor de 13 min

probando de nuevo con concurrencia> 10 seg

COMMENT