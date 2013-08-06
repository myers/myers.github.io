---
layout: post
title: "Two itches that need scratching in Mnet"
date: 2002-06-02T20:34:23
tags: []
---

I think Mnet would become a lot more usable if we added two things: 

  * [Achord routing and lookup][1] - this is a nice solution because achord gives you some guaranties about the time to find something in the network and also some privacy. It's yet to be seen if the XOR routing can be hacked in the same what chord was hacked to get achord. 
  * Expanded search fields - I want to be able to tell the content tracker as much as I can about a file, but I want everyone else to at least tell me a few things about their file. All files should have a [bitprint][2], file size (in bytes, who decided that the file size should be in kb in the current version), and a type field. The type could be any string with len(str) < 50, but if it was set to certain value the content trackers would require other fields (for audio files, [a musicbrainz track id][3], a trm signature, audio Sha1, artist, title) 

The itch I can't scratch is getting [Octal][4] to start [OpenDBS][5] up and running so we can reinstate the $$$ for all transactions again. 

   [1]: http://thalassocracy.org/achord/achord-iptps.html
   [2]: http://bitzi.com/
   [3]: http://musicbrainz.org
   [4]: http://www.venona.com/rdl/
   [5]: http://opendbs.org



