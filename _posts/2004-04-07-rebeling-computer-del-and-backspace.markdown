---
layout: post
title: "Rebeling computer: DEL and backspace"
date: 2004-04-07T11:24:03
tags: []
---

Debian for a long time tried to have their own xterm type 'xterm-debain'. In order to work around some problem I was having some point in the past (the oldest dotfile I have in my home directory is dated "Jan 27 1997") I created a my personal xterm terminfo file that had some bug fix.

Fast forward to present day: I've upgraded to gnome 2.4, bringing with it many other updates, and suddenly bash is printing "~" when I hit DEL and joe is DEL'ing when I backspace.

This drives me nuts trying to compare the setup on that machine with all the other well behaving debian boxes I have. Finally I ran `strace`


    [...]
    access("/home/myers/.terminfo/x/xterm", R_OK) = 0
    open("/home/myers/.terminfo/x/xterm", O_RDONLY) = 3
    [...]


Lessions learned:

  * `strace` is the greatest
  * It might be nice to start with a clean `$HOME` every so often
