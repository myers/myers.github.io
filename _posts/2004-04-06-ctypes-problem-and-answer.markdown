---
layout: post
title: "Ctypes problem and answer: __gxx_personality_v0"
date: 2004-04-06T17:46:54
tags: ["python"]
---

Today I was playing with [ctypes][1]. I was getting this error: 
    
    
    Traceback (most recent call last):
      File "mb.py", line 4, in ?
          mb = cdll.LoadLibrary("/usr/local/lib/libmusicbrainz.so.4")
            File "/usr/local/lib/python2.3/site-packages/ctypes/__init__.py",
    line 286, in LoadLibrary
        return self._dlltype(name)
          File "/usr/local/lib/python2.3/site-packages/ctypes/__init__.py", line
    222, in __init__
        self._handle = LoadLibrary(self._name)
        OSError: /usr/local/lib/libmusicbrainz.so.4: undefined symbol:
    __gxx_personality_v0
    

Turns out that I had built libmusicbrainz.so with an older g++. [This debian bug report][2] helped, as did [ this posting on gcc-l][3]. 

   [1]: http://starship.python.net/crew/theller/ctypes/
   [2]: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=186788+
   [3]: http://www.faqchest.com/prgm/gcc-l/gcc-02/gcc-0207/gcc-020703/gcc02071822_33715.html



