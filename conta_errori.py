#!/usr/bin/python3
from pprint import pprint
import glob
import gzip
import re


#debug = True;
debug = False;
fileErrori = '404.log.gz';
conteggioErrori = {};

h_fileErrori =  gzip.GzipFile(fileErrori,'r');
if debug: type(h_fileErrori);

for line in h_fileErrori.readlines():
    if debug: print(line);
    uri = line.decode('utf-8').split("\t");
    chiave = uri[7].split("/")[1];
    if debug: print(chiave);
    try:
        conteggioErrori[chiave] +=1;
    except:
        conteggioErrori[chiave] =1;

pprint(conteggioErrori);

h_fileErrori.close();
