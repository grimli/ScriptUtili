#!/usr/bin/python
from pprint import pprint
import glob
import gzip
import re


debug = False;
fileListaBlog="lista_blog.txt"
listaLog = '../2015*_blogowp*';
listaFile={};
listaBlog=[];
cond_404 = re.compile('.*HTTP\/1.[01]\" 40.*');
cond_galleria = re.compile('.*\/galleria.*');
conteggi={};

for line in open(fileListaBlog, 'r'):
	listaBlog.append(line.replace("\n","_errors.gz"));
	#conteggi[line.replace("\n","")] = {};

for file in listaBlog:
	listaFile[file] = gzip.open(file,'w');

for log in glob.glob(listaLog):
	print log;
	for line in gzip.GzipFile(log, 'r'):
		if(cond_404.match(line)):
			if(cond_galleria.match(line)):
				blog = line.split('\"')[7];
				try:
					 type(conteggi[blog]);
				except:
					 conteggi[blog]={}; 
				if debug: print line.split('\"')[9];
				galleria = re.sub(r'GET /(galleria|galleriazoom)/(big/)?([\w\-!%]*)\b/?.*d* HTTP/\d\.\d', r'\g<3>', line.split('\"')[9]);
				try : 
					listaFile[blog+"_errors.gz"].write(galleria+"\n");
				except :
					print blog;

				try:
					conteggi[blog][galleria]+=1;
					if debug: print("num: "+str(conteggi[blog][galleria]));
					#print "\""+galleria+"\",\""+str(conteggi[blog][galleria])+"\"\n";
				except:
					conteggi[blog][galleria] = 1;
					if debug: print("num: "+str(conteggi[blog][galleria]));
					#print "\""+galleria+"\",\""+str(conteggi[blog][galleria])+"\"\n";

for name,fh in listaFile.items():
	fh.close();

# salvo conteggi
for keys, values in conteggi.items():
	file = open( "conteggi_"+keys, 'w');
	for galleria, conteggio in values.items():
		if debug: print "\""+galleria+"\",\""+str(conteggio)+"\"\n";
		file.write("\""+galleria+"\",\""+str(conteggio)+"\"\n");
	file.close();

