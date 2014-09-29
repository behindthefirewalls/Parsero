# parsero - A Python based Robots.txt audit tool
# Copyright (c) 2013-2014 Javier Nieto <javier.nieto at behindthefirewalls.com>
#
# Released under the GPLv2+ license. See LICENSE file for details.
#
from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == '__main__':
    setup(
        name = 'parsero',
        version="0.81",
        description = 'A Python based Robots.txt audit tool',
        long_description = read('README.md'),
        author = 'Javier Nieto',
        author_email = 'javier.nieto@behindthefirewalls.com',
        maintainer = 'Fabian Affolter, C0r3dump, fikoborquez',
        maintainer_email = 'fabian@affolter-engineering.ch, coredump@autistici.org',
        url = 'https://github.com/behindthefirewalls/Parsero',
        license = 'GPLv2+',
        platforms = 'Linux',
        py_modules = ['parsero'],
        entry_points = {
            'console_scripts': ['parsero = parsero:main'],
        },
        include_package_data = True,
        install_requires = [
            'beautifulsoup4',
            'urllib3',
            'pip'
        ],
        keywords = 'Robots.txt Audit Webserver',
        classifiers = [
                'Development Status :: 5 - Production/Stable',
                'Environment :: Console',
                'Intended Audience :: End Users/Desktop',
                'Intended Audience :: System Administrators',
                'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
                'Operating System :: POSIX',
                'Programming Language :: Python :: 3.3',
                'Topic :: Internet :: WWW/HTTP',
                'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
                ],
    )
