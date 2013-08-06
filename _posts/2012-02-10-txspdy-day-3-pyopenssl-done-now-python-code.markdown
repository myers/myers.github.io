---
layout: post
title: "txspdy: Day 3: pyopenssl done... now to python code"
date: 2012-02-10T01:26:57
tags: ["txspdy"]
---

I don't know where to start talking about the problems with building your own copy of Openssl.  Ubuntu has added a few patches, one of which adds symbol versioning to the openssl shared libraries.  Sounds great, but it means you can't build a new version of openssl from upstream and install it system wide without problems, like say your openssh server dies because of it and you can't login.  I have a monitoring system, icinga, that noticed this and sent emails/txt msgs about it so I fixed the problem before finding myself locked out of the system.

Once that was settled I got the three new methods added to pyopenssl and made a test as well.  I've sent it upstream to get merged.  You can see it (at LaunchPad)[https://code.launchpad.net/~myers-1/pyopenssl/npn].

Now I'm writing a twisted protocol that will parse SPDY frames.  The frames build to multiple streams, and I'm not sure how to deal with those.  Maybe there is some other multiplexing protocol like this already in twisted.



