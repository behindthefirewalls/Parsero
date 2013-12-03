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


import sys

if sys.version_info<(3,0,0):
	print("\n" + bcolors.FAIL + "You need Python3 or later to run this script." + bcolors.ENDC + "\n")
	exit(1)


import urllib.request
import argparse
import os
import time

try:
	import urllib3
except ImportError:
	print("\n" + bcolors.FAIL + 'You need install urllib3. "sudo pip install urllib3"' + bcolors.ENDC + "\n")
	exit(1)


def check_file():
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
	links.close()

def conn_check(url):
	links = open("path.txt")
	http = urllib3.PoolManager()
	for line in links.readlines():
		read = line.split("\n")
		path = read[0].lstrip()
		disurl = "http://"+url+"/"+path
		r1 = http.request('GET', disurl, redirect = False, retries = 5)
		if r1.status == 200:
			print (bcolors.OKGREEN + url+path + ' ' + str(r1.status) + ' ' + str(r1.reason) + bcolors.ENDC)
		else:
			print (bcolors.FAIL + url+path + ' ' + str(r1.status) + ' ' + str(r1.reason) + bcolors.ENDC)
	print('\nFinished!!!\n')
	links.close()
	os.remove("path.txt")
	os.remove("robots.txt")

def date(url):
	print("Starting Parsero v0.4 (https://github.com/behindthefirewalls/Parsero) at " + time.strftime("%x") + " " + time.strftime("%X"))
	print("Parsero scan report for " + url)



def main():
	parse = argparse.ArgumentParser()
	parse.add_argument('-u', action='store', dest='url', help='Type the URL which will be analyzed')
	
	logo()

	args = parse.parse_args()
	if args.url == None:
		parse.print_help()
		print("\n")
		exit(1)

	url = str(args.url)

	check_file()
	download(url)
	parseo(url)
	date(url)
	conn_check(url)

if __name__=="__main__":
	main()
