# Easy Secrets
Perform OSINT on Github users and organizations.

Platforms:
---------
- Linux cli

Report a bug:
-------------
https://github.com/GuerrillaWarfare/EasySecrets/issues

Protip:
-------
- When querying a database, a "keyword" is something or someone you're looking for.
- Record the information you want, then query the database for it.

Basic Usage:
------------
    # Global operations
    -----------------------
    ./es.py ego [USERNAME]| Get the profile of a user. (Doesn't work on Organizations.)

    ./es.py -a [USERNAME]| Add a username to the user database.

    ./es.py ping [USERNAME] OR ID number | query the user database for a username.

          OR

    # User query operations
     -----------------------
    ./es.py ping [USERNAME] [SECTION] [KEYWORD]

    | Section: repo      | query a users repo database for a repo name.
    | Section: followers | query a users followers database for a username that follows the user.
    | Section: following | query a users following database for a user that the user is following.
    | Section: starred   | query a users starred repo database for a repo name they have bookmarked.

    # User offensive operations
    -----------------------
    ./es.py -g [USERNAME] [KEYWORD] | Get something from a user.

    | Keyword: repos     | Record all the repos a user has.
    | Keyword: followers | Record all the followers a user has.
    | Keyword: starred   | Record all repos a user has bookmarked.
    | Keyword: following | Record all the accounts a user is following.

          OR

    # Organiztaon query operations
     ------------------------------
    ./es.py ping org [ORGNAME] [SECTION] [KEYWORD]

    | Section: repo      | query an organizations repo database for a repo name.
    | Section: ppl       | query an organizations people database for a user or user id.

    # Organization offensive operations
    --------------------------------------
    ./es.py -g org [ORGNAME][KEYWORD] | Get something from an organization.

    | Keyword: repos     | Record all the repos an organization has.
    | Keyword: ppl       | Record all the people an organization has.

Changelog:
----------
- Added more options.
- Added the ability to record an organizations people (members).
- Added the ability to record an organizations repositories.

Python Dependencies:
--------------------
1. python2
2. requests | pip install requests

Guerrilla Warfare Free License ("GWFL"):
----------------------------------------
- You're free to modify this software to YOUR liking or leave it as is.
- This software comes as is, and may or may not receive any additional updates, Contact the developer for help.
- The initial download and use of this software constitutes that you adhere and comply to the writing of this EULA.
- The Developer is NOT at ALL under any circumstances responsible for YOUR actions or the actions of any other third party instances that may use this software for any illegal or nefarious activities.
