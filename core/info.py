#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

from libs.paint import colors
from libs.functions import utilities

# Not functional yet.
# ./es.py hunt [GITHUB-REPO-LINK] | Hunt for all possible things that can be found.

def Help():
      utilities.pi("""
      """+colors.T+"""[GWF Certified] """+colors.N+""" - https://twitter.com/GuerrillaWF

      """+colors.W+"""# Global operations"""+colors.N+"""
      -----------------------
      ./es.py ego [USERNAME]| Get the profile of a user. (Doesn't work on Organizations.)

      ./es.py -a [USERNAME]| Add a username to the user database.

      ./es.py ping [USERNAME] OR ID number | query the user database for a username.

            OR

      """+colors.B+"""# User query operations"""+colors.N+"""
        -----------------------
      ./es.py ping [USERNAME] [SECTION] [KEYWORD]

      | Section: repo      | query a users repo database for a repo name.
      | Section: followers | query a users followers database for a username that follows the user.
      | Section: following | query a users following database for a user that the user is following.
      | Section: starred   | query a users starred repo database for a repo name they have bookmarked.

      """+colors.R+"""# User offensive operations"""+colors.N+"""
      -----------------------
      ./es.py -g [USERNAME] [KEYWORD] | Get something from a user.

      | Keyword: repos     | Record all the repos a user has.
      | Keyword: followers | Record all the followers a user has.
      | Keyword: starred   | Record all repos a user has bookmarked.
      | Keyword: following | Record all the accounts a user is following.

            OR

      """+colors.B+"""# Organization query operations"""+colors.N+"""
        ------------------------------
      ./es.py ping org [ORGNAME] [SECTION] [KEYWORD]

      | Section: repo      | query an organizations repo database for a repo name.
      | Section: ppl       | query an organizations people database for a user or user id.

      """+colors.R+"""# Organizations offensive operations"""+colors.N+"""
      --------------------------------------
      ./es.py -g org [ORGNAME][KEYWORD] | Get something from an organization.

      | Keyword: repos     | Record all the repos an organization has.
      | Keyword: ppl       | Record all the people an organization has.
      """)
