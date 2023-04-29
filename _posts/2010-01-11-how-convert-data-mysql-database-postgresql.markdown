---
layout: post
title: "How to convert data in a MySQL database to Postgresql"
date: 2010-01-11T19:32:14
tags: [django, python]
---

To do this you need both mysql and postgresql running on a local computer.
You probably want this to be a local workstation that you have superuser
access to.  We are going to use features in mysql and postgres that makes
the database daemon read and write to local files.

We'll use django's schema format deal with the difference between postgresql
and mysql.  We'll use tab separated value (TSV) data files as the
interchange format between databases.  Mysql has a different idea of how to
escape newlines and carriage returns than Postgresql so we'll use a quick and
dirty python script to clean that up.

While this should work in many different OS's, I did this on a Ubuntu, so
the details might be a bit different.

Let's start with the [most recent data dump](http://dev.comics.org/data/2009-12-21/)
from the [Grand Comicbook Database](http://docs.comics.org/wiki/Main_Page)

### load data into mysql

    mysqladmin -uroot create gcd
    mysql -uroot gcd < pub_dec21_schema_innodb.sql
    unzip pub_dec21_data.zip
    mysql -uroot gcd < pub_dec21_data.sql

### create django project

    django-admin.py startproject grandcomicdb
    cd grandcomicdb
    chmod +x manage.py
    ./manage.py startapp gcd
    # edit settings.py to add gcd to INSTALLED_APPS
    # edit settings.py to set up connection to mysql
    ./manage.py inspectdb > gcd/models.py
    # edit gcd/models.py to make the fk quoted, and add relative_name's

### create mysql clean up script

    cat >> fix_mysql_tsv.py << EOF
    #!/usr/bin/env python

    # this will not work for very big files.

    import sys
    ff = open(sys.argv[1], 'r').read()
    ff = ff.replace('\r', '\\r')
    ff = ff.replace('\\\n', '\\n')

    open(sys.argv[1], 'w').write(ff)
    EOF
    chmod +x fix_mysql_tsv.py

### dump data to tab separated value files

    mkdir /tmp/gcd_dump
    chmod 777 /tmp/gcd_dump
    mysqldump -uroot -t --tab /tmp/gcd_dump gcd
    find /tmp/gcd_dump -type f -exec ~/web/grandcomicsdb/fix_mysql_tsv.py \{\} \;

### create postgres database with schema derived from the mysql database

    sudo -s -u postgres
    createuser gcd --pwprompt --no-createrole --no-createdb
    createdb gcd -O gcd
    exit
    # edit settings.py to set up connection to postgresql
    ./manage syncdb

### create postgres database and load data

    sudo -s -u postgres
    psql
    BEGIN;
    COPY gcd_language FROM '/tmp/gcd_dump/gcd_language.txt';
    COPY gcd_country FROM '/tmp/gcd_dump/gcd_country.txt';
    COPY gcd_brand FROM '/tmp/gcd_dump/gcd_brand.txt';
    COPY gcd_publisher FROM '/tmp/gcd_dump/gcd_publisher.txt';
    COPY gcd_indicia_publisher FROM '/tmp/gcd_dump/gcd_indicia_publisher.txt';
    COPY gcd_story_type FROM '/tmp/gcd_dump/gcd_story_type.txt';
    COPY gcd_series FROM '/tmp/gcd_dump/gcd_series.txt';
    COPY gcd_issue FROM '/tmp/gcd_dump/gcd_issue.txt';
    COPY gcd_story FROM '/tmp/gcd_dump/gcd_story.txt';
    COMMIT;
