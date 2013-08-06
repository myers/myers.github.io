---
layout: post
title: "How to find how much space a file is really taking"
date: 2005-03-01T19:04:26
tags: []
---

<p>Azerus the bittorrent client creates a sparse file for every file in the torrent you are downloading.  I had a 52GiB torrent I only wanted 10 files from.  When it got done ls -l couldn&#8217;t tell me which files had stuff in them.</p>

<p>After searching for a way to find out if a file makes use of the sparse file trick I discovered that it&#8217;s quite possible that <strong>any</strong> file that has nulls in it might be sparse.  Oh great&#8230;</p>

<p><code>du</code> turned out to actually show how much space on disk the file was taking.  I couldn&#8217;t find anything that linked <code>du</code> to sparse files so&#8230; here it is.</p>

