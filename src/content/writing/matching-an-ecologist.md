---
title: "What it means to say a model matched an ecologist"
date: 2026-02-20
summary: "Our habitat classifier performs comparably with an experienced ecologist. That sentence is doing more work than it looks, and most of the work is in the word 'comparably'."
tags: ["ai-hab", "evaluation", "computer-vision"]
draft: true  # written by Claude from CV facts — review before publishing
---

> Draft. This piece is a starting point assembled from the paper's results — the
> argument is mine to defend and every sentence is still up for revision.

The result in our [*Ecological Informatics*
paper](https://doi.org/10.1016/j.ecoinf.2026.103751) that people repeat back to
me is that the model "performs comparably with an experienced ecologist". It is
an accurate sentence. It is also the sentence most likely to be misread, and I
want to set out exactly what it does and does not claim.

## The claim, stated precisely

We asked three experienced ecologists to label a stratified held-out subset of
Countryside Survey photographs into the same 18 UKHab-aligned classes the model
predicts. The best model reached 71.5% top-1 accuracy against the reference
labels. The strongest of the three ecologists was in the same region. The other
two were lower.

So the honest phrasing is: *on this task, on this data, against these reference
labels, the model sits at the top of a three-person human range.* Every clause
in that sentence is load-bearing.

## Why top-1 is the wrong number to fixate on

Top-3 accuracy was 90.9%. The 19.4-point gap between top-1 and top-3 is not
noise — it is the shape of the problem.

If we write top-$k$ accuracy over a test set of $N$ observations as

$$
\mathrm{Acc}_k = \frac{1}{N}\sum_{i=1}^{N} \mathbf{1}\!\left[y_i \in \mathcal{T}_k(x_i)\right]
$$

where $\mathcal{T}_k(x_i)$ is the set of $k$ highest-scoring classes for image
$x_i$, then a large $\mathrm{Acc}_3 - \mathrm{Acc}_1$ tells you the true class
is nearly always *in contention* and the model is losing on the final
discrimination. That is a very different failure from not knowing what it is
looking at.

Where does it lose? Overwhelmingly among the grasslands. Improved Grassland,
Neutral Grassland and their neighbours are separated by management history and
species composition that a single photograph may simply not contain. Adding
contrastive learning raised class-specific recall by six percentage points for
Improved Grassland and five for Neutral Grassland — a real gain, and one that
targeted exactly the classes where the confusion lived rather than lifting the
average.

## The reference labels are not the ground truth

Here is the part that gets skipped. We evaluate the model and the ecologists
against reference labels that were themselves produced by people. When a model
"disagrees" with the reference label, there are at least three possibilities:
the model is wrong, the reference label is wrong, or the photograph does not
determine the answer.

Class imbalance makes this worse in a specific way. Rare classes have fewer
labelled examples, which means both that the model has less to learn from and
that the reference labels for those classes have had less scrutiny. The
measured error rate on a rare class is a sum of model error and label error,
and the split between them is not identified by the accuracy number alone.

This is why the workshop feedback that mattered was about error structure
rather than accuracy. Clustering-based review of potentially mislabelled
observations is not a nicety bolted on after the modelling. It is part of
knowing what the 71.5% means.

## What "comparable to an expert" should license

A reasonable reading: for the classes where photographs are informative, an
automated pass over a large photographic archive can produce labels of roughly
expert quality at a cost that makes the archive usable at all. The Countryside
Survey holds far more photographs than anyone will ever hand-label. That is the
actual value proposition, and it does not require the model to beat anybody.

An unreasonable reading: the model can replace the ecologist. It cannot,
because the cases it gets wrong are not randomly distributed. They concentrate
in exactly the distinctions that matter most for management decisions —
distinguishing improved from semi-natural grassland is not a tie-break, it is
often the point of the survey.

The useful framing is triage, not replacement. A model that is right 71.5% of
the time and *knows which 71.5%* is far more valuable than one that is right
75% of the time and is uniformly confident. That is the direction the
multimodal work is going: not chasing top-1, but making disagreement between
views into a signal for which observations a human should look at.

## What I would want checked

If you want to poke holes, these are the load-bearing joints:

- Three ecologists is a small human sample. The range between them was wide
  enough that "comparable to an expert" would read differently if we had
  sampled three others.
- The held-out subset was stratified, which makes the comparison fairer per
  class but means the headline number is not a straight estimate of performance
  on the archive's natural class distribution.
- Reference-label error is acknowledged but not quantified. I do not have a
  clean estimate of it, and that is the single biggest caveat on everything
  above.

The [code and trained models](https://github.com/WhiteGiveFive/Habitat-Classification-from-Ground-Level-Imagery)
are public, and the [demonstrator](https://huggingface.co/spaces/whitegivefive/aihab-demo)
takes an uploaded photograph if you want to try to break it.
