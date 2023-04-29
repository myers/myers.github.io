---
layout: post
title: "DBS Wiki and OpenDBS update"
date: 2002-08-14T19:06:06
tags: []
---

I've started a [Wiki][1] on Digital Bearer Settlements. There are a lot of sites out there with links to papers, but I wish to write analysis and synthesis of the info out there. I only have the barest amount of stuff on there thus far, but if you felt so inclined add some stuff.

I'm working a cryptomonkey.net logo in Gimp. Think cartoon monkey outline on top of a hex dump of the Declaration of Independence. No, I didn't read too much cyberpunk while growing up.

Of course what I really want is Ryan to reply to my email about [OpenDBS][2], preferably with a link to some source code.

Oh yeah, I haven't mention here what I found out from him at H2K2 because I didn't want to steal any thunder from his talk at Defcon (which I'm looking for an mp3 of). [Kevin Burton][3] made [some notes][4] of the talk, but I'm not sure how much of these details he gave out.

There is code (that's a good start). It's in python (yeah!). It makes use of the [Cryptix][5] crypto lib, from which we can extrapolate that the code is in Jython, not the C based Python we know and love. Ryan initially wants to have the whole system (client wallet and all) hosted on Sealand accessable via a web interface while he works out the client-server protocol (this I wish to change his mind on. I'm not total sure what he means by that, the diffrent digital bearer systems take care of what numbers you send, and why not use XML-RPC/SOAP/XML-REST for the packaging of those numbers?). He has code for Chaum and Wagner type digital cash, and wishes to add Brands as well.

   [1]: http://cryptomonkey.net/dbs/
   [2]: http://opendbs.com
   [3]: http://www.peerfear.org/
   [4]: http://www.peerfear.org/rss/permalink/1028322224.shtml
   [5]: http://www.cryptix.org/
