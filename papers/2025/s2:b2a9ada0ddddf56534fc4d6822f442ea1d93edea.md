---
arxiv_id: s2:b2a9ada0ddddf56534fc4d6822f442ea1d93edea
title: Accelerating LatentSync Lip-Synchronization via OmniQuant-Inspired Post-Training
  Quantization
authors:
- Guolin Wang
submitted: '2025-12-26'
categories: []
arxiv_url: https://www.semanticscholar.org/paper/b2a9ada0ddddf56534fc4d6822f442ea1d93edea
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: '2026-07-07T14:16:24+00:00'
references_parsed: 0
arxiv_version: ''
---

## Abstract

Lip-synchronization models play an important role in audio-driven facial animation and virtual human applications. LatentSync is a representative latent-based lip synchronization model that achieves high-quality temporal alignment between audio and visual modalities. However, the inference process of LatentSync relies on deep neural network components with considerable computational cost, which limits its deployment in real-time and resource-constrained scenarios. In this paper, we investigate an OmniQuant-inspired posttraining quantization (PTQ) strategy to accelerate the inference of the LatentSync lip-synchronization model. By applying INT8 weight-only quantization to the core generative backbone, the proposed method significantly reduces model size and inference latency without requiring retraining. The proposed approach follows the calibration principles of OmniQuant, including adaptive weight clipping and equivalent transformation, to mitigate quantization-induced performance degradation. Experimental results show that the proposed approach achieves noticeable inference acceleration and model compression, with no obvious functional degradation observed during empirical evaluation. These results demonstrate that OmniQuant-inspired post-training quantization provides a practical and efficient solution for accelerating lip-synchronization models in real-world applications.
