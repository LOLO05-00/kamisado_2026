import socket
import struct
import json 

def register(nom, port, matricules): 
    s = socket.socket() 
    
    try:
        s.connect(('192.168.129.200', 3000))
        
        data = json.dumps({
            "request": "subscribe",
            "port": port,
            "name": nom,
            "matricules": matricules
        }).encode("utf-8") 
        
        s.send(struct.pack('I', len(data)) + data)
        
        reponse_b = s.recv(4)
        if not reponse_b:
            print("connexion out")
            return
            
        reponse = struct.unpack('I', reponse_b)[0]
        msg = s.recv(reponse).decode('utf-8')
        print("Inscription :", msg)
        
    except OSError as e:
        print(f"Erreur réseau : {e}")
    except struct.error as e:
        print(f"Erreur de dépaquetage : {e}")
    finally:
        s.close()
    serveur = socket.socket()
    
    try:
       serveur.bind(('0.0.0.0', port))
       serveur.listen()
       print("En écoute...")
        
       while True:
            conn, _ = serveur.accept()
            try:
              taille_b = conn.recv(4)
              if not taille_b:
                    continue
                    
              taille = struct.unpack('I', taille_b)[0]
                
              donnees = b''
              while len(donnees) < taille:
                  donnees += conn.recv(taille - len(donnees))
                    
              requete = json.loads(donnees.decode('utf-8'))
                
              if requete.get("request") == "ping":
                    reponse_pong = json.dumps({"response": "pong"}).encode('utf-8')
                    conn.send(struct.pack('I', len(reponse_pong)) + reponse_pong)
                    print("Pong envoyé")
            except OSError as e:
              print(f"Erreur de communication : {e}")
            except struct.error as e:
              print(f"Erreur de dépaquetage serveur : {e}")
            finally:
              conn.close()
    except OSError as e:
       print(f"Erreur de communication : {e}")
    except struct.error as e:
       print(f"Erreur de dépaquetage serveur : {e}")
    finally:
       conn.close()      
    
    

    



register("AdamIA", 5000, ["24186"])     