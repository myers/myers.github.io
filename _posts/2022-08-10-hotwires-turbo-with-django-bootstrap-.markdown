---
layout: post
title: "HotWire's Turbo with Django Bootstrap 5"
date: 2022-08-10T20:59:42-0400
tags: [django, hotwired, turbo]
---

If you use turbo and django-bootstrap5 drop downs will not work once you
load another page.  You can fix this by adding the
`data-turbolinks-eval=false` attribute to bootstrap's `<script>`.

`settings.py`

```python
from django_bootstrap5.core import BOOTSTRAP5_DEFAULTS

BOOTSTRAP5 = {
    "javascript_in_head": False,
    "javascript_url": BOOTSTRAP5_DEFAULTS["javascript_url"].copy()
}
BOOTSTRAP5["javascript_url"]["data-turbolinks-eval"] = "false"
```
