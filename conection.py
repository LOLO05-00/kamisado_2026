import socket
import struct
import json 


def register(nom, port, matricules): 
    s= socket.socket() 
    s.connect(('172.17.83.160', 3000))
    
    data = json.dumps({
            "request": "subscribe",
            "port": port,
            "name": nom,
            "matricules": matricules
        }).encode() 
    
    taille_en_b = struct.pack('I', len(data))
    s.send(taille_en_b) 
    sent = s.send(data)
    
    if sent == len (data): 
     print (" Envoi complet ") 
    taille_reponse_b = s.recv(4)
    taille_reponse = struct.unpack('I', taille_reponse_b)[0]
    
    
    msg = s.recv(taille_reponse).decode('utf-8')
    print("Reçu")
    print(msg)


register("MonIA", 5000, ["24186"])     