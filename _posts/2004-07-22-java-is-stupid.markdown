---
layout: post
title: "Java is stupid"
date: 2004-07-22T12:08:26
tags: []
---

<p>Aside from typing 10x as much and haven&#8217;t to struggle to get basic concepts to work (iterating over a map for example), there are other irritating things:</p>

<p>java.lang.ClassCastException does not provide a error string, of like, I don&#8217;t know, <span class="caps">MAYBE</span> <span class="caps">THE</span> <span class="caps">NAME</span> OF <span class="caps">THE</span> <span class="caps">TWO</span> <span class="caps">CLASSTYPES</span>.  This is where open source shines.  A mistake like that that adds hours of time to your debugging session would last maybe a week before some said, &#8220;I&#8217;ll fix the jvm itself so that it helps me the programmer&#8221;.</p>

<p><span class="caps">JDBC</span> apparently has no method to communicate what columns an <span class="caps">SQL</span> error occurs in, so if you insert a row that causes an error you have to get the schema file and the <span class="caps">SQL</span> statement (not easy to do if you use prepared statements) and go over it column by column.</p>

<p>People save your time, use python.  There is NO reason to use Java. It&#8217;s old dead and gone.  By being closed source all other languages are rapidly speeding past it as far as ease of use to the programmer.</p>

