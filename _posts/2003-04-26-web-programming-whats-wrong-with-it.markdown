---
layout: post
title: "Web Programming: what's wrong with it"
date: 2003-04-26T09:34:34
tags: ["python"]
---

While looking for some python web framework that might work under mod_python, twisted.web, and cgi on google I ran across [this post][1] which descibes my thoughts on what's wrong with PHP, (and though he doesn't mention it) ASP, as well as mod_python: 

> The problem with the first should be obvious, it works well, but you end up reimplementing a lot of stuff that you just feel should be done well once, and then reused. The problem with the second is more subtle. It has to do with all such systems I've looked at consisting of a huge network of interdependent objects, where you have to take it or leave it, there's no way to reuse a simple part of the system without also using the rest. 
> 
> ... 
> 
> But there's no denying that PHP is a language that can be picked up by a newbie and in 10 minutes, he'll be doing rudimentary web stuff with it. Compare to Python, which is extremely easy to pick up for a newbie when it comes to ordinary scripting, but when you want to do web stuff, you're stuck with configuring handlers for mod_python and doing all sorts of strangeness. Of course, it's easy when you know it, but how many web development newbies are lost because of this? 

At work I'm beating [Commersus][2] into something is respectable. I hope they take my patches. 

   [1]: http://www.avmaria.com/activitylog.php?year=2003&month=01
   [2]: http://www.commersus.com



