---
layout: post
title: "More on music merging"
date: 2002-06-06T09:23:30
tags: []
---

My mergeing project has gone awry. While I did pick off the easy duplicates (the ones with matching audioSha1's), I decided it would be better to finish TuneTagger. 

TuneTagger (project at [sf.net][1] is way out of date) is a music file renaming/tagging utility. It's greatest feature will be making use of [Musicbrainz][2]. Once a track as been id'ed by one person, Musicbrainz remember the sound signature (aka TRM) of the song so the next person that points a Musicbrainz enabled tool at any file that is the same song it will know right away what that song is. 

I figure it probably won't need that many users before you will be able to sort out and rename your music collection without lifting a finger. 

At first I was going to use wxPython, but I have gotten to play with pygtk/pygnome and the mozilla wrapper [ pygme][3] and it looks like that will be an easier route to take with just has much portablity. 

   [1]: http://sf.net/tunetagger/
   [2]: http://musicbrainz.org
   [3]: http://cvs.gnome.org/bonsai/rview.cgi?cvsroot=/cvs/gnome&dir=pygme



