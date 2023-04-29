#!/usr/bin/env python

"""
quickblog - simple python script to post to a blog that supports the blogger xmlrpc api

sample config (~/.quickblog/config)

[default]
blog_url = http://example.com/xmlrpc.php
username = someone
password = something
blogid = 1
"""


import sys, tempfile, os, ConfigParser # python 2.1 std lib
import xmlrpclib # python 2.2 std lib or at http://effbot.org/downloads/xmlrpclib-1.0.1.zip


APP_KEY = '0'
APP_PATH = os.path.expanduser('~/.quickblog')
CONFIG_PATH = APP_PATH + '/config'

def quickblog():
    # make our app directory
    try:
        os.makedirs(APP_PATH)
    except OSError:
        pass

    # read the config file
    config = ConfigParser.ConfigParser()
    config.read(CONFIG_PATH)
    check_config(config)

    filename = os.path.join(APP_PATH, tempfile.gettempprefix())

    # start editor
    os.system("%s %s" % (os.environ['EDITOR'], filename))

    answer = raw_input('Post? (y/N):').lower()
    if answer != 'y':
        sys.exit()

    # mark up
    ff = open(filename, 'r')
    title = ff.readline().strip()
    blog_entry = ff.read().strip()
    ff.close()

    blog_entry = "<title>%s</title>\n%s" % (title, blog_entry.replace('\n\n', '\n<br /><br />\n'))

    srv = xmlrpclib.Server(config.get('default', 'blog_url'))

    publish = xmlrpclib.Boolean(1)

    srv.blogger.newPost(
        APP_KEY,
        config.get('default', 'blogid'),
        config.get('default', 'username'),
        config.get('default', 'password'),
        blog_entry,
        publish)

def check_config(config):
    try:
        config.get('default', 'blog_url')
        config.get('default', 'username')
        config.get('default', 'password')
        config.get('default', 'blogid')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        raise "config file incomplete:", e

if __name__ == '__main__':
    quickblog()
