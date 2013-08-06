---
layout: post
title: "Software of the day: ext2fsd"
date: 2004-01-18T05:37:55
tags: []
---

I got a 160GB drive to replace a failing 120GB one, but since I don't need the
data on the 120GB right now I unplugged it and put it away. Then I took the
new drive and made a dup of my music drive and brought it to work. Only
problem is there's no linux box to put it in and it's formated ext2. Enter
[ext2fsd][1]. I installed the drive, installed ext2fsd and I could mount my
drive. Now I have access to 140GB of music at work and I'm happy.

Only a few problems so far: I tried to get [Musik][2] to index all the drive,
and the computer just snapped off. Judging by the error I got when WinXP
recovered it had to do with ext2fsd. Either WinXP or the driver doesn't know
how to deal with UTF-8 filenames. And last up, sometime renaming files causes
weird things.

   [1]: http://ext2fsd.sourceforge.net/

   [2]: http://musik.berlios.de/



