---
layout: post
title: "Circle: what all p2p system should be"
date: 2002-06-02T18:51:22
tags: []
---

If you know anything about the state of the mnet code you know that what I like to do is make thing more usable to the average person. So tonight I had the pleasure of play with [The Circle][1] tonight. It's got some cool stuff.

  * you can share your debian apt cache (meaning all the *.deb files that you've downloaded, installed, but not deleted) with everyone else on circle, and added apt methods that will transparently try to get packages from circle before trying to get them from the normal site. (md5sums make the world go 'round)
  * the daemon script has an option that can be run to install an init.d script to bring the daemon up on reboot (not sure if the init.d scripts are in the debian package)
  * some kind of shell extention where you can switch between circle and the shell (havn't tried it yet)

I hope to bring some of these same UI ideas to Mnet right after I get the other two big things out of the way. (what are those? stay tuned.)

   [1]: http://yoyo.cc.monash.edu.au/~pfh/circle/
