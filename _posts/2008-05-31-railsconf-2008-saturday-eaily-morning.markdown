---
layout: post
title: "RailsConf 2008: Saturday Eaily Morning"
date: 2008-05-31T13:31:06
tags: [railsconf2008]
---

<p>(mostly randy here again. I was putting up my first ec2 instance. :)</p>

<h4>Saturday Keynotes</h4>

<ul>
<li>funny video from the RailsEnvy guys about testing</li>
</ul>

<h5><span class="caps">DHH</span> introducing Jeremy Kemper</h5>

<ul>
<li>Jeremy has done a buttload of work lately in the Rails core</li>
<li>dhh on a coding vacation?</li>
<li>some people think about one part of rails Jeremy thinks about the whole thing</li>
</ul>

<h5>Jeremy&#8217;s talk about Rails 2&#8230; where it&#8217;s going, etc</h5>

<ul>
<li>&#8220;it&#8217;s all about resources&#8221;</li>
<li>&#8220;we shed a lot of fat&#8221; &#8211; split things off into plugins</li>
<li>&#8220;we gained speed&#8221; &#8211; &#8220;i&#8217;m not concerned about rails being super super quick&#8221; &#8212; huh???</li>
<li>1600 patches&#8230; it&#8217;s hard to read all that code!  so we embraced git and lighthouse instead of svn and trac</li>
<li>Rails 2.1
<ul>
<li>refactoring</li>
<li>documentation</li>
<li>thinner + faster</li>
<li>(he looks exhausted&#8230; too much free five runs beer and cheese pies)</li>
<li>he wants rails to look pretty.</li>
<li>use rubyprof</li>
<li>merging migrations</li>
<li>making timezones fitter, happier, more productive</li>
<li>migrations now have change_table block for modifying tables (just like create_table)</li>
<li>gem dependencies</li>
<li>improved memcache&#8230; making it a first-class citizen in rails.  memcache-client now bundled with rails</li>
<li>much of what he&#8217;s covering Myers read in <a href="http://www.akitaonrails.com/2008/5/25/rolling-with-rails-2-1-the-first-full-tutorial-part-1">this tutorial on rails 2.1</a></li>
<li>dirty &#8211; AR now knows when an attribute has changed
<ul>
<li>message.body_changed?</li>
<li>message.body_was</li>
<li>message.changed?</li>
<li>enables partial updates</li>
</ul></li>
<li>smarter :include &#8212; it&#8217;s not as eager to join on the first query.  this seems like it will be slower, but benchmarking supposedly proves that querying the join table on an as-needed basis is faster</li>
<li>named_scope
<ul>
<li>so you can say user.messages.recent instead of user.recent_messages by saying named_scope :recent, :order -> 'created_at desc&#8217; in the Message model</li>
</ul></li>
<li>Message.scoped(:limit => 10)</li>
<li>jruby -S jetty_rails (run rails on jruby)</li>
<li>rbx script/server (run rails on rubinius) </li>
<li>rails now runs on ruby 1.9</li>
</ul></li>
<li>rails 2.1 out today (a gem update at 10:14am didn&#8217;t do anything tho&#8230; it will be later&#8230; so not a Steve Jobs &#8220;and you can buy it right now&#8221;)</li>
</ul>
