# lipsync-papers

A curated, automatically-updated collection of papers on **lip sync**, talking-head synthesis, audio-driven face animation, and related topics — starting from [Wav2Lip](https://arxiv.org/abs/2008.10010) (2020) and growing every week.

Beyond a reading list, this repo is built to be **browsed by LLMs**. Every paper is mirrored as a markdown file with structured YAML frontmatter and inline citation links that resolve to sibling files in the corpus when the cited work is here, or to arXiv / DOI otherwise. Point an agent at [`papers/README.md`](papers/README.md) and it can crawl the literature graph the same way you would.

## How it works

* Papers are sourced from [arXiv](https://arxiv.org/) and [Semantic Scholar](https://www.semanticscholar.org/) via their public APIs.
* A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs **daily at 06:00 UTC** to pull papers submitted in the previous 8 days.
* Results are filtered with a negative-keyword blacklist plus an ML signal check and a positive lipsync/talking-face relevance gate.
* The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Markdown corpus

Each paper is also available as LLM-friendly markdown under `papers/<year>/<arxiv_id>.md`. The conversion pipeline:

* Converts arXiv's HTML rendering (`arxiv.org/html/<id>`, falling back to [ar5iv](https://ar5iv.labs.arxiv.org) for pre-2024 papers) — the article is extracted from the page, figures become absolute-URL images, and equations become GitHub-native ` ```math ` blocks.
* Papers without a usable HTML rendering fall back to LaTeX source (`arxiv.org/e-print/<id>`) via [pandoc](https://pandoc.org), then PDF via [marker](https://github.com/datalab-to/marker).
* Auto-flagged or manually-listed (`papers/.fixme.txt`) low-quality outputs go through a Claude Sonnet 4.6 remediation pass.
* Citations are rewritten as clickable links — local sibling MD when the cited paper is in this corpus, external arXiv/DOI URLs otherwise.

Browse the corpus at [papers/README.md](papers/README.md). Each paper file has YAML frontmatter with metadata + diagnostics (`source`, `converter`, `llm_remediated`, `citations_resolved`).

## Running locally

You'll need pandoc:

```bash
# macOS
brew install pandoc

# Ubuntu
sudo apt-get install pandoc
```

```bash
# Incremental fetch (last 8 days)
uv run python scripts/fetch_papers.py

# Full historical fetch (everything since 2020-01-01)
uv run python scripts/fetch_papers.py --full
uv run python scripts/convert_papers.py --regenerate-all

# Custom window
uv run python scripts/fetch_papers.py --days 30
```

The fetch script uses only the Python standard library; the conversion pipeline adds `marker-pdf`, `anthropic`, `pyyaml`, and the `pandoc` system binary (managed via `uv` and your package manager).

## Triggering a manual update

Open the **Actions** tab → **Fetch Lipsync Papers** → **Run workflow**.
Select *full = true* to back-fill from 2020 and rebuild all paper markdown, or leave it as *false* for an incremental update.

## Papers

<!-- PAPERS_TABLE_START -->
_Showing the last 30 days (10 of 540 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [Multi-Modal Deepfake Detection via Spatial, Temporal, and Audio-Visual Fusion with Vision Transformers](https://www.semanticscholar.org/paper/5ad7261ad284f64c1b7776c990a9bbb305c402b5) · [📄 Read](papers/2026/s2:5ad7261ad284f64c1b7776c990a9bbb305c402b5.md)
**Merlin Gethsy D., S. V** · 2026-06-30

<details>
<summary>Abstract</summary>

The rapid advancement of the deepfake generation technologies has intensified concerns related to digital misinformation, identity impersonation, and media manipulation. Although numerous deepfake detection methods have been developed by mitigate these threats, most rely on a single modality and exhibit limited robustness when confronted with diverse manipulation techniques and cross-dataset scenarios. To overcome these deficiencies, we propose VeriSphere, a multimodal deepfake detection framework that combines spatial, temporal, and audiovisual forensics in one system. It uses a Vision Transformer for detecting spatial artifacts, an X-CLIP-based module for capturing temporality, and an AV synchronization module to examine whether speech aligns with lip movements. The outputs are then fused using a weighted strategy to produce a single trust score for prediction. Results show that VeriSphere achieves a high accuracy of 92.1%, an AUC of 0.963, and an F1-score of 0.924 across three benchmark datasets: FaceForensics++, Celeb-DF, and DFDC.

</details>

#### [SyncCache: Exploiting Asymmetric Dynamics for Fast Audio-Driven Portrait Animation](https://arxiv.org/abs/2606.30849) · [📄 Read](papers/2026/2606.30849.md)
**Juncheng Ma, Yuxuan Du, Yanan Sun, Zhening Xing et al.** · 2026-06-29

<details>
<summary>Abstract</summary>

Diffusion Transformers (DiTs) have significantly advanced audio-driven portrait animation, but their high computational cost leads to substantial inference latency. Although training-free diffusion caching accelerates inference significant, existing methods are primarily developed for text-conditioned generation and overlook the spatial and modality imbalances inherent in audio-driven portrait animation. In this paper, we propose SyncCache, a training-free caching acceleration method tailored for DiT-based portrait animation that explicitly exploits asymmetric dynamics. Specifically, high-frequency dynamics driven by audio conditions and concentrated in human regions are more challenging and critical to cache and reuse than the low-frequency visual background in portrait animation. First, we introduce Spatially-Asymmetric Probing to prioritize error sensitivity in dynamic human region. Second, through Modality-Decoupled Caching, we bypass heavy DiT block by reusing stable inter-block residuals, while continuously recomputing lightweight audio blocks to preserve precise lip synchronization. Furthermore, we introduce a cache ratio to control cache capacity and formulate memory-adaptive cache selection as an offline dynamic programming problem without online overhead. Extensive experiments demonstrate that SyncCache achieves superior speed-quality trade-offs, delivering up to 4.12x acceleration on HunyuanVideo-Avatar and 3.75x on Wan-S2V with near-lossless visual fidelity and precise audio alignment.

</details>

#### [DIVA-3D: a diverse 3D talking head dataset from in-the-wild videos](https://www.semanticscholar.org/paper/636d2024d246b43d37b6bb3d887c5607ad8ba1d1) · [📄 Read](papers/2026/s2:636d2024d246b43d37b6bb3d887c5607ad8ba1d1.md)
**Yuhang Wu, Yixuan Zhang, Qing Chang, Junran Peng et al.** · 2026-06-29

<details>
<summary>Abstract</summary>

The synthesis of lifelike three-dimensional (3D) talking heads from audio requires precise lip synchronization and nuanced facial expressions. However, current methods often fall short of this goal, largely due to the scarcity of large-scale, diverse training data. To address this issue, this paper first presents a novel, semi-automated pipeline to efficiently harvest audio and corresponding 3D facial FLAME data from public videos. We then use this pipeline to construct DIVA-3D, a large-scale, diverse, in-the-wild audio-visual dataset, which contains 73 hours of both Chinese and English data. This is, to our best knowledge, the most topically diverse 3D talking head dataset available, with six distinct domains. Based on DIVA-3D, we propose a robust generative framework that produces highly accurate lip synchronization and natural facial expressions. Finally, we conduct a comprehensive benchmark of state-of-the-art methods using our new dataset. Extensive results validate the effectiveness of our dataset and demonstrate the superior performance of our framework, underscoring its significant practical value of our framework for real-world applications.

</details>

#### [KM-Speaker: Keypoint-Based Style Control for High-Quality Speech-Driven 3D Facial Animation and Dialogue Localization](https://arxiv.org/abs/2606.28568) · [📄 Read](papers/2026/2606.28568.md)
**Arthur Josi, Emeline Got, Abdallah Dib, Luiz Gustavo Hafemann et al.** · 2026-06-26

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation methods face significant challenges in simultaneously achieving high-fidelity motion and precise artistic control at production quality. Existing controllable models typically learn global style control by relying on large-scale, low-quality \emph{in-the-wild} datasets that compromise overall animation realism. Furthermore, these frameworks often lack the fine-grained temporal precision required for demanding tasks such as dialogue localization (e.g., dubbing), where matching specific facial expressions is as critical as lip synchronization. We present KM-Speaker (Keypoint-Matching Speaker), a novel keypoint-conditioned flow-based generative framework that provides both global style guidance and frame-level temporal control from reference performances. We propose a disentanglement strategy that separates audio-driven lip motion from keypoint-driven upper-face dynamics, together with a global style context preservation mechanism to ensure coherent full-face expressiveness. KM-Speaker advances example-based 3D facial animation by achieving high-fidelity motion and flexible controllability in a data-constrained setting, consistently outperforming state-of-the-art methods in lip-sync accuracy, style adherence, and expressive temporal control.

</details>

#### [Audio-visual Contrastive Alignment for Diffusion-based Visual-conditioned Speech Enhancement](https://arxiv.org/abs/2606.23712) · [📄 Read](papers/2026/2606.23712.md)
**Colombe Mboungou, Mostafa Sadeghi, Jean-Eudes Ayilo, Romain Serizel** · 2026-06-16

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement (AVSE) exploits visual cues such as lip movements to recover speech in noisy environments. Recent work introduced diffusion-based unsupervised AVSE, where a speech diffusion model conditioned on visual features via cross-attention is trained and used as a data-driven prior for posterior sampling-based speech enhancement. Despite promising performance over its audio-only counterpart, the impact of explicitly enforcing cross-modal alignment in the fusion remains unclear. In this work, we propose to augment the diffusion training objective with a contrastive audio-visual loss to encourage stronger use of visual information while keeping the posterior sampling framework unchanged. Experiments across matched and mismatched test data show consistent improvements in interference suppression, signal reconstruction, and perceptual quality, with the largest gains at low SNRs. Code is available at https://github.com/ cexauce/AV-CA-DiffUSE

</details>

#### [EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units](https://arxiv.org/abs/2606.15848) · [📄 Read](papers/2026/2606.15848.md)
**Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang et al.** · 2026-06-14

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has shown strong potential for high-fidelity talking head synthesis. However, enabling fine-grained, interpretable, and editable facial expression control remains fundamentally challenging due to intrinsic conflicts between speech-driven facial dynamics and explicit expression signals. Existing methods rely on implicit multimodal fusion, leading to spatial entanglement and temporal instability. We present EmoZone-Talker, a novel framework that reformulates audio-driven facial animation as a structured spatial-temporal coordination problem under cross-modal conflicts. Our approach introduces an explicit spatial disentanglement and temporal dynamics modeling of facial motion. Specifically, we propose Synergy Zones with Prioritized Attention Bias (SZ-PAB) to explicitly decouple modality contributions via region-wise constraints guided by anatomical priors, and a Channel-Independent Temporal AU Encoder (CIT-AE) to model temporally coherent AU dynamics. By integrating these representations into 3D Gaussian deformation, EmoZone-Talker enables precise and interpretable control over facial expressions. Extensive experiments demonstrate that our method improves expression controllability and realism, with notable gains in upper-face accuracy and temporal coherence, while preserving high rendering quality and accurate lip synchronization. Code will be publicly released to facilitate reproducibility and further research.

</details>

#### [ReFree: Towards Realistic Co-Speech Video Generation via Reward-Free RL and Multilevel Speech Guidance](https://arxiv.org/abs/2606.13304) · [📄 Read](papers/2026/2606.13304.md)
**Salaheldin Mohamed, M. Hamza Mughal, Rishabh Dabral, Christian Theobalt** · 2026-06-11

<details>
<summary>Abstract</summary>

Speech-driven talking character animation seeks to generate life-like portrait videos that convey natural conversation behavior, aligning facial motion with spoken audio. Although recent advances in video generation have substantially improved realism in video-based animation, achieving both accurate lip articulation and expressive behavior remains challenging. Existing approaches typically trade off precise phoneme-to-lip synchronization against dynamic facial expressions and head motion, yielding animations that are either accurate yet rigid, or expressive but poorly synchronized. We address this challenge by proposing ReFree-S2V, a flow-matching speech-to-portrait animation framework that builds upon a pretrained video generation model to achieve fine-grained speech articulation and high-level expressive cues in speech-driven portrait animation. This model introduces a multi-level speech representation capturing phonetic and prosodic information at both local and global granularities. These representations are selectively injected into transformer blocks via learnable level selectors, enabling both accurate lip synchronization and natural expressive motion. To achieve natural head movements, we further introduce a novel reward-free reinforcement learning scheme into flow-matching training to discourage perceptually implausible motion without relying on handcrafted synchronization metrics or reward models, or the high cost of human preference annotation. Extensive experiments demonstrate that ReFree-S2V achieves state-of-the-art performance, significantly outperforming existing methods in both quantitative lip-sync accuracy and qualitative human evaluations of naturalness and expressivity.

</details>

#### [From Tokens to Faces: Investigating Discrete Speech Representations for 3D Facial Animation](https://arxiv.org/abs/2606.13630) · [📄 Read](papers/2026/2606.13630.md)
**Pedro Corrêa, Olivier Perrotin, Samir Sadok, P. Costa et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

The choice of speech representation is critical in speech-driven 3D facial animation. Representations differ in what they encode: SSL features emphasize segmental and semantic cues, neural codecs yield latents optimized for acoustic reconstruction, and ASR-style objectives produce label-based spaces. We evaluate four speech representation families for 3D facial synthesis, comparing their facial reconstruction quality across two facial decoders using objective metrics and a perceptual evaluation. We additionally conduct probing analyses that relate tokenized representations to phonetic units and to articulatory deformations. We found that encoding phonetic classes is beneficial for accurate facial animation prediction on both semantic and label-based representations with comparable facial animation quality. From the latter, we introduce an Audio Visual Text-to-Speech (AVTTS) pipeline that leverages, as a shared space, discrete representations to decode speech and 3D facial motion.

</details>

#### [EmoPoseFace: Head Pose Aware Speech- driven 3D Emotional Facial Animation Using Latent Diffusion.](https://www.semanticscholar.org/paper/7e1a054065faab0115b3ce00098b395a13617397) · [📄 Read](papers/2026/s2:7e1a054065faab0115b3ce00098b395a13617397.md)
**Xin Zhao, Ju Dai, Feng Zhou, Haofei Wang et al.** · 2026-06-10


#### [Lip Forcing: Few-Step Autoregressive Diffusion for Real-time Lip Synchronization](https://arxiv.org/abs/2606.11180) · [📄 Read](papers/2026/2606.11180.md)
**Paul Hyunbin Cho, Jinhyuk Jang, SeokYoung Lee, Joungbin Lee et al.** · 2026-06-09

<details>
<summary>Abstract</summary>

Diffusion-based lip synchronization models achieve strong visual quality and audio-visual alignment, but full-sequence bidirectional attention and many denoising steps make them impractical for real-time inference. We present Lip Forcing, to our knowledge the first autoregressive diffusion method for video-to-video (V2V) lip synchronization, which distills a 14B audio-conditioned bidirectional video diffusion teacher into causal students. At inference, the students generate each chunk in only two denoising steps without inference-time CFG, enabling real-time lip synchronization. A lip-sync-specific teacher-trajectory analysis reveals a CFG fidelity-sync tradeoff: no-CFG predictions favor reference fidelity, whereas CFG-guided predictions favor synchronization within a mid-trajectory band. Lip Forcing translates this finding into three analysis-derived components: Sync-Window DMD, a two-step inference schedule, and a SyncNet-based reward. We validate Lip Forcing at two student scales, both distilled from the 14B teacher. The 1.3B student crosses into real-time streaming at 31 FPS, $17.6\times$ faster than its same-scale bidirectional model. The 14B student, the largest diffusion model reported for V2V lip synchronization, runs $39.8\times$ faster than its teacher at comparable reference fidelity. Time-to-first-frame is sub-millisecond at both scales, far below every diffusion baseline.

</details>

</details>
<!-- PAPERS_TABLE_END -->
