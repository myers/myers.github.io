---
layout: post
title: "Practical Deep Learning: Lesson 1: Is it a Hotdog?"
date: 2023-04-30T15:51:34-0400
tags: [machine-learning]
---

[Practical Deep Learning for Coders](https://course.fast.ai/) [Lesson 1](https://course.fast.ai/Lessons/lesson1.html)

The biggest change since I last took a course on Machine Learning is one of the key points of this course:  the use of foundational models that you fine tune to get great results.  In this lesson's video we fine tune an image classifier to see if a picture has a bird in it.

While building my own model I attempted to get the classifier fine tuned to look at comic book covers and tell me what publisher it was from.  I thought with the publishers mark on 100 issues from Marvel, DC, Dark Horse, and Image the classifier would be able to tell.  The best I was able to do was about 30% error rate.  I tried a few different ideas of how to improve:

- train with larger images.  The notebook used in the video makes the training go faster by reducing the size of the image.  As I write this I wonder if it is even possible to use larger images in a model that might have been trained on a fixed size.
- create a smaller image by getting the 4 corners of the cover into one image.
- clean the data so that all the covers in the dataset had a publisher mark on them.

 <figure>
  <img src="/2023/04/30/X-Men - Red (2022-) 001-000.jpg" width="372" height="573" />
  <figcaption>sample cover with only the corners</figcaption>
</figure>

Nothing moved the needle.  I'm hoping something I learn later in the course will give me the insight I need to do better.

I took a second attempt with a simpler project.  Of course I remembered that Silicon Valley episode with the hot dog detector, and make a hot dog vs hamburger classifier.  It works great.  The next lesson covers getting a model like that into production, so hang tight.
