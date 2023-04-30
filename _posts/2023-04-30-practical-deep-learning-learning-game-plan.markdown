---
layout: post
title: "Practical Deep Learning: Learning Game Plan"
date: 2023-04-30T15:31:21-0400
tags: [machine-learning]
---

I dug this video up from the older version of [Practical Deep Learning for Coders](https://course.fast.ai/).  It's a "learn how to learn" type video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/gGxe2mN3kAg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

My take aways:

- Practical work is the goal.  Don't fool yourself into thinking you know what is taught by just watching the videos or reading the book.  Watch the video, watch it again but with the tools at hand, pausing to try stuff out, do a project using what you learned.
- I have my own ML workstation setup with a GPU.  I used poetry to set it up.  This was a pain due to lack of attention to repeatability.  Below is what it looks like after finishing Lesson 1 (the next video).
- Be tenacious.  Finish a project.
- One message that's very close to my heart is not keep on getting ready to do a project, like stopping to learn [linear algebra](https://www.khanacademy.org/math/linear-algebra) (and then remembering how I never learned all the math terms, and therefore want to go back even deeper) in order to do well on this course.  Try to do a complete project, then on the next project go deeper, dig in deeper when the code needs it.
- Show your work to the world.  Blog not to be a breaking news source, but blog for the audience of yourself 6 months ago.

`pyproject.toml`

```toml
[tool.poetry]
name = "dl"
version = "0.1.0"
description = ""
authors = []
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"
fastai = "2.7.11"
duckduckgo-search = "^2.8.5"
ipykernel = "^6.22.0"
ipywidgets = "^8.0.5"
jupyterlab = "^3.6.3"
jupyterlab-git = "^0.41.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
