#!/usr/bin/python3
from pprint import pprint

debug = False
file = 'ldirectord.cf'

a = open(file, 'r')
itemList = a.readlines()
a.close()

riga = []
struttura = {}
linea = ""

# leggo dati
for line in itemList:
   riga=line.lstrip("\t ").rstrip("\n").split("=")
   if ( riga[0] == "virtual" ):
      pool = riga[1]
      struttura[ pool ] = []
   elif ( riga[0] == "real" ):
      struttura[ pool ].append( riga[1].split()[0] )

#pprint( struttura )

#genero output
for chiave, valore in struttura.items():
   linea = ""
   linea += chiave +  "," 
   for real in sorted( valore ):
      linea +=  real + "," 
   
   print( linea )
