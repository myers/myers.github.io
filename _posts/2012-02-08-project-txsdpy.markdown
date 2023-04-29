---
layout: post
title: "Project: txsdpy"
date: 2012-02-08T18:14:53
tags: [txspdy]
---

A [ShRUG](http://ruby.meetup.com/128/) this week someone mentioned a guy who was working a project every night and blogging about the progress he was making.  He was up to 200+ days of this.  I thought I'd try to do the same.

So first project: txspdy - a python twisted implementation of a [SPDY](http://www.chromium.org/spdy) server.

### Why?

 1. knowing http has helped in my day job and protocols are fun.  XMPP hacking was a lot of fun.
 2. new shiny
 3. websockets over spdy sounds awesome.  I've used websockets to build a app UI for a DirectConnect client I've written.

### Why hasn't anyone else done this yet?

There is a [python prototype](http://github.com/mnot/nbhttp/tree/spdy) linked off the SDPY page, but it's doesn't use twisted.  I will, no doubt, be reading over that code.  The fun thing is that no one knows if SDPY will take off.

### First problem

SPDY uses a new SSL extension to tell connecting clients what protocols the server can speak.  OpenSSL has a beta version that implements this extension, but you can't use it via [pyopenssl](http://pypi.python.org/pypi/pyOpenSSL/).  So I've checked that out and started hacking on the C code for it.

I wanted to test that I could get Chrome to talk SPDY to a test server before I went much further.  First thing you need are some real ssl certs.  I had some from StartCom.  I used the openssl binary like this:

    /usr/local/ssl/bin/openssl s_server -key server.key \
       -cert server.crt -accept 9000 -www -nextprotoneg spdy/2,http/1.1 -debug

My first attempts with a self signed cert resulted in Chrome connecting and stopping the ssl handshake 3 times then using http/1.1 even thought I had spdy listed too.  Not sure what the purpose of that was.
