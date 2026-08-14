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

_Showing the last 30 papers (30 of 1123 total). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>Last 30 Papers</h3></summary>

#### [LiveAnimate: Stable Long-Form Streaming Human Animation in Real-Time](https://arxiv.org/abs/2608.11745)

**Yuxuan Zhang, Haozhong Xiong, Yubo Huang, Jiayi Song et al.** · 2026-08-13

<details>
<summary>Abstract</summary>

Pose-driven human animation synthesizes a video of a target person from a single reference image and a driving pose stream. Real-time generation is essential for interactive applications such as live streaming, telepresence, and virtual avatars, yet diffusion-based systems require minutes to hours per clip, precluding responsive interaction. We present LiveAnimate, to our knowledge the first animation system to combine real-time streaming with stable long-form generation at billion scale, built on a 14B-parameter video Diffusion Transformer (DiT). A two-stage training pipeline first adapts a pretrained bidirectional DiT into a block-causal autoregressive generator through Reference-Anchored Teacher-Forcing Adaptation, and then reduces the sampling budget to three steps through Block-wise Self-Forcing Distillation. To preserve appearance over extended streams, we introduce Pose-Retrieval Sink Attention (PR-Sink), a bounded KV-cache mechanism combining a Static Sink that permanently anchors the first generated block, a Dynamic Sink that holds a pose-retrieved historical block, and a three-slot Rolling Window. When a pose recurs, PR-Sink restores the relevant appearance context without retaining the entire sequence, so memory and per-block latency remain constant regardless of stream duration. Together with Ulysses sequence parallelism and operator fusion, these designs enable 19.63\,FPS streaming inference on two NVIDIA H100 GPUs. On a three-minute benchmark, LiveAnimate maintains nearly constant perceptual quality and identity from the first 30 seconds to the final minute, while prior systems degrade substantially or require hours of offline computation for the same rollout. These results establish a new operating point in quality, latency, and duration for interactive full-body animation.

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

#### [Recognizing Co-Speech Gestures in-the-Wild](https://arxiv.org/abs/2605.31589)

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

#### [OmniMate: Open-Ended Real-Time Streaming Audio-Visual Generation for Interactive Avatars](https://arxiv.org/abs/2607.23023) · [📄 Read](papers/2026/2607.23023.md)

**Quanyue Song, Yishan He, Yanbo Ding, Zhixiang He et al.** · 2026-07-25

<details>
<summary>Abstract</summary>

Recent advances in diffusion-based generative models have enabled real-time audio-driven avatar generation and unified audio-visual synthesis, providing a promising foundation for interactive avatar systems. However, extending these models to real-time interactive streaming remains challenging, as the generation horizon is unknown in advance and cross-modal identity consistency gradually degrades during long-term generation. To address these challenges, we propose OmniMate, a unified framework for open-ended real-time interactive audio-visual avatar generation. OmniMate jointly synthesizes visual content, speech, and audio effects in real time, enabling natural and immersive multi-turn interactions. To achieve adaptive response progression, we introduce a Generation Progress Controller (GPC) that explicitly models the generation progress of each streaming chunk, allowing the model to complete responses according to the desired progress and achieve seamless transitions between execution and listening states. To preserve long-term cross-modal identity consistency, we propose a Multi-Reference Conditioning Module (MRCM), which leverages multiple reference images and a reference speech segment to provide persistent visual and speaker identity cues throughout long-duration streaming interactions. Extensive experiments on an interaction-oriented adaptation of VerseBench demonstrate that OmniMate achieves high-quality, low-latency streaming generation while maintaining strong long-term audio-visual consistency. The results further show that OmniMate supports realistic, coherent, and responsive interactive avatar experiences over extended multi-turn conversations.

</details>

#### [ID-V2V: Identity-Preserving Video Restylization](https://arxiv.org/abs/2607.22830) · [📄 Read](papers/2026/2607.22830.md)

**Yuancheng Xu, Mingming He, Pablo Salamanca, Li Ma et al.** · 2026-07-24

<details>
<summary>Abstract</summary>

In visual storytelling, human performances are central to creative intent and narrative meaning. However, preserving human identity and performance while enabling flexible visual edits remains challenging for generative video models. We formalize this challenge as identity-preserving video restylization, which propagates scene, lighting, and style changes specified by an edited keyframe across a source video, while preserving facial likeness and performance, including expressions, eye gaze, and lip synchronization. A key obstacle is the absence of paired training data, as identity-preserving restylized video pairs are rare in real-world settings. To address this, we propose a decoupling of source-grounded identity preservation and edit-driven video synthesis. Our key insight is that facial appearance and expression should remain invariant, with illumination being the primary permissible variation. We therefore cast identity preservation as a video relighting problem, while modeling visual edit propagation as controlled video synthesis guided by the edited keyframe. Building on this formulation, we introduce ID-V2V, a video-to-video generative framework integrating complementary control signals: relit facial regions and facial normal maps tightly constrain facial likeness and performance, while edited keyframes and depth sequences enable flexible and temporally coherent generation. This design enables constructing training pairs from a single video, eliminating the need for scarce paired data. Extensive experiments demonstrate that ID-V2V significantly outperforms existing methods in preserving facial likeness and fine-grained facial performance, supports both single- and multi-subject scenarios, and delivers high visual quality, highlighting its potential as a human-centric tool for real-world content production. The code is available at: https://github.com/Eyeline-Labs/ID-V2V.

</details>

#### [Fusion Embedding: A Unified Embedding Space for Text, Image, Video, and Audio](https://arxiv.org/abs/2607.18666) · [📄 Read](papers/2026/2607.18666.md)

**Abdul Basit Tonmoy, Kazi Fardinul Hoque, Md. Shahrier Islam Arham, Arman Luthra** · 2026-07-21

<details>
<summary>Abstract</summary>

A single embedding space that covers text, images, video, and audio lets one index serve every query a user can pose. Embedding models built on vision-language backbones now lead text/image/video retrieval benchmarks but lack audio entirely, while audio-text retrieval is led by specialist systems that serve no other modality. We present the Fusion Embedding family, which adds audio to a frozen vision-language embedding base whose parameters are never updated: generation 1 (fusion-embedding-1) trains only a 16.4M-parameter connector between a frozen audio tower and the frozen base, and generation 2 (fusion-embedding-2) adds modality-gated deep adapters (44.2M parameters) whose branch never executes on text, image, or video inputs: their outputs are bit-for-bit those of the released base, verified after every training run. Because the base already binds text, images, and video, aligning audio to text alone makes audio-image retrieval emerge, with zero paired audio-visual training data. Alongside the recipe we map its design space with controlled negative results (rewriting training captions with an LLM, substituting a leaderboard-stronger audio tower, and widening the connector each reduce retrieval) and with training-protocol findings that we expect to transfer to any frozen decoder-LM embedding backbone. Both generations train in hours on a single GPU. Weights, code, and the evaluation harness are openly released.

</details>

#### [PolyInterview: An LLM-based Platform for Immersive Mock Interview Practice with Comprehensive Multimodal Assessment](https://arxiv.org/abs/2607.10310) · [📄 Read](papers/2026/2607.10310.md)

**Zhiyuan Wen, Jiannong Cao, Zijian Wang, Chen Chen et al.** · 2026-07-11

<details>
<summary>Abstract</summary>

Preparing for job interviews is important for securing desired positions, yet realistic practice remains difficult to access: real interviews are infrequent, expert mock coaching is costly, and self-practice offers neither adaptive dialogue nor structured assessment. Existing systems typically address only parts of this need through fixed question sequences, limited communication channels, or feedback with little supporting evidence. We present PolyInterview, an LLM-based platform for immersive mock interview practice with comprehensive multimodal assessment. PolyInterview uses the target job description and CV to generate questions tailored to the role and candidate, conducts multi-turn spoken interviews with a lip-synced digital human interviewer that asks answer-aware follow-up questions, and evaluates response content, vocal delivery, and non-verbal behavior. Four parallel evaluators produce 13 behavior-level features that are aggregated into 10 assessment aspects and two competency tracks. Guided by the KSA and STAR frameworks, the report links each score to behavioral evidence and actionable recommendations. PolyInterview is publicly accessible. Its current all-account snapshot contains 101 accounts, 1,564 interview sessions, 7,665 generated questions, and 1,422 five-stage question sets. Generated questions are more closely aligned with their matched job description than with cross-role job descriptions in 93.7% of sessions. An evaluation by ten experts found strong question plans and actionable feedback.

</details>

#### [Learn2Chat: Rethinking Dyadic Talking Heads via Interaction-Modulated Monologic Priors](https://arxiv.org/abs/2607.10313) · [📄 Read](papers/2026/2607.10313.md)

**Zikai Huang, Siyue Chen, Xuemiao Xu, Haoxin Yang et al.** · 2026-07-11

<details>
<summary>Abstract</summary>

Dyadic conversational motion generation is essential for realistic interactive digital humans. Existing approaches typically model conversational behaviors within unified dyadic generators. However, such holistic formulations tend to couple self-speech-driven motion with partner-responsive social feedback, leaving the interaction-specific component implicit and underutilizing the speech-motion correspondence already learned by pretrained monologic motion models. We propose Learn2Chat, a unified framework that models dyadic motion as interaction modulation over pretrained monologic motion priors. This design separates intrinsic speech-driven motion from social interaction effects and enables more structured interaction modeling. Specifically, we introduce a Monologic-Anchored Motion Factorization scheme that leverages the semantic motion manifold learned from monologic data to disentangle audio-driven motion dynamics from interaction-induced modulation, yielding clean interaction representations from dyadic sequences. On top of this representation space, a Cross-Attentive Interaction Latent Prediction module maps paired speech signals to interaction latents through cross-branch attention and interaction alignment. During inference, the predicted interaction latents modulate canonical monologic motion to generate coherent and synchronized dyadic behaviors in a data-efficient manner. Extensive experiments on the DualTalk benchmark demonstrate that Learn2Chat achieves state-of-the-art performance across both quantitative metrics and perceptual evaluations. Moreover, the framework is model-agnostic and seamlessly integrates with diverse pretrained monologic motion backbones, highlighting the effectiveness of prior reuse and interaction adaptation for scalable conversational motion generation. More visual results are available on the project page.

</details>

#### [Conversational Human Audio-visual Talking Dialogue Generation](https://arxiv.org/abs/2607.02799) · [📄 Read](papers/2026/2607.02799.md)

**Junhao Song, Lluis Guasch, Xilin He, Zhongyu Yang et al.** · 2026-07-02

<details>
<summary>Abstract</summary>

Large-scale dyadic interactive audio-visual dialogue (DIAD) datasets provide fundamental data resources for developing humanoid interactive virtual agents and digital humans. However, collecting such data is time-consuming, expensive, and ethically sensitive. To address this, we propose CHAT, a new dyadic interactive audio-visual dialogue generation (DIADG) framework that generates diverse, paired, and mutually responsive speech-face dialogue clips from a single textual prompt. CHAT unifies large language models and talking face models with interactive audio and facial behaviour refinement modules, enabling the generation of aligned dyadic dialogue clips with diverse contents and facial identities. Experiments show that CHAT outperforms existing related methods designed for similar tasks under both objective and subjective evaluations. Moreover, our synthesised CHAT-AVD-50k dataset serves as effective pre-training data for downstream interactive head generation, consistently improving PerFRDiff and ReactDiff on REACT 2024. CHAT offers a scalable alternative to the costly and ethically sensitive collection of real dyadic interaction data.

</details>

#### [GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting](https://arxiv.org/abs/2607.00959) · [📄 Read](papers/2026/2607.00959.md)

**Haijie Yang, Zhenyu Zhang, Yixuan Dong, Jianjun Qian et al.** · 2026-07-01

<details>
<summary>Abstract</summary>

Audio-driven talking head synthesis has achieved impressive progress in lip synchronization and visual quality, yet generating expressive emotional avatars with controllable intensity remains challenging, especially under real-time constraints. In this paper, we present GaussianEmoTalker, an audio-driven framework for real-time emotional talking head synthesis based on 3D Gaussian Splatting. Instead of directly predicting the final emotional avatar from speech, we formulate emotional animation as a neutral-to-emotional residual deformation problem. GaussianEmoTalker first constructs an identity-specific neutral talking space with GaussianBlendshapes, which provides high-fidelity Gaussian attributes and phoneme-synchronized neutral motion. It then predicts an emotion-conditioned residual deformation by combining mesh displacement cues, audio features, emotion categories, and intensity encodings. To fuse these heterogeneous signals, we introduce a spatial-audio-emotion attention module that estimates the offsets of Gaussian attributes for expressive and temporally stable rendering. Extensive experiments demonstrate that GaussianEmoTalker achieves competitive video quality, accurate lip synchronization, controllable emotional expression, and real-time rendering compared with recent emotional talking head methods. Our project page is available at https://njust-yang.github.io/GaussianEmoTalker.github.io/

</details>

#### [Multi-Modal Deepfake Detection via Spatial, Temporal, and Audio-Visual Fusion with Vision Transformers](https://www.semanticscholar.org/paper/5ad7261ad284f64c1b7776c990a9bbb305c402b5) · [📄 Read](papers/2026/s2:5ad7261ad284f64c1b7776c990a9bbb305c402b5.md)

**Merlin Gethsy D., S. V** · 2026-06-30

<details>
<summary>Abstract</summary>

The rapid advancement of the deepfake generation technologies has intensified concerns related to digital misinformation, identity impersonation, and media manipulation. Although numerous deepfake detection methods have been developed by mitigate these threats, most rely on a single modality and exhibit limited robustness when confronted with diverse manipulation techniques and cross-dataset scenarios. To overcome these deficiencies, we propose VeriSphere, a multimodal deepfake detection framework that combines spatial, temporal, and audiovisual forensics in one system. It uses a Vision Transformer for detecting spatial artifacts, an X-CLIP-based module for capturing temporality, and an AV synchronization module to examine whether speech aligns with lip movements. The outputs are then fused using a weighted strategy to produce a single trust score for prediction. Results show that VeriSphere achieves a high accuracy of 92.1%, an AUC of 0.963, and an F1-score of 0.924 across three benchmark datasets: FaceForensics++, Celeb-DF, and DFDC.

</details>

#### [Towards Flexible, Natural, Efficient Interaction for Conversational Talking Face Generation](https://arxiv.org/abs/2606.31088) · [📄 Read](papers/2026/2606.31088.md)

**Baiqin Wang, Sen Chen, Jiankuo Zhao, Xiangyu Liu et al.** · 2026-06-30

<details>
<summary>Abstract</summary>

Conversational talking face generation has recently attracted increasing attention, aiming to synthesize interactive talking videos where characters speak, listen, and respond dynamically to each other. This task presents three core challenges: 1) Flexibility: enabling multi-round dialogues with an arbitrary number of participants; 2) Naturalness: maintaining coherent motion and appropriate non-verbal feedback throughout the interaction; and 3) Efficiency: achieving real-time generation and low computation overhead for long-term continuous online conversation. Despite recent advances, existing methods still fall short in balancing all three requirements. To bridge this gap, we introduce InterTalk, a novel and efficient framework designed for highly interactive conversational talking face generation. Built upon a motion-based architecture, InterTalk supports real-time conversation synthesis. Our method achieves strong flexibility by explicitly modeling multi-round conversational dynamics among each participant, eliminating constraints on their numbers. To enhance interactivity, we incorporate motion feedback from multiple participants and introduce an iterative generation strategy for more natural behaviors. Besides, we disentangle motion into several facial components, enabling targeted refinements for natural response such as precise lip sync and realistic eye blinking. Finally, we construct a new multi-person conversational dataset and enrich it with 3D face-based data augmentation. Extensive experiments demonstrate that InterTalk achieves superior interaction quality while maintaining real-time performance at 30 FPS.

</details>

</details>
<!-- PAPERS_TABLE_END -->
