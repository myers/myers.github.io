---
layout: post
title: "CD Ripping on Win98"
date: 2004-05-01T08:35:56
tags: []
---

<p>On reason people have suggested that P2P took off was that people could not easily rip their own CD&#8217;s on to their computer.  After trying to rip a CD on a stock Win98 box I believe it.  I tried both <a href="http://www.audiograbber.com-us.net/">Audiograbber</a> which didn&#8217;t work out of the box (or rather it popped with a warning).</p>

<p>Then I tried <a href="http://cdexos.sourceforge.net/">CDex</a>, which said it required the &#8220;Adaptec&#8217;s ASPI&#8221;:http://www.adaptec.com/worldwide/support/driverdetail.jsp?cat=%2fProduct%2fASPI-4.70&filekey=aspi_471a2.exe&sess=no  driver, which once installed didn&#8217;t show the CD drive. Maybe because it isn&#8217;t a Adaptec product?</p>

<p>Then after consulting <a href="http://www.nu2.nu/aspi/">Bart&#8217;s page about ASPI</a> I tried the Nero&#8217;s <span class="caps">ASPI</span> (no installer, you have to copy files into c:\windows yourself, ug!)  CDex started, but complained that it wanted the &#8220;orignal&#8221; wnaspi32.dll.  I just ripped a track and it appears to work, just really slow (like 1x speed).</p>

<p>Since I was trying to take a survey of how different programs used the <span class="caps">MCDI</span> frame in id3v2 tags, I tried AudioGrabber again, which now sees the Nero <span class="caps">ASPI</span> driver and has the <strong>exact</strong> same dialog warning me that it&#8217;s not the &#8220;orignal&#8221; wnaspi32.dll.  Looks like AudioGrabber is based some what on some thing CDex is (CDex is <span class="caps">GPL</span>, so that would be a no-no).  The option to get it to include a <span class="caps">MCDI</span> frame is deep in some config dialog, <br />not on by default.</p>

<p>What a total pain in the butt.  But I did get my two example tracks.</p>

<p>CDex work under WinNT based systems, because M$ added calls to access <span class="caps">CDDA</span> in those versions, but it still pops up a warning first.</p>

<p>Given the grief it took to rip my own CD on a Napster Era PC I can totally believe people would get on Napster to just get music they already owned on their computer.  Not that I think that&#8217;s all they did.</p>

