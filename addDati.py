#!/usr/bin/env python
'''
Icecast

This program is distributed under the GNU General Public License, version 2.
A copy of this license is included with this source.
Copyright 2013,     Mattia Valente <extremepowermetal@hotmail.it>, 
                    Maicol Aprigliano <mai_c@live.it>
                    and others (see AUTHORS for details).
'''
from bs4 import BeautifulSoup
from database import database
from time import strftime,localtime

class InfoMountPoint:                                                                    #estrapolazione info dei Mount Point                                                                                                                  
    '''
        contaMP(html):
        addDati(html)
    '''
    def __init__ (self,tabinfo,mp=None):
        '''definition of InfoMountPoint'
       
       
       
        Arguments:
       
       :params tabinfo: attributes of Mount point
       :params mp: name of Mount Point
        '''
        self.__name=None                                                                         
        self.__attributo={}
        self.__tabinfo=tabinfo
        if not  mp:
                         
            self.__name="Global Server"                                                 #se non esiste si passa il Global Server
        else:
            try:
               self.__name=mp.h3.get_text().split('/',1)[1]                             #controllo il nome del Mount Point
               
            except:
                print "nessun mount point trovato"
                return None                                                                                                         
        
    def get_name(self):                                                                 #restituisce il nome del Mount Point
        return self.__name
    def get_attributo(self,key):
        if len(self.__attributo)==0:
            for link in self.__tabinfo.find_all('tr'):                                                                           
                self.__attributo[unicode(link.findNext('td').contents[0])]=unicode(link.findNext('td').findNext('td').contents[0])
        try:                                                                                                                                                                                              #restituisce il valore di una determinata caratteristica del Mount Point
            return self.__attributo[key]                                                      #scelta dal campo key
        except:
            return ""
        
def contaMp(html):
    '''count Mount Point of icecast'
   
   
   
        Arguments:
   
        :params html: the html's page of icecast/admin
   
        :returns: the number of Mount Point
    '''
    contMp=0
    soup=BeautifulSoup(html)
    for link in soup.find_all('h3'):
        contMp=contMp+1
    contMp=contMp-1
    return contMp


def addDati(html,db):
    '''add datas in a list called 'ListaInfoMp'
       
       
       
       Arguments:
       
       :params html: the html's page of icecast/admin
       :params db: class db
       
       :returns: the list called 'ListaInfoMP'
    '''
    soup = BeautifulSoup(html)
    info =list()                                                                
    table = list()                                                     
    for child in soup.find_all('table'):                                           #Trova tutte le tabelle     
        table.append(BeautifulSoup(str(child)))
    contT=2
    
    cont=0
    contMp=contaMp(html) 
    k=(3*(contMp-1))+contT
    ChiaviMp=db.get_keyMp()                                                        #restituisce tutti i nomi delle colonne della tab. Mp
    ChiaviGSS=db.get_keyGSS()                                                      #restituisce tutti i nomi delle colonne della tab. Global 
    ListaInfoMp=[]
    ListaInfoMp.append(list())                                                            
    a=InfoMountPoint(table[1])                                                  #crea l'oggetto InfoMoutPoint
    tempo=strftime("%Y-%m-%d %H:%M:%S", localtime())
    
    ListaInfoMp[cont].append(a.get_name())
    for c in range(1,len(ChiaviGSS)-1):                                           #inserisce  i valori del Global nella lista
        ListaInfoMp[cont].append(unicode(a.get_attributo(ChiaviGSS[c])))
    ListaInfoMp[cont].append(unicode(tempo))
    
    cont=cont+1
    while contT<=k:                                                             #ciclo per tutti i MP presenti
        a=InfoMountPoint(table[contT+2],table[contT])                           #Richiama la classe InfoMoutPoint
        ListaInfoMp.append(list())
        ListaInfoMp[cont].append(unicode(a.get_name()))                                   #inserisce il nome del MP nella lista
        for s in range (1,len(ChiaviMp)-1):                                       #inserisce  i valori del MP nella lista
            ListaInfoMp[cont].append(unicode(a.get_attributo(ChiaviMp[s])))
        ListaInfoMp[cont].append(unicode(tempo))    
        contT=contT+3
        cont=cont+1
    return ListaInfoMp
    

    
