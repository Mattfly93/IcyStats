#!/usr/bin/env python
'''
Icecast

This program is distributed under the GNU General Public License, version 2.
A copy of this license is included with this source.
Copyright 2013,     Mattia Valente <extremepowermetal@hotmail.it>, 
                    Maicol Aprigliano <mai_c@live.it>
                    and others (see AUTHORS for details).
'''

from connessione import check_con
from addDati import addDati
from database import database
from time import localtime
import time

if __name__ == "__main__":
    database=database()
    database.crea_tabella()
    print "Registro su DB"
    while 1:    
        html = check_con("150.217.48.146", "8000","admin","akelsdvve292")
        if html:
            database.caricamento_database(addDati(html,database)) 
            time.sleep(30)
            
        else:
            print "----------"
            time.sleep(10)
   
