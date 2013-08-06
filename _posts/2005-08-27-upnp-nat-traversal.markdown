---
layout: post
title: "UPnP NAT Traversal"
date: 2005-08-27T09:26:13
tags: []
---

<p>I can&#8217;t really claim credit for this: more than a year ago I had started to write code to interface with the <span class="caps">NAT</span> box at my office via <a href="http://www.upnp.org/">UPnP</a>.  I never finished but passed the python code on to one of the <a href="http://divmod.org">divmod</a> guys.  They put that in <span class="caps">CVS</span>, made major changes but didn&#8217;t get it working.  Raphaël Slinckx now has taken that code and got it working resulting in <a href="http://raphael.slinckx.net/nattraverso.php">Nattraverso</a>.  Good Job!</p>

<p>I see that he requires a <span class="caps">SOAP</span> library, so that means the a) python <span class="caps">SOAP</span> libraries have evolved enough to deal with the &#8220;not quite SOAP&#8221; used in UPnP, or b) He&#8217;s targeting some new UPnP spec.</p>

<p>I have no UPnP <span class="caps">NAT</span> box now to test on.</p>

