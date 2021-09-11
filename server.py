# -*- coding: utf-8 -*-

import socket
nb_requetes = 5 #nombre de requetes de connexions 
host = 'localhost'
port = 9000

ourSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	ourSocket.bind((host, port))
except socket.error : 
	("server error")
	exit()
ourSocket.listen(nb_requetes)
print("serveur en ligne")
unending = True
while unending:
	connexion , adresse = ourSocket.accept()

	print("un connecté , ip : {0} , port : {1}".format(adresse[0],adresse[1]))
