#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

# Native imports
import sys

from core.libs.paint import colors # For colorful output.
from core.info import Help # Help Message
from core.libs.shark import huntdown # HUNT DOWN INFORMATION !
from core.libs.functions import utilities
from core.libs.storage import dbops # Database operations # Auto Write to database
from core.libs.github import regexops # NON  API limited scraping!

# POSSIBLE ADDITIONS
# Grab if user belongs to an organization.
# Improve database query searches w/multiple responses
# May use configure.py to block out things you don't want to grab when hunting.
# Case detection for getting organization info when querying a user.
# https://github.com/orgs/facebook/people | 404 based check for detering wrong searches


# SEARCH FEATURES:
# Add github dorks, for code, repo ... etc searching.

# BUGS:
# Emails render as hex ... must find a way to decode.

# Colored variables for output use.
INFO = colors.W+"[INFO]"+colors.N + ": "
FAIL = colors.R+"[FAILED]"+colors.N + ": "
ERROR = colors.R+"[ERROR]"+colors.N + ": "
FOUND = colors.W+"[FOUND]"+colors.N + ": "

#HTTP_PROXY = {'http':''} # Set the proxy yourself.
#SOCKS5_PROXY = [] # Set the proxy yourself.
#HTTP_PROXY['http'] = '' # Uses your current ip by defualt.
#SOCKS5_PROXY.append("127.0.0.1")

def main(IFNOMAINARG):

    #options, arguments = getopt.getopt(sys.argv[1:], 'h a: g: p:', ['hunt=','ping=', 'ego='])

    # System arg bools
    s1 = utilities.sabc(1)
    s2 = utilities.sabc(2)
    s3 = utilities.sabc(3)
    s4 = utilities.sabc(4)
    s5 = utilities.sabc(5)
    s6 = utilities.sabc(6)
    s7 = utilities.sabc(7)

    try:
        # Keywords:
        # repos, followers, following, starred

        if sys.argv[1] == "help" or sys.argv[1] == "-h":
            Help()

        # Add Username/ID/Link to user mass database
        if sys.argv[1] == '-a': # Add Username/ID/Link to user database
            dbops.WriteUserToDatabaseVERBALLY(sys.argv[2])

        # Ping the user database for an account, can be id or name.
        if sys.argv[1] == 'ping' and s2 is True and s3 is False and s4 is False:
            dbops.QueryUserDatabase(sys.argv[2])

        # Ping a users repo database for a repo
        if sys.argv[1] == 'ping' and s3 is True and s4 is True and sys.argv[3] == 'repo':
            try:
                dbops.QueryUserRepoDatabase(sys.argv[2], sys.argv[4])
            except IOError:
                utilities.pi('{}No repos have been recoreded for {}\n'.format(ERROR, sys.argv[2]))

        # Ping a users follower database for a users follower.
        if sys.argv[1] == 'ping' and s3 is True and s4 is True and sys.argv[3] == 'followers':
            try:
                dbops.QueryUserFollowersDatabase(sys.argv[2], sys.argv[4])
            except IOError:
                utilities.pi('{}No followers have been recoreded for {}\n'.format(ERROR, sys.argv[2]))

        # Ping a users following database for an account a user is following.
        if sys.argv[1] == 'ping' and s3 is True and s4 is True and sys.argv[3] == 'following':
            try:
                dbops.QueryUserFollowingDatabase(sys.argv[2], sys.argv[4])
            except IOError:
                utilities.pi('{}None of the users that {} is following have been recorded yet.\n'.format(ERROR, sys.argv[2]))

        # Ping a users starred repo database for a repo.
        if sys.argv[1] == 'ping'  and s3 is True and s4 is True and sys.argv[3] == 'starred':
            try:
                dbops.QueryUserStarredRepoDatabase(sys.argv[2], sys.argv[4])
            except IOError:
                utilities.pi('{} No starred repositories have been recorded for {} \n'.format(ERROR, sys.argv[2]))

        # Ping an orgs repo database for a repo.
        if sys.argv[1] == 'ping'  and sys.argv[2] == "org" and s3 is True and s4 is True and s5 is True and sys.argv[4] == 'repo':
            try:
                dbops.QueryOrgRepoDatabase(sys.argv[3], sys.argv[5])
            except IOError:
                utilities.pi('{} No repositories have been recorded for {} \n'.format(ERROR, sys.argv[3]))

        # Ping an orgs people/members database for a person.
        if sys.argv[1] == 'ping'  and sys.argv[2] == "org" and s3 is True and s4 is True and s5 is True and sys.argv[4] == 'ppl':
            try:
                dbops.QueryOrgPeopleDatabase(sys.argv[3], sys.argv[5])
            except IOError:
                utilities.pi('{} No people have been recorded from {}s github organization\n'.format(ERROR, sys.argv[3]))

        # Get a github USERS profile
        if  sys.argv[1] == 'ego' and s2 is True and s3 is False:
            dbops.WriteUserToDatabaseSILENTLY(sys.argv[2])
            regexops.GetCurrentProfile(sys.argv[2])
            exit(0)

        # Get a github USERS repositories
        if sys.argv[1] == '-g' and sys.argv[3] == "repos": #Record repo names
            dbops.WriteUserToDatabaseSILENTLY(sys.argv[2])
            repos = regexops.CollectRepositories(sys.argv[2])
            dbops.WriteUsersReposToFile(sys.argv[2], repos)

        # Get a github USERS starred repositories
        if sys.argv[1] == '-g' and s2 is True and s3 is True and sys.argv[3] == "starred":
            starred = regexops.CollectStarredRepos(sys.argv[2])
            # Record users bookmarks (what repose they have starred.)
            dbops.WriteUsersStarredReposToFile(sys.argv[2], starred)

        # Get a github USERS followers
        if sys.argv[1] == '-g' and sys.argv[3] == "followers":
            dbops.WriteUserToDatabaseSILENTLY(sys.argv[2])
            # Record a users followers
            followers = regexops.CollectFollowers(sys.argv[2])
            dbops.WriteUsersFollowersToFile(sys.argv[2], followers)

        # Get who a gith USER is following
        if sys.argv[1] == '-g' and sys.argv[3] == "following":
            dbops.WriteUserToDatabaseSILENTLY(sys.argv[2])
            # Record who a user is following
            following = regexops.CollectFollowing(sys.argv[2])
            dbops.WriteWhoUserIsFollowingToFile(sys.argv[2], following)

        # Get an organizations github repositories
        if sys.argv[1] == '-g' and sys.argv[2] == "org" and sys.argv[4] == "repos":
            dbops.WriteUserToDatabaseSILENTLY(sys.argv[3])
            # Record an organizations repositories
            orgrepos = regexops.CollectORGRepos(sys.argv[3])
            dbops.WriteOrgReposToFile(sys.argv[3], orgrepos)

        # Get an organizations github members
        if sys.argv[1] == '-g' and sys.argv[2] == "org" and sys.argv[4] == "ppl":
            dbops.WriteUserToDatabaseSILENTLY(sys.argv[3])
            # Record an organizations people/memebers
            orgpeople = regexops.CollectORGPEOPLE(sys.argv[3])
            dbops.WriteOrgPeopleToFile(sys.argv[3], orgpeople)

        if sys.argv[1] != '-g' and sys.argv[1] != 'ego' and sys.argv[1] != 'ping' and sys.argv[1] != '-a' and sys.argv[1] != 'help' and sys.argv[1] != '-h':
            Help()

    except IndexError:
        pass

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        Help()
