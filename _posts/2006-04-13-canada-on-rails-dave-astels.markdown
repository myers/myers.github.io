---
layout: post
title: "Canada on Rails: Dave Astels"
date: 2006-04-13T18:19:41
tags: ["canada-on-rails"]
---

<p><a href="http://canadaonrails.com/talks/show/4">Dave Astels on Behaviour Driven Development.. the step after TDD</a></p>

<p><a href="http://blog.daveastels.com/">Dave Astels&#8217; Blog</a></p>

<p><em>Looks interesting now if only to see what a <a href="http://www.starwars.com/databank/species/wookiee/">wookie</a> looks like in real life</em></p>

<h4>Act I</h4>

<ul>
<li>Not about creating a bunch of test, but doing design via tests.</li>
<li>Sapir-Wharf: language is important.  The language you use effects and shapes your thoughts</li>
<li>Think Different: yes I do have a powerbook.</li>
<li>Not <span class="caps">TDD</span> but Behaviour DD.</li>
<li>Danial North coined the term.</li>
<li>classic mistake in TDD: do something look at state</li>
<li>never write a private method.</li>
<li>You should not be looking at the internal state of the object. </li>
</ul>
(state with a big red x thru it)
<ul>
<li>Stubs are not Mocks (_I&#8217;m currently reading an article about this: <a href="http://www.martinfowler.com/articles/mocksArentStubs.html">Martin Fowler: Mocks Aren&#8217;t Stubs</a> _)</li>
</ul>

<h4>Act II</h4>

<ul>
<li><a href="http://rubyforge.org/projects/rspec/">rSpec</a> (also in gems)</li>
<li>a way to describe specs in code, then test against those specs</li>
<li>rather than <code>assert_equal(a, b)</code> do <code>actual.should.equal expected</code></li>
<li><code>object.question?</code> should be vocalized as &#8220;question, eh?&#8221;</li>
</ul>

<p><em>The talk is bogging down into him showing every possible combo of this .should biz enabled by rSpec.  This is great lesson about what I don&#8217;t think makes a good conf. talk</em></p>

<ul>
<li>Mocking <span class="caps">API</span></li>
<li>Mocks are auto verified, stubs are not</li>
</ul>

<h4>Act <span class="caps">III</span></h4>

<ul>
<li>Code, Questions and Discussion</li>
</ul>

<p><span class="caps">DSL</span> &#8211; Domain-Specific Language</p>

<ul>
<li>one more thing: shows up some code he hacked on the plane</li>
</ul>

