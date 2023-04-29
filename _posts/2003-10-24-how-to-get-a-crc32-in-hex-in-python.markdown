---
layout: post
title: "How to get a CRC32 in Hex in Python"
date: 2003-10-24T11:12:50
tags: [python]
---

Before I did this:

    import zlib

    def crc32(filename):
        return "%08x" %  zlib.crc32(file(filename, 'r').read())

But in python2.3 that gives a warning:

    FutureWarning: %u/%o/%x/%X of negative int will return a signed string in Python 2.4 and up

So I changed it to:

    import zlib, binascii, struct

    def crc32(filename):
        bin = struct.pack('!l', zlib.crc32(file(filename, 'r').read()))
        return binascii.hexlify(bin)

I tested these two on a few thousand files and they seem to both have the exact same results.
