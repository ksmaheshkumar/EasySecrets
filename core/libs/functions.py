#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

# Dependency imports
import os
import sys
import requests
import threading

# Global user agent to use.
GLOBALUSERAGENT = {"User-Agent":"Mozilla/5.0 (X11; Linux x86; rv:37.0) Gecko/20100101 Firefox/37.0"}

class Utilities():

    def Acceleration(self, mtarget):
        """ Thread certain processes."""
        process = threading.Thread(target=mtarget)
        return process.start()

    def pi(self, pdata=''):
        print pdata

    # sys.argv bool checks for assurance.
    def sabc(self, argnum):
        try:
            if sys.argv[argnum]:
                return True
        except Exception:
            return False

    # Useful for interactive operations
    def select(self, message):
        while True:
            select = raw_input("\n{} ".format(message))
            return select

    # Get Socks 5 Requests | Will travel through here.
    def GetSOCKS5Request(self, url):
        """ Global get request w/browser UserAgent string."""
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, user.SOCKS5_PROXY[0], 9050) # TOR network socket
        socket.socket = socks.socksocket # use TOR
        GetRequestSession = requests.Session()
        response = GetRequestSession.get(url, headers=GLOBALUSERAGENT)
        return response # Just return the object, not the content.

    # String boolean self-check.
    def sbc(self, fn, s): # Check if string is in a file.
        #return a NoneType if the string is not in the file.
        #.readlines() May be a problem is database files get too large.

        if os.path.exists(fn) is False:
            MakeFile = open(fn, 'a').close()

        if os.path.exists(fn) is True:
            pass

        f = open(fn, 'r')
        f = f.readlines()
        for i in f:
            i = i.replace("\n", '')
            if s.encode('utf-8') in i:
                return True

    # Post Socks 5 Requests | Will travel through here.
    def PostSOCKS5Request(self, url):
        """ Global get request w/browser UserAgent string."""
        #socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, user.SOCKS5_PROXY[0], 9050) # TOR network socket
        #socket.socket = socks.socksocket # use TOR
        PostRequestSession = requests.Session()
        response = PostRequestSession.post(url, headers=GLOBALUSERAGENT, data=params)
        return response # Just return the object, not the content.

    # Get Requests HTTP style
    def GetHTTPRequest(self, url):
        GetRequestSession = requests.Session()
        #GetRequestSession.proxies = HTTP_PROXY # Only accepts http at this time.
        response = GetRequestSession.get(url, headers=GLOBALUSERAGENT)
        return response # Just return the object, not the content.

    # Post Requests HTTP style
    def PostHTTPRequest(self, url, params):
        PostRequestSession = requests.Session()
        PostRequestSession.proxies = user.HTTP_PROXY
        response = PostRequestSession.post(url, headers=GLOBALUSERAGENT, data=params)
        return response # Just return the object, not the content.
utilities = Utilities()
