#!/usr/bin/python
# -*- coding: utf-8 -*-
'''# -*- coding: latin-1 -*-'''
from xml.dom.minidom import parse
from xml.dom import minidom
import urllib2
import sys
import time
from pprint import pprint 

''' url = 'http://servicos.cptec.inpe.br/XML/cidade/239/estendida.xml' '''
url = 'http://servicos.cptec.inpe.br/XML/cidade/239/previsao.xml'
dom = minidom.parse(urllib2.urlopen(url))
collection = dom.documentElement

dataAtual = time.strftime("%Y-%m-%d")
previsoes = collection.getElementsByTagName("previsao")

'''pprint(previsoes)'''

reload(sys).setdefaultencoding("utf8")
'''print sys.getdefaultencoding()'''
'''print(len(previsoes))'''


for a in previsoes :
	dia = a.getElementsByTagName('dia')[0]	
	if dataAtual==dia.childNodes[0].data.strip() :
		'''print "Dia: %s" % dia.childNodes[0].data'''
		tempo1 = a.getElementsByTagName('tempo')[0]
		'''print "tempo: %s" % tempo1.childNodes[0].data'''
	   
		maxima1 = a.getElementsByTagName('maxima')[0]
		'''print "maxima: %s" % maxima1.childNodes[0].data'''
	   
		minima1 = a.getElementsByTagName('minima')[0]
		'''print "minima: %s" % minima1.childNodes[0].data'''
			










'''pprint(tempo1)
pprint(maxima1)
pprint(minima1)'''
	
'''
for previsao in previsoes :
   print "*****Previsao*****"
   dia = previsao.getElementsByTagName('dia')[0]
   print "Dia: %s" % dia.childNodes[0].data
   
   tempo1 = previsao.getElementsByTagName('tempo')[0]
   print "tempo: %s" % tempo1.childNodes[0].data
   
   maxima1 = previsao.getElementsByTagName('maxima')[0]
   print "maxima: %s" % maxima1.childNodes[0].data
   
   minima1 = previsao.getElementsByTagName('minima')[0]
   print "minima: %s" % minima1.childNodes[0].data
'''


'''tempo1 = previsoes2[0].getElementsByTagName('tempo')[0]
maxima1 = previsoes2[0].getElementsByTagName('maxima')[0]
minima1 = previsoes2[0].getElementsByTagName('minima')[0] '''


stringNomeTempo=""
if tempo1.childNodes[0].data.strip()=="c":
    stringNomeTempo = "Chuva"
elif tempo1.childNodes[0].data.strip()=="ec":
    stringNomeTempo = "Enc. com Chuvas Isoladas"
elif tempo1.childNodes[0].data.strip()=="ci":
    stringNomeTempo = "Chuvas Isoladas"
elif tempo1.childNodes[0].data.strip()=="in":
    stringNomeTempo = "Instável"
elif tempo1.childNodes[0].data.strip()=="pp":
    stringNomeTempo = "Poss. de Pancadas de Chuva"
elif tempo1.childNodes[0].data.strip()=="cm":
    stringNomeTempo = "Chuva pela Manhã"
elif tempo1.childNodes[0].data.strip()=="cn":
    stringNomeTempo = "Chuva a Noite"
elif tempo1.childNodes[0].data.strip()=="pt":
    stringNomeTempo = "Pan. de Chuva a Tarde"
elif tempo1.childNodes[0].data.strip()=="pm":
    stringNomeTempo = "Pan. de Chuva pela Manhã"
elif tempo1.childNodes[0].data.strip()=="np":
    stringNomeTempo = "Nublado e Pancadas de Chuva"
elif tempo1.childNodes[0].data.strip()=="pc":
    stringNomeTempo = "Pancadas de Chuva"
elif tempo1.childNodes[0].data.strip()=="pn":
    stringNomeTempo = "Parcialmente Nublado"
elif tempo1.childNodes[0].data.strip()=="cv":
    stringNomeTempo = "Chuvisco"
elif tempo1.childNodes[0].data.strip()=="ch":
    stringNomeTempo = "Chuvoso"
elif tempo1.childNodes[0].data.strip()=="t":
    stringNomeTempo = "Tempestade"
elif tempo1.childNodes[0].data.strip()=="ps":
    stringNomeTempo = "Predomínio de Sol"
elif tempo1.childNodes[0].data.strip()=="e":
    stringNomeTempo = "Encoberto"
elif tempo1.childNodes[0].data.strip()=="n":
    stringNomeTempo = "Nublado"
elif tempo1.childNodes[0].data.strip()=="cl":
    stringNomeTempo = "Céu Claro"
elif tempo1.childNodes[0].data.strip()=="nv":
    stringNomeTempo = "Nevoeiro"
elif tempo1.childNodes[0].data.strip()=="g":
    stringNomeTempo = "Geada"
elif tempo1.childNodes[0].data.strip()=="ne":
    stringNomeTempo = "Neve"
elif tempo1.childNodes[0].data.strip()=="nd":
    stringNomeTempo = "Não Definido"
elif tempo1.childNodes[0].data.strip()=="pnt":
    stringNomeTempo = "Pancadas de Chuva a Noite"
elif tempo1.childNodes[0].data.strip()=="psc":
    stringNomeTempo = "Poss. de Chuva"
elif tempo1.childNodes[0].data.strip()=="pcm":
    stringNomeTempo = "Poss. de Chuva pela Manhã"
elif tempo1.childNodes[0].data.strip()=="pct":
    stringNomeTempo = "Poss. de Chuva a Tarde"
elif tempo1.childNodes[0].data.strip()=="pcn":
    stringNomeTempo = "Poss. de Chuva a Noite"
elif tempo1.childNodes[0].data.strip()=="npt":
    stringNomeTempo = "Nublado com Pancadas a Tarde"
elif tempo1.childNodes[0].data.strip()=="npn":
    stringNomeTempo = "Nublado com Pancadas a Noite"
elif tempo1.childNodes[0].data.strip()=="ncn":
    stringNomeTempo = "Nublado com Poss. de Chuva a Noite"
elif tempo1.childNodes[0].data.strip()=="nct":
    stringNomeTempo = "Nublado com Poss. de Chuva a Noite"
elif tempo1.childNodes[0].data.strip()=="ncm":
    stringNomeTempo = "Nubl. c/ Poss. de Chuva pela Manhã"
elif tempo1.childNodes[0].data.strip()=="npm":
    stringNomeTempo = "Nublado com Pancadas pela Manhã"
elif tempo1.childNodes[0].data.strip()=="npp":
    stringNomeTempo = "Nublado com Possibilidade de Chuva"
elif tempo1.childNodes[0].data.strip()=="vn":
    stringNomeTempo = "Variação de Nebulosidade"
elif tempo1.childNodes[0].data.strip()=="ct":
    stringNomeTempo = "Chuva a Tarde"
elif tempo1.childNodes[0].data.strip()=="ppn":
    stringNomeTempo = "Poss. de Panc. de Chuva a Noite"
elif tempo1.childNodes[0].data.strip()=="ppt":
    stringNomeTempo = "Poss. de Panc. de Chuva a Tarde"
elif tempo1.childNodes[0].data.strip()=="ppm":
    stringNomeTempo = "Poss. de Panc. de Chuva pela Manhã"

print '${voffset -2}${image ~/.conky/imgTempo/'+tempo1.childNodes[0].data.strip()+'.png -p 150,8 -s 101x64}'
print '${voffset -15}${color4}Recife'
print stringNomeTempo
print 'Máx. '+maxima1.childNodes[0].data.strip()+'ºC - Mín. '+minima1.childNodes[0].data.strip()+'ºC'
# pra continuar olhar este link https://blog.eduardoweiland.info/exibindo-a-temperatura-atual-no-conky/
#listaPrevisao = dom.getElementsByTagName('previsao');
#print(len(listaPrevisao));
#print(listaPrevisao);
#for s in listaPrevisao:	
	#elemento = s.getElementsByTagName('maxima')

	#pprint(dom)



#import urllib
#from xml.dom import minidom
#from pprint import pprint
 
# config options
#WEATHER_URL = 'http://servicos.cptec.inpe.br/XML/cidade/239/estendida.xml'
#WEATHER_NS  = 'http://xml.weather.yahoo.com/ns/rss/1.0'
#location    = '455988'
 
#url      = WEATHER_URL % location
#url      = WEATHER_URL
#response = urllib.urlopen(url)
#xml      = minidom.parse(response)


 
# get current temperature
#current = xml.getElementsByTagNameNS(WEATHER_URL, 'cidade')
#temperature = current.getAttribute('temp')

#pprint(current)

 
#print temperature

