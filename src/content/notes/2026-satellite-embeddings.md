---
title: "Satellite embeddings add two points over the image-only baseline"
date: 2026-05-02
summary: "Early multimodal results: adding Google Satellite Embeddings to ground-level imagery gives +2pp top-1. Smaller than hoped, and informative about why."
tags: ["ai-hab", "multimodal"]
draft: true  # written by Claude from CV facts — review before publishing
---

Internal result, not yet written up. Extending AI-Hab beyond image-only
assessment by combining three views of the same location — the ground-level
photograph, Google's Satellite Embeddings for the coordinate, and an
LLM-derived ecological description — gives a **two-percentage-point top-1
gain** over the image-only baseline.

Two points is real but modest, and the shape of it matters more than the size.
The gain is not spread evenly across classes; it concentrates where the
ground-level photograph is genuinely ambiguous and the surrounding landscape
context is not. A photograph taken facing down at a sward tells you about the
sward. The satellite embedding tells you what the sward sits inside.

That suggests the ceiling here is not "more modalities" but "modalities that
disagree in useful places". Next test is whether disagreement between the
image-only and multimodal predictions is itself a usable confidence signal for
routing observations to a human.
