---
layout: post
title: "WebXR + WebGPU on Quest 3 via Virtual Desktop"
date: 2025-10-24T11:03:39-0400
tags: [webxr webgpu]
---
I saw [this
post](https://toji.dev/2025/03/03/experimenting-with-webgpu-in-webxr.html)
with a demo link in it, and wondered: can I use my quest 3 with virtual
desktop to try this WebGPU + WebXR demo out?

WebGPU is the modern way to tap into your computer's graphics card (GPU)
directly from a web browser.  Before WebGPU, browsers used an
older technology called WebGL, which worked but was kind of showing its age.
WebGPU is faster, more efficient, and gives developers way more control over
how they use the GPU.

WebXR you experience virtual reality (VR) and augmented reality (AR)
directly through your web browser.  The "XR" stands for "extended reality,"
which is just a catch-all term for both VR (where you're fully immersed in a
virtual world) and AR (where digital stuff gets overlaid on the real world).
So if you've got a VR headset like a Meta Quest, WebXR lets websites tap
into that hardware and create immersive experiences.

The Chrome team is working towards allowing you to use WebGPU to power
WebXR, but it's not in the navtive Quest Browser.

I couldn't get a good answer about if it would work, and if not, why not
from Claude Research.  The answer is it does work.

1. Buy Virtual Desktop
2. In Chrome go to `chrome://flags` and turn on any flags to do with WebGPU.
3. Put on your Quest 3 and connect to your desktop via Virtual Desktop
4. go to
[`https://toji.github.io/webgpu-metaballs/`](https://toji.dev/2025/03/03/experimenting-with-webgpu-in-webxr.html)
5. in the panel on the right, open the WebXR section
6. enjoy the lava.

I tried a bunch of the [threejs examples](https://threejs.org/examples/) and they don't all work correctly.
