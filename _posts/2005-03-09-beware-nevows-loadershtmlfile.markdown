---
layout: post
title: "beware nevow's loaders.htmlfile"
date: 2005-03-09T20:54:12
tags: [python]
---

<p>I&#8217;m using <a href="http://nevow.com/">Nevow</a> for a website I&#8217;m working on, it&#8217;s pretty nice.  Biggest problem is that I have a many to many relationship with attributes which is hard to model in <a href="http://twistedmatrix.com/documents/current/howto/row.html">Twisted&#8217;s ROW</a>.  I could just write a property to the Row objects that have the many to many relationship so that it can pull in the right info, but I can&#8217;t figure out a clean what to get a ref to the reflector object. I&#8217;ve looked at Atop, but I&#8217;m a bit worried about the many command line utils I have written around the <span class="caps">SQL</span> database I&#8217;m using.</p>

<p>My caution to you, internet reader, is be careful you use loaders.xmlfile not loaders.htmlfile.  htmlfile just doesn&#8217;t work well.   I was trying to assign a data object for the whole page (it feeds data to the page title tag, and many other places, plus all other data on the page is a child of that data object), and after the second nevow:render it had lost track of the data object.  Change htmlfile to xmlfile and everything works.</p>
