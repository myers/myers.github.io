---
layout: post
title: "Joy's of netfilter"
date: 2004-03-30T23:26:14
tags: []
---

This weekend I found enough RAM to put in one of my boxes called "mp3slave" so that it can run mldonkey and btmanager at the same time again. With all the downloads I have they take up about 300mb and will swap like crazy if they have less than that. 

Then the other reason I havn't been using bittorrent kicked in: slow downloads. I had wondershaper up and running but the way I categorized traffic was bad. I knew everythink p2p related was coming from one machine and one user. So on that machine I put 

    `iptables -t mangle -A OUTPUT -m owner --uid-owner p2p -j MARK --set-mark 1`

And then got `tc` to put those packets into their own class 

    `/sbin/tc filter add dev eth1 parent 1:0 protocol ip prio 200 handle 1 fw classid 1:20`

So now all the p2p traffic is stuck in one class using no more than 3/4 of my outgoing traffic. 

Oh and one more discovery: my outgoing while on dsl was 256Kbit/s, on cable modem it's 512Kbit/s. Quite a step up. 


