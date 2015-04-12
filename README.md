# Easy Secrets
Perform OSINT on Github repos and users.

Platforms:
---------
- Linux

Basic Usage:
------------
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

Changelog:
----------.
- Added options.
- Added Keywords.
- Added Sections.
- Added database infrastructure.
- Added user database to mass collect usernames/ids
- Added the ability to collect & record all of a users followers ... etc.
- Added database components to ensure that information gets recorded appropriately.

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
