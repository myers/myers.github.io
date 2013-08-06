---
layout: post
title: "mnetproject.org back up"
date: 2005-07-29T14:50:53
tags: ["python"]
---

<p>After a long while of doing nothing on Mnet, I&#8217;m getting the p2p itch again.  It&#8217;s funny how some projects you just run out of the urge to keep working on them.</p>

<p>First thing I&#8217;ve done is get <a href="http://mnetproject.org/">mnetproject.org</a> back up and running.  Not sure what do to about the sf.net version, but I haven&#8217;t seen a lot of activity there either.</p>

<p>I&#8217;m on <span class="caps">IRC</span> again, #mnet.  I still am not happy with the chump bot.  I think I would blog more via chump if it was working well.</p>

<p>So, on to the code.  When we last left, Mnet 0.7 could publish and download files using &#8220;mnet&#8221; URI&#8217;s.  It used it&#8217;s own protocol, <span class="caps">EGTP</span>, which used <span class="caps">TCP</span> and a custom encryption protocol to communicate between nodes.  No anonymity was attempted.  I was working on a search engine, then planning on moving to reworking the <span class="caps">GUI</span>.</p>

<p>Right now I&#8217;d rather work on Mnet over <a href="http://www.i2p.net/">I2P</a> via <a href="http://www.i2p.net/sam">Simple Anonymous Messaging</a> .  I don&#8217;t know if I&#8217;ll do this as a egtp protocol or just remove egtp and replace it with a twisted port of <span class="caps">SAM</span>.</p>

