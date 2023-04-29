---
layout: post
title: "Happy fun python snippit"
date: 2003-08-25T09:07:41
tags: [python]
---

An example of how to add a method to a class, and how to add to just an instance of object.

    import new

    # add method to all object of a class

    class test:
        pass

    def monkey(self):
        print "eek"

    tta = test()
    ttb = test()
    tta.__class__.monkey = monkey
    print "%r" % tta.monkey
    print "%r" % ttb.monkey

    # add to one instance

    class test2:
        pass

    tt2a = test2()
    tt2b = test2()

    tt2a.monkey = new.instancemethod(monkey, tt2a, tt2a.__class__)

    print "%r" % tt2a.monkey
    # this will cause an exception
    print "%r" % tt2b.monkey
