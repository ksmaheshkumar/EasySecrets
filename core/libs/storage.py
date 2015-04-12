#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

import os
import time
from paint import colors
from functions import utilities
from github import github, regexops

INFO = colors.W+"[INFO]"+colors.N + ": "
FAIL = colors.R+"[FAILED]"+colors.N + ": "
ERROR = colors.R+"[ERROR]"+colors.N + ": "
FOUND = colors.W+"[FOUND]"+colors.N + ": "

class DatabaseOpertaions():

    # QUERY/LOOKUP INFORMATION
    def QueryUserFollowingDatabase(self, username, followingname):
        username = username.lower()
        followingdatabasepath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/following/{}.following'.format(username)

        unidbool = followingname.isdigit() # smart case detection

        utilities.pi(" ")

        if unidbool is True:
            with open(followingdatabasepath, 'r') as file:

                # Database item check
                ic = utilities.sbc(followingdatabasepath, followingname) # Database item/name check
                for item in file:
                    itemlink = item.split(' - ')[2].replace("\n", '')
                    itemid = item.split(' - ')[0].replace("\n", '') # Link to github profile
                    item = item.split(' - ')[1] # github username
                    if followingname in item and ic is True:
                        utilities.pi("{}{}".format(FOUND, item + " - " + itemid + " - " + itemlink))
                        break

                    if ic is None:
                        utilities.pi("{}{} Not found in {}'s following database".format(FAIL, followingname, username))
                        break

        elif unidbool is False:
            with open(followingdatabasepath, 'r') as file:

                # Database item check
                ic = utilities.sbc(followingdatabasepath, followingname) # Database item/name check
                for item in file:
                    itemlink = item.split(' - ')[2].replace("\n", '')
                    itemid = item.split(' - ')[1].replace("\n", '') # Link to github profile
                    item = item.split(' - ')[0] # github username
                    if followingname in item and ic is True:
                        utilities.pi("{}{}".format(FOUND, item + " - " + itemid + " - " + itemlink))
                        break

                    if ic is None:
                        utilities.pi("{}{} Not found in {}'s following database".format(FAIL, followingname, username))
                        break
        utilities.pi(" ")

    def QueryUserFollowersDatabase(self, username, followername):
        username = username.lower()
        followersdatabasepath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/followers/{}.followers'.format(username)

        unidbool = followername.isdigit() # smart case detection

        utilities.pi(" ")
        if unidbool is True:
            with open(followersdatabasepath, 'r') as file:

                # Database item check
                ic = utilities.sbc(followersdatabasepath, followername) # Database item/name check
                for item in file:
                    itemlink = item.split(' - ')[2].replace("\n", '')
                    itemid = item.split(' - ')[0].replace("\n", '') # Link to github profile
                    item = item.split(' - ')[1] # github username
                    if followername in item and ic is True:
                        utilities.pi("{}{}".format(FOUND, item + " - " + itemid + " - " + itemlink))
                        break

                    if ic is None:
                        utilities.pi("{}{} Not found in {}'s followers database".format(FAIL, followername, username))
                        break

        if unidbool is False:
            with open(followersdatabasepath, 'r') as file:

                # Database item check
                ic = utilities.sbc(followersdatabasepath, followername) # Database item/name check
                for item in file:
                    itemlink = item.split(' - ')[2].replace("\n", '')
                    itemid = item.split(' - ')[1].replace("\n", '') # Link to github profile
                    item = item.split(' - ')[0] # github username
                    if followername in item and ic is True:
                        utilities.pi("{}{}".format(FOUND, item + " - " + itemid + " - " + itemlink))
                        break

                    if ic is None:
                        utilities.pi("{}{} Not found in {}'s followers database".format(FAIL, followername, username))
                        break
        utilities.pi(" ")

    def QueryUserRepoDatabase(self, username, reponame):
        username = username.lower()
        reposdatabasepath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/repositories/{}.repositories'.format(username)
        utilities.pi(" ")
        with open(reposdatabasepath, 'r') as file:
            # Database item check
            ic = utilities.sbc(reposdatabasepath, reponame) # Database item/name check
            for item in file:
                itemlink = item.split(' - ')[1].replace("\n", '') # Link to github profile
                item = item.split(' - ')[0] # github username
                if reponame in item and ic is True:
                    utilities.pi("{}{}".format(FOUND, item + " - " + itemlink))
                    break

                if ic is None:
                    utilities.pi("{}{} Not found in {}'s repository database".format(FAIL, reponame, username))
                    break
        utilities.pi(" ")

    def QueryUserDatabase(self, UNID):
        userdatabase = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/users/user.database'

        unidbool = UNID.isdigit() # smart case detection

        efb = os.stat(userdatabase).st_size == 0
        if efb is True:
            utilities.pi("{} User database is currently empty!".format(FAIL))
            exit(0)

        utilities.pi(" ")

        if unidbool is False:

            with open(userdatabase, 'r') as file:
                # Database item check
                ic = utilities.sbc(userdatabase, UNID) # Database item/name check
                for item in file:
                    itemlink = item.split(' - ')[2].replace("\n", '')
                    itemid = item.split(' - ')[1].replace("\n", '') # Link to github profile
                    item = item.split(' - ')[0] # github username
                    if UNID in item and ic is True:
                        utilities.pi("{}{}".format(FOUND, item + " - " + itemid + " - " + itemlink))
                        break

                    if ic is None:
                        utilities.pi("{}{} Not found in database".format(FAIL, UNID))
                        break

        elif unidbool is True:
            with open(userdatabase, 'r') as file:
                # Database item check
                ic = utilities.sbc(userdatabase, UNID) # Database item/name check
                for item in file:
                    itemlink = item.split(' - ')[2].replace("\n", '')
                    itemid = item.split(' - ')[0].replace("\n", '') # Link to github profile
                    item = item.split(' - ')[1] # github username
                    if UNID in item and ic is True:
                        utilities.pi("{}{}".format(FOUND, item + " - " + itemid + " - " + itemlink))
                        break

                    if ic is None:
                        utilities.pi("{}{} Not found in database".format(FAIL, UNID))
                        break
        utilities.pi(" ")

    # WRITE INFROMATION TO FILE
    def WriteActivity2File():
        # Record public activity.
        pass

    def WriteOrgPeopleToFile(self):
        pass

    def WriteUserProfileToFile(self, ID, FOE, FOI, ST, UNAME, RNAME, JOINED, PL, PP):
        UNAME = UNAME.lower()
        profilepath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/profiles/{}.profile'.format(UNAME.replace(' ', ""))
        with open(profilepath, 'w') as file: # May switch back to a+ ... w mode for now, to keep an up to date profile on queried user.
                #bc = utilities.sbc(profilepath, ID)
                #if bc is None:
                    #print line | for debugging rounds.
                file.write(github.GHID + ID + "\n")
                file.write(github.GHFE + FOE + "\n")
                file.write(github.GHFI + FOI + "\n")
                file.write(github.GHSR + ST + "\n")
                file.write(github.GHJD + JOINED + "\n")
                file.write(github.GHUN + UNAME + "\n")
                file.write(github.GHRN + RNAME + "\n")
                file.write(github.GHPL + PL + "\n")
                file.write(github.GHPP + PP[0] + "\n")

    def WriteUserToDatabaseSILENTLY(self, Username):
        Username = Username.lower()
        userdatabase = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/users/user.database'
        DNC = utilities.sbc(userdatabase, Username) # Database name check
        if DNC is True:
            pass

        IDN = regexops.GetUserID(Username)
        if IDN is None:
            utilities.pi("\n{}User doesn't exist.\n".format(ERROR, ))
            exit(0)

        databasepath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/users/user.database'
        with open(databasepath, 'a+') as file:
                bc = utilities.sbc(databasepath, Username)
                if bc is None:
                    #print line | for debugging rounds.
                    file.write(Username + " - " + str(IDN) + " - " + github.domain + Username + "\n")

                if bc is True:
                    pass

    def WriteUserToDatabaseVERBALLY(self, Username):
        Username = Username.lower()
        IDN = regexops.GetUserID(Username)

        if IDN is None:
            utilities.pi("\n{}User doesn't exist.\n".format(ERROR, ))
            exit(0)

        databasepath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/users/user.database'
        with open(databasepath, 'a+') as file:
                bc = utilities.sbc(databasepath, Username)
                if bc is None:
                    utilities.pi('\n{}Added {} to the user database.\n'.format(INFO, Username))
                    #print line | for debugging rounds.
                    file.write(Username + " - " + str(IDN) + " - " + github.domain + Username + "\n")
                if bc is True:
                    utilities.pi('\n{}{} has already been added to the user database.\n'.format(INFO, Username))

    def WriteWhoUserIsFollowingToFile(self, Username, Following):
        utilities.pi(INFO + "Collected {} users that {} is following".format(len(Following), Username))
        time.sleep(3)
        utilities.pi(INFO + "Writing {} to disk\n".format(len(Following), Username))
        Username = Username.lower() # Override any UPPERCASE strings
        followspath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/following/{}.following'.format(Username)
        with open(followspath, 'a+') as file:
            for line in Following:
                line = line.lower()
                bc = utilities.sbc(followspath, line)
                if bc is None:
                    #print line | for debugging rounds.
                    IDN = regexops.GetUserID(line)
                    if IDN is None:
                        IDN = "No Profile Traceroute."
                    file.write(line + " - " + IDN + " - " + github.domain + line + "\n")
        utilities.pi(INFO + "Wrote {} to disk".format(len(Following), Username))

    def WriteUsersFollowersToFile(self, Username, Followers):
        utilities.pi(INFO + "Collected {} of {}'s followers".format(len(Followers), Username))
        time.sleep(3)
        utilities.pi(INFO + "Writing {} of {}'s followers to disk".format(len(Followers), Username))
        Username = Username.lower()
        #os.chdir('..')
        followerspath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/followers/{}.followers'.format(Username)
        with open(followerspath, 'a+') as file:
            for line in Followers:
                line = line.lower()
                bc = utilities.sbc(followerspath, line)
                if bc is None:
                    #print line | for debugging rounds.
                    IDN = regexops.GetUserID(line)
                    if IDN is None:
                        IDN = "No Profile Traceroute."
                    file.write(line + " - " + IDN + " - " + github.domain + line + "\n")
        utilities.pi(INFO + "Wrote {} of {}'s followers to disk.\n".format(len(Followers), Username))

    def WriteUsersReposToFile(self, Username, Repos):
        utilities.pi(INFO + "Collected {} of {}'s Repositories".format(len(Repos), Username))
        time.sleep(3)
        utilities.pi(INFO + "Wrote {} of {}'s Repositories to disk\n".format(len(Repos), Username))
        idwe = 'https://github.com'
        Username = Username.lower()
        repospath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/repositories/{}.repositories'.format(Username)
        with open(repospath, 'a+') as file:
            for line in Repos:
                line = line.lower()
                bc = utilities.sbc(repospath, line)
                if bc is None:
                    #print line | for debugging rounds.
                    reponame = line.split('/')[2]
                    file.write(reponame + " - " + idwe + line + "\n")

    def WriteUsersStarredReposToFile(self, Username, Repos):
        utilities.pi(INFO + "Collected {} of {}'s Starred Repositories".format(len(Repos), Username))
        time.sleep(3)
        utilities.pi(INFO + "Writing {} of {}'s Starred Repositories to disk\n".format(len(Repos), Username))
        idwe = 'https://github.com'
        Username = Username.lower()
        repospath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/core/database/repositories/starred/{}.starred.repos'.format(Username)
        with open(repospath, 'a+') as file:
            for line in Repos:
                line = line.lower()
                bc = utilities.sbc(repospath, line)
                if bc is None:
                    #print line | for debugging rounds.
                    reponame = line.split('/')[2]
                    file.write(reponame + " - " + idwe + line + "\n")
        utilities.pi(INFO + "Wrote {} of {}'s Starred Repositories to disk\n".format(len(Repos), Username))
dbops = DatabaseOpertaions()
