#!/usr/bin/env python
'''
Icecast

This program is distributed under the GNU General Public License, version 2.
A copy of this license is included with this source.
Copyright 2013,     Mattia Valente <extremepowermetal@hotmail.it>, 
                    Maicol Aprigliano <mai_c@live.it>
                    and others (see AUTHORS for details).
'''
import urllib2
import base64

def check_con(server,port,usn,psw):
    '''controll connection between pc and icecsat server'
       
       
       
       Arguments:
       
       :params server: name of the server
       :params port: port
       :params usn: username
       :params psw: password
       
       :returns: if the connection go on or not
    '''
    theurl = "http://%s:%s/" % (server,port)
    request = urllib2.Request(theurl)
    try:
        op=urllib2.urlopen(request)
    except:
        print "Connessione fallita"
        return None
    
    #theurl = "http://%s:%s/admin/stats.xsl" % (server,port)
    richiesta = urllib2.Request(str(theurl)+"admin/stats.xsl")
    base64string = base64.encodestring('%s:%s' % (usn, psw)).replace('\n', '')          
    richiesta.add_header("Authorization", "Basic %s" % (base64string))
    
    try:
        response = urllib2.urlopen(richiesta)
        return response.read()
    except:
        print "Autenticazione fallita"
        return None
    
