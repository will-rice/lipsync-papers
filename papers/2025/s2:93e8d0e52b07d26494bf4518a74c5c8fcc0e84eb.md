---
arxiv_id: s2:93e8d0e52b07d26494bf4518a74c5c8fcc0e84eb
title:
  "DFNeRF: Disentangled Facial Neural Radiance Fields for Text-based Editing
  of Free-view Talking Head"
authors:
  - Benwang Chen
  - Xiaoyu Li
  - Xuan Wang
  - Qi Zhang
  - Haoqian Wang
submitted: "2025-04-06"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/93e8d0e52b07d26494bf4518a74c5c8fcc0e84eb
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-21T00:15:52+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

In this paper, we propose a text-based approach that can edit the speech content of a free-view talking head based on its transcript. The core of our method is to establish the relationship between phonemes and head attributes. To avoid discontinuities in head pose and facial expressions caused by editing mouth shape. We design the disentangled facial neural radiance fields (DFNeRF) to automatically disentangle these attributes controlled by the learned latent codes. Using the free-view talking head synthesized by DFNeRF as the base corpus, we could re-assemble the latent codes based on the new content using the phoneme search method to produce a seamless edited result. Our phoneme search method with a discriminator could find the best-matched phonemes in the sequence and ensure a smooth transition of mouth shape between the adjacent phonemes. Extensive experiments demonstrate the effectiveness of our method both qualitatively and quantitatively.
