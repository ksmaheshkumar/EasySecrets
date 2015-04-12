#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

import re

class HuntingOperations():
    # Regex based hunting.

    # Amazon Access Key: ‘(access_key_id|secret_access_key)'
    # Obfuscated HTTP url: ‘h[x]{2}p[s]*:\/\/[a-z0-9\-\./]+':
    # Certificate: ‘^—–BEGIN CERTIFICATE—–‘:
    # URL w/creds: ‘[ht|f]tp[s]*:\/\/\w+\:.*\@\w*\.\w*':

    def links(self, content):

        found = [] # List of found links
        linksrch = re.findall(r're.findall(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F])))+', content)
        print linksrch

        # remove duplicate link elements
        u = {}
        for item in found:
            u[item] = 1

        #returns a list of unique link(s)
        return u.keys()

    def usernamesandpasswords(self, content):
        pass

    def emailsandpasswords(self, content):
    # Email w/password: ‘[\s\|,;’]+[a-z0-9\-\._]+@[a-z0-9\-\.]+\.[a-z]{2,4}[\s\|,;:’]+':
        pass

    def simplecredentials(self, content):
        # Simple password: ‘^\s*pass(word|phrase|wd|code)*\s*(:|=|is|was)\s*[a-z0-9\-_\!]+$':
        # Simple password: ‘\s*pass[word]+\s*[:=]\s*[“‘][a-z0-9\-_\!\$]+[“‘]':
        pass

    def facebookaccesstokens(self, content):
        # API/private key: ‘(api|private)[-_]key[ “‘]*=[ =”‘]*\w+':
        pass

    def amazonec2keys(self, content):
        # Amazon EC2 Key:  ‘ec2.*[“‘][A-Z0-9]{20}[“‘]':
        pass

    def bitoinwallets(self, content):

        found = [] # List of found
        btcwsrch = re.compile(r'(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,30}(?![a-km-zA-HJ-NP-Z0-9])|(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{33,35}(?![a-km-zA-HJ-NP-Z0-9])')
        with open(fwbw, 'rb') as FileWithBitcoinAddress:
            for wallet in FileWithBitcoinAddress:
                wallet = wallet.replace('\n', '')
                if btcwsrch.findall(wallet):
                    found.append(wallet)

        # remove duplicate link elements
        u = {}
        for item in found:
            u[item] = 1

        #returns a list of unique link(s)
        return u.keys()

    def creditcards(self, content):
        # Supports detection for these Credit Card Types:

                # Visa
                # MasterCard
                # Discover
                # AMEX
                # Diners Club
                # JCB

        found = [] # List of found Credit card numbers

        ccsrch = re.compile(r'^(?:(4[0-9]{12}(?:[0-9]{3})?)|(5[1-5][0-9]{14})|(6(?:011|5[0-9]{2})[0-9]{12})|(3[47][0-9]{13})|(3(?:0[0-5]|[68][0-9])[0-9]{11})|((?:2131|1800|35[0-9]{3})[0-9]{11}))$')

        with open(foccn, 'rb') as FileWithCCN:
            for line in FileWithCCN:
                cnumbers = line.replace('\n', '')
                if ccsrch.findall(cnumbers):
                    found.append(cnumbers)

        # remove duplicate Cred card number elements
        u = {}
        for item in found:
            u[item] = 1

        #returns a list of unique CCN numbers
        return u.keys()

    def ssns(self, content): # USA Based

        found = [] # List of found SSN numbers
        ssnsrch = re.compile(r'^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$') # USA based.
        ssnsrch2 = re.compile(r'^(?!000|666)[0-8][0-9]{2}(?!00)[0-9]{2}(?!0000)[0-9]{4}$') # USA based.
        with open(fwssn, 'rb') as FileWithSSN:
            for line in FileWithSSN:
                numbers = line.replace('\n', '')

                if ssnsrch.findall(numbers): # adds SSN with (-) to list
                    found.append(numbers)

                if ssnsrch2.findall(numbers): # adds SSN without (-) to list
                    found.append(numbers)

        # remove duplicate ssn elements
        u = {}
        for item in found:
            u[item] = 1

        #returns a list of unique ssn numbers
        return u.keys()

    def emails(self, content):
        # if passed a list of text files, will return a list of
        # email addresses found in the files, matched according to
        # basic address conventions. Note: supports most possible
        # names, but not all valid ones.

        found = [] # List of found emails
        mailsrch = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')

        with open(foe, 'rb') as FileWithEmail:
            for line in FileWithEmail:
                email = line.replace('\n', '')
                if mailsrch.findall(email):
                    found.append(email)
            #return found | for debugging, when the code goes out of style.

        # remove duplicate email elements
        u = {}
        for item in found:
            u[item] = 1

        #returns a list of unique email addresses
        return u.keys()
huntdown = HuntingOperations()
