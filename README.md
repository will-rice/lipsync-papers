# lipsync-papers

A curated, automatically-updated collection of papers on **lip sync**, talking-head synthesis, audio-driven face animation, and related topics — starting from [Wav2Lip](https://arxiv.org/abs/2008.10010) (2020) and growing every week.

Beyond a reading list, this repo is built to be **browsed by LLMs**. Every paper is mirrored as a markdown file with structured YAML frontmatter and inline citation links that resolve to sibling files in the corpus when the cited work is here, or to arXiv / DOI otherwise. Point an agent at [`papers/README.md`](papers/README.md) and it can crawl the literature graph the same way you would.

## How it works

- Papers are sourced from [arXiv](https://arxiv.org/) and [Hugging Face Papers](https://huggingface.co/papers) via their public APIs. (Entries with `s2:` IDs are historical finds from Semantic Scholar, which was retired as a source after persistent API rate-limiting.)
- Query this corpus over MCP: `https://wrice-papers-mcp.hf.space/lipsync/mcp` ([server code](https://huggingface.co/spaces/wrice/papers-mcp)).
- A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs **daily at 06:00 UTC** to pull papers submitted in the previous 8 days.
- Results are filtered with a negative-keyword blacklist plus two admit paths: a positive lipsync/talking-face keyword gate (with an ML signal check), or semantic similarity of the abstract to the curated corpus (MiniLM embeddings, top-k mean against `papers.csv`).
- The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Markdown corpus

Each paper is also available as LLM-friendly markdown under `papers/<year>/<arxiv_id>.md`. The conversion pipeline:

- Converts arXiv's HTML rendering (`arxiv.org/html/<id>`, falling back to [ar5iv](https://ar5iv.labs.arxiv.org) for pre-2024 papers) — the article is extracted from the page, figures become absolute-URL images, and equations become GitHub-native ` ```math ` blocks.
- Papers without a usable HTML rendering fall back to LaTeX source (`arxiv.org/e-print/<id>`) via [pandoc](https://pandoc.org), then PDF via [marker](https://github.com/datalab-to/marker).
- Auto-flagged or manually-listed (`papers/.fixme.txt`) low-quality outputs go through a Claude Sonnet 4.6 remediation pass.
- Citations are rewritten as clickable links — local sibling MD when the cited paper is in this corpus, external arXiv/DOI URLs otherwise.

Browse the corpus at [papers/README.md](papers/README.md). Each paper file has YAML frontmatter with metadata + diagnostics (`source`, `converter`, `llm_remediated`, `citations_resolved`).

## Running locally

You'll need pandoc and Node (for Prettier, which normalizes the generated markdown):

```bash
# macOS
brew install pandoc node

# Ubuntu
sudo apt-get install pandoc nodejs npm
```

Then run `npm ci` to install the pinned Prettier used by the pipeline, CI, and pre-commit.

```bash
# Incremental fetch (last 8 days)
uv run python scripts/fetch_papers.py

# Full historical fetch (everything since 2020-01-01)
uv run python scripts/fetch_papers.py --full
uv run python scripts/convert_papers.py --regenerate-all

# Custom window
uv run python scripts/fetch_papers.py --days 30
```

The fetch script uses only the Python standard library (plus a Prettier pass on the README); the conversion pipeline adds `marker-pdf`, `anthropic`, `pyyaml`, and the `pandoc` system binary (managed via `uv` and your package manager). Both scripts format the markdown they generate with the repo-pinned [Prettier](https://prettier.io/) (`npm ci`), and a [Format workflow](.github/workflows/format.yml) enforces it on every PR.

## Triggering a manual update

Open the **Actions** tab → **Fetch Lipsync Papers** → **Run workflow**.
Select _full = true_ to back-fill from 2020 and rebuild all paper markdown, or leave it as _false_ for an incremental update.

## Papers

<!-- PAPERS_TABLE_START -->

_Showing the last 60 days (18 of 541 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>Last 60 Days</h3></summary>

#### [PolyInterview: An LLM-based Platform for Immersive Mock Interview Practice with Comprehensive Multimodal Assessment](https://arxiv.org/abs/2607.10310) · [📄 Read](papers/2026/2607.10310.md)

**Zhiyuan Wen, Jiannong Cao, Zijian Wang, Chen Chen et al.** · 2026-07-11

<details>
<summary>Abstract</summary>

Preparing for job interviews is important for securing desired positions, yet realistic practice remains difficult to access: real interviews are infrequent, expert mock coaching is costly, and self-practice offers neither adaptive dialogue nor structured assessment. Existing systems typically address only parts of this need through fixed question sequences, limited communication channels, or feedback with little supporting evidence. We present PolyInterview, an LLM-based platform for immersive mock interview practice with comprehensive multimodal assessment. PolyInterview uses the target job description and CV to generate questions tailored to the role and candidate, conducts multi-turn spoken interviews with a lip-synced digital human interviewer that asks answer-aware follow-up questions, and evaluates response content, vocal delivery, and non-verbal behavior. Four parallel evaluators produce 13 behavior-level features that are aggregated into 10 assessment aspects and two competency tracks. Guided by the KSA and STAR frameworks, the report links each score to behavioral evidence and actionable recommendations. PolyInterview is publicly accessible. Its current all-account snapshot contains 101 accounts, 1,564 interview sessions, 7,665 generated questions, and 1,422 five-stage question sets. Generated questions are more closely aligned with their matched job description than with cross-role job descriptions in 93.7% of sessions. An evaluation by ten experts found strong question plans and actionable feedback.

</details>

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

#### [Resonant Minds: Closed-Loop Social Avatars with Theory of Mind](https://arxiv.org/abs/2606.05896) · [📄 Read](papers/2026/2606.05896.md)

**Jianxu Shangguan, Jing Xu, Hang Ye, Xiaoxuan Ma et al.** · 2026-06-04

<details>
<summary>Abstract</summary>

Creating lifelike digital humans with genuine social intelligence requires unifying cognitive reasoning and multimodal generation within a coherent framework. Current approaches treat these as separate tasks: Large Language Models excel at dialogue but lack embodied expression, while diffusion-based talking head models achieve visual fidelity but ignore social cognition. To bridge this gap, we propose a closed-loop dual-agent framework integrating perception, social reasoning, and expression into a continuous interaction cycle. The perception module analyzes partners' multimodal behaviors from video, while the social reasoning module infers hidden mental states through Theory of Mind and selects responses via an ensemble mechanism. The expression module then generates emotion-controllable dual-agent videos synthesizing both speaker speech and expression alongside listener reactive behaviors, capturing bidirectional dynamics absent in prior work. We construct a hierarchical Persona-Scenario dataset with psychologically grounded personas and private social goals to support evaluation under information asymmetry. Experiments on this dataset demonstrate competitive or superior performance on both dialogue quality and video generation metrics. Notably, our method surpasses even the full-information Script mode on key dialogue quality dimensions, suggesting that explicit mental state inference under uncertainty can elicit more thoughtful dialogue than unrestricted information access.

</details>

#### [Temporally-Aligned Evaluation for Audio-Driven Talking Head Generation](https://arxiv.org/abs/2606.01031) · [📄 Read](papers/2026/2606.01031.md)

**Zhicheng Zhang, Lei Wang, Yu Zhang, Yongsheng Gao** · 2026-05-31

<details>
<summary>Abstract</summary>

Audio-driven talking-head generation has advanced rapidly, yet existing evaluation protocols mainly rely on frame-wise metrics that assume strict temporal correspondence between generated and reference videos. This assumption does not match speech-driven facial motion, which naturally includes slight timing shifts, different speaking speeds, and stylistic variations. As a result, conventional metrics may treat harmless timing differences as quality errors, making it harder to fairly compare methods and understand their trade-offs. In this work, we argue that evaluation of dynamic generative models should be formulated as a sequence-alignment problem rather than independent frame comparison. We introduce a unified sequence-level reformulation that integrates Soft Dynamic Time Warping into established evaluation pipelines. By aligning feature trajectories while preserving temporal order, the proposed framework provides robustness to bounded temporal misalignments without altering the underlying perceptual, identity, or synchronization encoders. We show that frame-wise evaluation can be viewed as a special case under rigid alignment, while sequence-level alignment provides improved stability, lower sensitivity to timing differences, and clearer separation between modeling paradigms. Building on this principled formulation, we conduct a large-scale benchmark of 20 methods across seven datasets spanning canonical, in-the-wild, and style-diverse scenarios under standardized protocols. Extensive experiments show that temporally aligned metrics are more robust to timing differences, provide more consistent results across datasets, and better reveal systematic trade-offs between modeling paradigms, such as synchronization versus realism and expressiveness versus stability.

</details>

#### [IP-Adapter Is All You Need: Towards Fine-Tuning-Free Diffusion-Based Talking Face Generation](https://arxiv.org/abs/2605.30230) · [📄 Read](papers/2026/2605.30230.md)

**Hao Wu, Xiangyang Luo, Hao Wang, Jiawei Zhang et al.** · 2026-05-28

<details>
<summary>Abstract</summary>

With the rapid advancement of diffusion models, talking face generation has made remarkable progress. However, existing diffusion-based methods still require task-specific fine-tuning and large-scale audiovisual datasets, resulting in high computational costs that hinder scalability and accessibility of diffusion-based approaches across the research community. To address this, we propose a finetuning-free paradigm that directly performs talking face generation using the pretrained weights of Stable Diffusion and IP-Adapter. This backbone leverages the visual embedding capability of IP-Adapter to mine lip-related semantics from the pretrained Stable Diffusion. To address the challenges of identity drift, synchronization errors, and temporal instability, we also design three trainable-parameterfree components: (1) the Structurist, which explicitly disentangles and reassembles lip and appearance features to mitigate identity drift and appearance distortion; (2) the Structure Controller, which adaptively refines embeddings based on quasi-monotonic motion trends for precise lip synchronization; and (3) the Noise Sensor, which introduces Gaussian prior to detect and suppress flicker and jitter artifacts and enhance temporal consistency. Experimental results show that our method outperforms existing SOTA approaches in both lip-sync accuracy (at least 0.16 gain in PCLD) and visual fidelity (at least 0.7 improvement in FID), establishing a novel fine-tuning-free diffusion framework for talking face generation.

</details>

#### [Explainable Children Autism Detection using Gaze Features in Audio-Visual Speech Comprehension ETRA012](https://www.semanticscholar.org/paper/b608a5b26365240ad5a5ce13e553fd8577a83ef0) · [📄 Read](papers/2026/s2:b608a5b26365240ad5a5ce13e553fd8577a83ef0.md)

**Miguel Zaragozá-Portolés, David Gimeno-Gómez, V. Ávila, Dr. Inmaculada Fajardo et al.** · 2026-05-28

<details>
<summary>Abstract</summary>

Autism Spectrum Disorder (ASD) is a neurodevelopmental condition marked by impairments in social interaction and delayed language acquisition. Early and accurate identification is crucial for timely interventions that support cognitive and social development. Motivated by the subjectivity of traditional behavior-based assessments, computational methodologies offer more objective and cost-effective alternatives. Among these, eye-tracking stands out for capturing subtle attentional and perceptual patterns. This paper investigates the use of eye-tracking data for automatic ASD detection in children during audio-visual storytelling interactions, emphasizing traditional yet explainable machine learning methods. Although performance remains modest, our analyses reveal that fixation duration and revisit patterns to facial regions may serve as potential biomarkers. Further analyses highlight the impact of stimulus modality, suggesting that the inclusion of visual speech cues provides valuable discriminative information. These findings have the potential to support and guide the work of psychologists in the assessment of ASD within speech comprehension contexts.

</details>

#### [CogPortrait: Fine-Grained Eye-Region Control in Portrait Animation via Hierarchical Agent Planning](https://arxiv.org/abs/2605.28056) · [📄 Read](papers/2026/2605.28056.md)

**He Feng, Yongjia Ma, Donglin Di, Lei Fan et al.** · 2026-05-27

<details>
<summary>Abstract</summary>

Portrait animation methods have achieved substantial visual quality and lip synchronization, but fine-grained manipulation of the eye region still faces a trade-off between input granularity and motion accuracy. Existing methods using emotion labels or coarse text prompts are insufficient for describing subtle ocular dynamics, whereas approaches based on Action Units or driving videos provide higher fidelity at the cost of a heavier input burden. These limitations are still restrictive for beyond-emotion states (e.g., thinking) and drowsiness. In light of the above, we propose CogPortrait, a two-stage framework that generates portrait animations from high-level labels. In the first stage, three chain-of-thought Multimodal Large Language Models (MLLMs) agents compile high-level labels into facial keypoints through temporal event planning, prototype retrieval, and composition from a real-behavior library, and semantic-physiological constraint enforcement. In the second stage, a DiT-based video generation backbone synthesizes the final animation conditioned on the keypoints, reference portrait, audio, and text prompt, enhanced by a dynamic classifier-free guidance strategy with eye-region-aware reweighting and KTO-based refinement for boundary cases. We further introduce the EMH benchmark covering diverse emotions and beyond-emotion categories with two AU-level metrics for evaluating fine-grained eye-region and head-motion control. Extensive experiments on HDTF and the EMH benchmark demonstrate that CogPortrait achieves more precise eye-region control than existing methods while maintaining supe- rior visual quality and identity consistency

</details>

#### [From Talking to Singing: A New Challenge for Audio-Visual Deepfake Detection](https://arxiv.org/abs/2605.27944) · [📄 Read](papers/2026/2605.27944.md)

**Keqi Liu, Jiwei Wei, Wenyuan Zhang, Shuchang Zhou et al.** · 2026-05-27

<details>
<summary>Abstract</summary>

With rapid advances in audio-visual generative models, reliable forgery detection becomes increasingly critical. Existing methods for audio-visual deepfake detection typically rely on cross-modal inconsistencies. In singing, rhythmic vocalization weakens this coupling and introduces a nontrivial domain shift, substantially degrading detection performance. We construct the Singing Head DeepFake (SHDF) dataset using rhythm-aware generative models to fill the gap in singing benchmarks. To cope with cross-scenario domain shifts, we propose a Text-guided Audio-Visual Forgery Detection (T-AVFD) framework that generalizes across both talking and singing scenarios. T-AVFD comprises a facial authenticity pattern learner and a multi-modal differential weight learning module. The pattern learner aligns facial features with multi-granularity textual descriptions to learn generalizable authenticity patterns. The weight learning module preserves intrinsic audio-visual consistency and adaptively integrates it with authenticity patterns via differential weighting. Extensive experiments on multiple talking head deepfake datasets and SHDF show consistent improvements over existing baselines and strong robustness under diverse perturbations.

</details>

#### [Test-Time Self-Adaptive Conditioning for Stable Audio-Driven Talking-Head Generation](https://arxiv.org/abs/2605.25488) · [📄 Read](papers/2026/2605.25488.md)

**Zhicheng Zhang, Lei Wang, Yu Zhang, Yongsheng Gao** · 2026-05-25

<details>
<summary>Abstract</summary>

Audio-driven talking-head generation has achieved remarkable progress with recent models such as AniTalker, FLOAT, and Sonic. Despite their success, most existing approaches rely on a single static reference image to condition the entire video generation process at inference stage. This static conditioning paradigm often creates a mismatch between fixed identity features and dynamically evolving facial motion, leading to identity drift, temporal inconsistency, and degraded perceptual quality. We introduce Test-Time Self-Adaptive Conditioning (TT-SAC), a parameter-free inference framework that enables pretrained talking-head generators to adapt their conditioning representations during inference without retraining, gradient updates, or additional supervision. Instead of treating the reference portrait as immutable, TT-SAC composes the generator with its encoder in a feedback loop: the generator's own outputs are re-encoded to construct a refined conditioning representation that better aligns with the temporal dynamics of the synthesized sequence. A single adaptation step approximates a self-consistent equilibrium of the generative process, stabilizing identity and motion across time. We further provide theoretical analysis showing that test-time conditioning adaptation reduces feature variance and improves generative stability under mild Lipschitz assumptions, while exhibiting a principled bias-variance tradeoff that governs the optimal strength of adaptation. Extensive experiments on state-of-the-art talking-head generators and benchmark datasets demonstrate consistent improvements in lip-sync accuracy, temporal coherence, identity preservation, and perceptual fidelity. TT-SAC offers a model-agnostic and training-free strategy for enhancing generative video models, establishing test-time conditioning adaptation as an effective mechanism for stabilizing audio-driven portrait animation.

</details>

</details>
<!-- PAPERS_TABLE_END -->
