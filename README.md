Here, you can get all the info about Parsero updated:

http://www.behindthefirewalls.com/search/?q=parsero
What's Parsero?
===============
Parsero is a free script written in Python which reads the Robots.txt file of a web server and looks at the Disallow entries. The Disallow entries are the URL path of directories or files hosted on a web server which the administrators don't want to be indexed by the crawlers. For example, "Disallow: /portal/login" don't allow to www.example.com/portal/login be indexed by the search engines like Google, Bing, Yahoo... so nobody can locate it when searching on them.

Sometimes these paths typed in the Disallows entries  are directly accessible by the users (without using a search engine) just visiting the URL and the Path and sometimes they are not available to be visited by anybody... Because it is really common that the administrators write a lot of Disallows and some of them are available and some of them are not, you can use Parsero in order to check the HTTP status code of each Disallow entry in order to check automatically if these directories are available or not.

When you execute Parsero, you can see the HTTP status codes. For example, the codes bellow:


    200 OK          The request has succeeded.
    403 Forbidden   The server understood the request, but is refusing to fulfill it.
    404 Not Found   The server hasn't found anything matching the Request-URI.
    302 Found       The requested resource resides temporarily under a different URI.
    ...

Also, that the administrator write a robots.txt, it doesn't mean that the files or direcotories typed in this file will not be indexed by Bing, Google, Yahoo... For this reason, Parsero is capable of searching in Bing to locate content indexed whithout the web administrator authorization.

Installing:
==========
This tool needs at least Python3 and urllib3.
       
    sudo apt-get install python3
    sudo apt-get install python3-pip
    sudo pip-3.3 install urllib3
    sudo pip-3.2 install beautifulsoup4
        
Make sure that your default version of Python is 3 or later. If you don't want to change your default version, you can execute typing $ python3.3 parsero (if this version has been installed) instead of $ python parsero.

Usage:
======
    $ python3.3 parsero.py -h
        
    usage: parsero.py [-h] [-u URL] [-o] [-sb]
	
    optional arguments:
    -h, --help  show this help message and exit
    -u URL      Type the URL which will be analyzed
    -o          Show only the "HTTP 200" status code
    -sb         Search in Bing indexed Disallows


Example:
=======
	 
    root@kali:~/my-tools/Parsero# python3.2 parsero.py -u www.example.com -sb

         ____                               
        |  _ \ __ _ _ __ ___  ___ _ __ ___  
        | |_) / _` | '__/ __|/ _ \ '__/ _ \ 
        |  __/ (_| | |  \__ \  __/ | | (_) |
        |_|   \__,_|_|  |___/\___|_|  \___/ 

        Starting Parsero v0.6 (https://github.com/behindthefirewalls/Parsero) at 02/05/14 12:35:00
        Parsero scan report for www.example.com
        www.example.com 301 MOVED PERMANENTLY
        www.example.com/s/ 301 MOVED PERMANENTLY
        www.example.com/sh/ 301 MOVED PERMANENTLY
        www.example.com/static/ 403 Forbidden
        www.example.com/gallery/ 301 MOVED PERMANENTLY
        www.example.com/connect 500 Internal Server Error
        www.example.com/invite 500 Internal Server Error
        www.example.com/invite_register 500 Internal Server Error
        www.example.com/m/invite 301 MOVED PERMANENTLY

        [+] 9 links have been analyzed but any them are available...

        Searching the Disallows entries in Bing...

        http://www.bing.com/search?q=site:www.example.com/s/
         - https://www.example.com/s/tokfd9t86rbbstp/os2.pdf
         - https://www.example.com/s
         - https://www.example.com/s/ikq8r518nwrf443/vegemesta_placeholder.png
         - https://www.example.com/s/g2fg906npzk0in4/acca-f5-study-text-ebook...
         - https://www.example.com/s/pk4s3mxsgtrjl8q/acca-f2-study-text-ebook...
         - https://www.example.com/s/wklmsfph99ylycp/acca-p3-study-text-ebook...
         - https://www.example.com/s/5vqgh090jnh5h6i/acca-p1-study-text-ebook...
         - https://www.example.com/s/c4fw5qwt8dgx4j8/os2_01.pdf
         - https://www.example.com/s/ikq8r518nwrf443/vegemesta_placeholder...
        http://www.bing.com/search?q=site:www.example.com/sh/
         - https://www.example.com/sh/7rirtejc4vgjyqb/LtF_Brb_c0
         - https://www.example.com/sh/e2qwi6va030grv9/AdEqTi5KE5?n=51225956
         - https://www.example.com/sh/arg9xnf0spr36i5/hPe0llAPw4
        http://www.bing.com/search?q=site:www.example.com/connect
        http://www.bing.com/search?q=site:www.example.com/invite
        http://www.bing.com/search?q=site:www.example.com/invite_register
        http://www.bing.com/search?q=site:www.example.com/m/invite

        Finished in 9.444016933441162 seconds



Disclaimer
==========
The use of this tools is your responsability. Use parsero to audit your own servers or servers which they have been given permission to scan. I hereby disclaim any responsibility for actions taken with this tool.


Author:
=======

  Javier Nieto
  
  eMail: javier.nieto<@>behindthefirewalls.com
  
  Twitter: @behindfirewalls
  
  Web: http://www.behindthefirewalls.com
  

