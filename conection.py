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
    
    while True:
     taille_reponse_b = s.recv(4)
     if not taille_reponse_b:
            print("connexion out")
            break
     
     taille_reponse = struct.unpack('I', taille_reponse_b)[0] 
    
    
     msg_binaire = s.recv(taille_reponse)
     msg = json.loads(msg_binaire.decode('utf-8'))
    
    
     if msg.get("request") == "ping":
            print("Ping reçu !") 
    
     pong_data = json.dumps({"response": "pong"}).encode('utf-8')
            
           
     s.send(struct.pack('I', len(pong_data)) + pong_data)
    



register("MonIA", 5000, ["24186"])     