import socket
import struct
import json 


def register(nom, port, matricules): 
    s= socket.socket() 
    
    data = json.dumps({
            "request": "subscribe",
            "port": port,
            "nom": nom,
            "matricules": matricules
        }).encode() 
    sent = s.send( data ) 
    
    if sent == len ( data ):
     print (" Envoi complet ") 
    
    msg = s. recv (512) . decode ()
    print ("Reçu" , len ( msg ) , "octets :")
    print ( msg )