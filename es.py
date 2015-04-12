#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

# Native imports
import sys

from core.info import Help # Help Message
from core.libs.shark import huntdown # HUNT DOWN INFORMATION !
from core.libs.functions import utilities
from core.libs.storage import dbops # Database operations # Auto Write to database
from core.libs.github import regexops # NON  API limited scraping!

# Dependency imports
import requests

# POSSIBLE ADDITIONS
# Grab if user belongs to an organization.
# Improve database query searches w/multiple responses
# May use configure.py to block out things you don't want to grab when hunting.

# SEARCH FEATURES:
# Add github dorks, for faster searching.

# BUGS:
# Emails render as hex ... must find a way to decode.

PL = "https://github.com/" # Initial Profile link

HTTP_PROXY = {'http':''} # Set the proxy yourself.
SOCKS5_PROXY = [] # Set the proxy yourself.
HTTP_PROXY['http'] = '' # Uses your current ip by defualt.
SOCKS5_PROXY.append("127.0.0.1")

def main(IFNOMAINARG):

    #options, arguments = getopt.getopt(sys.argv[1:], 'h a: g: p:', ['hunt=','ping=', 'ego='])

    # System arg bools
    s1 = utilities.sabc(1)
    s2 = utilities.sabc(2)
    s3 = utilities.sabc(3)
    s4 = utilities.sabc(4)

    try:
        # Keywords:
        # repos, followers, following, starred

        if sys.argv[1] == "help" or sys.argv[1] == "-h":
            Help()

        if sys.argv[1] == '-a': # Add Username/ID/Link to user database
            dbops.WriteUserToDatabaseVERBALLY(sys.argv[2])

        if sys.argv[1] == 'ping' and s2 is True and s3 is False and s4 is False:
            dbops.QueryUserDatabase(sys.argv[2])

        if 'ping' and s3 is True and s4 is True and sys.argv[3] == 'repo':
            dbops.QueryUserRepoDatabase(sys.argv[2], sys.argv[4])

        if 'ping' and s3 is True and s4 is True and sys.argv[3] == 'followers':
            dbops.QueryUserFollowersDatabase(sys.argv[2], sys.argv[4])

        if 'ping' and s3 is True and s4 is True and sys.argv[3] == 'following':
            dbops.QueryUserFollowingDatabase(sys.argv[2], sys.argv[4])

        if  sys.argv[1] == 'ego' and s2 is True and s3 is False:
            dbops.WriteUserToDatabaseSILENTLY(sys.argv[2])
            regexops.GetCurrentProfile(sys.argv[2])
            exit(0)

        if sys.argv[1] == '-g' and sys.argv[3] == "repos": #Record repo names
            dbops.WriteUserToDatabaseSILENTLY(sys.argv[2])
            repos = regexops.CollectRepositories(sys.argv[2])
            dbops.WriteUsersReposToFile(sys.argv[2], repos)

        if sys.argv[1] == '-g' and s2 is True and s3 is True and sys.argv[3] == "starred":
            starred = regexops.CollectStarredRepos(sys.argv[2])
            # Record users bookmarks (what repose they have starred.)
            dbops.WriteUsersStarredReposToFile(sys.argv[2], starred)

        if sys.argv[1] == '-g' and sys.argv[3] == "followers":
            dbops.WriteUserToDatabaseSILENTLY(sys.argv[2])
            # Record a users followers
            followers = regexops.CollectFollowers(sys.argv[2])
            dbops.WriteUsersFollowersToFile(sys.argv[2], followers)

        if sys.argv[1] == '-g' and sys.argv[3] == "following":
            dbops.WriteUserToDatabaseSILENTLY(sys.argv[2])
            # Record who a user is following
            following = regexops.CollectFollowing(sys.argv[2])
            dbops.WriteWhoUserIsFollowingToFile(sys.argv[2], following)

        if sys.argv[1] != '-g' and sys.argv[1] != 'ego' and sys.argv[1] != 'ping' and sys.argv[1] != '-a' and sys.argv[1] != 'help' and sys.argv[1] != '-h':
            Help()

    except IndexError:
        pass

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        Help()
