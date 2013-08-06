---
layout: post
title: "Canada on Rails: Opening keynote: David"
date: 2006-04-13T13:34:50
tags: ["canada-on-rails"]
---

<p>Watching <a href="http://en.wikipedia.org/wiki/David_Heinemeier_Hansson">David Heinemeier Hansson</a> <br />give the keynotes at .ca on rails.</p>

<p><em>My notes in italics</em></p>

<ul>
<li>&#8220;It&#8217;s early&#8221; (it&#8217;s 11:15 his time).</li>
<li>Nothing as easy as GEMs, even for dynamic languages like Python :(.</li>
<li>Book explosion: 16 new rails books this year.  Last year there were only 4 on ruby at all.</li>
<li>Mainstream journals have picked up Rails (e.g. eWeek).  Quite a few mentions on /.</li>
<li><span class="caps">IBM</span> writer doing one article on something, then an article on Rails, one article on something, then Rails agian.  Good pattern.</li>
<li>Awards: O&#8217;Riely, then RadRail&#8217;s award.  <span class="caps">JOLT</span> award</li>
<li>All this indicative on an ecosystem.  Critical mass.</li>
<li>Screenfeld of people that have committed a patch.</li>
</ul>

<ul>
<li>Has been accused of being arrogant, he&#8217;s cool with that. He had a &#8220;exaggerated sense of one&#8217;s own importance or abilities&#8221; about Rails. 2 years ago Rails better than other solution in market.  50 revisions of David&#8217;s wikipedia page removing and readding &#8220;David is widely considered to be extremely arrogant.&#8221;</li>
<li>&#8220;Mostly doing this for me&#8221;. So he doesn&#8217;t have an problem with saying <a href="http://www.flickr.com/photos/planetargon/127984254/in/pool-canadaonrails/">Fuck You</a></li>
<li>Rails is saying FU to a lot of things other solutions want to do.</li>
<li>FU to having a smart db.  FU to everything should configurable.  Way too much objectivity, not enough subjectivity.</li>
<li>Rails has lots of opinions on how to do things. (_He saying sell the stack as a product rather than a wild open solution_)</li>
<li>Not going to OpenACS or Zope.  Represent a mindset that dev should be painful and avoided at all cost.  Thus they use components</li>
<li><em>I&#8217;m hungry no breakfest, maybe sushi for lunch</em></li>
<li>Don&#8217;t like the results of putting components together.</li>
<li>Rails == what most people want most of the time.</li>
<li>Todo list on 3 sites, but each is different in subtle ways. Rather than making a <span class="caps">TODO</span> component and ignore the diffs, abstract on a lower level: acts_as_list.</li>
</ul>

<ul>
<li>&#8220;WS-(deathstar)&#8221;: &#8220;I can about little things, like not going insane&#8221;</li>
<li>Care about ourselves, care about small teams doing big things, not enterprise happy (Yeah! (said like a 5 year old)).</li>
<li>No vender, <span class="caps">DIY</span>.</li>
</ul>

<ul>
<li><span class="caps">WHERE</span> <span class="caps">ARE</span> WE <span class="caps">ACTUALLY</span> GOING: Who knows?</li>
<li>It&#8217;s all about abstractions.  Not about a roadmap.  All the interesting features in 1.1 no idea he&#8217;d ever do.</li>
</ul>

<ul>
<li>Probably not what some of you wanted to hear, so (shows roadmap of 1.1.x &#8211; bugfix, 1.2.0, then 2.0.0)</li>
<li>Deprecation: 2.0 is where we settle the score.  Get rid of the baggage.  1.2.0 will put warnings in the log file.</li>
<li>If your app is working fine let it sit there.</li>
</ul>

<ul>
<li>Rails about infrastruction, not about biz logic.</li>
</ul>

<ul>
<li>Things going away (really becoming a plugin):
<ul>
<li>Components (use plugins)</li>
<li>JavaScript Macros</li>
<li>Pagination (not everyone wants the same pagination)</li>
<li>Rich has and belongs to many (use Join Models in 1.1)</li>
<li>Action Web Service</li>
</ul></li>
</ul>

<ul>
<li>Plugin: saying no to ideas without really saying no.  Do not burden core. <em>Eariler he talk about features in Rails that they get lots of bug reports on but none of core team use or care about</em>.</li>
<li>Do more of:
<ul>
<li>use <span class="caps">HTTP</span> features, like caching.  How do I know when I want to expire the cache.  acts_as_timestamp</li>
<li><span class="caps">REST</span>
<ul>
<li>Google Web Accelerator guys morons.  Designing for world that doesn&#8217;t exists.</li>
<li>make a link that does a <span class="caps">POST</span>.  Fix <span class="caps">HTML</span> problems (_Wish they could fix bloody <span class="caps">HTTP</span> auth_).</li>
<li>exposing <span class="caps">REST</span> api.  Need a single controller map two resources &#8220;/articles/&#8221; and then &#8220;/article/1&#8221;.  Something committed last night.</li>
<li>entities (&#8221;/article/1&#8221;) can be worked on via verbs</li>
<li>_If you are interested in this go read <a href="http://en.wikipedia.org/wiki/REST">this article on REST</a> _</li>
<li>Making the rest of Rails see everything as a REST-style request, and making browser base resquest look like <span class="caps">REST</span> to the framework.</li>
<li>Optional.  If you follow convention you get a lot of stuff for free.</li>
<li>In <a href="http://svn.jamisbuck.org/rails-plugins/simply_restful/">SVN</a></li>
</ul></li>
</ul></li>
<li>One more thing.  Campfire scales because bits are written in C.</li>
<li>Thus Armageddon, Push with <span class="caps">AJAX</span>.   Show demo.  Control browser from command line.  Turned h1 green.</li>
<li>Updated DB, and change propagated to another browser window.</li>
<li>Uses reusable 1&#215;1 flash to open a socket.to push <span class="caps">RJS</span> (_???_) down.   Don&#8217;t have to write a line of Flash.</li>
<li><em>I need a mac to use SubEthaEdit</em></li>
</ul>

<p>Q&A:</p>

<ul>
<li>what&#8217;s diff between components and plugins?  Size and if includes views and &#8230;, permission system is a component, not a plugin&#8230; too big.  People spend too long on getting plugins up and running when they could write it themselves quicker.  People coming to rails with battle scars of what Software Dev used to be.</li>
</ul>

<p><a href="http://37s.campfirenow.com/eb527">Canada on Rails Campfire Room</a></p>

<p><a href="http://www.flickr.com/groups/canadaonrails/pool/">Canada on Rails Flickr Pool</a></p>

