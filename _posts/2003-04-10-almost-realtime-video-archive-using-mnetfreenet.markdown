---
layout: post
title: "Almost realtime video archive using mnet/freenet"
date: 2003-04-10T11:01:48
tags: [ideas]
---

(this is not going to make sense unless you know the inner workings of [mnet][1] or [freenet][2])

Software reads and encodes 1m of video, then publishes those FEC blocks, then the inode block and then waits for the next 1m of video to be published with an inode. Then it publishes a metadata block with the info about this clip (stuff like timecode in UTC, the [URI of the channel you are encoding][3]) and then three mnet/freenet URI's one pointing this 1m of video, the next 1m and prev 1m. So then, anyone can pick up the video stream from that point and follow it either way.

This would be great for allowing people to refer back into time and point their friends at a bit of CNN/FOX/BBC/MyersTV/Whatever.

   [1]: http://mnet.sf.net
   [2]: http://freenet.sourceforge.net/
   [3]: http://ftp.ics.uci.edu/pub/ietf/uri/draft-zigmond-tv-url-03.txt
