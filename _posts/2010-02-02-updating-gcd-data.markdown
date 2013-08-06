---
layout: post
title: "Updating GCD Data"
date: 2010-02-02T23:40:16
tags: ["django", "python"]
---

So you have [loaded the Grand Comicbook Database into a local postgresql instance][2] and wrote some code that makes use of the data... They just did a [new data dump][1]... Now how do you update your copy of the data?

### Prep the data

Do the steps in "create mysql clean up script" and "dump data to tab separated value files" steps.

Now copy this python script:

    #!/usr/bin/env python

    """
    update gcd data that's prep'ed in /tmp/gcd_dump
    """

    import os, glob
    from pprint import pprint
    import psycopg2, psycopg2.extras

    table_names = [os.path.splitext(os.path.basename(fp))[0] for fp in glob.glob('/tmp/gcd_dump/*.txt')]

    conn = psycopg2.connect("dbname='gcd' user='postgres'")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def sql_logger(sql):
        print sql
        cur.execute(sql)

    constraints = []
    for ii in table_names:
        sql_logger("""
    select t.constraint_name, t.table_name, t.constraint_type,
      c.table_name as c_table_name, c.column_name as c_column_name, k.column_name as k_column_name
    from information_schema.table_constraints t,
      information_schema.constraint_column_usage c,
      information_schema.key_column_usage k

      where t.constraint_name = c.constraint_name
        and t.constraint_name = k.constraint_name
        and t.constraint_type = 'FOREIGN KEY'
        and c.table_name = '%s'
      """ % ii)
        for row in cur:
            constraints.append(dict(row))

    sql_logger('begin')
    for ii in constraints:
        sql_logger('alter table %s drop constraint %s;' % (ii['table_name'], ii['constraint_name'],))

    for table_name in table_names:
        sql_logger("DELETE FROM %(table_name)s" % locals())
        sql_logger("COPY %(table_name)s FROM '/tmp/gcd_dump/%(table_name)s.txt'" % locals())

    for ii in constraints:
        sql_logger("""
    ALTER TABLE ONLY %(table_name)s 
      ADD CONSTRAINT %(constraint_name)s 
        FOREIGN KEY (%(k_column_name)s) REFERENCES %(c_table_name)s(%(c_column_name)s) DEFERRABLE INITIALLY DEFERRED;
    """ % ii)

    sql_logger('commit')  


You'll have to run this as the postgres user just as before.  It records the FOREIGN KEY CONSTRAINT, drops them, deletes the old data, copies in the new, and recreates the constraints, all in one transaction!  Eat that MySQL.  

  [1]: http://dev.comics.org/data/2010-01-30/
  [2]: /2010/01/11/how-convert-data-mysql-database-postgresql/

