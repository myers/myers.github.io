---
layout: post
title: "python-bitzi 0.1 Released"
date: 2003-12-02T01:08:56
tags: [python]
---

I've put out a python wrapper around the bitzi library. It's good at
extracting some metadata out of files. It should be useful for other p2p
hackers. You can download it on my [python-bitzi][1] project page.

An example of it's usage

    >>> import bitzi, pprint
    >>> bc = bitzi.Bitcollider()
    >>> ret = bc.analyze('/home/myers/zim_propaganda_r5_c1.gif')
    >>> pprint.pprint(ret)
    {'bitprint': 'XIUF4RY3UTHYAYVP2SUVWPP45E4LPQWA.74QG2SYGG7SFVRSSR4BN6BNEAFBTOVRTR7LLFJA',
     'head.agent': 'Bitprinter/0.5.1 (Dec  1 2003 16:15:19)',
     'head.version': 'S0.4',
     'tag.ed2k.ed2khash': '19fd58da4d5b9236d8e0706d1b6b14e9',
     'tag.file.first20': '47494638396164020202D500000000008C0B0699',
     'tag.file.length': '8348',
     'tag.filename.filename': 'zim_propaganda_r5_c1.gif',
     'tag.image.bpp': '6',
     'tag.image.format': 'GIF',
     'tag.image.height': '514',
     'tag.image.width': '612',
     'tag.uuhash.uuhash': 'klaiKcvdxJb+gfmSlMz5ZWPf//8'}

   [1]: /projects/python-bitzi/
