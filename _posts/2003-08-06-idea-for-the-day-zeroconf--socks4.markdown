---
layout: post
title: "Idea for the day: Zeroconf + SOCKS4"
date: 2003-08-06T08:34:11
tags: []
---

After spending much too long trying to figure out if I wanted to deal with the greif of implementing a UPnP Gateway with Twisted, I thought of another idea: Use [Zeroconf][1] to advertise a [SOCKS4][2] server. That shouldn't be too hard to do in Twisted, just need a zeroconf module, and a mDNS server.

And client developers could probably make use of [Howl][3] to do the zeroconf stuff. SOCKS4 is even easier (or so I'm told). Also Howl seems to have a mDNS server for linux... so we just need debian packages.

On a side note, now that I look at the howl tarball I see that it's GPL'ed... why oh why do you GPL a library. :(.

[ Later: I heard back from the Howl developers that the license supposed to be BSD and will be in the next release. ]

   [1]: http://www.zeroconf.org/
   [2]: http://archive.socks.permeo.com/protocol/socks4.protocol
   [3]: http://www.swampwolf.com/products/
