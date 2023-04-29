---
layout: post
title: "Undocumented weird thing with hard links and rename(2)"
date: 2004-07-04T07:23:45
tags: []
---

Try this:

    myers@soap:~/tmp$ touch a
    myers@soap:~/tmp$ link a b
    myers@soap:~/tmp$ mv a b
    myers@soap:~/tmp$ ls
    a  b

What? Why is "a" still around? Turns out rename(2) will not delete the first file in a rename if the second is linked to the same inode. AND the man page doesn't say anything.
