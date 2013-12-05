What's Parsero?
===============
Parsero is a free script written in Python which read the Robots.txt file of a web server and look at the Disallow entries. The Disallow entries are the URL path of directories or files hosted on the web server which the administrators don't want they be indexed by the crawlers. For example, "Disallow: /portal/login" don't allow to "www.example.com/portal/login" be indexed by the search engines like Google, Bing, Yahoo... in order nobody locate it seeking on them.

Sometimes these paths typed in the Disallows entries  are directly accessible by the users (without using a search engine) just visiting the URL and the path, even sometimes they are not available to be visited by anybody... Because it is really common that the administrators write a lot of Disallows in the Robots.txt and some of them are available and some of them are not, you can use Parsero in order to check the HTTP status code of each Disallow entry in order to check automatically if these directories are available or not. 

When you execute Parsero, you can see the HTTP status codes. For example, the codes bellow:


    200 OK          The request has succeeded.
    403 Forbidden   The server understood the request, but is refusing to fulfill it.
    404 Not Found   The server hasn't found anything matching the Request-URI.
    302 Found       The requested resource resides temporarily under a different URI.
    ...
    ...
    ...

Installing:
==========
This tool needs at least Python3 and urllib3.
        
        sudo apt-get install python3
        sudo apt-get install python-pip
        sudo pip install urllib3
        
Make sure that your default version of Python is 3 or later. If you don't want to change your default version, you can execute typing $ python3.3 parsero (if this version has been installed) instead of $ python parsero.


Usage:
======
        $ python3.3 parsero.py -h
        
        usage: parsero.py [-h] [-u URL]
        
        optional arguments:
        -h, --help  show this help message and exit
        -u URL      Type the URL which will be analyzed

Example:
=======
	 
        jnieto@behindthefirewalls:~/Parsero$ python3.3 parsero.py -u www.example.com
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

  Javier Nieto
  
  eMail: javier.nieto<@>behindthefirewalls.com
  
  Twitter: @behindfirewalls
  
  Web: http://www.behindthefirewalls.com
  

