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

_Showing the last 30 papers (30 of 1142 total). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>Last 30 Papers</h3></summary>

#### [Decoupled Self-Forcing Distillation for Streaming Talking Head Generation](https://arxiv.org/abs/2609.10317)

**Yanru An, Ruiyan Wang, Wenwu Wei, Rui Bu et al.** · 2026-09-09

<details>
<summary>Abstract</summary>

Streaming talking-head generation produces each frame as its driving audio arrives, yet fidelity and efficiency have so far pulled in opposite directions: end-to-end methods condition a video diffusion model on audio directly and achieve high quality but only at large scale, while cheaper two-stage methods generate an intermediate motion representation and trail in fidelity. We argue the cost of the former lies in the target of fusion: the video latent is dominated by identity, appearance and background, none of which audio bears on, so coupling audio to every pixel blurs detail and wastes capacity. We instead fuse conditions in a low-dimensional identity-disentangled motion space, routing audio and motion captions by their temporal granularity, and generate motion latents with a small causal autoregressive transformer that a pretrained diffusion renderer turns into video. Conditions thus control video transitively, and high fidelity no longer requires a large backbone. Streaming this decomposition needs both models to be causal, and the exposure-bias problem could be solved by self-forcing given a bidirectional teacher. But there is no such teacher in motion space. Our decoupled self-forcing distillation resolves both models under one frozen teacher: conditioned on motion, it distills the renderer into a block-causal student; unconditionally, it scores rendered rollouts against real videos, supervising motion by the video it produces. This lifts the fidelity ceiling from the motion generator onto the stronger renderer. The two models run as parallel causal streams, reaching 15.4 FPS at 1.3 s latency with no quality degradation.

</details>

#### [Noise Adaptive Streaming Audio-Visual Speech Token Enhancement for Robust Full-Duplex Spoken Dialogue Models](https://arxiv.org/abs/2609.08390) · [📄 Read](papers/2026/2609.08390.md)

**Bella Godiva, Yeonju Kim, Yong Man Ro** · 2026-09-08

<details>
<summary>Abstract</summary>

Full-duplex spoken dialogue systems enable simultaneous listening and speaking, but their audio-only perception often fails under background noise and overlapping speech, leading to incoherent responses. Recent audio-visual dialogue approaches show that incorporating visual cues such as lip movements improve robustness under audio corruption. However, existing approaches often adapt the large speech dialogue model itself to process visual input, requiring costly multimodal training. We propose AV-STE, a modular streaming audio-visual front-end that restores corrupted semantic speech tokens from noisy audio and lip video before they reach the speech LLM. The downstream dialogue model remains entirely frozen, preserving its pretrained conversational capabilities. When integrated with frozen Moshi, AV-STE improves average GPT-4o-judged response coherence from 1.42 to 1.91 under same-dataset speaker interference while largely preserving turn-taking behavior. Gains also transfer to out-of-domain Seamless Interaction.

</details>

#### [TBDub: Production-Oriented Visual Dubbing](https://arxiv.org/abs/2609.06144) · [📄 Read](papers/2026/2609.06144.md)

**Bihan Li, Xinyang Li, Zeran Xu, Meiguang Jin et al.** · 2026-09-05

<details>
<summary>Abstract</summary>

Visual dubbing must synchronize mouth motion with replacement speech while preserving identity, appearance, and temporal consistency. Although X-Dub provides a strong mask-free video-editing baseline, its application to livestream and generated-video content reveals limitations in production-domain robustness, temporal and motion stability, identity and oral-detail preservation, and inference efficiency. We present \textbf{TBDub}, a production-oriented extension of X-Dub that combines task-adaptive post-training with task-aware few-step distillation. Post-training adapts the video DiT using production-domain data, production-specific conditioning and filtering, and enhanced audio features to obtain a 30-step Teacher. Distillation adapts DMD/DMD2 to conditional video editing and compresses the Teacher into a two-step Student. On 38 TalkVid clips, the Teacher improves all eight reported reconstruction, perceptual, identity, and synchronization metrics over X-Dub. In the MOS evaluation, it improves lip-sync consistency, identity consistency, and visual quality over X-Dub by 0.14, 0.95, and 0.90 points, while the Student achieves the highest lip-sync and visual-quality scores and remains close to the Teacher in identity consistency. In paired end-to-end generation timing from the first VAE encode through the final VAE decode on a single NVIDIA H20 GPU at $512\times512$, the Student reaches 7.13 effective FPS and reduces total latency by $13.93\times$; the DiT stage alone is accelerated by $42.49\times$. The Student largely retains the Teacher's generation quality and audiovisual synchronization. The code is available on GitHub at \https://github.com/TaoLiveAIGC/TBDub, and the 30-step Teacher and two-step Student weights are available on Hugging Face at https://huggingface.co/TaoLiveAIGC/TBDub.

</details>

#### [Alignment-Free Text-Audiobox for Voice Dubbing and Full-Duplex Dialogue Synthesis](https://arxiv.org/abs/2609.03992) · [📄 Read](papers/2026/2609.03992.md)

**Sanyuan Chen, Min-Jae Hwang, Sho Inoue, Anna Sun et al.** · 2026-09-03

<details>
<summary>Abstract</summary>

We present Alignment-Free Text-Audiobox (Text-AB), a unified framework for high-quality voice dubbing and full-duplex dialogue synthesis. Building on a Diffusion Transformer trained with a flow-matching objective, Text-AB departs from the Audiobox system along three dimensions. First, it operates in a latent diffusion framework using DAC-VAE features that encode 48 kHz waveforms into a 25 Hz latent sequence, giving over 10x higher compression than previous EnCodec representations while improving resynthesis quality. Second, Text-AB is alignment-free: it consumes raw text via an off-the-shelf text encoder and learns text-speech alignment through cross-attention, removing the need for forced alignment and explicit duration prediction. Third, we scale model and data substantially, pretraining a 3B-parameter model on 480k hours of monolingual speech, followed by supervised fine-tuning on three downstream tasks: cross-lingual voice dubbing, full-duplex dialogue synthesis, and emotional full-duplex dialogue synthesis. At inference, Text-AB supports one-shot generation for up to ~1 min of speech and arbitrarily long-form generation via a multi-diffusion scheme, plus a multi-stage reranking strategy that enhances quality based on automated metrics. On a real-world dubbing benchmark, Text-AB delivers a step-change improvement over the latest internal dubbing system, with large gains in prosody similarity, voice similarity, naturalness, and shareability. For full-duplex dialogue synthesis, it approaches human recordings on short-form conversations and substantially outperforms the latest internal model on long-form human-likeness and expressivity, while natively modeling turn-taking, back-channeling, and emotional dynamics. For emotional dialogue synthesis, emotion conditioning significantly improves emotion alignment and emotional interaction quality over the unconditioned baseline.

</details>

#### [Audio-Driven Adversarial Defense for 3D Talking Face Generation with totally Visual Fidelity Preservation](https://arxiv.org/abs/2608.30951) · [📄 Read](papers/2026/2608.30951.md)

**Rui-Qing Sun, Chen-Hao Cui, Hui-Yang Zhao, Tian Lan et al.** · 2026-08-31

<details>
<summary>Abstract</summary>

The rapid development of generative portrait models has raised growing concerns about privacy leakage and identity misuse. In particular, audio-driven 3D talking face generation can reconstruct a reusable 3D portrait of a target person from a monocular video and animate it with arbitrary speech, making realistic identity impersonation alarmingly practical. Existing proactive defenses mainly operate in the visual domain by injecting subtle perturbations into acial regions to disrupt identity acquisition. However, such perturbations often compromise visual quality due to the strong structural priors and social sensitivity of human faces, and are easily weakened by common real-world transformations such as resizing. To overcome these limitations, we propose an imperceptible audio defense for audio-driven 3D talking face generation by shifting protection from the visual modality to the audio modality. Specifically,we exploit psychoacoustic masking to hide protective perturbations within perceptually masked frequency regions of the speech signal, thereby reducing perceptual distortion while suppressing reliable facial animation. Extensive experiments demonstrate that the proposed method effectively degrades 3D talking face generation while preserving favorable perceptual quality. These findings highlight psychoacoustically guided audio perturbations as a practical and promising direction for privacy-preserving portrait protection.

</details>

#### [Puppeteer: Object-Grounded Posture-Aware Co-Speech Gesture Generation](https://arxiv.org/abs/2609.00369) · [📄 Read](papers/2026/2609.00369.md)

**Vida Adeli, Soroush Mehraban, Jacob Rommann, Harrison Sanborn et al.** · 2026-08-31

<details>
<summary>Abstract</summary>

Generating co-speech gestures that are temporally coherent, semantically aligned with speech, and grounded with surrounding objects remains challenging. Prior speech-driven gesture models emphasize audio-gesture alignment but do not explicitly account for posture constraints or surrounding objects, failing to capture the inherent correlation between body gestures and the physical space. We present Puppeteer, a posture-aware, object-grounded co-speech gesture diffusion model operating in a causal latent space. We decompose long gestures into structured primitives and learn a causal variational autoencoder that encodes them into temporally ordered latent tokens, each depending only on the past. We then perform conditional diffusion directly in the causal latent space, conditioning on speech signals, motion history, an initial posture reference, and object geometry to synthesize physically consistent gestures. This temporally ordered latent formulation enables explicit temporal control and supports tasks such as gesture in-betweening and gesture completion. To better assess co-speech gesture synthesis beyond existing measures, we introduce new evaluation metrics tailored to this task. We also created SceneGes, the first curated synthetic 3D dataset of embodied co-speech gestures and corresponding 3D objects, enabling object-grounded gesture generation. Experiments show that Puppeteer generates more diverse and temporally synchronized gestures than prior methods, while enabling object-grounded gesture synthesis.

</details>

#### [RoboGesture: Real-Time Semantic-aligned Co-Speech Gestures Generation for Humanoid Interaction](https://arxiv.org/abs/2608.28693) · [📄 Read](papers/2026/2608.28693.md)

**Zifan Wang, Ziang Ren, Pengyang Shi, Zirui Wang et al.** · 2026-08-27

<details>
<summary>Abstract</summary>

Enabling humanoid robots to respond to human speech with synchronized and semantically meaningful gestures is fundamental to natural human-robot interaction. However, this task faces three critical barriers: the scarcity of semantically rich datasets, the "modality eclipse" where models ignore audio cues in favor of kinematic inertia, and the sim-to-real gap regarding physical safety. We propose RoboGesture, a robot-centric framework that co-designs data, modeling, and control to power a complete interactive human-humanoid system in which the robot listens, responds, and gestures in real time. We first establish the RoboGesture dataset featuring over 300 gesture categories and develop an automated pipeline to synthesize large-scale collision-free, robot-specific audio-motion pairs. Our architecture features a Hierarchical Semantic-Acoustic Aligner that extracts multi-granular prosodic and semantic cues directly from raw audio tokens. These cues drive a Streaming Conditional Motion Generator based on a diffusion transformer with conditional flow matching. To ensure high responsiveness, we introduce Anti-Inertia CFG Masking, which prevents the model from collapsing into repetitive historical patterns by compelling it to proactively mine control signals from the audio modality. Finally, an MPC-based safety filter ensures real-time, collision-free execution on physical hardware. Experiments on a Unitree G1 humanoid demonstrate that RoboGesture generates safer, more rhythmic, and more semantically appropriate responses compared to state-of-the-art baselines.

</details>

#### [InteractGesture: Progressive Chunk Guidance for Continuous Streaming Co-Speech Gesture Control](https://arxiv.org/abs/2608.25734) · [📄 Read](papers/2026/2608.25734.md)

**Ekkasit Pinyoanuntapong, Ajinkya Deogade, Paul Streli, Wenjing Zhang et al.** · 2026-08-26

<details>
<summary>Abstract</summary>

Co-speech gesture generation has made significant progress toward realistic full-body motion from speaker audio, yet existing models lack fine-grained spatial controllability of individual joints. To address this, we introduce \emph{InteractGesture}, a model-agnostic, inference-time method for spatially controllable gesture generation. \emph{InteractGesture} guides target latent estimates of a diffusion sampler through a differentiable RVQ-VAE decoder, backpropagating spatial control gradients to adjust motion latents during sampling. A primary challenge in streaming co-speech generation is chunk-wise dependency: standard sequential inference freezes prior chunks, preventing spatial constraints in future chunks from adjusting preceding trajectories and causing boundary inconsistencies. To overcome this limitation, we propose \emph{Progressive Chunk Guidance}, a chunk-window strategy that maintains an active set of editable chunk latents with staggered delays, enabling spatial constraints to propagate gradients backward across chunk boundaries during streaming generation. Experiments on the BEAT2 dataset show that \emph{InteractGesture} improves multi-joint spatial control while preserving overall gesture quality. Furthermore, our approach supports diverse applications, including sparse joint positioning, dense joint trajectory control, and directional pointing. Our project page is available at https://exitudio.github.io/interactgesture-page .

</details>

#### [Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](https://arxiv.org/abs/2608.23383) · [📄 Read](papers/2026/2608.23383.md)

**Nan Duan, Haoyang Huang, Weiyang Jin, Haoran Li et al.** · 2026-08-24

<details>
<summary>Abstract</summary>

Video generation is progressing beyond isolated clips toward long-form narratives and interactive worlds, requiring models to preserve identities, follow user controls, and remain stable over extended rollouts. We present JoyAI-Echo-1.5, a unified audio-visual generation system with two purpose-built variants. The long-video variant introduces composable cross-shot memory that aggregates visual evidence across multiple prior shots and speaker cues derived from speech-filtered full-shot audio, enabling persistent character appearance and voice identity across flexible combinations of text, image, and memory conditioning. The world-model variant converts heterogeneous navigation inputs into calibrated metric 6-DoF camera trajectories and injects them through a geometry-aware conditioning pathway, enabling controller-agnostic interaction across flexible viewpoints. To support efficient long-horizon generation, we transform a bidirectional audio-visual backbone into a causal few-step generator using progressive teacher forcing and short- and long-horizon Self-Gradient Forcing on self-generated rollouts. Experiments demonstrate strong performance in both settings. JoyAI-Echo-1.5 achieves improvements over existing long-video baselines in cross-shot consistency, visual quality, text alignment, and speech fidelity. Its world-model variant ranks first on WBench, with an average score of 81.7, and achieves leading visual quality and long-horizon persistence on SANA-WM-Bench. Together, these results indicate that memory, geometric control, and rollout-aware training provide a practical foundation for generating coherent stories and continuously evolving interactive worlds. Project page: https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page/.

</details>

#### [The ISCSLP 2026 Real-World Audio-Visual Speech Enhancement Challenge](https://arxiv.org/abs/2608.23759) · [📄 Read](papers/2026/2608.23759.md)

**Challenge Organizers** · 2026-08-24

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement (AVSE) uses visual-speech cues from a target speaker to recover that speaker's speech from noisy or overlapping speech. Many widely used protocols construct mixed signals from separately recorded audio sources and assume reliable video, leaving their performance under natural overlap and visual failure insufficiently characterized. The Real-World AVSE Challenge evaluates two related settings. Track~1 comprises two scenarios: real-world mixtures recorded with two speakers speaking simultaneously, without a corresponding clean reference signal, and synthetic remixes obtained by manually mixing the separately recorded speech of two speakers, with a clean reference signal available; Track~2 reuses audio but pairs it with a degraded target video and contains additional 3-m far-field recordings. The speakers in the development and test sets are disjoint. Evaluation metrics include clean-waveform fidelity, learned quality estimates, transcription accuracy, and speaker identification. In the remix task on the development set, the baseline model achieved an SI-SDR of $-4.069$~dB and an STOI of $0.388$ on Track~1, and an SI-SDR of $-2.851$~dB and an STOI of $0.470$ on Track~2. We release the AV-ConvTasNet checkpoints, the offline evaluator, and the official baseline results on the development and test sets.

</details>

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

</details>
<!-- PAPERS_TABLE_END -->
