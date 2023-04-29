---
layout: post
title: "RailsConf 2008: Friday Early Afternoon"
date: 2008-05-30T18:59:49
tags: [railsconf2008]
---

<h4><a href="http://en.oreilly.com/rails2008/public/schedule/detail/1960">Dialogue Concerning the Two Chief Modeling Systems</a></h4>

<ul>
<li>it&#8217;s a Play</li>
</ul>

<p>(again you should read the slides)</p>

<ul>
<li>choosing the right name will make the dev think about this model and give it the right property</li>
<li>Jim keeps saying we&#8217;re skipping layers</li>
<li>using story cards</li>
<li>jammed up over reoccurring events</li>
<li>objects = data + behavior, so you can&#8217;t just talk about the data (rows/tables), you must look at behavior</li>
<li>pull out the Class, Responsibilities, and Collaborator cards</li>
<li>card only useful for organizing your thoughts not need to fill them all out</li>
<li>&#8220;temporal expressions&#8221;</li>
<li>CJ Date: apparently wrote a lot about data modeling</li>
<li>Code Smell in Refactoring by Chad Fowler </li>
</ul>

<h4><a href="http://en.oreilly.com/rails2008/public/schedule/detail/2127">Flexible Scaling: How to Handle 1 Billion Pageviews</a> &#8211; TJ</h4>

<ul>
<li>WoW: you see all kinds of human behaviors: Mafia, Philantropis  </li>
<li>Building games on Facebook</li>
<li>He&#8217;s the author of Warbook: Rise of the Infernals</li>
<li>w/i a week he had to fix stuff</li>
<li>w/i 3 weeks had to rewrite</li>
<li>started with firebug&#8217;s net tab</li>
<li>look at your logs: pl_analyze</li>
<li>iostat </li>
</ul>

<ul>
<li>you need tools, but you also need strategies</li>
<li>don&#8217;t need it? ditch it.</li>
<li>slowing it down? simplify it.</li>
<li>logging it? stop</li>
<li>selecting it? cache it.</li>
<li>memcache</li>
<li>put sessions in cache</li>
<li>no-select design
<ul>
<li>use memcache</li>
<li>cache_fu already does this</li>
</ul></li>
<li>using ec2</li>
<li>1 db box</li>
<li>1 memcache box</li>
<li>1 static file</li>
<li>X mongrel boxes</li>
<li>The Hard Part
<ul>
<li>Scale Everything Else</li>
<li>Scale your deploymnet
<ul>
<li>use capistrano</li>
</ul></li>
<li>Scaling your support</li>
<li>community management
<ul>
<li>give them updates every day</li>
</ul></li>
</ul></li>
<li>server cost $2000 a month</li>
<li>you need money</li>
<li>warbook makes $100,000/month</li>
<li>1.5 million users</li>
<li>16 million page views</li>
</ul>

<h5>Q&A</h5>

<ul>
<li>remove transactional saves</li>
<li>save per fields</li>
<li>how to solve the persistence problem on ec2? db not on amazon</li>
<li>which facebook lib? started with rfacebook, facebooker, bebo</li>
</ul>

<p><a href="http://freewebs.com/warbook">Slides</a></p>
