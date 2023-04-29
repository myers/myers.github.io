---
layout: post
title: "RailsConf 2008: Friday Late Morning"
date: 2008-05-30T15:34:00
tags: [railsconf2008]
---

<h4><a href="http://en.oreilly.com/rails2008/public/schedule/detail/2495">Entrepreneurs On Rails &#8211; Dan Benjamin</a></h4>

<ul>
<li>Successful biz fills a need</li>
<li>What do you need
<ul>
<li>paper work important, expressing the idea idea is better, being flexable on that idea</li>
<li>energy</li>
</ul></li>
<li>so much you have to do before hand, why are you doing this?</li>
<li>set goals &#8211; we need to do x by y, if we don&#8217;t get there we&#8217;ll change things</li>
<li>have a path to cash</li>
<li>have an exit strategy</li>
<li>why create a company
<ul>
<li>Liability &#8211; legal protection from your bugs :)</li>
<li>Taxes &#8211; more buying power, talk to an accountant</li>
<li>working with other companies</li>
<li>easy of working with other companies</li>
<li>Ownership &#8211; knowing who gets what</li>
<li>perception of credibility &#8211; but don&#8217;t try to be what you are not (cd of office noises for phone calls)</li>
</ul></li>
<li>types of business</li>
<li>Fictitious Name</li>
<li><span class="caps">LLC</span> is a good idea</li>
<li>You don&#8217;t have to do this in Delaware</li>
<li>hire lawyer/accountant</li>
<li>your website should be very clear about what you wanted</li>
<li>we build things we need, but if you look at say moms with kids at home you have a much bigger audience</li>
<li>marketing.  peepcode logo (myers: I&#8217;ve always thought it looked like a lingerie ad)
<ul>
<li>you will spend 40% or more of you time marketing</li>
</ul></li>
<li>making it work is the hard part not the (unknown) paper work</li>
<li>hard part: adjusting the the lack of stability</li>
<li>common to be in a feast or famine situation</li>
<li>co-working is a way to get an office with others</li>
<li>creativity zone </li>
<li>biz deals goes like this
<ul>
<li><span class="caps">NDA</span> &#8211; worth it for a 10k deal to have your lawyer look at it</li>
<li>proposal &#8211; 40 pages shortest he ever did</li>
<li>contract &#8211; you should write the contract, here&#8217;s what I&#8217;ll do, he&#8217;s what I&#8217;m liabile and not liabile for</li>
<li>Functionality Outline &#8211; evolution of a statement of work</li>
<li>getting the money &#8211; net 30, net 60, net 15, net 0 &#8211; put it in your contract, also &#8220;there is a 2% fee for late payments&#8221;</li>
</ul></li>
<li>products: it&#8217;s about liability </li>
<li>TOS/privacy policy &#8211; be clear, be up front</li>
<li>ways to get money (see slides)</li>
<li>on hivelogic he&#8217;ll post a sample <span class="caps">SOW</span></li>
</ul>

<h4><a href="http://en.oreilly.com/rails2008/public/schedule/detail/2082">Surviving the Big Rewrite: Moving <span class="caps">YELLOWPAGES</span>.<span class="caps">COM</span> to Rails</a></h4>

<ul>
<li>biggest website at&t runs</li>
<li>all rails</li>
<li>1 year ago 1/2 as big</li>
<li>(long slides)</li>
<li>why a big rewrite? &#8211; it&#8217;s a great bundler</li>
<li>no automated tests, new features really hard</li>
<li>lots of code being replace with site redesign</li>
<li>hard to leverage</li>
<li>java: get around this web thing with design patterns so you get to the real business of talking to middleware</li>
<li>devs except that not everything they want will get done</li>
<li>core team never more that 4 &#8211; trying to keep it small</li>
<li>they looked at django and ejb3/jboss</li>
<li>no to django
<ul>
<li>better automated testing integration (hear hear)</li>
<li>more platform maturity</li>
<li>clearer path to C if necessary for performance (I don&#8217;t agree with that.  Python + C is easy, plus you have psyco and ctype that let you get C performance or use c libs with pure python)</li>
<li>developer comfort and experience</li>
</ul></li>
<li>not convinced anyone needs <span class="caps">MOM</span></li>
<li>only one developer that knew rails at the start</li>
<li>project got stuck</li>
<li>project lead appointed to make decision-making and communication with executive team, or at least the appearance
<ul>
<li>sometimes she decided in private with her bosses</li>
</ul></li>
<li>freeze current site</li>
<li>if it&#8217;s not simple to decide how to change a current site behavior, don&#8217;t change it.  save it for a later phase.</li>
</ul>

<p>(it&#8217;s worth it to read the slides, even for a non rewrite project.  The slides are probably have too much on them, but that&#8217;s good for you)</p>

<ul>
<li>they spent an amazing amount of time communicating what was changing.</li>
<li>F5 Load Balancers</li>
<li>switched to erubis in web tier</li>
</ul>
