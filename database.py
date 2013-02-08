#!/usr/bin/env python
'''
Icecast

This program is distributed under the GNU General Public License, version 2.
A copy of this license is included with this source.
Copyright 2013,     Mattia Valente <extremepowermetal@hotmail.it>, 
                    Maicol Aprigliano <mai_c@live.it>
                    and others (see AUTHORS for details).
'''
import sqlite3
import sys
import os
class database():
    '''definition of class database:
        crea_tabella():
        get_keyGSS():
        get_keyMP():
        caricamento_database(ListaInfoMP):
        apertura_db():
        chisura_db():
        check_condb()
    
    '''
    def __init__(self):
        

        conne=self.check_condb()
        if conne==False:  
            self.crea_tabella()
        self.__c,self.__conn=self.apertura_db()
         
         
         
    def crea_tabella(self):
        '''create the table for insert the data'
       
       
       
        Arguments:
       
       :returns: the exist or not of the database
        '''
        try:
            self.__c.execute('''Create table MountPoint (nomeM text,audio_info text,bitrate text,channels text,
                   genre text,listener_peak text,listeners text,listenurl text,max_listeners text,public text,
                   samplerate text,server_description text,server_name text,server_type text,server_url text,
                   slow_listeners text,source_ip text,stream_start text,title text,total_bytes_read text,
                   total_bytes_sent text,dataC date)''')
           
            self.__c.execute('''CREATE TABLE Global(nome text, admin text, client_connections text,
                   clients text, connections text, file_connections text, host text,
                   listener_connections text, listeners text, location text,
                   server_id text, server_start text, source_client_connections text,
                   source_relay_connections text, source_total_connections text,
                   sources text, stats text, stats_connections text,data date)''')
       
            print "Creo le 2 tabelle"
        except:
            print "Tabelle gia' esistenti"
       
       
    def get_keyGSS(self):
        '''take the column's name of Global Server's table
       
       
       
         Arguments:
       
            :returns: column's name of Global Server's table
        '''
           
        columns = []
        strSQL = "SELECT * FROM Global"
        self.__c.execute(strSQL)
        for fieldName in self.__c.description:
            temp = fieldName[0]
            columns.append(temp)
     
        return columns

    def caricamento_database(self,ListaInfoMp):
        '''insert 
       
       
       
         Arguments:
       
            :returns: column's name of Mount Point's table
        '''
        for k in ListaInfoMp:
                if k[0]=="Global Server":
                    self.__c.execute('''insert into Global values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',k)
                     
                else:
                    self.__c.execute('''insert into MountPoint values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',k)
                self.__conn.commit()
        print 'dati inseriti'   
       
    def get_keyMp(self):
        '''take the column's name of Mount Point's table
       
       
       
         Arguments:
       
            :returns: column's name of Mount Point's table
        '''
        columns = []
        strSQL = "SELECT * FROM MountPoint"
        self.__c.execute(strSQL)
        for fieldName in self.__c.description:
            temp = fieldName[0]
            columns.append(temp)
        return columns
       
    def apertura_db (self):
        '''open the database'''
        conn=sqlite3.connect('icecast.db')
        c = conn.cursor()
        return c,conn
    def chiusura_db(self):
        '''close the database'''
        conn.close()
       
   
    def check_condb(self):
        '''control the existence of the database'''
        conne=os.path.exists( os.path.relpath(sys.path[0] + "/icecast.db"))
        return conne
