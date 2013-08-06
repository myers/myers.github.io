---
layout: post
title: "Higher level protocols for websockets"
date: 2013-04-19T10:07:46
tags: ["ideas"]
---

I ran across [WAMP](http://wamp.ws/spec#welcome) recently.  When I built my DC++ client who's primary GUI is a jquery/jquery ui web app connected to the twisted python backend via websocket I had to create something just like this.  Later reading over the [JSON RPC 2.0](http://www.jsonrpc.org/specification) spec I realized you could just use their format and leverage json rpc libs already written.  

Small note: you might want to remove the "jsonrpc" key from the request and response to save some bytes.

There is also this: [Cutting Down Bandwidth with JSON Alternatives](http://blog.gradientstudios.com/2012/08/15/cutting-down-bandwith-with-json-alternatives/)

