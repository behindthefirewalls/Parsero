What's Parsero?
===============
Parsero is a free script which read the Robots.txt file of a web server and look at the Disallow entries. Then it 
visits these entries and prints the status code in order to show you which of them are available and which not.

Installing:
==========
This tool needs at least Python3 and urllib3.
        
        sudo apt-get install python3
        sudo apt-get install python-pip
        sudo pip install urllib3

Usage:
======
        $ python3 parsero.py -h
        
        usage: parsero.py [-h] [-u URL]
        
        optional arguments:
        -h, --help  show this help message and exit
        -u URL      Type the URL which will be analyzed

Example:
=======
	 
	 jnieto@behindthefirewalls:~/Parsero$ python parsero.py -u www.example.com
		  ____                               
		 |  _ \ __ _ _ __ ___  ___ _ __ ___  
		 | |_) / _` | '__/ __|/ _ \ '__/ _ \ 
		 |  __/ (_| | |  \__ \  __/ | | (_) |
		 |_|   \__,_|_|  |___/\___|_|  \___/ 
	
	Starting Parsero v0.45 (https://github.com/behindthefirewalls/Parsero) at 12/03/13 15:56:43
	Parsero scan report for www.example.com
	www.example.com/includes/ 403 Forbidden
	www.example.com/misc/ 403 Forbidden
	www.example.com/modules/ 403 Forbidden
	www.example.com/profiles/ 403 Forbidden
	www.example.com/scripts/ 403 Forbidden
	www.example.com/themes/ 403 Forbidden
	www.example.com/sites/ 403 Forbidden
	www.example.com/CHANGELOG.txt 200 OK
	www.example.com/cron.php 200 OK
	www.example.com/INSTALL.mysql.txt 200 OK
	www.example.com/INSTALL.pgsql.txt 200 OK
	www.example.com/install.php 200 OK
	www.example.com/INSTALL.txt 200 OK
	www.example.com/LICENSE.txt 200 OK
	www.example.com/MAINTAINERS.txt 200 OK
	www.example.com/update.php 302 Found
	www.example.com/UPGRADE.txt 200 OK
	www.example.com/xmlrpc.php 200 OK
	www.example.com/admin/ 403 Forbidden
	www.example.com/comment/reply/ 404 Not Found
	www.example.com/logout/ 403 Forbidden
	www.example.com/node/add/ 403 Forbidden
	www.example.com/search/ 200 OK
	www.example.com/user/register/ 403 Forbidden
	www.example.com/user/password/ 404 Not Found
	www.example.com/user/login/ 200 OK
	www.example.com/?q=admin/ 403 Forbidden
	www.example.com/?q=comment/reply/ 404 Not Found
	www.example.com/?q=logout/ 403 Forbidden
	www.example.com/?q=node/add/ 403 Forbidden
	www.example.com/?q=search/ 200 OK
	www.example.com/?q=user/password/ 404 Not Found
	www.example.com/?q=user/register/ 403 Forbidden
	www.example.com/?q=user/login/ 200 OK
	
	Finished!!!



Disclaimer
==========
The use of this tools is your responsability. Use parsero to audit your own servers or servers which they have been given permission to scan. I hereby disclaim any responsibility for actions taken with this tool.


Author:
=======

    Javier Nieto | javier.nieto<@>behindthefirewalls.com
    Twitter: @behindfirewalls
  Web: http://www.behindthefirewalls.com
