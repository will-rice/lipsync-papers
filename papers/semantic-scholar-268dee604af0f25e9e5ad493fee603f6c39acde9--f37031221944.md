---
arxiv_id: s2:268dee604af0f25e9e5ad493fee603f6c39acde9
title:
  Lip-Sync Analyzer for Deepfake Detection and Peeking Behind the Black Box with
  Explainable AI
authors:
  - S. Sakib
  - S. Haque
  - Atanu Shome
submitted: "2025-10-23"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/268dee604af0f25e9e5ad493fee603f6c39acde9
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-21T00:12:39+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

The swift evolution of deepfake technology presents significant threats to the credibility and trustworthiness of digital media. This work presents a deepfake detection framework that combines spatial and audio-visual features, with a specific focus on lip-sync forgeries. We evaluate multiple state-of-the-art CNN architectures—DenseNet-121, EfficientNet-B0, InceptionV3, ResNet-50, and XceptionNet—alongside a Vision Transformer (ViT-B/32). Experiments on the AVLips dataset (3,396 real and 4,206 fake videos) show that ViT-B/32 achieves superior performance, with 96% F1-score, and 99% AUC. Audio-visual fusion consistently outperforms visual-only models, highlighting the strength of multimodal analysis. To enhance transparency, LIME-based explainable AI visualizations are employed to interpret model predictions. Unlike previous works that primarily rely on unimodal cues, our approach uniquely integrates audio waveforms with visual frames to expose subtle inconsistencies in lip synchronization. Given the potential misuse of deepfakes in misinformation, fraud, and political manipulation, this study emphasizes the urgent need for robust and interpretable detection methods. Our findings confirm the effectiveness of transformer-based models with XAI for dependable deepfake detection, with future work focusing on temporal modeling and scalability.
