What's Parsero:
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
	 jnieto@behindthefirewalls:~/Parsero$ python parsero.py -u www.behindthefirewalls.com

	  ____                               
	 |  _ \ __ _ _ __ ___  ___ _ __ ___  
	 | |_) / _` | '__/ __|/ _ \ '__/ _ \ 
	 |  __/ (_| | |  \__ \  __/ | | (_) |
	 |_|   \__,_|_|  |___/\___|_|  \___/ 

	 Starting Parsero v0.4 (https://github.com/behindthefirewalls/Parsero) at 12/03/13 11:24:16
	 Parsero scan report for www.behindthefirewalls.com
	 www.behindthefirewalls.com 200 OK
	 www.behindthefirewalls.com/search 200 OK

	 Finished!!!


Disclaimer
==========
The use of this tools is your responsability. Use parsero to audit your own servers or servers which they have been given permission to scan. I hereby disclaim any responsibility for actions taken with this tool.


Author:
=======

    Javier Nieto | javier.nieto<@>behindthefirewalls.com
    Twitter: @behindfirewalls
  Web: http://www.behindthefirewalls.com
