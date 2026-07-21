---
arxiv_id: s2:6e6d3daeb11675414391bd935a9e4e84dcff8d47
title: Audio-Driven Talking Head Video Generation with Diffusion Model
authors:
  - Yizhe Zhu
  - Chunhui Zhang
  - Qiong Liu
  - Xi Zhou
submitted: "2023-06-04"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/6e6d3daeb11675414391bd935a9e4e84dcff8d47
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-21T00:25:42+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Synthesizing high-fidelity talking head videos by fitting input audio sequences is a highly anticipated technique in many applications, such as digital humans, virtual video conferences, and human-computer interaction. Popular GAN-based methods aim to align speech audio with lip motions and head poses. However, existing methods are prone to training instability and even mode collapse, resulting in low-quality video generation. In this paper, we propose a novel audio-driven diffusion method for generating high-resolution realistic videos of talking heads with the help of the denoising diffusion model. Specifically, the face attribute disentanglement module is proposed to disentangle eye blinking and lip motion features, where the lip motion features are synchronized with audio features via the contrastive learning strategy, and the disentangled motion features are aligned well with the talking head. Furthermore, the denoising diffusion model takes the source image and the warped motion features as input to generate the high-resolution realistic talking head with diverse head poses. Extensive evaluations using multiple metrics demonstrate that our method outperforms the current techniques both qualitatively and quantitatively.
