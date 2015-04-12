#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-


import random
from libs.paint import colors
from libs.functions import utilities
# Incorporate random protips for the help screen

# Not functional yet.
# ./es.py hunt [GITHUB-REPO-LINK] | Hunt for all possible things that can be found.

def Help():
      utilities.pi("""
      """+colors.T+"""[GWF Certified] """+colors.N+""" - https://twitter.com/GuerrillaWF

      ./es.py ego [USERNAME]| Get the profile of a user. (Doesn't work on Organizations.)

      ./es.py -a [USERNAME]| Add a username to the user database.

      ./es.py ping [USERNAME] OR ID number | query the user database for a username.

            OR

      ./es.py ping [USERNAME] [SECTION] [KEYWORD]

      | Section: repo      | query a users repo database for a repo name.
      | Section: followers | query a users followers database for a username that follows the user.
      | Section: following | query a users following database for a user that the user is following.
      | Section: starred   | query a users starred repo database for a repo name they have bookmarked.


      ./es.py -g [USERNAME] [KEYWORD] | Get something from a user.

      | Keyword: repos     | Record all the repos a user has.
      | Keyword: followers | Record all the followers a user has.
      | Keyword: starred   | Record all repos a user has bookmarked.
      | Keyword: following | Record all the accounts a user is following.
      """)
