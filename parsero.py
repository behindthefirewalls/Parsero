#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__license__ = """

Parsero is a free script which read the Robots.txt file of a web server and
look at the Disallow entries. Then it visits these entries and prints the
status code in order to show you which of them are available and which not.

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

if sys.version_info < (3, 0, 0):
    print("\n" + bcolors.FAIL + \
            "You need Python3 or later to run this script." + \
            bcolors.ENDC + "\n")
    exit(1)

import urllib.request
import argparse
import time

try:
    import urllib3

except ImportError:
    print("\n" + bcolors.FAIL + \
            'You need to install urllib3. "sudo pip-3.3 install urllib3"' + \
            bcolors.ENDC + "\n")
    exit(1)

def logo():
    hello = """
      ____                               
     |  _ \ __ _ _ __ ___  ___ _ __ ___  
     | |_) / _` | '__/ __|/ _ \ '__/ _ \ 
     |  __/ (_| | |  \__ \  __/ | | (_) |
     |_|   \__,_|_|  |___/\___|_|  \___/ 
"""

    print(bcolors.YELLOW + hello + bcolors.ENDC)
    now = time.strftime("%c")

def conn_check(url, only200):
    global pathlist
    pathlist = []
    salida = 1
    try:
        for line in urllib.request.urlopen("http://" + url + "/robots.txt"):
            lineStr = str(line, encoding='utf8')
            path = lineStr.split(': /')
            if "Disallow" == path[0]:
                pathlist.append(path[1].replace("\n", "").replace("\r", ""))
                pathlist = list(set(pathlist))
            try:
                inx = pathlist.index("/")
                del pathlist[inx]
            except:
                pass
    except urllib.error.HTTPError:
        print("\n" + bcolors.FAIL + "No robots.txt file has been found." + bcolors.ENDC)
        salida = 0
    except urllib.error.URLError:
        print("\n" + bcolors.FAIL + "Please, type a valid URL. This URL can't be resolved." + bcolors.ENDC)
        print("\n" + bcolors.FAIL + "e.g: python3 parsero.py -u www.behindthefirewalls.com -o -sb" + bcolors.ENDC + "\n")
        salida = 0

    http = urllib3.PoolManager()
    count = 0
    count_ok = 0

    for p in pathlist:
        disurl = "http://" + url + '/' + p
        r1 = http.request('GET', disurl, redirect=False, retries=5)
        if r1.status == 200:
            print(bcolors.OKGREEN + disurl + ' ' + str(r1.status) + ' ' + str(r1.reason) + bcolors.ENDC)
            count_ok = count_ok + 1
        elif only200 == False:
            print(bcolors.FAIL + disurl + ' ' + str(r1.status) + ' ' + str(r1.reason) + bcolors.ENDC)
        count = count + 1

    count_int = int(count)
    count_ok_int = int(count_ok)

    if salida == 1:
        if count_ok_int != 0 and only200 == True:
            print('\n[+] %i links have been analyzed and %i of them are available!!!' % (count_int, count_ok_int))
        elif count_ok_int != 0:
            print('\n[+] %i links have been analyzed and %i of them are available!!!' % (count_int, count_ok_int))
        elif count_ok_int == 0 and only200 == True:
            print('\n' + bcolors.FAIL + '[+] %i links have been analyzed but any them are available...' % count_int + bcolors.ENDC)
        else:
            print('\n' + bcolors.FAIL + '[+] %i links have been analyzed but any them are available...' % count_int + bcolors.ENDC)

def search_bing(url, searchbing, only200):
    try:
        print("\nSearching the Disallows entries in Bing...\n")
        from bs4 import BeautifulSoup

        count = 0
        for p in pathlist:
            disurl = "http://" + url + '/' + p
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0')]
            url2 = "http://www.bing.com/search?q=site:" + disurl
            print(url2)

            page = opener.open(url2)
            soup = BeautifulSoup(page)

            http = urllib3.PoolManager()
            for cite in soup.findAll('cite'):
                try:
                    if url in cite.text:
                        count = count + 1
                        r2 = http.request('GET', cite.text, redirect=False, retries=5)
                        if r2.status == 200:
                            print(bcolors.OKGREEN + ' - ' + cite.text + ' ' + str(r2.status) + ' ' + str(r2.reason) + bcolors.ENDC)
                        elif only200 == False:
                            print(bcolors.FAIL + ' - ' + cite.text + ' ' + str(r2.status) + ' ' + str(r2.reason) + bcolors.ENDC)
                except UnicodeEncodeError:
                    pass

        if count == 0:
            print("\n" + bcolors.FAIL + '[+] No Dissallows have been indexed in Bing' + bcolors.ENDC)

    except ImportError:
        print(bcolors.FAIL + 'You need to install Beautifulsoup. "sudo pip-3.3 install beautifulsoup4"' + bcolors.ENDC)

def date(url):
    print("Starting Parsero v0.81 (https://github.com/behindthefirewalls/Parsero) at " + time.strftime("%x") + " " + time.strftime("%X"))
    print("Parsero scan report for " + url)

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('-u', action='store', dest='url', help='Type the URL which will be analyzed')
    parse.add_argument('-o', action='store_true', dest='only200', help='Show only the "HTTP 200" status code')
    parse.add_argument('-sb', action='store_true', dest='searchbing', help='Search in Bing indexed Disallows')
    parse.add_argument('-f', action='store', dest='file', help='Scan a list of domains from a list')

    args = parse.parse_args()

    if args.file == None and args.url == None:
        logo()
        parse.print_help()
        print("\n")
        exit(1)

    urls = []
    if args.file != None:
        try:
            hostFile = open(args.file, 'r')
        except IOError:
            logo()
            print(bcolors.FAIL + "[-] The file '"'%s'"' doesn't exist." % (args.file) + "\n" + bcolors.ENDC)
            exit(1)

        for line in hostFile.readlines():
            line = line.split("\n")
            urls.append(str(line[0]))

    if args.url != None:
        urls.append(str(args.url))

    urls = filter(None, urls)
    urls = list(set(urls))
    logo()
    for url in urls:
        if url.find("http://") == 0:
            url = url.replace("http://", "")
        start_time = time.time()
        only200 = args.only200
        searchbing = args.searchbing
        date(url)
        conn_check(url, only200)
        if searchbing == True:
            search_bing(url, searchbing, only200)
        print("\nFinished in %0.2f seconds.\n" % (time.time() - start_time))

if __name__ == "__main__":
    main()

