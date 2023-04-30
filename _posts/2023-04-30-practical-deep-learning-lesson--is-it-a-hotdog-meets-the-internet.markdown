---
layout: post
title: "Practical Deep Learning: Lesson 2: Is it a Hotdog? meets the Internet"
date: 2023-04-30T16:16:52-0400
tags: [machine-learning]
---

[Practical Deep Learning for Coders](https://course.fast.ai/) [Lesson 2](https://course.fast.ai/Lessons/lesson2.html): Let's share this with the world.

I have shipped even more ML code: [Hotdog or Not?](https://huggingface.co/spaces/myers/hotdog-or-not)

<figure>
  <img src="/2023/04/30/hf-hotdog-or-not.jpg" width="2568" height="1122" />
  <figcaption>my first model deployed on Hugging Face 🤗</figcaption>
</figure>

Hugging Face 🤗 is darn slick.  Your project is built into a docker image and then launched as needed.  Github could learn a thing or two about showing status.  There was some errors due to the `fastai` API changing to no longer needing you to wrap an image that you want to predict in a `PILImage` and another problem with adding example images, that I solved by just removing them.
