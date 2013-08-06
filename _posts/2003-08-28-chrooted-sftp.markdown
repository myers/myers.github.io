---
layout: post
title: "Chroot'ed sftp"
date: 2003-08-28T09:34:39
tags: []
---

Today I made our new server at work only let some people to use sftp on login, and made sftp-server chroot before running. This was on a RedHat 8.0 box. 

First I downloaded the openssh source, using [apt][1] with the command `sudo apt-get source openssh`. Then I tried to run `rpm -ba /usr/src/redhat/SPECS/openssh.spec`, but of course that didn't. After much poking around on google I found that rpmbuild -ba would do the trick. That of course failed half way thur, but I did poke into the `openssh.spec` file and found out what options it passed to `./configure`. I unpacked the tarball myself, then ran `./configure` with the right options. Then I applied the [ `sftp-chroot.diff`][2] patch and did `make sftp-server`. I copied that file to `/usr/libexec/openssh/sftp-server-chroot`, and did `chmod +s /usr/libexec/openssh/sftp-server-chroot`. 

Then I edited `/etc/passwd` and added the magic chars "/." to the users path, and changed their shell to `/usr/libexec/openssh/sftp-server-chroot`. And it worked. 

   [1]: /2003/08/26/for-those-stuck-on-redhat/
   [2]: http://mail.incredimail.com/howto/openssh/addons/sftp-chroot.diff"



