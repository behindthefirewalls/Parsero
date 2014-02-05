#!/usr/bin/python3
# -*- coding: utf-8 -*-

__license__="""

Parsero is a free script which read the Robots.txt file of a web server and look at the Disallow entries. Then it 
visits these entries and prints the status code in order to show you which of them are available and which not.

Author:
	Javier Nieto | javier.nieto@behindthefirewalls.com
	Twitter: @behindfirewalls
	Web: www.behindthefirewalls.com

	Parsero project site: https://github.com/behindthefirewalls/Parsero

	This program is free software; you can redistribute it and/or
	modify it under the terms of the GNU General Public License
	as published by the Free Software Foundation; either version 2
	of the License, or (at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program; if not, write to the Free Software
	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

	The authors disclaims all responsibility in the use of this tool.

	"""

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    YELLOW = '\033[33m'

    def disable(self):
            self.OKGREEN = ''
            self.FAIL = ''
            self.ENDC = ''

<<<<<<< HEAD
=======

>>>>>>> 0ad335f2139e316c3ebec781a98a6468e62b62c9
import sys

if sys.version_info<(3,0,0):
	print("\n" + bcolors.FAIL + "You need Python3 or later to run this script." + bcolors.ENDC + "\n")
	exit(1)

<<<<<<< HEAD
=======

>>>>>>> 0ad335f2139e316c3ebec781a98a6468e62b62c9
import urllib.request
import argparse
import os
import time
import timeit

try:
	import urllib3
<<<<<<< HEAD

except ImportError:

	print("\n" + bcolors.FAIL + 'You need to install urllib3. "sudo pip-3.3 install urllib3"' + bcolors.ENDC + "\n")
	exit(1)

def check_file():

=======
except ImportError:
	print("\n" + bcolors.FAIL + 'You need install urllib3. "sudo pip install urllib3"' + bcolors.ENDC + "\n")
	exit(1)


def check_file():
>>>>>>> 0ad335f2139e316c3ebec781a98a6468e62b62c9
	from os import path
	PATH = "./robots.txt"
	PATH2 = "./path.txt"
	
	if os.path.isfile(PATH):
		os.remove(PATH)
	
	if os.path.isfile(PATH2):
		os.remove(PATH2)

def download(url):
	try:
		g = urllib.request.urlopen("http://"+url+"/robots.txt")
	except urllib.error.HTTPError:
		print("\n" + bcolors.FAIL + "No robots.txt file has been found." + bcolors.ENDC + "\n")
		exit(1)
	except urllib.error.URLError:
		print("\n" + bcolors.FAIL + "Please, type a valid URL. This URL can't be resolved." + bcolors.ENDC + "\n")
		exit(1)
	with open('robots.txt', 'b+w') as f:
        	            f.write(g.read())

<<<<<<< HEAD
=======

>>>>>>> 0ad335f2139e316c3ebec781a98a6468e62b62c9
def logo():

	hello="""
	  ____                               
	 |  _ \ __ _ _ __ ___  ___ _ __ ___  
	 | |_) / _` | '__/ __|/ _ \ '__/ _ \ 
	 |  __/ (_| | |  \__ \  __/ | | (_) |
	 |_|   \__,_|_|  |___/\___|_|  \___/ 
"""
        
	print(bcolors.YELLOW + hello + bcolors.ENDC)

	now = time.strftime("%c")

<<<<<<< HEAD
=======


>>>>>>> 0ad335f2139e316c3ebec781a98a6468e62b62c9
def parseo(url):
	
	robots = open("robots.txt")
	robots_length = len(open('robots.txt','r').read().split('\n'))
	for i in range(1,robots_length):
		read = robots.readline()
		path = read.split(':')
		if "Disallow" == path[0]:
			disallow = path[1]
			links = open("path.txt",'a')
			links.write(path[1])
	robots.close()
	if os.path.isfile("./path.txt") == False:
		print("\n" + bcolors.FAIL + "Parsero doesn't find any Disallow, Robots.txt is not valid or is empty." + bcolors.ENDC + "\n")
		os.remove("robots.txt")
		exit(1)

	links.close()

def conn_check(url, only200):
	links = open("path.txt")
	http = urllib3.PoolManager()
	count = 0
	count_ok = 0
	for line in links.readlines():
		read = line.split("\n")
		path = read[0].lstrip()
		disurl = "http://"+url+"/"+path
		r1 = http.request('GET', disurl, redirect = False, retries = 5)
		if r1.status == 200:
			print (bcolors.OKGREEN + url+path + ' ' + str(r1.status) + ' ' + str(r1.reason) + bcolors.ENDC)
			count_ok = count_ok+1
		elif only200 == False:
			print (bcolors.FAIL + url+path + ' ' + str(r1.status) + ' ' + str(r1.reason) + bcolors.ENDC)
		count = count+1

	count_int = int(count)
	count_ok_int = int(count_ok)
	if count_ok_int != 0 and only200 == True :
<<<<<<< HEAD
		print('\n[+] %i links have been analyzed and %i of them are available!!!'%(count_int,count_ok_int))
	elif count_ok_int != 0 :
		print('\n[+] %i links have been analyzed and %i of them are available!!!'%(count_int,count_ok_int))
	elif count_ok_int == 0 and only200 == True :
		print('\n' + bcolors.FAIL + '[+] %i links have been analyzed but any them are available...'%count_int + bcolors.ENDC)
	else:
		print('\n' + bcolors.FAIL + '[+] %i links have been analyzed but any them are available...'%count_int + bcolors.ENDC)

	links.close()

def search_bing(url, searchbing):
	
	try:
		print("\nSearching the Disallows entries in Bing...\n")
		sys.path.append("./bs4")
		from bs4 import BeautifulSoup
		
	
		links = open("path.txt")
		count = 0
		for line in links.readlines():
			read = line.split("\n")
			path = read[0].lstrip()
		
			opener = urllib.request.build_opener()
			opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0')]
		
			url2 = "http://www.bing.com/search?q=site:"+url+path
			print (url2)
			
			page = opener.open(url2)
			soup = BeautifulSoup(page)
	
			
			for cite in soup.findAll('cite'):
				if url in cite.text:
					count = count +1
					print (bcolors.OKGREEN + " - " + cite.text + bcolors.ENDC)
	
		if count == 0:
			print('\n' + bcolors.FAIL + '[+] No Dissallows have been indexed in Bing' + bcolors.ENDC)
	
		links.close()

	except ImportError:
		print(bcolors.FAIL + 'You need to install Beautifulsoup. "sudo pip-3.3 install beautifulsoup4"' + bcolors.ENDC)

def date(url):
	print("Starting Parsero v0.6 (https://github.com/behindthefirewalls/Parsero) at " + time.strftime("%x") + " " + time.strftime("%X"))
	print("Parsero scan report for " + url)

def remove_files():
	os.remove("path.txt")
	os.remove("robots.txt")
=======
		print('\n%i links have been analyzed and %i of them are available!!!'%(count_int,count_ok_int))
		print('Showing only available links\n');
	elif count_ok_int != 0 :
		print('\n%i links have been analyzed and %i of them are available!!!\n'%(count_int,count_ok_int))
	else:
		print('\n%i links have been analyzed but any them are available... :(\n'%count_int)

	links.close()
	os.remove("path.txt")
	os.remove("robots.txt")

def date(url):
	print("Starting Parsero v0.45 (https://github.com/behindthefirewalls/Parsero) at " + time.strftime("%x") + " " + time.strftime("%X"))
	print("Parsero scan report for " + url)


>>>>>>> 0ad335f2139e316c3ebec781a98a6468e62b62c9

def main():
	parse = argparse.ArgumentParser()
	parse.add_argument('-u', action='store', dest='url', help='Type the URL which will be analyzed')
<<<<<<< HEAD
	parse.add_argument('-o', action='store_true', dest='only200', help='Show only the "HTTP 200" status code')
	parse.add_argument('-sb', action='store_true', dest='searchbing', help='Search in Bing indexed Disallows')

=======
	parse.add_argument('-o', action='store_true', dest='only200', help='Show only HTTP 200 status code')
	
>>>>>>> 0ad335f2139e316c3ebec781a98a6468e62b62c9
	logo()

	args = parse.parse_args()
	if args.url == None:
		parse.print_help()
		print("\n")
		exit(1)

	url = str(args.url)
	only200 = args.only200
<<<<<<< HEAD
	searchbing = args.searchbing
=======
>>>>>>> 0ad335f2139e316c3ebec781a98a6468e62b62c9

	check_file()
	download(url)
	parseo(url)
	date(url)
	conn_check(url, only200)
<<<<<<< HEAD
	if searchbing == True:
		search_bing(url, searchbing)
	remove_files()
=======
>>>>>>> 0ad335f2139e316c3ebec781a98a6468e62b62c9

if __name__=="__main__":
	start_time = time.time()
	main()
<<<<<<< HEAD
	print("\nFinished in", time.time() - start_time, "seconds\n")
=======
	print("Finished in", time.time() - start_time, "seconds\n")
>>>>>>> 0ad335f2139e316c3ebec781a98a6468e62b62c9
