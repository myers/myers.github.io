---
layout: post
title: "django_loader.py"
date: 2010-01-21T10:07:16
tags: [django, python]
---

I got tired of putting

    import os, sys
    sys.path.append(<django project parent dir>)
    sys.path.append(<django project dir>)
    os.environ['DJANGO_SETTINGS_MODULE']='<django project name>.settings'

at the top of all my scripts that do command line things with my django models.  So I share with you 'django_loader.py'.  Note the use of traceback to figure out what file is importing 'django_loader.py'.

    """
    Put this in your python path.  At the top of your script put 'import
    django_loader'.  This will start with the directory your file is in and
    search through it and it's parent directories until it finds a file named
    'settings.py'.  It will then add that directory and it's parent to your
    sys.path, and set DJANGO_SETTINGS env var.
    """

    import os, sys, traceback

    class CouldNotFindSettings(StandardError):
        pass
    def find_settings(current_dir):
        if current_dir == '/':
            raise CouldNotFindSettings
        if 'settings.py' in os.listdir(current_dir):
            return current_dir
        return find_settings(os.path.dirname(current_dir))
    def load(filepath):
        django_project_dir = find_settings(os.path.dirname(filepath))
        django_project_name = os.path.basename(django_project_dir)

        sys.path.append(os.path.dirname(django_project_dir))
        sys.path.append(django_project_dir)
        os.environ['DJANGO_SETTINGS_MODULE']='%s.settings' % (django_project_name,)

    current_filepath = os.path.normpath(os.path.join(os.getcwd(), traceback.extract_stack(limit=2)[0][0]))
    load(current_filepath)
