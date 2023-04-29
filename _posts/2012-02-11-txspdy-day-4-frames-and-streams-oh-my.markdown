---
layout: post
title: "txspdy: Day 4: frames and streams oh my"
date: 2012-02-11T12:07:36
tags: [txspdy]
---

Last night was light on hacking time.  Did a lot of reading of the twisted.web code.  What I would like to end up way to create a duel https/spdy exposing the same `Resource` instance tree.  Unfortunately it seems like the `Site` class is a subclass of a `HTTPFactory` where it would be better for this if it had a ref to that factory.

I used some code from nbhttp to parse the frames and frame headers for a single request.  Next up is creating the headers and response frame.  Then we'll have enough for a "hello world".
