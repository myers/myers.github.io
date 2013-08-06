---
layout: post
title: "Tunetagger progress"
date: 2002-06-07T05:16:36
tags: []
---

Ugg... 

I couldn't sleep last night and I had no internet, due to a massive power out on the north side of town, so I played with the mozilla embed widget in python. I now have a fully usable browser (back/forward/stop/location bar/status bar) in about 150 lines of python. 

One problem I had was when submitting to a form it wanted a new window to tell me about submitting form insecurely is a bad idea, but the gtk signal handler was expected to hand back a handle (pointer to a pointer) to a new mozilla embed widget. Python didn't know how to do that, and the way they have it designed is funky (the signal handler could return this instead of setting the handle). I also can't set the prefs without pyxpcom which I don't feel like going to trouble of building. 

Perhaps it would be easier to actually write a better thought out wrapper for wxWindows and then use that. Then it should be reusable on the mac and win32 (I hope!). 

Off to work... oh wait... I work at home... 


