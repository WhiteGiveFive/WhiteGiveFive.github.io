---
title: "AI-Hab paper out in Ecological Informatics"
date: 2026-01-15
summary: "Ground-level photographs classify into 18 UKHab-aligned habitat classes at 71.5% top-1, comparable to an experienced ecologist."
tags: ["ai-hab", "computer-vision", "publication"]
draft: true  # written by Claude from CV facts — review before publishing
---

The AI-Hab classification paper is out in *Ecological Informatics*:
[Habitat classification from ground-level imagery using deep neural
networks](https://doi.org/10.1016/j.ecoinf.2026.103751).

The short version: given a single ground-level photograph from the UKCEH
Countryside Survey, a fine-tuned vision model places the site into one of 18
fine-grained UKHab-aligned habitat classes at **71.5% top-1** and **90.9%
top-3** accuracy. On a stratified held-out subset, that is comparable to the
strongest of three experienced ecologists labelling the same photographs.

We compared nine convolutional and vision-transformer architectures under one
training and evaluation pipeline, so the comparison is about the architectures
rather than about who tuned what. Code, trained models and a demonstrator are
public — the [demo](https://huggingface.co/spaces/whitegivefive/aihab-demo)
takes an uploaded photo.

The number I keep coming back to is not 71.5%. It is the gap between top-1 and
top-3: 19.4 points. That gap is where the confusable grassland classes live,
and it is the part of the problem that better architectures did not fix.
