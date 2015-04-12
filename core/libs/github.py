#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

import re
import time
import storage # Database operations # Auto Write to database
from paint import colors
from functions import utilities

# Dependency import
import requests

INFO = colors.W+"[INFO]"+colors.N + ": "
FAIL = colors.R+"[FAILED]"+colors.N + ": "
ERROR = colors.R+"[ERROR]"+colors.N + ": "

GLOBALUSERAGENT = {"User-Agent":"Mozilla/5.0 (X11; Linux x86; rv:37.0) Gecko/20100101 Firefox/40.0"}

class GITHUB():
    #Github tab & edges.

    domain  = 'https://github.com/'
    repotab = '/repositories' # repositories edge.
    activitytab = '?tab=activity'
    followerstab = '/followers' # followers edge

    # Github output global variables.
    GHID = 'ID: '
    GHNR = "Repos: "
    GHSR = "Starred repos: "
    GHUN = "Username: "
    GHRN = "Real Name: "
    GHPP = "Profile Picture: "
    GHOC = "Company: "
    GHOB = "Blog: "
    GHOE = "Email: "
    GHOL = "Location: "
    GHPL = "Profile Link: "
    GHFE = "Followers: "
    GHFI = "Following: "
    GHJD = "Joined: "

github = GITHUB() # Never call this class outside of this module.

class REGEXRESPONSES():


    # USER OPERATIONAL FUNCTIONS!
    def GetUserRepoActivity(self):
        pass

    def GetWhenUserJoined(self, USERNAME):
        link2profile = github.domain + USERNAME
        response = utilities.GetHTTPRequest(link2profile)
        try:
            if response.status_code == 404:
                utilities.pi("{}User not found!".format(ERROR))
                return None
                exit(0)

            jdc = re.findall(r'<time class="join-date".*?>(.*)</time>', response.text)
            jd = jdc[0]
            return jd
        except IndexError:
            return None

    def GetRepoNames(self , url):
        # gets repo names/links
        response = utilities.GetHTTPRequest(url).text.encode('utf-8')
        s = re.findall(r'<h3 .*?</h3>', response, re.DOTALL)
        c = 0
        l = []
        for i in s:
            e = re.findall(r'<a .*?</a>', i, re.DOTALL)
            for x in e:
                p = re.findall(r'href=".*"', x)
                for item in p:
                    item = item.replace('href=', '').replace('"', '')
                    l.append(item)
        return l

    def GetCurrentProfile(self, USERNAME):
        # Provide output for a users GithubProfile
        try:
            ID = regexops.GetUserID(USERNAME)
            if ID is None:
                raise KeyError

            utilities.pi("\n{}Attempting to generate {}'s github profile information\n".format(INFO, USERNAME))
            link2profile = github.domain + USERNAME
            contentdish = utilities.GetHTTPRequest(link2profile).text.encode('utf-8')
            PFP = regexops.GetProfilePicture(contentdish) # Link to user profile picture
            #NOR = str(regexops.GetNumberOfRepos(USERNAME)) # Number of repos
            NOSR = str(regexops.GetNumberOfUserStarredRepos(USERNAME)) # Number of Starred repos
            LINK = regexops.GetProfileLink(USERNAME)
            BLOG = regexops.GetOwnerBlog(USERNAME)
            #EMAIL = github.GetOwnerEmail(USERNAME)
            COMPANY = regexops.GetOwnerCompany(USERNAME)
            PFUNAME = regexops.GetOwnerUserName(USERNAME)
            REALNAME = regexops.GetOwnerRegularName(USERNAME)
            LOCATION = regexops.GetOwnerLocation(USERNAME)
            FOLLOWERS = str(regexops.GetNumberOfUserFollowers(USERNAME))
            FOLLOWING = str(regexops.GetNumberOfWhoUserIsFollowing(USERNAME))
            JOINED = regexops.GetWhenUserJoined(USERNAME)

            # Write the information to Database
            storage.dbops.WriteUserProfileToFile(ID, FOLLOWERS, FOLLOWING, NOSR, PFUNAME, REALNAME, JOINED, LINK, PFP)

            #Output the info
            utilities.pi(github.GHID + str(ID)) # ID
            #utilities.pi(GHNR + NOR) # Number of repos
            utilities.pi(github.GHFE + FOLLOWERS) # Number of follwers a user has.
            utilities.pi(github.GHFI + FOLLOWING) # Number of peole who a user is following.
            utilities.pi(github.GHSR + NOSR) # Number of starred repos

            if JOINED != None:
                utilities.pi(github.GHJD + JOINED) # When User joined github

            utilities.pi(github.GHUN + PFUNAME) # Username of account
            utilities.pi(github.GHRN + REALNAME) # Real name of account, may return username.

            if COMPANY != None:
                utilities.pi(github.GHOC + COMPANY) # Company

            if BLOG != None:
                utilities.pi(github.GHOB + BLOG) # Blog address

            #if LOCATION != None: # Must fix.
                #utilities.pi(GHOL + LOCATION) # Location | May sometimes be the blog address.

            utilities.pi(github.GHPL + LINK) # Profile Link
            utilities.pi(github.GHPP + PFP[0]) # Profile picture

            print ""
        except KeyError:
            utilities.pi("{}User not found!".format(INFO))
            exit(0)

    def GetProfileLink(self, USERNAME):
        username = regexops.GetOwnerUserName(USERNAME)
        link = github.domain + username
        return link

    def GetOwnerEmail(self, USERNAME):
        # Returns VERY BUGGY/Non-decodable Email string.
        # WILL NOT USE ATM.
        link2profile = github.domain + USERNAME
        response = utilities.GetHTTPRequest(link2profile).text
        ec = re.findall(r'<span class="octicon octicon-mail">.*</a>', response)
        email = ec[0]
        print email
        #if "@" in email:
        #    return email.replace('</span>', '').replace('</li>', '')
        #else:
        #    return None

    def GetOwnerBlog(self, USERNAME):
        # CAN ONLY BE USED WITH OWNER PROFILE
        try:
            link2profile = github.domain + USERNAME
            response = utilities.GetHTTPRequest(link2profile).text.encode('utf-8')
            ic = re.findall(r'</span>.*</li>', response)
            blc = re.findall(r'">.*?</a>', ic[2])
            bl =  blc[0].replace('">', '').replace('</a>', '')
            return bl
        except IndexError:
            return None

    def GetOwnerLocation(self, USERNAME):
        # CAN ONLY BE USED WITH OWNER PROFILE
        link2profile = github.domain + USERNAME
        response = utilities.GetHTTPRequest(link2profile).text.encode('utf-8')
        lc = re.findall(r'</span>.*</li>', response)
        location = lc[1]
        if "@" in location:
            return None
        else:
            return location.replace('</span>', '').replace('</li>', '')

    def GetOwnerCompany(self, USERNAME):
        # CAN ONLY BE USED WITH OWNER PROFILE
        link2profile = github.domain + USERNAME
        response = utilities.GetHTTPRequest(link2profile).text.encode('utf-8')
        ic = re.findall(r'</span>.*</li>', response)
        company = ic[0].replace('</span>', '').replace('</li>', '')
        if "@" in company:
            return company
        else:
            return None

    def GetOwnerRegularName(self, USERNAME):
        # CAN BE USE FOR ANY SPECIFIC USER OP.
        link2profile = github.domain + USERNAME
        response = utilities.GetHTTPRequest(link2profile).text.encode('utf-8')
        repo_owner_regularname_regex = re.search(r'<title>.*?</title>', response)
        RepoOwnerRegularName = repo_owner_regularname_regex.group(0).replace('<title>', '').replace('</title>', '').split("·")[0].split('/')[0].split('(')[1]
        return RepoOwnerRegularName.replace(')', '')

    def GetOwnerUserName(self, USERNAME):
        #Get the username through regex.
        # CAN BE USE FOR ANY SPECIFIC USER OP.
        link2profile = github.domain + USERNAME
        response = utilities.GetHTTPRequest(link2profile).text.encode('utf-8')
        repo_owner_username_regex = re.search(r'<title>.*?</title>', response)
        RepoOwnerUserName = repo_owner_username_regex.group(0).replace('<title>', '').replace('</title>', '').split("·")[0].split('/')[0].split('(')[0]
        return RepoOwnerUserName

    def GetProfilePicture(self, content):
        # CAN ONLY BE USED ON PROFILES, FOLLOWERS, FOLLOWING pages.
        ppc = re.findall(r'https://.*githubusercontent.com/u/.*v=', content)
        picturelinks = []
        for pic in ppc:
            pic = pic.replace('?v=', '')
            picturelinks.append(pic)
        return picturelinks # Return the profile link in it's entirety.

    def GetNamesOfFollowing(self, url):
        # ONLY WORKS WHEN /followers edge is present in link
        # Grab the user names of a users followers.
        content = utilities.GetHTTPRequest(url).text
        s = re.findall(r'<li class="follow-list-item">\n.*', content)
        lol = len(s) # Funny dynamic changing list length.
        followers = []
        for i in s[0:lol]:
            d = re.findall(r' <a href="/.*">', i)
            follower = d[0].replace(' <a href="/', '').replace('">', '')
            followers.append(follower)
        return followers

    def CollectStarredRepos(self, USERNAME):
        try:
            #print ""
            #FollowersNumber = regexops.GetNumberOfUserFollowers(USERNAME)
            utilities.pi('\n{}Attempting to collect all of {}\'s starred repositories'.format(INFO, USERNAME))
            d = regexops.GrabNextPageOfStarredRepos("https://github.com/stars/{}".format(USERNAME))
            p = [] # pages visited
            p.append("https://github.com/stars/{}".format(USERNAME))
            f = [] # list of followers, the container
            #return p
            while True:
                if d is None: # If there is only ONE page of followers
                    for s in p:
                        d = regexops.GetRepoNames(s)
                        for i in d:
                            f.append(i)
                        return f
                # If there is more than one page of followers.
                for o in p:
                    time.sleep(1)
                    if o is None:
                        p.remove(p[-1])
                        for z in p:
                            n = regexops.GetRepoNames(z)
                            for so in n:
                                f.append(so)
                        return f
                    o = regexops.GrabNextPageOfStarredRepos(o)
                    p.append(o)
                    print p
                    #print p | for debugging
                #return p | for debugging

        except TypeError:
            pass

    def GetNamesOfFollowers(self, url):
        # ONLY WORKS WHEN /followers edge is present in link
        # Grab the user names of a users followers.
        content = utilities.GetHTTPRequest(url).text
        s = re.findall(r'<li class="follow-list-item">\n.*', content)
        lol = len(s) # Funny dynamic changing list length.
        followers = []
        for i in s[0:lol]:
            d = re.findall(r' <a href="/.*">', i)
            follower = d[0].replace(' <a href="/', '').replace('">', '')
            followers.append(follower)
        return followers

    def GrabNextPageOfFollowing(self, url):
        # Content Extractor
        # Grab the next page of followers if there are more than one.
        try:
            url = utilities.GetHTTPRequest(url).text
            nplc = re.search(r'href="https://github.com/.*/following.*"' , url)
            nplc1 = nplc.group().replace('rel="nofollow">Previous</a>', '').replace('rel="nofollow"', '').replace('<a href="', '')
            nplc2 = nplc1.replace('href="', '').replace('"', '')
            npl  = nplc2.split(' ')[0:2] # Remove the empty item
            np = npl
            if np[1] == '':
                return np[0]

            elif np[1] == '<span': # Will return None
                return None

            else:
                return np[1]
        except AttributeError:
            return None

    def GrabNextPageOfStarredRepos(self, url):
        # Content Extractor
        # Grab the next page of followers if there are more than one.

        il = 'https://github.com'
        content = utilities.GetHTTPRequest(url).text
        nplc = re.findall(r'<a href="https://github.com/stars/.*direction=desc&amp;page=.*&amp;sort=created" .*>Next</a>' , content)
        try:
            nplc1 = nplc[0].replace('<a href="', '').replace('amp;', '').replace('" rel="nofollow">Next</a>', '')
        except IndexError:
            return None

        nplc2 = nplc1.replace('rel="nofollow">Previous</a>', '').replace('"', '')
        np = nplc2.split(' ')
        try:
            if np[1] == '<span':
                return None
            else:
                return np[1]
        except IndexError:
            return np[0]

    def GrabNextPageOfRepos(self, url):
        # Content Extractor
        # Grab the next page of followers if there are more than one.
        try:
            il = 'https://github.com'
            content = utilities.GetHTTPRequest(url).text
            nplc = re.search(r'<a class="next_page" rel="next" href="/.*/repositories.*">Next</a>' , content)
            nplc1 = nplc.group().replace('<a class="next_page" rel="next" href="', '').replace('">Next</a>', '')
            np = il + nplc1
            return np
        except AttributeError:
            return None

    def CollectRepositories(self, USERNAME):
        try:
            #print ""
            #FollowersNumber = regexops.GetNumberOfUserFollowers(USERNAME)
            utilities.pi('\n{}Attempting to collect all of {}\'s github repositories'.format(INFO, USERNAME))
            d = regexops.GrabNextPageOfRepos("https://github.com/{}/repositories".format(USERNAME))
            p = [] # pages visited
            p.append("https://github.com/{}/repositories".format(USERNAME))
            f = [] # list of followers, the container
            #return p
            while True:
                if d is None: # If there is only ONE page of followers
                    for s in p:
                        d = regexops.GetRepoNames(s)
                        for i in d:
                            f.append(i)
                        return f
                # If there is more than one page of followers.
                for o in p:
                    time.sleep(1)
                    if o is None:
                        p.remove(p[-1])
                        for z in p:
                            n = regexops.GetRepoNames(z)
                            for so in n:
                                f.append(so)
                        return f
                    o = regexops.GrabNextPageOfRepos(o)
                    p.append(o)
                    #print p | for debugging
                #return p | for debugging

        except TypeError:
            pass

    def CollectFollowing(self, USERNAME):
        try:
            #print ""
            #FollowingNumber = regexops.GetNumberOfWhoUserIsFollowing(USERNAME)
            utilities.pi('\n{}Attempting to collect all users that {} is following on github'.format(INFO ,USERNAME))
            d = regexops.GrabNextPageOfFollowing("https://github.com/{}/following".format(USERNAME))
            p = [] # pages visited
            p.append("https://github.com/{}/following".format(USERNAME))
            f = [] # list of followers, the container
            #return p
            while True:
                if d is None: # If there is only ONE page of followers
                    for s in p:
                        d = regexops.GetNamesOfFollowing(s)
                        for i in d:
                            f.append(i)
                        return f
                # If there is more than one page of followers.
                for o in p:
                    time.sleep(1)
                    if o is None:
                        p.remove(p[-1])
                        for z in p:
                            n = regexops.GetNamesOfFollowing(z)
                            for so in n:
                                f.append(so)
                        return f
                    o = regexops.GrabNextPageOfFollowing(o)
                    p.append(o)
                    #print p | for debugging
                #return p | for debugging

        except TypeError:
            pass

    def GrabNextPageOfFollowers(self, url):
        # Content Extractor
        # Grab the next page of followers if there are more than one.
        try:
            url = utilities.GetHTTPRequest(url).text
            nplc = re.search(r'href="https://github.com/.*/followers.*"' , url)
            nplc1 = nplc.group().replace('rel="nofollow">Previous</a>', '').replace('rel="nofollow"', '').replace('<a href="', '')
            nplc2 = nplc1.replace('href="', '').replace('"', '')
            npl  = nplc2.split(' ')[0:2] # Remove the empty item
            np = npl
            if np[1] == '':
                return np[0]

            elif np[1] == '<span': # Will return None
                return None

            else:
                return np[1]
        except AttributeError:
            return None

    def CollectFollowers(self, USERNAME):
        try:
            #print ""
            FollowersNumber = regexops.GetNumberOfUserFollowers(USERNAME)
            utilities.pi('\n{}Attempting to collect {} of {}\'s github followers'.format(INFO, FollowersNumber ,USERNAME))
            d = regexops.GrabNextPageOfFollowers("https://github.com/{}/followers".format(USERNAME))
            p = [] # pages visited
            p.append("https://github.com/{}/followers".format(USERNAME))
            f = [] # list of followers, the container
            #return p
            while True:
                if d is None: # If there is only ONE page of followers
                    for s in p:
                        d = regexops.GetNamesOfFollowers(s)
                        for i in d:
                            f.append(i)
                        return f
                # If there is more than one page of followers.
                for o in p:
                    time.sleep(1)
                    if o is None:
                        p.remove(p[-1])
                        for z in p:
                            n = regexops.GetNamesOfFollowers(z)
                            for so in n:
                                f.append(so)
                        return f
                    o = regexops.GrabNextPageOfFollowers(o)
                    p.append(o)
                    #print p | for debugging
                #return p | for debugging

        except TypeError:
            #utilities.pi(INFO + 'User Doesn\'t exist.')
            #exit(0)
            pass

    def GetUserIDS(self, response):
        # CAN ONLY BE USED ON FOLLOWERS, FOLLOWING pages.
        # OWNERS id is at list[0]
        idc1 = re.findall(r'.githubusercontent.com/u/.*v=', response)
        loids = []
        for c in idc1:
            c = c.replace('?v=', '').replace('.githubusercontent.com/u/', '')
            loids.append(c)
        return loids

    def GetUserID(self, USERNAME):
        # WILL WORK ON ONLY ONE PERSON
        try:
            link2profile = github.domain + USERNAME
            response = utilities.GetHTTPRequest(link2profile)
            if response.status_code is 404:
                return None
            idc = re.search(r'.githubusercontent.com/u/.*v=', response.text.encode('utf-8'))
            idn = idc.group(0).replace('?v=', '').replace('.githubusercontent.com/u/', '')
            return idn
        except Exception:
            return None

    def GetNumberOfUserStarredRepos(self, USERNAME):
        # Must be set to users profile page.
        link2profile = github.domain + USERNAME
        response = utilities.GetHTTPRequest(link2profile).text.encode('utf-8')
        p = re.findall(r'<a class="vcard-stat" href="/stars.*">\n.*<', response)
        sus = re.findall(r'<strong class="vcard-stat-count">.*<', p[0])[0].replace('<strong class="vcard-stat-count">', '').replace('<', '')
        return sus

    def GetNumberOfWhoUserIsFollowing(self, USERNAME):
        link2profile = github.domain + USERNAME
        response = utilities.GetHTTPRequest(link2profile).text.encode('utf-8')
        p = re.findall(r'<a class="vcard-stat" href="/.*/following">\n.*<', response)
        wtuifs = re.findall(r'<strong class="vcard-stat-count">.*<', p[0])[0].replace('<strong class="vcard-stat-count">', '').replace('<', '')
        return wtuifs

    def GetNumberOfUserFollowers(self, USERNAME):
        link2profile = github.domain + USERNAME
        response = utilities.GetHTTPRequest(link2profile).text.encode('utf-8')
        p = re.findall(r'<a class="vcard-stat" href="/.*/followers">\n.*<', response)
        fs = re.findall(r'<strong class="vcard-stat-count">.*<', p[0])[0].replace('<strong class="vcard-stat-count">', '').replace('<', '')
        return fs

    def GetNumberOfRepos(self, USERNAME):
        # Returns the number of repos on a given page.
        link2profile = github.domain + USERNAME + github.repotab
        response = utilities.GetHTTPRequest(link2profile).text.encode('utf-8')
        s = re.findall(r'<h3 .*?</h3>', response, re.DOTALL)
        c = 0
        l = []
        for i in s:
            e = re.findall(r'<a .*?</a>', i, re.DOTALL)
            for x in e:
                l.append(x)
        return len(l) # The final count of the number of repos for a given page.

    # Repo OPs Section.
    def GetRepoName(self, REPOHTML):
        # ONLY FOR REPO GIVEN LINKS
        # https://github.com/GuerrillaWarfare/TiM
        repo_name_regex = re.search(r'<title>.*?</title>', REPOHTML)
        RepoName = repo_name_regex.group(0).replace('<title>', '').replace('</title>', '').split("·")[0].split('/')[1]
        return RepoName

    def GetRepoOwnerName(self, REPOHTML):
        # Get who ever the repo belongs to.
        # ONLY FOR REPO GIVEN LINKS
        repo_owner_name_regex = re.search(r'<title>.*?</title>', REPOHTML)
        RepoOwnerName = repo_owner_name_regex.group(0).replace('<title>', '').replace('</title>', '').split("·")[0].split('/')[0]
        return RepoOwnerName

    def MakeLink2RepoOwner(self, REPOHTML):
        Link2Owner = github.domain + github.GetRepoOwnerName(REPOHTML)
        return Link2Owner

regexops = REGEXRESPONSES()
