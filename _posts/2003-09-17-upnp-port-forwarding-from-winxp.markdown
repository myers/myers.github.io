---
layout: post
title: "UPnP Port Forwarding from WinXP"
date: 2003-09-17T08:37:34
tags: [python]
---

In a P2P app (say like [Mnet][1]) you need as many full peer (computers that can receive incoming connections as well as outgoing). Lots of homes now have (probably full of security holes) [UPnP][2] routers that will allow you to forward incoming connection to comptuers behind it.

I'm trying to learn how to monkey with this. On linux you might need to grok SOAP and learn whatever way M$ broke the standards with that ([SOAPAction][3] is a pain in the ass), but on WinXP you should be able to make some w32 api calls and have some COM object do the network calls for you.

So quickly poking around I found [Programmatically Controlling a UPnP-Capable Firewall][4], on how to control port forwarding via COM in VB... and since I want to do this in python I found [Quick Start to Client side COM and Python][5].

If I write some python to do this I will post it here.

   [1]: http://mnet.sf.net/
   [2]: http://www.upnp.org/
   [3]: http://216.239.33.104/search?q=cache:apghERVzlegJ:www.oreillynet.com/cs/weblog/view/wlg/2331+soap-action&hl=en&ie=UTF-8
   [4]: http://www.knoxscape.com/Upnp/NAT.htm
   [5]: http://www.python.org/windows/win32com/QuickStartClientCom.html
