---
layout: post
title: "Using Ruby's SVN bindings"
date: 2008-09-25T17:11:25
tags: [ruby]
---

I couldn't find the simplest example of using Ruby's SVN bindings.  Here's something simple, get the info on some file in a local working directory.

    require 'svn/client'

    ctx = Svn::Client::Context.new
    ctx.add_simple_provider
    ctx.info('some file in your svn working dir') do |path,info|
      p path
      p info.last_changed_rev
    end

[This page](http://www.oneofthewolves.com/2007/03/06/ruby-subversion-bindings-finally-some-documentation/) is also useful.
