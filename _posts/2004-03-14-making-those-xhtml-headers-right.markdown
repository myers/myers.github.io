---
layout: post
title: "Making those xhtml headers right"
date: 2004-03-14T22:18:32
tags: []
---

Apache can make it easy for you to give the right mime type for xhtml docs. 
    
    
    # server all files w/ ext .xhtml as application/xhtml+xml to those that can
    # handle it
    AddType  application/xhtml+xml xhtml
    
    RewriteEngine On
    RewriteCond %{HTTP_ACCEPT} !application/xhtml\+xml
    RewriteCond %{HTTP_ACCEPT} (text/html|\*/\*)
    RewriteCond %{REQUEST_FILENAME} .*\.xhtml
    RewriteRule ^.*$ - "[T=text/html,L]"
    


