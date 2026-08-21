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

_Showing the last 30 papers (30 of 1132 total). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>Last 30 Papers</h3></summary>

#### [EfficientSync: Real-Time Lip Synchronization via Deformation-Based Reference Texture Mixing](https://arxiv.org/abs/2608.18832) · [📄 Read](papers/2026/2608.18832.md)

**Fa-Ting Hong, Runzhen Liu, Luchuan Song, Hongmin Cai et al.** · 2026-08-19

<details>
<summary>Abstract</summary>

Audio-driven lip synchronization manipulates the mouth region of a talking-face video to match the driving audio while preserving head pose, identity, and background. Although the task is inherently local editing, prevailing approaches reconstruct the entire lower face with heavy GAN- or diffusion-based decoders, incurring substantial latency and, more critically, hallucinating intra-oral details such as teeth and lip wrinkles instead of preserving authentic textures. We contend that the bottleneck in identity preservation is not the scarcity of reference frames, but the lack of a mechanism that faithfully transfers the genuine textures they already contain. We therefore present EfficientSync, a real-time deformation-based framework that retains reference textures rather than resynthesizing them. First, the Dynamic Texture Mixer reformulates multi-reference fusion as channel-wise selection, evaluating each spatially aligned reference in a global context and aggregating them by channel-wise weighted summation, preserving textural integrity at low cost. Second, Spatio-Temporal Shifted Adaptive Masking decomposes the source frame into lip-generation conditions and an independent background prior, suppressing lower-face leakage while blending the synthesized mouth seamlessly into the background. Third, STAR Sampling, a zero-overhead pre-processing step, retrieves the sharpest and most topologically diverse reference frames. Experiments on HDTF and VFHQ show state-of-the-art visual quality and identity preservation at 166 FPS on a single GPU. Video demos: https://alunaticat.github.io/EfficientSync/index.html.

</details>

#### [DynaForcing: Overcoming Dynamic Collapse in Self-Forcing Distillation for Streaming Avatar Generation](https://arxiv.org/abs/2608.17707) · [📄 Read](papers/2026/2608.17707.md)

**Yubo Huang, Sirui Zhao, Xinchen Yao, Zhengye Zhang et al.** · 2026-08-18

<details>
<summary>Abstract</summary>

Audio-driven avatar generation requires realistic lip-sync, expressive motion, and real-time streaming. Recent work achieves the latter via self-forcing with Distribution Matching Distillation (DMD), but this paradigm suffers from a critical failure that has not been systematically characterized: dynamic collapse, where the student model converges to a near-static optimum with high perceptual quality but severely suppressed temporal dynamics. We trace this to two causes: the reverse KL objective in DMD, which biases toward low-motion modes, and unanchored self-conditioning, which creates a feedback loop that amplifies collapse. This is especially harmful for avatars, where even subtle motion loss breaks lip-sync and expression. To address this, we propose DynaForcing, a training framework with three complementary strategies applied at different levels. Specifically, Hybrid Forcing anchors rollouts to ground-truth dynamics at the data level to break the feedback loop. Dynamics-Aware Reward Regularization introduces explicit motion rewards via the RL interpretation of DMD to counteract the reverse KL bias at the loss level. Reference Perturbation perturbs reference images to decouple identity from static details, forcing the model to rely on audio for motion at the conditioning level. We further introduce computation graph pruning and gradient replay, reducing the GPU footprint of self-forcing by over an order of magnitude. Experiments show that DynaForcing recovers dynamics to teacher-comparable levels (Dyn-Deg: 0.31 -> 0.73, Sync-C: 7.03 -> 7.68) while improving visual quality, resolving the quality-dynamics trade-off throughout training without early stopping.

</details>

#### [AnyTalk: Speech Animation for Arbitrary Characters Leveraging a Video Generation Model](https://arxiv.org/abs/2608.16143) · [📄 Read](papers/2026/2608.16143.md)

**Kwan Yun, Serin Yoon, Sunjin Jung, Jung Eun Yoo et al.** · 2026-08-17

<details>
<summary>Abstract</summary>

We present AnyTalk, a novel method for generating 3D speech animations for arbitrary characters without requiring any animation data. While existing audio-driven 3D speech animation methods rely on character-specific training data or laborious rigging/re-meshing, AnyTalk circumvents these limitations by leveraging recent video diffusion models trained on extensive video datasets. We first adapt a pre-trained video diffusion model to a target character through our Character-specific Fine-tuning (\textit{CsF}) technique. By fine-tuning on rendered images of the 3D character paired with zeroed-out audio embeddings (representing "no motion"), we eliminate the need for animation data while preserving the motion prior of large-scale video diffusion model. We then uplift the resulting talking-head video into a 3D speech animation by estimating blendshape parameters through a proposed optimization process. AnyTalk enables lip-synced animations across diverse face meshes and blendshape configurations, significantly reducing manual effort and data requirements. We further enhance usability by distilling AnyTalk into a streamlined network, $\text{AnyTalk}_{RT}$, thereby enabling real-time performance. By leveraging talking-head video generation, our method broadens access to audio-driven speech animation technology for arbitrary characters. The code is publicly available at https://serin-yoon.github.io/projects/anytalk/.

</details>

#### [SingDance: Compositional Zero-Shot Singing-and-Dancing Video Generation with Role-Aware Audio Conditioning](https://arxiv.org/abs/2608.16220) · [📄 Read](papers/2026/2608.16220.md)

**Tao Feng, Xu Li, Xiangyang Luo, Ming Wen et al.** · 2026-08-17

<details>
<summary>Abstract</summary>

Generating personalized dance videos from a reference image, text prompt, and audio track requires music-conditioned body motion. Singing-and-dancing adds a second requirement: the visible subject must also articulate the vocals. Existing music-conditioned methods focus primarily on choreography, while speech-driven models generally assume that the visible subject produces the input voice, leaving this combined setting largely underexplored. We introduce SingDance, a unified video diffusion framework that formulates controllable vocal articulation as a semantic role: the visible subject is either the source, who produces the vocal signal, or the listener, who receives it from an off-screen performer. Hard-compact routing selects task-relevant speech, music, and role conditions, which are composed through frame-wise joint audio injection; source and listener retain the same speech pathway. Training uses asymmetric supervision: on-screen speaking and curated off-screen conversational-response videos establish role control, while instrumental and song-based dancing-only videos establish music-conditioned body motion. The target Song/Source configuration is never observed during training. At inference, assigning the source role to a song composes separately learned articulation and song-conditioned dance capabilities, enabling compositional zero-shot singing-and-dancing. Experiments demonstrate strong motion--beat alignment and visual fidelity, reliable paired switching of vocal articulation while preserving music-aligned body motion, and highly competitive lip synchronization with substantially fewer generation-time parameters than the strongest speech-driven baseline evaluated.

</details>

#### [CineDub: Scaling End-to-End Video Dubbing to Multi-Speaker Dialogues with Coherent Sound Effects](https://arxiv.org/abs/2608.15734) · [📄 Read](papers/2026/2608.15734.md)

**Yusheng Dai, Kangdi Wang, Baolong Gao, Yuxuan Jiang et al.** · 2026-08-16

<details>
<summary>Abstract</summary>

Automatic video dubbing in the wild remains fundamentally limited by two competing constraints: hierarchical methods depend on brittle, multi-stage preprocessing pipelines that severely restrict data scalability and practical deployment, while holistic approaches operating on uncropped video suffer from weak temporal alignment and speaker-utterance ambiguity in multi-speaker settings. To overcome these limitations, we propose CineDub, a unified diffusion-based model that achieves precise multi-speaker dialogue dubbing directly from uncropped videos, without face cropping or speaker diarization. Central to our approach is the Implicitly-Coupled Holistic Conditioning (ICHC) paradigm, where holistic visual representations and a semantic-bundled transcription format are encoded independently, yet implicitly coupled through cross-modal training to resolve speaker ambiguity and enable precise multi-speaker multi-turn dialogue dubbing. Building on the unified temporal cues captured by holistic visual features, we further extend CineDub to joint speech and audio generation. We introduce an Ambient-to-Linguistic Curriculum Learning (ALC) to mitigate sub-task degradation, and a decoupled textual branch control mechanism to resolve cross-prompt interference during simultaneous generation. We also release two in-the-wild benchmarks, CineDub-Multi for multi-speaker dialogue dubbing and CineDub-SA for video-to-speech-and-audio (V2SA) generation, to enable evaluation under realistic conditions. Experiments show that CineDub achieves state-of-the-art results on established single-speaker dubbing and video-to-audio benchmarks while excelling in multi-speaker dialogue dubbing and acoustically coherent joint generation.

</details>

#### [CETalk: Continuous Valence-Arousal Control for Audio-Driven 3D Talking Head Generation](https://arxiv.org/abs/2608.15110) · [📄 Read](papers/2026/2608.15110.md)

**Peng Jia, Li Dai, Zhen Xiao, Xueliang Liu et al.** · 2026-08-15

<details>
<summary>Abstract</summary>

Emotional 3D talking head generation aims to synthesize expressive facial animations with accurate lip synchronization. However, existing methods often rely on discrete emotion categories, which fail to capture the continuous evolution of affect. They also overlook the temporal frequency mismatch between audio articulation and emotional expression. In this paper, we propose CETalk, an audio-driven 3D facial animation framework conditioned on continuous Valence--Arousal (VA) representations for fine-grained emotion control. CETalk predicts a sequence of FLAME parameters through three key components: a Dynamic Emotion Modulation Module that adaptively scales emotional intensity using audio-derived cues; a Multi-Scale Temporal Modeling mechanism that employs parallel branches to decouple high-frequency articulatory movements from low-frequency emotional dynamics; and a Dynamic Fusion Mechanism that integrates these multi-scale features via an adaptive gating network. To support training and evaluation, we construct 3D-VA-MEAD, a large-scale dataset with automatically estimated VA annotations and reconstructed 3D facial motions. Extensive experiments demonstrate that CETalk outperforms state-of-the-art methods in both lip-sync accuracy and emotional expressiveness, while enabling smooth and controllable emotion transitions.

</details>

#### [Separate First, Then Associate: A Two-Stage Approach for Real-World Audio-Visual Speech Enhancement](https://arxiv.org/abs/2608.14812) · [📄 Read](papers/2026/2608.14812.md)

**Tongtao Ling, Zhong-Qiu Wang** · 2026-08-14

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement (AVSE) aims at extracting target speech from multi-speaker mixtures by exploiting visual cues. Although recent studies have reported strong performance on simulated datasets, the performance, however, often drops dramatically when they are applied to real-world audio-visual recordings. To bridge this gap, the Real-World AVSE Challenge held in the ISCSLP 2026 conference calls for participants to design a practical solution for AVSE under real-world conditions, where speaker overlap, acoustic interferences, room reverberation and visual degradations naturally co-exist. In our submission to the challenge, we propose a decoupled separation-then-association approach. It consists of two stages: a separation stage in which a trained, audio-only model (i.e., not using visual cues) is used to separate input multi-speaker mixture to individual speaker signals, followed by an association stage, where an audio-visual CLIP model is used to identify the separated speech signal with the highest similarity with the target speaker's facial video via cross-modal similarity matching. Evaluation results on the challenge dataset show the effectiveness of our proposed approach.

</details>

#### [LiveAnimate: Stable Long-Form Streaming Human Animation in Real-Time](https://arxiv.org/abs/2608.11745) · [📄 Read](papers/2026/2608.11745.md)

**Yuxuan Zhang, Haozhong Xiong, Yubo Huang, Jiayi Song et al.** · 2026-08-13

<details>
<summary>Abstract</summary>

Pose-driven human animation synthesizes a video of a target person from a single reference image and a driving pose stream. Real-time generation is essential for interactive applications such as live streaming, telepresence, and virtual avatars, yet diffusion-based systems require minutes to hours per clip, precluding responsive interaction. We present LiveAnimate, to our knowledge the first animation system to combine real-time streaming with stable long-form generation at billion scale, built on a 14B-parameter video Diffusion Transformer (DiT). A two-stage training pipeline first adapts a pretrained bidirectional DiT into a block-causal autoregressive generator through Reference-Anchored Teacher-Forcing Adaptation, and then reduces the sampling budget to three steps through Block-wise Self-Forcing Distillation. To preserve appearance over extended streams, we introduce Pose-Retrieval Sink Attention (PR-Sink), a bounded KV-cache mechanism combining a Static Sink that permanently anchors the first generated block, a Dynamic Sink that holds a pose-retrieved historical block, and a three-slot Rolling Window. When a pose recurs, PR-Sink restores the relevant appearance context without retaining the entire sequence, so memory and per-block latency remain constant regardless of stream duration. Together with Ulysses sequence parallelism and operator fusion, these designs enable 19.63\,FPS streaming inference on two NVIDIA H100 GPUs. On a three-minute benchmark, LiveAnimate maintains nearly constant perceptual quality and identity from the first 30 seconds to the final minute, while prior systems degrade substantially or require hours of offline computation for the same rollout. These results establish a new operating point in quality, latency, and duration for interactive full-body animation.

</details>

#### [UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos](https://arxiv.org/abs/2608.11752) · [📄 Read](papers/2026/2608.11752.md)

**Yuxuan Zhang, Haozhong Xiong, Jiayi Song, Jinpeng Yu et al.** · 2026-08-13

<details>
<summary>Abstract</summary>

Talking-video character replacement requires coordinated transfer of appearance and voice while preserving the source motion, scene, linguistic content, and audio-video timing. Existing methods use separately optimized models for the two modalities, making audio-visual consistency difficult to enforce. We present UniSwap, the first framework for streaming joint audio-visual identity replacement in talking videos. Given a source video, a reference image, and a reference voice clip, UniSwap transfers the reference appearance and vocal timbre within a single audio-visual diffusion transformer while preserving the source content and dynamics. To address the scarcity of aligned cross-identity training pairs, we introduce a swap-and-reconstruct pipeline that removes visual and vocal identity from real clips and uses the original clips as reconstruction targets. Starting from a bidirectional backbone, we progressively adapt the model through In-context Pretraining for joint replacement, Conditional Streaming Adaptation for block-causal KV-cached generation, and Efficient Self-forcing DMD for mitigating exposure bias and reducing sampling from 30 to 3 denoising steps per block. Efficient Multi-LoRA Switching enables the three DMD roles to share a single frozen backbone. Feature-RoPE Decomposition keeps cached positions within the training range, supporting stable long-form inference. Experiments demonstrate strong audio-visual synchronization, competitive identity preservation, efficient streaming, and stable long-form generation.

</details>

#### [Avatar-Forever: Decoupled Parallel Training for High-Quality Real-Time Infinite Avatars](https://arxiv.org/abs/2608.12107) · [📄 Read](papers/2026/2608.12107.md)

**Ruibin Li, Tao Yang, Zhiyuan Ma, Fangzhou Ai et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Existing streaming video systems often rely on sequential, distillation-centered training pipelines to enable few-step long-video generation. However, this paradigm suffers from two limitations. First, failures or distribution shifts introduced in earlier stages affect later optimization, complicating the training process to converge. Second, the distillation-centric objective favours short-term generation but is prone to quality degradation when autoregressive errors accumulate over long rollouts. We propose Avatar-Forever, a decoupled parallel training framework for high-quality real-time infinite interactive avatars. Instead of coupling generation efficiency and long-horizon robustness under a sequential distillation pipeline, we treat them as two independent capabilities that can be trained in parallel. One branch performs full-parameter distillation to train an efficient generator with high visual quality, while another trains a lightweight long-horizon adapter via Recovery-oriented Rollout Training (RRT), which improves generation robustness under long-horizon inference conditions. Our decoupled parallel training design simplifies the overall training process and avoids unnecessary objective conflicts between few-step generation and long-horizon adaptation. We further introduce ForeverCache, a chunk-wise feature caching mechanism to substantially reduce redundant history computation during streaming inference. Built upon a 22B video foundation model, Avatar-Forever supports unbounded audio-driven avatar generation while maintaining identity consistency, motion coherence, and visual fidelity, enabling an end-to-end throughput of high-resolution 768x512 videos at 27.2 FPS on a single H100 GPU and providing a practical path toward stable digital humans.

</details>

#### [DAVE: A Decoupled Audio-Visual Enhancement Framework for Real-World Speech Separation](https://arxiv.org/abs/2608.09288) · [📄 Read](papers/2026/2608.09288.md)

**Wei Zhou, Wanyi Ning, Yinshang Guo, Qianxiao Fang et al.** · 2026-08-10

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement under real-world conditions remains challenging due to unreliable visual inputs and the lack of large-scale training data with realistic acoustic conditions. Existing approaches usually fuse visual features directly into the separation network, making them vulnerable to degraded visual signals. In this paper, we present DAVE, a decoupled audio-visual enhancement framework for real-world speech separation. Firstly, to address the data scarcity issue, we construct DAVE-Corpus, a large-scale training corpus with 219,411 mixtures generated from public meeting corpora through combinatorial acoustic augmentation. Then, we introduce a progressive multi-objective optimization strategy to jointly improve speech separation, intelligibility, speaker identity preservation, and perceptual quality. We further develop a certified selective enhancement chain that applies scene routing, GAN-based denoising, and loudness normalization only within the no-reference partition, guaranteeing non-degradation of reference-based metrics. Experimental results on the Real-World Audio-Visual Speech Enhancement Challenge demonstrate the robustness of DAVE under both real-world mixed scenarios and visual degradation conditions.

</details>

#### [Xemo-Talker: Unlock Emotions Explicitly for Audio-Driven Talking Portrait Synthesis](https://arxiv.org/abs/2608.14700) · [📄 Read](papers/2026/2608.14700.md)

**Chaolong Yang, Yinuo Guo, Kai Yao, Yuyao Yan et al.** · 2026-08-10

<details>
<summary>Abstract</summary>

Precise emotion control in audio-driven talking heads remains a challenge due to the reliance on implicit emotion regulation in existing systems, which often leads to indirect and insufficient control. Additionally, training with explicit emotion-related losses across the entire motion space poses significant difficulties due to the inherent trade-off between accurate lip synchronization and fine-grained emotion control. In this paper, we reveal a key finding: although emotional cues are distributed throughout the motion space, concentrating discriminative supervision on less-principal components achieves a better emotion-lip synchronization balance, as principal components mainly encode high-energy articulation and pose variations. Building on this insight, we propose Xemo-Talker, which first learns a neutral speech-to-motion mapping for stable articulation and lip synchronization, and then introduces a lightweight emotion branch guided by less-principal subspace supervision. To enhance emotion control, we design a Tri-Loss consisting of inter-class separation, intra-class compactness, and less-principal contrastive learning. Given an audio input, a reference image, and an emotion label, Xemo-Talker achieves state-of-the-art emotion classification accuracy while maintaining competitive lip synchronization and high inference efficiency, with performance approaching that measured on real videos.The source code is publicly available at https://github.com/chaolongy/Xemo-Talker.

</details>

#### [Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection](https://arxiv.org/abs/2608.06865) · [📄 Read](papers/2026/2608.06865.md)

**Xuechao Zou, Shun Zhang, Kai Li, Yi Zhou et al.** · 2026-08-07

<details>
<summary>Abstract</summary>

The malicious use of generative artificial intelligence to create highly realistic deepfake videos raises serious ethical concerns and poses substantial challenges to AI safety. However, existing deepfake video benchmarks provide limited coverage of recent synthesis methods and generally lack reliable fine-grained textual annotations. Meanwhile, conventional detectors and multimodal large language models (MLLMs), whether operating as a single model or relying on a single analytical perspective, often fail to capture subtle forgery artifacts, limiting their generalization to emerging AI-generated methods. To address these limitations, we introduce FaceVid-Forensics-100K, a large-scale deepfake video dataset comprising 100,000 videos and spanning 33 synthesis methods across face swapping, face reenactment, and entire-face synthesis, including recent generators such as Seedance 2.0. The dataset provides fine-grained textual annotations of visual observations and verdict-consistent forensic explanations, automatically synthesized through a multi-model aggregation and conflict-resolution pipeline powered by advanced MLLMs. Building on this benchmark, we propose a multi-agent forensic reasoning framework that employs four specialized domain-expert agents to independently analyze forgery cues from four perspectives: texture, lighting, motion, and physics. A judge agent then reconciles their reports to produce a final prediction together with an explanation. Extensive evaluations on out-of-domain test sets show that, despite being composed entirely of small open-source MLLMs, our framework outperforms all methods including closed-source GPT and Gemini models and ranks first across all reported metrics on this benchmark. The project page is available at https://xavierjiezou.github.io/ARGUS/.

</details>

#### [Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663) · [📄 Read](papers/2026/2608.05663.md)

**Menglin Han, Yang Ding, Yulei Lu, Haoran Yu et al.** · 2026-08-06

<details>
<summary>Abstract</summary>

Real-time long-form avatar audio--video generation requires causal, continuous synthesis while maintaining audiovisual synchronization and visual consistency. Adapting a pretrained bidirectional model to this setting presents two key dilemmas. First, autoregressively reusing generated blocks as context creates exposure bias, causing errors and visual drift to accumulate over long rollouts. Second, a global speech utterance does not indicates a causal generator which portion should be spoken next when only limited local audio--video context is available. We present \textbf{Vorch-Streamer}, a post-training framework that addresses these challenges and enables real-time long-form Text-to-Audio-Video (T2AV) streaming. We construct a synthetic corpus of 80K avatar clips spanning 12--21 seconds and first train a causal generator with mixed Teacher Forcing and Diffusion Forcing. We then apply long-horizon Self Forcing with DMD distillation, exposing the model to its own rollout distribution while preserving the quality of the pretrained bidirectional teacher. To explicitly control speech progression, an external language model predicts discrete 25-Hz speech-planning tokens, whose continuous features condition the audio diffusion branch and align each causal block with the content it should speak. With bounded causal context and four-step denoising, Vorch-Streamer jointly generates audio and video from text at 27.12 FPS, exceeding the 24-FPS real-time playback rate while maintaining competitive audio--lip synchronization and strong identity preservation over long-form generation.

</details>

#### [Wan-Animate-2: Pushing the Application Boundaries of Character Animation](https://arxiv.org/abs/2608.06009) · [📄 Read](papers/2026/2608.06009.md)

**Guangyuan Wang, Li Hu, Dechao Meng, Zhongyi Zhang et al.** · 2026-08-06

<details>
<summary>Abstract</summary>

Character image animation remains a foundational yet challenging task in computer vision. Existing approaches can be broadly categorized into three paradigms: methods based on explicit motion representations suffer from extraction errors and identity drift; methods based on implicit motion features lose fine-grained dynamics through compression; and in-context learning approaches avoid intermediate representations but incur prohibitive computational costs. Furthermore, all current systems are designed for offline synthesis, unable to meet the real-time requirements of interactive applications such as digital avatars and live-streaming hosts. To address these limitations, we present Wan-Animate-2, an end-to-end character animation framework that directly consumes the driving video within a redesigned Diffusion Transformer. Our architecture achieves superior motion fidelity and identity preservation by eliminating intermediate motion extractors entirely. We further introduce text driven viewpoint control that decouples the output camera perspective from the driving video--a capability rarely supported by prior character animation methods that rely on explicit motion representations. Beyond generation quality, we present Wan-Animate-2-Lite, an efficient variant that reduces inference latency to real-time thresholds through a three-stage training paradigm: teacher forcing pretraining with error buffer mechanism, and Self-Forcing distillation with chunk-wise backpropagation. This enables streaming character animation for interactive applications, opening new deployment scenarios that were previously infeasible. Qualitative evaluations and user studies demonstrate that Wan-Animate-2 achieves high-fidelity animation results across diverse characters and motion patterns. To foster further research and community development, we will release the Wan-Animate-2-Base model weights to the public.

</details>

#### [Recognizing Co-Speech Gestures in-the-Wild](https://arxiv.org/abs/2605.31589) · [📄 Read](papers/2026/2605.31589.md)

**Sindhu B Hegde, K R Prajwal, Andrew Zisserman** · 2026-08-06

<details>
<summary>Abstract</summary>

While humans naturally gesture during speech, only a sparse subset of these co-speech gestures are visually depictive and semantically linked to specific spoken words. In this paper, we introduce a large-scale dataset -- Gesture Recognition in the Wild (GRW), comprising co-speech gestures corresponding to a diverse vocabulary of 155 words. GRW contains 140k manually annotated video clips where the word is spoken, with 17k instances of semantic co-speech gestures including their frame-level temporal boundaries. The video clips are collected 'in the wild' from public-facing discourse, including lectures, talk shows, and interviews, covering a diverse range of speakers and visual conditions. We also introduce video models to: (a) classify gestures as semantic or not; (b) recognize the word corresponding to a co-speech gesture; and (c) temporally localize the gesture. These models are trained and evaluated on the GRW dataset and compared against a range of strong baselines, establishing benchmark results for all three tasks. The dataset, annotations, and trained models are publicly available on the project website: https://www.robots.ox.ac.uk/~vgg/research/grw.

</details>

#### [PD-GS: Phoneme-Driven 3DGS for Audio-Driven Talking Heads](https://arxiv.org/abs/2608.05218) · [📄 Read](papers/2026/2608.05218.md)

**Ao Fu, Yi Zhou** · 2026-08-05

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables fast, photorealistic talking-head rendering, yet accurate lip articulation remains elusive: mouth motion is often over-smoothed and may violate hard articulatory constraints such as bilabial closures, producing the notorious ``leaky mouth'' artifact. A key difficulty is that brief, discrete articulatory events are inferred from a continuous acoustic embedding under a regression objective, which biases predictions toward averaged mouth configurations. While modern self-supervised speech encoders provide rich prosodic and phonetic cues, they do not provide an explicit, frame-aligned linguistic target that reliably disambiguates closure-level events. We propose \textbf{Phoneme-Driven Gaussian Splatting (PD-GS)}, which augments a 3DGS talker with time-aligned phoneme tokens obtained from an automatic ASR and forced-alignment pipeline. Our core component, the \textbf{Linguistic Fusion Module (LFM)}, adaptively fuses continuous audio context with discrete phoneme embeddings through a learned gate, allowing the model to preserve smooth audio-driven dynamics while strengthening phoneme guidance on articulation-critical segments. PD-GS is trained purely from monocular video using image reconstruction and lip landmark supervision. On HDTF, PD-GS achieves the best lip geometry among the compared baselines (LMD 2.66) and qualitatively reduces closure violations in challenging phoneme sequences, yielding more linguistically faithful neural avatars.

</details>

#### [ETHead: Generating Expressive 3D Facial Animation and Head Movement from Speech](https://arxiv.org/abs/2608.01605) · [📄 Read](papers/2026/2608.01605.md)

**Jiu-Cheng Xie, Jiwang Zheng, Yongkang Xia, Jian Xiong et al.** · 2026-08-03

<details>
<summary>Abstract</summary>

Generating expressive 3D talking heads solely from speech remains a significant challenge due to the scarcity of high-fidelity 3D data, which limits the modeling of complex emotional motion patterns. In this paper, we introduce \textbf{E}xpressive \textbf{T}alking \textbf{Head} (ETHead), a method for generating 3D facial and head motions that vividly align with the emotional content of input speech. To overcome the data limitations, we design a self-distillation framework that leverages large-scale 2D talking videos to pre-train a specialized speech encoder. By incorporating a novel emotion-modulated probabilistic masking mechanism, this framework aligns speech representations with expressive visual dynamics, allowing the encoder to extract features highly correlated with facial and head motions directly from audio. These features are then leveraged to guide 3D generation, enriching input cues and providing explicit supervision through a joint speech-motion latent space. Extensive experiments demonstrate that ETHead substantially outperforms state-of-the-art methods. Furthermore, our motion-aligned speech encoder can serve as a transferable module, offering a general solution for enhancing expressiveness in other 3D talking head animation frameworks. The project page is available at https://verdure-oss.github.io/ETHead.github.io/.

</details>

#### [Proxy Avatar Meets Low-Rank Caching: Real-Time One-Shot Emotion-Controllable Portrait Animation](https://arxiv.org/abs/2608.01978) · [📄 Read](papers/2026/2608.01978.md)

**Haijie Yang, Jindi Bao, Yixuan Dong, Hongliang Zhang et al.** · 2026-08-03

<details>
<summary>Abstract</summary>

Audio-driven portrait animation has advanced rapidly with diffusion-based generative models, yet real-time one-shot generation with expressive emotion control remains challenging. Existing methods often suffer from insufficient emotion-aware motion priors and expensive appearance computation during multi-step denoising. To address these issues, we propose Proxy Avatar Meets Low-Rank Caching, a cascaded framework for real-time one-shot emotion-controllable portrait animation. Instead of directly generating the target portrait from audio, our method uses a Gaussian-based emotion proxy avatar as a reusable motion generator, which is trained once on a single identity to produce expressive driving videos from audio and emotion labels. Since the proxy avatar only provides motion rather than target appearance or geometry, a large-scale one-shot retargeting model further extracts identity-independent motion from the proxy performance and adapts it to arbitrary target portraits. To improve inference efficiency, we introduce zero-shot appearance reuse with low-rank caching, which caches reference appearance features at the initial denoising step and models subsequent feature variations using lightweight low-rank adapters. Extensive experiments demonstrate that our method achieves stronger emotional expressiveness, better identity-preserving animation, and substantially reduced inference cost, enabling real-time one-shot portrait animation.

</details>

#### [StreamTalk: Streaming Co-Speech Gesture Generation with Key-Pose Anchoring](https://arxiv.org/abs/2608.01643) · [📄 Read](papers/2026/2608.01643.md)

**Xiangyue Zhang, Jianfang Li, Jiaxu Zhang, Kaixing Yang et al.** · 2026-08-03

<details>
<summary>Abstract</summary>

Real-time co-speech gesture generation must produce 3D motion clip by clip as speech arrives. Existing streaming methods are open-loop: each clip depends on past context, but the model cannot check or correct its trajectory. Small errors therefore accumulate and cause drift over long sequences. We observe that this failure is mainly caused by the lack of a forward constraint rather than poor short-clip quality. A plausible key pose at the end of each clip provides a destination anchor that limits drift. Based on this observation, we propose StreamTalk, a closed-loop framework with a periodic generate-retrieve-refine cycle. Streaming Pose-Guided Generation first predicts a coarse clip, retrieves a plausible tail pose from a speaker-specific motion database, and refines the clip using this pose before continuing to the next window. During training, Stochastic Anchor Masking randomly masks pose and translation frames, teaching the model to recover complete motion from sparse boundary conditions. A part-aware DiT separates hand, body, and translation streams to reduce interference between global displacement and local articulation. On BEAT2, StreamTalk achieves state-of-the-art FGD, reduces long-horizon drift relative to open-loop baselines, and runs in real time at 76 FPS. Project page: https://xiangyue-zhang.github.io/StreamTalk/.

</details>

#### [SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct and Zero-Shot Tasks](https://arxiv.org/abs/2608.02023) · [📄 Read](papers/2026/2608.02023.md)

**Yu Zhang, Ruiqi Li, Changhao Pan, Ke Lei et al.** · 2026-08-03

<details>
<summary>Abstract</summary>

Speech and audio generation is often needed in animation dubbing, audio drama, movies, advertising, games, podcasts, and short-video production. In these scenarios, creators may need to design voices without reference recordings, control speaker styles with natural language, support acoustic scenes with environments and audio effects, and later reuse the designed voices. Therefore, it is important to support multi-speaker speech and audio generation for both instruct and zero-shot tasks. The instruct task requires a caption of the environment, speaker styles, and fine-grained content, while the zero-shot task uses reference audio together with the same fine-grained content. We address these tasks from both the data and model sides. First, we propose SwanData-Caption, which cleans raw speech and audio data, adds targeted synthetic coverage, and annotates diverse and accurate multi-level captions. Then, we propose SwanTale, a multi-speaker expressive speech and audio generation model that supports both zero-shot and instruct tasks. We introduce SwanVAE to support high-quality multi-audio-modality generation. Then, we adopt reward-conditioned quality control and Engram conditioning, along with Unified MoE for multi-task and multi-audio-modality modeling. In addition, we use curriculum learning and GRPO post-training to let the model progressively learn and strengthen its capabilities. Experimental results show that SwanTale leads on multiple key zero-shot and instruct metrics, achieves the best expressiveness scores in both tasks, and supports complex instruct generation involving multi-speaker speech and audio. Demos can be found at https://swanaigc.github.io/\#swantale.

</details>

#### [SubtleTalk: Generating Controllable Weakly-correlated Facial Dynamics for 3D Talking Heads via Residual Flow Matching](https://arxiv.org/abs/2608.06408) · [📄 Read](papers/2026/2608.06408.md)

**Chenyang Ding, Shuai Tan, Qunfen Lin, Xinwei Jiang et al.** · 2026-08-03

<details>
<summary>Abstract</summary>

Audio-driven 3D facial animation aims to synthesize realistic and temporally coherent motions from speech. Despite notable progress in lip synchronization, weakly correlated dynamics, including eyebrow movements, eye blinks, and head motion, which are essential to photorealistic facial animation, remain difficult to model faithfully and often appear static or unnaturally repetitive. We attribute this limitation to three factors: (a) insufficient conditioning for weakly correlated dynamics; (b) the limited ability of deterministic regression to capture diverse motion patterns; (c) data bottlenecks from unreliable upper-face pseudo-labels and limited dataset diversity. To address these issues, we propose SubtleTalk, a framework for generating natural and controllable weakly correlated facial dynamics via multi-condition modeling and residual flow matching. First, to compensate for the limited guidance of speech alone, we introduce interpretable controls, including prosody, regional intensity, and Valence-Arousal signals, to explicitly capture the timing, magnitude, and affective variation of weakly correlated dynamics. Second, to overcome the limited expressiveness of deterministic regression, we build residual flow matching based on a stable speech-driven motion prior, allowing the model to capture stochastic deviations beyond deterministic prediction. Third, to alleviate the data bottleneck, we construct SubtleTalk-Face, a large-scale 3D facial animation dataset comprising about 3,900 identities and 74 hours of data, built via a simple and scalable pseudo-labeling pipeline and featuring improved upper-face tracking and frame-level VA annotations. Extensive experiments demonstrate that our method significantly improves the realism and diversity of weakly correlated facial dynamics while preserving accurate lip synchronization.

</details>

#### [Geometry-guided Emotion Modulation for Controllable and Photorealistic Emotional Talking Face Generation](https://arxiv.org/abs/2608.00663) · [📄 Read](papers/2026/2608.00663.md)

**Chenggong Hu, Shaoyin Ma, Yi Wang, Li Sun et al.** · 2026-08-01

<details>
<summary>Abstract</summary>

Audio-driven emotional talking face generation aims to synthesize realistic videos with expressive facial dynamics. However, existing methods struggle to balance controllability and visual fidelity. Although implicit representations capture rich semantics, they lack structural guidance, often resulting in averaged emotional expressions. In contrast, explicit geometric methods offer better control over facial expressions but tend to sacrifice high-frequency texture details. To address it, we propose GemTalk, a diffusion-based framework that combines the semantic richness of implicit representations with the structural precision of explicit geometric priors. We introduce a Vision-guided Audio Emotion Projection (V-AEP) module to extract implicit emotional lip and expression features. At the same time, a Diffusion-based Geometric Priors Generator (D-GPG) generates identity-aware blendshape coefficients as explicit structural priors. Crucially, our Geometry-guided Emotion Modulation (GEM) module leverages these geometric priors to recalibrate the magnitude of implicit features, enabling precise, continuous control over emotional expressions, especially emotion intensity, without sacrificing visual quality. Extensive experiments show GemTalk achieves superior performance in photo-realism, and facial emotional dynamics.

</details>

#### [ReGenVC: End-to-End Real-Time Generative Video Coding at Ultra-Low Bitrate](https://arxiv.org/abs/2607.28144) · [📄 Read](papers/2026/2607.28144.md)

**Zheyuan Zhang, Johnson Wu** · 2026-07-30

<details>
<summary>Abstract</summary>

We present ReGenVC, an end-to-end generative video codec that compresses talking-head video to an ultra-low bitrate and decodes it in real time. The encoder reduces a source clip to a compact bitstream -- a neurally compressed first frame, per-frame pose keypoints, and metadata -- totaling about 26 kB for a 77-frame sequence. The decoder is a four-step distilled diffusion transformer that reconstructs the video conditioned on the transmitted pose and reference frame. Compared with x264/x265, ReGenVC reduces the bitrate to roughly one tenth of that required by traditional codecs (about 26 kB vs. 250--280 kB for essentially artifact-free reconstruction); at a matched ultra-low bitrate, conventional codecs collapse into blocking artifacts while ReGenVC stays sharp by exploiting a strong generative prior. The central obstacle to deploying such a codec is decoder latency: multi-step sampling with transformer and VAE components is too slow for interactive use. We make the decoder real-time through four-step distillation and three model-preserving system techniques: (i) eight-GPU unified sequence parallelism (Ulysses & Ring), (ii) a spatially-split VAE, and (iii) a three-stage overlapped pipeline; an analytical timing model characterizes the real-time feasibility region. On an 8-GPU node, the system sustains 24 fps output (972 ms per 25-frame window, within the 1000 ms budget), enabling a live browser stream without observed frame underruns. A hybrid CPU-GPU deployment further runs the encoder on the CPU at 24 fps and offloads the decoder-side one-shot conditioning encoders to the CPU, reducing the per-GPU memory peak from 21.1 GB to about 7.7 GB. To our knowledge, ReGenVC is the first end-to-end generative video codec to combine ultra-low-bitrate encoding with real-time decoding on an 8-GPU system.

</details>

#### [TongueReenact: Geometry-Anchored Tongue Synthesis for Face Reenactment](https://arxiv.org/abs/2607.28039) · [📄 Read](papers/2026/2607.28039.md)

**MD Wahiduzzaman Khan, Mingshan Jia, Xiaolin Zhang, En Yu et al.** · 2026-07-30

<details>
<summary>Abstract</summary>

Modern face reenactment systems achieve impressive pose and expression transfer using geometry-driven representations. However, they largely ignore tongue dynamics, leading to anatomically inconsistent mouth interiors during speech and expressive motions. We introduce the first framework for cross-identity tongue dynamics transfer in face reenactment. We propose a foundation-model-assisted bootstrapping pipeline that produces a dedicated tongue segmentation model for in-the-wild reenactment without curated annotations. We further introduce a spatially constrained latent masked diffusion model for realistic tongue synthesis, with adaptive mask dilation for seamless mouth boundary transitions. Extensive experiments demonstrate improvements of more than two times over all baselines on every tongue-specific metric. We additionally propose a VLM-based evaluation protocol that replicates expert annotation at scale, confirming perceptual superiority across all ablation variants.

</details>

#### [LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation](https://arxiv.org/abs/2608.00079) · [📄 Read](papers/2026/2608.00079.md)

**Rongxiang Zhang, Songhua Liu** · 2026-07-29

<details>
<summary>Abstract</summary>

Long-form and real-time talking-head generation remains challenging due to a latency-quality trade-off: inefficient multi-step diffusion prohibits streaming generation, whereas real-time autoregressive approaches suffer from error accumulation and identity drift. To address this drawback, we propose LeapTalk, a novel framework that achieves stable and real-time talking-head generation with a single forward step, scaling to arbitrarily long videos. At the heart of our approach lies a single-step bridge distillation scheme. On the one hand, departing from the conventional noise-to-data paradigm, we introduce a data-to-data transport formulation based on a Brownian bridge. Anchored by a persistent reference, this strategy effectively mitigates identity drift and enhances long-term temporal stability. On the other hand, to enable smooth knowledge transfer from a pre-trained diffusion teacher to the student bridge model, we explore a heterogeneous distillation framework with an SNR-aligned time transformation $Φ(τ)$, which bridges the functional discrepancy between the two models. Moreover, we propose an audio-driven classifier-free guidance mechanism to maintain fine-grained lip synchronization under extreme step reduction. Extensive experiments demonstrate that our method achieves high-fidelity and temporally consistent video generation with only 1 step at up to 200 FPS, significantly outperforming existing approaches in both efficiency and stability. Project Page: https://zhangrongxiang.github.io/leaptalk-page/

</details>

#### [ViDS: Video Diffusion Shader using 3D Face Tracking](https://arxiv.org/abs/2607.24124) · [📄 Read](papers/2026/2607.24124.md)

**Wenbo Ji, Davide Davoli, Zhe Chen, Liam Schoneveld et al.** · 2026-07-27

<details>
<summary>Abstract</summary>

We introduce ViDS, a Video Diffusion Shader that leverages 3D face tracking for expressive and identity-preserving portrait animation. We first reconstruct the identity-specific 3DMM mesh from the reference image, and then animate it using expression and pose parameters from a driving video. Leveraging dense geometric cues from 3DMM normal maps, we employ a video diffusion model as a neural shader to synthesize lifelike portrait animations while preserving the appearance and identity of the reference image. We find that more accurate 3DMM tracking enables finer-grained expression control. We also introduce an autoregressive diffusion sampling process that extends generation beyond the model's native window while reducing discontinuities between adjacent clips. Compared with prior diffusion-based approaches for portrait animation that rely on landmark-based conditioning or implicit motion latents, our method achieves more detailed and consistent expression and pose control while faithfully preserving identity and appearance. Detailed ablation studies validate the effectiveness of our design choices. Project page: https://fusheng-ji.github.io/ViDS/

</details>

#### [AptAvatar: Fast and Vivid Long-Form Audio-Driven Video Generation for Production-Ready Avatars](https://arxiv.org/abs/2607.24013) · [📄 Read](papers/2026/2607.24013.md)

**Hengyuan Zhang, Jingna Sun, Meiguang Jin, Junfeng Ma** · 2026-07-27

<details>
<summary>Abstract</summary>

Production-ready audio-driven avatar generation requires efficient inference without sacrificing fidelity or motion expressiveness. However, existing acceleration methods often compromise quality through restrictive architectural choices, such as causal attention and short temporal horizons, or by reducing model capacity and resolution. Without such compromises, we propose AptAvatar, a 14B-parameter long-form audio-driven avatar generation framework that delivers fast and expressive inference. For efficiency in production-level applications, AptAvatar addresses the extreme two-step generation challenge. To bridge the gap between the multi-step teacher model and the two-step student model, we introduce Endpoint-Anchored Distribution Distillation. It augments vanilla distribution matching with a dedicated Anchor Score Estimator trained on the trajectory-endpoint distribution defined from a frozen pretrained 4-step bridge generator. This provides an attainable endpoint-level anchor for the evolving two-step student. To improve long-horizon consistency, we further introduce Self-Generated History Replay, which reuses cached outputs from earlier generator checkpoints as history conditions during chunk-wise training. This approximates inference-time conditioning on self-generated histories without costly online rollouts, mitigating quality degradation from accumulated history errors. Extensive experiments demonstrate that AptAvatar generates vivid 720p long-form avatar videos with only 2 NFEs, achieving a 60x speedup while preserving visual fidelity and long-horizon identity. Code is available at https://github.com/TaoLiveAIGC/AptAvatar

</details>

#### [STEER: Steerable Dyadic Head Avatars](https://arxiv.org/abs/2607.23840) · [📄 Read](papers/2026/2607.23840.md)

**Kartik Teotia, Helge Rhodin, Hyeongwoo Kim, Marc Habermann et al.** · 2026-07-26

<details>
<summary>Abstract</summary>

Facial movement and expression are central to face-to-face communication, conveying turn-taking, attention, agreement, and engagement alongside speech. While speech-driven facial animation has made strong progress in lip synchronization and audio-conditioned motion generation, most methods treat conversational behavior as an emergent byproduct of audio, or expose only coarse sequence-level affect control. As a result, key non-verbal channels such as gaze contact and aversion, rhythmic head motion, and emotion remain difficult to explicitly control. We present STEER, a controllable 3D dyadic motion prior for reactive conversational head avatars. STEER factorizes conversational behavior into explicit controls for gaze, head rhythm, and emotion, allowing users to steer how an avatar listens, reacts, and engages with a conversation partner. Since temporally aligned annotations for these behaviors are not available in public dyadic corpora, we introduce a tracking and annotation pipeline that recovers behavioral pseudo-labels from in-the-wild dyadic video. A causal flow-matching transformer then learns partner-aware target motion conditioned on audio, partner motion, emotion and the proposed behavioral controls. We further embed STEER in a photorealistic avatar pipeline by extending a Universal Gaussian Head-Avatar Prior with a learned mapping from tracked parametric motion into its avatar-driving space. This enables controllable animation of high-fidelity Gaussian head avatars without re-training the underlying avatar model. STEER outperforms recent dyadic motion baselines on motion quality, dynamics, and diversity, remains competitive on partner coupling, and enables gaze, head-rhythm, and emotion edits together with an interactive live deployment. We make our code and dataset annotations available at our webpage.

</details>

#### [GRAPE: Graduated Routing for Articulated Portrait mesh Estimation](https://arxiv.org/abs/2607.23657) · [📄 Read](papers/2026/2607.23657.md)

**Yunfei Liu, Lijian Lin, Ye Zhu, Yu Li** · 2026-07-26

<details>
<summary>Abstract</summary>

Articulated portrait mesh estimation is fundamental to 3D understanding, avatar generation, and immersive interaction. Existing approaches primarily rely on 3D Morphable Models (3DMMs). However, face-centric models suffer from the "floating head" assumption, conflating head pose with global rotation due to the lack of neck kinematics. Conversely, body-centric models lack high-fidelity facial expression capabilities. Furthermore, current methods struggle to disentangle jaw articulation from expression blendshapes, often over-relying on expressions for mouth opening. These limitations make monocular portrait recovery difficult across representation, supervision, and anatomical parameter estimation. To address these limitations, we introduce GRAPE(Graduated Routing for Articulated Portrait mesh Estimation). We build a Portrait Parametric Model (PPM) with an explicit torso-to-head kinematic chain and a canonical injection step to merge FLAME and the SMPL-X torso. We propose a Progressive Anatomical Alignment (PAA) network, which is composed of a pretrained portrait encoder, a Graduated-Mask Router, and coarse-to-fine experts that follow the portrait anatomical prior. We then train this network with multi-source supervision that combines sparse anatomical keypoints, feature distillation, foreground mask constraints, and relative geometry constraints. Experiments show that GRAPE improves portrait mesh recovery quality, pose alignment, and jaw--expression disentanglement over prior methods. We also demonstrate that our method can benefit the downstream tasks of audio-driven talking-head generation and 3D portrait generation.

</details>

</details>
<!-- PAPERS_TABLE_END -->
