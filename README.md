# lipsync-papers

A curated, automatically-updated collection of papers on **lip sync**, talking-head synthesis, audio-driven face animation, and related topics — starting from [Wav2Lip](https://arxiv.org/abs/2008.10010) (2020) and growing every week.

## How it works

* Papers are sourced from [arXiv](https://arxiv.org/), [Semantic Scholar](https://www.semanticscholar.org/), and [Papers With Code](https://paperswithcode.com/) via their public APIs.
* A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs **daily at 06:00 UTC** to pull papers submitted in the previous 8 days.
* Results are filtered with a negative-keyword blacklist plus an ML signal check and a positive lipsync/talking-face relevance gate.
* The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Running locally

```bash
# Incremental fetch (last 8 days)
python scripts/fetch_papers.py

# Full historical fetch (everything since 2020-01-01)
python scripts/fetch_papers.py --full

# Custom window
python scripts/fetch_papers.py --days 30
```

No third-party dependencies are required — the script uses only the Python standard library.

## Triggering a manual update

Open the **Actions** tab → **Fetch Lipsync Papers** → **Run workflow**.  
Select *full = true* to back-fill from 2020, or leave it as *false* for an incremental update.

## Search terms

The following keyword queries are used against arXiv, Semantic Scholar, and Papers With Code title and abstract fields:

`lip sync` · `lip synchronization` · `wav2lip` · `talking head` · `talking face` · `audio-driven face` · `speech-driven face` · `audio visual speech` · `face reenactment` · `neural dubbing`

## Negative keywords

Papers whose title or abstract contain any of the following phrases (case-insensitive) are excluded:

`speech recognition` · `power synchronization` · `grid-forming` · `electric load` · `spacecraft` · `tractor engine` · `audio encryption` · `audio steganography` · `job-shop scheduling` · `mechanical system` · `warp-knitted` · `integrated sensing and communication` · `rate-splitting` · `reconfigurable intelligent surface` · `spread spectrum` · `spectrum access` · `radiation field reconstruction` · `wireless human gesture` · `programmable data-plane` · `indoor positioning` · `near-field positioning` · `human-drone` · `temporal knowledge graph` · `event localization` · `audio backdoor` · `forensic speaker` · `intrusion detection` · `nanostructure` · `quantum neural` · `pde solver` · `printed memristor` · `sonar` · `cleft lip` · `rhinoplasty` · `head and neck cancer` · `alveolar bone` · `lip balm` · `lip-ms` · `transcranial` · `alzheimer` · `polycystic ovary` · `diabetes mellitus` · `perinatal` · `dentofacial` · `stuttering` · `oral health` · `face-to-face stacking` · `talking therapies` · `talking therapy` · `autocratic leadership` · `cloud cost` · `professional wrestling` · `respondent-driven` · `partisan` · `macaque` · `ai companion chatbot` · `immersive analytics` · `audio description text` · `audio hallucination` · `audio language model` · `membership inference attack` · `binaural audio` · `spatial audio` · `sound field interpolation` · `audio transfer learning` · `audio pre-training` · `audio captioning` · `resting-state fmri` · `granger causality` · `speech neuroprosthesis` · `neural speech tracking` · `cochlear implant` · `mmwave radar` · `lidar-camera` · `network twin` · `machine translation` · `grammar error correction` · `named entity recognition` · `video quality assessment` · `scene dynamics compression` · `video object insertion` · `hand object interaction` · `road damage` · `music-driven dance` · `dietary action` · `active acoustic sensing` · `talking-heads attention` · `inter-layer communication` · `audio-visual scene classification` · `area threat identification` · `pedagogical agent` · `empathetic chatbot` · `multimodal biometric database` · `tiktok` · `street video` · `sign language detection` · `chinese sign language` · `sentiment analysis` · `video motion transfer` · `structured pruning u-net` · `scene2audio` · `image and layout editing` · `body pose estimation` · `android robot head` · `embodied conversational agent` · `text-audio steganography` · `joint steganography` · `reference audio-visual segmentation` · `multi-view stereo`

## Papers

<!-- PAPERS_TABLE_START -->
<details open>
<summary><h3>2026</h3></summary>

#### [Polyglot: Multilingual Style Preserving Speech-Driven Facial Animation](https://arxiv.org/abs/2604.16108)
**Federico Nocentini, Kwang-duck Seo, Qingju Liu, C. Ferrari et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Speech-Driven Facial Animation (SDFA) has gained significant attention due to its applications in movies, video games, and virtual reality. However, most existing models are trained on single-language data, limiting their effectiveness in real-world multilingual scenarios. In this work, we address multilingual SDFA, which is essential for realistic generation since language influences phonetics, rhythm, intonation, and facial expressions. Speaking style is also shaped by individual differences, not only by language. Existing methods typically rely on either language-specific or speaker-specific conditioning, but not both, limiting their ability to model their interaction. We introduce Polyglot, a unified diffusion-based architecture for personalized multilingual SDFA. Our method uses transcript embeddings to encode language information and style embeddings extracted from reference facial sequences to capture individual speaking characteristics. Polyglot does not require predefined language or speaker labels, enabling generalization across languages and speakers through self-supervised learning. By jointly conditioning on language and style, it captures expressive traits such as rhythm, articulation, and habitual facial movements, producing temporally coherent and realistic animations. Experiments show improved performance in both monolingual and multilingual settings, providing a unified framework for modeling language and personal style in SDFA.

</details>

#### [TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580)
**Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang et al.** · 2026-04-16

<details>
<summary>Abstract</summary>

Existing audio-driven video digital human generation models rely on multi-step denoising, resulting in substantial computational overhead that severely limits their deployment in real-world settings. While one-step distillation approaches can significantly accelerate inference, they often suffer from training instability. To address this challenge, we propose TurboTalk, a two-stage progressive distillation framework that effectively compresses a multi-step audio-driven video diffusion model into a single-step generator. We first adopt Distribution Matching Distillation to obtain a strong and stable 4-step student, and then progressively reduce the denoising steps from 4 to 1 through adversarial distillation. To ensure stable training under extreme step reduction, we introduce a progressive timestep sampling strategy and a self-compare adversarial objective that provides an intermediate adversarial reference that stabilizes progressive distillation. Our method achieve single-step generation of video talking avatar, boosting inference speed by 120 times while maintaining high generation quality.

</details>

#### [DiffMagicFace: Identity Consistent Facial Editing of Real Videos](https://arxiv.org/abs/2604.13841)
**Huanghao Yin, Shenkun Xu, Kanle Shi, Junhai Yong et al.** · 2026-04-15

<details>
<summary>Abstract</summary>

Text-conditioned image editing has greatly benefitted from the advancements in Image Diffusion Models. However, extending these techniques to facial video editing introduces challenges in preserving facial identity throughout the source video and ensuring consistency of the edited subject across frames. In this paper, we introduce DiffMagicFace, a unique video editing framework that integrates two fine-tuned models for text and image control. These models operate concurrently during inference to produce video frames that maintain identity features while seamlessly aligning with the editing semantics. To ensure the consistency of the edited videos, we develop a dataset comprising images showcasing various facial perspectives for each edited subject. The creation of a data set is achieved through rendering techniques and the subsequent application of optimization algorithms. Remarkably, our approach does not depend on video datasets but still delivers high-quality results in both consistency and content. The excellent effect holds even for complex tasks like talking head videos and distinguishing closely related categories. The videos edited using our framework exhibit parity with videos that are made using traditional rendering software. Through comparative analysis with current state-of-the-art methods, our framework demonstrates superior performance in both visual appeal and quantitative metrics.

</details>

#### [CoSyncDiT: Cognitive Synchronous Diffusion Transformer for Movie Dubbing](https://arxiv.org/abs/2604.12292)
**Gaoxiang Cong, Liang Li, Jiaxin Ye, Zhedong Zhang et al.** · 2026-04-14

<details>
<summary>Abstract</summary>

Movie dubbing aims to synthesize speech that preserves the vocal identity of a reference audio while synchronizing with the lip movements in a target video. Existing methods fail to achieve precise lip-sync and lack naturalness due to explicit alignment at the duration level. While implicit alignment solutions have emerged, they remain susceptible to interference from the reference audio, triggering timbre and pronunciation degradation in in-the-wild scenarios. In this paper, we propose a novel flow matching-based movie dubbing framework driven by the Cognitive Synchronous Diffusion Transformer (CoSync-DiT), inspired by the cognitive process of professional actors. This architecture progressively guides the noise-to-speech generative trajectory by executing acoustic style adapting, fine-grained visual calibrating, and time-aware context aligning. Furthermore, we design the Joint Semantic and Alignment Regularization (JSAR) mechanism to simultaneously constrain frame-level temporal consistency on the contextual outputs and semantic consistency on the flow hidden states, ensuring robust alignment. Extensive experiments on both standard benchmarks and challenging in-the-wild dubbing benchmarks demonstrate that our method achieves the state-of-the-art performance across multiple metrics.

</details>

#### [SEDTalker: Emotion-Aware 3D Facial Animation Using Frame-Level Speech Emotion Diarization](https://arxiv.org/abs/2604.13335)
**Farzaneh Jafari, Stefano Berretti, Anup Basu** · 2026-04-14

<details>
<summary>Abstract</summary>

We introduce SEDTalker, an emotion-aware framework for speech-driven 3D facial animation that leverages frame-level speech emotion diarization to achieve fine-grained expressive control. Unlike prior approaches that rely on utterance-level or manually specified emotion labels, our method predicts temporally dense emotion categories and intensities directly from speech, enabling continuous modulation of facial expressions over time. The diarized emotion signals are encoded as learned embeddings and used to condition a speech-driven 3D animation model based on a hybrid Transformer-Mamba architecture. This design allows effective disentanglement of linguistic content and emotional style while preserving identity and temporal coherence. We evaluate our approach on a large-scale multi-corpus dataset for speech emotion diarization and on the EmoVOCA dataset for emotional 3D facial animation. Quantitative results demonstrate strong frame-level emotion recognition performance and low geometric and temporal reconstruction errors, while qualitative results show smooth emotion transitions and consistent expression control. These findings highlight the effectiveness of frame-level emotion diarization for expressive and controllable 3D talking head generation.

</details>

#### [SyncBreaker:Stage-Aware Multimodal Adversarial Attacks on Audio-Driven Talking Head Generation](https://arxiv.org/abs/2604.08405)
**Wenli Zhang, Xianglong Shi, Sirui Zhao, Xinqi Chen et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

Diffusion-based audio-driven talking-head generation enables realistic portrait animation, but also introduces risks of misuse, such as fraud and misinformation. Existing protection methods are largely limited to a single modality, and neither image-only nor audio-only attacks can effectively suppress speech-driven facial dynamics. To address this gap, we propose SyncBreaker, a stage-aware multimodal protection framework that jointly perturbs portrait and audio inputs under modality-specific perceptual constraints. Our key contributions are twofold. First, for the image stream, we introduce nullifying supervision with Multi-Interval Sampling (MIS) across diffusion stages to steer the generation toward the static reference portrait by aggregating guidance from multiple denoising intervals. Second, for the audio stream, we propose Cross-Attention Fooling (CAF), which suppresses interval-specific audio-conditioned cross-attention responses. Both streams are optimized independently and combined at inference time to enable flexible deployment. We evaluate SyncBreaker in a white-box proactive protection setting. Extensive experiments demonstrate that SyncBreaker more effectively degrades lip synchronization and facial dynamics than strong single-modality baselines, while preserving input perceptual quality and remaining robust under purification. Code: https://github.com/kitty384/SyncBreaker.

</details>

#### [Cross-Modal Emotion Transfer for Emotion Editing in Talking Face Video](https://arxiv.org/abs/2604.07786)
**Chanhyuk Choi, Taesoo Kim, Donggyu Lee, Siyeol Jung et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

Talking face generation has gained significant attention as a core application of generative models. To enhance the expressiveness and realism of synthesized videos, emotion editing in talking face video plays a crucial role. However, existing approaches often limit expressive flexibility and struggle to generate extended emotions. Label-based methods represent emotions with discrete categories, which fail to capture a wide range of emotions. Audio-based methods can leverage emotionally rich speech signals - and even benefit from expressive text-to-speech (TTS) synthesis - but they fail to express the target emotions because emotions and linguistic contents are entangled in emotional speeches. Images-based methods, on the other hand, rely on target reference images to guide emotion transfer, yet they require high-quality frontal views and face challenges in acquiring reference data for extended emotions (e.g., sarcasm). To address these limitations, we propose Cross-Modal Emotion Transfer (C-MET), a novel approach that generates facial expressions based on speeches by modeling emotion semantic vectors between speech and visual feature spaces. C-MET leverages a large-scale pretrained audio encoder and a disentangled facial expression encoder to learn emotion semantic vectors that represent the difference between two different emotional embeddings across modalities. Extensive experiments on the MEAD and CREMA-D datasets demonstrate that our method improves emotion accuracy by 14% over state-of-the-art methods, while generating expressive talking face videos - even for unseen extended emotions. Code, checkpoint, and demo are available at https://chanhyeok-choi.github.io/C-MET/

</details>

#### [Multimodal AI in education: an avatar-based intelligent learning system for the Kazakh language](https://www.semanticscholar.org/paper/cc4c9cc6f66ac5f4ecfff5028a0cd8e4761c9d6d)
**Aru Ukenova, G. Bekmanova, B. Yergesh, Sadok Ben Yahia et al.** · 2026-04-08

<details>
<summary>Abstract</summary>

This article describes the development of a multimodal learning system for the Kazakh language intended for digital educational environments. The study focuses on the lack of avatar-based learning systems adapted to the linguistic properties of the Kazakh language and the limited integration of verbal and non-verbal components in existing solutions. The proposed system combines syntactic and morphological text analysis with sentiment processing and intonation control. Speech synthesis, gesture generation, facial expression control, and lip synchronization are implemented within a single system architecture. Prosodic parameters are formed based on sentence structure and sentence-level emotional indicators, while visual articulation is synchronized with audio output. The system was tested in speech synthesis scenarios relevant to interactive educational use. The results show that the system can be used for automated lecture narration, voice-over of instructional materials, and basic learner interaction in avatar-based educational settings.

</details>

#### [MMTalker: Multiresolution 3D Talking Head Synthesis with Multimodal Feature Fusion](https://arxiv.org/abs/2604.02941)
**Bin Liu, Zhixiang Xiong, Zhifen He, Bo Li** · 2026-04-03

<details>
<summary>Abstract</summary>

Speech-driven three-dimensional (3D) facial animation synthesis aims to build a mapping from one-dimensional (1D) speech signals to time-varying 3D facial motion signals. Current methods still face challenges in maintaining lip-sync accuracy and producing realistic facial expressions, primarily due to the highly ill-posed nature of this cross-modal mapping. In this paper, we introduce a novel 3D audio-driven facial animation synthesis method through multi-resolution representation and multi-modal feature fusion, called MMTalker which can accurately reconstruct the rich details of 3D facial motion. We first achieve the continuous representation of 3D face with details by mesh parameterization and non-uniform differentiable sampling. The mesh parameterization technique establishes the correspondence between UV plane and 3D facial mesh and is used to offer ground truth for the continuous learning. Differentiable non-uniform sampling enables precise facial detail acquisition by setting learnable sampling probability in each triangular face. Next, we employ residual graph convolutional network and dual cross-attention mechanism to extract discriminative facial motion feature from multiple input modalities. This proposed multimodal fusion strategy takes full use of the hierarchical features of speech and the explicit spatiotemporal geometric features of facial mesh. Finally, a lightweight regression network predicts the vertex-wise geometric displacements of the synthesized talking face by jointly processing the sampled points in the canonical UV space and the encoded facial motion features. Comprehensive experiments demonstrate that significant improvements are achieved over state-of-the-art methods, especially in the synchronization accuracy of lip and eye movements.

</details>

#### [Precise Speech-driven Talking-Face Synthesis with Realistic Speaker-Emulated Facil Expressions](https://www.semanticscholar.org/paper/98adc42cb44096970eea8474b43ffd8087df0f6b)
**Jhing-Fa Wang, Din-Yuen Chan, Shu-Yan Liou, Hsin-Chun Tsai** · 2026-04-03

<details>
<summary>Abstract</summary>

Traditional facial animation models do not particularly stress on the naturalness of imitating the dynamic facial expressions including eye movements, dynamic eyebrow deformation and head motion naturalness. Hence, in this paper, a speech-driven talking-face synthesizer (SDTS) is proposed for generating the dynamic talking video of given static face for semantically mimicking the speech of any real person. The SDTS can lead the static digital-twin face to vividly mimic the expressive motions of face and lip-synced mouth of various speakers with the personalized accent with high distinctiveness. The SDTS framework has two stages. In first stage, one branch termed the dynamic fused-features generation module (DFGM) contains cross-modal speech-facial fusion module (CSFF) and temporal convolutional network (TCN). The CSFF is the core to seamlessly align the speech features and facial features. The second branch is the self-designed adaptive identity extractor (AIE) where a series of the residual blocks using partial batch normalization unit (PBN-ResNet blocks) and the residual blocks with the squeeze-and-excitation unit (SE-ResNet blocks) are cascaded to precisely capture the key features of face in a static reference image. In the second stage of SDTS, the diffusion model termed diffusion-based rendering model (DIRM) is applied to generate the high-resolution video reconstruction with the consistencies of appearance and emotion via fusing the driving speech features and the referred facial features. The extensive experiments demonstrate that SDTS can significantly promote the lip-synchronization, enrich the upper facial expression, and exhibit the naturalness of the head movements. Moreover, the SDTS can steadily maintain the facial identity consistency and the facial expression coherence for varying speaking speeds and emotions. Hence, it can attain less than 5.26 FID, 0.72 LSE-D and 0.56 LME than the StyleTalk model which is a well-known talking-face synthesis model.

</details>

#### [SAVe: Self-Supervised Audio-visual Deepfake Detection Exploiting Visual Artifacts and Audio-visual Misalignment](https://arxiv.org/abs/2603.25140)
**Sahibzada Adil Shahzad, Ammarah Hashmi, Junichi Yamagishi, Yusuke Yasuda et al.** · 2026-03-26

<details>
<summary>Abstract</summary>

Multimodal deepfakes can exhibit subtle visual artifacts and cross-modal inconsistencies, which remain challenging to detect, especially when detectors are trained primarily on curated synthetic forgeries. Such synthetic dependence can introduce dataset and generator bias, limiting scalability and robustness to unseen manipulations. We propose SAVe, a self-supervised audio-visual deepfake detection framework that learns entirely on authentic videos. SAVe generates on-the-fly, identity-preserving, region-aware self-blended pseudo-manipulations to emulate tampering artifacts, enabling the model to learn complementary visual cues across multiple facial granularities. To capture cross-modal evidence, SAVe also models lip-speech synchronization via an audio-visual alignment component that detects temporal misalignment patterns characteristic of audio-visual forgeries. Experiments on FakeAVCeleb and AV-LipSync-TIMIT demonstrate competitive in-domain performance and strong cross-dataset generalization, highlighting self-supervised learning as a scalable paradigm for multimodal deepfake detection.

</details>

#### [InterDyad: Interactive Dyadic Speech-to-Video Generation by Querying Intermediate Visual Guidance](https://arxiv.org/abs/2603.23132)
**Dongwei Pan, Longwei Guo, Jiazhi Guan, Luying Huang et al.** · 2026-03-24

<details>
<summary>Abstract</summary>

Despite progress in speech-to-video synthesis, existing methods often struggle to capture cross-individual dependencies and provide fine-grained control over reactive behaviors in dyadic settings. To address these challenges, we propose InterDyad, a framework that enables naturalistic interactive dynamics synthesis via querying structural motion guidance. Specifically, we first design an Interactivity Injector that achieves video reenactment based on identity-agnostic motion priors extracted from reference videos. Building upon this, we introduce a MetaQuery-based modality alignment mechanism to bridge the gap between conversational audio and these motion priors. By leveraging a Multimodal Large Language Model (MLLM), our framework is able to distill linguistic intent from audio to dictate the precise timing and appropriateness of reactions. To further improve lip-sync quality under extreme head poses, we propose Role-aware Dyadic Gaussian Guidance (RoDG) for enhanced lip-synchronization and spatial consistency. Finally, we introduce a dedicated evaluation suite with novelly designed metrics to quantify dyadic interaction. Comprehensive experiments demonstrate that InterDyad significantly outperforms state-of-the-art methods in producing natural and contextually grounded two-person interactions. Please refer to our project page for demo videos: https://interdyad.github.io/.

</details>

#### [EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332)
**Haolan Xu, Keli Cheng, Lei Wang, Ning Bi et al.** · 2026-03-22

<details>
<summary>Abstract</summary>

Audio-driven 3D talking head synthesis has advanced rapidly with Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). By leveraging rich pre-trained priors, few-shot methods enable instant personalization from just a few seconds of video. However, under expressive facial motion, existing few-shot approaches often suffer from geometric instability and audio-emotion mismatch, highlighting the need for more effective emotion-aware motion modeling. In this work, we present EmoTaG, a few-shot emotion-aware 3D talking head synthesis framework built on the Pretrain-and-Adapt paradigm. Our key insight is to reformulate motion prediction in a structured FLAME parameter space rather than directly deforming 3D Gaussians, thereby introducing explicit geometric priors that improve motion stability. Building upon this, we propose a Gated Residual Motion Network (GRMN), which captures emotional prosody from audio while supplementing head pose and upper-face cues absent from audio, enabling expressive and coherent motion generation. Extensive experiments demonstrate that EmoTaG achieves state-of-the-art performance in emotional expressiveness, lip synchronization, visual realism, and motion stability.

</details>

#### [Real-Time Multi Model Synchronization of TTS, Lip Sync, and Caption Generation using Deep Learning](https://www.semanticscholar.org/paper/fed7460b81f31dc2f11a904110a7283afd760241)
**Abhay Gupta, Aditi Kesarwani, Ashish Kumar Mishra, Shubha Mishra** · 2026-03-20

<details>
<summary>Abstract</summary>

Abstract: Real-time multimodal communication systems require seamless synchronization between speech generation, lip movements, and textual captions to create natural, accessible, and interactive digital experiences. This work proposes a unified deep-learning–based framework for real-time multimodal synchronization of Text-to-Speech (TTS), lipsync animation, and caption generation. The system integrates a streaming neural TTS model, an audio/text-driven lipsync module, and a low-latency caption generator built on streaming ASR. A central synchronization engine aligns phoneme timestamps, viseme transitions, and caption token timings using adaptive buffering and drift-correction strategies. This ensures that all three modalities—audio, visual articulation, and text output—remain synchronized within perceptually acceptable thresholds (<40 ms). The proposed pipeline improves temporal coherence, reduces caption lag, and enhances user experience in applications such as virtual presenters, digital avatars, assistive technologies, and human–AI communication. Experimental evaluation demonstrates significant improvements in alignment accuracy and latency over baseline independent systems. The framework sets a scalable foundation for future advancements in expressive avatars, multilingual communication, and low-resource real-time deployment. Keywords: Real-time synchronization, Text-to-Speech (TTS), Lipsync, Caption generation, Multimodal deep learning, Phoneme–viseme alignment, Streaming ASR, Neural vocoder, Human–computer interaction, Virtual avatar systems.

</details>

#### [EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307)
**Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du et al.** · 2026-03-19

<details>
<summary>Abstract</summary>

Audio-driven talking head generation aims to create vivid and realistic videos from a static portrait and speech. Existing AR-based methods rely on intermediate facial representations, which limit their expressiveness and realism. Meanwhile, diffusion-based methods generate clip-by-clip, lacking fine-grained control and causing inherent latency due to overall denoising across the window. To address these limitations, we propose EARTalking, a novel end-to-end, GPT-style autoregressive model for interactive audio-driven talking head generation. Our method introduces a novel frame-by-frame, in-context, audio-driven streaming generation paradigm. For inherently supporting variable-length video generation with identity consistency, we propose the Sink Frame Window Attention (SFA) mechanism. Furthermore, to avoid the complex, separate networks that prior works required for diverse control signals, we propose a streaming Frame Condition In-Context (FCIC) scheme. This scheme efficiently injects diverse control signals in a streaming, in-context manner, enabling interactive control at every frame and at arbitrary moments. Experiments demonstrate that EARTalking outperforms existing autoregressive methods and achieves performance comparable to diffusion-based methods. Our work demonstrates the feasibility of in-context streaming autoregressive control, unlocking a scalable direction for flexible, efficient generation. The code will be released for reproducibility.

</details>

#### [AvatarForcing: One-Step Streaming Talking Avatars via Local-Future Sliding-Window Denoising](https://arxiv.org/abs/2603.14331)
**Liyuan Cui, Wentao Hu, Wenyuan Zhang, Zesong Yang et al.** · 2026-03-15

<details>
<summary>Abstract</summary>

Real-time talking avatar generation requires low latency and minute-level temporal stability. Autoregressive (AR) forcing enables streaming inference but suffers from exposure bias, which causes errors to accumulate and become irreversible over long rollouts. In contrast, full-sequence diffusion transformers mitigate drift but remain computationally prohibitive for real-time long-form synthesis. We present AvatarForcing, a one-step streaming diffusion framework that denoises a fixed local-future window with heterogeneous noise levels and emits one clean block per step under constant per-step cost. To stabilize unbounded streams, the method introduces dual-anchor temporal forcing: a style anchor that re-indexes RoPE to maintain a fixed relative position with respect to the active window and applies anchor-audio zero-padding, and a temporal anchor that reuses recently emitted clean blocks to ensure smooth transitions. Real-time one-step inference is enabled by two-stage streaming distillation with offline ODE backfill and distribution matching. Experiments on standard benchmarks and a new 400-video long-form benchmark show strong visual quality and lip synchronization at 34 ms/frame using a 1.3B-parameter student model for realtime streaming. Our page is available at: https://cuiliyuan121.github.io/AvatarForcing/

</details>

#### [DiFlowDubber: Discrete Flow Matching for Automated Video Dubbing via Cross-Modal Alignment and Synchronization](https://arxiv.org/abs/2603.14267)
**Ngoc-Son Nguyen, Thanh V. T. Tran, Jeongsoo Choi, Hieu-Nghia Huynh-Nguyen et al.** · 2026-03-15

<details>
<summary>Abstract</summary>

Video dubbing has broad applications in filmmaking, multimedia creation, and assistive speech technology. Existing approaches either train directly on limited dubbing datasets or adopt a two-stage pipeline that adapts pre-trained text-to-speech (TTS) models, which often struggle to produce expressive prosody, rich acoustic characteristics, and precise synchronization. To address these issues, we propose DiFlowDubber with a novel two-stage training framework that effectively transfers knowledge from a pre-trained TTS model to video-driven dubbing, with a discrete flow matching generative backbone. Specifically, we design a FaPro module that captures global prosody and stylistic cues from facial expressions and leverages this information to guide the modeling of subsequent speech attributes. To ensure precise speech-lip synchronization, we introduce a Synchronizer module that bridges the modality gap among text, video, and speech, thereby improving cross-modal alignment and generating speech that is temporally synchronized with lip movements. Experiments on two primary benchmark datasets demonstrate that DiFlowDubber outperforms previous methods across multiple metrics.

</details>

#### [Emotion-Conditioned Motion Sub-spaces with Flow Matching for Real-Time Audio-Driven Talking Heads](https://www.semanticscholar.org/paper/ca037d58a95f1448e433fe8e8e21e003cfbd7fa8)
**Haoyu Wang, Xiaozhe Xin, Xiaoyu Qin, Meiguang Jin et al.** · 2026-03-14

<details>
<summary>Abstract</summary>

Recent advances in audio-driven talking-head synthesis have brought lip-sync precision close to human perception, yet emotional fidelity and real-time inference remain open challenges. Existing pipelines typically disentangle lip articulation, facial expression, and head pose in latent space; this rigid factorization ignores the intrinsic coupling between articulation and affect — e.g., downward lip corners when sad—thus limiting expressiveness. We cast speech-conditioned facial motion as a sample from an emotion-conditioned distribution in a motion latent space. Concretely, we (i) learn a motion dictionary of orthogonal bases with an autoencoder via self-supervision, (ii) construct emotion-conditioned sub-spaces within the latent space, and (iii) design a layer-progressive cross-attention fusion module that modulates a flow-matching sampler with both audio and emotion signals. Only ten reverse ODE steps are required to generate a motion-latent trajectory, enabling real-time end-to-end latency. Extensive experiments on MEAD and RAVDESS show that our method outperforms recent GAN- and diffusion-based baselines in emotion accuracy while running at around 75 FPS on a single desktop GPU. The proposed framework delivers the first emotionally expressive Audio2Face system that simultaneously achieves lip-sync accuracy, affective realism, and real-time performance.

</details>

#### [Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback](https://www.semanticscholar.org/paper/a69575793b10289587dc5a63e4779186c1466f81)
**Xingpei Ma, Shenneng Huang, Jiaran Cai, Yuansheng Guan et al.** · 2026-03-14

<details>
<summary>Abstract</summary>

Recent advances in diffusion models have significantly improved audio-driven human video generation, surpassing traditional methods in both quality and controllability. However, existing approaches still face challenges in lip-sync accuracy, temporal coherence for long video generation, and multi-character animation. In this work, we propose a diffusion transformer (DiT)-based framework for generating lifelike talking videos of arbitrary length, and introduce a training-free method for multi-character audio-driven animation. First, we employ a LoRA-based training strategy combined with a position shift inference approach, which enables efficient long video generation while preserving the capabilities of the foundation model. Moreover, we combine partial parameter updates with reward feedback to enhance both lip synchronization and natural body motion. Finally, we propose a training-free approach, Mask Classifier-Free Guidance (Mask-CFG), for multi-character animation, which requires no specialized datasets or model modifications and supports audio-driven animation for three or more characters. Experimental results demonstrate that our method outperforms existing state-of-the-art approaches, achieving high-quality, temporally coherent, and multi-character audio-driven video generation in a simple, efficient, and cost-effective manner.

</details>

#### [OmniEdit: A Training-free framework for Lip Synchronization and Audio-Visual Editing](https://arxiv.org/abs/2603.09084)
**Lixiang Lin, Siyuan Jin, Jinshan Zhang** · 2026-03-10

<details>
<summary>Abstract</summary>

Lip synchronization and audio-visual editing have emerged as fundamental challenges in multimodal learning, underpinning a wide range of applications, including film production, virtual avatars, and telepresence. Despite recent progress, most existing methods for lip synchronization and audio-visual editing depend on supervised fine-tuning of pre-trained models, leading to considerable computational overhead and data requirements. In this paper, we present OmniEdit, a training-free framework designed for both lip synchronization and audio-visual editing. Our approach reformulates the editing paradigm by substituting the edit sequence in FlowEdit with the target sequence, yielding an unbiased estimation of the desired output. Moreover, by removing stochastic elements from the generation process, we establish a smooth and stable editing trajectory. Extensive experimental results validate the effectiveness and robustness of the proposed framework. Code is available at https://github.com/l1346792580123/OmniEdit.

</details>

#### [EmbedTalk: Triplane-Free Talking Head Synthesis using Embedding-Driven Gaussian Deformation](https://arxiv.org/abs/2603.07604)
**Arpita Saggar, Jonathan C. Darling, Duygu Sarikaya, David C. Hogg** · 2026-03-08

<details>
<summary>Abstract</summary>

Real-time talking head synthesis increasingly relies on deformable 3D Gaussian Splatting (3DGS) due to its low latency. Tri-planes are the standard choice for encoding Gaussians prior to deformation, since they provide a continuous domain with explicit spatial relationships. However, tri-plane representations are limited by grid resolution and approximation errors introduced by projecting 3D volumetric fields onto 2D subspaces. Recent work has shown the superiority of learnt embeddings for driving temporal deformations in 4D scene reconstruction. We introduce $\textbf{EmbedTalk}$, which shows how such embeddings can be leveraged for modelling speech deformations in talking head synthesis. Through comprehensive experiments, we show that EmbedTalk outperforms existing 3DGS-based methods in rendering quality, lip synchronisation, and motion consistency, while remaining competitive with state-of-the-art generative models. Moreover, replacing the tri-plane encoding with learnt embeddings enables significantly more compact models that achieve over 60 FPS on a mobile GPU (RTX 2060 6 GB). Our code will be placed in the public domain on acceptance.

</details>

#### [TempoSyncDiff: Distilled Temporally-Consistent Diffusion for Low-Latency Audio-Driven Talking Head Generation](https://arxiv.org/abs/2603.06057)
**Soumya Mazumdar, Vineet Kumar Rakesh** · 2026-03-06

<details>
<summary>Abstract</summary>

Diffusion models have recently advanced photorealistic human synthesis, although practical talking-head generation (THG) remains constrained by high inference latency, temporal instability such as flicker and identity drift, and imperfect audio-visual alignment under challenging speech conditions. This paper introduces TempoSyncDiff, a reference-conditioned latent diffusion framework that explores few-step inference for efficient audio-driven talking-head generation. The approach adopts a teacher-student distillation formulation in which a diffusion teacher trained with a standard noise prediction objective guides a lightweight student denoiser capable of operating with significantly fewer inference steps to improve generation stability. The framework incorporates identity anchoring and temporal regularization designed to mitigate identity drift and frame-to-frame flicker during synthesis, while viseme-based audio conditioning provides coarse lip motion control. Experiments on the LRS3 dataset report denoising-stage component-level metrics relative to VAE reconstructions and preliminary latency characterization, including CPU-only and edge computing measurements and feasibility estimates for edge deployment. The results suggest that distilled diffusion models can retain much of the reconstruction behaviour of a stronger teacher while enabling substantially lower latency inference. The study is positioned as an initial step toward practical diffusion-based talking-head generation under constrained computational settings. GitHub: https://mazumdarsoumya.github.io/TempoSyncDiff

</details>

#### [FlowPortrait: Reinforcement Learning for Audio-Driven Portrait Video Generation](https://arxiv.org/abs/2603.00159)
**Weiting Tan, Andy T. Liu, Ming Tu, Xinghua Qu et al.** · 2026-02-25

<details>
<summary>Abstract</summary>

Generating realistic talking-head videos remains challenging due to persistent issues such as imperfect lip synchronization, unnatural motion, and evaluation metrics that correlate poorly with human perception. We propose FlowPortrait, a reinforcement-learning framework for audio-driven portrait animation built on a multimodal backbone for autoregressive audio-to-video generation. FlowPortrait introduces a human-aligned evaluation system based on Multimodal Large Language Models (MLLMs) to assess lip-sync accuracy, expressiveness, and motion quality. These signals are combined with perceptual and temporal consistency regularizers to form a stable composite reward, which is used to post-train the generator via Group Relative Policy Optimization (GRPO). Extensive experiments, including both automatic evaluations and human preference studies, demonstrate that FlowPortrait consistently produces higher-quality talking-head videos, highlighting the effectiveness of reinforcement learning for portrait animation.

</details>

#### [EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](https://arxiv.org/abs/2602.13669)
**Rang Meng, Weipeng Wu, Yingjie Yin, Yuming Li et al.** · 2026-02-14

<details>
<summary>Abstract</summary>

Recent multi-modal video generation models have achieved high visual quality, but their prohibitive latency and limited temporal stability hinder real-time deployment. Streaming inference exacerbates these issues, leading to pronounced multimodal degradation, such as spatial blurring, temporal drift, and lip desynchronization, which creates an unresolved efficiency-performance trade-off. To this end, we propose EchoTorrent, a novel schema with a fourfold design: (1) Multi-Teacher Training fine-tunes a pre-trained model on distinct preference domains to obtain specialized domain experts, which sequentially transfer domain-specific knowledge to a student model; (2) Adaptive CFG Calibration (ACC-DMD), which calibrates the audio CFG augmentation errors in DMD via a phased spatiotemporal schedule, eliminating redundant CFG computations and enabling single-pass inference per step; (3) Hybrid Long Tail Forcing, which enforces alignment exclusively on tail frames during long-horizon self-rollout training via a causal-bidirectional hybrid architecture, effectively mitigates spatiotemporal degradation in streaming mode while enhancing fidelity to reference frames; and (4) VAE Decoder Refiner through pixel-domain optimization of the VAE decoder to recover high-frequency details while circumventing latent-space ambiguities. Extensive experiments and analysis demonstrate that EchoTorrent achieves few-pass autoregressive generation with substantially extended temporal consistency, identity preservation, and audio-lip synchronization.

</details>

#### [3DXTalker: Unifying Identity, Lip Sync, Emotion, and Spatial Dynamics in Expressive 3D Talking Avatars](https://arxiv.org/abs/2602.10516)
**Zhongju Wang, Zhenhong Sun, Beier Wang, Yifu Wang et al.** · 2026-02-11

<details>
<summary>Abstract</summary>

Audio-driven 3D talking avatar generation is increasingly important in virtual communication, digital humans, and interactive media, where avatars must preserve identity, synchronize lip motion with speech, express emotion, and exhibit lifelike spatial dynamics, collectively defining a broader objective of expressivity. However, achieving this remains challenging due to insufficient training data with limited subject identities, narrow audio representations, and restricted explicit controllability. In this paper, we propose 3DXTalker, an expressive 3D talking avatar through data-curated identity modeling, audio-rich representations, and spatial dynamics controllability. 3DXTalker enables scalable identity modeling via 2D-to-3D data curation pipeline and disentangled representations, alleviating data scarcity and improving identity generalization. Then, we introduce frame-wise amplitude and emotional cues beyond standard speech embeddings, ensuring superior lip synchronization and nuanced expression modulation. These cues are unified by a flow-matching-based transformer for coherent facial dynamics. Moreover, 3DXTalker also enables natural head-pose motion generation while supporting stylized control via prompt-based conditioning. Extensive experiments show that 3DXTalker integrates lip synchronization, emotional expression, and head-pose dynamics within a unified framework, achieves superior performance in 3D talking avatar generation.

</details>

#### [AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534)
**Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang et al.** · 2026-02-10

<details>
<summary>Abstract</summary>

Realistic talking-head video generation is critical for virtual avatars, film production, and interactive systems. Current methods struggle with nuanced emotional expressions due to the lack of fine-grained emotion control. To address this issue, we introduce a novel two-stage method (AUHead) to disentangle fine-grained emotion control, i.e. , Action Units (AUs), from audio and achieve controllable generation. In the first stage, we explore the AU generation abilities of large audio-language models (ALMs), by spatial-temporal AU tokenization and an "emotion-then-AU" chain-of-thought mechanism. It aims to disentangle AUs from raw speech, effectively capturing subtle emotional cues. In the second stage, we propose an AU-driven controllable diffusion model that synthesizes realistic talking-head videos conditioned on AU sequences. Specifically, we first map the AU sequences into the structured 2D facial representation to enhance spatial fidelity, and then model the AU-vision interaction within cross-attention modules. To achieve flexible AU-quality trade-off control, we introduce an AU disentanglement guidance strategy during inference, further refining the emotional expressiveness and identity consistency of the generated videos. Results on benchmark datasets demonstrate that our approach achieves competitive performance in emotional realism, accurate lip synchronization, and visual coherence, significantly surpassing existing techniques. Our implementation is available at https://github.com/laura990501/AUHead_ICLR

</details>

#### [MOVA: Towards Scalable and Synchronized Video-Audio Generation](https://arxiv.org/abs/2602.08794)
**SII-OpenMOSS Team, :, Donghua Yu, Mingshu Chen et al.** · 2026-02-09

<details>
<summary>Abstract</summary>

Audio is indispensable for real-world video, yet generation models have largely overlooked audio components. Current approaches to producing audio-visual content often rely on cascaded pipelines, which increase cost, accumulate errors, and degrade overall quality. While systems such as Veo 3 and Sora 2 emphasize the value of simultaneous generation, joint multimodal modeling introduces unique challenges in architecture, data, and training. Moreover, the closed-source nature of existing systems limits progress in the field. In this work, we introduce MOVA (MOSS Video and Audio), an open-source model capable of generating high-quality, synchronized audio-visual content, including realistic lip-synced speech, environment-aware sound effects, and content-aligned music. MOVA employs a Mixture-of-Experts (MoE) architecture, with a total of 32B parameters, of which 18B are active during inference. It supports IT2VA (Image-Text to Video-Audio) generation task. By releasing the model weights and code, we aim to advance research and foster a vibrant community of creators. The released codebase features comprehensive support for efficient inference, LoRA fine-tuning, and prompt enhancement.

</details>

#### [From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122)
**Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro et al.** · 2026-02-05

<details>
<summary>Abstract</summary>

Creating high-fidelity, animatable 3D talking heads is crucial for immersive applications, yet often hindered by the prevalence of low-quality image or video sources, which yield poor 3D reconstructions. In this paper, we introduce SuperHead, a novel framework for enhancing low-resolution, animatable 3D head avatars. The core challenge lies in synthesizing high-quality geometry and textures, while ensuring both 3D and temporal consistency during animation and preserving subject identity. Despite recent progress in image, video and 3D-based super-resolution (SR), existing SR techniques are ill-equipped to handle dynamic 3D inputs. To address this, SuperHead leverages the rich priors from pre-trained 3D generative models via a novel dynamics-aware 3D inversion scheme. This process optimizes the latent representation of the generative model to produce a super-resolved 3D Gaussian Splatting (3DGS) head model, which is subsequently rigged to an underlying parametric head model (e.g., FLAME) for animation. The inversion is jointly supervised using a sparse collection of upscaled 2D face renderings and corresponding depth maps, captured from diverse facial expressions and camera viewpoints, to ensure realism under dynamic facial motions. Experiments demonstrate that SuperHead generates avatars with fine-grained facial details under dynamic motions, significantly outperforming baseline methods in visual quality.

</details>

#### [A$^2$-LLM: An End-to-end Conversational Audio Avatar Large Language Model](https://arxiv.org/abs/2602.04913)
**Xiaolin Hu, Hang Yuan, Xinzhu Sang, Binbin Yan et al.** · 2026-02-04

<details>
<summary>Abstract</summary>

Developing expressive and responsive conversational digital humans is a cornerstone of next-generation human-computer interaction. While large language models (LLMs) have significantly enhanced dialogue capabilities, most current systems still rely on cascaded architectures that connect independent modules. These pipelines are often plagued by accumulated errors, high latency, and poor real-time performance. Lacking access to the underlying conversational context, these pipelines inherently prioritize rigid lip-sync over emotional depth. To address these challenges, we propose A$^2$-LLM, an end-to-end conversational audio avatar large language model that jointly reasons about language, audio prosody, and 3D facial motion within a unified framework. To facilitate training, we introduce FLAME-QA, a high-quality multimodal dataset designed to align semantic intent with expressive facial dynamics within a QA format. By leveraging deep semantic understanding, A$^2$-LLM generates emotionally rich facial movements beyond simple lip-synchronization. Experimental results demonstrate that our system achieves superior emotional expressiveness while maintaining real-time efficiency (500 ms latency, 0.7 RTF).

</details>

#### [MIRRORTALK: Forging Personalized Avatars Via Disentangled Style and Hierarchical Motion Control](https://arxiv.org/abs/2601.22501)
**Renjie Lu, Xulong Zhang, Xiaoyang Qu, Jianzong Wang et al.** · 2026-01-30

<details>
<summary>Abstract</summary>

Synthesizing personalized talking faces that uphold and highlight a speaker's unique style while maintaining lip-sync accuracy remains a significant challenge. A primary limitation of existing approaches is the intrinsic confounding of speaker-specific talking style and semantic content within facial motions, which prevents the faithful transfer of a speaker's unique persona to arbitrary speech. In this paper, we propose MirrorTalk, a generative framework based on a conditional diffusion model, combined with a Semantically-Disentangled Style Encoder (SDSE) that can distill pure style representations from a brief reference video. To effectively utilize this representation, we further introduce a hierarchical modulation strategy within the diffusion process. This mechanism guides the synthesis by dynamically balancing the contributions of audio and style features across distinct facial regions, ensuring both precise lip-sync accuracy and expressive full-face dynamics. Extensive experiments demonstrate that MirrorTalk achieves significant improvements over state-of-the-art methods in terms of lip-sync accuracy and personalization preservation.

</details>

#### [JUST-DUB-IT: Video Dubbing via Joint Audio-Visual Diffusion](https://arxiv.org/abs/2601.22143)
**Anthony Chen, Naomi Ken Korem, Tavi Halperin, Matan Ben Yosef et al.** · 2026-01-29

<details>
<summary>Abstract</summary>

Audio-Visual Foundation Models, which are pretrained to jointly generate sound and visual content, have recently shown an unprecedented ability to model multi-modal generation and editing, opening new opportunities for downstream tasks. Among these tasks, video dubbing could greatly benefit from such priors, yet most existing solutions still rely on complex, task-specific pipelines that struggle in real-world settings. In this work, we introduce a single-model approach that adapts a foundational audio-video diffusion model for video-to-video dubbing via a lightweight LoRA. The LoRA enables the model to condition on an input audio-video while jointly generating translated audio and synchronized facial motion. To train this LoRA, we leverage the generative model itself to synthesize paired multilingual videos of the same speaker. Specifically, we generate multilingual videos with language switches within a single clip, and then inpaint the face and audio in each half to match the language of the other half. By leveraging the rich generative prior of the audio-visual model, our approach preserves speaker identity and lip synchronization while remaining robust to complex motion and real-world dynamics. We demonstrate that our approach produces high-quality dubbed videos with improved visual fidelity, lip synchronization, and robustness compared to existing dubbing pipelines.

</details>

#### [EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers](https://arxiv.org/abs/2601.22127)
**John Flynn, Wolfgang Paier, Dimitar Dinev, Sam Nhut Nguyen et al.** · 2026-01-29

<details>
<summary>Abstract</summary>

Current generative video models excel at producing novel content from text and image prompts, but leave a critical gap in editing existing pre-recorded videos, where minor alterations to the spoken script require preserving motion, temporal coherence, speaker identity, and accurate lip synchronization. We introduce EditYourself, a DiT-based framework for audio-driven video-to-video (V2V) editing that enables transcript-based modification of talking head videos, including the seamless addition, removal, and retiming of visually spoken content. Building on a general-purpose video diffusion model, EditYourself augments its V2V capabilities with audio conditioning and region-aware, edit-focused training extensions. This enables precise lip synchronization and temporally coherent restructuring of existing performances via spatiotemporal inpainting, including the synthesis of realistic human motion in newly added segments, while maintaining visual fidelity and identity consistency over long durations. This work represents a foundational step toward generative video models as practical tools for professional video post-production.

</details>

#### [Lightweight High-Fidelity Low-Bitrate Talking Face Compression for 3D Video Conference](https://arxiv.org/abs/2601.21269)
**Jianglong Li, Jun Xu, Bingcong Lu, Zhengxue Cheng et al.** · 2026-01-29

<details>
<summary>Abstract</summary>

The demand for immersive and interactive communication has driven advancements in 3D video conferencing, yet achieving high-fidelity 3D talking face representation at low bitrates remains a challenge. Traditional 2D video compression techniques fail to preserve fine-grained geometric and appearance details, while implicit neural rendering methods like NeRF suffer from prohibitive computational costs. To address these challenges, we propose a lightweight, high-fidelity, low-bitrate 3D talking face compression framework that integrates FLAME-based parametric modeling with 3DGS neural rendering. Our approach transmits only essential facial metadata in real time, enabling efficient reconstruction with a Gaussian-based head model. Additionally, we introduce a compact representation and compression scheme, including Gaussian attribute compression and MLP optimization, to enhance transmission efficiency. Experimental results demonstrate that our method achieves superior rate-distortion performance, delivering high-quality facial rendering at extremely low bitrates, making it well-suited for real-time 3D video conferencing applications.

</details>

#### [Audio-Driven Talking Face Generation with Blink Embedding and Hash Grid Landmarks Encoding](https://arxiv.org/abs/2601.18849)
**Yuhui Zhang, Hui Yu, Wei Liang, Sunjie Zhang** · 2026-01-26

<details>
<summary>Abstract</summary>

Dynamic Neural Radiance Fields (NeRF) have demonstrated considerable success in generating high-fidelity 3D models of talking portraits. Despite significant advancements in the rendering speed and generation quality, challenges persist in accurately and efficiently capturing mouth movements in talking portraits. To tackle this challenge, we propose an automatic method based on blink embedding and hash grid landmarks encoding in this study, which can substantially enhance the fidelity of talking faces. Specifically, we leverage facial features encoded as conditional features and integrate audio features as residual terms into our model through a Dynamic Landmark Transformer. Furthermore, we employ neural radiance fields to model the entire face, resulting in a lifelike face representation. Experimental evaluations have validated the superiority of our approach to existing methods.

</details>

#### [FunCineForge: A Unified Dataset Toolkit and Model for Zero-Shot Movie Dubbing in Diverse Cinematic Scenes](https://arxiv.org/abs/2601.14777)
**Jiaxuan Liu, Yang Xiang, Han Zhao, Xiangang Li et al.** · 2026-01-21

<details>
<summary>Abstract</summary>

Movie dubbing is the task of synthesizing speech from scripts conditioned on video scenes, requiring accurate lip sync, faithful timbre transfer, and proper modeling of character identity and emotion. However, existing methods face two major limitations: (1) high-quality multimodal dubbing datasets are limited in scale, suffer from high word error rates, contain sparse annotations, rely on costly manual labeling, and are restricted to monologue scenes, all of which hinder effective model training; (2) existing dubbing models rely solely on the lip region to learn audio-visual alignment, which limits their applicability to complex live-action cinematic scenes, and exhibit suboptimal performance in lip sync, speech quality, and emotional expressiveness. To address these issues, we propose FunCineForge, which comprises an end-to-end production pipeline for large-scale dubbing datasets and an MLLM-based dubbing model designed for diverse cinematic scenes. Using the pipeline, we construct the first Chinese television dubbing dataset with rich annotations, and demonstrate the high quality of these data. Experiments across monologue, narration, dialogue, and multi-speaker scenes show that our dubbing model consistently outperforms SOTA methods in audio quality, lip sync, timbre transfer, and instruction following. Code and demos are available at https://anonymous.4open.science/w/FunCineForge.

</details>

#### [Audio-driven single image talking face animation with transformers](https://www.semanticscholar.org/paper/8728bdcb4f6492c5cd9541df88d1b79ad351ded8)
**Yixin Li, Xizhong Shen** · 2026-01-19

<details>
<summary>Abstract</summary>

Audio-driven talking-head video generation is a critical task in cross-modal expressive synthesis, with applications in virtual humans, digital content creation, and human-computer interaction. Existing methods, however, often suffer from unnatural lip movements and distortions in non-speech facial regions, especially under exaggerated expressions or emotional variations. These issues arise due to the entanglement of linguistic content, prosodic emotion, and speaker-specific attributes within the audio signal. To address these challenges, we propose ExpNet, a Transformer-based expression regression framework that decouples global head motion from local facial expressions using 3DMM coefficients. The method employs a conditional VAE for robust head pose coefficient generation, while a CNN-Transformer architecture regresses expression coefficients. ExpNet introduces ALiBi-based relative positional bias in the self-attention mechanism, which captures long-range dependencies while focusing on local temporal context. It also conditions on the first-frame expression coefficient to preserve identity and emotion consistency throughout the video. Experimental evaluations on multiple datasets, including HDTF, MEAD, and LRS3, demonstrate that the method presented in this paper outperforms existing methods in terms of expression realism, lip synchronization, and video quality. Ablation studies reveal that key components such as ALiBi, landmark supervision, and the Transformer module are crucial for improving temporal stability, reducing lip jitter, and enhancing overall facial animation consistency.

</details>

#### [Now You See Me, Now You Don't: A Unified Framework for Expression Consistent Anonymization in Talking Head Videos](https://arxiv.org/abs/2601.11635)
**Anil Egin, Andrea Tangherloni, Antitza Dantcheva** · 2026-01-14

<details>
<summary>Abstract</summary>

Face video anonymization is aimed at privacy preservation while allowing for the analysis of videos in a number of computer vision downstream tasks such as expression recognition, people tracking, and action recognition. We propose here a novel unified framework referred to as Anon-NET, streamlined to de-identify facial videos, while preserving age, gender, race, pose, and expression of the original video. Specifically, we inpaint faces by a diffusion-based generative model guided by high-level attribute recognition and motion-aware expression transfer. We then animate deidentified faces by video-driven animation, which accepts the de-identified face and the original video as input. Extensive experiments on the datasets VoxCeleb2, CelebV-HQ, and HDTF, which include diverse facial dynamics, demonstrate the effectiveness of AnonNET in obfuscating identity while retaining visual realism and temporal consistency. The code of AnonNet will be publicly released.

</details>

#### [MANGO:Natural Multi-speaker 3D Talking Head Generation via 2D-Lifted Enhancement](https://arxiv.org/abs/2601.01749)
**Lei Zhu, Lijian Lin, Ye Zhu, Jiahao Wu et al.** · 2026-01-05

<details>
<summary>Abstract</summary>

Current audio-driven 3D head generation methods mainly focus on single-speaker scenarios, lacking natural, bidirectional listen-and-speak interaction. Achieving seamless conversational behavior, where speaking and listening states transition fluidly remains a key challenge. Existing 3D conversational avatar approaches rely on error-prone pseudo-3D labels that fail to capture fine-grained facial dynamics. To address these limitations, we introduce a novel two-stage framework MANGO, which leveraging pure image-level supervision by alternately training to mitigate the noise introduced by pseudo-3D labels, thereby achieving better alignment with real-world conversational behaviors. Specifically, in the first stage, a diffusion-based transformer with a dual-audio interaction module models natural 3D motion from multi-speaker audio. In the second stage, we use a fast 3D Gaussian Renderer to generate high-fidelity images and provide 2D-level photometric supervision for the 3D motions through alternate training. Additionally, we introduce MANGO-Dialog, a high-quality dataset with over 50 hours of aligned 2D-3D conversational data across 500+ identities. Extensive experiments demonstrate that our method achieves exceptional accuracy and realism in modeling two-person 3D dialogue motion, significantly advancing the fidelity and controllability of audio-driven talking heads.

</details>

#### [MM-Sonate: Multimodal Controllable Audio-Video Generation with Zero-Shot Voice Cloning](https://arxiv.org/abs/2601.01568)
**Chunyu Qiang, Jun Wang, Xiaopeng Wang, Kang Yin et al.** · 2026-01-04

<details>
<summary>Abstract</summary>

Joint audio-video generation aims to synthesize synchronized multisensory content, yet current unified models struggle with fine-grained acoustic control, particularly for identity-preserving speech. Existing approaches either suffer from temporal misalignment due to cascaded generation or lack the capability to perform zero-shot voice cloning within a joint synthesis framework. In this work, we present MM-Sonate, a multimodal flow-matching framework that unifies controllable audio-video joint generation with zero-shot voice cloning capabilities. Unlike prior works that rely on coarse semantic descriptions, MM-Sonate utilizes a unified instruction-phoneme input to enforce strict linguistic and temporal alignment. To enable zero-shot voice cloning, we introduce a timbre injection mechanism that effectively decouples speaker identity from linguistic content. Furthermore, addressing the limitations of standard classifier-free guidance in multimodal settings, we propose a noise-based negative conditioning strategy that utilizes natural noise priors to significantly enhance acoustic fidelity. Empirical evaluations demonstrate that MM-Sonate establishes new state-of-the-art performance in joint generation benchmarks, significantly outperforming baselines in lip synchronization and speech intelligibility, while achieving voice cloning fidelity comparable to specialized Text-to-Speech systems.

</details>

#### [Emotionally Controllable Audio-driven Talking Face Generation](https://www.semanticscholar.org/paper/599c27a3333605649161d905c21060d190becf2d)
**Yifan Xu, Sirui Zhao, Shifeng Liu, Tong Xu et al.** · 2026-01-03

<details>
<summary>Abstract</summary>

Talking face generation is a technique that synthesizes realistic, speech-synchronized facial animations from static images driven by audio or textual input. In recent years, notable advancements have been achieved in the generation of realistic lip-synchronized talking face videos. Although these methods have demonstrated highly realistic results in lip-sync generation, they rarely focus on the expression of emotions, which is essential for achieving emotionally rich and lifelike talking face videos. In this article, we propose a novel emotionally controllable audio-driven talking face generation framework, termed ECATFG. Specifically, the proposed ECATFG mainly consists of three modules: template video generator, landmark generator, and rendering module. Firstly, we integrate a customized motion transfer module into StyleGAN to generate template videos that encapsulate the target emotions and head movements. Subsequently, a Mamba-based landmark generator is proposed to accurately model the correlation between input audio and facial landmarks. Afterwards, in the rendering module, we employ a framework that combines both AdaIN and SPADE layers to transform audio-predicted landmarks into highly realistic images, guided by reference images and facial contour landmarks. Finally, comprehensive experiments validate the effectiveness of ECATFG, demonstrating its capability to generate high-quality talking face videos that not only achieve exceptional lip-synchronization accuracy but also effectively convey a wide range of emotions.

</details>

#### [Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation](https://arxiv.org/abs/2601.00664)
**Taekyung Ki, Sangwon Jang, Jaehyeong Jo, Jaehong Yoon et al.** · 2026-01-02

<details>
<summary>Abstract</summary>

Talking head generation creates lifelike avatars from static portraits for virtual communication and content creation. However, current models do not yet convey the feeling of truly interactive communication, often generating one-way responses that lack emotional engagement. We identify two key challenges toward truly interactive avatars: generating motion in real-time under causal constraints and learning expressive, vibrant reactions without additional labeled data. To address these challenges, we propose Avatar Forcing, a new framework for interactive head avatar generation that models real-time user-avatar interactions through diffusion forcing. This design allows the avatar to process real-time multimodal inputs, including the user's audio and motion, with low latency for instant reactions to both verbal and non-verbal cues such as speech, nods, and laughter. Furthermore, we introduce a direct preference optimization method that leverages synthetic losing samples constructed by dropping user conditions, enabling label-free learning of expressive interaction. Experimental results demonstrate that our framework enables real-time interaction with low latency (approximately 500ms), achieving 6.8X speedup compared to the baseline, and produces reactive and expressive avatar motion, which is preferred over 80% against the baseline.

</details>

#### [EMTA: End-to-End Multi-Task Audio-Driven Talking-Head Animation](https://www.semanticscholar.org/paper/1c5597407caf0c273264e4ba1283cb9722cb3c54)
**L. Venkatesan, Divya Choudhary, Sai G, Subhajeet Lahiri et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

: Audio-Driven facial animation has advanced rapidly, yet most methods remain task-specific (e.g., reenactment, dubbing) and domain-locked (2D or 3D). This fragmentation limits flexibility across applications like telep-resence and AR/VR. We introduce EMTA , an end-to-end, identity-preserving framework that unifies multiple audio-driven tasks within a unified architecture. EMTA decouples audio-to-geometry from geometry-to-appearance generation: (1) Audio2Mesh predicts expressive, temporally coherent 3D facial landmarks from audio and employs a novel rotation decoder module, directly usable for 3D avatars; and (2) LaPix-GAN synthesizes photorealistic 2D frames through an identity-aware generator, a novel Audio-Gated Spatial Attention (AGSA) module, and enhanced Facial-Inpainted Landmark (FIL) sketches. EMTA achieves robust and competitive results across 3D mesh prediction, 2D reenactment, talking portraits, and dubbing tasks against baselines on multiple datasets, validating it as a flexible and practical solution (25 FPS).

</details>

#### [High-fidelity and Lip-synced Talking Face Synthesis via Landmark-based Diffusion Model](https://www.semanticscholar.org/paper/d3e3159653a29ff817335f8db6da5ef03409a191)
**Wei‐Tao Zhong, Junfan Lin, Peixin Chen, Feng Gao et al.** · 2026-01-01


#### [Enhanced Audio-Visual Speech Synthesis via Multi-Discriminative Learning](https://www.semanticscholar.org/paper/aad984cc65c272b2610d4f852fe05062a71bfa30)
**Subhayu Ghosh, Frank Zalkow, N. D. Jana** · 2026-01-01

<details>
<summary>Abstract</summary>

Audio-visual speech synthesis (AVSS) aims to produce an audio-visual stream that conveys a target speaker’s speech. In this study, the AVSS system takes the input speech of a source speaker and generates the audio-visual stream of the target speaker while preserving the linguistic content of the source speech. The process involves two main components: voice conversion (VC), which adapts the vocal features from the source to the target speaker, and audio-visual synthesis (AVS), which generates the synchronized audio-visual stream from the transformed speech. This paper presents a novel generative framework based on multi-discriminative learning to enhance the realism and quality of AVSS outputs. The proposed approach integrates multiple discriminators, including capsule networks, co-occurrence neural networks, and vision transformers (ViTs), within the VC model to leverage their unique strengths in capturing diverse speech features. Additionally, the AVS model incorporates a co-occurrence neural network to improve video quality and achieve better temporal alignment between audio and visual data. Experimental evaluations on standard benchmarks demonstrate that the proposed method achieves significant improvements in both audio and video quality, offering a substantial advancement in AVSS technology.

</details>

#### [Viseme-Gated Multilayer Cross-Attentional Feature Fusion for Cognitively-Inspired Multimodal Speech Enhancement](https://www.semanticscholar.org/paper/c2772c139c0efc437de2fe000580c6d0a0519a2b)
**Nasir Saleem, Adeel Hussain, K. Dashtipour, Eamon Sheikh et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

Human speech perception naturally integrates visual and auditory cues, with lip movements providing critical disambiguation in noisy environments where audio signals are degraded (SNR $\leq$ −5 dB). While existing audio-visual speech enhancement (AVSE) models use this multimodal synergy, they often fail to exploit phoneme-specific viseme correlations. We propose VG-MCA-AVSENet, a cognitively inspired architecture that introduces a viseme-gated multilayer cross-attention mechanism within a convolutional encoder-decoder framework. The model dynamically weights visual features using auditory context and learned viseme importance (prioritizing lip closures for plosives), while maintaining efficiency through depthwise separable convolutions and MobileNetV3-based visual encoding. Our AVSE system comprises an audio encoder, visual encoder with temporal modeling, separation module with 3-layer viseme-aware attention, and neural vocoder decoder. Evaluated on GRID-CHiME, NTCD-TIMIT, and LRS3 datasets, the model achieves 72.58% STOI (+12.28% over baseline), 2.56 PESQ, and 7.80 dB SI-SDR in extreme noise conditions (SNR$\leq$ -6 dB). The viseme gating specifically improves plosive intelligibility by 7% with a few additional parameters, showing that explicit phoneme-viseme modeling significantly outperforms conventional approaches.

</details>

#### [Audiovisual speech enhancement and voice activity detection using generative and regressive visual features](https://www.semanticscholar.org/paper/39f39c0552dada9cc7cef73426ef4adde6a9a344)
**Cheng Yu, Vahid Ahmadi Kalkhorani, Buye Xu, DeLiang Wang** · 2026-01-01


</details>

<details open>
<summary><h3>2025</h3></summary>

#### [From Inpainting to Editing: A Self-Bootstrapping Framework for Context-Rich Visual Dubbing](https://arxiv.org/abs/2512.25066)
**Xu He, Haoxian Zhang, Hejia Chen, Changyuan Zheng et al.** · 2025-12-31

<details>
<summary>Abstract</summary>

Audio-driven visual dubbing aims to synchronize a video's lip movements with new speech, but is fundamentally challenged by the lack of ideal training data: paired videos where only a subject's lip movements differ while all other visual conditions are identical. Existing methods circumvent this with a mask-based inpainting paradigm, where an incomplete visual conditioning forces models to simultaneously hallucinate missing content and sync lips, leading to visual artifacts, identity drift, and poor synchronization. In this work, we propose a novel self-bootstrapping framework that reframes visual dubbing from an ill-posed inpainting task into a well-conditioned video-to-video editing problem. Our approach employs a Diffusion Transformer, first as a data generator, to synthesize ideal training data: a lip-altered companion video for each real sample, forming visually aligned video pairs. A DiT-based audio-driven editor is then trained on these pairs end-to-end, leveraging the complete and aligned input video frames to focus solely on precise, audio-driven lip modifications. This complete, frame-aligned input conditioning forms a rich visual context for the editor, providing it with complete identity cues, scene interactions, and continuous spatiotemporal dynamics. Leveraging this rich context fundamentally enables our method to achieve highly accurate lip sync, faithful identity preservation, and exceptional robustness against challenging in-the-wild scenarios. We further introduce a timestep-adaptive multi-phase learning strategy as a necessary component to disentangle conflicting editing objectives across diffusion timesteps, thereby facilitating stable training and yielding enhanced lip synchronization and visual fidelity. Additionally, we propose ContextDubBench, a comprehensive benchmark dataset for robust evaluation in diverse and challenging practical application scenarios.

</details>

#### [DyStream: Streaming Dyadic Talking Heads Generation via Flow Matching-based Autoregressive Model](https://arxiv.org/abs/2512.24408)
**Bohong Chen, Haiyang Liu** · 2025-12-30

<details>
<summary>Abstract</summary>

Generating realistic, dyadic talking head video requires ultra-low latency. Existing chunk-based methods require full non-causal context windows, introducing significant delays. This high latency critically prevents the immediate, non-verbal feedback required for a realistic listener. To address this, we present DyStream, a flow matching-based autoregressive model that could generate video in real-time from both speaker and listener audio. Our method contains two key designs: (1) we adopt a stream-friendly autoregressive framework with flow-matching heads for probabilistic modeling, and (2) We propose a causal encoder enhanced by a lookahead module to incorporate short future context (e.g., 60 ms) to improve quality while maintaining low latency. Our analysis shows this simple-and-effective method significantly surpass alternative causal strategies, including distillation and generative encoder. Extensive experiments show that DyStream could generate video within 34 ms per frame, guaranteeing the entire system latency remains under 100 ms. Besides, it achieves state-of-the-art lip-sync quality, with offline and online LipSync Confidence scores of 8.13 and 7.61 on HDTF, respectively. The model, weights and codes are available.

</details>

#### [Accelerating LatentSync Lip-Synchronization via OmniQuant-Inspired Post-Training Quantization](https://www.semanticscholar.org/paper/b2a9ada0ddddf56534fc4d6822f442ea1d93edea)
**Guolin Wang** · 2025-12-26

<details>
<summary>Abstract</summary>

Lip-synchronization models play an important role in audio-driven facial animation and virtual human applications. LatentSync is a representative latent-based lip synchronization model that achieves high-quality temporal alignment between audio and visual modalities. However, the inference process of LatentSync relies on deep neural network components with considerable computational cost, which limits its deployment in real-time and resource-constrained scenarios. In this paper, we investigate an OmniQuant-inspired posttraining quantization (PTQ) strategy to accelerate the inference of the LatentSync lip-synchronization model. By applying INT8 weight-only quantization to the core generative backbone, the proposed method significantly reduces model size and inference latency without requiring retraining. The proposed approach follows the calibration principles of OmniQuant, including adaptive weight clipping and equivalent transformation, to mitigate quantization-induced performance degradation. Experimental results show that the proposed approach achieves noticeable inference acceleration and model compression, with no obvious functional degradation observed during empirical evaluation. These results demonstrate that OmniQuant-inspired post-training quantization provides a practical and efficient solution for accelerating lip-synchronization models in real-world applications.

</details>

#### [SyncAnyone: Implicit Disentanglement via Progressive Self-Correction for Lip-Syncing in the wild](https://arxiv.org/abs/2512.21736)
**Xindi Zhang, Dechao Meng, Steven Xiao, Qi Wang et al.** · 2025-12-25

<details>
<summary>Abstract</summary>

High-quality AI-powered video dubbing demands precise audio-lip synchronization, high-fidelity visual generation, and faithful preservation of identity and background. Most existing methods rely on a mask-based training strategy, where the mouth region is masked in talking-head videos, and the model learns to synthesize lip movements from corrupted inputs and target audios. While this facilitates lip-sync accuracy, it disrupts spatiotemporal context, impairing performance on dynamic facial motions and causing instability in facial structure and background consistency. To overcome this limitation, we propose SyncAnyone, a novel two-stage learning framework that achieves accurate motion modeling and high visual fidelity simultaneously. In Stage 1, we train a diffusion-based video transformer for masked mouth inpainting, leveraging its strong spatiotemporal modeling to generate accurate, audio-driven lip movements. However, due to input corruption, minor artifacts may arise in the surrounding facial regions and the background. In Stage 2, we develop a mask-free tuning pipeline to address mask-induced artifacts. Specifically, on the basis of the Stage 1 model, we develop a data generation pipeline that creates pseudo-paired training samples by synthesizing lip-synced videos from the source video and random sampled audio. We further tune the stage 2 model on this synthetic data, achieving precise lip editing and better background consistency. Extensive experiments show that our method achieves state-of-the-art results in visual quality, temporal coherence, and identity preservation under in-the wild lip-syncing scenarios.

</details>

#### [TAVID: Text-Driven Audio-Visual Interactive Dialogue Generation](https://arxiv.org/abs/2512.20296)
**Ji-Hoon Kim, Junseok Ahn, Doyeop Kwak, Joon Son Chung et al.** · 2025-12-23

<details>
<summary>Abstract</summary>

The objective of this paper is to jointly synthesize interactive videos and conversational speech from text and reference images. With the ultimate goal of building human-like conversational systems, recent studies have explored talking or listening head generation as well as conversational speech generation. However, these works are typically studied in isolation, overlooking the multimodal nature of human conversation, which involves tightly coupled audio-visual interactions. In this paper, we introduce TAVID, a unified framework that generates both interactive faces and conversational speech in a synchronized manner. TAVID integrates face and speech generation pipelines through two cross-modal mappers (i.e., a motion mapper and a speaker mapper), which enable bidirectional exchange of complementary information between the audio and visual modalities. We evaluate our system across four dimensions: talking face realism, listening head responsiveness, dyadic interaction fluency, and speech quality. Extensive experiments demonstrate the effectiveness of our approach across all these aspects.

</details>

#### [In-Context Audio Control of Video Diffusion Transformers](https://arxiv.org/abs/2512.18772)
**Wenze Liu, Weicai Ye, Minghong Cai, Quande Liu et al.** · 2025-12-21

<details>
<summary>Abstract</summary>

Recent advancements in video generation have seen a shift towards unified, transformer-based foundation models that can handle multiple conditional inputs in-context. However, these models have primarily focused on modalities like text, images, and depth maps, while strictly time-synchronous signals like audio have been underexplored. This paper introduces In-Context Audio Control of video diffusion transformers (ICAC), a framework that investigates the integration of audio signals for speech-driven video generation within a unified full-attention architecture, akin to FullDiT. We systematically explore three distinct mechanisms for injecting audio conditions: standard cross-attention, 2D self-attention, and unified 3D self-attention. Our findings reveal that while 3D attention offers the highest potential for capturing spatio-temporal audio-visual correlations, it presents significant training challenges. To overcome this, we propose a Masked 3D Attention mechanism that constrains the attention pattern to enforce temporal alignment, enabling stable training and superior performance. Our experiments demonstrate that this approach achieves strong lip synchronization and video quality, conditioned on an audio stream and reference images.

</details>

#### [Asynchronous Pipeline Parallelism for Real-Time Multilingual Lip Synchronization in Video Communication Systems](https://arxiv.org/abs/2512.18318)
**Eren Caglar, Amirkia Rafiei Oskooei, Mehmet Kutanoglu, Mustafa Keles et al.** · 2025-12-20

<details>
<summary>Abstract</summary>

This paper introduces a parallel and asynchronous Transformer framework designed for efficient and accurate multilingual lip synchronization in real-time video conferencing systems. The proposed architecture integrates translation, speech processing, and lip-synchronization modules within a pipeline-parallel design that enables concurrent module execution through message-queue-based decoupling, reducing end-to-end latency by up to 3.1 times compared to sequential approaches. To enhance computational efficiency and throughput, the inference workflow of each module is optimized through low-level graph compilation, mixed-precision quantization, and hardware-accelerated kernel fusion. These optimizations provide substantial gains in efficiency while preserving model accuracy and visual quality. In addition, a context-adaptive silence-detection component segments the input speech stream at semantically coherent boundaries, improving translation consistency and temporal alignment across languages. Experimental results demonstrate that the proposed parallel architecture outperforms conventional sequential pipelines in processing speed, synchronization stability, and resource utilization. The modular, message-oriented design makes this work applicable to resource-constrained IoT communication scenarios including telemedicine, multilingual kiosks, and remote assistance systems. Overall, this work advances the development of low-latency, resource-efficient multimodal communication frameworks for next-generation AIoT systems.

</details>

#### [3D Face Animation Generation Method Based on Self-Supervised Speech Coding and Lattice Convolutional Architecture](https://www.semanticscholar.org/paper/40f7cbd9952048787b5ae47712473017f2927ff5)
**Yunying Wang** · 2025-12-20

<details>
<summary>Abstract</summary>

Existing 3D face animation generation methods focus on lip movement and audio synchronization, ignoring the ability to synchronize expressions and poses. To address this problem, the study proposes a Self-Supervised Speech-Driven 3D Face Animation via Lattice Convolution Networks. The study first selected students from a certain school to read aloud the same corpus and record audio and video as the dataset. Through self-supervised learning and encoder-decoder structure, the speech features were extracted and mapped, and the obtained facial parameters were applied to the Face Latent Animated Mesh Estimator model to achieve lip-sync. Then, by combining the optical flow information in the video stream with the changes of facial key points, the grid convolutional network is used to model the expression dynamics and head postures, achieving multimodal feature fusion. In the experiment of analyzing the naturalness and accuracy of the generated animation, the lip shape vertex error, naturalness score, lip reading character error rate, and pixel error rate of the proposed method were only 2.54mm ², 9.45, 2.34%, and 2.53% respectively. In the performance analysis experiment of the emotion and posture recognition model, the accuracy rate of expression recognition and the posture offset error were 92.34% and 1.2° respectively. The lighting sensitivity, micro-expression fidelity and rendering frame rate of the generated face animation were 5.01, 93.48% and 63.74FPS respectively. The proposed 3D face animation generation method can effectively improve the realism and synchronization of the animation and achieve more accurate face animation generation.

</details>

#### [InstructDubber: Instruction-based Alignment for Zero-shot Movie Dubbing](https://arxiv.org/abs/2512.17154)
**Zhedong Zhang, Liang Li, Gaoxiang Cong, Chunshan Liu et al.** · 2025-12-19

<details>
<summary>Abstract</summary>

Movie dubbing seeks to synthesize speech from a given script using a specific voice, while ensuring accurate lip synchronization and emotion-prosody alignment with the character's visual performance. However, existing alignment approaches based on visual features face two key limitations: (1)they rely on complex, handcrafted visual preprocessing pipelines, including facial landmark detection and feature extraction; and (2) they generalize poorly to unseen visual domains, often resulting in degraded alignment and dubbing quality. To address these issues, we propose InstructDubber, a novel instruction-based alignment dubbing method for both robust in-domain and zero-shot movie dubbing. Specifically, we first feed the video, script, and corresponding prompts into a multimodal large language model to generate natural language dubbing instructions regarding the speaking rate and emotion state depicted in the video, which is robust to visual domain variations. Second, we design an instructed duration distilling module to mine discriminative duration cues from speaking rate instructions to predict lip-aligned phoneme-level pronunciation duration. Third, for emotion-prosody alignment, we devise an instructed emotion calibrating module, which finetunes an LLM-based instruction analyzer using ground truth dubbing emotion as supervision and predicts prosody based on the calibrated emotion analysis. Finally, the predicted duration and prosody, together with the script, are fed into the audio decoder to generate video-aligned dubbing. Extensive experiments on three major benchmarks demonstrate that InstructDubber outperforms state-of-the-art approaches across both in-domain and zero-shot scenarios.

</details>

#### [SynergyWarpNet: Attention-Guided Cooperative Warping for Neural Portrait Animation](https://arxiv.org/abs/2512.17331)
**Shihang Li, Zhiqiang Gong, Minming Ye, Yue Gao et al.** · 2025-12-19

<details>
<summary>Abstract</summary>

Recent advances in neural portrait animation have demonstrated remarked potential for applications in virtual avatars, telepresence, and digital content creation. However, traditional explicit warping approaches often struggle with accurate motion transfer or recovering missing regions, while recent attention-based warping methods, though effective, frequently suffer from high complexity and weak geometric grounding. To address these issues, we propose SynergyWarpNet, an attention-guided cooperative warping framework designed for high-fidelity talking head synthesis. Given a source portrait, a driving image, and a set of reference images, our model progressively refines the animation in three stages. First, an explicit warping module performs coarse spatial alignment between the source and driving image using 3D dense optical flow. Next, a reference-augmented correction module leverages cross-attention across 3D keypoints and texture features from multiple reference images to semantically complete occluded or distorted regions. Finally, a confidence-guided fusion module integrates the warped outputs with spatially-adaptive fusing, using a learned confidence map to balance structural alignment and visual consistency. Comprehensive evaluations on benchmark datasets demonstrate state-of-the-art performance.

</details>

#### [TalkPersonaDiff: High-Fidelity Speech-Driven 3D Facial Animation Generation via Unified Multimodal Synergistic Encoding and Dual-Style Modulation](https://www.semanticscholar.org/paper/05fd46beb0bf6e21f12896e708fa6ea24afea52c)
**Ouyang Peng, Zhuoyuan Yu, Tong Wu, Zhiqiang Zhang** · 2025-12-19

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation is critical for virtual humans, yet balancing Long-term Identity Consistency and Fine-grained Lip-sync in long sequences remains challenging. We propose TalkPersonaDiff, a conditional diffusion framework featuring a Unified Multimodal Synergistic Encoder to align speech semantics and identity priors in a latent space. Furthermore, to mitigate condition forgetting, we design a Dual-Style Modulation Mechanism that employs global injection and local re-weighting to maintain conditional efficacy throughout the denoising process. Experiments on BIWI and VOCASET demonstrate that TalkPersonaDiff outperforms mainstream methods in identity distinctiveness, lip-sync accuracy, and temporal smoothness, achieving high-fidelity, personalized 3D animation .

</details>

#### [FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling](https://arxiv.org/abs/2512.14056)
**Kim Sung-Bin, Joohyun Chang, David Harwath, Tae-Hyun Oh** · 2025-12-16

<details>
<summary>Abstract</summary>

Talking face editing and face generation have often been studied as distinct problems. In this work, we propose viewing both not as separate tasks but as subtasks of a unifying formulation, speech-conditional facial motion infilling. We explore facial motion infilling as a self-supervised pretext task that also serves as a unifying formulation of dynamic talking face synthesis. To instantiate this idea, we propose FacEDiT, a speech-conditional Diffusion Transformer trained with flow matching. Inspired by masked autoencoders, FacEDiT learns to synthesize masked facial motions conditioned on surrounding motions and speech. This formulation enables both localized generation and edits, such as substitution, insertion, and deletion, while ensuring seamless transitions with unedited regions. In addition, biased attention and temporal smoothness constraints enhance boundary continuity and lip synchronization. To address the lack of a standard editing benchmark, we introduce FacEDiTBench, the first dataset for talking face editing, featuring diverse edit types and lengths, along with new evaluation metrics. Extensive experiments validate that talking face editing and generation emerge as subtasks of speech-conditional motion infilling; FacEDiT produces accurate, speech-aligned facial edits with strong identity preservation and smooth visual continuity while generalizing effectively to talking face generation.

</details>

#### [JoVA: Unified Multimodal Learning for Joint Video-Audio Generation](https://arxiv.org/abs/2512.13677)
**Xiaohu Huang, Hao Zhou, Qiangpeng Yang, Shilei Wen et al.** · 2025-12-15

<details>
<summary>Abstract</summary>

In this paper, we present JoVA, a unified framework for joint video-audio generation. Despite recent encouraging advances, existing methods face two critical limitations. First, most existing approaches can only generate ambient sounds and lack the capability to produce human speech synchronized with lip movements. Second, recent attempts at unified human video-audio generation typically rely on explicit fusion or modality-specific alignment modules, which introduce additional architecture design and weaken the model simplicity of the original transformers. To address these issues, JoVA employs joint self-attention across video and audio tokens within each transformer layer, enabling direct and efficient cross-modal interaction without the need for additional alignment modules. Furthermore, to enable high-quality lip-speech synchronization, we introduce a simple yet effective mouth-area loss based on facial keypoint detection, which enhances supervision on the critical mouth region during training without compromising architectural simplicity. Extensive experiments on benchmarks demonstrate that JoVA outperforms or is competitive with both unified and audio-driven state-of-the-art methods in lip-sync accuracy, speech quality, and overall video-audio generation fidelity. Our results establish JoVA as an elegant framework for high-quality multimodal generation.

</details>

#### [Soul: Breathe Life into Digital Human for High-fidelity Long-term Multimodal Animation](https://arxiv.org/abs/2512.13495)
**Jiangning Zhang, Junwei Zhu, Zhenye Gan, Donghao Luo et al.** · 2025-12-15

<details>
<summary>Abstract</summary>

We propose a multimodal-driven framework for high-fidelity long-term digital human animation termed $\textbf{Soul}$, which generates semantically coherent videos from a single-frame portrait image, text prompts, and audio, achieving precise lip synchronization, vivid facial expressions, and robust identity preservation. We construct Soul-1M, containing 1 million finely annotated samples with a precise automated annotation pipeline (covering portrait, upper-body, full-body, and multi-person scenes) to mitigate data scarcity, and we carefully curate Soul-Bench for comprehensive and fair evaluation of audio-/text-guided animation methods. The model is built on the Wan2.2-5B backbone, integrating audio-injection layers and multiple training strategies together with threshold-aware codebook replacement to ensure long-term generation consistency. Meanwhile, step/CFG distillation and a lightweight VAE are used to optimize inference efficiency, achieving an 11.4$\times$ speedup with negligible quality loss. Extensive experiments show that Soul significantly outperforms current leading open-source and commercial models on video quality, video-text alignment, identity preservation, and lip-synchronization accuracy, demonstrating broad applicability in real-world scenarios such as virtual anchors and film production. Project page at https://zhangzjn.github.io/projects/Soul/

</details>

#### [KlingAvatar 2.0 Technical Report](https://arxiv.org/abs/2512.13313)
**Kling Team, Jialu Chen, Yikang Ding, Zhixue Fang et al.** · 2025-12-15

<details>
<summary>Abstract</summary>

Avatar video generation models have achieved remarkable progress in recent years. However, prior work exhibits limited efficiency in generating long-duration high-resolution videos, suffering from temporal drifting, quality degradation, and weak prompt following as video length increases. To address these challenges, we propose KlingAvatar 2.0, a spatio-temporal cascade framework that performs upscaling in both spatial resolution and temporal dimension. The framework first generates low-resolution blueprint video keyframes that capture global semantics and motion, and then refines them into high-resolution, temporally coherent sub-clips using a first-last frame strategy, while retaining smooth temporal transitions in long-form videos. To enhance cross-modal instruction fusion and alignment in extended videos, we introduce a Co-Reasoning Director composed of three modality-specific large language model (LLM) experts. These experts reason about modality priorities and infer underlying user intent, converting inputs into detailed storylines through multi-turn dialogue. A Negative Director further refines negative prompts to improve instruction alignment. Building on these components, we extend the framework to support ID-specific multi-character control. Extensive experiments demonstrate that our model effectively addresses the challenges of efficient, multimodally aligned long-form high-resolution video generation, delivering enhanced visual clarity, realistic lip-teeth rendering with accurate lip synchronization, strong identity preservation, and coherent multimodal instruction following.

</details>

#### [JoyAvatar-Flash: Real-time and Infinite Audio-Driven Avatar Generation with Autoregressive Diffusion](https://arxiv.org/abs/2512.11423)
**Chaochao Li, Ruikui Wang, Liangbo Zhou, Jinheng Feng et al.** · 2025-12-12

<details>
<summary>Abstract</summary>

Existing DiT-based audio-driven avatar generation methods have achieved considerable progress, yet their broader application is constrained by limitations such as high computational overhead and the inability to synthesize long-duration videos. Autoregressive methods address this problem by applying block-wise autoregressive diffusion methods. However, these methods suffer from the problem of error accumulation and quality degradation. To address this, we propose JoyAvatar-Flash, an audio-driven autoregressive model capable of real-time inference and infinite-length video generation with the following contributions: (1) Progressive Step Bootstrapping (PSB), which allocates more denoising steps to initial frames to stabilize generation and reduce error accumulation; (2) Motion Condition Injection (MCI), enhancing temporal coherence by injecting noise-corrupted previous frames as motion condition; and (3) Unbounded RoPE via Cache-Resetting (URCR), enabling infinite-length generation through dynamic positional encoding. Our 1.3B-parameter causal model achieves 16 FPS on a single GPU and achieves competitive results in visual quality, temporal consistency, and lip synchronization.

</details>

#### [REST: Diffusion-based Real-time End-to-end Streaming Talking Head Generation via ID-Context Caching and Asynchronous Streaming Distillation](https://arxiv.org/abs/2512.11229)
**Haotian Wang, Yuzhe Weng, Jun Du, Haoran Xu et al.** · 2025-12-12

<details>
<summary>Abstract</summary>

Diffusion models have significantly advanced the field of talking head generation (THG). However, slow inference speeds and prevalent non-autoregressive paradigms severely constrain the application of diffusion-based THG models. In this study, we propose REST, a pioneering diffusion-based, real-time, end-to-end streaming audio-driven talking head generation framework. To support real-time end-to-end generation, a compact video latent space is first learned through a spatiotemporal variational autoencoder with a high compression ratio. Additionally, to enable semi-autoregressive streaming within the compact video latent space, we introduce an ID-Context Cache mechanism, which integrates ID-Sink and Context-Cache principles into key-value caching for maintaining identity consistency and temporal coherence during long-term streaming generation. Furthermore, an Asynchronous Streaming Distillation (ASD) strategy is proposed to mitigate error accumulation and enhance temporal consistency in streaming generation, leveraging a non-streaming teacher with an asynchronous noise schedule to supervise the streaming student. REST bridges the gap between autoregressive and diffusion-based approaches, achieving a breakthrough in efficiency for applications requiring real-time THG. Experimental results demonstrate that REST outperforms state-of-the-art methods in both generation speed and overall performance.

</details>

#### [GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939)
**Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh** · 2025-12-11

<details>
<summary>Abstract</summary>

Speech-driven talking heads have recently emerged and enable interactive avatars. However, real-world applications are limited, as current methods achieve high visual fidelity but slow or fast yet temporally unstable. Diffusion methods provide realistic image generation, yet struggle with oneshot settings. Gaussian Splatting approaches are real-time, yet inaccuracies in facial tracking, or inconsistent Gaussian mappings, lead to unstable outputs and video artifacts that are detrimental to realistic use cases. We address this problem by mapping Gaussian Splatting using 3D Morphable Models to generate person-specific avatars. We introduce transformer-based prediction of model parameters, directly from audio, to drive temporal consistency. From monocular video and independent audio speech inputs, our method enables generation of real-time talking head videos where we report competitive quantitative and qualitative performance.

</details>

#### [FlowTalk: Real-Time Audio-Driven Talking Head Synthesis via Motion-Space Flow Matching](https://www.semanticscholar.org/paper/90b687acd9b3b1df39583c9cbf9a36e41fd13538)
**Kaijun Deng, Yuhang Guo, Linlin Shen** · 2025-12-08

<details>
<summary>Abstract</summary>

Audio-driven talking head synthesis has achieved significant progress, yet existing methods face critical trade-offs among generation quality, inference efficiency, and cross-ethnic generalization. Diffusion-based approaches produce high-fidelity results but suffer from slow inference due to iterative denoising, while GAN-based methods achieve faster speed at the cost of reduced motion naturalness and limited generalization. To address these challenges, we propose FlowTalk, a novel framework that enables real-time high-fidelity talking head video synthesis. Our approach leverages Flow Matching technology to perform efficient motion modeling in a decoupled motion space rather than pixel space, achieving significant speedup while maintaining generation quality. Specifically, we adopt an off-the-shelf motion extractor to disentangle facial appearance from motion, and employ an OT-based flow matching model with a transformer architecture to predict identity-agnostic motion sequences conditioned on audio features. To improve cross-ethnic generalization, we train on a balanced combination of DH-FaceVid-1K and HDTF datasets with HuBert-CN as the audio encoder. Experimental results demonstrate that FlowTalk achieves over 100 FPS in motion-space inference with 32 ODE solver steps, approximately 5 times faster than diffusion-based baselines with 500 steps, while preserving comparable visual quality in lip synchronization, facial expressions, and head movements. This efficiency, further enhanced through TensorRT deployment, enables truly real-time generation. Our framework provides an effective and practical solution for real-time talking head generation applications.

</details>

#### [Synchronization of Speech and Lip Motion with a Service Humanoid Robot](https://www.semanticscholar.org/paper/0982ab995632b833b80b34147e62c8a00824f7d0)
**Qiaowen Wu, Huan Peng, Songji Chen, Mingcong Wang et al.** · 2025-12-03

<details>
<summary>Abstract</summary>

With the increasing deployment of humanoid service robots in presentation and narration scenarios, there is a growing demand for more natural and effective interactive capabilities. To enhance the expressiveness and motion coordination of robot-delivered narration, this study presents a lip-synchronized presentation system. The proposed system ensures precise synchronization among speech output, lip movements, and slide progression, thereby enhancing the naturalness and coherence of the narration process. It consists of three primary modules: a speech processing module for speech synthesis and recognition, a slide control module for intent recognition and presentation management, and a lip-synchronization module that aligns lip motions with spoken content. Experimental results demonstrate that the system achieves high synchronization accuracy and operational stability. This work provides a solid technical foundation for integrating humanoid service robots into multimodal narration tasks.

</details>

#### [PhonemeNet: A Transformer Pipeline for Text-Driven Facial Animation](https://www.semanticscholar.org/paper/26a484edbab96233b524fd429d76807a23c3e116)
**Philine Witzig, Barbara Solenthaler, Markus Gross, Rafael Wampfler** · 2025-12-02

<details>
<summary>Abstract</summary>

We present a fully text-driven framework for 3D facial animation that eliminates the need for audio input or explicit prosodic cues. Our architecture extracts rich phoneme embeddings from text using a pre-trained TTS encoder, aligns them with quantized motion embeddings via a transformer decoder, and decodes the result into mesh deformations through a pre-trained transformer decoder. We explore two scenarios of our pipeline: (1) In the single-subject setting, we find that phoneme embeddings alone can yield accurate lip motion. (2) In a multi-subject setting, where speaker articulation varies widely, we introduce stochastic latent modulation to model residual variability conditioned on both phoneme context and speaker identity. We evaluate our approach quantitatively and qualitatively: We demonstrate accurate lip sync in the single-subject case, and compare against audio-driven baselines on a large multi-subject dataset. Our results show that PhonemeNet not only achieves competitive lip sync and motion quality, but also offers flexibility, modularity, and scalability as an alternative to audio-driven facial animation.

</details>

#### [Multilingual Speech-Driven Talking-Face Generation with Precise Lip Synchronization](https://www.semanticscholar.org/paper/e716de5959076556b3c54bc846fb61ee9a29204d)
**Che-Wen Chen, Jhing-Fa Wang, Din-Yuen Chan, James Chao et al.** · 2025-12-01

<details>
<summary>Abstract</summary>

We propose a modular pipeline that converts Chinese text into Taiwanese Hokkien speech and synthesizes a photorealistic talking-face video. The system couples a Taiwanese-aware TTS front end (hybrid word segmentation, iTaigi Tâi-lô romanization with dynamic tone annotation, tone-aware Tacotron2) with a Seed-VC–style timbre converter and a two-stage speech-driven talking-face synthesizer using cross-modal fusion, temporal modeling, and diffusion rendering. On an internal set, the speech reaches MOS 4.602 and CER 2.01%. On talking-face benchmarks, we obtain FID 29.18, CPBD 0.498, and LSE-D 7.23, surpassing representative baselines in realism, sharpness, and lip-sync. The design is lightweight and modular, runs on a single RTX 3080, and is transferable to other low-resource tonal languages.

</details>

#### [EmoDiffTalk:Emotion-aware Diffusion for Editable 3D Gaussian Talking Head](https://arxiv.org/abs/2512.05991)
**Chang Liu, Tianjiao Jing, Chengcheng Ma, Xuanqi Zhou et al.** · 2025-11-30

<details>
<summary>Abstract</summary>

Recent photo-realistic 3D talking head via 3D Gaussian Splatting still has significant shortcoming in emotional expression manipulation, especially for fine-grained and expansive dynamics emotional editing using multi-modal control. This paper introduces a new editable 3D Gaussian talking head, i.e. EmoDiffTalk. Our key idea is a novel Emotion-aware Gaussian Diffusion, which includes an action unit (AU) prompt Gaussian diffusion process for fine-grained facial animator, and moreover an accurate text-to-AU emotion controller to provide accurate and expansive dynamic emotional editing using text input. Experiments on public EmoTalk3D and RenderMe-360 datasets demonstrate superior emotional subtlety, lip-sync fidelity, and controllability of our EmoDiffTalk over previous works, establishing a principled pathway toward high-quality, diffusion-driven, multimodal editable 3D talking-head synthesis. To our best knowledge, our EmoDiffTalk is one of the first few 3D Gaussian Splatting talking-head generation framework, especially supporting continuous, multimodal emotional editing within the AU-based expression space.

</details>

#### [Open-Source Lip-Sync Models in the Period 2020--2025: A Structured Comparative Analysis](https://www.semanticscholar.org/paper/944e04e8799bbee4507ce55cfcadc179ba7064b5)
**Bilge Sağlam, Mustafa Keles, Mehmet Kutanoglu** · 2025-11-30

<details>
<summary>Abstract</summary>

Recent advancements in artificial intelligence have led to significant progress in the field of lip synchronization (lip-sync). This paper presents a systematic literature review focusing on popular open-source lip-sync models developed between 2020 and 2025, a period marked by the rapid evolution of deep generative models. Our aim was to examine and classify the prominent models of this era based on their architecture, performance, and technological approaches. To conduct our review, we searched the IEEE Xplore and Scopus databases. This study is based on three main methods most commonly used in the field: Generative Adversarial Networks (GANs), Transformers, and Diffusion Models. Each method was analyzed in detail using its popular representatives: Wav2Lip (GAN), GeneFace (Transformer/NeRF), and Diff2Lip (Diffusion). In this study, the training processes, architectural features, and performance metrics, such as video quality, synchronization accuracy, and computational cost, of these models were compared. Our findings indicate that diffusion models have recently gained prominence because they offer photorealistic outputs and stable training processes, although GAN-based models such as Wav2Lip are still widely used. This review serves as a comprehensive guide for researchers by summarizing the current state of the art in the field. Furthermore, it aims to contribute to new work by discussing the current challenges faced by lip-sync technologies and future research directions (e.g., real-time performance and multilingual support).

</details>

#### [AnyTalker: Scaling Multi-Person Talking Video Generation with Interactivity Refinement](https://arxiv.org/abs/2511.23475)
**Zhizhou Zhong, Yicheng Ji, Zhe Kong, Yiying Liu et al.** · 2025-11-28

<details>
<summary>Abstract</summary>

Recently, multi-person video generation has started to gain prominence. While a few preliminary works have explored audio-driven multi-person talking video generation, they often face challenges due to the high costs of diverse multi-person data collection and the difficulty of driving multiple identities with coherent interactivity. To address these challenges, we propose AnyTalker, a multi-person generation framework that features an extensible multi-stream processing architecture. Specifically, we extend Diffusion Transformer's attention block with a novel identity-aware attention mechanism that iteratively processes identity-audio pairs, allowing arbitrary scaling of drivable identities. Besides, training multi-person generative models demands massive multi-person data. Our proposed training pipeline depends solely on single-person videos to learn multi-person speaking patterns and refines interactivity with only a few real multi-person clips. Furthermore, we contribute a targeted metric and dataset designed to evaluate the naturalness and interactivity of the generated multi-person videos. Extensive experiments demonstrate that AnyTalker achieves remarkable lip synchronization, visual quality, and natural interactivity, striking a favorable balance between data costs and identity scalability.

</details>

#### [AI killed the video star. Audio-driven diffusion model for expressive talking head generation](https://arxiv.org/abs/2511.22488)
**Baptiste Chopin, Tashvik Dhamija, Pranav Balaji, Yaohui Wang et al.** · 2025-11-27

<details>
<summary>Abstract</summary>

We propose Dimitra++, a novel framework for audio-driven talking head generation, streamlined to learn lip motion, facial expression, as well as head pose motion. Specifically, we propose a conditional Motion Diffusion Transformer (cMDT) to model facial motion sequences, employing a 3D representation. The cMDT is conditioned on two inputs: a reference facial image, which determines appearance, as well as an audio sequence, which drives the motion. Quantitative and qualitative experiments, as well as a user study on two widely employed datasets, i.e., VoxCeleb2 and CelebV-HQ, suggest that Dimitra++ is able to outperform existing approaches in generating realistic talking heads imparting lip motion, facial expression, and head pose.

</details>

#### [Towards Authentic Movie Dubbing with Retrieve-Augmented Director-Actor Interaction Learning](https://arxiv.org/abs/2511.14249)
**Rui Liu, Yuan Zhao, Zhenqi Jia** · 2025-11-18

<details>
<summary>Abstract</summary>

The automatic movie dubbing model generates vivid speech from given scripts, replicating a speaker's timbre from a brief timbre prompt while ensuring lip-sync with the silent video. Existing approaches simulate a simplified workflow where actors dub directly without preparation, overlooking the critical director-actor interaction. In contrast, authentic workflows involve a dynamic collaboration: directors actively engage with actors, guiding them to internalize the context cues, specifically emotion, before performance. To address this issue, we propose a new Retrieve-Augmented Director-Actor Interaction Learning scheme to achieve authentic movie dubbing, termed Authentic-Dubber, which contains three novel mechanisms: (1) We construct a multimodal Reference Footage library to simulate the learning footage provided by directors. Note that we integrate Large Language Models (LLMs) to achieve deep comprehension of emotional representations across multimodal signals. (2) To emulate how actors efficiently and comprehensively internalize director-provided footage during dubbing, we propose an Emotion-Similarity-based Retrieval-Augmentation strategy. This strategy retrieves the most relevant multimodal information that aligns with the target silent video. (3) We develop a Progressive Graph-based speech generation approach that incrementally incorporates the retrieved multimodal emotional knowledge, thereby simulating the actor's final dubbing process. The above mechanisms enable the Authentic-Dubber to faithfully replicate the authentic dubbing workflow, achieving comprehensive improvements in emotional expressiveness. Both subjective and objective evaluations on the V2C Animation benchmark dataset validate the effectiveness. The code and demos are available at https://github.com/AI-S2-Lab/Authentic-Dubber.

</details>

#### [The Creation of Immersive Experiences in Transcultural Entertainment: An Action Design Process Focused on Neural Rendering](https://www.semanticscholar.org/paper/60618f2e0144dad7862f144e02000e3e2a11fd55)
**Mike Seymour, Barney Tan, Yang Li** · 2025-11-13

<details>
<summary>Abstract</summary>

This study examines how artificial intelligence (AI), specifically neural facial reenactment (NFR), can address the limitations of dubbing and subtitling in adapting foreign films. Using action design research and guided by presence theory, we codeveloped and evaluated an NFR process during the English adaptation of the Polish feature film The Champion. Unlike conventional dubbing, which often disrupts immersion through poor lip-sync or script changes, NFR preserves the original actors’ performances, aligning them with new dialogue. Independent broadcast-quality assessments confirmed technical validity, and subsequent commercial distribution on a major streaming platform demonstrated scalability and audience acceptance. From this process, we derived six design principles: avoid forced script changes, respect creative intent, minimize intrusive technology, reduce training data requirements, enable flexible audience access, and codesign with existing creative structures. These principles offer a replicable template for the responsible researching and developing of AI in information systems. For practice, the findings show that NFR can improve cultural accessibility and create new creative and technical roles rather than displacing talent. For policy, the study highlights the importance of codesign, transparency, and preserving artistic integrity when integrating AI into global cultural products.

</details>

#### [Lightweight Audio-Visual Networks for Real-Time Lip-Sync DeepFake Detection](https://www.semanticscholar.org/paper/33c3ab9ce4d8fe0062d491667557f2b4f44103f6)
**Quoc-Dat Le, Vu-Hoang Tran, Viet-Dat Nguyen** · 2025-11-12

<details>
<summary>Abstract</summary>

Lip-sync DeepFakes, which manipulate lip movements to match tampered audio while preserving visual identity, pose significant challenges to digital content integrity due to their subtle temporal inconsistencies. Traditional detection methods focusing on spatial artifacts are often ineffective against these forgeries, while recent temporal correlation models, despite their accuracy, are computationally intensive and impractical for resource-constrained devices. This paper proposes a lightweight, real-time framework for lip-sync DeepFake detection, leveraging compact neural networks, temporal attention mechanisms, and knowledge distillation. Utilizing ShuffleNetV2x0.5 as the backbone, our model incorporates audio-visual temporal modeling and human-inspired perceptual cues, such as lip-speech synchronization, to achieve robust detection. Knowledge distillation transfers insights from a high-capacity teacher model to ensure high accuracy with a model size of only 18 MB and an inference speed of 20 FPS on standard CPUs, optimized for edge device deployment. Evaluated on the AVLIP and FakeAVCeleb datasets, our approach achieves 93.50% average precision on AVLIP and 99.23% average precision on FakeAVCeleb, rivaling state-of-the-art models while enabling real-time performance on edge devices. This framework is well-suited for applications like mobile video authentication, livestream monitoring, and content moderation, addressing the growing need for efficient and scalable DeepFake detection solutions.

</details>

#### [Is It Truly Necessary to Process and Fit Minutes-Long Reference Videos for Personalized Talking Face Generation?](https://arxiv.org/abs/2511.07940)
**Rui-Qing Sun, Ang Li, Zhijing Wu, Tian Lan et al.** · 2025-11-11

<details>
<summary>Abstract</summary>

Talking Face Generation (TFG) aims to produce realistic and dynamic talking portraits, with broad applications in fields such as digital education, film and television production, e-commerce live streaming, and other related areas. Currently, TFG methods based on Neural Radiated Field (NeRF) or 3D Gaussian sputtering (3DGS) are received widespread attention. They learn and store personalized features from reference videos of each target individual to generate realistic speaking videos. To ensure models can capture sufficient 3D information and successfully learns the lip-audio mapping, previous studies usually require meticulous processing and fitting several minutes of reference video, which always takes hours. The computational burden of processing and fitting long reference videos severely limits the practical application value of these methods.However, is it really necessary to fit such minutes of reference video? Our exploratory case studies show that using some informative reference video segments of just a few seconds can achieve performance comparable to or even better than the full reference video. This indicates that video informative quality is much more important than its length. Inspired by this observation, we propose the ISExplore (short for Informative Segment Explore), a simple-yet-effective segment selection strategy that automatically identifies the informative 5-second reference video segment based on three key data quality dimensions: audio feature diversity, lip movement amplitude, and number of camera views. Extensive experiments demonstrate that our approach increases data processing and training speed by more than 5x for NeRF and 3DGS methods, while maintaining high-fidelity output. Project resources are available at xx.

</details>

#### [ConsistTalk: Intensity Controllable Temporally Consistent Talking Head Generation with Diffusion Noise Search](https://arxiv.org/abs/2511.06833)
**Zhenjie Liu, Jianzhang Lu, Renjie Lu, Cong Liang et al.** · 2025-11-10

<details>
<summary>Abstract</summary>

Recent advancements in video diffusion models have significantly enhanced audio-driven portrait animation. However, current methods still suffer from flickering, identity drift, and poor audio-visual synchronization. These issues primarily stem from entangled appearance-motion representations and unstable inference strategies. In this paper, we introduce \textbf{ConsistTalk}, a novel intensity-controllable and temporally consistent talking head generation framework with diffusion noise search inference. First, we propose \textbf{an optical flow-guided temporal module (OFT)} that decouples motion features from static appearance by leveraging facial optical flow, thereby reducing visual flicker and improving temporal consistency. Second, we present an \textbf{Audio-to-Intensity (A2I) model} obtained through multimodal teacher-student knowledge distillation. By transforming audio and facial velocity features into a frame-wise intensity sequence, the A2I model enables joint modeling of audio and visual motion, resulting in more natural dynamics. This further enables fine-grained, frame-wise control of motion dynamics while maintaining tight audio-visual synchronization. Third, we introduce a \textbf{diffusion noise initialization strategy (IC-Init)}. By enforcing explicit constraints on background coherence and motion continuity during inference-time noise search, we achieve better identity preservation and refine motion dynamics compared to the current autoregressive strategy. Extensive experiments demonstrate that ConsistTalk significantly outperforms prior methods in reducing flicker, preserving identity, and delivering temporally stable, high-fidelity talking head videos.

</details>

#### [THEval. Evaluation Framework for Talking Head Video Generation](https://arxiv.org/abs/2511.04520)
**Nabyl Quignon, Baptiste Chopin, Yaohui Wang, Antitza Dantcheva** · 2025-11-06

<details>
<summary>Abstract</summary>

Video generation has achieved remarkable progress, with generated videos increasingly resembling real ones. However, the rapid advance in generation has outpaced the development of adequate evaluation metrics. Currently, the assessment of talking head generation primarily relies on limited metrics, evaluating general video quality, lip synchronization, and on conducting user studies. Motivated by this, we propose a new evaluation framework comprising 8 metrics related to three dimensions (i) quality, (ii) naturalness, and (iii) synchronization. In selecting the metrics, we place emphasis on efficiency, as well as alignment with human preferences. Based on this considerations, we streamline to analyze fine-grained dynamics of head, mouth, and eyebrows, as well as face quality. Our extensive experiments on 85,000 videos generated by 17 state-of-the-art models suggest that while many algorithms excel in lip synchronization, they face challenges with generating expressiveness and artifact-free details. These videos were generated based on a novel real dataset, that we have curated, in order to mitigate bias of training data. Our proposed benchmark framework is aimed at evaluating the improvement of generative methods. Original code, dataset and leaderboards will be publicly released and regularly updated with new methods, in order to reflect progress in the field.

</details>

#### [UniAVGen: Unified Audio and Video Generation with Asymmetric Cross-Modal Interactions](https://arxiv.org/abs/2511.03334)
**Guozhen Zhang, Zixiang Zhou, Teng Hu, Ziqiao Peng et al.** · 2025-11-05

<details>
<summary>Abstract</summary>

Due to the lack of effective cross-modal modeling, existing open-source audio-video generation methods often exhibit compromised lip synchronization and insufficient semantic consistency. To mitigate these drawbacks, we propose UniAVGen, a unified framework for joint audio and video generation. UniAVGen is anchored in a dual-branch joint synthesis architecture, incorporating two parallel Diffusion Transformers (DiTs) to build a cohesive cross-modal latent space. At its heart lies an Asymmetric Cross-Modal Interaction mechanism, which enables bidirectional, temporally aligned cross-attention, thus ensuring precise spatiotemporal synchronization and semantic consistency. Furthermore, this cross-modal interaction is augmented by a Face-Aware Modulation module, which dynamically prioritizes salient regions in the interaction process. To enhance generative fidelity during inference, we additionally introduce Modality-Aware Classifier-Free Guidance, a novel strategy that explicitly amplifies cross-modal correlation signals. Notably, UniAVGen's robust joint synthesis design enables seamless unification of pivotal audio-video tasks within a single model, such as joint audio-video generation and continuation, video-to-audio dubbing, and audio-driven video synthesis. Comprehensive experiments validate that, with far fewer training samples (1.3M vs. 30.1M), UniAVGen delivers overall advantages in audio-video synchronization, timbre consistency, and emotion consistency.

</details>

#### [Densemarks: Learning Canonical Embeddings for Human Heads Images via Point Tracks](https://arxiv.org/abs/2511.02830)
**Dmitrii Pozdeev, Alexey Artemov, Ananta R. Bhattarai, Artem Sevastopolsky** · 2025-11-04

<details>
<summary>Abstract</summary>

We propose DenseMarks - a new learned representation for human heads, enabling high-quality dense correspondences of human head images. For a 2D image of a human head, a Vision Transformer network predicts a 3D embedding for each pixel, which corresponds to a location in a 3D canonical unit cube. In order to train our network, we collect a dataset of pairwise point matches, estimated by a state-of-the-art point tracker over a collection of diverse in-the-wild talking heads videos, and guide the mapping via a contrastive loss, encouraging matched points to have close embeddings. We further employ multi-task learning with face landmarks and segmentation constraints, as well as imposing spatial continuity of embeddings through latent cube features, which results in an interpretable and queryable canonical space. The representation can be used for finding common semantic parts, face/head tracking, and stereo reconstruction. Due to the strong supervision, our method is robust to pose variations and covers the entire head, including hair. Additionally, the canonical space bottleneck makes sure the obtained representations are consistent across diverse poses and individuals. We demonstrate state-of-the-art results in geometry-aware point matching and monocular head tracking with 3D Morphable Models. The code and the model checkpoint will be made available to the public.

</details>

#### [Immersive interactive intelligent patient educational system for venous thromboembolism](https://www.semanticscholar.org/paper/64754368ff056b9a72c6e188261c73bff3dcd7a6)
**Y. Guo** · 2025-11-01

<details>
<summary>Abstract</summary>

Large language models (LLMs) can serve as virtual teaching assistants, providing patients with detailed and relevant information and perhaps eventually interactive simulations. This study explored the integration of LLMs into the education and patient-centered care for venous thromboembolism (VTE). We developed a immersive interactive intelligent patient educational system for patients with VTE using LLM，Qwen1.5-7B, Text-to-Speech(TTS)，and Lip Synchronization(Lip-Sync) technologies. The immersive interactive intelligent patient educational system (ChatVTE) consisted of four components (Figure 1): 1) Information Collection of Multimodal Optical Character Recognition Technology Based on Large Models, which collecting patient's clinical data. 2) Knowledge, Attitude/Belief, Practice and Health Belief Model, which capturing patient's health requirement. 3) VTE relevant data were systematically gathered from open-access Internet sources and indexed into a knowledge database. We leveraged Retrieval-Augmented Language Modeling to recall this information and utilized it for pretraining, which was then integrated into Qwen1.5-7B, creating an VTE-specific knowledge question & answer platform. 4) Based on intelligent question & answer, a digital virtual doctor created with TTS Lip-Sync technologies to facilities patient education （Figure 2）. ChatVTE generated fewer hallucinations and demonstrated greater consistency，improved the quality of doctor-patient interaction and enhance the effectiveness of knowledge dissemination. To the best of our knowledge, the digital virtual VTE doctor of ChatVTE was the first digital virtual doctor driven by specialty-specific VTE knowledge retrieval AI that utilizes the latest LLM. It appeared the promising for patient education and shared clinical decision support. Continued research and evaluation are necessary to ensure the optimal integration of AI-based interactive tools into patient-centered care.

</details>

#### [Audio-Visual Speech Enhancement In Complex Scenarios With Separation And Dereverberation Joint Modeling](https://arxiv.org/abs/2510.26825)
**Jiarong Du, Zhan Jin, Peijun Yang, Juan Liu et al.** · 2025-10-29

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement (AVSE) is a task that uses visual auxiliary information to extract a target speaker's speech from mixed audio. In real-world scenarios, there often exist complex acoustic environments, accompanied by various interfering sounds and reverberation. Most previous methods struggle to cope with such complex conditions, resulting in poor perceptual quality of the extracted speech. In this paper, we propose an effective AVSE system that performs well in complex acoustic environments. Specifically, we design a "separation before dereverberation" pipeline that can be extended to other AVSE networks. The 4th COGMHEAR Audio-Visual Speech Enhancement Challenge (AVSEC) aims to explore new approaches to speech processing in multimodal complex environments. We validated the performance of our system in AVSEC-4: we achieved excellent results in the three objective metrics on the competition leaderboard, and ultimately secured first place in the human subjective listening test.

</details>

#### [See the Speaker: Crafting High-Resolution Talking Faces from Speech with Prior Guidance and Region Refinement](https://arxiv.org/abs/2510.26819)
**Jinting Wang, Jun Wang, Hei Victor Cheng, Li Liu** · 2025-10-28

<details>
<summary>Abstract</summary>

Unlike existing methods that rely on source images as appearance references and use source speech to generate motion, this work proposes a novel approach that directly extracts information from the speech, addressing key challenges in speech-to-talking face. Specifically, we first employ a speech-to-face portrait generation stage, utilizing a speech-conditioned diffusion model combined with statistical facial prior and a sample-adaptive weighting module to achieve high-quality portrait generation. In the subsequent speech-driven talking face generation stage, we embed expressive dynamics such as lip movement, facial expressions, and eye movements into the latent space of the diffusion model and further optimize lip synchronization using a region-enhancement module. To generate high-resolution outputs, we integrate a pre-trained Transformer-based discrete codebook with an image rendering network, enhancing video frame details in an end-to-end manner. Experimental results demonstrate that our method outperforms existing approaches on the HDTF, VoxCeleb, and AVSpeech datasets. Notably, this is the first method capable of generating high-resolution, high-quality talking face videos exclusively from a single speech input.

</details>

#### [MAGIC-Talk: Motion-aware Audio-Driven Talking Face Generation with Customizable Identity Control](https://arxiv.org/abs/2510.22810)
**Fatemeh Nazarieh, Zhenhua Feng, Diptesh Kanojia, Muhammad Awais et al.** · 2025-10-26

<details>
<summary>Abstract</summary>

Audio-driven talking face generation has gained significant attention for applications in digital media and virtual avatars. While recent methods improve audio-lip synchronization, they often struggle with temporal consistency, identity preservation, and customization, especially in long video generation. To address these issues, we propose MAGIC-Talk, a one-shot diffusion-based framework for customizable and temporally stable talking face generation. MAGIC-Talk consists of ReferenceNet, which preserves identity and enables fine-grained facial editing via text prompts, and AnimateNet, which enhances motion coherence using structured motion priors. Unlike previous methods requiring multiple reference images or fine-tuning, MAGIC-Talk maintains identity from a single image while ensuring smooth transitions across frames. Additionally, a progressive latent fusion strategy is introduced to improve long-form video quality by reducing motion inconsistencies and flickering. Extensive experiments demonstrate that MAGIC-Talk outperforms state-of-the-art methods in visual quality, identity preservation, and synchronization accuracy, offering a robust solution for talking face generation.

</details>

#### [DeepfakeBench-MM: A Comprehensive Benchmark for Multimodal Deepfake Detection](https://arxiv.org/abs/2510.22622)
**Kangran Zhao, Yupeng Chen, Xiaoyu Zhang, Yize Chen et al.** · 2025-10-26

<details>
<summary>Abstract</summary>

The misuse of advanced generative AI models has resulted in the widespread proliferation of falsified data, particularly forged human-centric audiovisual content, which poses substantial societal risks (e.g., financial fraud and social instability). In response to this growing threat, several works have preliminarily explored countermeasures. However, the lack of sufficient and diverse training data, along with the absence of a standardized benchmark, hinder deeper exploration. To address this challenge, we first build Mega-MMDF, a large-scale, diverse, and high-quality dataset for multimodal deepfake detection. Specifically, we employ 21 forgery pipelines through the combination of 10 audio forgery methods, 12 visual forgery methods, and 6 audio-driven face reenactment methods. Mega-MMDF currently contains 0.1 million real samples and 1.1 million forged samples, making it one of the largest and most diverse multimodal deepfake datasets, with plans for continuous expansion. Building on it, we present DeepfakeBench-MM, the first unified benchmark for multimodal deepfake detection. It establishes standardized protocols across the entire detection pipeline and serves as a versatile platform for evaluating existing methods as well as exploring novel approaches. DeepfakeBench-MM currently supports 5 datasets and 11 multimodal deepfake detectors. Furthermore, our comprehensive evaluations and in-depth analyses uncover several key findings from multiple perspectives (e.g., augmentation, stacked forgery). We believe that DeepfakeBench-MM, together with our large-scale Mega-MMDF, will serve as foundational infrastructures for advancing multimodal deepfake detection.

</details>

#### [Lip-Sync Analyzer for Deepfake Detection and Peeking Behind the Black Box with Explainable AI](https://www.semanticscholar.org/paper/268dee604af0f25e9e5ad493fee603f6c39acde9)
**S. Sakib, S. Haque, Atanu Shome** · 2025-10-23

<details>
<summary>Abstract</summary>

The swift evolution of deepfake technology presents significant threats to the credibility and trustworthiness of digital media. This work presents a deepfake detection framework that combines spatial and audio-visual features, with a specific focus on lip-sync forgeries. We evaluate multiple state-of-the-art CNN architectures—DenseNet-121, EfficientNet-B0, InceptionV3, ResNet-50, and XceptionNet—alongside a Vision Transformer (ViT-B/32). Experiments on the AVLips dataset (3,396 real and 4,206 fake videos) show that ViT-B/32 achieves superior performance, with 96% F1-score, and 99% AUC. Audio-visual fusion consistently outperforms visual-only models, highlighting the strength of multimodal analysis. To enhance transparency, LIME-based explainable AI visualizations are employed to interpret model predictions. Unlike previous works that primarily rely on unimodal cues, our approach uniquely integrates audio waveforms with visual frames to expose subtle inconsistencies in lip synchronization. Given the potential misuse of deepfakes in misinformation, fraud, and political manipulation, this study emphasizes the urgent need for robust and interpretable detection methods. Our findings confirm the effectiveness of transformer-based models with XAI for dependable deepfake detection, with future work focusing on temporal modeling and scalability.

</details>

#### [Playmate2: Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback](https://arxiv.org/abs/2510.12089)
**Xingpei Ma, Shenneng Huang, Jiaran Cai, Yuansheng Guan et al.** · 2025-10-14

<details>
<summary>Abstract</summary>

Recent advances in diffusion models have significantly improved audio-driven human video generation, surpassing traditional methods in both quality and controllability. However, existing approaches still face challenges in lip-sync accuracy, temporal coherence for long video generation, and multi-character animation. In this work, we propose a diffusion transformer (DiT)-based framework for generating lifelike talking videos of arbitrary length, and introduce a training-free method for multi-character audio-driven animation. First, we employ a LoRA-based training strategy combined with a position shift inference approach, which enables efficient long video generation while preserving the capabilities of the foundation model. Moreover, we combine partial parameter updates with reward feedback to enhance both lip synchronization and natural body motion. Finally, we propose a training-free approach, Mask Classifier-Free Guidance (Mask-CFG), for multi-character animation, which requires no specialized datasets or model modifications and supports audio-driven animation for three or more characters. Experimental results demonstrate that our method outperforms existing state-of-the-art approaches, achieving high-quality, temporally coherent, and multi-character audio-driven video generation in a simple, efficient, and cost-effective manner.

</details>

#### [DEMO: Disentangled Motion Latent Flow Matching for Fine-Grained Controllable Talking Portrait Synthesis](https://arxiv.org/abs/2510.10650)
**Peiyin Chen, Zhuowei Yang, Hui Feng, Sheng Jiang et al.** · 2025-10-12

<details>
<summary>Abstract</summary>

Audio-driven talking-head generation has advanced rapidly with diffusion-based generative models, yet producing temporally coherent videos with fine-grained motion control remains challenging. We propose DEMO, a flow-matching generative framework for audio-driven talking-portrait video synthesis that delivers disentangled, high-fidelity control of lip motion, head pose, and eye gaze. The core contribution is a motion auto-encoder that builds a structured latent space in which motion factors are independently represented and approximately orthogonalized. On this disentangled motion space, we apply optimal-transport-based flow matching with a transformer predictor to generate temporally smooth motion trajectories conditioned on audio. Extensive experiments across multiple benchmarks show that DEMO outperforms prior methods in video realism, lip-audio synchronization, and motion fidelity. These results demonstrate that combining fine-grained motion disentanglement with flow-based generative modeling provides a powerful new paradigm for controllable talking-head video synthesis.

</details>

#### [AUREXA-SE: Audio-Visual Unified Representation Exchange Architecture with Cross-Attention and Squeezeformer for Speech Enhancement](https://arxiv.org/abs/2510.05295)
**M. Sajid, Deepanshu Gupta, Yash Modi, Sanskriti Jain et al.** · 2025-10-06

<details>
<summary>Abstract</summary>

In this paper, we propose AUREXA-SE (Audio-Visual Unified Representation Exchange Architecture with Cross-Attention and Squeezeformer for Speech Enhancement), a progressive bimodal framework tailored for audio-visual speech enhancement (AVSE). AUREXA-SE jointly leverages raw audio waveforms and visual cues by employing a U-Net-based 1D convolutional encoder for audio and a Swin Transformer V2 for efficient and expressive visual feature extraction. Central to the architecture is a novel bidirectional cross-attention mechanism, which facilitates deep contextual fusion between modalities, enabling rich and complementary representation learning. To capture temporal dependencies within the fused embeddings, a stack of lightweight Squeezeformer blocks combining convolutional and attention modules is introduced. The enhanced embeddings are then decoded via a U-Net-style decoder for direct waveform reconstruction, ensuring perceptually consistent and intelligible speech output. Experimental evaluations demonstrate the effectiveness of AUREXA-SE, achieving significant performance improvements over noisy baselines, with STOI of 0.516, PESQ of 1.323, and SI-SDR of -4.322 dB. The source code of AUREXA-SE is available at https://github.com/mtanveer1/AVSEC-4-Challenge-2025.

</details>

#### [Input-Aware Sparse Attention for Real-Time Co-Speech Video Generation](https://arxiv.org/abs/2510.02617)
**Beijia Lu, Ziyi Chen, Jing Xiao, Jun-Yan Zhu** · 2025-10-02

<details>
<summary>Abstract</summary>

Diffusion models can synthesize realistic co-speech video from audio for various applications, such as video creation and virtual agents. However, existing diffusion-based methods are slow due to numerous denoising steps and costly attention mechanisms, preventing real-time deployment. In this work, we distill a many-step diffusion video model into a few-step student model. Unfortunately, directly applying recent diffusion distillation methods degrades video quality and falls short of real-time performance. To address these issues, our new video distillation method leverages input human pose conditioning for both attention and loss functions. We first propose using accurate correspondence between input human pose keypoints to guide attention to relevant regions, such as the speaker's face, hands, and upper body. This input-aware sparse attention reduces redundant computations and strengthens temporal correspondences of body parts, improving inference efficiency and motion coherence. To further enhance visual quality, we introduce an input-aware distillation loss that improves lip synchronization and hand motion realism. By integrating our input-aware sparse attention and distillation loss, our method achieves real-time performance with improved visual quality compared to recent audio-driven and input-driven methods. We also conduct extensive experiments showing the effectiveness of our algorithmic design choices.

</details>

#### [StableDub: Taming Diffusion Prior for Generalized and Efficient Visual Dubbing](https://arxiv.org/abs/2509.21887)
**Liyang Chen, Tianze Zhou, Xu He, Boshi Tang et al.** · 2025-09-26

<details>
<summary>Abstract</summary>

The visual dubbing task aims to generate mouth movements synchronized with the driving audio, which has seen significant progress in recent years. However, two critical deficiencies hinder their wide application: (1) Audio-only driving paradigms inadequately capture speaker-specific lip habits, which fail to generate lip movements similar to the target avatar; (2) Conventional blind-inpainting approaches frequently produce visual artifacts when handling obstructions (e.g., microphones, hands), limiting practical deployment. In this paper, we propose StableDub, a novel and concise framework integrating lip-habit-aware modeling with occlusion-robust synthesis. Specifically, building upon the Stable-Diffusion backbone, we develop a lip-habit-modulated mechanism that jointly models phonemic audio-visual synchronization and speaker-specific orofacial dynamics. To achieve plausible lip geometries and object appearances under occlusion, we introduce the occlusion-aware training strategy by explicitly exposing the occlusion objects to the inpainting process. By incorporating the proposed designs, the model eliminates the necessity for cost-intensive priors in previous methods, thereby exhibiting superior training efficiency on the computationally intensive diffusion-based backbone. To further optimize training efficiency from the perspective of model architecture, we introduce a hybrid Mamba-Transformer architecture, which demonstrates the enhanced applicability in low-resource research scenarios. Extensive experimental results demonstrate that StableDub achieves superior performance in lip habit resemblance and occlusion robustness. Our method also surpasses other methods in audio-lip sync, video quality, and resolution consistency. We expand the applicability of visual dubbing methods from comprehensive aspects, and demo videos can be found at https://stabledub.github.io.

</details>

#### [Talking Head Generation via AU-Guided Landmark Prediction](https://arxiv.org/abs/2509.19749)
**Shao-Yu Chang, Jingyi Xu, Hieu Le, Dimitris Samaras** · 2025-09-24

<details>
<summary>Abstract</summary>

We propose a two-stage framework for audio-driven talking head generation with fine-grained expression control via facial Action Units (AUs). Unlike prior methods relying on emotion labels or implicit AU conditioning, our model explicitly maps AUs to 2D facial landmarks, enabling physically grounded, per-frame expression control. In the first stage, a variational motion generator predicts temporally coherent landmark sequences from audio and AU intensities. In the second stage, a diffusion-based synthesizer generates realistic, lip-synced videos conditioned on these landmarks and a reference image. This separation of motion and appearance improves expression accuracy, temporal stability, and visual realism. Experiments on the MEAD dataset show that our method outperforms state-of-the-art baselines across multiple metrics, demonstrating the effectiveness of explicit AU-to-landmark modeling for expressive talking head generation.

</details>

#### [KSDiff: Keyframe-Augmented Speech-Aware Dual-Path Diffusion for Facial Animation](https://arxiv.org/abs/2509.20128)
**Tianle Lyu, Junchuan Zhao, Ye Wang** · 2025-09-24

<details>
<summary>Abstract</summary>

Audio-driven facial animation has made significant progress in multimedia applications, with diffusion models showing strong potential for talking-face synthesis. However, most existing works treat speech features as a monolithic representation and fail to capture their fine-grained roles in driving different facial motions, while also overlooking the importance of modeling keyframes with intense dynamics. To address these limitations, we propose KSDiff, a Keyframe-Augmented Speech-Aware Dual-Path Diffusion framework. Specifically, the raw audio and transcript are processed by a Dual-Path Speech Encoder (DPSE) to disentangle expression-related and head-pose-related features, while an autoregressive Keyframe Establishment Learning (KEL) module predicts the most salient motion frames. These components are integrated into a Dual-path Motion generator to synthesize coherent and realistic facial motions. Extensive experiments on HDTF and VoxCeleb demonstrate that KSDiff achieves state-of-the-art performance, with improvements in both lip synchronization accuracy and head-pose naturalness. Our results highlight the effectiveness of combining speech disentanglement with keyframe-aware diffusion for talking-head generation.

</details>

#### [PGSTalker: Real-Time Audio-Driven Talking Head Generation via 3D Gaussian Splatting with Pixel-Aware Density Control](https://arxiv.org/abs/2509.16922)
**Tianheng Zhu, Yinfeng Yu, Liejun Wang, Fuchun Sun et al.** · 2025-09-21

<details>
<summary>Abstract</summary>

Audio-driven talking head generation is crucial for applications in virtual reality, digital avatars, and film production. While NeRF-based methods enable high-fidelity reconstruction, they suffer from low rendering efficiency and suboptimal audio-visual synchronization. This work presents PGSTalker, a real-time audio-driven talking head synthesis framework based on 3D Gaussian Splatting (3DGS). To improve rendering performance, we propose a pixel-aware density control strategy that adaptively allocates point density, enhancing detail in dynamic facial regions while reducing redundancy elsewhere. Additionally, we introduce a lightweight Multimodal Gated Fusion Module to effectively fuse audio and spatial features, thereby improving the accuracy of Gaussian deformation prediction. Extensive experiments on public datasets demonstrate that PGSTalker outperforms existing NeRF- and 3DGS-based approaches in rendering quality, lip-sync precision, and inference speed. Our method exhibits strong generalization capabilities and practical potential for real-world deployment.

</details>

#### [Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior](https://arxiv.org/abs/2509.14379)
**Yochai Yemini, Rami Ben-Ari, Sharon Gannot, Ethan Fetaya** · 2025-09-17

<details>
<summary>Abstract</summary>

In this paper, we address the problem of single-microphone speech separation in the presence of ambient noise. We propose a generative unsupervised technique that directly models both clean speech and structured noise components, training exclusively on these individual signals rather than noisy mixtures. Our approach leverages an audio-visual score model that incorporates visual cues to serve as a strong generative speech prior. By explicitly modelling the noise distribution alongside the speech distribution, we enable effective decomposition through the inverse problem paradigm. We perform speech separation by sampling from the posterior distributions via a reverse diffusion process, which directly estimates and removes the modelled noise component to recover clean constituent signals. Experimental results demonstrate promising performance, highlighting the effectiveness of our direct noise modelling approach in challenging acoustic environments.

</details>

#### [A Lightweight Pipeline for Noisy Speech Voice Cloning and Accurate Lip Sync Synthesis](https://arxiv.org/abs/2509.12831)
**Javeria Amir, Farwa Attaria, Mah Jabeen, Umara Noor et al.** · 2025-09-16

<details>
<summary>Abstract</summary>

Recent developments in voice cloning and talking head generation demonstrate impressive capabilities in synthesizing natural speech and realistic lip synchronization. Current methods typically require and are trained on large scale datasets and computationally intensive processes using clean studio recorded inputs that is infeasible in noisy or low resource environments. In this paper, we introduce a new modular pipeline comprising Tortoise text to speech. It is a transformer based latent diffusion model that can perform high fidelity zero shot voice cloning given only a few training samples. We use a lightweight generative adversarial network architecture for robust real time lip synchronization. The solution will contribute to many essential tasks concerning less reliance on massive pre training generation of emotionally expressive speech and lip synchronization in noisy and unconstrained scenarios. The modular structure of the pipeline allows an easy extension for future multi modal and text guided voice modulation and it could be used in real world systems.

</details>

#### [Robust Audio-Visual Target Speaker Extraction with Emotion-Aware Multiple Enrollment Fusion](https://arxiv.org/abs/2509.12583)
**Zhan Jin, Bang Zeng, Peijun Yang, Jiarong Du et al.** · 2025-09-16

<details>
<summary>Abstract</summary>

Target Speaker Extraction (TSE) is a critical challenge in cocktail party scenarios. While leveraging multiple modalities, such as voice, lip, face, and expression embeddings, can enhance performance, real-world applications often suffer from intermittent modality dropout. This paper presents a comprehensive study on the interactions and robustness of various multimodal fusion strategies under varying degrees of modality dropout. We build upon a state-of-the-art audio-visual speech enhancement system and integrate four distinct speaker identity cues: lip embeddings for synchronized contextual information, a voice speaker embedding extracted via cross-attention for acoustic consistency, a static face embedding for speaker identity, and a novel dynamic expression embedding for frame-wise emotional features. We systematically evaluate different combinations of these modalities under two key training regimes: zero dropout and 80% modality dropout. Extensive experiments demonstrate that while a full multimodal ensemble achieves optimal performance under ideal (zero dropout) conditions, its effectiveness diminishes significantly when test-time dropout occurs without prior exposure during training. Crucially, we show that training with a high (80%) modality dropout rate dramatically enhances model robustness, enabling the system to maintain superior performance even under severe test-time missing modalities. Our findings highlight that voice embeddings exhibit consistent robustness, while the proposed expression embedding provides valuable complementary information. This work underscores the importance of training strategies that account for real-world imperfection, moving beyond pure performance maximization to achieve practical reliability in multimodal speech enhancement systems.

</details>

#### [Kling-Avatar: Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis](https://arxiv.org/abs/2509.09595)
**Yikang Ding, Jiwen Liu, Wenyuan Zhang, Zekun Wang et al.** · 2025-09-11

<details>
<summary>Abstract</summary>

Recent advances in audio-driven avatar video generation have significantly enhanced audio-visual realism. However, existing methods treat instruction conditioning merely as low-level tracking driven by acoustic or visual cues, without modeling the communicative purpose conveyed by the instructions. This limitation compromises their narrative coherence and character expressiveness. To bridge this gap, we introduce Kling-Avatar, a novel cascaded framework that unifies multimodal instruction understanding with photorealistic portrait generation. Our approach adopts a two-stage pipeline. In the first stage, we design a multimodal large language model (MLLM) director that produces a blueprint video conditioned on diverse instruction signals, thereby governing high-level semantics such as character motion and emotions. In the second stage, guided by blueprint keyframes, we generate multiple sub-clips in parallel using a first-last frame strategy. This global-to-local framework preserves fine-grained details while faithfully encoding the high-level intent behind multimodal instructions. Our parallel architecture also enables fast and stable generation of long-duration videos, making it suitable for real-world applications such as digital human livestreaming and vlogging. To comprehensively evaluate our method, we construct a benchmark of 375 curated samples covering diverse instructions and challenging scenarios. Extensive experiments demonstrate that Kling-Avatar is capable of generating vivid, fluent, long-duration videos at up to 1080p and 48 fps, achieving superior performance in lip synchronization accuracy, emotion and dynamic expressiveness, instruction controllability, identity preservation, and cross-domain generalization. These results establish Kling-Avatar as a new benchmark for semantically grounded, high-fidelity audio-driven avatar synthesis.

</details>

#### [Bitrate-Controlled Diffusion for Disentangling Motion and Content in Video](https://arxiv.org/abs/2509.08376)
**Xiao Li, Qi Chen, Xiulian Peng, Kai Yu et al.** · 2025-09-10

<details>
<summary>Abstract</summary>

We propose a novel and general framework to disentangle video data into its dynamic motion and static content components. Our proposed method is a self-supervised pipeline with less assumptions and inductive biases than previous works: it utilizes a transformer-based architecture to jointly generate flexible implicit features for frame-wise motion and clip-wise content, and incorporates a low-bitrate vector quantization as an information bottleneck to promote disentanglement and form a meaningful discrete motion space. The bitrate-controlled latent motion and content are used as conditional inputs to a denoising diffusion model to facilitate self-supervised representation learning. We validate our disentangled representation learning framework on real-world talking head videos with motion transfer and auto-regressive motion generation tasks. Furthermore, we also show that our method can generalize to other types of video data, such as pixel sprites of 2D cartoon characters. Our work presents a new perspective on self-supervised learning of disentangled video representations, contributing to the broader field of video analysis and generation.

</details>

#### [NeRF-LipSync: A Diffusion Model for Speech-Driven and View-Consistent Lip Synchronization in Digital Avatars](https://www.semanticscholar.org/paper/e63487520103d92b2c8eccaaa6b1f5784f679822)
**A. Axyonov, Mikhail Dolgushin, D. Ryumin** · 2025-09-04

<details>
<summary>Abstract</summary>

Abstract. Achieving natural, accurate, and identity-preserving lip synchronization in talking avatars is a fundamental problem in audio-visual synthesis. Existing methods often struggle to generalize across speakers, maintain temporal smoothness, or preserve view consistency due to architectural limitations. In this paper, we present NeRF-LipSync, a novel generative framework that synthesizes lip movements conditioned on speech audio while maintaining temporal coherence and view-consistent appearance through a combination of diffusion-based modeling and NeRF-based spatial alignment. Our model incorporates temporal attention and leverages rich audio-visual embeddings to produce expressive, speaker-specific articulation. We evaluate NeRF-LipSync on the VoxCeleb2 and LRW datasets and compare it against strong baselines including Wav2Lip, PC-AVS, and Diff2Lip. On VoxCeleb2, our method achieves an FID of 2.75, SSIM of 0.56, PSNR of 18.32, and LMD of 3.01, with synchronization accuracy (Syncc) reaching 9.06. On LRW, it yields an FID of 2.40, SSIM of 0.71, PSNR of 21.03, and LMD of 2.16. These results confirm the strong generalization ability and perceptual realism of our approach. Ablation studies highlight the contribution of NeRF alignment to identity consistency, diffusion to visual expressiveness, and temporal attention to motion stability. NeRF-LipSync thus offers a robust, scalable solution for high-quality, speech-driven avatar animation.

</details>

#### [All’s Well That FID’s Well? Result Quality and Metric Scores in GAN Models for Lip-Synchronization Tasks](https://www.semanticscholar.org/paper/f70029ecaf500aafde9906acb27fb830b4d22b21)
**Carina Geldhauser, Johan Liljegren, Pontus Nordqvist** · 2025-08-31

<details>
<summary>Abstract</summary>

This exploratory study investigates the usability of performance metrics for generative adversarial network (GAN)-based models for speech-driven facial animation. These models focus on the transfer of speech information from an audio file to a still image to generate talking-head videos in a small-scale “everyday usage” setting. Two models, LipGAN and a custom implementation of a Wasserstein GAN with gradient penalty (L1WGAN-GP), are examined for their visual performance and scoring according to commonly used metrics: Quantitative comparisons using FID, SSIM, and PSNR metrics on the GRIDTest dataset show mixed results, and metrics fail to capture local artifacts crucial for lip synchronization, pointing to limitations in their applicability for video animation tasks. The study points towards the inadequacy of current quantitative measures and emphasizes the continued necessity of human qualitative assessment for evaluating talking-head video quality.

</details>

#### [EmoCAST: Emotional Talking Portrait via Emotive Text Description](https://arxiv.org/abs/2508.20615)
**Yiguo Jiang, Xiaodong Cun, Yong Zhang, Yudian Zheng et al.** · 2025-08-28

<details>
<summary>Abstract</summary>

Emotional talking head synthesis aims to generate talking portrait videos with vivid expressions. Existing methods still exhibit limitations in control flexibility, motion naturalness, and expression quality. Moreover, currently available datasets are mainly collected in lab settings, further exacerbating these shortcomings and hindering real-world deployment. To address these challenges, we propose EmoCAST, a diffusion-based talking head framework for precise, text-driven emotional synthesis. Its contributions are threefold: (1) architectural modules that enable effective text control; (2) an emotional talking-head dataset that expands the framework's ability; and (3) training strategies that further improve performance. Specifically, for appearance modeling, emotional prompts are integrated through a text-guided emotive attention module, enhancing spatial knowledge to improve emotion understanding. To strengthen audio-emotion alignment, we introduce an emotive audio attention module to capture the interplay between controlled emotion and driving audio, generating emotion-aware features to guide precise facial motion synthesis. Additionally, we construct a large-scale, in-the-wild emotional talking head dataset with emotive text descriptions to optimize the framework's performance. Based on this dataset, we propose an emotion-aware sampling strategy and a progressive functional training strategy that improve the model's ability to capture nuanced expressive features and achieve accurate lip-sync. Overall, EmoCAST achieves state-of-the-art performance in generating realistic, emotionally expressive, and audio-synchronized talking-head videos. Project Page: https://github.com/GVCLab/EmoCAST

</details>

#### [Enhancing Visual Speaker Authentication using Dynamic Lip Movement and Meta-Learning](https://www.semanticscholar.org/paper/a197b6d30b625f38a0355ba80433c99e69ad93bb)
**P. Pathare, Garima Bajwa** · 2025-08-26

<details>
<summary>Abstract</summary>

Visual speaker authentication (VSA) remains vulnerable to sophisticated spoofing methods, such as deepfakes. Traditional deep learning approaches require extensive userspecific enrollment data and show poor generalization to new speakers. In response, we employ a few-shot meta-learning technique, specifically Model-Agnostic Meta-Learning (MAML), integrated with dynamic lip movement analysis utilizing optical flow to develop a scalable anti-spoof VSA framework. We validated our model using the GRID audiovisual dataset, with spoofing attacks simulated via Wav2Lip for deepfake lip synchronization. The results demonstrate the model’s superior performance, evidenced by near-perfect classification accuracy and negligible error rates, addressing two key challenges of VSA: eliminating extensive training data while enabling rapid adaptation to unfamiliar speakers. Our approach significantly surpasses standard non-meta-learning approaches, substantiating its ability to address real-world scenarios.

</details>

#### [Warm Chat: Diffuse Emotion-aware Interactive Talking Head Avatar with Tree-Structured Guidance](https://arxiv.org/abs/2508.18337)
**Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian et al.** · 2025-08-25

<details>
<summary>Abstract</summary>

Generative models have advanced rapidly, enabling impressive talking head generation that brings AI to life. However, most existing methods focus solely on one-way portrait animation. Even the few that support bidirectional conversational interactions lack precise emotion-adaptive capabilities, significantly limiting their practical applicability. In this paper, we propose Warm Chat, a novel emotion-aware talking head generation framework for dyadic interactions. Leveraging the dialogue generation capability of large language models (LLMs, e.g., GPT-4), our method produces temporally consistent virtual avatars with rich emotional variations that seamlessly transition between speaking and listening states. Specifically, we design a Transformer-based head mask generator that learns temporally consistent motion features in a latent mask space, capable of generating arbitrary-length, temporally consistent mask sequences to constrain head motions. Furthermore, we introduce an interactive talking tree structure to represent dialogue state transitions, where each tree node contains information such as child/parent/sibling nodes and the current character's emotional state. By performing reverse-level traversal, we extract rich historical emotional cues from the current node to guide expression synthesis. Extensive experiments demonstrate the superior performance and effectiveness of our method.

</details>

#### [Lightning Fast Caching-based Parallel Denoising Prediction for Accelerating Talking Head Generation](https://arxiv.org/abs/2509.00052)
**Jianzhi Long, Wenhao Sun, Rongcheng Tu, Dacheng Tao** · 2025-08-25

<details>
<summary>Abstract</summary>

Diffusion-based talking head models generate high-quality, photorealistic videos but suffer from slow inference, limiting practical applications. Existing acceleration methods for general diffusion models fail to exploit the temporal and spatial redundancies unique to talking head generation. In this paper, we propose a task-specific framework addressing these inefficiencies through two key innovations. First, we introduce Lightning-fast Caching-based Parallel denoising prediction (LightningCP), caching static features to bypass most model layers in inference time. We also enable parallel prediction using cached features and estimated noisy latents as inputs, efficiently bypassing sequential sampling. Second, we propose Decoupled Foreground Attention (DFA) to further accelerate attention computations, exploiting the spatial decoupling in talking head videos to restrict attention to dynamic foreground regions. Additionally, we remove reference features in certain layers to bring extra speedup. Extensive experiments demonstrate that our framework significantly improves inference speed while preserving video quality.

</details>

#### [Taming Transformer for Emotion-Controllable Talking Face Generation](https://arxiv.org/abs/2508.14359)
**Ziqi Zhang, Cheng Deng** · 2025-08-20

<details>
<summary>Abstract</summary>

Talking face generation is a novel and challenging generation task, aiming at synthesizing a vivid speaking-face video given a specific audio. To fulfill emotion-controllable talking face generation, current methods need to overcome two challenges: One is how to effectively model the multimodal relationship related to the specific emotion, and the other is how to leverage this relationship to synthesize identity preserving emotional videos. In this paper, we propose a novel method to tackle the emotion-controllable talking face generation task discretely. Specifically, we employ two pre-training strategies to disentangle audio into independent components and quantize videos into combinations of visual tokens. Subsequently, we propose the emotion-anchor (EA) representation that integrates the emotional information into visual tokens. Finally, we introduce an autoregressive transformer to model the global distribution of the visual tokens under the given conditions and further predict the index sequence for synthesizing the manipulated videos. We conduct experiments on the MEAD dataset that controls the emotion of videos conditioned on multiple emotional audios. Extensive experiments demonstrate the superiorities of our method both qualitatively and quantitatively.

</details>

#### [RealTalk: Realistic Emotion-Aware Lifelike Talking-Head Synthesis](https://arxiv.org/abs/2508.12163)
**Wenqing Wang, Yun Fu** · 2025-08-16

<details>
<summary>Abstract</summary>

Emotion is a critical component of artificial social intelligence. However, while current methods excel in lip synchronization and image quality, they often fail to generate accurate and controllable emotional expressions while preserving the subject's identity. To address this challenge, we introduce RealTalk, a novel framework for synthesizing emotional talking heads with high emotion accuracy, enhanced emotion controllability, and robust identity preservation. RealTalk employs a variational autoencoder (VAE) to generate 3D facial landmarks from driving audio, which are concatenated with emotion-label embeddings using a ResNet-based landmark deformation model (LDM) to produce emotional landmarks. These landmarks and facial blendshape coefficients jointly condition a novel tri-plane attention Neural Radiance Field (NeRF) to synthesize highly realistic emotional talking heads. Extensive experiments demonstrate that RealTalk outperforms existing methods in emotion accuracy, controllability, and identity preservation, advancing the development of socially intelligent AI systems.

</details>

#### [SpeechForensics: Audio-Visual Speech Representation Learning for Face Forgery Detection](https://arxiv.org/abs/2508.09913)
**Yachao Liang, Min Yu, Gang Li, Jianguo Jiang et al.** · 2025-08-13

<details>
<summary>Abstract</summary>

Detection of face forgery videos remains a formidable challenge in the field of digital forensics, especially the generalization to unseen datasets and common perturbations. In this paper, we tackle this issue by leveraging the synergy between audio and visual speech elements, embarking on a novel approach through audio-visual speech representation learning. Our work is motivated by the finding that audio signals, enriched with speech content, can provide precise information effectively reflecting facial movements. To this end, we first learn precise audio-visual speech representations on real videos via a self-supervised masked prediction task, which encodes both local and global semantic information simultaneously. Then, the derived model is directly transferred to the forgery detection task. Extensive experiments demonstrate that our method outperforms the state-of-the-art methods in terms of cross-dataset generalization and robustness, without the participation of any fake video in model training. Code is available at https://github.com/Eleven4AI/SpeechForensics.

</details>

#### [Audio-Visual Speech Enhancement: Architectural Design and Deployment Strategies](https://arxiv.org/abs/2508.08468)
**Anis Hamadouche, Haifeng Luo, Mathini Sellathurai, Tharm Ratnarajah** · 2025-08-11

<details>
<summary>Abstract</summary>

This paper introduces a new AI-based Audio-Visual Speech Enhancement (AVSE) system and presents a comparative performance analysis of different deployment architectures. The proposed AVSE system employs convolutional neural networks (CNNs) for spectral feature extraction and long short-term memory (LSTM) networks for temporal modeling, enabling robust speech enhancement through multimodal fusion of audio and visual cues. Multiple deployment scenarios are investigated, including cloud-based, edge-assisted, and standalone device implementations. Their performance is evaluated in terms of speech quality improvement, latency, and computational overhead. Real-world experiments are conducted across various network conditions, including Ethernet, Wi-Fi, 4G, and 5G, to analyze the trade-offs between processing delay, communication latency, and perceptual speech quality. The results show that while cloud deployment achieves the highest enhancement quality, edge-assisted architectures offer the best balance between latency and intelligibility, meeting real-time requirements under 5G and Wi-Fi 6 conditions. These findings provide practical guidelines for selecting and optimizing AVSE deployment architectures in diverse applications, including assistive hearing devices, telepresence, and industrial communications.

</details>

#### [KLASSify to Verify: Audio-Visual Deepfake Detection Using SSL-based Audio and Handcrafted Visual Features](https://arxiv.org/abs/2508.07337)
**Ivan Kukanov, Jun Wah Ng** · 2025-08-10

<details>
<summary>Abstract</summary>

The rapid development of audio-driven talking head generators and advanced Text-To-Speech (TTS) models has led to more sophisticated temporal deepfakes. These advances highlight the need for robust methods capable of detecting and localizing deepfakes, even under novel, unseen attack scenarios. Current state-of-the-art deepfake detectors, while accurate, are often computationally expensive and struggle to generalize to novel manipulation techniques. To address these challenges, we propose multimodal approaches for the AV-Deepfake1M 2025 challenge. For the visual modality, we leverage handcrafted features to improve interpretability and adaptability. For the audio modality, we adapt a self-supervised learning (SSL) backbone coupled with graph attention networks to capture rich audio representations, improving detection robustness. Our approach strikes a balance between performance and real-world deployment, focusing on resilience and potential interpretability. On the AV-Deepfake1M++ dataset, our multimodal system achieves AUC of 92.78% for deepfake classification task and IoU of 0.3536 for temporal localization using only the audio modality.

</details>

#### [MotionSwap](https://arxiv.org/abs/2508.06430)
**Om Patil, Jinesh Modi, Suryabha Mukhopadhyay, Meghaditya Giri et al.** · 2025-08-08

<details>
<summary>Abstract</summary>

Face swapping technology has gained significant attention in both academic research and commercial applications. This paper presents our implementation and enhancement of SimSwap, an efficient framework for high fidelity face swapping. We introduce several improvements to the original model, including the integration of self and cross-attention mechanisms in the generator architecture, dynamic loss weighting, and cosine annealing learning rate scheduling. These enhancements lead to significant improvements in identity preservation, attribute consistency, and overall visual quality. Our experimental results, spanning 400,000 training iterations, demonstrate progressive improvements in generator and discriminator performance. The enhanced model achieves better identity similarity, lower FID scores, and visibly superior qualitative results compared to the baseline. Ablation studies confirm the importance of each architectural and training improvement. We conclude by identifying key future directions, such as integrating StyleGAN3, improving lip synchronization, incorporating 3D facial modeling, and introducing temporal consistency for video-based applications.

</details>

#### [RAP: Real-time Audio-driven Portrait Animation with Video Diffusion Transformer](https://arxiv.org/abs/2508.05115)
**Fangyu Du, Taiqing Li, Qian Qiao, Tan Yu et al.** · 2025-08-07

<details>
<summary>Abstract</summary>

Audio-driven portrait animation aims to synthesize realistic and natural talking head videos from an input audio signal and a single reference image. While existing methods achieve high-quality results by leveraging high-dimensional intermediate representations and explicitly modeling motion dynamics, their computational complexity renders them unsuitable for real-time deployment. Real-time inference imposes stringent latency and memory constraints, often necessitating the use of highly compressed latent representations. However, operating in such compact spaces hinders the preservation of fine-grained spatiotemporal details, thereby complicating audio-visual synchronization RAP (Real-time Audio-driven Portrait animation), a unified framework for generating high-quality talking portraits under real-time constraints. Specifically, RAP introduces a hybrid attention mechanism for fine-grained audio control, and a static-dynamic training-inference paradigm that avoids explicit motion supervision. Through these techniques, RAP achieves precise audio-driven control, mitigates long-term temporal drift, and maintains high visual fidelity. Extensive experiments demonstrate that RAP achieves state-of-the-art performance while operating under real-time constraints.

</details>

#### [READ: Real-time and Efficient Asynchronous Diffusion for Audio-driven Talking Head Generation](https://arxiv.org/abs/2508.03457)
**Haotian Wang, Yuzhe Weng, Jun Du, Haoran Xu et al.** · 2025-08-05

<details>
<summary>Abstract</summary>

The introduction of diffusion models has brought significant advances to the field of audio-driven talking head generation. However, the extremely slow inference speed severely limits the practical implementation of diffusion-based talking head generation models. In this study, we propose READ, a real-time diffusion-transformer-based talking head generation framework. Our approach first learns a spatiotemporal highly compressed video latent space via a temporal VAE, significantly reducing the token count to accelerate generation. To achieve better audio-visual alignment within this compressed latent space, a pre-trained Speech Autoencoder (SpeechAE) is proposed to generate temporally compressed speech latent codes corresponding to the video latent space. These latent representations are then modeled by a carefully designed Audio-to-Video Diffusion Transformer (A2V-DiT) backbone for efficient talking head synthesis. Furthermore, to ensure temporal consistency and accelerated inference in extended generation, we propose a novel asynchronous noise scheduler (ANS) for both the training and inference processes of our framework. The ANS leverages asynchronous add-noise and asynchronous motion-guided generation in the latent space, ensuring consistency in generated video clips. Experimental results demonstrate that READ outperforms state-of-the-art methods by generating competitive talking head videos with significantly reduced runtime, achieving an optimal balance between quality and speed while maintaining robust metric stability in long-time generation.

</details>

#### [X-Actor: Emotional and Expressive Long-Range Portrait Acting from Audio](https://arxiv.org/abs/2508.02944)
**Chenxu Zhang, Zenan Li, Hongyi Xu, You Xie et al.** · 2025-08-04

<details>
<summary>Abstract</summary>

We present X-Actor, a novel audio-driven portrait animation framework that generates lifelike, emotionally expressive talking head videos from a single reference image and an input audio clip. Unlike prior methods that emphasize lip synchronization and short-range visual fidelity in constrained speaking scenarios, X-Actor enables actor-quality, long-form portrait performance capturing nuanced, dynamically evolving emotions that flow coherently with the rhythm and content of speech. Central to our approach is a two-stage decoupled generation pipeline: an audio-conditioned autoregressive diffusion model that predicts expressive yet identity-agnostic facial motion latent tokens within a long temporal context window, followed by a diffusion-based video synthesis module that translates these motions into high-fidelity video animations. By operating in a compact facial motion latent space decoupled from visual and identity cues, our autoregressive diffusion model effectively captures long-range correlations between audio and facial dynamics through a diffusion-forcing training paradigm, enabling infinite-length emotionally-rich motion prediction without error accumulation. Extensive experiments demonstrate that X-Actor produces compelling, cinematic-style performances that go beyond standard talking head animations and achieves state-of-the-art results in long-range, audio-driven emotional portrait acting.

</details>

#### [Wav2Lip-HQ High-Resolution Audio-Driven Lip Synchronization for Realistic Virtual Avatars](https://www.semanticscholar.org/paper/aca90d844d61baac040a8cf612d00a5532f33d4b)
**Mallikarjuna G D** · 2025-07-31

<details>
<summary>Abstract</summary>

High-quality lip synchronization is essential for creating realistic talking face videos in applications such as virtual interviews, online education, film dubbing, and digital avatars. Traditional lip-sync methods often struggle with maintaining high visual fidelity, especially in high-resolution outputs. To address this challenge, Wav2Lip-HQ introduces an advanced Generative Adversarial Network (GAN)[1]-based solution capable of generating photorealistic, high-resolution lip-synced videos with accurate mouth movements synchronized to any given speech audio. In this research, we evaluate the performance of Wav2Lip-HQ, leveraging its core components, including the lipsync_gan.pth[1] model trained on the LRS2 dataset[1] for precise audio-visual synchronization, the face_segmentation.pth[2] model trained on CelebAMask-HQ for accurate facial region parsing, and the esrgan_max.pth[3] enhancer utilizing DIV2K[3] and CelebA[2] datasets to upscale and refine facial details post-synchronization. We conducted extensive experiments using diverse video-audio pairs to assess the improvement in lip-sync accuracy and overall video quality. Our analysis demonstrates that Wav2Lip-HQ significantly outperforms traditional methods and the original Wav2Lip model by delivering sharper, more coherent, and highly realistic talking face videos. The findings of this study confirm that Wav2Lip-HQ is an effective solution for high-resolution, photorealistic lip synchronization, making it highly applicable for real-world use cases requiring professional-grade video quality. Future work will focus on enhancing emotional expressions and optimizing performance for real-time applications.

</details>

#### [DiTalker: A Unified DiT-based Framework for High-Quality and Speaking Styles Controllable Portrait Animation](https://arxiv.org/abs/2508.06511)
**He Feng, Yongjia Ma, Donglin Di, Lei Fan et al.** · 2025-07-29

<details>
<summary>Abstract</summary>

Portrait animation aims to synthesize talking videos from a static reference face, conditioned on audio and style frame cues (e.g., emotion and head poses), while ensuring precise lip synchronization and faithful reproduction of speaking styles. Existing diffusion-based portrait animation methods primarily focus on lip synchronization or static emotion transformation, often overlooking dynamic styles such as head movements. Moreover, most of these methods rely on a dual U-Net architecture, which preserves identity consistency but incurs additional computational overhead. To this end, we propose DiTalker, a unified DiT-based framework for speaking style-controllable portrait animation. We design a Style-Emotion Encoding Module that employs two separate branches: a style branch extracting identity-specific style information (e.g., head poses and movements), and an emotion branch extracting identity-agnostic emotion features. We further introduce an Audio-Style Fusion Module that decouples audio and speaking styles via two parallel cross-attention layers, using these features to guide the animation process. To enhance the quality of results, we adopt and modify two optimization constraints: one to improve lip synchronization and the other to preserve fine-grained identity and background details. Extensive experiments demonstrate the superiority of DiTalker in terms of lip synchronization and speaking style controllability. Project Page: https://thenameishope.github.io/DiTalker/

</details>

#### [MagicAnime: A Hierarchically Annotated, Multimodal and Multitasking Dataset with Benchmarks for Cartoon Animation Generation](https://arxiv.org/abs/2507.20368)
**Shuolin Xu, Bingyuan Wang, Zeyu Cai, Fangteng Fu et al.** · 2025-07-27

<details>
<summary>Abstract</summary>

Generating high-quality cartoon animations multimodal control is challenging due to the complexity of non-human characters, stylistically diverse motions and fine-grained emotions. There is a huge domain gap between real-world videos and cartoon animation, as cartoon animation is usually abstract and has exaggerated motion. Meanwhile, public multimodal cartoon data are extremely scarce due to the difficulty of large-scale automatic annotation processes compared with real-life scenarios. To bridge this gap, We propose the MagicAnime dataset, a large-scale, hierarchically annotated, and multimodal dataset designed to support multiple video generation tasks, along with the benchmarks it includes. Containing 400k video clips for image-to-video generation, 50k pairs of video clips and keypoints for whole-body annotation, 12k pairs of video clips for video-to-video face animation, and 2.9k pairs of video and audio clips for audio-driven face animation. Meanwhile, we also build a set of multi-modal cartoon animation benchmarks, called MagicAnime-Bench, to support the comparisons of different methods in the tasks above. Comprehensive experiments on four tasks, including video-driven face animation, audio-driven face animation, image-to-video animation, and pose-driven character animation, validate its effectiveness in supporting high-fidelity, fine-grained, and controllable generation.

</details>

#### [Navigating Large-Pose Challenge for High-Fidelity Face Reenactment with Video Diffusion Model](https://arxiv.org/abs/2507.16341)
**Mingtao Guo, Guanyu Xing, Yanci Zhang, Yanli Liu** · 2025-07-22

<details>
<summary>Abstract</summary>

Face reenactment aims to generate realistic talking head videos by transferring motion from a driving video to a static source image while preserving the source identity. Although existing methods based on either implicit or explicit keypoints have shown promise, they struggle with large pose variations due to warping artifacts or the limitations of coarse facial landmarks. In this paper, we present the Face Reenactment Video Diffusion model (FRVD), a novel framework for high-fidelity face reenactment under large pose changes. Our method first employs a motion extractor to extract implicit facial keypoints from the source and driving images to represent fine-grained motion and to perform motion alignment through a warping module. To address the degradation introduced by warping, we introduce a Warping Feature Mapper (WFM) that maps the warped source image into the motion-aware latent space of a pretrained image-to-video (I2V) model. This latent space encodes rich priors of facial dynamics learned from large-scale video data, enabling effective warping correction and enhancing temporal coherence. Extensive experiments show that FRVD achieves superior performance over existing methods in terms of pose accuracy, identity preservation, and visual quality, especially in challenging scenarios with extreme pose variations.

</details>

#### [ATL-Diff: Audio-Driven Talking Head Generation with Early Landmarks-Guide Noise Diffusion](https://arxiv.org/abs/2507.12804)
**Hoang-Son Vo, Quang-Vinh Nguyen, Seungwon Kim, Hyung-Jeong Yang et al.** · 2025-07-17

<details>
<summary>Abstract</summary>

Audio-driven talking head generation requires precise synchronization between facial animations and audio signals. This paper introduces ATL-Diff, a novel approach addressing synchronization limitations while reducing noise and computational costs. Our framework features three key components: a Landmark Generation Module converting audio to facial landmarks, a Landmarks-Guide Noise approach that decouples audio by distributing noise according to landmarks, and a 3D Identity Diffusion network preserving identity characteristics. Experiments on MEAD and CREMA-D datasets demonstrate that ATL-Diff outperforms state-of-the-art methods across all metrics. Our approach achieves near real-time processing with high-quality animations, computational efficiency, and exceptional preservation of facial nuances. This advancement offers promising applications for virtual assistants, education, medical communication, and digital platforms. The source code is available at: \href{https://github.com/sonvth/ATL-Diff}{https://github.com/sonvth/ATL-Diff}

</details>

#### [Think-Before-Draw: Decomposing Emotion Semantics & Fine-Grained Controllable Expressive Talking Head Generation](https://arxiv.org/abs/2507.12761)
**Hanlei Shi, Leyuan Qu, Yu Liu, Di Gao et al.** · 2025-07-17

<details>
<summary>Abstract</summary>

Emotional talking-head generation has emerged as a pivotal research area at the intersection of computer vision and multimodal artificial intelligence, with its core value lying in enhancing human-computer interaction through immersive and empathetic engagement.With the advancement of multimodal large language models, the driving signals for emotional talking-head generation has shifted from audio and video to more flexible text. However, current text-driven methods rely on predefined discrete emotion label texts, oversimplifying the dynamic complexity of real facial muscle movements and thus failing to achieve natural emotional expressiveness.This study proposes the Think-Before-Draw framework to address two key challenges: (1) In-depth semantic parsing of emotions--by innovatively introducing Chain-of-Thought (CoT), abstract emotion labels are transformed into physiologically grounded facial muscle movement descriptions, enabling the mapping from high-level semantics to actionable motion features; and (2) Fine-grained expressiveness optimization--inspired by artists' portrait painting process, a progressive guidance denoising strategy is proposed, employing a "global emotion localization--local muscle control" mechanism to refine micro-expression dynamics in generated videos.Our experiments demonstrate that our approach achieves state-of-the-art performance on widely-used benchmarks, including MEAD and HDTF. Additionally, we collected a set of portrait images to evaluate our model's zero-shot generation capability.

</details>

#### [Detecting Deepfake Talking Heads from Facial Biometric Anomalies](https://arxiv.org/abs/2507.08917)
**Justin D. Norman, Hany Farid** · 2025-07-11

<details>
<summary>Abstract</summary>

The combination of highly realistic voice cloning, along with visually compelling avatar, face-swap, or lip-sync deepfake video generation, makes it relatively easy to create a video of anyone saying anything. Today, such deepfake impersonations are often used to power frauds, scams, and political disinformation. We propose a novel forensic machine learning technique for the detection of deepfake video impersonations that leverages unnatural patterns in facial biometrics. We evaluate this technique across a large dataset of deepfake techniques and impersonations, as well as assess its reliability to video laundering and its generalization to previously unseen video deepfake generators.

</details>

#### [MEDTalk: Multimodal Controlled 3D Facial Animation with Dynamic Emotions by Disentangled Embedding](https://arxiv.org/abs/2507.06071)
**Chang Liu, Ye Pan, Chenyang Ding, Susanto Rahardja et al.** · 2025-07-08

<details>
<summary>Abstract</summary>

Audio-driven emotional 3D facial animation aims to generate synchronized lip movements and vivid facial expressions. However, most existing approaches focus on static and predefined emotion labels, limiting their diversity and naturalness. To address these challenges, we propose MEDTalk, a novel framework for fine-grained and dynamic emotional talking head generation. Our approach first disentangles content and emotion embedding spaces from motion sequences using a carefully designed cross-reconstruction process, enabling independent control over lip movements and facial expressions. Beyond conventional audio-driven lip synchronization, we integrate audio and speech text, predicting frame-wise intensity variations and dynamically adjusting static emotion features to generate realistic emotional expressions. Furthermore, to enhance control and personalization, we incorporate multimodal inputs-including text descriptions and reference expression images-to guide the generation of user-specified facial expressions. With MetaHuman as the priority, our generated results can be conveniently integrated into the industrial production pipeline. The code is available at: https://github.com/SJTU-Lucy/MEDTalk.

</details>

#### [MoDiT: Learning Highly Consistent 3D Motion Coefficients with Diffusion Transformer for Talking Head Generation](https://arxiv.org/abs/2507.05092)
**Yucheng Wang, Dan Xu** · 2025-07-07

<details>
<summary>Abstract</summary>

Audio-driven talking head generation is critical for applications such as virtual assistants, video games, and films, where natural lip movements are essential. Despite progress in this field, challenges remain in producing both consistent and realistic facial animations. Existing methods, often based on GANs or UNet-based diffusion models, face three major limitations: (i) temporal jittering caused by weak temporal constraints, resulting in frame inconsistencies; (ii) identity drift due to insufficient 3D information extraction, leading to poor preservation of facial identity; and (iii) unnatural blinking behavior due to inadequate modeling of realistic blink dynamics. To address these issues, we propose MoDiT, a novel framework that combines the 3D Morphable Model (3DMM) with a Diffusion-based Transformer. Our contributions include: (i) A hierarchical denoising strategy with revised temporal attention and biased self/cross-attention mechanisms, enabling the model to refine lip synchronization and progressively enhance full-face coherence, effectively mitigating temporal jittering. (ii) The integration of 3DMM coefficients to provide explicit spatial constraints, ensuring accurate 3D-informed optical flow prediction and improved lip synchronization using Wav2Lip results, thereby preserving identity consistency. (iii) A refined blinking strategy to model natural eye movements, with smoother and more realistic blinking behaviors.

</details>

#### [MoDA: Multi-modal Diffusion Architecture for Talking Head Generation](https://arxiv.org/abs/2507.03256)
**Xinyang Li, Gen Li, Zhihui Lin, Yichen Qian et al.** · 2025-07-04

<details>
<summary>Abstract</summary>

Talking head generation with arbitrary identities and speech audio remains a crucial problem in the realm of the virtual metaverse. Recently, diffusion models have become a popular generative technique in this field with their strong generation capabilities. However, several challenges remain for diffusion-based methods: 1) inefficient inference and visual artifacts caused by the implicit latent space of Variational Auto-Encoders (VAE), which complicates the diffusion process; 2) a lack of authentic facial expressions and head movements due to inadequate multi-modal information fusion. In this paper, MoDA handles these challenges by: 1) defining a joint parameter space that bridges motion generation and neural rendering, and leveraging flow matching to simplify diffusion learning; 2) introducing a multi-modal diffusion architecture to model the interaction among noisy motion, audio, and auxiliary conditions, enhancing overall facial expressiveness. In addition, a coarse-to-fine fusion strategy is employed to progressively integrate different modalities, ensuring effective feature fusion. Experimental results demonstrate that MoDA improves video diversity, realism, and efficiency, making it suitable for real-world applications. Project Page: https://lixinyyang.github.io/MoDA.github.io/

</details>

#### [Multimodal Feature-Guided Audio-Driven Emotional Talking Face Generation](https://www.semanticscholar.org/paper/49c1bcd1d1eb546f2454dfaef7491897a1744a9c)
**Xueping Wang, Yuemeng Huo, Yanan Liu, Xueni Guo et al.** · 2025-07-02

<details>
<summary>Abstract</summary>

Audio-driven emotional talking face generation aims to generate talking face videos with rich facial expressions and temporal coherence. Current diffusion model-based approaches predominantly depend on either single-label emotion annotations or external video references, which often struggle to capture the complex relationships between modalities, resulting in less natural emotional expressions. To address these issues, we propose MF-ETalk, a multimodal feature-guided method for emotional talking face generation. Specifically, we design an emotion-aware multimodal feature disentanglement and fusion framework that leverages Action Units (AUs) to disentangle facial expressions and models the nonlinear relationships among AU features using a residual encoder. Furthermore, we introduce a hierarchical multimodal feature fusion module that enables dynamic interactions among audio, visual cues, AUs, and motion dynamics. This module is optimized through global motion modeling, lip synchronization, and expression subspace learning, enabling full-face dynamic generation. Finally, an emotion-consistency constraint module is employed to refine the generated results and ensure the naturalness of expressions. Extensive experiments on the MEAD and HDTF datasets demonstrate that MF-ETalk outperforms state-of-the-art methods in both expression naturalness and lip-sync accuracy. For example, it achieves an FID of 43.052 and E-FID of 2.403 on MEAD, along with strong synchronization performance (LSE-C of 6.781, LSE-D of 7.962), confirming the effectiveness of our approach in producing realistic and emotionally expressive talking face videos.

</details>

#### [JAM-Flow: Joint Audio-Motion Synthesis with Flow Matching](https://arxiv.org/abs/2506.23552)
**Mingi Kwon, Joonghyuk Shin, Jaeseok Jung, Jaesik Park et al.** · 2025-06-30

<details>
<summary>Abstract</summary>

The intrinsic link between facial motion and speech is often overlooked in generative modeling, where talking head synthesis and text-to-speech (TTS) are typically addressed as separate tasks. This paper introduces JAM-Flow, a unified framework to simultaneously synthesize and condition on both facial motion and speech. Our approach leverages flow matching and a novel Multi-Modal Diffusion Transformer (MM-DiT) architecture, integrating specialized Motion-DiT and Audio-DiT modules. These are coupled via selective joint attention layers and incorporate key architectural choices, such as temporally aligned positional embeddings and localized joint attention masking, to enable effective cross-modal interaction while preserving modality-specific strengths. Trained with an inpainting-style objective, JAM-Flow supports a wide array of conditioning inputs-including text, reference audio, and reference motion-facilitating tasks such as synchronized talking head generation from text, audio-driven animation, and much more, within a single, coherent model. JAM-Flow significantly advances multi-modal generative modeling by providing a practical solution for holistic audio-visual synthesis. project page: https://joonghyuk.com/jamflow-web

</details>

#### [ConAvatar: Harnessing Facial Mesh for Controllable Avatar Animation](https://www.semanticscholar.org/paper/a862f36ce73d574aad5b4a06f70f05e440acc3f5)
**Zheng Tan, Wei Wei** · 2025-06-30

<details>
<summary>Abstract</summary>

Recent advancements in talking head generation have focused on temporal consistency and lip-sync accuracy, but controlling the head pose remains a challenge. Existing methods often rely on reference videos or random generation, leading to unrealistic results. In this paper, we propose ConAvatar, a novel framework that enables precise control over head pose while generating realistic talking heads. Our approach consists of two stages: first, converting control information (Euler angles and position) into 3D facial meshes; second, using these structured information to guide a diffusion model for realistic video generation. This allows the talking head to move in sync with both speech and pose, ensuring natural, controlled head movements. Extensive experiments show that our method delivers high-quality results with improved temporal consistency, accurate lip-sync, and controllable head pose, effectively demonstrating the validity and effectiveness of our approach in realistic talking head synthesis.

</details>

#### [EmoHuman: Fine-Grained Emotion-Controlled Talking Head Generation via Audio-Text Multimodal Detangling](https://www.semanticscholar.org/paper/001006557262952b7a5d58265206618f486d6ed6)
**Qifeng Dai, Huidong Feng, Wendi Cui, Xinqi Cai et al.** · 2025-06-30

<details>
<summary>Abstract</summary>

Audio-driven talking head generation has made significant strides in creating realistic and lip-synchronized portraits. However, most existing approaches overlook facial expressions, with only a few attempting to model facial emotions explicitly, often leading to unnatural results. To address this gap, we introduce EmoHuman, an audio-to-video synthesis method that generates emotionally nuanced talking head videos without relying on intermediate 3D representations or facial landmarks. EmoHuman decouples content, emotion, and emotional intensity from the multimodal information of the audio and the corresponding textual content through an Audio Emotion Decoupling Module. The content features are used to drive a powerful video diffusion model, generating synchronized lip movements, while emotion and emotional intensity govern the simulation of facial expressions, resulting in more realistic video outputs. Extensive experiments demonstrate that EmoHuman outperforms state-of-the-art methods in image and video quality, expression correlation, and lip-synchronization accuracy.

</details>

#### [GE-Talker: Generalizable and Efficient Neural Rendering for Talking Head Generation](https://www.semanticscholar.org/paper/ab7592118a4e5ba323dd9be80ba30f2ce810347f)
**Zixuan Wang, Li Fang, Fei Hu, L. Ye** · 2025-06-30

<details>
<summary>Abstract</summary>

Talking head generation aims to create videos that preserve a source character’s identity while replicating synchronized lip movements, facial expressions, and head gestures from audio inputs. While personalized methods have achieved impressive results by training neural radiance fields (NeRFs) for specific identities, they often face limitations in generalization and incur high computational costs due to identity-specific retraining. We propose GE-Talker, a Generalizable and Efficient NeRF for talking head generation, which addresses these challenges through two key innovations. First, we leverage FLAME-based full-head modeling as intermediate representations, conditioned on audio features, to achieve precise lip synchronization and natural facial movements. Second, we introduce a semantic-aware depth-guided sampling strategy that uses FLAME-generated depth maps to restrict sampling ranges and semantic segmentation to focus on human regions, improving rendering quality and efficiency. GE-Talker achieves high-quality outputs for unseen speaker identities with a 109% speed-up over baseline methods and enables rapid fine-tuning on new speakers within 14 minutes, establishing it as a powerful and adaptable solution for talking head generation.

</details>

#### [Audio-Driven Emotion-Aware 3D Talking Face Generation from Single Image](https://www.semanticscholar.org/paper/9fde057351c2841cfd3b47d3ed719e1b4f0012e2)
**Chun-Shuo Qiu, Feng-Lin Liu, Hongbo Fu, Fan Zhang et al.** · 2025-06-30

<details>
<summary>Abstract</summary>

Audio-driven talking face generation from a single source image is a popular research topic. There still exist many challenges for its practical applications, e.g., diverse motion generation, effective emotional control, and large view angle changes. In this work, we propose a novel one-shot emotion-controllable audio-driven 3D talking face generation framework, which creates free-view talking videos from one reference image. Firstly, to synchronize the motion with the input audio, we use a transformer-based motion generator to capture the context of the input audio and predict motion coefficient sequences, which are leveraged by a motion encoder to extract motion codes. Meanwhile, to reconstruct a 3D portrait from one reference image, an identity encoder is utilized to extract an identity code and generate emotion-dependent appearance with a specific emotion label. Finally, we introduce an emotion-controllable 3D portrait video generator to synthesize free-view talking videos using the disentangled motion and identity codes. Thanks to the audio-synchronized motion codes and emotion-aware identity code, we can render a talking face with realistic emotional expressions in novel views. Extensive experiments show that our method is capable of maintaining superior visual performance and motion accuracy in both front view and novel views.

</details>

#### [Few-Shot Identity Adaptation for 3D Talking Heads via Global Gaussian Field](https://arxiv.org/abs/2506.22044)
**Hong Nie, Fuyuan Cao, Lu Chen, Fengxin Chen et al.** · 2025-06-27

<details>
<summary>Abstract</summary>

Reconstruction and rendering-based talking head synthesis methods achieve high-quality results with strong identity preservation but are limited by their dependence on identity-specific models. Each new identity requires training from scratch, incurring high computational costs and reduced scalability compared to generative model-based approaches. To overcome this limitation, we propose FIAG, a novel 3D speaking head synthesis framework that enables efficient identity-specific adaptation using only a few training footage. FIAG incorporates Global Gaussian Field, which supports the representation of multiple identities within a shared field, and Universal Motion Field, which captures the common motion dynamics across diverse identities. Benefiting from the shared facial structure information encoded in the Global Gaussian Field and the general motion priors learned in the motion field, our framework enables rapid adaptation from canonical identity representations to specific ones with minimal data. Extensive comparative and ablation experiments demonstrate that our method outperforms existing state-of-the-art approaches, validating both the effectiveness and generalizability of the proposed framework. Code is available at: \textit{https://github.com/gme-hong/FIAG}.

</details>

#### [Advancing Talking Head Generation: A Comprehensive Survey of Multi-Modal Methodologies, Datasets, Evaluation Metrics, and Loss Functions](https://arxiv.org/abs/2507.02900)
**Vineet Kumar Rakesh, Soumya Mazumdar, Research Pratim Maity, Sarbajit Pal et al.** · 2025-06-23

<details>
<summary>Abstract</summary>

Talking Head Generation (THG) has emerged as a transformative technology in computer vision, enabling the synthesis of realistic human faces synchronized with image, audio, text, or video inputs. This paper provides a comprehensive review of methodologies and frameworks for talking head generation, categorizing approaches into 2D--based, 3D--based, Neural Radiance Fields (NeRF)--based, diffusion--based, parameter-driven techniques and many other techniques. It evaluates algorithms, datasets, and evaluation metrics while highlighting advancements in perceptual realism and technical efficiency critical for applications such as digital avatars, video dubbing, ultra-low bitrate video conferencing, and online education. The study identifies challenges such as reliance on pre--trained models, extreme pose handling, multilingual synthesis, and temporal consistency. Future directions include modular architectures, multilingual datasets, hybrid models blending pre--trained and task-specific layers, and innovative loss functions. By synthesizing existing research and exploring emerging trends, this paper aims to provide actionable insights for researchers and practitioners in the field of talking head generation. For the complete survey, code, and curated resource list, visit our GitHub repository: https://github.com/VineetKumarRakesh/thg.

</details>

#### [Compressed Video Super-Resolution based on Hierarchical Encoding](https://arxiv.org/abs/2506.14381)
**Yuxuan Jiang, Siyue Teng, Qiang Zhu, Chen Feng et al.** · 2025-06-17

<details>
<summary>Abstract</summary>

This paper presents a general-purpose video super-resolution (VSR) method, dubbed VSR-HE, specifically designed to enhance the perceptual quality of compressed content. Targeting scenarios characterized by heavy compression, the method upscales low-resolution videos by a ratio of four, from 180p to 720p or from 270p to 1080p. VSR-HE adopts hierarchical encoding transformer blocks and has been sophisticatedly optimized to eliminate a wide range of compression artifacts commonly introduced by H.265/HEVC encoding across various quantization parameter (QP) levels. To ensure robustness and generalization, the model is trained and evaluated under diverse compression settings, allowing it to effectively restore fine-grained details and preserve visual fidelity. The proposed VSR-HE has been officially submitted to the ICME 2025 Grand Challenge on VSR for Video Conferencing (Team BVI-VSR), under both the Track 1 (General-Purpose Real-World Video Content) and Track 2 (Talking Head Videos).

</details>

#### [Audio-Visual Driven Compression for Low-Bitrate Talking Head Videos](https://arxiv.org/abs/2506.13419)
**Riku Takahashi, Ryugo Morita, Jinjia Zhou** · 2025-06-16

<details>
<summary>Abstract</summary>

Talking head video compression has advanced with neural rendering and keypoint-based methods, but challenges remain, especially at low bit rates, including handling large head movements, suboptimal lip synchronization, and distorted facial reconstructions. To address these problems, we propose a novel audio-visual driven video codec that integrates compact 3D motion features and audio signals. This approach robustly models significant head rotations and aligns lip movements with speech, improving both compression efficiency and reconstruction quality. Experiments on the CelebV-HQ dataset show that our method reduces bitrate by 22% compared to VVC and by 8.5% over state-of-the-art learning-based codec. Furthermore, it provides superior lip-sync accuracy and visual fidelity at comparable bitrates, highlighting its effectiveness in bandwidth-constrained scenarios.

</details>

#### [Viseme Morphing and Text-to-Speech Integration for Indonesian News Broadcasting](https://www.semanticscholar.org/paper/de6942a79eaf13d3334a57729f09995a4851f822)
**Mirza Ardiana** · 2025-06-16

<details>
<summary>Abstract</summary>

Advancements in multimedia technology and artificial intelligence have driven innovation in digital broadcasting, including virtual newsreaders. This study proposes a text-to-speech-based lip-sync animation system specifically for the Indonesian language to improve synchronization between lip movements and speech. The primary challenge in developing this system lies in generating realistic lip animations that correspond with the phonetic structure of Indonesian. The system workflow involves text input, syllable parsing using the Finite State Automata (FSA) method, viseme conversion (viseme morphing), and web-based animation output. Test results show a viseme duration accuracy of 98.5%, voice-lip movement synchronization of 94.26%, and a Mean Opinion Score (MOS) of 77.12%, indicating that the system is reasonably feasible for implementation. Despite minor delays, the system demonstrates strong potential for further development through the integration of Natural Language Processing (NLP) and deep learning, which could improve viseme mapping accuracy and enhance system flexibility across various digital broadcasting platforms.

</details>

#### [ICME 2025 Grand Challenge on Video Super-Resolution for Video Conferencing](https://arxiv.org/abs/2506.12269)
**Babak Naderi, Ross Cutler, Juhee Cho, Nabakumar Khongbantabam et al.** · 2025-06-13

<details>
<summary>Abstract</summary>

Super-Resolution (SR) is a critical task in computer vision, focusing on reconstructing high-resolution (HR) images from low-resolution (LR) inputs. The field has seen significant progress through various challenges, particularly in single-image SR. Video Super-Resolution (VSR) extends this to the temporal domain, aiming to enhance video quality using methods like local, uni-, bi-directional propagation, or traditional upscaling followed by restoration. This challenge addresses VSR for conferencing, where LR videos are encoded with H.265 at fixed QPs. The goal is to upscale videos by a specific factor, providing HR outputs with enhanced perceptual quality under a low-delay scenario using causal models. The challenge included three tracks: general-purpose videos, talking head videos, and screen content videos, with separate datasets provided by the organizers for training, validation, and testing. We open-sourced a new screen content dataset for the SR task in this challenge. Submissions were evaluated through subjective tests using a crowdsourced implementation of the ITU-T Rec P.910.

</details>

#### [HunyuanVideo-HOMA: Generic Human-Object Interaction in Multimodal Driven Human Animation](https://arxiv.org/abs/2506.08797)
**Ziyao Huang, Zixiang Zhou, Juan Cao, Yifeng Ma et al.** · 2025-06-10

<details>
<summary>Abstract</summary>

To address key limitations in human-object interaction (HOI) video generation -- specifically the reliance on curated motion data, limited generalization to novel objects/scenarios, and restricted accessibility -- we introduce HunyuanVideo-HOMA, a weakly conditioned multimodal-driven framework. HunyuanVideo-HOMA enhances controllability and reduces dependency on precise inputs through sparse, decoupled motion guidance. It encodes appearance and motion signals into the dual input space of a multimodal diffusion transformer (MMDiT), fusing them within a shared context space to synthesize temporally consistent and physically plausible interactions. To optimize training, we integrate a parameter-space HOI adapter initialized from pretrained MMDiT weights, preserving prior knowledge while enabling efficient adaptation, and a facial cross-attention adapter for anatomically accurate audio-driven lip synchronization. Extensive experiments confirm state-of-the-art performance in interaction naturalness and generalization under weak supervision. Finally, HunyuanVideo-HOMA demonstrates versatility in text-conditioned generation and interactive object manipulation, supported by a user-friendly demo interface. The project page is at https://anonymous.4open.science/w/homa-page-0FBE/.

</details>

#### [Hallo4: High-Fidelity Dynamic Portrait Animation via Direct Preference Optimization](https://arxiv.org/abs/2505.23525)
**Jiahao Cui, Yan Chen, Mingwang Xu, Hanlin Shang et al.** · 2025-05-29

<details>
<summary>Abstract</summary>

Generating highly dynamic and photorealistic portrait animations driven by audio and skeletal motion remains challenging due to the need for precise lip synchronization, natural facial expressions, and high-fidelity body motion dynamics. We propose a human-preference-aligned diffusion framework that addresses these challenges through two key innovations. First, we introduce direct preference optimization tailored for human-centric animation, leveraging a curated dataset of human preferences to align generated outputs with perceptual metrics for portrait motion-video alignment and naturalness of expression. Second, the proposed temporal motion modulation resolves spatiotemporal resolution mismatches by reshaping motion conditions into dimensionally aligned latent features through temporal channel redistribution and proportional feature expansion, preserving the fidelity of high-frequency motion details in diffusion-based synthesis. The proposed mechanism is complementary to existing UNet and DiT-based portrait diffusion approaches, and experiments demonstrate obvious improvements in lip-audio synchronization, expression vividness, body motion coherence over baseline methods, alongside notable gains in human preference metrics. Our model and source code can be found at: https://github.com/fudan-generative-vision/hallo4.

</details>

#### [FaceEditTalker: Controllable Talking Head Generation with Facial Attribute Editing](https://arxiv.org/abs/2505.22141)
**Guanwen Feng, Zhiyuan Ma, Yunan Li, Jiahao Yang et al.** · 2025-05-28

<details>
<summary>Abstract</summary>

Recent advances in audio-driven talking head generation have achieved impressive results in lip synchronization and emotional expression. However, they largely overlook the crucial task of facial attribute editing. This capability is indispensable for achieving deep personalization and expanding the range of practical applications, including user-tailored digital avatars, engaging online education content, and brand-specific digital customer service. In these key domains, flexible adjustment of visual attributes, such as hairstyle, accessories, and subtle facial features, is essential for aligning with user preferences, reflecting diverse brand identities and adapting to varying contextual demands. In this paper, we present FaceEditTalker, a unified framework that enables controllable facial attribute manipulation while generating high-quality, audio-synchronized talking head videos. Our method consists of two key components: an image feature space editing module, which extracts semantic and detail features and allows flexible control over attributes like expression, hairstyle, and accessories; and an audio-driven video generation module, which fuses these edited features with audio-guided facial landmarks to drive a diffusion-based generator. This design ensures temporal coherence, visual fidelity, and identity preservation across frames. Extensive experiments on public datasets demonstrate that our method achieves comparable or superior performance to representative baseline methods in lip-sync accuracy, video quality, and attribute controllability. Project page: https://peterfanfan.github.io/FaceEditTalker/

</details>

#### [OmniSync: Towards Universal Lip Synchronization via Diffusion Transformers](https://arxiv.org/abs/2505.21448)
**Ziqiao Peng, Jiwen Liu, Haoxian Zhang, Xiaoqiang Liu et al.** · 2025-05-27

<details>
<summary>Abstract</summary>

Lip synchronization is the task of aligning a speaker's lip movements in video with corresponding speech audio, and it is essential for creating realistic, expressive video content. However, existing methods often rely on reference frames and masked-frame inpainting, which limit their robustness to identity consistency, pose variations, facial occlusions, and stylized content. In addition, since audio signals provide weaker conditioning than visual cues, lip shape leakage from the original video will affect lip sync quality. In this paper, we present OmniSync, a universal lip synchronization framework for diverse visual scenarios. Our approach introduces a mask-free training paradigm using Diffusion Transformer models for direct frame editing without explicit masks, enabling unlimited-duration inference while maintaining natural facial dynamics and preserving character identity. During inference, we propose a flow-matching-based progressive noise initialization to ensure pose and identity consistency, while allowing precise mouth-region editing. To address the weak conditioning signal of audio, we develop a Dynamic Spatiotemporal Classifier-Free Guidance (DS-CFG) mechanism that adaptively adjusts guidance strength over time and space. We also establish the AIGC-LipSync Benchmark, the first evaluation suite for lip synchronization in diverse AI-generated videos. Extensive experiments demonstrate that OmniSync significantly outperforms prior methods in both visual quality and lip sync accuracy, achieving superior results in both real-world and AI-generated videos.

</details>

#### [Total-Editing: Head Avatar with Editable Appearance, Motion, and Lighting](https://arxiv.org/abs/2505.20582)
**Yizhou Zhao, Chunjiang Liu, Haoyu Chen, Bhiksha Raj et al.** · 2025-05-26

<details>
<summary>Abstract</summary>

Face reenactment and portrait relighting are essential tasks in portrait editing, yet they are typically addressed independently, without much synergy. Most face reenactment methods prioritize motion control and multiview consistency, while portrait relighting focuses on adjusting shading effects. To take advantage of both geometric consistency and illumination awareness, we introduce Total-Editing, a unified portrait editing framework that enables precise control over appearance, motion, and lighting. Specifically, we design a neural radiance field decoder with intrinsic decomposition capabilities. This allows seamless integration of lighting information from portrait images or HDR environment maps into synthesized portraits. We also incorporate a moving least squares based deformation field to enhance the spatiotemporal coherence of avatar motion and shading effects. With these innovations, our unified framework significantly improves the quality and realism of portrait editing results. Further, the multi-source nature of Total-Editing supports more flexible applications, such as illumination transfer from one portrait to another, or portrait animation with customized backgrounds.

</details>

#### [Research on lip synthesis of virtual digital humans based on the Spark large model](https://www.semanticscholar.org/paper/4d808178b1a61adeb25368223adf92728e46cd5c)
**Yuqi Huang** · 2025-05-09

<details>
<summary>Abstract</summary>

In recent years, with the support of key technologies such as deep learning algorithms, computer vision, natural language processing, and graphics rendering, the production process of virtual digital humans has achieved revolutionary breakthroughs. Lip synthesis technology, as a crucial component, has also garnered widespread attention. Most existing lip synthesis models are trained on English datasets, resulting in poor synthesis effects in Chinese contexts. This paper, based on the study of the Wav2Lip lip synthesis model, constructs a Chinese lip-sync dataset and conducts a series of training fine-tunings to achieve better synthesis effects. By leveraging the multimodal capabilities of the Spark large model, it realizes efficient speech-driven facial animation generation. Furthermore, this paper explores the application potential of the Wav2Lip model, providing a solid theoretical foundation and technical support for future commercial applications.

</details>

#### [OXSeg: Multidimensional attention UNet-based lip segmentation using semi-supervised lip contours](https://arxiv.org/abs/2505.05531)
**Hanie Moghaddasi, Christina Chambers, Sarah N. Mattson, Jeffrey R. Wozniak et al.** · 2025-05-08

<details>
<summary>Abstract</summary>

Lip segmentation plays a crucial role in various domains, such as lip synchronization, lipreading, and diagnostics. However, the effectiveness of supervised lip segmentation is constrained by the availability of lip contour in the training phase. A further challenge with lip segmentation is its reliance on image quality , lighting, and skin tone, leading to inaccuracies in the detected boundaries. To address these challenges, we propose a sequential lip segmentation method that integrates attention UNet and multidimensional input. We unravel the micro-patterns in facial images using local binary patterns to build multidimensional inputs. Subsequently, the multidimensional inputs are fed into sequential attention UNets, where the lip contour is reconstructed. We introduce a mask generation method that uses a few anatomical landmarks and estimates the complete lip contour to improve segmentation accuracy. This mask has been utilized in the training phase for lip segmentation. To evaluate the proposed method, we use facial images to segment the upper lips and subsequently assess lip-related facial anomalies in subjects with fetal alcohol syndrome (FAS). Using the proposed lip segmentation method, we achieved a mean dice score of 84.75%, and a mean pixel accuracy of 99.77% in upper lip segmentation. To further evaluate the method, we implemented classifiers to identify those with FAS. Using a generative adversarial network (GAN), we reached an accuracy of 98.55% in identifying FAS in one of the study populations. This method could be used to improve lip segmentation accuracy, especially around Cupid's bow, and shed light on distinct lip-related characteristics of FAS.

</details>

#### [OT-Talk: Animating 3D Talking Head with Optimal Transportation](https://arxiv.org/abs/2505.01932)
**Xinmu Wang, Xiang Gao, Xiyun Song, Heather Yu et al.** · 2025-05-03

<details>
<summary>Abstract</summary>

Animating 3D head meshes using audio inputs has significant applications in AR/VR, gaming, and entertainment through 3D avatars. However, bridging the modality gap between speech signals and facial dynamics remains a challenge, often resulting in incorrect lip syncing and unnatural facial movements. To address this, we propose OT-Talk, the first approach to leverage optimal transportation to optimize the learning model in talking head animation. Building on existing learning frameworks, we utilize a pre-trained Hubert model to extract audio features and a transformer model to process temporal sequences. Unlike previous methods that focus solely on vertex coordinates or displacements, we introduce Chebyshev Graph Convolution to extract geometric features from triangulated meshes. To measure mesh dissimilarities, we go beyond traditional mesh reconstruction errors and velocity differences between adjacent frames. Instead, we represent meshes as probability measures and approximate their surfaces. This allows us to leverage the sliced Wasserstein distance for modeling mesh variations. This approach facilitates the learning of smooth and accurate facial motions, resulting in coherent and natural facial animations. Our experiments on two public audio-mesh datasets demonstrate that our method outperforms state-of-the-art techniques both quantitatively and qualitatively in terms of mesh reconstruction accuracy and temporal alignment. In addition, we conducted a user perception study with 20 volunteers to further assess the effectiveness of our approach.

</details>

#### [Model See Model Do: Speech-Driven Facial Animation with Style Control](https://arxiv.org/abs/2505.01319)
**Yifang Pan, Karan Singh, Luiz Gustavo Hafemann** · 2025-05-02

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation plays a key role in applications such as virtual avatars, gaming, and digital content creation. While existing methods have made significant progress in achieving accurate lip synchronization and generating basic emotional expressions, they often struggle to capture and effectively transfer nuanced performance styles. We propose a novel example-based generation framework that conditions a latent diffusion model on a reference style clip to produce highly expressive and temporally coherent facial animations. To address the challenge of accurately adhering to the style reference, we introduce a novel conditioning mechanism called style basis, which extracts key poses from the reference and additively guides the diffusion generation process to fit the style without compromising lip synchronization quality. This approach enables the model to capture subtle stylistic cues while ensuring that the generated animations align closely with the input speech. Extensive qualitative, quantitative, and perceptual evaluations demonstrate the effectiveness of our method in faithfully reproducing the desired style while achieving superior lip synchronization across various speech scenarios.

</details>

#### [Audio-Driven Talking Face Generation With Segmented Static Facial References for Customized Health Device Interactions](https://www.semanticscholar.org/paper/dc0087781c32ad17f315f856e42f53af965bb8c3)
**Zige Wang, Yashuai Wang, Tianyu Liu, Peng Zhang et al.** · 2025-05-01

<details>
<summary>Abstract</summary>

In a variety of human-machine interaction (HMI) applications, the high-level techniques based on audio-driven talking face generation are often challenged by the issues of temporal misalignment and low-quality outputs. Recent solutions have sought to improve synchronization by maximizing the similarity between audio-visual pairs. However, the temporal disturbances introduced during the inference phase continue to limit the enhancement of generative performance. Inspired by the intrinsic connection between the segmented static facial image and the stable appearance representation, in this study, two strategies, Manual Temporal Segmentation (MTS) and Static Facial Reference (SFR), are proposed to improve performance during the inference stage. The corresponding functionality consists of: MTS involves segmenting the input video into several clips, effectively reducing the complexity of the inference process, and SFR utilizes static facial references to mitigate the temporal noise generated by dynamic sequences, thereby enhancing the quality of the generated outputs. Substantial experiments on the LRS2 and VoxCeleb2 datasets have demonstrated that the proposed strategies are able to significantly enhance inference performance with the LSE-C and LSE-D metrics, without altering the network architecture or training strategy. For effectiveness validation in realistic scenario applications, a deployment has also been conducted on the healthcare devices with the proposed solution.

</details>

#### [MagicPortrait: Temporally Consistent Face Reenactment with 3D Geometric Guidance](https://arxiv.org/abs/2504.21497)
**Mengting Wei, Yante Li, Tuomas Varanka, Yan Jiang et al.** · 2025-04-30

<details>
<summary>Abstract</summary>

In this study, we propose a method for video face reenactment that integrates a 3D face parametric model into a latent diffusion framework, aiming to improve shape consistency and motion control in existing video-based face generation approaches. Our approach employs the FLAME (Faces Learned with an Articulated Model and Expressions) model as the 3D face parametric representation, providing a unified framework for modeling face expressions and head pose. This not only enables precise extraction of motion features from driving videos, but also contributes to the faithful preservation of face shape and geometry. Specifically, we enhance the latent diffusion model with rich 3D expression and detailed pose information by incorporating depth maps, normal maps, and rendering maps derived from FLAME sequences. These maps serve as motion guidance and are encoded into the denoising UNet through a specifically designed Geometric Guidance Encoder (GGE). A multi-layer feature fusion module with integrated self-attention mechanisms is used to combine facial appearance and motion latent features within the spatial domain. By utilizing the 3D face parametric model as motion guidance, our method enables parametric alignment of face identity between the reference image and the motion captured from the driving video. Experimental results on benchmark datasets show that our method excels at generating high-quality face animations with precise expression and head pose variation modeling. In addition, it demonstrates strong generalization performance on out-of-domain images. Code is publicly available at https://github.com/weimengting/MagicPortrait.

</details>

#### [IM-Portrait: Learning 3D-aware Video Diffusion for Photorealistic Talking Heads from Monocular Videos](https://arxiv.org/abs/2504.19165)
**Yuan Li, Ziqian Bai, Feitong Tan, Zhaopeng Cui et al.** · 2025-04-27

<details>
<summary>Abstract</summary>

We propose a novel 3D-aware diffusion-based method for generating photorealistic talking head videos directly from a single identity image and explicit control signals (e.g., expressions). Our method generates Multiplane Images (MPIs) that ensure geometric consistency, making them ideal for immersive viewing experiences like binocular videos for VR headsets. Unlike existing methods that often require a separate stage or joint optimization to reconstruct a 3D representation (such as NeRF or 3D Gaussians), our approach directly generates the final output through a single denoising process, eliminating the need for post-processing steps to render novel views efficiently. To effectively learn from monocular videos, we introduce a training mechanism that reconstructs the output MPI randomly in either the target or the reference camera space. This approach enables the model to simultaneously learn sharp image details and underlying 3D information. Extensive experiments demonstrate the effectiveness of our method, which achieves competitive avatar quality and novel-view rendering capabilities, even without explicit 3D reconstruction or high-quality multi-view training data.

</details>

#### [Disentangle Identity, Cooperate Emotion: Correlation-Aware Emotional Talking Portrait Generation](https://arxiv.org/abs/2504.18087)
**Weipeng Tan, Chuming Lin, Chengming Xu, FeiFan Xu et al.** · 2025-04-25

<details>
<summary>Abstract</summary>

Recent advances in Talking Head Generation (THG) have achieved impressive lip synchronization and visual quality through diffusion models; yet existing methods struggle to generate emotionally expressive portraits while preserving speaker identity. We identify three critical limitations in current emotional talking head generation: insufficient utilization of audio's inherent emotional cues, identity leakage in emotion representations, and isolated learning of emotion correlations. To address these challenges, we propose a novel framework dubbed as DICE-Talk, following the idea of disentangling identity with emotion, and then cooperating emotions with similar characteristics. First, we develop a disentangled emotion embedder that jointly models audio-visual emotional cues through cross-modal attention, representing emotions as identity-agnostic Gaussian distributions. Second, we introduce a correlation-enhanced emotion conditioning module with learnable Emotion Banks that explicitly capture inter-emotion relationships through vector quantization and attention-based feature aggregation. Third, we design an emotion discrimination objective that enforces affective consistency during the diffusion process through latent-space classification. Extensive experiments on MEAD and HDTF datasets demonstrate our method's superiority, outperforming state-of-the-art approaches in emotion accuracy while maintaining competitive lip-sync performance. Qualitative results and user studies further confirm our method's ability to generate identity-preserving portraits with rich, correlated emotional expressions that naturally adapt to unseen identities.

</details>

#### [Supervising 3D Talking Head Avatars with Analysis-by-Audio-Synthesis](https://arxiv.org/abs/2504.13386)
**Radek Daněček, Carolin Schmitt, Senya Polikovsky, Michael J. Black** · 2025-04-18

<details>
<summary>Abstract</summary>

In order to be widely applicable, speech-driven 3D head avatars must articulate their lips in accordance with speech, while also conveying the appropriate emotions with dynamically changing facial expressions. The key problem is that deterministic models produce high-quality lip-sync but without rich expressions, whereas stochastic models generate diverse expressions but with lower lip-sync quality. To get the best of both, we seek a stochastic model with accurate lip-sync. To that end, we develop a new approach based on the following observation: if a method generates realistic 3D lip motions, it should be possible to infer the spoken audio from the lip motion. The inferred speech should match the original input audio, and erroneous predictions create a novel supervision signal for training 3D talking head avatars with accurate lip-sync. To demonstrate this effect, we propose THUNDER (Talking Heads Under Neural Differentiable Elocution Reconstruction), a 3D talking head avatar framework that introduces a novel supervision mechanism via differentiable sound production. First, we train a novel mesh-to-speech model that regresses audio from facial animation. Then, we incorporate this model into a diffusion-based talking avatar framework. During training, the mesh-to-speech model takes the generated animation and produces a sound that is compared to the input speech, creating a differentiable analysis-by-audio-synthesis supervision loop. Our extensive qualitative and quantitative experiments demonstrate that THUNDER significantly improves the quality of the lip-sync of talking head avatars while still allowing for generation of diverse, high-quality, expressive facial animations. The code and models will be available at https://thunder.is.tue.mpg.de/

</details>

#### [Hierarchically Controlled Deformable 3D Gaussians for Talking Head Synthesis](https://www.semanticscholar.org/paper/e4c1fe41a4249e205fe596b17e921199d5333b12)
**Zhenhua Wu, Linxuan Jiang, Xiang Li, Chaowei Fang et al.** · 2025-04-11

<details>
<summary>Abstract</summary>

Audio-driven talking head synthesis is a critical task in digital human modeling. While recent advances using diffusion models and Neural Radiance Fields (NeRF) have improved visual quality, they often require substantial computational resources, limiting practical deployment. We present a novel framework for audio-driven talking head synthesis, namely it Hierarchically Controlled Deformable 3D Gaussians (HiCoDe), which achieves state-of-the-art performance with significantly reduced computational costs. Our key contribution is a hierarchical control strategy that effectively bridges the gap between sparse audio features and dense 3D Gaussian point clouds. Specifically, this strategy comprises two control levels: i) coarse-level control based on a 3D Morphable Model (3DMM) and ii) fine-level control using facial landmarks. Extensive experiments on the HDTF dataset and additional test sets demonstrate that our method outperforms existing approaches in visual quality, facial landmark accuracy, and audio-visual synchronization while being more computationally efficient in both training and inference.

</details>

#### [A Survey on Audio-Driven Talking Face Generation](https://www.semanticscholar.org/paper/54112d0b2c9786c7e32504c08190f784cd891a67)
**Xue Bai, Xiangzhen He, Mengdi Ma, Xiang Wang et al.** · 2025-04-11

<details>
<summary>Abstract</summary>

In recent years, advancements in deep learning have driven the development of audio-driven talking face generation. This technology has widespread applications in virtual avatars, intelligent assistants, film and television special effects, remote education, digital human live streaming, and more. Audio-driven talking face generation methods synthesize synchronized talking videos based on input speech signals, ensuring that the mouth movements, facial expressions, and head poses of virtual characters naturally align with the speech content. This paper provides an overview of the major research progress in this field and analyzes the advantages and limitations of different techniques. Additionally, it introduces evaluation metrics used to assess model performance in detail. Finally, the paper summarizes current challenges and potential future research directions.

</details>

#### [VideoSPatS: Video SPatiotemporal Splines for Disentangled Occlusion, Appearance and Motion Modeling and Editing](https://arxiv.org/abs/2504.07146)
**Juan Luis Gonzalez Bello, Xu Yao, Alex Whelan, Kyle Olszewski et al.** · 2025-04-08

<details>
<summary>Abstract</summary>

We present an implicit video representation for occlusions, appearance, and motion disentanglement from monocular videos, which we call Video SPatiotemporal Splines (VideoSPatS). Unlike previous methods that map time and coordinates to deformation and canonical colors, our VideoSPatS maps input coordinates into Spatial and Color Spline deformation fields $D_s$ and $D_c$, which disentangle motion and appearance in videos. With spline-based parametrization, our method naturally generates temporally consistent flow and guarantees long-term temporal consistency, which is crucial for convincing video editing. Using multiple prediction branches, our VideoSPatS model also performs layer separation between the latent video and the selected occluder. By disentangling occlusions, appearance, and motion, our method enables better spatiotemporal modeling and editing of diverse videos, including in-the-wild talking head videos with challenging occlusions, shadows, and specularities while maintaining an appropriate canonical space for editing. We also present general video modeling results on the DAVIS and CoDeF datasets, as well as our own talking head video dataset collected from open-source web videos. Extensive ablations show the combination of $D_s$ and $D_c$ under neural splines can overcome motion and appearance ambiguities, paving the way for more advanced video editing models.

</details>

#### [FluentLip: A Phonemes-Based Two-stage Approach for Audio-Driven Lip Synthesis with Optical Flow Consistency](https://arxiv.org/abs/2504.04427)
**Shiyan Liu, Rui Qu, Yan Jin** · 2025-04-06

<details>
<summary>Abstract</summary>

Generating consecutive images of lip movements that align with a given speech in audio-driven lip synthesis is a challenging task. While previous studies have made strides in synchronization and visual quality, lip intelligibility and video fluency remain persistent challenges. This work proposes FluentLip, a two-stage approach for audio-driven lip synthesis, incorporating three featured strategies. To improve lip synchronization and intelligibility, we integrate a phoneme extractor and encoder to generate a fusion of audio and phoneme information for multimodal learning. Additionally, we employ optical flow consistency loss to ensure natural transitions between image frames. Furthermore, we incorporate a diffusion chain during the training of Generative Adversarial Networks (GANs) to improve both stability and efficiency. We evaluate our proposed FluentLip through extensive experiments, comparing it with five state-of-the-art (SOTA) approaches across five metrics, including a proposed metric called Phoneme Error Rate (PER) that evaluates lip pose intelligibility and video fluency. The experimental results demonstrate that our FluentLip approach is highly competitive, achieving significant improvements in smoothness and naturalness. In particular, it outperforms these SOTA approaches by approximately $\textbf{16.3%}$ in Fréchet Inception Distance (FID) and $\textbf{35.2%}$ in PER.

</details>

#### [DFNeRF: Disentangled Facial Neural Radiance Fields for Text-based Editing of Free-view Talking Head](https://www.semanticscholar.org/paper/93e8d0e52b07d26494bf4518a74c5c8fcc0e84eb)
**Benwang Chen, Xiaoyu Li, Xuan Wang, Qi Zhang et al.** · 2025-04-06

<details>
<summary>Abstract</summary>

In this paper, we propose a text-based approach that can edit the speech content of a free-view talking head based on its transcript. The core of our method is to establish the relationship between phonemes and head attributes. To avoid discontinuities in head pose and facial expressions caused by editing mouth shape. We design the disentangled facial neural radiance fields (DFNeRF) to automatically disentangle these attributes controlled by the learned latent codes. Using the free-view talking head synthesized by DFNeRF as the base corpus, we could re-assemble the latent codes based on the new content using the phoneme search method to produce a seamless edited result. Our phoneme search method with a discriminator could find the best-matched phonemes in the sequence and ensure a smooth transition of mouth shape between the adjacent phonemes. Extensive experiments demonstrate the effectiveness of our method both qualitatively and quantitatively.

</details>

#### [Gaussian-Face: Talking Head Generation with Hybrid Density via 3D Gaussian Splatting](https://www.semanticscholar.org/paper/eea6b50f30ec571eafc0cbea6aa04173cfb51201)
**Guanwen Feng, Yilin Zhang, Yunan Li, Siyu Jin et al.** · 2025-04-06

<details>
<summary>Abstract</summary>

In recent years, audio-driven neural radiance field (NeRF)-based talking head generation techniques have achieved impressive results. However, these methods still have some limitations, such as unsynchronized lip movements and visual jitter. Recently, 3D Gaussian splatting has gradually replaced NeRF. Compared to NeRF, 3D Gaussian offers notable advantages, including higher efficiency and better reconstruction quality. Based on this, we propose Gaussian-Face, an audio-driven Gaussian-based facial avatar. With just a few minutes of monocular video and audio, a high-fidelity, driveable facial avatar can be reconstructed within hours. To achieve this, we first use FLAME to obtain the 3D representation of the face and then design a Lip Motion Translator to map audio to 3D lip representations. To model higher-quality facial details, we propose a hybrid density modeling method that balances rendering speed and quality, enabling our approach to render high-fidelity facial avatars at more than 160 FPS. Project page: https://peterfanfan.github.io/Gaussian-Face/

</details>

#### [Subjective Fidelity Assessment of Audio- and Video-Driven Talking Head Generation Methods](https://www.semanticscholar.org/paper/b78b96a87356fe953bd7095007ea90acdac1c2c6)
**Anthony Trioux, Yusong Gao, Jiarun Song, Wenjie Wu et al.** · 2025-04-06

<details>
<summary>Abstract</summary>

Audio- and Video-Driven Talking Head Generation methods have attracted considerable research interest due to recent advances in Artificial Intelligence Generated Content (AIGC) technologies. In such approaches, a single image is artificially animated by leveraging audio and/or motion features extracted from video sources. Despite notable progress, current performance assessments rely primarily on traditional objective metrics, often neglecting subjective evaluation aspects. To address this issue, we propose in this paper a subjective fidelity assessment of recent Audio- and/or Video-Driven Talking Head Generation methods. This study aims to assess how accurately and convincingly the generated video reproduces the visual and behavioral characteristics of a real human face, as well as how closely the video aligns with expected natural human expressions, movements, and/or audio synchronization. In order to provide a detailed assessment of the fidelity in the context of talking heads, our study focuses on six key criteria: Overall Fidelity, Gaze Fidelity, Audio-Video Sync Fidelity, Head Pose Fidelity, Expression Fidelity, and Overall Visual Quality. Experiments results reveal a nuanced picture of the fidelity in this context, where the performance varies significantly depending on the video content itself as well as how the animation is generated, highlighting the needs for further research. This research represents an initial step towards the evaluation of Audio- and Video-Driven generative image animation methods for Talking heads while offering insights for improving the accuracy and realism of those techniques. The dataset and corresponding results are available at https://github.com/a-trioux/Subjective-Fidelity-Assessment-Talking-Head.

</details>

#### [Diffused Poses and Distilled Expressions for Controllable Audio-driven Talking Face Generation](https://www.semanticscholar.org/paper/374f3581e81548fed6775f732af5840889d75475)
**Ziqi Zhou, Weize Quan, Zhaojin Lu, Dong-Ming Yan** · 2025-04-06

<details>
<summary>Abstract</summary>

Audio-driven portrait animation is an emerging field in multi-modal generation that aims to create lifelike talking face videos from audio input. While significant progress has been made, accurately modeling the relationship between audio signals and various facial motions, such as head poses and expressions, remains a challenge. Existing methods have primarily focused on generating lip-synchronized movements, often neglecting the intricate correlations between audio and other facial dynamics like head movements and eye blinks. More recent approaches have attempted to address these limitations by introducing latent disentanglement of facial motions, though this often comes at the cost of reduced flexibility in motion control. In this work, we propose a novel framework for audio-driven talking portrait animation that allows for precise and controllable generation of head poses and facial expressions. Our approach includes two key components: an audio-conditional diffusion model for generating prosody-aware head poses and a noise-conditional, lip-distilling transformer for predicting synchronized facial expressions. We further introduce an innovative animation model that uses these generated poses and expressions to produce highly realistic and controllable talking head videos. Extensive experiments demonstrate that our method not only achieves superior performance in generating natural and synchronized facial motions but also outperforms state-of-the-art techniques in the field.

</details>

#### [VoiceCraft-Dub: Automated Video Dubbing with Neural Codec Language Models](https://arxiv.org/abs/2504.02386)
**Kim Sung-Bin, Jeongsoo Choi, Puyuan Peng, Joon Son Chung et al.** · 2025-04-03

<details>
<summary>Abstract</summary>

We present VoiceCraft-Dub, a novel approach for automated video dubbing that synthesizes high-quality speech from text and facial cues. This task has broad applications in filmmaking, multimedia creation, and assisting voice-impaired individuals. Building on the success of Neural Codec Language Models (NCLMs) for speech synthesis, our method extends their capabilities by incorporating video features, ensuring that synthesized speech is time-synchronized and expressively aligned with facial movements while preserving natural prosody. To inject visual cues, we design adapters to align facial features with the NCLM token space and introduce audio-visual fusion layers to merge audio-visual information within the NCLM framework. Additionally, we curate CelebV-Dub, a new dataset of expressive, real-world videos specifically designed for automated video dubbing. Extensive experiments show that our model achieves high-quality, intelligible, and natural speech synthesis with accurate lip synchronization, outperforming existing methods in human perception and performing favorably in objective evaluations. We also adapt VoiceCraft-Dub for the video-to-speech task, demonstrating its versatility for various applications.

</details>

#### [Audio-visual Controlled Video Diffusion with Masked Selective State Spaces Modeling for Natural Talking Head Generation](https://arxiv.org/abs/2504.02542)
**Fa-Ting Hong, Zunnan Xu, Zixiang Zhou, Jun Zhou et al.** · 2025-04-03

<details>
<summary>Abstract</summary>

Talking head synthesis is vital for virtual avatars and human-computer interaction. However, most existing methods are typically limited to accepting control from a single primary modality, restricting their practical utility. To this end, we introduce \textbf{ACTalker}, an end-to-end video diffusion framework that supports both multi-signals control and single-signal control for talking head video generation. For multiple control, we design a parallel mamba structure with multiple branches, each utilizing a separate driving signal to control specific facial regions. A gate mechanism is applied across all branches, providing flexible control over video generation. To ensure natural coordination of the controlled video both temporally and spatially, we employ the mamba structure, which enables driving signals to manipulate feature tokens across both dimensions in each branch. Additionally, we introduce a mask-drop strategy that allows each driving signal to independently control its corresponding facial region within the mamba structure, preventing control conflicts. Experimental results demonstrate that our method produces natural-looking facial videos driven by diverse signals and that the mamba layer seamlessly integrates multiple driving modalities without conflict. The project website can be found at https://harlanhong.github.io/publications/actalker/index.html.

</details>

#### [OmniTalker: One-shot Real-time Text-Driven Talking Audio-Video Generation With Multimodal Style Mimicking](https://arxiv.org/abs/2504.02433)
**Zhongjian Wang, Peng Zhang, Jinwei Qi, Guangyuan Wang et al.** · 2025-04-03

<details>
<summary>Abstract</summary>

Although significant progress has been made in audio-driven talking head generation, text-driven methods remain underexplored. In this work, we present OmniTalker, a unified framework that jointly generates synchronized talking audio-video content from input text while emulating the speaking and facial movement styles of the target identity, including speech characteristics, head motion, and facial dynamics. Our framework adopts a dual-branch diffusion transformer (DiT) architecture, with one branch dedicated to audio generation and the other to video synthesis. At the shallow layers, cross-modal fusion modules are introduced to integrate information between the two modalities. In deeper layers, each modality is processed independently, with the generated audio decoded by a vocoder and the video rendered using a GAN-based high-quality visual renderer. Leveraging the in-context learning capability of DiT through a masked-infilling strategy, our model can simultaneously capture both audio and visual styles without requiring explicit style extraction modules. Thanks to the efficiency of the DiT backbone and the optimized visual renderer, OmniTalker achieves real-time inference at 25 FPS. To the best of our knowledge, OmniTalker is the first one-shot framework capable of jointly modeling speech and facial styles in real time. Extensive experiments demonstrate its superiority over existing methods in terms of generation quality, particularly in preserving style consistency and ensuring precise audio-video synchronization, all while maintaining efficient inference.

</details>

#### [TransLip: AI-Driven Video Translation and Synchronization](https://www.semanticscholar.org/paper/505f78f7846f2feae20a665472e5820e15ebda73)
**Adarsh Muralidharan, Minsa Aji, Rohan Jacob Jacob, Shasna Cherukat et al.** · 2025-04-03

<details>
<summary>Abstract</summary>

The increasing need for region-specific digital content has spurred progress in technologies like video translation and lip synchronization. This work introduces an innovative system for converting video and audio from English into Malayalam, a regional language while achieving precise lip synchronization. The process involves extracting audio and converting speech to text, translating the text and generating speech in the target language. The synchronized audio is then aligned with the speaker’s lip movements using the Generative Adversarial Network(GAN) powered Wav2Lip model. The result is a cohesive video where the translated audio and lip movement are in harmony, delivering a lifelike and engaging experience for viewers. This approach offers substantial benefits in sectors like entertainment, education, and media localization, broadening access to content while upholding the integrity of the original material.

</details>

#### [Detecting Lip-Syncing Deepfakes: Vision Temporal Transformer for Analyzing Mouth Inconsistencies](https://arxiv.org/abs/2504.01470)
**Soumyya Kanti Datta, Shan Jia, Siwei Lyu** · 2025-04-02

<details>
<summary>Abstract</summary>

Deepfakes are AI-generated media in which the original content is digitally altered to create convincing but manipulated images, videos, or audio. Among the various types of deepfakes, lip-syncing deepfakes are one of the most challenging deepfakes to detect. In these videos, a person's lip movements are synthesized to match altered or entirely new audio using AI models. Therefore, unlike other types of deepfakes, the artifacts in lip-syncing deepfakes are confined to the mouth region, making them more subtle and, thus harder to discern. In this paper, we propose LIPINC-V2, a novel detection framework that leverages a combination of vision temporal transformer with multihead cross-attention to detect lip-syncing deepfakes by identifying spatiotemporal inconsistencies in the mouth region. These inconsistencies appear across adjacent frames and persist throughout the video. Our model can successfully capture both short-term and long-term variations in mouth movement, enhancing its ability to detect these inconsistencies. Additionally, we created a new lip-syncing deepfake dataset, LipSyncTIMIT, which was generated using five state-of-the-art lip-syncing models to simulate real-world scenarios. Extensive experiments on our proposed LipSyncTIMIT dataset and two other benchmark deepfake datasets demonstrate that our model achieves state-of-the-art performance. The code and the dataset are available at https://github.com/skrantidatta/LIPINC-V2 .

</details>

#### [Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](https://arxiv.org/abs/2503.22225)
**Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian et al.** · 2025-03-28

<details>
<summary>Abstract</summary>

Pre-trained conditional diffusion models have demonstrated remarkable potential in image editing. However, they often face challenges with temporal consistency, particularly in the talking head domain, where continuous changes in facial expressions intensify the level of difficulty. These issues stem from the independent editing of individual images and the inherent loss of temporal continuity during the editing process. In this paper, we introduce Follow Your Motion (FYM), a generic framework for maintaining temporal consistency in portrait editing. Specifically, given portrait images rendered by a pre-trained 3D Gaussian Splatting model, we first develop a diffusion model that intuitively and inherently learns motion trajectory changes at different scales and pixel coordinates, from the first frame to each subsequent frame. This approach ensures that temporally inconsistent edited avatars inherit the motion information from the rendered avatars. Secondly, to maintain fine-grained expression temporal consistency in talking head editing, we propose a dynamic re-weighted attention mechanism. This mechanism assigns higher weight coefficients to landmark points in space and dynamically updates these weights based on landmark loss, achieving more consistent and refined facial expressions. Extensive experiments demonstrate that our method outperforms existing approaches in terms of temporal consistency and can be used to optimize and compensate for temporally inconsistent outputs in a range of applications, such as text-driven editing, relighting, and various other applications.

</details>

#### [ChatAnyone: Stylized Real-time Portrait Video Generation with Hierarchical Motion Diffusion Model](https://arxiv.org/abs/2503.21144)
**Jinwei Qi, Chaonan Ji, Sheng Xu, Peng Zhang et al.** · 2025-03-27

<details>
<summary>Abstract</summary>

Real-time interactive video-chat portraits have been increasingly recognized as the future trend, particularly due to the remarkable progress made in text and voice chat technologies. However, existing methods primarily focus on real-time generation of head movements, but struggle to produce synchronized body motions that match these head actions. Additionally, achieving fine-grained control over the speaking style and nuances of facial expressions remains a challenge. To address these limitations, we introduce a novel framework for stylized real-time portrait video generation, enabling expressive and flexible video chat that extends from talking head to upper-body interaction. Our approach consists of the following two stages. The first stage involves efficient hierarchical motion diffusion models, that take both explicit and implicit motion representations into account based on audio inputs, which can generate a diverse range of facial expressions with stylistic control and synchronization between head and body movements. The second stage aims to generate portrait video featuring upper-body movements, including hand gestures. We inject explicit hand control signals into the generator to produce more detailed hand movements, and further perform face refinement to enhance the overall realism and expressiveness of the portrait video. Additionally, our approach supports efficient and continuous generation of upper-body portrait video in maximum 512 * 768 resolution at up to 30fps on 4090 GPU, supporting interactive video-chat in real-time. Experimental results demonstrate the capability of our approach to produce portrait videos with rich expressiveness and natural upper-body movements.

</details>

#### [Dual Audio-Centric Modality Coupling for Talking Head Generation](https://arxiv.org/abs/2503.22728)
**Ao Fu, Ziqi Ni, Yi Zhou** · 2025-03-26

<details>
<summary>Abstract</summary>

The generation of audio-driven talking head videos is a key challenge in computer vision and graphics, with applications in virtual avatars and digital media. Traditional approaches often struggle with capturing the complex interaction between audio and facial dynamics, leading to lip synchronization and visual quality issues. In this paper, we propose a novel NeRF-based framework, Dual Audio-Centric Modality Coupling (DAMC), which effectively integrates content and dynamic features from audio inputs. By leveraging a dual encoder structure, DAMC captures semantic content through the Content-Aware Encoder and ensures precise visual synchronization through the Dynamic-Sync Encoder. These features are fused using a Cross-Synchronized Fusion Module (CSFM), enhancing content representation and lip synchronization. Extensive experiments show that our method outperforms existing state-of-the-art approaches in key metrics such as lip synchronization accuracy and image quality, demonstrating robust generalization across various audio inputs, including synthetic speech from text-to-speech (TTS) systems. Our results provide a promising solution for high-quality, audio-driven talking head generation and present a scalable approach for creating realistic talking heads.

</details>

#### [MVPortrait: Text-Guided Motion and Emotion Control for Multi-view Vivid Portrait Animation](https://arxiv.org/abs/2503.19383)
**Yukang Lin, Hokit Fung, Jianjin Xu, Zeping Ren et al.** · 2025-03-25

<details>
<summary>Abstract</summary>

Recent portrait animation methods have made significant strides in generating realistic lip synchronization. However, they often lack explicit control over head movements and facial expressions, and cannot produce videos from multiple viewpoints, resulting in less controllable and expressive animations. Moreover, text-guided portrait animation remains underexplored, despite its user-friendly nature. We present a novel two-stage text-guided framework, MVPortrait (Multi-view Vivid Portrait), to generate expressive multi-view portrait animations that faithfully capture the described motion and emotion. MVPortrait is the first to introduce FLAME as an intermediate representation, effectively embedding facial movements, expressions, and view transformations within its parameter space. In the first stage, we separately train the FLAME motion and emotion diffusion models based on text input. In the second stage, we train a multi-view video generation model conditioned on a reference portrait image and multi-view FLAME rendering sequences from the first stage. Experimental results exhibit that MVPortrait outperforms existing methods in terms of motion and emotion control, as well as view consistency. Furthermore, by leveraging FLAME as a bridge, MVPortrait becomes the first controllable portrait animation framework that is compatible with text, speech, and video as driving signals.

</details>

#### [EmoHead: Emotional Talking Head via Manipulating Semantic Expression Parameters](https://arxiv.org/abs/2503.19416)
**Xuli Shen, Hua Cai, Dingding Yu, Weilin Shen et al.** · 2025-03-25

<details>
<summary>Abstract</summary>

Generating emotion-specific talking head videos from audio input is an important and complex challenge for human-machine interaction. However, emotion is highly abstract concept with ambiguous boundaries, and it necessitates disentangled expression parameters to generate emotionally expressive talking head videos. In this work, we present EmoHead to synthesize talking head videos via semantic expression parameters. To predict expression parameter for arbitrary audio input, we apply an audio-expression module that can be specified by an emotion tag. This module aims to enhance correlation from audio input across various emotions. Furthermore, we leverage pre-trained hyperplane to refine facial movements by probing along the vertical direction. Finally, the refined expression parameters regularize neural radiance fields and facilitate the emotion-consistent generation of talking head videos. Experimental results demonstrate that semantic expression parameters lead to better reconstruction quality and controllability.

</details>

#### [DisentTalk: Cross-lingual Talking Face Generation via Semantic Disentangled Diffusion Model](https://arxiv.org/abs/2503.19001)
**Kangwei Liu, Junwu Liu, Yun Cao, Jinlin Guo et al.** · 2025-03-24

<details>
<summary>Abstract</summary>

Recent advances in talking face generation have significantly improved facial animation synthesis. However, existing approaches face fundamental limitations: 3DMM-based methods maintain temporal consistency but lack fine-grained regional control, while Stable Diffusion-based methods enable spatial manipulation but suffer from temporal inconsistencies. The integration of these approaches is hindered by incompatible control mechanisms and semantic entanglement of facial representations. This paper presents DisentTalk, introducing a data-driven semantic disentanglement framework that decomposes 3DMM expression parameters into meaningful subspaces for fine-grained facial control. Building upon this disentangled representation, we develop a hierarchical latent diffusion architecture that operates in 3DMM parameter space, integrating region-aware attention mechanisms to ensure both spatial precision and temporal coherence. To address the scarcity of high-quality Chinese training data, we introduce CHDTF, a Chinese high-definition talking face dataset. Extensive experiments show superior performance over existing methods across multiple metrics, including lip synchronization, expression quality, and temporal consistency. Project Page: https://kangweiiliu.github.io/DisentTalk.

</details>

#### [Teller: Real-Time Streaming Audio-Driven Portrait Animation with Autoregressive Motion Generation](https://arxiv.org/abs/2503.18429)
**Dingcheng Zhen, Shunshun Yin, Shiyang Qin, Hou Yi et al.** · 2025-03-24

<details>
<summary>Abstract</summary>

In this work, we introduce the first autoregressive framework for real-time, audio-driven portrait animation, a.k.a, talking head. Beyond the challenge of lengthy animation times, a critical challenge in realistic talking head generation lies in preserving the natural movement of diverse body parts. To this end, we propose Teller, the first streaming audio-driven protrait animation framework with autoregressive motion generation. Specifically, Teller first decomposes facial and body detail animation into two components: Facial Motion Latent Generation (FMLG) based on an autoregressive transfromer, and movement authenticity refinement using a Efficient Temporal Module (ETM).Concretely, FMLG employs a Residual VQ model to map the facial motion latent from the implicit keypoint-based model into discrete motion tokens, which are then temporally sliced with audio embeddings. This enables the AR tranformer to learn real-time, stream-based mappings from audio to motion. Furthermore, Teller incorporate ETM to capture finer motion details. This module ensures the physical consistency of body parts and accessories, such as neck muscles and earrings, improving the realism of these movements. Teller is designed to be efficient, surpassing the inference speed of diffusion-based models (Hallo 20.93s vs. Teller 0.92s for one second video generation), and achieves a real-time streaming performance of up to 25 FPS. Extensive experiments demonstrate that our method outperforms recent audio-driven portrait animation models, especially in small movements, as validated by human evaluations with a significant margin in quality and realism.

</details>

#### [DiffusionTalker: Efficient and Compact Speech-Driven 3D Talking Head via Personalizer-Guided Distillation](https://arxiv.org/abs/2503.18159)
**Peng Chen, Xiaobao Wei, Ming Lu, Hui Chen et al.** · 2025-03-23

<details>
<summary>Abstract</summary>

Real-time speech-driven 3D facial animation has been attractive in academia and industry. Traditional methods mainly focus on learning a deterministic mapping from speech to animation. Recent approaches start to consider the nondeterministic fact of speech-driven 3D face animation and employ the diffusion model for the task. Existing diffusion-based methods can improve the diversity of facial animation. However, personalized speaking styles conveying accurate lip language is still lacking, besides, efficiency and compactness still need to be improved. In this work, we propose DiffusionTalker to address the above limitations via personalizer-guided distillation. In terms of personalization, we introduce a contrastive personalizer that learns identity and emotion embeddings to capture speaking styles from audio. We further propose a personalizer enhancer during distillation to enhance the influence of embeddings on facial animation. For efficiency, we use iterative distillation to reduce the steps required for animation generation and achieve more than 8x speedup in inference. To achieve compactness, we distill the large teacher model into a smaller student model, reducing our model's storage by 86.4\% while minimizing performance loss. After distillation, users can derive their identity and emotion embeddings from audio to quickly create personalized animations that reflect specific speaking styles. Extensive experiments are conducted to demonstrate that our method outperforms state-of-the-art methods. The code will be released at: https://github.com/ChenVoid/DiffusionTalker.

</details>

#### [Unlock Pose Diversity: Accurate and Efficient Implicit Keypoint-based Spatiotemporal Diffusion for Audio-driven Talking Portrait](https://arxiv.org/abs/2503.12963)
**Chaolong Yang, Kai Yao, Yuyao Yan, Chenru Jiang et al.** · 2025-03-17

<details>
<summary>Abstract</summary>

Audio-driven single-image talking portrait generation plays a crucial role in virtual reality, digital human creation, and filmmaking. Existing approaches are generally categorized into keypoint-based and image-based methods. Keypoint-based methods effectively preserve character identity but struggle to capture fine facial details due to the fixed points limitation of the 3D Morphable Model. Moreover, traditional generative networks face challenges in establishing causality between audio and keypoints on limited datasets, resulting in low pose diversity. In contrast, image-based approaches produce high-quality portraits with diverse details using the diffusion network but incur identity distortion and expensive computational costs. In this work, we propose KDTalker, the first framework to combine unsupervised implicit 3D keypoint with a spatiotemporal diffusion model. Leveraging unsupervised implicit 3D keypoints, KDTalker adapts facial information densities, allowing the diffusion process to model diverse head poses and capture fine facial details flexibly. The custom-designed spatiotemporal attention mechanism ensures accurate lip synchronization, producing temporally consistent, high-quality animations while enhancing computational efficiency. Experimental results demonstrate that KDTalker achieves state-of-the-art performance regarding lip synchronization accuracy, head pose diversity, and execution efficiency.Our codes are available at https://github.com/chaolongy/KDTalker.

</details>

#### [SyncDiff: Diffusion-based Talking Head Synthesis with Bottlenecked Temporal Visual Prior for Improved Synchronization](https://arxiv.org/abs/2503.13371)
**Xulin Fan, Heting Gao, Ziyi Chen, Peng Chang et al.** · 2025-03-17

<details>
<summary>Abstract</summary>

Talking head synthesis, also known as speech-to-lip synthesis, reconstructs the facial motions that align with the given audio tracks. The synthesized videos are evaluated on mainly two aspects, lip-speech synchronization and image fidelity. Recent studies demonstrate that GAN-based and diffusion-based models achieve state-of-the-art (SOTA) performance on this task, with diffusion-based models achieving superior image fidelity but experiencing lower synchronization compared to their GAN-based counterparts. To this end, we propose SyncDiff, a simple yet effective approach to improve diffusion-based models using a temporal pose frame with information bottleneck and facial-informative audio features extracted from AVHuBERT, as conditioning input into the diffusion process. We evaluate SyncDiff on two canonical talking head datasets, LRS2 and LRS3 for direct comparison with other SOTA models. Experiments on LRS2/LRS3 datasets show that SyncDiff achieves a synchronization score 27.7%/62.3% relatively higher than previous diffusion-based methods, while preserving their high-fidelity characteristics.

</details>

#### [Cafe-Talk: Generating 3D Talking Face Animation with Multimodal Coarse- and Fine-grained Control](https://arxiv.org/abs/2503.14517)
**Hejia Chen, Haoxian Zhang, Shoulong Zhang, Xiaoqiang Liu et al.** · 2025-03-14

<details>
<summary>Abstract</summary>

Speech-driven 3D talking face method should offer both accurate lip synchronization and controllable expressions. Previous methods solely adopt discrete emotion labels to globally control expressions throughout sequences while limiting flexible fine-grained facial control within the spatiotemporal domain. We propose a diffusion-transformer-based 3D talking face generation model, Cafe-Talk, which simultaneously incorporates coarse- and fine-grained multimodal control conditions. Nevertheless, the entanglement of multiple conditions challenges achieving satisfying performance. To disentangle speech audio and fine-grained conditions, we employ a two-stage training pipeline. Specifically, Cafe-Talk is initially trained using only speech audio and coarse-grained conditions. Then, a proposed fine-grained control adapter gradually adds fine-grained instructions represented by action units (AUs), preventing unfavorable speech-lip synchronization. To disentangle coarse- and fine-grained conditions, we design a swap-label training mechanism, which enables the dominance of the fine-grained conditions. We also devise a mask-based CFG technique to regulate the occurrence and intensity of fine-grained control. In addition, a text-based detector is introduced with text-AU alignment to enable natural language user input and further support multimodal control. Extensive experimental results prove that Cafe-Talk achieves state-of-the-art lip synchronization and expressiveness performance and receives wide acceptance in fine-grained control in user studies. Project page: https://harryxd2018.github.io/cafe-talk/

</details>

#### [EmoDiffusion: Enhancing Emotional 3D Facial Animation with Latent Diffusion Models](https://arxiv.org/abs/2503.11028)
**Yixuan Zhang, Qing Chang, Yuxi Wang, Guang Chen et al.** · 2025-03-14

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation seeks to produce lifelike facial expressions that are synchronized with the speech content and its emotional nuances, finding applications in various multimedia fields. However, previous methods often overlook emotional facial expressions or fail to disentangle them effectively from the speech content. To address these challenges, we present EmoDiffusion, a novel approach that disentangles different emotions in speech to generate rich 3D emotional facial expressions. Specifically, our method employs two Variational Autoencoders (VAEs) to separately generate the upper face region and mouth region, thereby learning a more refined representation of the facial sequence. Unlike traditional methods that use diffusion models to connect facial expression sequences with audio inputs, we perform the diffusion process in the latent space. Furthermore, we introduce an Emotion Adapter to evaluate upper face movements accurately. Given the paucity of 3D emotional talking face data in the animation industry, we capture facial expressions under the guidance of animation experts using LiveLinkFace on an iPhone. This effort results in the creation of an innovative 3D blendshape emotional talking face dataset (3D-BEF) used to train our network. Extensive experiments and perceptual evaluations validate the effectiveness of our approach, confirming its superiority in generating realistic and emotionally rich facial animations.

</details>

#### [Bidirectional Learned Facial Animation Codec for Low Bitrate Talking Head Videos](https://arxiv.org/abs/2503.09787)
**Riku Takahashi, Ryugo Morita, Fuma Kimishima, Kosuke Iwama et al.** · 2025-03-12

<details>
<summary>Abstract</summary>

Existing deep facial animation coding techniques efficiently compress talking head videos by applying deep generative models. Instead of compressing the entire video sequence, these methods focus on compressing only the keyframe and the keypoints of non-keyframes (target frames). The target frames are then reconstructed by utilizing a single keyframe, and the keypoints of the target frame. Although these unidirectional methods can reduce the bitrate, they rely on a single keyframe and often struggle to capture large head movements accurately, resulting in distortions in the facial region. In this paper, we propose a novel bidirectional learned animation codec that generates natural facial videos using past and future keyframes. First, in the Bidirectional Reference-Guided Auxiliary Stream Enhancement (BRG-ASE) process, we introduce a compact auxiliary stream for non-keyframes, which is enhanced by adaptively selecting one of two keyframes (past and future). This stream improves video quality with a slight increase in bitrate. Then, in the Bidirectional Reference-Guided Video Reconstruction (BRG-VRec) process, we animate the adaptively selected keyframe and reconstruct the target frame using both the animated keyframe and the auxiliary frame. Extensive experiments demonstrate a 55% bitrate reduction compared to the latest animation based video codec, and a 35% bitrate reduction compared to the latest video coding standard, Versatile Video Coding (VVC) on a talking head video dataset. It showcases the efficiency of our approach in improving video quality while simultaneously decreasing bitrate.

</details>

#### [Versatile Multimodal Controls for Expressive Talking Human Animation](https://arxiv.org/abs/2503.08714)
**Zheng Qin, Ruobing Zheng, Yabing Wang, Tianqi Li et al.** · 2025-03-10

<details>
<summary>Abstract</summary>

In filmmaking, directors typically allow actors to perform freely based on the script before providing specific guidance on how to present key actions. AI-generated content faces similar requirements, where users not only need automatic generation of lip synchronization and basic gestures from audio input but also desire semantically accurate and expressive body movement that can be ``directly guided'' through text descriptions. Therefore, we present VersaAnimator, a versatile framework that synthesizes expressive talking human videos from arbitrary portrait images. Specifically, we design a motion generator that produces basic rhythmic movements from audio input and supports text-prompt control for specific actions. The generated whole-body 3D motion tokens can animate portraits of various scales, producing talking heads, half-body gestures and even leg movements for whole-body images. Besides, we introduce a multi-modal controlled video diffusion that generates photorealistic videos, where speech signals govern lip synchronization, facial expressions, and head motions while body movements are guided by the 2D poses. Furthermore, we introduce a token2pose translator to smoothly map 3D motion tokens to 2D pose sequences. This design mitigates the stiffness resulting from direct 3D to 2D conversion and enhances the details of the generated body movements. Extensive experiments shows that VersaAnimator synthesizes lip-synced and identity-preserving videos while generating expressive and semantically meaningful whole-body motions.

</details>

#### [Removing Averaging: Personalized Lip-Sync Driven Characters Based on Identity Adapter](https://arxiv.org/abs/2503.06397)
**Yanyu Zhu, Lichen Bai, Jintao Xu, Hai-tao Zheng** · 2025-03-09

<details>
<summary>Abstract</summary>

Recent advances in diffusion-based lip-syncing generative models have demonstrated their ability to produce highly synchronized talking face videos for visual dubbing. Although these models excel at lip synchronization, they often struggle to maintain fine-grained control over facial details in generated images. In this work, we identify "lip averaging" phenomenon where the model fails to preserve subtle facial details when dubbing unseen in-the-wild videos. This issue arises because the commonly used UNet backbone primarily integrates audio features into visual representations in the latent space via cross-attention mechanisms and multi-scale fusion, but it struggles to retain fine-grained lip details in the generated faces. To address this issue, we propose UnAvgLip, which extracts identity embeddings from reference videos to generate highly faithful facial sequences while maintaining accurate lip synchronization. Specifically, our method comprises two primary components: (1) an Identity Perceiver module that encodes facial embeddings to align with conditioned audio features; and (2) an ID-CrossAttn module that injects facial embeddings into the generation process, enhancing model's capability of identity retention. Extensive experiments demonstrate that, at a modest training and inference cost, UnAvgLip effectively mitigates the "averaging" phenomenon in lip inpainting, significantly preserving unique facial characteristics while maintaining precise lip synchronization. Compared with the original approach, our method demonstrates significant improvements of 5% on the identity consistency metric and 2% on the SSIM metric across two benchmark datasets (HDTF and LRW).

</details>

#### [MagicInfinite: Generating Infinite Talking Videos with Your Words and Voice](https://arxiv.org/abs/2503.05978)
**Hongwei Yi, Tian Ye, Shitong Shao, Xuancheng Yang et al.** · 2025-03-07

<details>
<summary>Abstract</summary>

We present MagicInfinite, a novel diffusion Transformer (DiT) framework that overcomes traditional portrait animation limitations, delivering high-fidelity results across diverse character types-realistic humans, full-body figures, and stylized anime characters. It supports varied facial poses, including back-facing views, and animates single or multiple characters with input masks for precise speaker designation in multi-character scenes. Our approach tackles key challenges with three innovations: (1) 3D full-attention mechanisms with a sliding window denoising strategy, enabling infinite video generation with temporal coherence and visual quality across diverse character styles; (2) a two-stage curriculum learning scheme, integrating audio for lip sync, text for expressive dynamics, and reference images for identity preservation, enabling flexible multi-modal control over long sequences; and (3) region-specific masks with adaptive loss functions to balance global textual control and local audio guidance, supporting speaker-specific animations. Efficiency is enhanced via our innovative unified step and cfg distillation techniques, achieving a 20x inference speed boost over the basemodel: generating a 10 second 540x540p video in 10 seconds or 720x720p in 30 seconds on 8 H100 GPUs, without quality loss. Evaluations on our new benchmark demonstrate MagicInfinite's superiority in audio-lip synchronization, identity preservation, and motion naturalness across diverse scenarios. It is publicly available at https://www.hedra.com/, with examples at https://magicinfinite.github.io/.

</details>

#### [FREAK: Frequency-modulated High-fidelity and Real-time Audio-driven Talking Portrait Synthesis](https://arxiv.org/abs/2503.04067)
**Ziqi Ni, Ao Fu, Yi Zhou** · 2025-03-06

<details>
<summary>Abstract</summary>

Achieving high-fidelity lip-speech synchronization in audio-driven talking portrait synthesis remains challenging. While multi-stage pipelines or diffusion models yield high-quality results, they suffer from high computational costs. Some approaches perform well on specific individuals with low resources, yet still exhibit mismatched lip movements. The aforementioned methods are modeled in the pixel domain. We observed that there are noticeable discrepancies in the frequency domain between the synthesized talking videos and natural videos. Currently, no research on talking portrait synthesis has considered this aspect. To address this, we propose a FREquency-modulated, high-fidelity, and real-time Audio-driven talKing portrait synthesis framework, named FREAK, which models talking portraits from the frequency domain perspective, enhancing the fidelity and naturalness of the synthesized portraits. FREAK introduces two novel frequency-based modules: 1) the Visual Encoding Frequency Modulator (VEFM) to couple multi-scale visual features in the frequency domain, better preserving visual frequency information and reducing the gap in the frequency spectrum between synthesized and natural frames. and 2) the Audio Visual Frequency Modulator (AVFM) to help the model learn the talking pattern in the frequency domain and improve audio-visual synchronization. Additionally, we optimize the model in both pixel domain and frequency domain jointly. Furthermore, FREAK supports seamless switching between one-shot and video dubbing settings, offering enhanced flexibility. Due to its superior performance, it can simultaneously support high-resolution video results and real-time inference. Extensive experiments demonstrate that our method synthesizes high-fidelity talking portraits with detailed facial textures and precise lip synchronization in real-time, outperforming state-of-the-art methods.

</details>

#### [Realistic Lip-Sync Generation from Text for Multimodal Applications](https://www.semanticscholar.org/paper/ea0ae8bc51add7570999bf6f8504cc9718349785)
**Doradla Kaushik, Konduru Praveen Karthik, Taduvai Satvik Gupta, Susmitha Vekkot** · 2025-03-06

<details>
<summary>Abstract</summary>

This paper explores an advanced framework for text-to-lip-sync generation, leveraging the integration of the Massively Multilingual Speech Text-to-Speech (MMS TTS) and Wav2Lip models. The MMS TTS model transforms text into natural, high-quality multilingual speech while preserving speaker identity, and the Wav2Lip model ensures accurate synchronization of lip movements with the generated audio. Using the GRID dataset for training, the Wav2Lip model achieves remarkable performance in audiovisual alignment, attaining high lip-sync confidence metrics with an LSE-C score of 6.701 and an LSE-D score of 7.362. The proposed solution has broad applicability in virtual assistants, media production, digital education, and accessibility, setting a new standard for immersive and realistic audiovisual experiences.

</details>

#### [A Unified Deep Learning Framework for Lip Reading and Deep Fake Audio Classification](https://www.semanticscholar.org/paper/384047c6c103814109d686cdaebe629b11cfd61c)
**Vijay A. Sangolgi, Mithun B. Patil, Omkar Nagnath Bhosale, Anurag Vivek Deshmukhe et al.** · 2025-03-06

<details>
<summary>Abstract</summary>

This study proposes a multimodal framework designed to enhance deepfake detection by integrating visual lip-reading analysis and audio signal processing for real-time applications. Leveraging LipNet—a deep learning model pre-trained on the GRID dataset—the system employs 3D convolutional neural networks (CNNs) combined with bidirectional long short-term memory (Bi-LSTM) layers to interpret lip movements and decode spoken words from visual inputs. Simultaneously, audio analysis modules evaluate acoustic features to detect synthetic or manipulated speech. By independently training these components and combining their outputs, the framework identifies inconsistencies between visual and auditory modalities, such as mismatched lip-audio synchronization or unnatural speech patterns. Experimental results demonstrate robust performance in both word-level lip-reading accuracy and deepfake detection reliability, achieving high precision in flagging fraudulent content. The system’s effectiveness in detecting audiovisual anomalies positions it as a practical tool for digital forensics and security applications, with potential to foster trust in digital media. Future work will expand the model’s adaptability to diverse datasets, including multilingual contexts, and refine its integration into real-world media authentication and accessibility tools.

</details>

#### [KeyFace: Expressive Audio-Driven Facial Animation for Long Sequences via KeyFrame Interpolation](https://arxiv.org/abs/2503.01715)
**Antoni Bigata, Michał Stypułkowski, Rodrigo Mira, Stella Bounareli et al.** · 2025-03-03

<details>
<summary>Abstract</summary>

Current audio-driven facial animation methods achieve impressive results for short videos but suffer from error accumulation and identity drift when extended to longer durations. Existing methods attempt to mitigate this through external spatial control, increasing long-term consistency but compromising the naturalness of motion. We propose KeyFace, a novel two-stage diffusion-based framework, to address these issues. In the first stage, keyframes are generated at a low frame rate, conditioned on audio input and an identity frame, to capture essential facial expressions and movements over extended periods of time. In the second stage, an interpolation model fills in the gaps between keyframes, ensuring smooth transitions and temporal coherence. To further enhance realism, we incorporate continuous emotion representations and handle a wide range of non-speech vocalizations (NSVs), such as laughter and sighs. We also introduce two new evaluation metrics for assessing lip synchronization and NSV generation. Experimental results show that KeyFace outperforms state-of-the-art methods in generating natural, coherent facial animations over extended durations, successfully encompassing NSVs and continuous emotions.

</details>

#### [Enhancing Video Conferencing Experience through Speech Activity Detection and Lip Synchronization with Deep Learning Models](https://www.semanticscholar.org/paper/502b96013aaa764b105468a5b31fd3e63ab40bd2)
**Weikun Lin** · 2025-03-03

<details>
<summary>Abstract</summary>

As video conferencing becomes increasingly integral to modern communication, the need for high-quality synchronization between speech and visual elements is paramount. Speech Activity Detection (VAD) and lip synchronization technologies play crucial roles in ensuring accurate, real-time communication by distinguishing speech signals from noise and aligning lip movements with audio. This paper proposes a novel multimodal fusion approach based on deep learning models that significantly improves the accuracy of speech activity detection and the real-time performance of lip synchronization. Using open datasets such as AVSpeech and LRW, this study showcases the effectiveness of the proposed models in various real-world scenarios, such as multi-party conferences, noisy environments, and cross-lingual settings. Experimental results demonstrate that the LSTM-based VAD model achieves an accuracy of 92%, outperforming traditional methods, while the lip synchronization module ensures seamless audio-visual alignment with minimal delay.

</details>

#### [Two-Stream Spatial-Temporal Transformer Framework for Person Identification via Natural Conversational Keypoints](https://arxiv.org/abs/2502.20803)
**Masoumeh Chapariniya, Hossein Ranjbar, Teodora Vukovic, Sarah Ebling et al.** · 2025-02-28

<details>
<summary>Abstract</summary>

In the age of AI-driven generative technologies, traditional biometric recognition systems face unprecedented challenges, particularly from sophisticated deepfake and face reenactment techniques. In this study, we propose a Two-Stream Spatial-Temporal Transformer Framework for person identification using upper body keypoints visible during online conversations, which we term conversational keypoints. Our framework processes both spatial relationships between keypoints and their temporal evolution through two specialized branches: a Spatial Transformer (STR) that learns distinctive structural patterns in keypoint configurations, and a Temporal Transformer (TTR) that captures sequential motion patterns. Using the state-of-the-art Sapiens pose estimator, we extract 133 keypoints (based on COCO-WholeBody format) representing facial features, head pose, and hand positions. The framework was evaluated on a dataset of 114 individuals engaged in natural conversations, achieving recognition accuracies of 80.12% for the spatial stream, 63.61% for the temporal stream. We then explored two fusion strategies: a shared loss function approach achieving 82.22% accuracy, and a feature-level fusion method that concatenates feature maps from both streams, significantly improving performance to 94.86%. By jointly modeling both static anatomical relationships and dynamic movement patterns, our approach learns comprehensive identity signatures that are more robust to spoofing than traditional appearance-based methods.

</details>

#### [ARTalk: Speech-Driven 3D Head Animation via Autoregressive Model](https://arxiv.org/abs/2502.20323)
**Xuangeng Chu, Nabarun Goswami, Ziteng Cui, Hanqin Wang et al.** · 2025-02-27

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation aims to generate realistic lip movements and facial expressions for 3D head models from arbitrary audio clips. Although existing diffusion-based methods are capable of producing natural motions, their slow generation speed limits their application potential. In this paper, we introduce a novel autoregressive model that achieves real-time generation of highly synchronized lip movements and realistic head poses and eye blinks by learning a mapping from speech to a multi-scale motion codebook. Furthermore, our model can adapt to unseen speaking styles, enabling the creation of 3D talking avatars with unique personal styles beyond the identities seen during training. Extensive evaluations and user studies demonstrate that our method outperforms existing approaches in lip synchronization accuracy and perceived quality.

</details>

#### [Talking Head Anime 4: Distillation for Real-Time Performance](https://www.semanticscholar.org/paper/a332eebf8c0df968876be9263ee0925a0811b27e)
**Pramook Khungurn** · 2025-02-26

<details>
<summary>Abstract</summary>

We study the problem of creating a character model that can be controlled in real time from a single image of an anime character. A solution would greatly reduce the cost of creating avatars, computer games, and other interactive applications. Talking Head Anime 3 (THA3) is an open source project that attempts to directly address the problem [40]. It takes as input (1) an image of an anime character's upper body and (2) a 45-dimensional pose vector and outputs a new image of the same character taking the specified pose. The range of possible movements is expressive enough for personal avatars and certain types of game characters. THA3's main limitation is its speed. It can achieve interactive frame rates (~ 20 FPS) only if it is run on a very powerful GPU (Nvidia Titan RTX or better). Based on the insight that avatars and game characters do not need to change their appearance every so often, we propose a technique to distill the system into a small student neural network ( 2 MB) specific to a particular character. The student model can generate $512 \times 512$ animation frames in real time (> 30 FPS) using consumer gaming GPUs while preserving the image quality of the teacher model. For the first time, our technique makes the whole system practical for real-time applications.

</details>

#### [Deep Face Gen: Speech-Driven Face Image Synthesis](https://www.semanticscholar.org/paper/e08961b0f03e5d184e052253bec3771e0c7c41eb)
**P. K. Thai, P. Manisha, L. Reddy, M. Reddy** · 2025-02-25

<details>
<summary>Abstract</summary>

A framework based on Generative Adversarial Networks (GANs) is proposed to synthesize facial images from audio inputs. The system aims to automatically translate large volumes of audio into understandable facial images without human intervention. By using a GAN architecture, the model generates image features from audio waveforms to reconstruct facial images. It is trained on a dataset of labeled examples, producing facial images corresponding to the identities of the speakers. The method achieves an accuracy of 96.88% for ungrouped data and 93.91% for grouped data. This approach demonstrates its capability to generate accurate facial representations from audio, offering an automated solution for converting speech into intelligible visual data. Keywords: Generative Adversarial Networks, facial image synthesis, audio-to-image, speech-to-visual, automated reconstruction.

</details>

#### [Dimitra: Audio-driven Diffusion model for Expressive Talking Head Generation](https://arxiv.org/abs/2502.17198)
**Baptiste Chopin, Tashvik Dhamija, Pranav Balaji, Yaohui Wang et al.** · 2025-02-24

<details>
<summary>Abstract</summary>

We propose Dimitra, a novel framework for audio-driven talking head generation, streamlined to learn lip motion, facial expression, as well as head pose motion. Specifically, we train a conditional Motion Diffusion Transformer (cMDT) by modeling facial motion sequences with 3D representation. We condition the cMDT with only two input signals, an audio-sequence, as well as a reference facial image. By extracting additional features directly from audio, Dimitra is able to increase quality and realism of generated videos. In particular, phoneme sequences contribute to the realism of lip motion, whereas text transcript to facial expression and head pose realism. Quantitative and qualitative experiments on two widely employed datasets, VoxCeleb2 and HDTF, showcase that Dimitra is able to outperform existing approaches for generating realistic talking heads imparting lip motion, facial expression, and head pose.

</details>

#### [Audio-driven Talking-face Synthesis based on 3D Gaussian](https://www.semanticscholar.org/paper/5f4cb16ff522da3007228ddd371c72b5d12d0602)
**Botao Xiong** · 2025-02-21

<details>
<summary>Abstract</summary>

Audio-driven talking-face synthesis is of significant importance in various application scenarios, such as remote meetings, AR/VR, and digital humans. Currently, the work in this field can be broadly divided into two categories: implicit representation-based methods and explicit representation-based methods. Implicit representation-based methods often use neural network models to represent human face. For example, NeRF (Neural Radiance Field) uses MLP (Multi-Layer Perceptron) to represent human face, and by inputting the camera pose, NeRF renders a face image from that viewpoint. When training with audio features, it can render face images with different facial movements. However, due to the lack of editability and slow rendering speed of implicit representations, the industry has been exploring new representation methods. Explicit representation-based methods commonly use 3D Gaussian representations of the face, which offers high editability and nearly real-time rendering speed, making these methods surpass implicit-based approaches in many metrics. However, it is difficult to incorporate other signals during the rendering optimization process. To address this issue, this paper combines 3D Gaussian representations with the 3D head model FLAME (Faces Learned with an Articulated Model and Expressions). The FLAME model represents the face's shape and facial movements with a set of parameters. In this paper, audio signals are first transformed into parameters representing facial movements, which are used to initialize the 3D model generated by the parameters, followed by rendering optimization. This paper proposes a 3D Gaussian-based audio-driven lip-sync video generation system. It consists of two main modules: the audio-to-facial movement module and the 3D Gaussian rendering module. The audio-to-facial movement module uses the extracted audio features to generate parameters that control the FLAME model, converting the audio input into natural and reasonable lip shapes and facial movements. The 3D Gaussian rendering module initializes the 3D Gaussian with the FLAME model, optimizes the rendered image from coarse to fine, and finally stitches the generated images together to create a continuous video. Experiments show that this system can generate lip-synchronized, accurate, high-fidelity videos.

</details>

#### [NeRF-3DTalker: Neural Radiance Field with 3D Prior Aided Audio Disentanglement for Talking Head Synthesis](https://arxiv.org/abs/2502.14178)
**Xiaoxing Liu, Zhilei Liu, Chongke Bi** · 2025-02-20

<details>
<summary>Abstract</summary>

Talking head synthesis is to synthesize a lip-synchronized talking head video using audio. Recently, the capability of NeRF to enhance the realism and texture details of synthesized talking heads has attracted the attention of researchers. However, most current NeRF methods based on audio are exclusively concerned with the rendering of frontal faces. These methods are unable to generate clear talking heads in novel views. Another prevalent challenge in current 3D talking head synthesis is the difficulty in aligning acoustic and visual spaces, which often results in suboptimal lip-syncing of the generated talking heads. To address these issues, we propose Neural Radiance Field with 3D Prior Aided Audio Disentanglement for Talking Head Synthesis (NeRF-3DTalker). Specifically, the proposed method employs 3D prior information to synthesize clear talking heads with free views. Additionally, we propose a 3D Prior Aided Audio Disentanglement module, which is designed to disentangle the audio into two distinct categories: features related to 3D awarded speech movements and features related to speaking style. Moreover, to reposition the generated frames that are distant from the speaker's motion space in the real space, we have devised a local-global Standardized Space. This method normalizes the irregular positions in the generated frames from both global and local semantic perspectives. Through comprehensive qualitative and quantitative experiments, it has been demonstrated that our NeRF-3DTalker outperforms state-of-the-art in synthesizing realistic talking head videos, exhibiting superior image quality and lip synchronization. Project page: https://nerf-3dtalker.github.io/NeRF-3Dtalker.

</details>

#### [SayAnything: Audio-Driven Lip Synchronization with Conditional Video Diffusion](https://arxiv.org/abs/2502.11515)
**Junxian Ma, Shiwen Wang, Jian Yang, Junyi Hu et al.** · 2025-02-17

<details>
<summary>Abstract</summary>

Recent advances in diffusion models have led to significant progress in audio-driven lip synchronization. However, existing methods typically rely on constrained audio-visual alignment priors or multi-stage learning of intermediate representations to force lip motion synthesis. This leads to complex training pipelines and limited motion naturalness. In this paper, we present SayAnything, a conditional video diffusion framework that directly synthesizes lip movements from audio input while preserving speaker identity. Specifically, we propose three specialized modules including identity preservation module, audio guidance module, and editing control module. Our novel design effectively balances different condition signals in the latent space, enabling precise control over appearance, motion, and region-specific generation without requiring additional supervision signals or intermediate representations. Extensive experiments demonstrate that SayAnything generates highly realistic videos with improved lip-teeth coherence, enabling unseen characters to say anything, while effectively generalizing to animated characters.

</details>

#### [Long-Term TalkingFace Generation via Motion-Prior Conditional Diffusion Model](https://arxiv.org/abs/2502.09533)
**Fei Shen, Cong Wang, Junyao Gao, Qin Guo et al.** · 2025-02-13

<details>
<summary>Abstract</summary>

Recent advances in conditional diffusion models have shown promise for generating realistic TalkingFace videos, yet challenges persist in achieving consistent head movement, synchronized facial expressions, and accurate lip synchronization over extended generations. To address these, we introduce the \textbf{M}otion-priors \textbf{C}onditional \textbf{D}iffusion \textbf{M}odel (\textbf{MCDM}), which utilizes both archived and current clip motion priors to enhance motion prediction and ensure temporal consistency. The model consists of three key elements: (1) an archived-clip motion-prior that incorporates historical frames and a reference frame to preserve identity and context; (2) a present-clip motion-prior diffusion model that captures multimodal causality for accurate predictions of head movements, lip sync, and expressions; and (3) a memory-efficient temporal attention mechanism that mitigates error accumulation by dynamically storing and updating motion features. We also release the \textbf{TalkingFace-Wild} dataset, a multilingual collection of over 200 hours of footage across 10 languages. Experimental results demonstrate the effectiveness of MCDM in maintaining identity and motion continuity for long-term TalkingFace generation. Code, models, and datasets will be publicly available.

</details>

#### [Playmate: Flexible Control of Portrait Animation via 3D-Implicit Space Guided Diffusion](https://arxiv.org/abs/2502.07203)
**Xingpei Ma, Jiaran Cai, Yuansheng Guan, Shenneng Huang et al.** · 2025-02-11

<details>
<summary>Abstract</summary>

Recent diffusion-based talking face generation models have demonstrated impressive potential in synthesizing videos that accurately match a speech audio clip with a given reference identity. However, existing approaches still encounter significant challenges due to uncontrollable factors, such as inaccurate lip-sync, inappropriate head posture and the lack of fine-grained control over facial expressions. In order to introduce more face-guided conditions beyond speech audio clips, a novel two-stage training framework Playmate is proposed to generate more lifelike facial expressions and talking faces. In the first stage, we introduce a decoupled implicit 3D representation along with a meticulously designed motion-decoupled module to facilitate more accurate attribute disentanglement and generate expressive talking videos directly from audio cues. Then, in the second stage, we introduce an emotion-control module to encode emotion control information into the latent space, enabling fine-grained control over emotions and thereby achieving the ability to generate talking videos with desired emotion. Extensive experiments demonstrate that Playmate not only outperforms existing state-of-the-art methods in terms of video quality, but also exhibits strong competitiveness in lip synchronization while offering improved flexibility in controlling emotion and head pose. The code will be available at https://github.com/Playmate111/Playmate.

</details>

#### [EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](https://arxiv.org/abs/2502.00654)
**Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond et al.** · 2025-02-02

<details>
<summary>Abstract</summary>

3D Gaussian splatting-based talking head synthesis has recently gained attention for its ability to render high-fidelity images with real-time inference speed. However, since it is typically trained on only a short video that lacks the diversity in facial emotions, the resultant talking heads struggle to represent a wide range of emotions. To address this issue, we propose a lip-aligned emotional face generator and leverage it to train our EmoTalkingGaussian model. It is able to manipulate facial emotions conditioned on continuous emotion values (i.e., valence and arousal); while retaining synchronization of lip movements with input audio. Additionally, to achieve the accurate lip synchronization for in-the-wild audio, we introduce a self-supervised learning method that leverages a text-to-speech network and a visual-audio synchronization network. We experiment our EmoTalkingGaussian on publicly available videos and have obtained better results than state-of-the-arts in terms of image quality (measured in PSNR, SSIM, LPIPS), emotion expression (measured in V-RMSE, A-RMSE, V-SA, A-SA, Emotion Accuracy), and lip synchronization (measured in LMD, Sync-E, Sync-C), respectively.

</details>

#### [Bridging The Multi-Modality Gaps of Audio, Visual and Linguistic for Speech Enhancement](https://arxiv.org/abs/2501.13375)
**Meng-Ping Lin, Jen-Cheng Hou, Chia-Wei Chen, Shao-Yi Chien et al.** · 2025-01-23

<details>
<summary>Abstract</summary>

Speech enhancement (SE) aims to improve the quality and intelligibility of speech in noisy environments. Recent studies have shown that incorporating visual cues in audio signal processing can enhance SE performance. Given that human speech communication naturally involves audio, visual, and linguistic modalities, it is reasonable to expect additional improvements by integrating linguistic information. However, effectively bridging these modality gaps, particularly during knowledge transfer remains a significant challenge. In this paper, we propose a novel multi-modal learning framework, termed DLAV-SE, which leverages a diffusion-based model integrating audio, visual, and linguistic information for audio-visual speech enhancement (AVSE). Within this framework, the linguistic modality is modeled using a pretrained language model (PLM), which transfers linguistic knowledge to the audio-visual domain through a cross-modal knowledge transfer (CMKT) mechanism during training. After training, the PLM is no longer required at inference, as its knowledge is embedded into the AVSE model through the CMKT process. We conduct a series of SE experiments to evaluate the effectiveness of our approach. Results show that the proposed DLAV-SE system significantly improves speech quality and reduces generative artifacts, such as phonetic confusion, compared to state-of-the-art (SOTA) methods. Furthermore, visualization analyses confirm that the CMKT method enhances the generation quality of the AVSE outputs. These findings highlight both the promise of diffusion-based methods for advancing AVSE and the value of incorporating linguistic information to further improve system performance.

</details>

#### [EMO2: End-Effector Guided Audio-Driven Avatar Video Generation](https://arxiv.org/abs/2501.10687)
**Linrui Tian, Siqi Hu, Qi Wang, Bang Zhang et al.** · 2025-01-18

<details>
<summary>Abstract</summary>

In this paper, we propose a novel audio-driven talking head method capable of simultaneously generating highly expressive facial expressions and hand gestures. Unlike existing methods that focus on generating full-body or half-body poses, we investigate the challenges of co-speech gesture generation and identify the weak correspondence between audio features and full-body gestures as a key limitation. To address this, we redefine the task as a two-stage process. In the first stage, we generate hand poses directly from audio input, leveraging the strong correlation between audio signals and hand movements. In the second stage, we employ a diffusion model to synthesize video frames, incorporating the hand poses generated in the first stage to produce realistic facial expressions and body movements. Our experimental results demonstrate that the proposed method outperforms state-of-the-art approaches, such as CyberHost and Vlogger, in terms of both visual quality and synchronization accuracy. This work provides a new perspective on audio-driven gesture generation and a robust framework for creating expressive and natural talking head animations.

</details>

#### [Joint Learning of Depth and Appearance for Portrait Image Animation](https://arxiv.org/abs/2501.08649)
**Xinya Ji, Gaspard Zoss, Prashanth Chandran, Lingchen Yang et al.** · 2025-01-15

<details>
<summary>Abstract</summary>

2D portrait animation has experienced significant advancements in recent years. Much research has utilized the prior knowledge embedded in large generative diffusion models to enhance high-quality image manipulation. However, most methods only focus on generating RGB images as output, and the co-generation of consistent visual plus 3D output remains largely under-explored. In our work, we propose to jointly learn the visual appearance and depth simultaneously in a diffusion-based portrait image generator. Our method embraces the end-to-end diffusion paradigm and introduces a new architecture suitable for learning this conditional joint distribution, consisting of a reference network and a channel-expanded diffusion backbone. Once trained, our framework can be efficiently adapted to various downstream applications, such as facial depth-to-image and image-to-depth generation, portrait relighting, and audio-driven talking head animation with consistent 3D output.

</details>

#### [Identity-Preserving Video Dubbing Using Motion Warping](https://arxiv.org/abs/2501.04586)
**Runzhen Liu, Qinjie Lin, Yunfei Liu, Lijian Lin et al.** · 2025-01-08

<details>
<summary>Abstract</summary>

Video dubbing aims to synthesize realistic, lip-synced videos from a reference video and a driving audio signal. Although existing methods can accurately generate mouth shapes driven by audio, they often fail to preserve identity-specific features, largely because they do not effectively capture the nuanced interplay between audio cues and the visual attributes of reference identity . As a result, the generated outputs frequently lack fidelity in reproducing the unique textural and structural details of the reference identity. To address these limitations, we propose IPTalker, a novel and robust framework for video dubbing that achieves seamless alignment between driving audio and reference identity while ensuring both lip-sync accuracy and high-fidelity identity preservation. At the core of IPTalker is a transformer-based alignment mechanism designed to dynamically capture and model the correspondence between audio features and reference images, thereby enabling precise, identity-aware audio-visual integration. Building on this alignment, a motion warping strategy further refines the results by spatially deforming reference images to match the target audio-driven configuration. A dedicated refinement process then mitigates occlusion artifacts and enhances the preservation of fine-grained textures, such as mouth details and skin features. Extensive qualitative and quantitative evaluations demonstrate that IPTalker consistently outperforms existing approaches in terms of realism, lip synchronization, and identity retention, establishing a new state of the art for high-quality, identity-consistent video dubbing.

</details>

#### [Generating and Detecting Various Types of Fake Image and Audio Content: A Review of Modern Deep Learning Technologies and Tools](https://arxiv.org/abs/2501.06227)
**Arash Dehghani, Hossein Saberi** · 2025-01-07

<details>
<summary>Abstract</summary>

This paper reviews the state-of-the-art in deepfake generation and detection, focusing on modern deep learning technologies and tools based on the latest scientific advancements. The rise of deepfakes, leveraging techniques like Variational Autoencoders (VAEs), Generative Adversarial Networks (GANs), Diffusion models and other generative models, presents significant threats to privacy, security, and democracy. This fake media can deceive individuals, discredit real people and organizations, facilitate blackmail, and even threaten the integrity of legal, political, and social systems. Therefore, finding appropriate solutions to counter the potential threats posed by this technology is essential. We explore various deepfake methods, including face swapping, voice conversion, reenactment and lip synchronization, highlighting their applications in both benign and malicious contexts. The review critically examines the ongoing "arms race" between deepfake generation and detection, analyzing the challenges in identifying manipulated contents. By examining current methods and highlighting future research directions, this paper contributes to a crucial understanding of this rapidly evolving field and the urgent need for robust detection strategies to counter the misuse of this powerful technology. While focusing primarily on audio, image, and video domains, this study allows the reader to easily grasp the latest advancements in deepfake generation and detection.

</details>

#### [Multi-Level Feature Dynamic Fusion Neural Radiance Fields for Audio-Driven Talking Head Generation](https://www.semanticscholar.org/paper/9e27ca01577afb9eba72b34aa9acfc6b61f93ee2)
**Wenchao Song, Qiong Liu, Yanchao Liu, Pengzhou Zhang et al.** · 2025-01-06

<details>
<summary>Abstract</summary>

Audio-driven cross-modal talking head generation has experienced significant advancement in the last several years, and it aims to generate a talking head video that corresponds to a given audio sequence. Out of these approaches, the NeRF-based method can generate videos featuring a specific person with more natural motion compared to the one-shot methods. However, previous approaches failed to distinguish the importance of different regions, resulting in the loss of information-rich region features. To alleviate the problem and improve video quality, we propose MLDF-NeRF, an end-to-end method for talking head generation, which can achieve better vector representation through multi-level feature dynamic fusion. Specifically, we designed two modules in MLDF-NeRF to enhance the cross-modal mapping ability between audio and different facial regions. We initially developed a multi-level tri-plane hash representation that uses three sets of tri-plane hash networks with varying resolutions of limitation to capture the dynamic information of the face more accurately. Then, we introduce the idea of multi-head attention and design an efficient audio-visual fusion module that explicitly fuses audio features with image features from different planes, thereby improving the mapping between audio features and spatial information. Meanwhile, the design helps to minimize interference from facial areas unrelated to audio, thereby improving the overall quality of the representation. The quantitative and qualitative results indicate that our proposed method can effectively generate talk heads with natural actions and realistic details. Compared with previous methods, it performs better in terms of image quality, lip sync, and other aspects.

</details>

#### [MoEE: Mixture of Emotion Experts for Audio-Driven Portrait Animation](https://arxiv.org/abs/2501.01808)
**Huaize Liu, Wenzhang Sun, Donglin Di, Shibo Sun et al.** · 2025-01-03

<details>
<summary>Abstract</summary>

The generation of talking avatars has achieved significant advancements in precise audio synchronization. However, crafting lifelike talking head videos requires capturing a broad spectrum of emotions and subtle facial expressions. Current methods face fundamental challenges: a) the absence of frameworks for modeling single basic emotional expressions, which restricts the generation of complex emotions such as compound emotions; b) the lack of comprehensive datasets rich in human emotional expressions, which limits the potential of models. To address these challenges, we propose the following innovations: 1) the Mixture of Emotion Experts (MoEE) model, which decouples six fundamental emotions to enable the precise synthesis of both singular and compound emotional states; 2) the DH-FaceEmoVid-150 dataset, specifically curated to include six prevalent human emotional expressions as well as four types of compound emotions, thereby expanding the training potential of emotion-driven models. Furthermore, to enhance the flexibility of emotion control, we propose an emotion-to-latents module that leverages multimodal inputs, aligning diverse control signals-such as audio, text, and labels-to ensure more varied control inputs as well as the ability to control emotions using audio alone. Through extensive quantitative and qualitative evaluations, we demonstrate that the MoEE framework, in conjunction with the DH-FaceEmoVid-150 dataset, excels in generating complex emotional expressions and nuanced facial details, setting a new benchmark in the field. These datasets will be publicly released.

</details>

#### [Decoupled Two-Stage Talking Head Generation via Gaussian-Landmark-Based Neural Radiance Fields](https://www.semanticscholar.org/paper/64ce7c264dd66ece77fff4210891dd4aadc3d2bb)
**Bo-Yao Ma, Yuanping Cao, Lei Zhang** · 2025-01-01

<details>
<summary>Abstract</summary>

—Talking head generation based on neural radiance fields (NeRF) has gained prominence, primarily owing to its implicit 3D representation capabilities within neural networks. However, most NeRF-based methods often intertwine audio-to-video conversion in a joint training process, resulting in challenges such as inadequate lip synchronization, limited learning efficiency, large memory requirement and lack of editability. In response to these issues, this paper introduces a fully decoupled NeRF-based method for generating talking head. This method separates the audio-to-video conversion into two stages through the use of facial landmarks. Notably, the Transformer network is used to establish the cross-modal connection between audio and landmarks effectively and generate landmarks conforming to the distribution of training data. Then, these landmarks are combined with Gaussian relative position coding to refine the sampling points on the rays, thereby constructing a dynamic neural radiation field conditioned on these landmarks for rendering the generated head. This decoupled setup enhances both the fidelity and flexibility of mapping audio to video with two independent small-scale networks. Additionally, it supports the generation of the torso part from the head-only image with deformable convolution, further enhancing the realism of the generated talking head. The experimental results demonstrate that our method excels in producing lifelike talking head, and the lightweight neural network models also exhibit superior speed and learning efficiency with less memory requirement.

</details>

#### [SynGauss: Real-Time 3D Gaussian Splatting for Audio-Driven Talking Head Synthesis](https://www.semanticscholar.org/paper/6e6d84175ff8896354892e3f0c20a196bde8a9ab)
**Zhanyi Zhou, Quandong Feng, Hongjun Li** · 2025-01-01

<details>
<summary>Abstract</summary>

In the field of virtual human generation, Neural Radiance Fields (NeRF) have made significant strides in precise geometric modeling and color accuracy, establishing new benchmarks for complex viewpoint synthesis and 3D reconstruction. Despite these advancements, existing methods face substantial limitations in real-time dynamic facial expression capture and managing high-frequency details, particularly in rapid facial movements and accurate lip synchronization. These constraints are largely due to the high computational load and the dense data requirements hamper real-time rendering. Additionally, traditional radiance fields struggle to capture subtle facial changes driven by audio, often resulting in animations that lack expressiveness and naturalness. Building upon the foundation laid by TalkingGaussian,this paper introduces an advanced framework named SynGauss that employs 3D Gaussian Splatting to precisely decouple facial and lip movements. We have enhanced this approach by incorporating lip expression coefficients and a regional multi-head attention mechanism, which allow for detailed and controlled animation of complex facial dynamics. Our modifications provide a more refined control over lip movements and facial expressions, significantly improving the realism and expressiveness of the animations while maintaining the efficiency required for real-time applications. This approach holds great promise for real-time applications such as virtual assistants and immersive entertainment experiences, offering more realistic and controllable animation generation.(Project address https://github.com/zzyfight0703/SynGauss/tree/main)

</details>

</details>

<details open>
<summary><h3>2024</h3></summary>

#### [Seeing the Sound: Multilingual Lip Sync for Real-Time Face-to-Face Translation](https://www.semanticscholar.org/paper/b3ad6e15a53015028e88171e6baf21bca5eb5682)
**A. Oskooei, Mehmet S. Aktas, Mustafa Keles** · 2024-12-28

<details>
<summary>Abstract</summary>

Imagine a future where language is no longer a barrier to real-time conversations, enabling instant and lifelike communication across the globe. As cultural boundaries blur, the demand for seamless multilingual communication has become a critical technological challenge. This paper addresses the lack of robust solutions for real-time face-to-face translation, particularly for low-resource languages, by introducing a comprehensive framework that not only translates language but also replicates voice nuances and synchronized facial expressions. Our research tackles the primary challenge of achieving accurate lip synchronization across culturally diverse languages, filling a significant gap in the literature by evaluating the generalizability of lip sync models beyond English. Specifically, we develop a novel evaluation framework combining quantitative lip sync error metrics and qualitative assessments by human observers. This framework is applied to assess two state-of-the-art lip sync models with different architectures for Turkish, Persian, and Arabic languages, using a newly collected dataset. Based on these findings, we propose and implement a modular system that integrates language-agnostic lip sync models with neural networks to deliver a fully functional face-to-face translation experience. Inference Time Analysis shows this system achieves highly realistic, face-translated talking heads in real time, with a throughput as low as 0.381 s. This transformative framework is primed for deployment in immersive environments such as VR/AR, Metaverse ecosystems, and advanced video conferencing platforms. It offers substantial benefits to developers and businesses aiming to build next-generation multilingual communication systems for diverse applications. While this work focuses on three languages, its modular design allows scalability to additional languages. However, further testing in broader linguistic and cultural contexts is required to confirm its universal applicability, paving the way for a more interconnected and inclusive world where language ceases to hinder human connection.

</details>

#### [Joint Co-Speech Gesture and Expressive Talking Face Generation using Diffusion with Adapters](https://arxiv.org/abs/2412.14333)
**Steven Hogue, Chenxu Zhang, Yapeng Tian, Xiaohu Guo** · 2024-12-18

<details>
<summary>Abstract</summary>

Recent advances in co-speech gesture and talking head generation have been impressive, yet most methods focus on only one of the two tasks. Those that attempt to generate both often rely on separate models or network modules, increasing training complexity and ignoring the inherent relationship between face and body movements. To address the challenges, in this paper, we propose a novel model architecture that jointly generates face and body motions within a single network. This approach leverages shared weights between modalities, facilitated by adapters that enable adaptation to a common latent space. Our experiments demonstrate that the proposed framework not only maintains state-of-the-art co-speech gesture and talking head generation performance but also significantly reduces the number of parameters required.

</details>

#### [GLCF: A Global-Local Multimodal Coherence Analysis Framework for Talking Face Generation Detection](https://arxiv.org/abs/2412.13656)
**Xiaocan Chen, Qilin Yin, Jiarui Liu, Wei Lu et al.** · 2024-12-18

<details>
<summary>Abstract</summary>

Talking face generation (TFG) allows for producing lifelike talking videos of any character using only facial images and accompanying text. Abuse of this technology could pose significant risks to society, creating the urgent need for research into corresponding detection methods. However, research in this field has been hindered by the lack of public datasets. In this paper, we construct the first large-scale multi-scenario talking face dataset (MSTF), which contains 22 audio and video forgery techniques, filling the gap of datasets in this field. The dataset covers 11 generation scenarios and more than 20 semantic scenarios, closer to the practical application scenario of TFG. Besides, we also propose a TFG detection framework, which leverages the analysis of both global and local coherence in the multimodal content of TFG videos. Therefore, a region-focused smoothness detection module (RSFDM) and a discrepancy capture-time frame aggregation module (DCTAM) are introduced to evaluate the global temporal coherence of TFG videos, aggregating multi-grained spatial information. Additionally, a visual-audio fusion module (V-AFM) is designed to evaluate audiovisual coherence within a localized temporal perspective. Comprehensive experiments demonstrate the reasonableness and challenges of our datasets, while also indicating the superiority of our proposed method compared to the state-of-the-art deepfake detection approaches.

</details>

#### [GRS-Wav2lip: General Speech-Driven Lip Synthesis in the Wild](https://www.semanticscholar.org/paper/5b6e1322be854160160f8f8201a478fc5839be3c)
**Junda Wu, Donghan Ye, Lijun Fu, Zixuan Zhang** · 2024-12-13

<details>
<summary>Abstract</summary>

In recent years, advancements in virtual digital human technology have accelerated considerably; however, many existing lip synchronization models lack adequate focus on lip details, often leading to asynchrony between speech and lip movements. This paper introduces a novel method, GRS- Wav2Lip, designed to enhance the naturalness and synchronization of generated talking face videos. We have restructured the convolutional layers of the identity encoder within the generator, replacing standard convolutional layers with gated convolutions to improve the model's ability to capture lip-related details and motion-specific features effectively. Additionally, we introduce the SAC module to dynamically adjust the receptive field, enabling the effective capture of both global and local features. To improve resolution and image detail, we integrate the RRDB module, which significantly enhances image quality even with low-resolution inputs. Finally, we employ the LPIPS loss function to accurately measure the perceptual quality of generated images. Experimental results show that our approach not only strengthens the model's generative capacity but also leads to substantial improvements in lip synchronization and image detail quality.

</details>

#### [LatentSync: Taming Audio-Conditioned Latent Diffusion Models for Lip Sync with SyncNet Supervision](https://arxiv.org/abs/2412.09262)
**Chunyu Li, Chao Zhang, Weikai Xu, Jingyu Lin et al.** · 2024-12-12

<details>
<summary>Abstract</summary>

End-to-end audio-conditioned latent diffusion models (LDMs) have been widely adopted for audio-driven portrait animation, demonstrating their effectiveness in generating lifelike and high-resolution talking videos. However, direct application of audio-conditioned LDMs to lip-synchronization (lip-sync) tasks results in suboptimal lip-sync accuracy. Through an in-depth analysis, we identified the underlying cause as the "shortcut learning problem", wherein the model predominantly learns visual-visual shortcuts while neglecting the critical audio-visual correlations. To address this issue, we explored different approaches for integrating SyncNet supervision into audio-conditioned LDMs to explicitly enforce the learning of audio-visual correlations. Since the performance of SyncNet directly influences the lip-sync accuracy of the supervised model, the training of a well-converged SyncNet becomes crucial. We conducted the first comprehensive empirical studies to identify key factors affecting SyncNet convergence. Based on our analysis, we introduce StableSyncNet, with an architecture designed for stable convergence. Our StableSyncNet achieved a significant improvement in accuracy, increasing from 91% to 94% on the HDTF test set. Additionally, we introduce a novel Temporal Representation Alignment (TREPA) mechanism to enhance temporal consistency in the generated videos. Experimental results show that our method surpasses state-of-the-art lip-sync approaches across various evaluation metrics on the HDTF and VoxCeleb2 datasets.

</details>

#### [GoHD: Gaze-oriented and Highly Disentangled Portrait Animation with Rhythmic Poses and Realistic Expression](https://arxiv.org/abs/2412.09296)
**Ziqi Zhou, Weize Quan, Hailin Shi, Wei Li et al.** · 2024-12-12

<details>
<summary>Abstract</summary>

Audio-driven talking head generation necessitates seamless integration of audio and visual data amidst the challenges posed by diverse input portraits and intricate correlations between audio and facial motions. In response, we propose a robust framework GoHD designed to produce highly realistic, expressive, and controllable portrait videos from any reference identity with any motion. GoHD innovates with three key modules: Firstly, an animation module utilizing latent navigation is introduced to improve the generalization ability across unseen input styles. This module achieves high disentanglement of motion and identity, and it also incorporates gaze orientation to rectify unnatural eye movements that were previously overlooked. Secondly, a conformer-structured conditional diffusion model is designed to guarantee head poses that are aware of prosody. Thirdly, to estimate lip-synchronized and realistic expressions from the input audio within limited training data, a two-stage training strategy is devised to decouple frequent and frame-wise lip motion distillation from the generation of other more temporally dependent but less audio-related motions, e.g., blinks and frowns. Extensive experiments validate GoHD's advanced generalization capabilities, demonstrating its effectiveness in generating realistic talking face results on arbitrary subjects.

</details>

#### [PortraitTalk: Towards Customizable One-Shot Audio-to-Talking Face Generation](https://arxiv.org/abs/2412.07754)
**Fatemeh Nazarieh, Zhenhua Feng, Diptesh Kanojia, Muhammad Awais et al.** · 2024-12-10

<details>
<summary>Abstract</summary>

Audio-driven talking face generation is a challenging task in digital communication. Despite significant progress in the area, most existing methods concentrate on audio-lip synchronization, often overlooking aspects such as visual quality, customization, and generalization that are crucial to producing realistic talking faces. To address these limitations, we introduce a novel, customizable one-shot audio-driven talking face generation framework, named PortraitTalk. Our proposed method utilizes a latent diffusion framework consisting of two main components: IdentityNet and AnimateNet. IdentityNet is designed to preserve identity features consistently across the generated video frames, while AnimateNet aims to enhance temporal coherence and motion consistency. This framework also integrates an audio input with the reference images, thereby reducing the reliance on reference-style videos prevalent in existing approaches. A key innovation of PortraitTalk is the incorporation of text prompts through decoupled cross-attention mechanisms, which significantly expands creative control over the generated videos. Through extensive experiments, including a newly developed evaluation metric, our model demonstrates superior performance over the state-of-the-art methods, setting a new standard for the generation of customizable realistic talking faces suitable for real-world applications.

</details>

#### [Emotional Synchronization for Audio-Driven Talking-Head Generation](https://www.semanticscholar.org/paper/2db415c4afcf4caa5ba6d3402e2a9a839fc5f3d0)
**Zhao Zhang, Yan Luo, Zhichao Zuo, Richang Hong et al.** · 2024-12-09

<details>
<summary>Abstract</summary>

Audio-driven talking-head synthesis has become a significant focus in the field of virtual human applications. However, existing methodologies face challenges in effectively synchronizing audio and video, especially in maintaining emotional consistency. Additionally, there is a notable inefficiency in leveraging emotional prompts to guide expression generation. To address these limitations, this paper introduces an Emotion Synchronized audio-driven Talking-head synthesis (EST) approach. The EST approach aims to enhance the emotion-agnostic talking-head models by enabling emotion control, and it incorporates a diffusion module to learn diverse latent rep-resentations. Furthermore, EST utilizes null-text embedding to align the latent code with emotional prompts. Additionally, a novel Sync Attention Block (SAB) is developed to broaden the spatial perceptual field, thus preventing the loss of critical information. Extensive experiments demonstrate the effectiveness of the EST method, showcasing state-of-the-art performance across widely-adopted datasets. Moreover, the EST approach exhibits exceptional generalization capabilities, even in scenarios where emotional training videos are unavailable.

</details>

#### [MEMO: Memory-Guided Diffusion for Expressive Talking Video Generation](https://arxiv.org/abs/2412.04448)
**Longtao Zheng, Yifan Zhang, Hanzhong Guo, Jiachun Pan et al.** · 2024-12-05

<details>
<summary>Abstract</summary>

Recent advances in video diffusion models have unlocked new potential for realistic audio-driven talking video generation. However, achieving seamless audio-lip synchronization, maintaining long-term identity consistency, and producing natural, audio-aligned expressions in generated talking videos remain significant challenges. To address these challenges, we propose Memory-guided EMOtion-aware diffusion (MEMO), an end-to-end audio-driven portrait animation approach to generate identity-consistent and expressive talking videos. Our approach is built around two key modules: (1) a memory-guided temporal module, which enhances long-term identity consistency and motion smoothness by developing memory states to store information from a longer past context to guide temporal modeling via linear attention; and (2) an emotion-aware audio module, which replaces traditional cross attention with multi-modal attention to enhance audio-video interaction, while detecting emotions from audio to refine facial expressions via emotion adaptive layer norm. Extensive quantitative and qualitative results demonstrate that MEMO generates more realistic talking videos across diverse image and audio types, outperforming state-of-the-art methods in overall quality, audio-lip synchronization, identity consistency, and expression-emotion alignment.

</details>

#### [IF-MDM: Implicit Face Motion Diffusion Model for High-Fidelity Realtime Talking Head Generation](https://arxiv.org/abs/2412.04000)
**Sejong Yang, Seoung Wug Oh, Yang Zhou, Seon Joo Kim** · 2024-12-05

<details>
<summary>Abstract</summary>

We introduce a novel approach for high-resolution talking head generation from a single image and audio input. Prior methods using explicit face models, like 3D morphable models (3DMM) and facial landmarks, often fall short in generating high-fidelity videos due to their lack of appearance-aware motion representation. While generative approaches such as video diffusion models achieve high video quality, their slow processing speeds limit practical application. Our proposed model, Implicit Face Motion Diffusion Model (IF-MDM), employs implicit motion to encode human faces into appearance-aware compressed facial latents, enhancing video generation. Although implicit motion lacks the spatial disentanglement of explicit models, which complicates alignment with subtle lip movements, we introduce motion statistics to help capture fine-grained motion information. Additionally, our model provides motion controllability to optimize the trade-off between motion intensity and visual quality during inference. IF-MDM supports real-time generation of 512x512 resolution videos at up to 45 frames per second (fps). Extensive evaluations demonstrate its superior performance over existing diffusion and explicit face models. The code will be released publicly, available alongside supplementary materials. The video results can be found on https://bit.ly/ifmdm_supplementary.

</details>

#### [SINGER: Vivid Audio-driven Singing Video Generation with Multi-scale Spectral Diffusion Model](https://arxiv.org/abs/2412.03430)
**Yan Li, Ziya Zhou, Zhiqiang Wang, Wei Xue et al.** · 2024-12-04

<details>
<summary>Abstract</summary>

Recent advancements in generative models have significantly enhanced talking face video generation, yet singing video generation remains underexplored. The differences between human talking and singing limit the performance of existing talking face video generation models when applied to singing. The fundamental differences between talking and singing-specifically in audio characteristics and behavioral expressions-limit the effectiveness of existing models. We observe that the differences between singing and talking audios manifest in terms of frequency and amplitude. To address this, we have designed a multi-scale spectral module to help the model learn singing patterns in the spectral domain. Additionally, we develop a spectral-filtering module that aids the model in learning the human behaviors associated with singing audio. These two modules are integrated into the diffusion model to enhance singing video generation performance, resulting in our proposed model, SINGER. Furthermore, the lack of high-quality real-world singing face videos has hindered the development of the singing video generation community. To address this gap, we have collected an in-the-wild audio-visual singing dataset to facilitate research in this area. Our experiments demonstrate that SINGER is capable of generating vivid singing videos and outperforms state-of-the-art methods in both objective and subjective evaluations.

</details>

#### [Synergizing Motion and Appearance: Multi-Scale Compensatory Codebooks for Talking Head Video Generation](https://arxiv.org/abs/2412.00719)
**Shuling Zhao, Fa-Ting Hong, Xiaoshui Huang, Dan Xu** · 2024-12-01

<details>
<summary>Abstract</summary>

Talking head video generation aims to generate a realistic talking head video that preserves the person's identity from a source image and the motion from a driving video. Despite the promising progress made in the field, it remains a challenging and critical problem to generate videos with accurate poses and fine-grained facial details simultaneously. Essentially, facial motion is often highly complex to model precisely, and the one-shot source face image cannot provide sufficient appearance guidance during generation due to dynamic pose changes. To tackle the problem, we propose to jointly learn motion and appearance codebooks and perform multi-scale codebook compensation to effectively refine both the facial motion conditions and appearance features for talking face image decoding. Specifically, the designed multi-scale motion and appearance codebooks are learned simultaneously in a unified framework to store representative global facial motion flow and appearance patterns. Then, we present a novel multi-scale motion and appearance compensation module, which utilizes a transformer-based codebook retrieval strategy to query complementary information from the two codebooks for joint motion and appearance compensation. The entire process produces motion flows of greater flexibility and appearance features with fewer distortions across different scales, resulting in a high-quality talking head video generation framework. Extensive experiments on various benchmarks validate the effectiveness of our approach and demonstrate superior generation results from both qualitative and quantitative perspectives when compared to state-of-the-art competitors.

</details>

#### [LokiTalk: Learning Fine-Grained and Generalizable Correspondences to Enhance NeRF-based Talking Head Synthesis](https://arxiv.org/abs/2411.19525)
**Tianqi Li, Ruobing Zheng, Bonan Li, Zicheng Zhang et al.** · 2024-11-29

<details>
<summary>Abstract</summary>

Despite significant progress in talking head synthesis since the introduction of Neural Radiance Fields (NeRF), visual artifacts and high training costs persist as major obstacles to large-scale commercial adoption. We propose that identifying and establishing fine-grained and generalizable correspondences between driving signals and generated results can simultaneously resolve both problems. Here we present LokiTalk, a novel framework designed to enhance NeRF-based talking heads with lifelike facial dynamics and improved training efficiency. To achieve fine-grained correspondences, we introduce Region-Specific Deformation Fields, which decompose the overall portrait motion into lip movements, eye blinking, head pose, and torso movements. By hierarchically modeling the driving signals and their associated regions through two cascaded deformation fields, we significantly improve dynamic accuracy and minimize synthetic artifacts. Furthermore, we propose ID-Aware Knowledge Transfer, a plug-and-play module that learns generalizable dynamic and static correspondences from multi-identity videos, while simultaneously extracting ID-specific dynamic and static features to refine the depiction of individual characters. Comprehensive evaluations demonstrate that LokiTalk delivers superior high-fidelity results and training efficiency compared to previous methods. The code will be released upon acceptance.

</details>

#### [Ditto: Motion-Space Diffusion for Controllable Realtime Talking Head Synthesis](https://arxiv.org/abs/2411.19509)
**Tianqi Li, Ruobing Zheng, Minghui Yang, Jingdong Chen et al.** · 2024-11-29

<details>
<summary>Abstract</summary>

Recent advances in diffusion models have endowed talking head synthesis with subtle expressions and vivid head movements, but have also led to slow inference speed and insufficient control over generated results. To address these issues, we propose Ditto, a diffusion-based talking head framework that enables fine-grained controls and real-time inference. Specifically, we utilize an off-the-shelf motion extractor and devise a diffusion transformer to generate representations in a specific motion space. We optimize the model architecture and training strategy to address the issues in generating motion representations, including insufficient disentanglement between motion and identity, and large internal discrepancies within the representation. Besides, we employ diverse conditional signals while establishing a mapping between motion representation and facial semantics, enabling control over the generation process and correction of the results. Moreover, we jointly optimize the holistic framework to enable streaming processing, real-time inference, and low first-frame delay, offering functionalities crucial for interactive applications such as AI assistants. Extensive experimental results demonstrate that Ditto generates compelling talking head videos and exhibits superiority in both controllability and real-time performance.

</details>

#### [V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow](https://arxiv.org/abs/2411.19486)
**Jeongsoo Choi, Ji-Hoon Kim, Jinyu Li, Joon Son Chung et al.** · 2024-11-29

<details>
<summary>Abstract</summary>

In this paper, we introduce V2SFlow, a novel Video-to-Speech (V2S) framework designed to generate natural and intelligible speech directly from silent talking face videos. While recent V2S systems have shown promising results on constrained datasets with limited speakers and vocabularies, their performance often degrades on real-world, unconstrained datasets due to the inherent variability and complexity of speech signals. To address these challenges, we decompose the speech signal into manageable subspaces (content, pitch, and speaker information), each representing distinct speech attributes, and predict them directly from the visual input. To generate coherent and realistic speech from these predicted attributes, we employ a rectified flow matching decoder built on a Transformer architecture, which models efficient probabilistic pathways from random noise to the target speech distribution. Extensive experiments demonstrate that V2SFlow significantly outperforms state-of-the-art methods, even surpassing the naturalness of ground truth utterances. Code and models are available at: https://github.com/kaistmm/V2SFlow

</details>

#### [EmotiveTalk: Expressive Talking Head Generation through Audio Information Decoupling and Emotional Video Diffusion](https://arxiv.org/abs/2411.16726)
**Haotian Wang, Yuzhe Weng, Yueyan Li, Zilu Guo et al.** · 2024-11-23

<details>
<summary>Abstract</summary>

Diffusion models have revolutionized the field of talking head generation, yet still face challenges in expressiveness, controllability, and stability in long-time generation. In this research, we propose an EmotiveTalk framework to address these issues. Firstly, to realize better control over the generation of lip movement and facial expression, a Vision-guided Audio Information Decoupling (V-AID) approach is designed to generate audio-based decoupled representations aligned with lip movements and expression. Specifically, to achieve alignment between audio and facial expression representation spaces, we present a Diffusion-based Co-speech Temporal Expansion (Di-CTE) module within V-AID to generate expression-related representations under multi-source emotion condition constraints. Then we propose a well-designed Emotional Talking Head Diffusion (ETHD) backbone to efficiently generate highly expressive talking head videos, which contains an Expression Decoupling Injection (EDI) module to automatically decouple the expressions from reference portraits while integrating the target expression information, achieving more expressive generation performance. Experimental results show that EmotiveTalk can generate expressive talking head videos, ensuring the promised controllability of emotions and stability during long-time generation, yielding state-of-the-art performance compared to existing methods.

</details>

#### [ConsistentAvatar: Learning to Diffuse Fully Consistent Talking Head Avatar with Temporal Guidance](https://arxiv.org/abs/2411.15436)
**Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian et al.** · 2024-11-23

<details>
<summary>Abstract</summary>

Diffusion models have shown impressive potential on talking head generation. While plausible appearance and talking effect are achieved, these methods still suffer from temporal, 3D or expression inconsistency due to the error accumulation and inherent limitation of single-image generation ability. In this paper, we propose ConsistentAvatar, a novel framework for fully consistent and high-fidelity talking avatar generation. Instead of directly employing multi-modal conditions to the diffusion process, our method learns to first model the temporal representation for stability between adjacent frames. Specifically, we propose a Temporally-Sensitive Detail (TSD) map containing high-frequency feature and contours that vary significantly along the time axis. Using a temporal consistent diffusion module, we learn to align TSD of the initial result to that of the video frame ground truth. The final avatar is generated by a fully consistent diffusion module, conditioned on the aligned TSD, rough head normal, and emotion prompt embedding. We find that the aligned TSD, which represents the temporal patterns, constrains the diffusion process to generate temporally stable talking head. Further, its reliable guidance complements the inaccuracy of other conditions, suppressing the accumulated error while improving the consistency on various aspects. Extensive experiments demonstrate that ConsistentAvatar outperforms the state-of-the-art methods on the generated appearance, 3D, expression and temporal consistency. Project page: https://njust-yang.github.io/ConsistentAvatar.github.io/

</details>

#### [Specialized Face Encoder for Audio-based Speech to Lip Generation](https://www.semanticscholar.org/paper/3cce025710c271851749ef988b732151d7becee6)
**Miaoyi Li, Dawei Dai, Lanyu Xue, Pengju Tang** · 2024-11-22

<details>
<summary>Abstract</summary>

Videos that are directly translated and dubbed often fail to provide a natural audiovisual experience, making it crucial to develop methods that can accurately generate lip movements to match the audio. Self-supervised learning models like MAE have proven their robust transfer capabilities. This paper employs the pretraining method of MAE and proposes a new automatic lip-sync network. Additionally, we introduce a separate perceptual loss for the lip region of the generated faces to ensure accurate and clear lip movements. Our automatic lip-sync network consists of four components: video preprocessing, audio preprocessing, generator, and lip-sync discriminator, using facial images and audio features as inputs. We trained an MAE encoder and integrated it into the lip generator. The system was tested on two audiovisual datasets, and the results demonstrate that our proposed method achieves superior performance in both the visual quality of generated talking faces and their synchronization with the audio.

</details>

#### [LES-Talker: Fine-Grained Emotion Editing for Talking Head Generation in Linear Emotion Space](https://arxiv.org/abs/2411.09268)
**Guanwen Feng, Zhihao Qian, Yunan Li, Siyu Jin et al.** · 2024-11-14

<details>
<summary>Abstract</summary>

While existing one-shot talking head generation models have achieved progress in coarse-grained emotion editing, there is still a lack of fine-grained emotion editing models with high interpretability. We argue that for an approach to be considered fine-grained, it needs to provide clear definitions and sufficiently detailed differentiation. We present LES-Talker, a novel one-shot talking head generation model with high interpretability, to achieve fine-grained emotion editing across emotion types, emotion levels, and facial units. We propose a Linear Emotion Space (LES) definition based on Facial Action Units to characterize emotion transformations as vector transformations. We design the Cross-Dimension Attention Net (CDAN) to deeply mine the correlation between LES representation and 3D model representation. Through mining multiple relationships across different feature and structure dimensions, we enable LES representation to guide the controllable deformation of 3D model. In order to adapt the multimodal data with deviations to the LES and enhance visual quality, we utilize specialized network design and training strategies. Experiments show that our method provides high visual quality along with multilevel and interpretable fine-grained emotion editing, outperforming mainstream methods.

</details>

#### [Audio-Semantic Enhanced Pose-Driven Talking Head Generation](https://www.semanticscholar.org/paper/43826e0f83cfedf6806325e950e8cbecf833b892)
**Meng Liu, Da Li, Yongqiang Li, Xuemeng Song et al.** · 2024-11-01

<details>
<summary>Abstract</summary>

Talking head generation, aiming to create photo-realistic videos from a single reference image and audio input, has emerged as a vibrant area of interest within the computer vision community. Despite notable advancements, several challenges remain unaddressed. For instance, many existing approaches overlook the nuanced relationship between audio semantics and head movement, such as nodding in agreement during affirmative expressions. Additionally, the visual quality of generated content, particularly in depicting teeth, often falls short of achieving authentic realism. To address these limitations, we introduce a groundbreaking audio-semantic enhanced pose-driven talking head generation method. Our approach encompasses a multimodal 3DMM parameter prediction network alongside a high-fidelity video synthesis network, meticulously designed to produce authentic and high-quality talking head videos. The multimodal 3DMM parameter prediction network harnesses both acoustic and audio-deduced semantic information, facilitating accurate head pose predictions that resonate with the semantics of spoken words. Furthermore, to significantly improve the depiction of the mouth area, especially the teeth, our video synthesis stage incorporates a mouth-enhanced network augmented by both local and global discriminators. Comprehensive evaluations across diverse metrics affirm the superiority of our method.

</details>

#### [Stereo-Talker: Audio-driven 3D Human Synthesis with Prior-Guided Mixture-of-Experts](https://arxiv.org/abs/2410.23836)
**Xiang Deng, Youxin Pang, Xiaochen Zhao, Chao Xu et al.** · 2024-10-31

<details>
<summary>Abstract</summary>

This paper introduces Stereo-Talker, a novel one-shot audio-driven human video synthesis system that generates 3D talking videos with precise lip synchronization, expressive body gestures, temporally consistent photo-realistic quality, and continuous viewpoint control. The process follows a two-stage approach. In the first stage, the system maps audio input to high-fidelity motion sequences, encompassing upper-body gestures and facial expressions. To enrich motion diversity and authenticity, large language model (LLM) priors are integrated with text-aligned semantic audio features, leveraging LLMs' cross-modal generalization power to enhance motion quality. In the second stage, we improve diffusion-based video generation models by incorporating a prior-guided Mixture-of-Experts (MoE) mechanism: a view-guided MoE focuses on view-specific attributes, while a mask-guided MoE enhances region-based rendering stability. Additionally, a mask prediction module is devised to derive human masks from motion data, enhancing the stability and accuracy of masks and enabling mask guiding during inference. We also introduce a comprehensive human video dataset with 2,203 identities, covering diverse body gestures and detailed annotations, facilitating broad generalization. The code, data, and pre-trained models will be released for research purposes.

</details>

#### [Multimodal Semantic Communication for Generative Audio-Driven Video Conferencing](https://arxiv.org/abs/2410.22112)
**Haonan Tong, Haopeng Li, Hongyang Du, Zhaohui Yang et al.** · 2024-10-29

<details>
<summary>Abstract</summary>

This paper studies an efficient multimodal data communication scheme for video conferencing. In our considered system, a speaker gives a talk to the audiences, with talking head video and audio being transmitted. Since the speaker does not frequently change posture and high-fidelity transmission of audio (speech and music) is required, redundant visual video data exists and can be removed by generating the video from the audio. To this end, we propose a wave-to-video (Wav2Vid) system, an efficient video transmission framework that reduces transmitted data by generating talking head video from audio. In particular, full-duration audio and short-duration video data are synchronously transmitted through a wireless channel, with neural networks (NNs) extracting and encoding audio and video semantics. The receiver then combines the decoded audio and video data, as well as uses a generative adversarial network (GAN) based model to generate the lip movement videos of the speaker. Simulation results show that the proposed Wav2Vid system can reduce the amount of transmitted data by up to 83% while maintaining the perceptual quality of the generated conferencing video.

</details>

#### [Real-time 3D-aware Portrait Video Relighting](https://arxiv.org/abs/2410.18355)
**Ziqi Cai, Kaiwen Jiang, Shu-Yu Chen, Yu-Kun Lai et al.** · 2024-10-24

<details>
<summary>Abstract</summary>

Synthesizing realistic videos of talking faces under custom lighting conditions and viewing angles benefits various downstream applications like video conferencing. However, most existing relighting methods are either time-consuming or unable to adjust the viewpoints. In this paper, we present the first real-time 3D-aware method for relighting in-the-wild videos of talking faces based on Neural Radiance Fields (NeRF). Given an input portrait video, our method can synthesize talking faces under both novel views and novel lighting conditions with a photo-realistic and disentangled 3D representation. Specifically, we infer an albedo tri-plane, as well as a shading tri-plane based on a desired lighting condition for each video frame with fast dual-encoders. We also leverage a temporal consistency network to ensure smooth transitions and reduce flickering artifacts. Our method runs at 32.98 fps on consumer-level hardware and achieves state-of-the-art results in terms of reconstruction quality, lighting error, lighting instability, temporal consistency and inference speed. We demonstrate the effectiveness and interactivity of our method on various portrait videos with diverse lighting and viewing conditions.

</details>

#### [Dynamic Region Fusion Neural Radiance Fields for Audio-Driven Talking Head Generation](https://www.semanticscholar.org/paper/1a3201b7b17d919513d915444858ab5434babcd2)
**Qiang He, Juan Cao, Haiyan Lu, Pengzhou Zhang** · 2024-10-18

<details>
<summary>Abstract</summary>

Since humans are sensitive to facial appearance and responsiveness, audio-driven talking head generation remains an ongoing challenge. The paper proposes DRMF-NeRF, a novel approach for generating audio-driven head generation by conditional Neural Radiance Fields (NeRF) audio, which can simultaneously achieve fast convergence of the model and generation of facial with natural motion. More specifically, we present an attention-based mechanism dynamic region fusion module that can effectively explore the potential connections and the degree of influence of audio on various face regions to generate a natural and accurate dynamic talking head. Furthermore, inspired by S3IM loss, we design an optimization function that combines the image pointwise loss and structural loss to enhance the quality of the generated image. Comprehensive experiments have shown that our method can generate realistic speech head videos, and its performance is superior to the baseline method.

</details>

#### [DAWN: Dynamic Frame Avatar with Non-autoregressive Diffusion Framework for Talking Head Video Generation](https://arxiv.org/abs/2410.13726)
**Hanbo Cheng, Limin Lin, Chenyu Liu, Pengcheng Xia et al.** · 2024-10-17

<details>
<summary>Abstract</summary>

Talking head generation intends to produce vivid and realistic talking head videos from a single portrait and speech audio clip. Although significant progress has been made in diffusion-based talking head generation, almost all methods rely on autoregressive strategies, which suffer from limited context utilization beyond the current generation step, error accumulation, and slower generation speed. To address these challenges, we present DAWN (Dynamic frame Avatar With Non-autoregressive diffusion), a framework that enables all-at-once generation of dynamic-length video sequences. Specifically, it consists of two main components: (1) audio-driven holistic facial dynamics generation in the latent motion space, and (2) audio-driven head pose and blink generation. Extensive experiments demonstrate that our method generates authentic and vivid videos with precise lip motions, and natural pose/blink movements. Additionally, with a high generation speed, DAWN possesses strong extrapolation capabilities, ensuring the stable production of high-quality long videos. These results highlight the considerable promise and potential impact of DAWN in the field of talking head video generation. Furthermore, we hope that DAWN sparks further exploration of non-autoregressive approaches in diffusion models. Our code will be publicly available at https://github.com/Hanbo-Cheng/DAWN-pytorch.

</details>

#### [Beyond Fixed Topologies: Unregistered Training and Comprehensive Evaluation Metrics for 3D Talking Heads](https://arxiv.org/abs/2410.11041)
**Federico Nocentini, Thomas Besnier, Claudio Ferrari, Sylvain Arguillere et al.** · 2024-10-14

<details>
<summary>Abstract</summary>

Generating speech-driven 3D talking heads presents numerous challenges; among those is dealing with varying mesh topologies where no point-wise correspondence exists across the meshes the model can animate. While previous literature works assume fixed mesh structures, in this work we present the first framework capable of animating 3D faces in arbitrary topologies, including real scanned data. Our approach leverages heat diffusion to predict features that are robust to the mesh topology. We explore two training settings: a registered one, in which meshes in a training sequences share a fixed topology but any mesh can be animated at test time, and an fully unregistered one, which allows effective training with varying mesh structures. Additionally, we highlight the limitations of current evaluation metrics and propose new metrics for better lip-syncing evaluation. An extensive evaluation shows our approach performs favorably compared to fixed topology techniques, setting a new benchmark by offering a versatile and high-fidelity solution for 3D talking heads where the topology constraint is dropped. The code along with the pre-trained model are available.

</details>

#### [MuseTalk: Real-Time High-Fidelity Video Dubbing via Spatio-Temporal Sampling](https://arxiv.org/abs/2410.10122)
**Yue Zhang, Zhizhou Zhong, Minhao Liu, Zhaokang Chen et al.** · 2024-10-14

<details>
<summary>Abstract</summary>

Real-time video dubbing that preserves identity consistency while achieving accurate lip synchronization remains a critical challenge. Existing approaches face a trilemma: diffusion-based methods achieve high visual fidelity but suffer from prohibitive computational costs, while GAN-based solutions sacrifice lip-sync accuracy or dental details for real-time performance. We present MuseTalk, a novel two-stage training framework that resolves this trade-off through latent space optimization and spatio-temporal data sampling strategy. Our key innovations include: (1) During the Facial Abstract Pretraining stage, we propose Informative Frame Sampling to temporally align reference-source pose pairs, eliminating redundant feature interference while preserving identity cues. (2) In the Lip-Sync Adversarial Finetuning stage, we employ Dynamic Margin Sampling to spatially select the most suitable lip-movement-promoting regions, balancing audio-visual synchronization and dental clarity. (3) MuseTalk establishes an effective audio-visual feature fusion framework in the latent space, delivering 30 FPS output at 256*256 resolution on an NVIDIA V100 GPU. Extensive experiments demonstrate that MuseTalk outperforms state-of-the-art methods in visual fidelity while achieving comparable lip-sync accuracy. %The codes and models will be made publicly available upon acceptance. The code is made available at \href{https://github.com/TMElyralab/MuseTalk}{https://github.com/TMElyralab/MuseTalk}

</details>

#### [MimicTalk: Mimicking a personalized and expressive 3D talking face in minutes](https://arxiv.org/abs/2410.06734)
**Zhenhui Ye, Tianyun Zhong, Yi Ren, Ziyue Jiang et al.** · 2024-10-09

<details>
<summary>Abstract</summary>

Talking face generation (TFG) aims to animate a target identity's face to create realistic talking videos. Personalized TFG is a variant that emphasizes the perceptual identity similarity of the synthesized result (from the perspective of appearance and talking style). While previous works typically solve this problem by learning an individual neural radiance field (NeRF) for each identity to implicitly store its static and dynamic information, we find it inefficient and non-generalized due to the per-identity-per-training framework and the limited training data. To this end, we propose MimicTalk, the first attempt that exploits the rich knowledge from a NeRF-based person-agnostic generic model for improving the efficiency and robustness of personalized TFG. To be specific, (1) we first come up with a person-agnostic 3D TFG model as the base model and propose to adapt it into a specific identity; (2) we propose a static-dynamic-hybrid adaptation pipeline to help the model learn the personalized static appearance and facial dynamic features; (3) To generate the facial motion of the personalized talking style, we propose an in-context stylized audio-to-motion model that mimics the implicit talking style provided in the reference video without information loss by an explicit style representation. The adaptation process to an unseen identity can be performed in 15 minutes, which is 47 times faster than previous person-dependent methods. Experiments show that our MimicTalk surpasses previous baselines regarding video quality, efficiency, and expressiveness. Source code and video samples are available at https://mimictalk.github.io .

</details>

#### [EmoGene: Audio-Driven Emotional 3D Talking-Head Generation](https://arxiv.org/abs/2410.17262)
**Wenqing Wang, Yun Fu** · 2024-10-07

<details>
<summary>Abstract</summary>

Audio-driven talking-head generation is a crucial and useful technology for virtual human interaction and film-making. While recent advances have focused on improving image fidelity and lip synchronization, generating accurate emotional expressions remains underexplored. In this paper, we introduce EmoGene, a novel framework for synthesizing high-fidelity, audio-driven video portraits with accurate emotional expressions. Our approach employs a variational autoencoder (VAE)-based audio-to-motion module to generate facial landmarks, which are concatenated with emotional embedding in a motion-to-emotion module to produce emotional landmarks. These landmarks drive a Neural Radiance Fields (NeRF)-based emotion-to-video module to render realistic emotional talking-head videos. Additionally, we propose a pose sampling method to generate natural idle-state (non-speaking) videos for silent audio inputs. Extensive experiments demonstrate that EmoGene outperforms previous methods in generating high-fidelity emotional talking-head videos.

</details>

#### [Diffusion-based Unsupervised Audio-visual Speech Enhancement](https://arxiv.org/abs/2410.05301)
**Jean-Eudes Ayilo, Mostafa Sadeghi, Romain Serizel, Xavier Alameda-Pineda** · 2024-10-04

<details>
<summary>Abstract</summary>

This paper proposes a new unsupervised audio-visual speech enhancement (AVSE) approach that combines a diffusion-based audio-visual speech generative model with a non-negative matrix factorization (NMF) noise model. First, the diffusion model is pre-trained on clean speech conditioned on corresponding video data to simulate the speech generative distribution. This pre-trained model is then paired with the NMF-based noise model to estimate clean speech iteratively. Specifically, a diffusion-based posterior sampling approach is implemented within the reverse diffusion process, where after each iteration, a speech estimate is obtained and used to update the noise parameters. Experimental results confirm that the proposed AVSE approach not only outperforms its audio-only counterpart but also generalizes better than a recent supervised-generative AVSE method. Additionally, the new inference algorithm offers a better balance between inference speed and performance compared to the previous diffusion-based method. Code and demo available at: https://jeaneudesayilo.github.io/fast_UdiffSE

</details>

#### [Lipschitz-Driven Noise Robustness in VQ-AE for High-Frequency Texture Repair in ID-Specific Talking Heads](https://arxiv.org/abs/2410.00990)
**Jian Yang, Xukun Wang, Wentao Wang, Guoming Li et al.** · 2024-10-01

<details>
<summary>Abstract</summary>

Audio-driven IDentity-specific Talking Head Generation (ID-specific THG) has shown increasing promise for applications in filmmaking and virtual reality. Existing approaches are generally constructed as end-to-end paradigms, and have achieved significant progress. However, they often struggle to capture high-frequency textures due to limited model capacity. To address these limitations, we adopt a simple yet efficient post-processing framework -- unlike previous studies that focus solely on end-to-end training -- guided by our theoretical insights. Specifically, leveraging the \textit{Lipschitz Continuity Theory} of neural networks, we prove a crucial noise tolerance property for the Vector Quantized AutoEncoder (VQ-AE), and establish the existence of a Noise Robustness Upper Bound (NRoUB). This insight reveals that we can efficiently obtain an identity-specific denoiser by training an identity-specific neural discrete representation, without requiring an extra network. Based on this theoretical foundation, we propose a plug-and-play Space-Optimized VQ-AE (SOVQAE) with enhanced NRoUB to achieve temporally-consistent denoising. For practical deployment, we further introduce a cascade pipeline combining a pretrained Wav2Lip model with SOVQAE to perform ID-specific THG. Our experiments demonstrate that this pipeline achieves \textit{state-of-the-art} performance in video quality and robustness for out-of-distribution lip synchronization, surpassing existing identity-specific THG methods. In addition, the pipeline requires only a couple of consumer GPU hours and runs in real time, which is both efficient and practical for industry applications.

</details>

#### [Diverse Code Query Learning for Speech-Driven Facial Animation](https://arxiv.org/abs/2409.19143)
**Chunzhi Gu, Shigeru Kuriyama, Katsuya Hotta** · 2024-09-27

<details>
<summary>Abstract</summary>

Speech-driven facial animation aims to synthesize lip-synchronized 3D talking faces following the given speech signal. Prior methods to this task mostly focus on pursuing realism with deterministic systems, yet characterizing the potentially stochastic nature of facial motions has been to date rarely studied. While generative modeling approaches can easily handle the one-to-many mapping by repeatedly drawing samples, ensuring a diverse mode coverage of plausible facial motions on small-scale datasets remains challenging and less explored. In this paper, we propose predicting multiple samples conditioned on the same audio signal and then explicitly encouraging sample diversity to address diverse facial animation synthesis. Our core insight is to guide our model to explore the expressive facial latent space with a diversity-promoting loss such that the desired latent codes for diversification can be ideally identified. To this end, building upon the rich facial prior learned with vector-quantized variational auto-encoding mechanism, our model temporally queries multiple stochastic codes which can be flexibly decoded into a diverse yet plausible set of speech-faithful facial motions. To further allow for control over different facial parts during generation, the proposed model is designed to predict different facial portions of interest in a sequential manner, and compose them to eventually form full-face motions. Our paradigm realizes both diverse and controllable facial animation synthesis in a unified formulation. We experimentally demonstrate that our method yields state-of-the-art performance both quantitatively and qualitatively, especially regarding sample diversity.

</details>

#### [Stable Video Portraits](https://arxiv.org/abs/2409.18083)
**Mirela Ostrek, Justus Thies** · 2024-09-26

<details>
<summary>Abstract</summary>

Rapid advances in the field of generative AI and text-to-image methods in particular have transformed the way we interact with and perceive computer-generated imagery today. In parallel, much progress has been made in 3D face reconstruction, using 3D Morphable Models (3DMM). In this paper, we present SVP, a novel hybrid 2D/3D generation method that outputs photorealistic videos of talking faces leveraging a large pre-trained text-to-image prior (2D), controlled via a 3DMM (3D). Specifically, we introduce a person-specific fine-tuning of a general 2D stable diffusion model which we lift to a video model by providing temporal 3DMM sequences as conditioning and by introducing a temporal denoising procedure. As an output, this model generates temporally smooth imagery of a person with 3DMM-based controls, i.e., a person-specific avatar. The facial appearance of this person-specific avatar can be edited and morphed to text-defined celebrities, without any fine-tuning at test time. The method is analyzed quantitatively and qualitatively, and we show that our method outperforms state-of-the-art monocular head avatar methods.

</details>

#### [DH-FaceVid-1K: A Large-Scale High-Quality Dataset for Face Video Generation](https://arxiv.org/abs/2410.07151)
**Donglin Di, He Feng, Wenzhang Sun, Yongjia Ma et al.** · 2024-09-23

<details>
<summary>Abstract</summary>

Human-centric generative models are becoming increasingly popular, giving rise to various innovative tools and applications, such as talking face videos conditioned on text or audio prompts. The core of these capabilities lies in powerful pre-trained foundation models, trained on large-scale, high-quality datasets. However, many advanced methods rely on in-house data subject to various constraints, and other current studies fail to generate high-resolution face videos, which is mainly attributed to the significant lack of large-scale, high-quality face video datasets. In this paper, we introduce a human face video dataset, \textbf{DH-FaceVid-1K}. Our collection spans 1,200 hours in total, encompassing 270,043 video clips from over 20,000 individuals. Each sample includes corresponding speech audio, facial keypoints, and text annotations. Compared to other publicly available datasets, ours distinguishes itself through its multi-ethnic coverage and high-quality, comprehensive individual attributes. We establish multiple face video generation models supporting tasks such as text-to-video and image-to-video generation. In addition, we develop comprehensive benchmarks to validate the scaling law when using different proportions of proposed dataset. Our primary aim is to contribute a face video dataset, particularly addressing the underrepresentation of Asian faces in existing curated datasets and thereby enriching the global spectrum of face-centric data and mitigating demographic biases. \textbf{Project Page:} https://luna-ai-lab.github.io/DH-FaceVid-1K/

</details>

#### [JEAN: Joint Expression and Audio-guided NeRF-based Talking Face Generation](https://arxiv.org/abs/2409.12156)
**Sai Tanmay Reddy Chakkera, Aggelina Chatziagapi, Dimitris Samaras** · 2024-09-18

<details>
<summary>Abstract</summary>

We introduce a novel method for joint expression and audio-guided talking face generation. Recent approaches either struggle to preserve the speaker identity or fail to produce faithful facial expressions. To address these challenges, we propose a NeRF-based network. Since we train our network on monocular videos without any ground truth, it is essential to learn disentangled representations for audio and expression. We first learn audio features in a self-supervised manner, given utterances from multiple subjects. By incorporating a contrastive learning technique, we ensure that the learned audio features are aligned to the lip motion and disentangled from the muscle motion of the rest of the face. We then devise a transformer-based architecture that learns expression features, capturing long-range facial expressions and disentangling them from the speech-specific mouth movements. Through quantitative and qualitative evaluation, we demonstrate that our method can synthesize high-fidelity talking face videos, achieving state-of-the-art facial expression transfer along with lip synchronization to unseen audio.

</details>

#### [DreamHead: Learning Spatial-Temporal Correspondence via Hierarchical Diffusion for Audio-driven Talking Head Synthesis](https://arxiv.org/abs/2409.10281)
**Fa-Ting Hong, Yunfei Liu, Yu Li, Changyin Zhou et al.** · 2024-09-16

<details>
<summary>Abstract</summary>

Audio-driven talking head synthesis strives to generate lifelike video portraits from provided audio. The diffusion model, recognized for its superior quality and robust generalization, has been explored for this task. However, establishing a robust correspondence between temporal audio cues and corresponding spatial facial expressions with diffusion models remains a significant challenge in talking head generation. To bridge this gap, we present DreamHead, a hierarchical diffusion framework that learns spatial-temporal correspondences in talking head synthesis without compromising the model's intrinsic quality and adaptability.~DreamHead learns to predict dense facial landmarks from audios as intermediate signals to model the spatial and temporal correspondences.~Specifically, a first hierarchy of audio-to-landmark diffusion is first designed to predict temporally smooth and accurate landmark sequences given audio sequence signals. Then, a second hierarchy of landmark-to-image diffusion is further proposed to produce spatially consistent facial portrait videos, by modeling spatial correspondences between the dense facial landmark and appearance. Extensive experiments show that proposed DreamHead can effectively learn spatial-temporal consistency with the designed hierarchical diffusion and produce high-fidelity audio-driven talking head videos for multiple identities.

</details>

#### [ProbTalk3D: Non-Deterministic Emotion Controllable Speech-Driven 3D Facial Animation Synthesis Using VQ-VAE](https://arxiv.org/abs/2409.07966)
**Sichun Wu, Kazi Injamamul Haque, Zerrin Yumak** · 2024-09-12

<details>
<summary>Abstract</summary>

Audio-driven 3D facial animation synthesis has been an active field of research with attention from both academia and industry. While there are promising results in this area, recent approaches largely focus on lip-sync and identity control, neglecting the role of emotions and emotion control in the generative process. That is mainly due to the lack of emotionally rich facial animation data and algorithms that can synthesize speech animations with emotional expressions at the same time. In addition, majority of the models are deterministic, meaning given the same audio input, they produce the same output motion. We argue that emotions and non-determinism are crucial to generate diverse and emotionally-rich facial animations. In this paper, we propose ProbTalk3D a non-deterministic neural network approach for emotion controllable speech-driven 3D facial animation synthesis using a two-stage VQ-VAE model and an emotionally rich facial animation dataset 3DMEAD. We provide an extensive comparative analysis of our model against the recent 3D facial animation synthesis approaches, by evaluating the results objectively, qualitatively, and with a perceptual user study. We highlight several objective metrics that are more suitable for evaluating stochastic outputs and use both in-the-wild and ground truth data for subjective evaluation. To our knowledge, that is the first non-deterministic 3D facial animation synthesis method incorporating a rich emotion dataset and emotion control with emotion labels and intensity levels. Our evaluation demonstrates that the proposed model achieves superior performance compared to state-of-the-art emotion-controlled, deterministic and non-deterministic models. We recommend watching the supplementary video for quality judgement. The entire codebase is publicly available (https://github.com/uuembodiedsocialai/ProbTalk3D/).

</details>

#### [EMOdiffhead: Continuously Emotional Control in Talking Head Generation via Diffusion](https://arxiv.org/abs/2409.07255)
**Jian Zhang, Weijian Mai, Zhijun Zhang** · 2024-09-11

<details>
<summary>Abstract</summary>

The task of audio-driven portrait animation involves generating a talking head video using an identity image and an audio track of speech. While many existing approaches focus on lip synchronization and video quality, few tackle the challenge of generating emotion-driven talking head videos. The ability to control and edit emotions is essential for producing expressive and realistic animations. In response to this challenge, we propose EMOdiffhead, a novel method for emotional talking head video generation that not only enables fine-grained control of emotion categories and intensities but also enables one-shot generation. Given the FLAME 3D model's linearity in expression modeling, we utilize the DECA method to extract expression vectors, that are combined with audio to guide a diffusion model in generating videos with precise lip synchronization and rich emotional expressiveness. This approach not only enables the learning of rich facial information from emotion-irrelevant data but also facilitates the generation of emotional videos. It effectively overcomes the limitations of emotional data, such as the lack of diversity in facial and background information, and addresses the absence of emotional details in emotion-irrelevant data. Extensive experiments and user studies demonstrate that our approach achieves state-of-the-art performance compared to other emotion portrait animation methods.

</details>

#### [DiffTED: One-shot Audio-driven TED Talk Video Generation with Diffusion-based Co-speech Gestures](https://arxiv.org/abs/2409.07649)
**Steven Hogue, Chenxu Zhang, Hamza Daruger, Yapeng Tian et al.** · 2024-09-11

<details>
<summary>Abstract</summary>

Audio-driven talking video generation has advanced significantly, but existing methods often depend on video-to-video translation techniques and traditional generative networks like GANs and they typically generate taking heads and co-speech gestures separately, leading to less coherent outputs. Furthermore, the gestures produced by these methods often appear overly smooth or subdued, lacking in diversity, and many gesture-centric approaches do not integrate talking head generation. To address these limitations, we introduce DiffTED, a new approach for one-shot audio-driven TED-style talking video generation from a single image. Specifically, we leverage a diffusion model to generate sequences of keypoints for a Thin-Plate Spline motion model, precisely controlling the avatar's animation while ensuring temporally coherent and diverse gestures. This innovative approach utilizes classifier-free guidance, empowering the gestures to flow naturally with the audio input without relying on pre-trained classifiers. Experiments demonstrate that DiffTED generates temporally coherent talking videos with diverse co-speech gestures.

</details>

#### [SegTalker: Segmentation-based Talking Face Generation with Mask-guided Local Editing](https://arxiv.org/abs/2409.03605)
**Lingyu Xiong, Xize Cheng, Jintao Tan, Xianjia Wu et al.** · 2024-09-05

<details>
<summary>Abstract</summary>

Audio-driven talking face generation aims to synthesize video with lip movements synchronized to input audio. However, current generative techniques face challenges in preserving intricate regional textures (skin, teeth). To address the aforementioned challenges, we propose a novel framework called SegTalker to decouple lip movements and image textures by introducing segmentation as intermediate representation. Specifically, given the mask of image employed by a parsing network, we first leverage the speech to drive the mask and generate talking segmentation. Then we disentangle semantic regions of image into style codes using a mask-guided encoder. Ultimately, we inject the previously generated talking segmentation and style codes into a mask-guided StyleGAN to synthesize video frame. In this way, most of textures are fully preserved. Moreover, our approach can inherently achieve background separation and facilitate mask-guided facial local editing. In particular, by editing the mask and swapping the region textures from a given reference image (e.g. hair, lip, eyebrows), our approach enables facial editing seamlessly when generating talking face video. Experiments demonstrate that our proposed approach can effectively preserve texture details and generate temporally consistent video while remaining competitive in lip synchronization. Quantitative and qualitative results on the HDTF and MEAD datasets illustrate the superior performance of our method over existing methods.

</details>

#### [SVP: Style-Enhanced Vivid Portrait Talking Head Diffusion Model](https://arxiv.org/abs/2409.03270)
**Weipeng Tan, Chuming Lin, Chengming Xu, Xiaozhong Ji et al.** · 2024-09-05

<details>
<summary>Abstract</summary>

Talking Head Generation (THG), typically driven by audio, is an important and challenging task with broad application prospects in various fields such as digital humans, film production, and virtual reality. While diffusion model-based THG methods present high quality and stable content generation, they often overlook the intrinsic style which encompasses personalized features such as speaking habits and facial expressions of a video. As consequence, the generated video content lacks diversity and vividness, thus being limited in real life scenarios. To address these issues, we propose a novel framework named Style-Enhanced Vivid Portrait (SVP) which fully leverages style-related information in THG. Specifically, we first introduce the novel probabilistic style prior learning to model the intrinsic style as a Gaussian distribution using facial expressions and audio embedding. The distribution is learned through the 'bespoked' contrastive objective, effectively capturing the dynamic style information in each video. Then we finetune a pretrained Stable Diffusion (SD) model to inject the learned intrinsic style as a controlling signal via cross attention. Experiments show that our model generates diverse, vivid, and high-quality videos with flexible control over intrinsic styles, outperforming existing state-of-the-art methods.

</details>

#### [PoseTalk: Text-and-Audio-based Pose Control and Motion Refinement for One-Shot Talking Head Generation](https://arxiv.org/abs/2409.02657)
**Jun Ling, Yiwen Wang, Han Xue, Rong Xie et al.** · 2024-09-04

<details>
<summary>Abstract</summary>

While previous audio-driven talking head generation (THG) methods generate head poses from driving audio, the generated poses or lips cannot match the audio well or are not editable. In this study, we propose \textbf{PoseTalk}, a THG system that can freely generate lip-synchronized talking head videos with free head poses conditioned on text prompts and audio. The core insight of our method is using head pose to connect visual, linguistic, and audio signals. First, we propose to generate poses from both audio and text prompts, where the audio offers short-term variations and rhythm correspondence of the head movements and the text prompts describe the long-term semantics of head motions. To achieve this goal, we devise a Pose Latent Diffusion (PLD) model to generate motion latent from text prompts and audio cues in a pose latent space. Second, we observe a loss-imbalance problem: the loss for the lip region contributes less than 4\% of the total reconstruction loss caused by both pose and lip, making optimization lean towards head movements rather than lip shapes. To address this issue, we propose a refinement-based learning strategy to synthesize natural talking videos using two cascaded networks, i.e., CoarseNet, and RefineNet. The CoarseNet estimates coarse motions to produce animated images in novel poses and the RefineNet focuses on learning finer lip motions by progressively estimating lip motions from low-to-high resolutions, yielding improved lip-synchronization performance. Experiments demonstrate our pose prediction strategy achieves better pose diversity and realness compared to text-only or audio-only, and our video generator model outperforms state-of-the-art methods in synthesizing talking videos with natural head motions. Project: https://junleen.github.io/projects/posetalk.

</details>

#### [G3FA: Geometry-guided GAN for Face Animation](https://arxiv.org/abs/2408.13049)
**Alireza Javanmardi, Alain Pagani, Didier Stricker** · 2024-08-23

<details>
<summary>Abstract</summary>

Animating human face images aims to synthesize a desired source identity in a natural-looking way mimicking a driving video's facial movements. In this context, Generative Adversarial Networks have demonstrated remarkable potential in real-time face reenactment using a single source image, yet are constrained by limited geometry consistency compared to graphic-based approaches. In this paper, we introduce Geometry-guided GAN for Face Animation (G3FA) to tackle this limitation. Our novel approach empowers the face animation model to incorporate 3D information using only 2D images, improving the image generation capabilities of the talking head synthesis model. We integrate inverse rendering techniques to extract 3D facial geometry properties, improving the feedback loop to the generator through a weighted average ensemble of discriminators. In our face reenactment model, we leverage 2D motion warping to capture motion dynamics along with orthogonal ray sampling and volume rendering techniques to produce the ultimate visual output. To evaluate the performance of our G3FA, we conducted comprehensive experiments using various evaluation protocols on VoxCeleb2 and TalkingHead benchmarks to demonstrate the effectiveness of our proposed framework compared to the state-of-the-art real-time face animation methods.

</details>

#### [DEGAS: Detailed Expressions on Full-Body Gaussian Avatars](https://arxiv.org/abs/2408.10588)
**Zhijing Shao, Duotun Wang, Qing-Yao Tian, Yao-Dong Yang et al.** · 2024-08-20

<details>
<summary>Abstract</summary>

Although neural rendering has made significant advances in creating lifelike, animatable full-body and head avatars, incorporating detailed expressions into full-body avatars remains largely unexplored. We present DEGAS, the first 3D Gaussian Splatting (3DGS)-based modeling method for full-body avatars with rich facial expressions. Trained on multiview videos of a given subject, our method learns a conditional variational autoencoder that takes both the body motion and facial expression as driving signals to generate Gaussian maps in the UV layout. To drive the facial expressions, instead of the commonly used 3D Morphable Models (3DMMs) in 3D head avatars, we propose to adopt the expression latent space trained solely on 2D portrait images, bridging the gap between 2D talking faces and 3D avatars. Leveraging the rendering capability of 3DGS and the rich expressiveness of the expression latent space, the learned avatars can be reenacted to reproduce photorealistic rendering images with subtle and accurate facial expressions. Experiments on an existing dataset and our newly proposed dataset of full-body talking avatars demonstrate the efficacy of our method. We also propose an audio-driven extension of our method with the help of 2D talking faces, opening new possibilities for interactive AI agents.

</details>

#### [S^3D-NeRF: Single-Shot Speech-Driven Neural Radiance Field for High Fidelity Talking Head Synthesis](https://arxiv.org/abs/2408.09347)
**Dongze Li, Kang Zhao, Wei Wang, Yifeng Ma et al.** · 2024-08-18

<details>
<summary>Abstract</summary>

Talking head synthesis is a practical technique with wide applications. Current Neural Radiance Field (NeRF) based approaches have shown their superiority on driving one-shot talking heads with videos or signals regressed from audio. However, most of them failed to take the audio as driven information directly, unable to enjoy the flexibility and availability of speech. Since mapping audio signals to face deformation is non-trivial, we design a Single-Shot Speech-Driven Neural Radiance Field (S^3D-NeRF) method in this paper to tackle the following three difficulties: learning a representative appearance feature for each identity, modeling motion of different face regions with audio, and keeping the temporal consistency of the lip area. To this end, we introduce a Hierarchical Facial Appearance Encoder to learn multi-scale representations for catching the appearance of different speakers, and elaborate a Cross-modal Facial Deformation Field to perform speech animation according to the relationship between the audio signal and different face regions. Moreover, to enhance the temporal consistency of the important lip area, we introduce a lip-sync discriminator to penalize the out-of-sync audio-visual sequences. Extensive experiments have shown that our S^3D-NeRF surpasses previous arts on both video fidelity and audio-lip synchronization.

</details>

#### [FD2Talk: Towards Generalized Talking Head Generation with Facial Decoupled Diffusion Model](https://arxiv.org/abs/2408.09384)
**Ziyu Yao, Xuxin Cheng, Zhiqi Huang** · 2024-08-18

<details>
<summary>Abstract</summary>

Talking head generation is a significant research topic that still faces numerous challenges. Previous works often adopt generative adversarial networks or regression models, which are plagued by generation quality and average facial shape problem. Although diffusion models show impressive generative ability, their exploration in talking head generation remains unsatisfactory. This is because they either solely use the diffusion model to obtain an intermediate representation and then employ another pre-trained renderer, or they overlook the feature decoupling of complex facial details, such as expressions, head poses and appearance textures. Therefore, we propose a Facial Decoupled Diffusion model for Talking head generation called FD2Talk, which fully leverages the advantages of diffusion models and decouples the complex facial details through multi-stages. Specifically, we separate facial details into motion and appearance. In the initial phase, we design the Diffusion Transformer to accurately predict motion coefficients from raw audio. These motions are highly decoupled from appearance, making them easier for the network to learn compared to high-dimensional RGB images. Subsequently, in the second phase, we encode the reference image to capture appearance textures. The predicted facial and head motions and encoded appearance then serve as the conditions for the Diffusion UNet, guiding the frame generation. Benefiting from decoupling facial details and fully leveraging diffusion models, extensive experiments substantiate that our approach excels in enhancing image quality and generating more accurate and diverse results compared to previous state-of-the-art methods.

</details>

#### [Meta-Learning Empowered Meta-Face: Personalized Speaking Style Adaptation for Audio-Driven 3D Talking Face Animation](https://arxiv.org/abs/2408.09357)
**Xukun Zhou, Fengxin Li, Ziqiao Peng, Kejian Wu et al.** · 2024-08-18

<details>
<summary>Abstract</summary>

Audio-driven 3D face animation is increasingly vital in live streaming and augmented reality applications. While remarkable progress has been observed, most existing approaches are designed for specific individuals with predefined speaking styles, thus neglecting the adaptability to varied speaking styles. To address this limitation, this paper introduces MetaFace, a novel methodology meticulously crafted for speaking style adaptation. Grounded in the novel concept of meta-learning, MetaFace is composed of several key components: the Robust Meta Initialization Stage (RMIS) for fundamental speaking style adaptation, the Dynamic Relation Mining Neural Process (DRMN) for forging connections between observed and unobserved speaking styles, and the Low-rank Matrix Memory Reduction Approach to enhance the efficiency of model optimization as well as learning style details. Leveraging these novel designs, MetaFace not only significantly outperforms robust existing baselines but also establishes a new state-of-the-art, as substantiated by our experimental results.

</details>

#### [High-fidelity and Lip-synced Talking Face Synthesis via Landmark-based Diffusion Model](https://arxiv.org/abs/2408.05416)
**Weizhi Zhong, Junfan Lin, Peixin Chen, Liang Lin et al.** · 2024-08-10

<details>
<summary>Abstract</summary>

Audio-driven talking face video generation has attracted increasing attention due to its huge industrial potential. Some previous methods focus on learning a direct mapping from audio to visual content. Despite progress, they often struggle with the ambiguity of the mapping process, leading to flawed results. An alternative strategy involves facial structural representations (e.g., facial landmarks) as intermediaries. This multi-stage approach better preserves the appearance details but suffers from error accumulation due to the independent optimization of different stages. Moreover, most previous methods rely on generative adversarial networks, prone to training instability and mode collapse. To address these challenges, our study proposes a novel landmark-based diffusion model for talking face generation, which leverages facial landmarks as intermediate representations while enabling end-to-end optimization. Specifically, we first establish the less ambiguous mapping from audio to landmark motion of lip and jaw. Then, we introduce an innovative conditioning module called TalkFormer to align the synthesized motion with the motion represented by landmarks via differentiable cross-attention, which enables end-to-end optimization for improved lip synchronization. Besides, TalkFormer employs implicit feature warping to align the reference image features with the target motion for preserving more appearance details. Extensive experiments demonstrate that our approach can synthesize high-fidelity and lip-synced talking face videos, preserving more subject appearance details from the reference image.

</details>

#### [Style-Preserving Lip Sync via Audio-Aware Style Reference](https://arxiv.org/abs/2408.05412)
**Weizhi Zhong, Jichang Li, Yinqi Cai, Ming Li et al.** · 2024-08-10

<details>
<summary>Abstract</summary>

Audio-driven lip sync has recently drawn significant attention due to its widespread application in the multimedia domain. Individuals exhibit distinct lip shapes when speaking the same utterance, attributed to the unique speaking styles of individuals, posing a notable challenge for audio-driven lip sync. Earlier methods for such task often bypassed the modeling of personalized speaking styles, resulting in sub-optimal lip sync conforming to the general styles. Recent lip sync techniques attempt to guide the lip sync for arbitrary audio by aggregating information from a style reference video, yet they can not preserve the speaking styles well due to their inaccuracy in style aggregation. This work proposes an innovative audio-aware style reference scheme that effectively leverages the relationships between input audio and reference audio from style reference video to address the style-preserving audio-driven lip sync. Specifically, we first develop an advanced Transformer-based model adept at predicting lip motion corresponding to the input audio, augmented by the style information aggregated through cross-attention layers from style reference video. Afterwards, to better render the lip motion into realistic talking face video, we devise a conditional latent diffusion model, integrating lip motion through modulated convolutional layers and fusing reference facial images via spatial cross-attention layers. Extensive experiments validate the efficacy of the proposed approach in achieving precise lip sync, preserving speaking styles, and generating high-fidelity, realistic talking face videos.

</details>

#### [The DeepSpeak Dataset](https://arxiv.org/abs/2408.05366)
**Sarah Barrington, Maty Bohacek, Hany Farid** · 2024-08-09

<details>
<summary>Abstract</summary>

Deepfakes represent a growing concern across domains such as disinformation, fraud, and non-consensual media. In particular, the rise of video conference and identity-driven attacks in high-stakes scenarios--such as impostor hiring--demands new forensic resources. Despite significant efforts to develop robust detection classifiers to distinguish the real from the fake, commonly used training datasets remain inadequate: relying on low-quality and outdated deepfake generators, consisting of content scraped from online repositories without participant consent, lacking in multimodal coverage, and rarely employing identity-matching protocols to ensure realistic fakes. To overcome these limitations, we present the DeepSpeak dataset, a diverse and multimodal dataset comprising over 100 hours of authentic and deepfake audiovisual content, specifically focused on the challenging and diverse talking heads context. We contribute: i) more than 50 hours of real, self-recorded data collected from 500 diverse and consenting participants, ii) more than 50 hours of state-of-the-art audio and visual deepfakes generated using 14 video synthesis engines and three voice cloning engines, and iii) an embedding-based, identity-matching approach to ensure the creation of convincing, high-quality identity face swaps that realistically simulate adversarial deepfake attacks. We also perform large-scale evaluations of state-of-the-art deepfake detectors and show that, without retraining, these detectors fail to generalize to this DeepSpeak dataset, highlighting the importance of a large and diverse dataset containing deepfakes from the latest generative-AI tools.

</details>

#### [ReSyncer: Rewiring Style-based Generator for Unified Audio-Visually Synced Facial Performer](https://arxiv.org/abs/2408.03284)
**Jiazhi Guan, Zhiliang Xu, Hang Zhou, Kaisiyuan Wang et al.** · 2024-08-06

<details>
<summary>Abstract</summary>

Lip-syncing videos with given audio is the foundation for various applications including the creation of virtual presenters or performers. While recent studies explore high-fidelity lip-sync with different techniques, their task-orientated models either require long-term videos for clip-specific training or retain visible artifacts. In this paper, we propose a unified and effective framework ReSyncer, that synchronizes generalized audio-visual facial information. The key design is revisiting and rewiring the Style-based generator to efficiently adopt 3D facial dynamics predicted by a principled style-injected Transformer. By simply re-configuring the information insertion mechanisms within the noise and style space, our framework fuses motion and appearance with unified training. Extensive experiments demonstrate that ReSyncer not only produces high-fidelity lip-synced videos according to audio, but also supports multiple appealing properties that are suitable for creating virtual presenters and performers, including fast personalized fine-tuning, video-driven lip-syncing, the transfer of speaking styles, and even face swapping. Resources can be found at https://guanjz20.github.io/projects/ReSyncer.

</details>

#### [GLDiTalker: Speech-Driven 3D Facial Animation with Graph Latent Diffusion Transformer](https://arxiv.org/abs/2408.01826)
**Yihong Lin, Zhaoxin Fan, Xianjia Wu, Lingyu Xiong et al.** · 2024-08-03

<details>
<summary>Abstract</summary>

Speech-driven talking head generation is a critical yet challenging task with applications in augmented reality and virtual human modeling. While recent approaches using autoregressive and diffusion-based models have achieved notable progress, they often suffer from modality inconsistencies, particularly misalignment between audio and mesh, leading to reduced motion diversity and lip-sync accuracy. To address this, we propose GLDiTalker, a novel speech-driven 3D facial animation model based on a Graph Latent Diffusion Transformer. GLDiTalker resolves modality misalignment by diffusing signals within a quantized spatiotemporal latent space. It employs a two-stage training pipeline: the Graph-Enhanced Quantized Space Learning Stage ensures lip-sync accuracy, while the Space-Time Powered Latent Diffusion Stage enhances motion diversity. Together, these stages enable GLDiTalker to generate realistic, temporally stable 3D facial animations. Extensive evaluations on standard benchmarks demonstrate that GLDiTalker outperforms existing methods, achieving superior results in both lip-sync accuracy and motion diversity.

</details>

#### [JambaTalk: Speech-Driven 3D Talking Head Generation Based on Hybrid Transformer-Mamba Model](https://arxiv.org/abs/2408.01627)
**Farzaneh Jafari, Stefano Berretti, Anup Basu** · 2024-08-03

<details>
<summary>Abstract</summary>

In recent years, the talking head generation has become a focal point for researchers. Considerable effort is being made to refine lip-sync motion, capture expressive facial expressions, generate natural head poses, and achieve high-quality video. However, no single model has yet achieved equivalence across all quantitative and qualitative metrics. We introduce Jamba, a hybrid Transformer-Mamba model, to animate a 3D face. Mamba, a pioneering Structured State Space Model (SSM) architecture, was developed to overcome the limitations of conventional Transformer architectures, particularly in handling long sequences. This challenge has constrained traditional models. Jamba combines the advantages of both the Transformer and Mamba approaches, offering a comprehensive solution. Based on the foundational Jamba block, we present JambaTalk to enhance motion variety and lip sync through multimodal integration. Extensive experiments reveal that our method achieves performance comparable or superior to state-of-the-art models.

</details>

#### [Landmark-guided Diffusion Model for High-fidelity and Temporally Coherent Talking Head Generation](https://arxiv.org/abs/2408.01732)
**Jintao Tan, Xize Cheng, Lingyu Xiong, Lei Zhu et al.** · 2024-08-03

<details>
<summary>Abstract</summary>

Audio-driven talking head generation is a significant and challenging task applicable to various fields such as virtual avatars, film production, and online conferences. However, the existing GAN-based models emphasize generating well-synchronized lip shapes but overlook the visual quality of generated frames, while diffusion-based models prioritize generating high-quality frames but neglect lip shape matching, resulting in jittery mouth movements. To address the aforementioned problems, we introduce a two-stage diffusion-based model. The first stage involves generating synchronized facial landmarks based on the given speech. In the second stage, these generated landmarks serve as a condition in the denoising process, aiming to optimize mouth jitter issues and generate high-fidelity, well-synchronized, and temporally coherent talking head videos. Extensive experiments demonstrate that our model yields the best performance.

</details>

#### [LinguaLinker: Audio-Driven Portraits Animation with Implicit Facial Control Enhancement](https://arxiv.org/abs/2407.18595)
**Rui Zhang, Yixiao Fang, Zhengnan Lu, Pei Cheng et al.** · 2024-07-26

<details>
<summary>Abstract</summary>

This study delves into the intricacies of synchronizing facial dynamics with multilingual audio inputs, focusing on the creation of visually compelling, time-synchronized animations through diffusion-based techniques. Diverging from traditional parametric models for facial animation, our approach, termed LinguaLinker, adopts a holistic diffusion-based framework that integrates audio-driven visual synthesis to enhance the synergy between auditory stimuli and visual responses. We process audio features separately and derive the corresponding control gates, which implicitly govern the movements in the mouth, eyes, and head, irrespective of the portrait's origin. The advanced audio-driven visual synthesis mechanism provides nuanced control but keeps the compatibility of output video and input audio, allowing for a more tailored and effective portrayal of distinct personas across different languages. The significant improvements in the fidelity of animated portraits, the accuracy of lip-syncing, and the appropriate motion variations achieved by our method render it a versatile tool for animating any portrait in any language.

</details>

#### [PAV: Personalized Head Avatar from Unstructured Video Collection](https://arxiv.org/abs/2407.21047)
**Akin Caliskan, Berkay Kicanaoglu, Hyeongwoo Kim** · 2024-07-22

<details>
<summary>Abstract</summary>

We propose PAV, Personalized Head Avatar for the synthesis of human faces under arbitrary viewpoints and facial expressions. PAV introduces a method that learns a dynamic deformable neural radiance field (NeRF), in particular from a collection of monocular talking face videos of the same character under various appearance and shape changes. Unlike existing head NeRF methods that are limited to modeling such input videos on a per-appearance basis, our method allows for learning multi-appearance NeRFs, introducing appearance embedding for each input video via learnable latent neural features attached to the underlying geometry. Furthermore, the proposed appearance-conditioned density formulation facilitates the shape variation of the character, such as facial hair and soft tissues, in the radiance field prediction. To the best of our knowledge, our approach is the first dynamic deformable NeRF framework to model appearance and shape variations in a single unified network for multi-appearances of the same subject. We demonstrate experimentally that PAV outperforms the baseline method in terms of visual rendering quality in our quantitative and qualitative studies on various subjects.

</details>

#### [Anchored Diffusion for Video Face Reenactment](https://arxiv.org/abs/2407.15153)
**Idan Kligvasser, Regev Cohen, George Leifman, Ehud Rivlin et al.** · 2024-07-21

<details>
<summary>Abstract</summary>

Video generation has drawn significant interest recently, pushing the development of large-scale models capable of producing realistic videos with coherent motion. Due to memory constraints, these models typically generate short video segments that are then combined into long videos. The merging process poses a significant challenge, as it requires ensuring smooth transitions and overall consistency. In this paper, we introduce Anchored Diffusion, a novel method for synthesizing relatively long and seamless videos. We extend Diffusion Transformers (DiTs) to incorporate temporal information, creating our sequence-DiT (sDiT) model for generating short video segments. Unlike previous works, we train our model on video sequences with random non-uniform temporal spacing and incorporate temporal information via external guidance, increasing flexibility and allowing it to capture both short and long-term relationships. Furthermore, during inference, we leverage the transformer architecture to modify the diffusion process, generating a batch of non-uniform sequences anchored to a common frame, ensuring consistency regardless of temporal distance. To demonstrate our method, we focus on face reenactment, the task of creating a video from a source image that replicates the facial expressions and movements from a driving video. Through comprehensive experiments, we show our approach outperforms current techniques in producing longer consistent high-quality videos while offering editing capabilities.

</details>

#### [Text-based Talking Video Editing with Cascaded Conditional Diffusion](https://arxiv.org/abs/2407.14841)
**Bo Han, Heqing Zou, Haoyang Li, Guangcong Wang et al.** · 2024-07-20

<details>
<summary>Abstract</summary>

Text-based talking-head video editing aims to efficiently insert, delete, and substitute segments of talking videos through a user-friendly text editing approach. It is challenging because of \textbf{1)} generalizable talking-face representation, \textbf{2)} seamless audio-visual transitions, and \textbf{3)} identity-preserved talking faces. Previous works either require minutes of talking-face video training data and expensive test-time optimization for customized talking video editing or directly generate a video sequence without considering in-context information, leading to a poor generalizable representation, or incoherent transitions, or even inconsistent identity. In this paper, we propose an efficient cascaded conditional diffusion-based framework, which consists of two stages: audio to dense-landmark motion and motion to video. \textit{\textbf{In the first stage}}, we first propose a dynamic weighted in-context diffusion module to synthesize dense-landmark motions given an edited audio. \textit{\textbf{In the second stage}}, we introduce a warping-guided conditional diffusion module. The module first interpolates between the start and end frames of the editing interval to generate smooth intermediate frames. Then, with the help of the audio-to-dense motion images, these intermediate frames are warped to obtain coarse intermediate frames. Conditioned on the warped intermedia frames, a diffusion model is adopted to generate detailed and high-resolution target frames, which guarantees coherent and identity-preserved transitions. The cascaded conditional diffusion model decomposes the complex talking editing task into two flexible generation tasks, which provides a generalizable talking-face representation, seamless audio-visual transitions, and identity-preserved faces on a small dataset. Experiments show the effectiveness and superiority of the proposed method.

</details>

#### [RT-LA-VocE: Real-Time Low-SNR Audio-Visual Speech Enhancement](https://arxiv.org/abs/2407.07825)
**Honglie Chen, Rodrigo Mira, Stavros Petridis, Maja Pantic** · 2024-07-10

<details>
<summary>Abstract</summary>

In this paper, we aim to generate clean speech frame by frame from a live video stream and a noisy audio stream without relying on future inputs. To this end, we propose RT-LA-VocE, which completely re-designs every component of LA-VocE, a state-of-the-art non-causal audio-visual speech enhancement model, to perform causal real-time inference with a 40ms input frame. We do so by devising new visual and audio encoders that rely solely on past frames, replacing the Transformer encoder with the Emformer, and designing a new causal neural vocoder C-HiFi-GAN. On the popular AVSpeech dataset, we show that our algorithm achieves state-of-the-art results in all real-time scenarios. More importantly, each component is carefully tuned to minimize the algorithm latency to the theoretical minimum (40ms) while maintaining a low end-to-end processing latency of 28.15ms per frame, enabling real-time frame-by-frame enhancement with minimal delay.

</details>

#### [Audio-driven High-resolution Seamless Talking Head Video Editing via StyleGAN](https://arxiv.org/abs/2407.05577)
**Jiacheng Su, Kunhong Liu, Liyan Chen, Junfeng Yao et al.** · 2024-07-08

<details>
<summary>Abstract</summary>

The existing methods for audio-driven talking head video editing have the limitations of poor visual effects. This paper tries to tackle this problem through editing talking face images seamless with different emotions based on two modules: (1) an audio-to-landmark module, consisting of the CrossReconstructed Emotion Disentanglement and an alignment network module. It bridges the gap between speech and facial motions by predicting corresponding emotional landmarks from speech; (2) a landmark-based editing module edits face videos via StyleGAN. It aims to generate the seamless edited video consisting of the emotion and content components from the input audio. Extensive experiments confirm that compared with state-of-the-arts methods, our method provides high-resolution videos with high visual quality.

</details>

#### [Enhancing Speech-Driven 3D Facial Animation with Audio-Visual Guidance from Lip Reading Expert](https://arxiv.org/abs/2407.01034)
**Han EunGi, Oh Hyun-Bin, Kim Sung-Bin, Corentin Nivelet Etcheberry et al.** · 2024-07-01

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation has recently garnered attention due to its cost-effective usability in multimedia production. However, most current advances overlook the intelligibility of lip movements, limiting the realism of facial expressions. In this paper, we introduce a method for speech-driven 3D facial animation to generate accurate lip movements, proposing an audio-visual multimodal perceptual loss. This loss provides guidance to train the speech-driven 3D facial animators to generate plausible lip motions aligned with the spoken transcripts. Furthermore, to incorporate the proposed audio-visual perceptual loss, we devise an audio-visual lip reading expert leveraging its prior knowledge about correlations between speech and lip motions. We validate the effectiveness of our approach through broad experiments, showing noticeable improvements in lip synchronization and lip readability performance. Codes are available at https://3d-talking-head-avguide.github.io/.

</details>

#### [Editing Audio-Driven Talking Head Based on Audio Information](https://www.semanticscholar.org/paper/6ec08eb464be74f258806ba9ab499abfdb041150)
**Rui Lang** · 2024-06-30

<details>
<summary>Abstract</summary>

Editing audio-driven talking head is a relatively new direction in the field of computer vision and still faces many challenges. First, the existing methods do not fully take into account the information contained in the driving audio, which can easily lead to the problem of mismatch between audio and video features (for example, the driving audio emotion is happy, but the corresponding facial emotion is calm). Second, existing face editing methods are often limited to one mode, and the variety they can produce is limited. Finally, we would like the final generated facial animation to be undistorted and to retain some of the identity of the original image. To address the above problems, this paper proposes a novel talking head editing method based on audio information. Specifically, we obtain comprehensive audio information by introducing multiple audio feature classifiers and use it to guide facial editing. We generate more diverse and detailed facial features by combining two different dimensional face editors. To ensure that the edited face retains as much of its original identity features as possible, we use a 3D head model to drive a single image, rather than introducing latent space or establishing complex cross-modal associations between audio and video frames, which can easily lead to facial distortion. Extensive experiments demonstrate the superiority of our method for audio-driven talking head editing. Please go to the link below to view detailed video results: https://drive.google.com/drive/folders/10T1nIktZciG6Cih_UEUOrg0YKXG6KM-C?usp=sharing

</details>

#### [RealTalk: Real-time and Realistic Audio-driven Face Generation with 3D Facial Prior-guided Identity Alignment Network](https://arxiv.org/abs/2406.18284)
**Xiaozhong Ji, Chuming Lin, Zhonggan Ding, Ying Tai et al.** · 2024-06-26

<details>
<summary>Abstract</summary>

Person-generic audio-driven face generation is a challenging task in computer vision. Previous methods have achieved remarkable progress in audio-visual synchronization, but there is still a significant gap between current results and practical applications. The challenges are two-fold: 1) Preserving unique individual traits for achieving high-precision lip synchronization. 2) Generating high-quality facial renderings in real-time performance. In this paper, we propose a novel generalized audio-driven framework RealTalk, which consists of an audio-to-expression transformer and a high-fidelity expression-to-face renderer. In the first component, we consider both identity and intra-personal variation features related to speaking lip movements. By incorporating cross-modal attention on the enriched facial priors, we can effectively align lip movements with audio, thus attaining greater precision in expression prediction. In the second component, we design a lightweight facial identity alignment (FIA) module which includes a lip-shape control structure and a face texture reference structure. This novel design allows us to generate fine details in real-time, without depending on sophisticated and inefficient feature alignment modules. Our experimental results, both quantitative and qualitative, on public datasets demonstrate the clear advantages of our method in terms of lip-speech synchronization and generation quality. Furthermore, our method is efficient and requires fewer computational resources, making it well-suited to meet the needs of practical applications.

</details>

#### [NLDF: Neural Light Dynamic Fields for Efficient 3D Talking Head Generation](https://arxiv.org/abs/2406.11259)
**Niu Guanchen** · 2024-06-17

<details>
<summary>Abstract</summary>

Talking head generation based on the neural radiation fields model has shown promising visual effects. However, the slow rendering speed of NeRF seriously limits its application, due to the burdensome calculation process over hundreds of sampled points to synthesize one pixel. In this work, a novel Neural Light Dynamic Fields model is proposed aiming to achieve generating high quality 3D talking face with significant speedup. The NLDF represents light fields based on light segments, and a deep network is used to learn the entire light beam's information at once. In learning the knowledge distillation is applied and the NeRF based synthesized result is used to guide the correct coloration of light segments in NLDF. Furthermore, a novel active pool training strategy is proposed to focus on high frequency movements, particularly on the speaker mouth and eyebrows. The propose method effectively represents the facial light dynamics in 3D talking video generation, and it achieves approximately 30 times faster speed compared to state of the art NeRF based method, with comparable generation visual quality.

</details>

#### [A Comprehensive Taxonomy and Analysis of Talking Head Synthesis: Techniques for Portrait Generation, Driving Mechanisms, and Editing](https://arxiv.org/abs/2406.10553)
**Ming Meng, Yufei Zhao, Bo Zhang, Yonggui Zhu et al.** · 2024-06-15

<details>
<summary>Abstract</summary>

Talking head synthesis, an advanced method for generating portrait videos from a still image driven by specific content, has garnered widespread attention in virtual reality, augmented reality and game production. Recently, significant breakthroughs have been made with the introduction of novel models such as the transformer and the diffusion model. Current methods can not only generate new content but also edit the generated material. This survey systematically reviews the technology, categorizing it into three pivotal domains: portrait generation, driven mechanisms, and editing techniques. We summarize milestone studies and critically analyze their innovations and shortcomings within each domain. Additionally, we organize an extensive collection of datasets and provide a thorough performance analysis of current methodologies based on various evaluation metrics, aiming to furnish a clear framework and robust data support for future research. Finally, we explore application scenarios of talking head synthesis, illustrate them with specific cases, and examine potential future directions.

</details>

#### [Hallo: Hierarchical Audio-Driven Visual Synthesis for Portrait Image Animation](https://arxiv.org/abs/2406.08801)
**Mingwang Xu, Hui Li, Qingkun Su, Hanlin Shang et al.** · 2024-06-13

<details>
<summary>Abstract</summary>

The field of portrait image animation, driven by speech audio input, has experienced significant advancements in the generation of realistic and dynamic portraits. This research delves into the complexities of synchronizing facial movements and creating visually appealing, temporally consistent animations within the framework of diffusion-based methodologies. Moving away from traditional paradigms that rely on parametric models for intermediate facial representations, our innovative approach embraces the end-to-end diffusion paradigm and introduces a hierarchical audio-driven visual synthesis module to enhance the precision of alignment between audio inputs and visual outputs, encompassing lip, expression, and pose motion. Our proposed network architecture seamlessly integrates diffusion-based generative models, a UNet-based denoiser, temporal alignment techniques, and a reference network. The proposed hierarchical audio-driven visual synthesis offers adaptive control over expression and pose diversity, enabling more effective personalization tailored to different identities. Through a comprehensive evaluation that incorporates both qualitative and quantitative analyses, our approach demonstrates obvious enhancements in image and video quality, lip synchronization precision, and motion diversity. Further visualization and access to the source code can be found at: https://fudan-generative-vision.github.io/hallo.

</details>

#### [FlowAVSE: Efficient Audio-Visual Speech Enhancement with Conditional Flow Matching](https://arxiv.org/abs/2406.09286)
**Chaeyoung Jung, Suyeon Lee, Ji-Hoon Kim, Joon Son Chung** · 2024-06-13

<details>
<summary>Abstract</summary>

This work proposes an efficient method to enhance the quality of corrupted speech signals by leveraging both acoustic and visual cues. While existing diffusion-based approaches have demonstrated remarkable quality, their applicability is limited by slow inference speeds and computational complexity. To address this issue, we present FlowAVSE which enhances the inference speed and reduces the number of learnable parameters without degrading the output quality. In particular, we employ a conditional flow matching algorithm that enables the generation of high-quality speech in a single sampling step. Moreover, we increase efficiency by optimizing the underlying U-net architecture of diffusion-based systems. Our experiments demonstrate that FlowAVSE achieves 22 times faster inference speed and reduces the model size by half while maintaining the output quality. The demo page is available at: https://cyongong.github.io/FlowAVSE.github.io/

</details>

#### [Make Your Actor Talk: Generalizable and High-Fidelity Lip Sync with Motion and Appearance Disentanglement](https://arxiv.org/abs/2406.08096)
**Runyi Yu, Tianyu He, Ailing Zhang, Yuchi Wang et al.** · 2024-06-12

<details>
<summary>Abstract</summary>

We aim to edit the lip movements in talking video according to the given speech while preserving the personal identity and visual details. The task can be decomposed into two sub-problems: (1) speech-driven lip motion generation and (2) visual appearance synthesis. Current solutions handle the two sub-problems within a single generative model, resulting in a challenging trade-off between lip-sync quality and visual details preservation. Instead, we propose to disentangle the motion and appearance, and then generate them one by one with a speech-to-motion diffusion model and a motion-conditioned appearance generation model. However, there still remain challenges in each stage, such as motion-aware identity preservation in (1) and visual details preservation in (2). Therefore, to preserve personal identity, we adopt landmarks to represent the motion, and further employ a landmark-based identity loss. To capture motion-agnostic visual details, we use separate encoders to encode the lip, non-lip appearance and motion, and then integrate them with a learned fusion module. We train MyTalk on a large-scale and diverse dataset. Experiments show that our method generalizes well to the unknown, even out-of-domain person, in terms of both lip sync and visual detail preservation. We encourage the readers to watch the videos on our project page (https://Ingrid789.github.io/MyTalk/).

</details>

#### [Emotional Conversation: Empowering Talking Faces with Cohesive Expression, Gaze and Pose Generation](https://arxiv.org/abs/2406.07895)
**Jiadong Liang, Feng Lu** · 2024-06-12

<details>
<summary>Abstract</summary>

Vivid talking face generation holds immense potential applications across diverse multimedia domains, such as film and game production. While existing methods accurately synchronize lip movements with input audio, they typically ignore crucial alignments between emotion and facial cues, which include expression, gaze, and head pose. These alignments are indispensable for synthesizing realistic videos. To address these issues, we propose a two-stage audio-driven talking face generation framework that employs 3D facial landmarks as intermediate variables. This framework achieves collaborative alignment of expression, gaze, and pose with emotions through self-supervised learning. Specifically, we decompose this task into two key steps, namely speech-to-landmarks synthesis and landmarks-to-face generation. The first step focuses on simultaneously synthesizing emotionally aligned facial cues, including normalized landmarks that represent expressions, gaze, and head pose. These cues are subsequently reassembled into relocated facial landmarks. In the second step, these relocated landmarks are mapped to latent key points using self-supervised learning and then input into a pretrained model to create high-quality face images. Extensive experiments on the MEAD dataset demonstrate that our model significantly advances the state-of-the-art performance in both visual quality and emotional alignment.

</details>

#### [Let's Go Real Talk: Spoken Dialogue Model for Face-to-Face Conversation](https://arxiv.org/abs/2406.07867)
**Se Jin Park, Chae Won Kim, Hyeongseop Rha, Minsu Kim et al.** · 2024-06-12

<details>
<summary>Abstract</summary>

In this paper, we introduce a novel Face-to-Face spoken dialogue model. It processes audio-visual speech from user input and generates audio-visual speech as the response, marking the initial step towards creating an avatar chatbot system without relying on intermediate text. To this end, we newly introduce MultiDialog, the first large-scale multimodal (i.e., audio and visual) spoken dialogue corpus containing 340 hours of approximately 9,000 dialogues, recorded based on the open domain dialogue dataset, TopicalChat. The MultiDialog contains parallel audio-visual recordings of conversation partners acting according to the given script with emotion annotations, which we expect to open up research opportunities in multimodal synthesis. Our Face-to-Face spoken dialogue model incorporates a textually pretrained large language model and adapts it into the audio-visual spoken dialogue domain by incorporating speech-text joint pretraining. Through extensive experiments, we validate the effectiveness of our model in facilitating a face-to-face conversation. Demo and data are available at https://multidialog.github.io and https://huggingface.co/datasets/IVLLab/MultiDialog, respectively.

</details>

#### [Audio2Rig: Artist-oriented deep learning tool for facial animation](https://arxiv.org/abs/2405.20412)
**Bastien Arcelin, Nicolas Chaverou** · 2024-05-30

<details>
<summary>Abstract</summary>

Creating realistic or stylized facial and lip sync animation is a tedious task. It requires lot of time and skills to sync the lips with audio and convey the right emotion to the character's face. To allow animators to spend more time on the artistic and creative part of the animation, we present Audio2Rig: a new deep learning based tool leveraging previously animated sequences of a show, to generate facial and lip sync rig animation from an audio file. Based in Maya, it learns from any production rig without any adjustment and generates high quality and stylized animations which mimic the style of the show. Audio2Rig fits in the animator workflow: since it generates keys on the rig controllers, the animation can be easily retaken. The method is based on 3 neural network modules which can learn an arbitrary number of controllers. Hence, different configurations can be created for specific parts of the face (such as the tongue, lips or eyes). With Audio2Rig, animators can also pick different emotions and adjust their intensities to experiment or customize the output, and have high level controls on the keyframes setting. Our method shows excellent results, generating fine animation details while respecting the show style. Finally, as the training relies on the studio data and is done internally, it ensures data privacy and prevents from copyright infringement.

</details>

#### [EAT-Face: Emotion-Controllable Audio-Driven Talking Face Generation via Diffusion Model](https://www.semanticscholar.org/paper/7b142d08b1319ab1d759083ff65b153400c907cb)
**Haodi Wang, Xiaojun Jia, Xiaochun Cao** · 2024-05-27

<details>
<summary>Abstract</summary>

Audio-driven talking face generation is a promising task with a lot of attention. Despite abundant efforts are devoted to video quality and lip synchronization, most existing works do not take the unignorable aspect of facial emotional expression into account during generation. In this paper, we propose an Emotion-controllable Audio-driven Talking Face generation framework called EAT-Face that enables us to control multiple types of emotions. Specifically, the proposed method consists of a Talking Face Reconstructor (TFR) and a Facial Emotion Controller (FEC), utilizing fused multimodal information including audio signals, visual images, and textual emotions for synthesis. Firstly, TFR predicts face images synchronized with given audios from random noises, leveraging external guidances comprised of audio features, character references, and face masks as conditions. Then, FEC further manipulates the facial emotions based on TFR, leveraging the emotion embeddings extracted from emotion texts. However, a semantic misalignment problem lies in the emotion-texts and character images. To tackle this issue, we additionally propose a strategy called joint Emotion-Visual Embedding (EVE) to mitigate the misalignment. In this way, the proposed EAT-Face is captive to control emotion more precisely. Extensive experiments involving both objective evaluations and subjective investigations demonstrate the effectiveness of our framework in synthesizing high-fidelity and emotional talking face videos.

</details>

#### [InstructAvatar: Text-Guided Emotion and Motion Control for Avatar Generation](https://arxiv.org/abs/2405.15758)
**Yuchi Wang, Junliang Guo, Jianhong Bai, Runyi Yu et al.** · 2024-05-24

<details>
<summary>Abstract</summary>

Recent talking avatar generation models have made strides in achieving realistic and accurate lip synchronization with the audio, but often fall short in controlling and conveying detailed expressions and emotions of the avatar, making the generated video less vivid and controllable. In this paper, we propose a novel text-guided approach for generating emotionally expressive 2D avatars, offering fine-grained control, improved interactivity, and generalizability to the resulting video. Our framework, named InstructAvatar, leverages a natural language interface to control the emotion as well as the facial motion of avatars. Technically, we design an automatic annotation pipeline to construct an instruction-video paired training dataset, equipped with a novel two-branch diffusion-based generator to predict avatars with audio and text instructions at the same time. Experimental results demonstrate that InstructAvatar produces results that align well with both conditions, and outperforms existing methods in fine-grained emotion control, lip-sync quality, and naturalness. Our project page is https://wangyuchi369.github.io/InstructAvatar/.

</details>

#### [OpFlowTalker: Realistic and Natural Talking Face Generation via Optical Flow Guidance](https://arxiv.org/abs/2405.14709)
**Shuheng Ge, Haoyu Xing, Li Zhang, Xiangqian Wu** · 2024-05-23

<details>
<summary>Abstract</summary>

Creating realistic, natural, and lip-readable talking face videos remains a formidable challenge. Previous research primarily concentrated on generating and aligning single-frame images while overlooking the smoothness of frame-to-frame transitions and temporal dependencies. This often compromised visual quality and effects in practical settings, particularly when handling complex facial data and audio content, which frequently led to semantically incongruent visual illusions. Specifically, synthesized videos commonly featured disorganized lip movements, making them difficult to understand and recognize. To overcome these limitations, this paper introduces the application of optical flow to guide facial image generation, enhancing inter-frame continuity and semantic consistency. We propose "OpFlowTalker", a novel approach that utilizes predicted optical flow changes from audio inputs rather than direct image predictions. This method smooths image transitions and aligns changes with semantic content. Moreover, it employs a sequence fusion technique to replace the independent generation of single frames, thus preserving contextual information and maintaining temporal coherence. We also developed an optical flow synchronization module that regulates both full-face and lip movements, optimizing visual synthesis by balancing regional dynamics. Furthermore, we introduce a Visual Text Consistency Score (VTCS) that accurately measures lip-readability in synthesized videos. Extensive empirical evidence validates the effectiveness of our approach.

</details>

#### [Face Adapter for Pre-Trained Diffusion Models with Fine-Grained ID and Attribute Control](https://arxiv.org/abs/2405.12970)
**Yue Han, Junwei Zhu, Keke He, Xu Chen et al.** · 2024-05-21

<details>
<summary>Abstract</summary>

Current face reenactment and swapping methods mainly rely on GAN frameworks, but recent focus has shifted to pre-trained diffusion models for their superior generation capabilities. However, training these models is resource-intensive, and the results have not yet achieved satisfactory performance levels. To address this issue, we introduce Face-Adapter, an efficient and effective adapter designed for high-precision and high-fidelity face editing for pre-trained diffusion models. We observe that both face reenactment/swapping tasks essentially involve combinations of target structure, ID and attribute. We aim to sufficiently decouple the control of these factors to achieve both tasks in one model. Specifically, our method contains: 1) A Spatial Condition Generator that provides precise landmarks and background; 2) A Plug-and-play Identity Encoder that transfers face embeddings to the text space by a transformer decoder. 3) An Attribute Controller that integrates spatial conditions and detailed attributes. Face-Adapter achieves comparable or even superior performance in terms of motion control precision, ID retention capability, and generation quality compared to fully fine-tuned face reenactment/swapping models. Additionally, Face-Adapter seamlessly integrates with various StableDiffusion models.

</details>

#### [Faces that Speak: Jointly Synthesising Talking Face and Speech from Text](https://arxiv.org/abs/2405.10272)
**Youngjoon Jang, Ji-Hoon Kim, Junseok Ahn, Doyeop Kwak et al.** · 2024-05-16

<details>
<summary>Abstract</summary>

The goal of this work is to simultaneously generate natural talking faces and speech outputs from text. We achieve this by integrating Talking Face Generation (TFG) and Text-to-Speech (TTS) systems into a unified framework. We address the main challenges of each task: (1) generating a range of head poses representative of real-world scenarios, and (2) ensuring voice consistency despite variations in facial motion for the same identity. To tackle these issues, we introduce a motion sampler based on conditional flow matching, which is capable of high-quality motion code generation in an efficient way. Moreover, we introduce a novel conditioning method for the TTS system, which utilises motion-removed features from the TFG model to yield uniform speech outputs. Our extensive experiments demonstrate that our method effectively creates natural-looking talking faces and speech that accurately match the input text. To our knowledge, this is the first effort to build a multimodal synthesis system that can generalise to unseen identities.

</details>

#### [NeRFFaceSpeech: One-shot Audio-driven 3D Talking Head Synthesis via Generative Prior](https://arxiv.org/abs/2405.05749)
**Gihoon Kim, Kwanggyoon Seo, Sihun Cha, Junyong Noh** · 2024-05-09

<details>
<summary>Abstract</summary>

Audio-driven talking head generation is advancing from 2D to 3D content. Notably, Neural Radiance Field (NeRF) is in the spotlight as a means to synthesize high-quality 3D talking head outputs. Unfortunately, this NeRF-based approach typically requires a large number of paired audio-visual data for each identity, thereby limiting the scalability of the method. Although there have been attempts to generate audio-driven 3D talking head animations with a single image, the results are often unsatisfactory due to insufficient information on obscured regions in the image. In this paper, we mainly focus on addressing the overlooked aspect of 3D consistency in the one-shot, audio-driven domain, where facial animations are synthesized primarily in front-facing perspectives. We propose a novel method, NeRFFaceSpeech, which enables to produce high-quality 3D-aware talking head. Using prior knowledge of generative models combined with NeRF, our method can craft a 3D-consistent facial feature space corresponding to a single image. Our spatial synchronization method employs audio-correlated vertex dynamics of a parametric face model to transform static image features into dynamic visuals through ray deformation, ensuring realistic 3D facial motion. Moreover, we introduce LipaintNet that can replenish the lacking information in the inner-mouth area, which can not be obtained from a given single image. The network is trained in a self-supervised manner by utilizing the generative capabilities without additional data. The comprehensive experiments demonstrate the superiority of our method in generating audio-driven talking heads from a single image with enhanced 3D consistency compared to previous approaches. In addition, we introduce a quantitative way of measuring the robustness of a model against pose changes for the first time, which has been possible only qualitatively.

</details>

#### [AniTalker: Animate Vivid and Diverse Talking Faces through Identity-Decoupled Facial Motion Encoding](https://arxiv.org/abs/2405.03121)
**Tao Liu, Feilong Chen, Shuai Fan, Chenpeng Du et al.** · 2024-05-06

<details>
<summary>Abstract</summary>

The paper introduces AniTalker, an innovative framework designed to generate lifelike talking faces from a single portrait. Unlike existing models that primarily focus on verbal cues such as lip synchronization and fail to capture the complex dynamics of facial expressions and nonverbal cues, AniTalker employs a universal motion representation. This innovative representation effectively captures a wide range of facial dynamics, including subtle expressions and head movements. AniTalker enhances motion depiction through two self-supervised learning strategies: the first involves reconstructing target video frames from source frames within the same identity to learn subtle motion representations, and the second develops an identity encoder using metric learning while actively minimizing mutual information between the identity and motion encoders. This approach ensures that the motion representation is dynamic and devoid of identity-specific details, significantly reducing the need for labeled data. Additionally, the integration of a diffusion model with a variance adapter allows for the generation of diverse and controllable facial animations. This method not only demonstrates AniTalker's capability to create detailed and realistic facial movements but also underscores its potential in crafting dynamic avatars for real-world applications. Synthetic results can be viewed at https://github.com/X-LANCE/AniTalker.

</details>

#### [Embedded Representation Learning Network for Animating Styled Video Portrait](https://arxiv.org/abs/2404.19038)
**Tianyong Wang, Xiangyu Liang, Wangguandong Zheng, Dan Niu et al.** · 2024-04-29

<details>
<summary>Abstract</summary>

The talking head generation recently attracted considerable attention due to its widespread application prospects, especially for digital avatars and 3D animation design. Inspired by this practical demand, several works explored Neural Radiance Fields (NeRF) to synthesize the talking heads. However, these methods based on NeRF face two challenges: (1) Difficulty in generating style-controllable talking heads. (2) Displacement artifacts around the neck in rendered images. To overcome these two challenges, we propose a novel generative paradigm \textit{Embedded Representation Learning Network} (ERLNet) with two learning stages. First, the \textit{ audio-driven FLAME} (ADF) module is constructed to produce facial expression and head pose sequences synchronized with content audio and style video. Second, given the sequence deduced by the ADF, one novel \textit{dual-branch fusion NeRF} (DBF-NeRF) explores these contents to render the final images. Extensive empirical studies demonstrate that the collaboration of these two stages effectively facilitates our method to render a more realistic talking head than the existing algorithms.

</details>

#### [GaussianTalker: Speaker-specific Talking Head Synthesis via 3D Gaussian Splatting](https://arxiv.org/abs/2404.14037)
**Hongyun Yu, Zhan Qu, Qihang Yu, Jianchuan Chen et al.** · 2024-04-22

<details>
<summary>Abstract</summary>

Recent works on audio-driven talking head synthesis using Neural Radiance Fields (NeRF) have achieved impressive results. However, due to inadequate pose and expression control caused by NeRF implicit representation, these methods still have some limitations, such as unsynchronized or unnatural lip movements, and visual jitter and artifacts. In this paper, we propose GaussianTalker, a novel method for audio-driven talking head synthesis based on 3D Gaussian Splatting. With the explicit representation property of 3D Gaussians, intuitive control of the facial motion is achieved by binding Gaussians to 3D facial models. GaussianTalker consists of two modules, Speaker-specific Motion Translator and Dynamic Gaussian Renderer. Speaker-specific Motion Translator achieves accurate lip movements specific to the target speaker through universalized audio feature extraction and customized lip motion generation. Dynamic Gaussian Renderer introduces Speaker-specific BlendShapes to enhance facial detail representation via a latent pose, delivering stable and realistic rendered videos. Extensive experimental results suggest that GaussianTalker outperforms existing state-of-the-art methods in talking head synthesis, delivering precise lip synchronization and exceptional visual quality. Our method achieves rendering speeds of 130 FPS on NVIDIA RTX4090 GPU, significantly exceeding the threshold for real-time rendering performance, and can potentially be deployed on other hardware platforms.

</details>

#### [FSRT: Facial Scene Representation Transformer for Face Reenactment from Factorized Appearance, Head-pose, and Facial Expression Features](https://arxiv.org/abs/2404.09736)
**Andre Rochow, Max Schwarz, Sven Behnke** · 2024-04-15

<details>
<summary>Abstract</summary>

The task of face reenactment is to transfer the head motion and facial expressions from a driving video to the appearance of a source image, which may be of a different person (cross-reenactment). Most existing methods are CNN-based and estimate optical flow from the source image to the current driving frame, which is then inpainted and refined to produce the output animation. We propose a transformer-based encoder for computing a set-latent representation of the source image(s). We then predict the output color of a query pixel using a transformer-based decoder, which is conditioned with keypoints and a facial expression vector extracted from the driving frame. Latent representations of the source person are learned in a self-supervised manner that factorize their appearance, head pose, and facial expressions. Thus, they are perfectly suited for cross-reenactment. In contrast to most related work, our method naturally extends to multiple source images and can thus adapt to person-specific facial dynamics. We also propose data augmentation and regularization schemes that are necessary to prevent overfitting and support generalizability of the learned representations. We evaluated our approach in a randomized user study. The results indicate superior performance compared to the state-of-the-art in terms of motion transfer quality and temporal consistency.

</details>

#### [Talk3D: High-Fidelity Talking Portrait Synthesis via Personalized 3D Generative Prior](https://arxiv.org/abs/2403.20153)
**Jaehoon Ko, Kyusun Cho, Joungbin Lee, Heeji Yoon et al.** · 2024-03-29

<details>
<summary>Abstract</summary>

Recent methods for audio-driven talking head synthesis often optimize neural radiance fields (NeRF) on a monocular talking portrait video, leveraging its capability to render high-fidelity and 3D-consistent novel-view frames. However, they often struggle to reconstruct complete face geometry due to the absence of comprehensive 3D information in the input monocular videos. In this paper, we introduce a novel audio-driven talking head synthesis framework, called Talk3D, that can faithfully reconstruct its plausible facial geometries by effectively adopting the pre-trained 3D-aware generative prior. Given the personalized 3D generative model, we present a novel audio-guided attention U-Net architecture that predicts the dynamic face variations in the NeRF space driven by audio. Furthermore, our model is further modulated by audio-unrelated conditioning tokens which effectively disentangle variations unrelated to audio features. Compared to existing methods, our method excels in generating realistic facial geometries even under extreme head poses. We also conduct extensive experiments showing our approach surpasses state-of-the-art benchmarks in terms of both quantitative and qualitative evaluations.

</details>

#### [MI-NeRF: Learning a Single Face NeRF from Multiple Identities](https://arxiv.org/abs/2403.19920)
**Aggelina Chatziagapi, Grigorios G. Chrysos, Dimitris Samaras** · 2024-03-29

<details>
<summary>Abstract</summary>

In this work, we introduce a method that learns a single dynamic neural radiance field (NeRF) from monocular talking face videos of multiple identities. NeRFs have shown remarkable results in modeling the 4D dynamics and appearance of human faces. However, they require per-identity optimization. Although recent approaches have proposed techniques to reduce the training and rendering time, increasing the number of identities can be expensive. We introduce MI-NeRF (multi-identity NeRF), a single unified network that models complex non-rigid facial motion for multiple identities, using only monocular videos of arbitrary length. The core premise in our method is to learn the non-linear interactions between identity and non-identity specific information with a multiplicative module. By training on multiple videos simultaneously, MI-NeRF not only reduces the total training time compared to standard single-identity NeRFs, but also demonstrates robustness in synthesizing novel expressions for any input identity. We present results for both facial expression transfer and talking face video synthesis. Our method can be further personalized for a target identity given only a short video.

</details>

#### [MoDiTalker: Motion-Disentangled Diffusion Model for High-Fidelity Talking Head Generation](https://arxiv.org/abs/2403.19144)
**Seyeon Kim, Siyoon Jin, Jihye Park, Kihong Kim et al.** · 2024-03-28

<details>
<summary>Abstract</summary>

Conventional GAN-based models for talking head generation often suffer from limited quality and unstable training. Recent approaches based on diffusion models aimed to address these limitations and improve fidelity. However, they still face challenges, including extensive sampling times and difficulties in maintaining temporal consistency due to the high stochasticity of diffusion models. To overcome these challenges, we propose a novel motion-disentangled diffusion model for high-quality talking head generation, dubbed MoDiTalker. We introduce the two modules: audio-to-motion (AToM), designed to generate a synchronized lip motion from audio, and motion-to-video (MToV), designed to produce high-quality head video following the generated motion. AToM excels in capturing subtle lip movements by leveraging an audio attention mechanism. In addition, MToV enhances temporal consistency by leveraging an efficient tri-plane representation. Our experiments conducted on standard benchmarks demonstrate that our model achieves superior performance compared to existing models. We also provide comprehensive ablation studies and user study results.

</details>

#### [Deepfake Generation and Detection: A Benchmark and Survey](https://arxiv.org/abs/2403.17881)
**Gan Pei, Jiangning Zhang, Menghan Hu, Zhenyu Zhang et al.** · 2024-03-26

<details>
<summary>Abstract</summary>

Deepfake is a technology dedicated to creating highly realistic facial images and videos under specific conditions, which has significant application potential in fields such as entertainment, movie production, digital human creation, to name a few. With the advancements in deep learning, techniques primarily represented by Variational Autoencoders and Generative Adversarial Networks have achieved impressive generation results. More recently, the emergence of diffusion models with powerful generation capabilities has sparked a renewed wave of research. In addition to deepfake generation, corresponding detection technologies continuously evolve to regulate the potential misuse of deepfakes, such as for privacy invasion and phishing attacks. This survey comprehensively reviews the latest developments in deepfake generation and detection, summarizing and analyzing current state-of-the-arts in this rapidly evolving field. We first unify task definitions, comprehensively introduce datasets and metrics, and discuss developing technologies. Then, we discuss the development of several related sub-fields and focus on researching four representative deepfake fields: face swapping, face reenactment, talking face generation, and facial attribute editing, as well as forgery detection. Subsequently, we comprehensively benchmark representative methods on popular datasets for each field, fully evaluating the latest and influential published works. Finally, we analyze challenges and future research directions of the discussed fields.

</details>

#### [AniPortrait: Audio-Driven Synthesis of Photorealistic Portrait Animation](https://arxiv.org/abs/2403.17694)
**Huawei Wei, Zejun Yang, Zhisheng Wang** · 2024-03-26

<details>
<summary>Abstract</summary>

In this study, we propose AniPortrait, a novel framework for generating high-quality animation driven by audio and a reference portrait image. Our methodology is divided into two stages. Initially, we extract 3D intermediate representations from audio and project them into a sequence of 2D facial landmarks. Subsequently, we employ a robust diffusion model, coupled with a motion module, to convert the landmark sequence into photorealistic and temporally consistent portrait animation. Experimental results demonstrate the superiority of AniPortrait in terms of facial naturalness, pose diversity, and visual quality, thereby offering an enhanced perceptual experience. Moreover, our methodology exhibits considerable potential in terms of flexibility and controllability, which can be effectively applied in areas such as facial motion editing or face reenactment. We release code and model weights at https://github.com/scutzzj/AniPortrait

</details>

#### [DiffusionAct: Controllable Diffusion Autoencoder for One-shot Face Reenactment](https://arxiv.org/abs/2403.17217)
**Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras et al.** · 2024-03-25

<details>
<summary>Abstract</summary>

Video-driven neural face reenactment aims to synthesize realistic facial images that successfully preserve the identity and appearance of a source face, while transferring the target head pose and facial expressions. Existing GAN-based methods suffer from either distortions and visual artifacts or poor reconstruction quality, i.e., the background and several important appearance details, such as hair style/color, glasses and accessories, are not faithfully reconstructed. Recent advances in Diffusion Probabilistic Models (DPMs) enable the generation of high-quality realistic images. To this end, in this paper we present DiffusionAct, a novel method that leverages the photo-realistic image generation of diffusion models to perform neural face reenactment. Specifically, we propose to control the semantic space of a Diffusion Autoencoder (DiffAE), in order to edit the facial pose of the input images, defined as the head pose orientation and the facial expressions. Our method allows one-shot, self, and cross-subject reenactment, without requiring subject-specific fine-tuning. We compare against state-of-the-art GAN-, StyleGAN2-, and diffusion-based methods, showing better or on-par reenactment performance.

</details>

#### [FG-EmoTalk: Talking Head Video Generation with Fine-Grained Controllable Facial Expressions](https://www.semanticscholar.org/paper/78396d47cff7a5d2e1330d9f75a2619bb7e1b713)
**Zhaoxu Sun, Yuze Xuan, Fang Liu, Yang Xiang** · 2024-03-24

<details>
<summary>Abstract</summary>

Although deep generative models have greatly improved one-shot video-driven talking head generation, few studies address fine-grained controllable facial expression editing, which is crucial for practical applications. Existing methods rely on a fixed set of predefined discrete emotion labels or simply copy expressions from input videos. This is limiting as expressions are complex, and methods using only emotion labels cannot generate fine-grained, accurate or mixed expressions. Generating talking head video with precise expressions is also difficult using 3D model-based approaches, as 3DMM only models facial movements and tends to produce deviations. In this paper, we propose a novel framework enabling fine-grained facial expression editing in talking face generation. Our goal is to achieve expression control by manipulating the intensities of individual facial Action Units (AUs) or groups. First, compared with existing methods which decouple the face into pose and expression, we propose a disentanglement scheme to isolates three components from the human face, namely, appearance, pose, and expression. Second, we propose to use input AUs to control muscle group intensities in the generated face, and integrate the AUs features with the disentangled expression latent code. Finally, we present a self-supervised training strategy with well-designed constraints. Experiments show our method achieves fine-grained expression control, produces high-quality talking head videos and outperforms baseline methods.

</details>

#### [ScanTalk: 3D Talking Heads from Unregistered Scans](https://arxiv.org/abs/2403.10942)
**Federico Nocentini, Thomas Besnier, Claudio Ferrari, Sylvain Arguillere et al.** · 2024-03-16

<details>
<summary>Abstract</summary>

Speech-driven 3D talking heads generation has emerged as a significant area of interest among researchers, presenting numerous challenges. Existing methods are constrained by animating faces with fixed topologies, wherein point-wise correspondence is established, and the number and order of points remains consistent across all identities the model can animate. In this work, we present \textbf{ScanTalk}, a novel framework capable of animating 3D faces in arbitrary topologies including scanned data. Our approach relies on the DiffusionNet architecture to overcome the fixed topology constraint, offering promising avenues for more flexible and realistic 3D animations. By leveraging the power of DiffusionNet, ScanTalk not only adapts to diverse facial structures but also maintains fidelity when dealing with scanned data, thereby enhancing the authenticity and versatility of generated 3D talking heads. Through comprehensive comparisons with state-of-the-art methods, we validate the efficacy of our approach, demonstrating its capacity to generate realistic talking heads comparable to existing techniques. While our primary objective is to develop a generic method free from topological constraints, all state-of-the-art methodologies are bound by such limitations. Code for reproducing our results, and the pre-trained model are available at https://github.com/miccunifi/ScanTalk .

</details>

#### [Style2Talker: High-Resolution Talking Head Generation with Emotion Style and Art Style](https://arxiv.org/abs/2403.06365)
**Shuai Tan, Bin Ji, Ye Pan** · 2024-03-11

<details>
<summary>Abstract</summary>

Although automatically animating audio-driven talking heads has recently received growing interest, previous efforts have mainly concentrated on achieving lip synchronization with the audio, neglecting two crucial elements for generating expressive videos: emotion style and art style. In this paper, we present an innovative audio-driven talking face generation method called Style2Talker. It involves two stylized stages, namely Style-E and Style-A, which integrate text-controlled emotion style and picture-controlled art style into the final output. In order to prepare the scarce emotional text descriptions corresponding to the videos, we propose a labor-free paradigm that employs large-scale pretrained models to automatically annotate emotional text labels for existing audiovisual datasets. Incorporating the synthetic emotion texts, the Style-E stage utilizes a large-scale CLIP model to extract emotion representations, which are combined with the audio, serving as the condition for an efficient latent diffusion model designed to produce emotional motion coefficients of a 3DMM model. Moving on to the Style-A stage, we develop a coefficient-driven motion generator and an art-specific style path embedded in the well-known StyleGAN. This allows us to synthesize high-resolution artistically stylized talking head videos using the generated emotional motion coefficients and an art style source picture. Moreover, to better preserve image details and avoid artifacts, we provide StyleGAN with the multi-scale content features extracted from the identity image and refine its intermediate feature maps by the designed content encoder and refinement network, respectively. Extensive experimental results demonstrate our method outperforms existing state-of-the-art methods in terms of audio-lip synchronization and performance of both emotion style and art style.

</details>

#### [Say Anything with Any Style](https://arxiv.org/abs/2403.06363)
**Shuai Tan, Bin Ji, Yu Ding, Ye Pan** · 2024-03-11

<details>
<summary>Abstract</summary>

Generating stylized talking head with diverse head motions is crucial for achieving natural-looking videos but still remains challenging. Previous works either adopt a regressive method to capture the speaking style, resulting in a coarse style that is averaged across all training data, or employ a universal network to synthesize videos with different styles which causes suboptimal performance. To address these, we propose a novel dynamic-weight method, namely Say Anything withAny Style (SAAS), which queries the discrete style representation via a generative model with a learned style codebook. Specifically, we develop a multi-task VQ-VAE that incorporates three closely related tasks to learn a style codebook as a prior for style extraction. This discrete prior, along with the generative model, enhances the precision and robustness when extracting the speaking styles of the given style clips. By utilizing the extracted style, a residual architecture comprising a canonical branch and style-specific branch is employed to predict the mouth shapes conditioned on any driving audio while transferring the speaking style from the source to any desired one. To adapt to different speaking styles, we steer clear of employing a universal network by exploring an elaborate HyperStyle to produce the style-specific weights offset for the style branch. Furthermore, we construct a pose generator and a pose codebook to store the quantized pose representation, allowing us to sample diverse head motions aligned with the audio and the extracted style. Experiments demonstrate that our approach surpasses state-of-theart methods in terms of both lip-synchronization and stylized expression. Besides, we extend our SAAS to video-driven style editing field and achieve satisfactory performance.

</details>

#### [A Comparative Study of Perceptual Quality Metrics for Audio-driven Talking Head Videos](https://arxiv.org/abs/2403.06421)
**Weixia Zhang, Chengguang Zhu, Jingnan Gao, Yichao Yan et al.** · 2024-03-11

<details>
<summary>Abstract</summary>

The rapid advancement of Artificial Intelligence Generated Content (AIGC) technology has propelled audio-driven talking head generation, gaining considerable research attention for practical applications. However, performance evaluation research lags behind the development of talking head generation techniques. Existing literature relies on heuristic quantitative metrics without human validation, hindering accurate progress assessment. To address this gap, we collect talking head videos generated from four generative methods and conduct controlled psychophysical experiments on visual quality, lip-audio synchronization, and head movement naturalness. Our experiments validate consistency between model predictions and human annotations, identifying metrics that align better with human opinions than widely-used measures. We believe our work will facilitate performance evaluation and model development, providing insights into AIGC in a broader context. Code and data will be made available at https://github.com/zwx8981/ADTH-QA.

</details>

#### [Audio–video syncing with lip movements using generative deep neural networks](https://www.semanticscholar.org/paper/75327cbf02cd2343bdef4a69b93a2be3889b701f)
**Amal Mathew, Aaryl Saldanha, C. Babu** · 2024-03-11


#### [FaceChain-ImagineID: Freely Crafting High-Fidelity Diverse Talking Faces from Disentangled Audio](https://arxiv.org/abs/2403.01901)
**Chao Xu, Yang Liu, Jiazheng Xing, Weida Wang et al.** · 2024-03-04

<details>
<summary>Abstract</summary>

In this paper, we abstract the process of people hearing speech, extracting meaningful cues, and creating various dynamically audio-consistent talking faces, termed Listening and Imagining, into the task of high-fidelity diverse talking faces generation from a single audio. Specifically, it involves two critical challenges: one is to effectively decouple identity, content, and emotion from entangled audio, and the other is to maintain intra-video diversity and inter-video consistency. To tackle the issues, we first dig out the intricate relationships among facial factors and simplify the decoupling process, tailoring a Progressive Audio Disentanglement for accurate facial geometry and semantics learning, where each stage incorporates a customized training module responsible for a specific factor. Secondly, to achieve visually diverse and audio-synchronized animation solely from input audio within a single model, we introduce the Controllable Coherent Frame generation, which involves the flexible integration of three trainable adapters with frozen Latent Diffusion Models (LDMs) to focus on maintaining facial geometry and semantics, as well as texture and temporal coherence between frames. In this way, we inherit high-quality diverse generation from LDMs while significantly improving their controllability at a low training cost. Extensive experiments demonstrate the flexibility and effectiveness of our method in handling this paradigm. The codes will be released at https://github.com/modelscope/facechain.

</details>

#### [Context-aware Talking Face Video Generation](https://arxiv.org/abs/2402.18092)
**Meidai Xuanyuan, Yuwang Wang, Honglei Guo, Qionghai Dai** · 2024-02-28

<details>
<summary>Abstract</summary>

In this paper, we consider a novel and practical case for talking face video generation. Specifically, we focus on the scenarios involving multi-people interactions, where the talking context, such as audience or surroundings, is present. In these situations, the video generation should take the context into consideration in order to generate video content naturally aligned with driving audios and spatially coherent to the context. To achieve this, we provide a two-stage and cross-modal controllable video generation pipeline, taking facial landmarks as an explicit and compact control signal to bridge the driving audio, talking context and generated videos. Inside this pipeline, we devise a 3D video diffusion model, allowing for efficient contort of both spatial conditions (landmarks and context video), as well as audio condition for temporally coherent generation. The experimental results verify the advantage of the proposed method over other baselines in terms of audio-video synchronization, video fidelity and frame consistency.

</details>

#### [Learning Dynamic Tetrahedra for High-Quality Talking Head Synthesis](https://arxiv.org/abs/2402.17364)
**Zicheng Zhang, Ruobing Zheng, Ziwen Liu, Congying Han et al.** · 2024-02-27

<details>
<summary>Abstract</summary>

Recent works in implicit representations, such as Neural Radiance Fields (NeRF), have advanced the generation of realistic and animatable head avatars from video sequences. These implicit methods are still confronted by visual artifacts and jitters, since the lack of explicit geometric constraints poses a fundamental challenge in accurately modeling complex facial deformations. In this paper, we introduce Dynamic Tetrahedra (DynTet), a novel hybrid representation that encodes explicit dynamic meshes by neural networks to ensure geometric consistency across various motions and viewpoints. DynTet is parameterized by the coordinate-based networks which learn signed distance, deformation, and material texture, anchoring the training data into a predefined tetrahedra grid. Leveraging Marching Tetrahedra, DynTet efficiently decodes textured meshes with a consistent topology, enabling fast rendering through a differentiable rasterizer and supervision via a pixel loss. To enhance training efficiency, we incorporate classical 3D Morphable Models to facilitate geometry learning and define a canonical space for simplifying texture learning. These advantages are readily achievable owing to the effective geometric representation employed in DynTet. Compared with prior works, DynTet demonstrates significant improvements in fidelity, lip synchronization, and real-time performance according to various metrics. Beyond producing stable and visually appealing synthesis videos, our method also outputs the dynamic meshes which is promising to enable many emerging applications.

</details>

#### [EMO: Emote Portrait Alive -- Generating Expressive Portrait Videos with Audio2Video Diffusion Model under Weak Conditions](https://arxiv.org/abs/2402.17485)
**Linrui Tian, Qi Wang, Bang Zhang, Liefeng Bo** · 2024-02-27

<details>
<summary>Abstract</summary>

In this work, we tackle the challenge of enhancing the realism and expressiveness in talking head video generation by focusing on the dynamic and nuanced relationship between audio cues and facial movements. We identify the limitations of traditional techniques that often fail to capture the full spectrum of human expressions and the uniqueness of individual facial styles. To address these issues, we propose EMO, a novel framework that utilizes a direct audio-to-video synthesis approach, bypassing the need for intermediate 3D models or facial landmarks. Our method ensures seamless frame transitions and consistent identity preservation throughout the video, resulting in highly expressive and lifelike animations. Experimental results demonsrate that EMO is able to produce not only convincing speaking videos but also singing videos in various styles, significantly outperforming existing state-of-the-art methodologies in terms of expressiveness and realism.

</details>

#### [Resolution-Agnostic Neural Compression for High-Fidelity Portrait Video Conferencing via Implicit Radiance Fields](https://arxiv.org/abs/2402.16599)
**Yifei Li, Xiaohong Liu, Yicong Peng, Guangtao Zhai et al.** · 2024-02-26

<details>
<summary>Abstract</summary>

Video conferencing has caught much more attention recently. High fidelity and low bandwidth are two major objectives of video compression for video conferencing applications. Most pioneering methods rely on classic video compression codec without high-level feature embedding and thus can not reach the extremely low bandwidth. Recent works instead employ model-based neural compression to acquire ultra-low bitrates using sparse representations of each frame such as facial landmark information, while these approaches can not maintain high fidelity due to 2D image-based warping. In this paper, we propose a novel low bandwidth neural compression approach for high-fidelity portrait video conferencing using implicit radiance fields to achieve both major objectives. We leverage dynamic neural radiance fields to reconstruct high-fidelity talking head with expression features, which are represented as frame substitution for transmission. The overall system employs deep model to encode expression features at the sender and reconstruct portrait at the receiver with volume rendering as decoder for ultra-low bandwidth. In particular, with the characteristic of neural radiance fields based model, our compression approach is resolution-agnostic, which means that the low bandwidth achieved by our approach is independent of video resolution, while maintaining fidelity for higher resolution reconstruction. Experimental results demonstrate that our novel framework can (1) construct ultra-low bandwidth video conferencing, (2) maintain high fidelity portrait and (3) have better performance on high-resolution video compression than previous works.

</details>

#### [Audio-Visual Speech Enhancement in Noisy Environments via Emotion-Based Contextual Cues](https://arxiv.org/abs/2402.16394)
**Tassadaq Hussain, Kia Dashtipour, Yu Tsao, Amir Hussain** · 2024-02-26

<details>
<summary>Abstract</summary>

In real-world environments, background noise significantly degrades the intelligibility and clarity of human speech. Audio-visual speech enhancement (AVSE) attempts to restore speech quality, but existing methods often fall short, particularly in dynamic noise conditions. This study investigates the inclusion of emotion as a novel contextual cue within AVSE, hypothesizing that incorporating emotional understanding can improve speech enhancement performance. We propose a novel emotion-aware AVSE system that leverages both auditory and visual information. It extracts emotional features from the facial landmarks of the speaker and fuses them with corresponding audio and visual modalities. This enriched data serves as input to a deep UNet-based encoder-decoder network, specifically designed to orchestrate the fusion of multimodal information enhanced with emotion. The network iteratively refines the enhanced speech representation through an encoder-decoder architecture, guided by perceptually-inspired loss functions for joint learning and optimization. We train and evaluate the model on the CMU Multimodal Opinion Sentiment and Emotion Intensity (CMU-MOSEI) dataset, a rich repository of audio-visual recordings with annotated emotions. Our comprehensive evaluation demonstrates the effectiveness of emotion as a contextual cue for AVSE. By integrating emotional features, the proposed system achieves significant improvements in both objective and subjective assessments of speech quality and intelligibility, especially in challenging noise environments. Compared to baseline AVSE and audio-only speech enhancement systems, our approach exhibits a noticeable increase in PESQ and STOI, indicating higher perceptual quality and intelligibility. Large-scale listening tests corroborate these findings, suggesting improved human understanding of enhanced speech.

</details>

#### [AVI-Talking: Learning Audio-Visual Instructions for Expressive 3D Talking Face Generation](https://arxiv.org/abs/2402.16124)
**Yasheng Sun, Wenqing Chu, Hang Zhou, Kaisiyuan Wang et al.** · 2024-02-25

<details>
<summary>Abstract</summary>

While considerable progress has been made in achieving accurate lip synchronization for 3D speech-driven talking face generation, the task of incorporating expressive facial detail synthesis aligned with the speaker's speaking status remains challenging. Our goal is to directly leverage the inherent style information conveyed by human speech for generating an expressive talking face that aligns with the speaking status. In this paper, we propose AVI-Talking, an Audio-Visual Instruction system for expressive Talking face generation. This system harnesses the robust contextual reasoning and hallucination capability offered by Large Language Models (LLMs) to instruct the realistic synthesis of 3D talking faces. Instead of directly learning facial movements from human speech, our two-stage strategy involves the LLMs first comprehending audio information and generating instructions implying expressive facial details seamlessly corresponding to the speech. Subsequently, a diffusion-based generative network executes these instructions. This two-stage process, coupled with the incorporation of LLMs, enhances model interpretability and provides users with flexibility to comprehend instructions and specify desired operations or modifications. Extensive experiments showcase the effectiveness of our approach in producing vivid talking faces with expressive facial movements and consistent emotional status.

</details>

#### [Lip Synchronization Model For Sinhala Language Using Machine Learning](https://www.semanticscholar.org/paper/20e6ef1cae962c4bf37c906cb6049664b18a24af)
**Dilani Ranaweera, R. Weerasinghe, R. Dinalankara** · 2024-02-21

<details>
<summary>Abstract</summary>

Realistic lip-synchronized animations can be produced by the appropriately timed voice and lip motions of the cartoon character. This process is called as “lip synchronization”. Building a talking face for languages such as English, Korean, and Portuguese has been subject of numerous studies. Compared to other languages, Sinhala is a low-resource language due to less contribution in these researches. This research study focuses to build a frontal view of a synthetic mouth part with smooth lip movements rather than opening and closing while speaking Sinhala sentences. The most difficult challenge is to match the basic sounds, “phonemes” with the lip movement called “visemes”. This study has been used static viseme approach by deriving twenty three (23) Sinhala viseme classes and a deep learning model has been developed to map visemes with Sinhala letters. In system implementation, text input is provided first, after which the system produces audio and the deep learning model generates a collection of visemes based on the given text. The system interface then offers three options for playing the visemes at various speeds, including fast, normal, and slow. The user interface was created in Python, and the deep learning model is integrated into the system. This model will be very helpful to use in cartoon industry to build Sinhala speaking cartoon characters and also be used to train deaf people to read lips.

</details>

#### [StyleDubber: Towards Multi-Scale Style Learning for Movie Dubbing](https://arxiv.org/abs/2402.12636)
**Gaoxiang Cong, Yuankai Qi, Liang Li, Amin Beheshti et al.** · 2024-02-20

<details>
<summary>Abstract</summary>

Given a script, the challenge in Movie Dubbing (Visual Voice Cloning, V2C) is to generate speech that aligns well with the video in both time and emotion, based on the tone of a reference audio track. Existing state-of-the-art V2C models break the phonemes in the script according to the divisions between video frames, which solves the temporal alignment problem but leads to incomplete phoneme pronunciation and poor identity stability. To address this problem, we propose StyleDubber, which switches dubbing learning from the frame level to phoneme level. It contains three main components: (1) A multimodal style adaptor operating at the phoneme level to learn pronunciation style from the reference audio, and generate intermediate representations informed by the facial emotion presented in the video; (2) An utterance-level style learning module, which guides both the mel-spectrogram decoding and the refining processes from the intermediate embeddings to improve the overall style expression; And (3) a phoneme-guided lip aligner to maintain lip sync. Extensive experiments on two of the primary benchmarks, V2C and Grid, demonstrate the favorable performance of the proposed method as compared to the current stateof-the-art. The code will be made available at https://github.com/GalaxyCong/StyleDubber.

</details>

#### [AnnoTheia: A Semi-Automatic Annotation Toolkit for Audio-Visual Speech Technologies](https://arxiv.org/abs/2402.13152)
**José-M. Acosta-Triana, David Gimeno-Gómez, Carlos-D. Martínez-Hinarejos** · 2024-02-20

<details>
<summary>Abstract</summary>

More than 7,000 known languages are spoken around the world. However, due to the lack of annotated resources, only a small fraction of them are currently covered by speech technologies. Albeit self-supervised speech representations, recent massive speech corpora collections, as well as the organization of challenges, have alleviated this inequality, most studies are mainly benchmarked on English. This situation is aggravated when tasks involving both acoustic and visual speech modalities are addressed. In order to promote research on low-resource languages for audio-visual speech technologies, we present AnnoTheia, a semi-automatic annotation toolkit that detects when a person speaks on the scene and the corresponding transcription. In addition, to show the complete process of preparing AnnoTheia for a language of interest, we also describe the adaptation of a pre-trained model for active speaker detection to Spanish, using a database not initially conceived for this type of task. The AnnoTheia toolkit, tutorials, and pre-trained models are available on GitHub.

</details>

#### [DiffSpeaker: Speech-Driven 3D Facial Animation with Diffusion Transformer](https://arxiv.org/abs/2402.05712)
**Zhiyuan Ma, Xiangyu Zhu, Guojun Qi, Chen Qian et al.** · 2024-02-08

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation is important for many multimedia applications. Recent work has shown promise in using either Diffusion models or Transformer architectures for this task. However, their mere aggregation does not lead to improved performance. We suspect this is due to a shortage of paired audio-4D data, which is crucial for the Transformer to effectively perform as a denoiser within the Diffusion framework. To tackle this issue, we present DiffSpeaker, a Transformer-based network equipped with novel biased conditional attention modules. These modules serve as substitutes for the traditional self/cross-attention in standard Transformers, incorporating thoughtfully designed biases that steer the attention mechanisms to concentrate on both the relevant task-specific and diffusion-related conditions. We also explore the trade-off between accurate lip synchronization and non-verbal facial expressions within the Diffusion paradigm. Experiments show our model not only achieves state-of-the-art performance on existing benchmarks, but also fast inference speed owing to its ability to generate facial motions in parallel.

</details>

#### [One-shot Neural Face Reenactment via Finding Directions in GAN's Latent Space](https://arxiv.org/abs/2402.03553)
**Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras et al.** · 2024-02-05

<details>
<summary>Abstract</summary>

In this paper, we present our framework for neural face/head reenactment whose goal is to transfer the 3D head orientation and expression of a target face to a source face. Previous methods focus on learning embedding networks for identity and head pose/expression disentanglement which proves to be a rather hard task, degrading the quality of the generated images. We take a different approach, bypassing the training of such networks, by using (fine-tuned) pre-trained GANs which have been shown capable of producing high-quality facial images. Because GANs are characterized by weak controllability, the core of our approach is a method to discover which directions in latent GAN space are responsible for controlling head pose and expression variations. We present a simple pipeline to learn such directions with the aid of a 3D shape model which, by construction, inherently captures disentangled directions for head pose, identity, and expression. Moreover, we show that by embedding real images in the GAN latent space, our method can be successfully used for the reenactment of real-world faces. Our method features several favorable properties including using a single source image (one-shot) and enabling cross-person reenactment. Extensive qualitative and quantitative results show that our approach typically produces reenacted faces of notably higher quality than those produced by state-of-the-art methods for the standard benchmarks of VoxCeleb1 & 2.

</details>

#### [EmoSpeaker: One-shot Fine-grained Emotion-Controlled Talking Face Generation](https://arxiv.org/abs/2402.01422)
**Guanwen Feng, Haoran Cheng, Yunan Li, Zhiyuan Ma et al.** · 2024-02-02

<details>
<summary>Abstract</summary>

Implementing fine-grained emotion control is crucial for emotion generation tasks because it enhances the expressive capability of the generative model, allowing it to accurately and comprehensively capture and express various nuanced emotional states, thereby improving the emotional quality and personalization of generated content. Generating fine-grained facial animations that accurately portray emotional expressions using only a portrait and an audio recording presents a challenge. In order to address this challenge, we propose a visual attribute-guided audio decoupler. This enables the obtention of content vectors solely related to the audio content, enhancing the stability of subsequent lip movement coefficient predictions. To achieve more precise emotional expression, we introduce a fine-grained emotion coefficient prediction module. Additionally, we propose an emotion intensity control method using a fine-grained emotion matrix. Through these, effective control over emotional expression in the generated videos and finer classification of emotion intensity are accomplished. Subsequently, a series of 3DMM coefficient generation networks are designed to predict 3D coefficients, followed by the utilization of a rendering network to generate the final video. Our experimental results demonstrate that our proposed method, EmoSpeaker, outperforms existing emotional talking face generation methods in terms of expression variation and lip synchronization. Project page: https://peterfanfan.github.io/EmoSpeaker/

</details>

#### [NeRF-AD: Neural Radiance Field with Attention-based Disentanglement for Talking Face Synthesis](https://arxiv.org/abs/2401.12568)
**Chongke Bi, Xiaoxing Liu, Zhilei Liu** · 2024-01-23

<details>
<summary>Abstract</summary>

Talking face synthesis driven by audio is one of the current research hotspots in the fields of multidimensional signal processing and multimedia. Neural Radiance Field (NeRF) has recently been brought to this research field in order to enhance the realism and 3D effect of the generated faces. However, most existing NeRF-based methods either burden NeRF with complex learning tasks while lacking methods for supervised multimodal feature fusion, or cannot precisely map audio to the facial region related to speech movements. These reasons ultimately result in existing methods generating inaccurate lip shapes. This paper moves a portion of NeRF learning tasks ahead and proposes a talking face synthesis method via NeRF with attention-based disentanglement (NeRF-AD). In particular, an Attention-based Disentanglement module is introduced to disentangle the face into Audio-face and Identity-face using speech-related facial action unit (AU) information. To precisely regulate how audio affects the talking face, we only fuse the Audio-face with audio feature. In addition, AU information is also utilized to supervise the fusion of these two modalities. Extensive qualitative and quantitative experiments demonstrate that our NeRF-AD outperforms state-of-the-art methods in generating realistic talking face videos, including image quality and lip synchronization. To view video results, please refer to https://xiaoxingliu02.github.io/NeRF-AD.

</details>

#### [Real3D-Portrait: One-shot Realistic 3D Talking Portrait Synthesis](https://arxiv.org/abs/2401.08503)
**Zhenhui Ye, Tianyun Zhong, Yi Ren, Jiaqi Yang et al.** · 2024-01-16

<details>
<summary>Abstract</summary>

One-shot 3D talking portrait generation aims to reconstruct a 3D avatar from an unseen image, and then animate it with a reference video or audio to generate a talking portrait video. The existing methods fail to simultaneously achieve the goals of accurate 3D avatar reconstruction and stable talking face animation. Besides, while the existing works mainly focus on synthesizing the head part, it is also vital to generate natural torso and background segments to obtain a realistic talking portrait video. To address these limitations, we present Real3D-Potrait, a framework that (1) improves the one-shot 3D reconstruction power with a large image-to-plane model that distills 3D prior knowledge from a 3D face generative model; (2) facilitates accurate motion-conditioned animation with an efficient motion adapter; (3) synthesizes realistic video with natural torso movement and switchable background using a head-torso-background super-resolution model; and (4) supports one-shot audio-driven talking face generation with a generalizable audio-to-motion model. Extensive experiments show that Real3D-Portrait generalizes well to unseen identities and generates more realistic talking portrait videos compared to previous methods. Video samples and source code are available at https://real3dportrait.github.io .

</details>

#### [EmoTalker: Emotionally Editable Talking Face Generation via Diffusion Model](https://arxiv.org/abs/2401.08049)
**Bingyuan Zhang, Xulong Zhang, Ning Cheng, Jun Yu et al.** · 2024-01-16

<details>
<summary>Abstract</summary>

In recent years, the field of talking faces generation has attracted considerable attention, with certain methods adept at generating virtual faces that convincingly imitate human expressions. However, existing methods face challenges related to limited generalization, particularly when dealing with challenging identities. Furthermore, methods for editing expressions are often confined to a singular emotion, failing to adapt to intricate emotions. To overcome these challenges, this paper proposes EmoTalker, an emotionally editable portraits animation approach based on the diffusion model. EmoTalker modifies the denoising process to ensure preservation of the original portrait's identity during inference. To enhance emotion comprehension from text input, Emotion Intensity Block is introduced to analyze fine-grained emotions and strengths derived from prompts. Additionally, a crafted dataset is harnessed to enhance emotion comprehension within prompts. Experiments show the effectiveness of EmoTalker in generating high-quality, emotionally customizable facial expressions.

</details>

#### [Towards a Simultaneous and Granular Identity-Expression Control in Personalized Face Generation](https://arxiv.org/abs/2401.01207)
**Renshuai Liu, Bowen Ma, Wei Zhang, Zhipeng Hu et al.** · 2024-01-02

<details>
<summary>Abstract</summary>

In human-centric content generation, the pre-trained text-to-image models struggle to produce user-wanted portrait images, which retain the identity of individuals while exhibiting diverse expressions. This paper introduces our efforts towards personalized face generation. To this end, we propose a novel multi-modal face generation framework, capable of simultaneous identity-expression control and more fine-grained expression synthesis. Our expression control is so sophisticated that it can be specialized by the fine-grained emotional vocabulary. We devise a novel diffusion model that can undertake the task of simultaneously face swapping and reenactment. Due to the entanglement of identity and expression, it's nontrivial to separately and precisely control them in one framework, thus has not been explored yet. To overcome this, we propose several innovative designs in the conditional diffusion model, including balancing identity and expression encoder, improved midpoint sampling, and explicitly background conditioning. Extensive experiments have demonstrated the controllability and scalability of the proposed framework, in comparison with state-of-the-art text-to-image, face swapping, and face reenactment methods.

</details>

#### [LatentSync: Audio Conditioned Latent Diffusion Models for Lip Sync](https://www.semanticscholar.org/paper/a9ec5c7585a50a5b9cc4458f6b5506693b658be4)
**Chunyu Li, Chao Zhang, Weikai Xu, Jinghui Xie et al.** · 2024-01-01


#### [SD-NeRF: Towards Lifelike Talking Head Animation via Spatially-Adaptive Dual-Driven NeRFs](https://www.semanticscholar.org/paper/e3ad82f6d53d582e03d51bd017f47fcd157fe4ba)
**Shuai Shen, Wanhua Li, Xiaoke Huang, Zhengbiao Zhu et al.** · 2024-01-01

<details>
<summary>Abstract</summary>

Recent years have witnessed great progress in audio-driven talking head animation. Among these methods, the 3D-based ones better preserve the 3D consistency of the generated head and produce more natural results compared with 2D-based approaches. However, most 3D-based methods employ 3D morphable face models as the intermediate representation and involve multi-stage training, which may lead to error accumulation. To alleviate this problem, in this article, we propose a fully end-to-end talking head animation method, which implicitly grasps the 3D structures by learning a conditional Neural Radiance Field (NeRF). As NeRF has proven to be an effective tool for 3D modeling, one can learn dynamic neural radiance fields conditioned on audio signals for talking head synthesis. Furthermore, we argue that audio signals cannot fully drive a lifelike talking head. When people are talking, they usually show many spontaneous facial movements like blinks and brow movements, which makes talkers natural and real. These movements cannot be fully driven by the audio signals since they are highly unrelated to the audio. Therefore, we incorporate motion information as another driving factor and develop an audio-motion dual-driven NeRF model to take a step toward more lifelike talking head synthesis. On this basis, as audio and motion mainly affect different regions of the human face, we propose a Spatially-adaptive Dual-driven NeRF (SD-NeRF), which fuses these two driven factors with a spatially-adaptive cross-attention mechanism. Quantitative and qualitative results demonstrate that, with finer facial controls, our method produces more realistic talking head videos compared with existing advanced works.

</details>

#### [MergeTalk: Audio-Driven Talking Head Generation From Single Image With Feature Merge](https://www.semanticscholar.org/paper/3c6249961137d5262a1f874ea9837918b3ebb946)
**Jian Gao, Chang Shu, Ximin Zheng, Zheng Lu et al.** · 2024-01-01

<details>
<summary>Abstract</summary>

Audio-driven talking head generation has wide real world applications but remains challenging due to the problems such as audio-lip synchronization, head poses, identity preservation, video quality, etc. We propose a novel two-stage framework that uses explicit 3D face images rendered from a 3D model based on the audio input, as intermediate features. We devise two independent 3D motion parameter generation networks to generate expression and pose parameters for the popular 3DMM model to solve the audio-lip synchronization problem and natural head poses without losing identity information. To improve the final talking head quality such as avoiding facial distortion and artifacts, we propose a novel face feature merge network to accurately extract and fuse the background, identity information, facial texture from the source image, and the lip movements and head poses from the 3D face images, and generate the final videos based on generative adversarial networks. Extensive experiments show that our framework outperforms the SOTA methods in several aspects and has good generalization ability.

</details>

</details>

<details open>
<summary><h3>2023</h3></summary>

#### [EFHQ: Multi-purpose ExtremePose-Face-HQ dataset](https://arxiv.org/abs/2312.17205)
**Trung Tuan Dao, Duc Hong Vu, Cuong Pham, Anh Tran** · 2023-12-28

<details>
<summary>Abstract</summary>

The existing facial datasets, while having plentiful images at near frontal views, lack images with extreme head poses, leading to the downgraded performance of deep learning models when dealing with profile or pitched faces. This work aims to address this gap by introducing a novel dataset named Extreme Pose Face High-Quality Dataset (EFHQ), which includes a maximum of 450k high-quality images of faces at extreme poses. To produce such a massive dataset, we utilize a novel and meticulous dataset processing pipeline to curate two publicly available datasets, VFHQ and CelebV-HQ, which contain many high-resolution face videos captured in various settings. Our dataset can complement existing datasets on various facial-related tasks, such as facial synthesis with 2D/3D-aware GAN, diffusion-based text-to-image face generation, and face reenactment. Specifically, training with EFHQ helps models generalize well across diverse poses, significantly improving performance in scenarios involving extreme views, confirmed by extensive experiments. Additionally, we utilize EFHQ to define a challenging cross-view face verification benchmark, in which the performance of SOTA face recognition models drops 5-37% compared to frontal-to-frontal scenarios, aiming to stimulate studies on face recognition under severe pose conditions in the wild.

</details>

#### [SAiD: Speech-driven Blendshape Facial Animation with Diffusion](https://arxiv.org/abs/2401.08655)
**Inkyu Park, Jaewoong Cho** · 2023-12-25

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation is challenging due to the scarcity of large-scale visual-audio datasets despite extensive research. Most prior works, typically focused on learning regression models on a small dataset using the method of least squares, encounter difficulties generating diverse lip movements from speech and require substantial effort in refining the generated outputs. To address these issues, we propose a speech-driven 3D facial animation with a diffusion model (SAiD), a lightweight Transformer-based U-Net with a cross-modality alignment bias between audio and visual to enhance lip synchronization. Moreover, we introduce BlendVOCA, a benchmark dataset of pairs of speech audio and parameters of a blendshape facial model, to address the scarcity of public resources. Our experimental results demonstrate that the proposed approach achieves comparable or superior performance in lip synchronization to baselines, ensures more diverse lip movements, and streamlines the animation editing process.

</details>

#### [TransFace: Unit-Based Audio-Visual Speech Synthesizer for Talking Head Translation](https://arxiv.org/abs/2312.15197)
**Xize Cheng, Rongjie Huang, Linjun Li, Tao Jin et al.** · 2023-12-23

<details>
<summary>Abstract</summary>

Direct speech-to-speech translation achieves high-quality results through the introduction of discrete units obtained from self-supervised learning. This approach circumvents delays and cascading errors associated with model cascading. However, talking head translation, converting audio-visual speech (i.e., talking head video) from one language into another, still confronts several challenges compared to audio speech: (1) Existing methods invariably rely on cascading, synthesizing via both audio and text, resulting in delays and cascading errors. (2) Talking head translation has a limited set of reference frames. If the generated translation exceeds the length of the original speech, the video sequence needs to be supplemented by repeating frames, leading to jarring video transitions. In this work, we propose a model for talking head translation, \textbf{TransFace}, which can directly translate audio-visual speech into audio-visual speech in other languages. It consists of a speech-to-unit translation model to convert audio speech into discrete units and a unit-based audio-visual speech synthesizer, Unit2Lip, to re-synthesize synchronized audio-visual speech from discrete units in parallel. Furthermore, we introduce a Bounded Duration Predictor, ensuring isometric talking head translation and preventing duplicate reference frames. Experiments demonstrate that our proposed Unit2Lip model significantly improves synchronization (1.601 and 0.982 on LSE-C for the original and generated audio speech, respectively) and boosts inference speed by a factor of 4.35 on LRS2. Additionally, TransFace achieves impressive BLEU scores of 61.93 and 47.55 for Es-En and Fr-En on LRS3-T and 100% isochronous translations.

</details>

#### [DREAM-Talk: Diffusion-based Realistic Emotional Audio-driven Method for Single Image Talking Face Generation](https://arxiv.org/abs/2312.13578)
**Chenxu Zhang, Chao Wang, Jianfeng Zhang, Hongyi Xu et al.** · 2023-12-21

<details>
<summary>Abstract</summary>

The generation of emotional talking faces from a single portrait image remains a significant challenge. The simultaneous achievement of expressive emotional talking and accurate lip-sync is particularly difficult, as expressiveness is often compromised for the accuracy of lip-sync. As widely adopted by many prior works, the LSTM network often fails to capture the subtleties and variations of emotional expressions. To address these challenges, we introduce DREAM-Talk, a two-stage diffusion-based audio-driven framework, tailored for generating diverse expressions and accurate lip-sync concurrently. In the first stage, we propose EmoDiff, a novel diffusion module that generates diverse highly dynamic emotional expressions and head poses in accordance with the audio and the referenced emotion style. Given the strong correlation between lip motion and audio, we then refine the dynamics with enhanced lip-sync accuracy using audio features and emotion style. To this end, we deploy a video-to-video rendering module to transfer the expressions and lip motions from our proxy 3D avatar to an arbitrary portrait. Both quantitatively and qualitatively, DREAM-Talk outperforms state-of-the-art methods in terms of expressiveness, lip-sync accuracy and perceptual quality.

</details>

#### [AE-NeRF: Audio Enhanced Neural Radiance Field for Few Shot Talking Head Synthesis](https://arxiv.org/abs/2312.10921)
**Dongze Li, Kang Zhao, Wei Wang, Bo Peng et al.** · 2023-12-18

<details>
<summary>Abstract</summary>

Audio-driven talking head synthesis is a promising topic with wide applications in digital human, film making and virtual reality. Recent NeRF-based approaches have shown superiority in quality and fidelity compared to previous studies. However, when it comes to few-shot talking head generation, a practical scenario where only few seconds of talking video is available for one identity, two limitations emerge: 1) they either have no base model, which serves as a facial prior for fast convergence, or ignore the importance of audio when building the prior; 2) most of them overlook the degree of correlation between different face regions and audio, e.g., mouth is audio related, while ear is audio independent. In this paper, we present Audio Enhanced Neural Radiance Field (AE-NeRF) to tackle the above issues, which can generate realistic portraits of a new speaker with fewshot dataset. Specifically, we introduce an Audio Aware Aggregation module into the feature fusion stage of the reference scheme, where the weight is determined by the similarity of audio between reference and target image. Then, an Audio-Aligned Face Generation strategy is proposed to model the audio related and audio independent regions respectively, with a dual-NeRF framework. Extensive experiments have shown AE-NeRF surpasses the state-of-the-art on image fidelity, audio-lip synchronization, and generalization ability, even in limited training set or training iterations.

</details>

#### [VectorTalker: SVG Talking Face Generation with Progressive Vectorisation](https://arxiv.org/abs/2312.11568)
**Hao Hu, Xuan Wang, Jingxiang Sun, Yanbo Fan et al.** · 2023-12-18

<details>
<summary>Abstract</summary>

High-fidelity and efficient audio-driven talking head generation has been a key research topic in computer graphics and computer vision. In this work, we study vector image based audio-driven talking head generation. Compared with directly animating the raster image that most widely used in existing works, vector image enjoys its excellent scalability being used for many applications. There are two main challenges for vector image based talking head generation: the high-quality vector image reconstruction w.r.t. the source portrait image and the vivid animation w.r.t. the audio signal. To address these, we propose a novel scalable vector graphic reconstruction and animation method, dubbed VectorTalker. Specifically, for the highfidelity reconstruction, VectorTalker hierarchically reconstructs the vector image in a coarse-to-fine manner. For the vivid audio-driven facial animation, we propose to use facial landmarks as intermediate motion representation and propose an efficient landmark-driven vector image deformation module. Our approach can handle various styles of portrait images within a unified framework, including Japanese manga, cartoon, and photorealistic images. We conduct extensive quantitative and qualitative evaluations and the experimental results demonstrate the superiority of VectorTalker in both vector graphic reconstruction and audio-driven animation.

</details>

#### [Learning Dense Correspondence for NeRF-Based Face Reenactment](https://arxiv.org/abs/2312.10422)
**Songlin Yang, Wei Wang, Yushi Lan, Xiangyu Fan et al.** · 2023-12-16

<details>
<summary>Abstract</summary>

Face reenactment is challenging due to the need to establish dense correspondence between various face representations for motion transfer. Recent studies have utilized Neural Radiance Field (NeRF) as fundamental representation, which further enhanced the performance of multi-view face reenactment in photo-realism and 3D consistency. However, establishing dense correspondence between different face NeRFs is non-trivial, because implicit representations lack ground-truth correspondence annotations like mesh-based 3D parametric models (e.g., 3DMM) with index-aligned vertexes. Although aligning 3DMM space with NeRF-based face representations can realize motion control, it is sub-optimal for their limited face-only modeling and low identity fidelity. Therefore, we are inspired to ask: Can we learn the dense correspondence between different NeRF-based face representations without a 3D parametric model prior? To address this challenge, we propose a novel framework, which adopts tri-planes as fundamental NeRF representation and decomposes face tri-planes into three components: canonical tri-planes, identity deformations, and motion. In terms of motion control, our key contribution is proposing a Plane Dictionary (PlaneDict) module, which efficiently maps the motion conditions to a linear weighted addition of learnable orthogonal plane bases. To the best of our knowledge, our framework is the first method that achieves one-shot multi-view face reenactment without a 3D parametric model prior. Extensive experiments demonstrate that we produce better results in fine-grained motion control and identity preservation than previous methods.

</details>

#### [DreamTalk: When Emotional Talking Head Generation Meets Diffusion Probabilistic Models](https://arxiv.org/abs/2312.09767)
**Yifeng Ma, Shiwei Zhang, Jiayu Wang, Xiang Wang et al.** · 2023-12-15

<details>
<summary>Abstract</summary>

Emotional talking head generation has attracted growing attention. Previous methods, which are mainly GAN-based, still struggle to consistently produce satisfactory results across diverse emotions and cannot conveniently specify personalized emotions. In this work, we leverage powerful diffusion models to address the issue and propose DreamTalk, a framework that employs meticulous design to unlock the potential of diffusion models in generating emotional talking heads. Specifically, DreamTalk consists of three crucial components: a denoising network, a style-aware lip expert, and a style predictor. The diffusion-based denoising network can consistently synthesize high-quality audio-driven face motions across diverse emotions. To enhance lip-motion accuracy and emotional fullness, we introduce a style-aware lip expert that can guide lip-sync while preserving emotion intensity. To more conveniently specify personalized emotions, a diffusion-based style predictor is utilized to predict the personalized emotion directly from the audio, eliminating the need for extra emotion reference. By this means, DreamTalk can consistently generate vivid talking faces across diverse emotions and conveniently specify personalized emotions. Extensive experiments validate DreamTalk's effectiveness and superiority. The code is available at https://github.com/ali-vilab/dreamtalk.

</details>

#### [Speech to Lip Sync generation using Deep learning Algorithm](https://www.semanticscholar.org/paper/114f13f0af15e596b7e6828a35c827b51f9a0a5f)
**P. Hirishikesh, Mvs Yaswanth, H. A.** · 2023-12-13

<details>
<summary>Abstract</summary>

The emerging growth of artificial intelligence (AI) technology created a way for many innovative developments. Speech to lip synchronization (STLS) is one of the key requirement in applications related to film making, voice modulation, video creation etc. The identification of speaking face synchronized with the voice need to be done accurately to improve the quality of the video. Many existing systems face the problem while imposing the new audio into the existing video files. The movement of lips dynamically changes according to the speaking faces. To solve the missing synchronization problem of existing videos to retrieve the original quality from the video input, the proposed system is focused on creating accurate lip synchronization model using Deep SyncNet (DSN) using Deep learning convolution architecture. The timing accuracy of the video synchronization extensively improve the quality of the video and demands real time experience from the video footage. Detection of facial variations without extracting the features are particularly challenging. The proposed system considers the existing challenges like misclassification, delayed synchronization and evaluated the SyncNet achieved the accuracy of 95% on lip synchronization with labelled dataset.

</details>

#### [GSmoothFace: Generalized Smooth Talking Face Generation via Fine Grained 3D Face Guidance](https://arxiv.org/abs/2312.07385)
**Haiming Zhang, Zhihao Yuan, Chaoda Zheng, Xu Yan et al.** · 2023-12-12

<details>
<summary>Abstract</summary>

Although existing speech-driven talking face generation methods achieve significant progress, they are far from real-world application due to the avatar-specific training demand and unstable lip movements. To address the above issues, we propose the GSmoothFace, a novel two-stage generalized talking face generation model guided by a fine-grained 3d face model, which can synthesize smooth lip dynamics while preserving the speaker's identity. Our proposed GSmoothFace model mainly consists of the Audio to Expression Prediction (A2EP) module and the Target Adaptive Face Translation (TAFT) module. Specifically, we first develop the A2EP module to predict expression parameters synchronized with the driven speech. It uses a transformer to capture the long-term audio context and learns the parameters from the fine-grained 3D facial vertices, resulting in accurate and smooth lip-synchronization performance. Afterward, the well-designed TAFT module, empowered by Morphology Augmented Face Blending (MAFB), takes the predicted expression parameters and target video as inputs to modify the facial region of the target video without distorting the background content. The TAFT effectively exploits the identity appearance and background context in the target video, which makes it possible to generalize to different speakers without retraining. Both quantitative and qualitative experiments confirm the superiority of our method in terms of realism, lip synchronization, and visual quality. See the project page for code, data, and request pre-trained models: https://zhanghm1995.github.io/GSmoothFace.

</details>

#### [Neural Text to Articulate Talk: Deep Text to Audiovisual Speech Synthesis achieving both Auditory and Photo-realism](https://arxiv.org/abs/2312.06613)
**Georgios Milis, Panagiotis P. Filntisis, Anastasios Roussos, Petros Maragos** · 2023-12-11

<details>
<summary>Abstract</summary>

Recent advances in deep learning for sequential data have given rise to fast and powerful models that produce realistic videos of talking humans. The state of the art in talking face generation focuses mainly on lip-syncing, being conditioned on audio clips. However, having the ability to synthesize talking humans from text transcriptions rather than audio is particularly beneficial for many applications and is expected to receive more and more attention, following the recent breakthroughs in large language models. For that, most methods implement a cascaded 2-stage architecture of a text-to-speech module followed by an audio-driven talking face generator, but this ignores the highly complex interplay between audio and visual streams that occurs during speaking. In this paper, we propose the first, to the best of our knowledge, text-driven audiovisual speech synthesizer that uses Transformers and does not follow a cascaded approach. Our method, which we call NEUral Text to ARticulate Talk (NEUTART), is a talking face generator that uses a joint audiovisual feature space, as well as speech-informed 3D facial reconstructions and a lip-reading loss for visual supervision. The proposed model produces photorealistic talking face videos with human-like articulation and well-synced audiovisual streams. Our experiments on audiovisual datasets as well as in-the-wild videos reveal state-of-the-art generation quality both in terms of objective metrics and human evaluation.

</details>

#### [DiT-Head: High-Resolution Talking Head Synthesis using Diffusion Transformers](https://arxiv.org/abs/2312.06400)
**Aaron Mir, Eduardo Alonso, Esther Mondragón** · 2023-12-11

<details>
<summary>Abstract</summary>

We propose a novel talking head synthesis pipeline called "DiT-Head", which is based on diffusion transformers and uses audio as a condition to drive the denoising process of a diffusion model. Our method is scalable and can generalise to multiple identities while producing high-quality results. We train and evaluate our proposed approach and compare it against existing methods of talking head synthesis. We show that our model can compete with these methods in terms of visual quality and lip-sync accuracy. Our results highlight the potential of our proposed approach to be used for a wide range of applications, including virtual assistants, entertainment, and education. For a video demonstration of the results and our user study, please refer to our supplementary material.

</details>

#### [FT2TF: First-Person Statement Text-To-Talking Face Generation](https://arxiv.org/abs/2312.05430)
**Xingjian Diao, Ming Cheng, Wayner Barrios, SouYoung Jin** · 2023-12-09

<details>
<summary>Abstract</summary>

Talking face generation has gained immense popularity in the computer vision community, with various applications including AR, VR, teleconferencing, digital assistants, and avatars. Traditional methods are mainly audio-driven, which have to deal with the inevitable resource-intensive nature of audio storage and processing. To address such a challenge, we propose FT2TF - First-Person Statement Text-To-Talking Face Generation, a novel one-stage end-to-end pipeline for talking face generation driven by first-person statement text. Different from previous work, our model only leverages visual and textual information without any other sources (e.g., audio/landmark/pose) during inference. Extensive experiments are conducted on LRS2 and LRS3 datasets, and results on multi-dimensional evaluation metrics are reported. Both quantitative and qualitative results showcase that FT2TF outperforms existing relevant methods and reaches the state-of-the-art. This achievement highlights our model's capability to bridge first-person statements and dynamic face generation, providing insightful guidance for future work.

</details>

#### [MyPortrait: Morphable Prior-Guided Personalized Portrait Generation](https://arxiv.org/abs/2312.02703)
**Bo Ding, Zhenfeng Fan, Shuang Yang, Shihong Xia** · 2023-12-05

<details>
<summary>Abstract</summary>

Generating realistic talking faces is an interesting and long-standing topic in the field of computer vision. Although significant progress has been made, it is still challenging to generate high-quality dynamic faces with personalized details. This is mainly due to the inability of the general model to represent personalized details and the generalization problem to unseen controllable parameters. In this work, we propose Myportrait, a simple, general, and flexible framework for neural portrait generation. We incorporate personalized prior in a monocular video and morphable prior in 3D face morphable space for generating personalized details under novel controllable parameters. Our proposed framework supports both video-driven and audio-driven face animation given a monocular video of a single person. Distinguished by whether the test data is sent to training or not, our method provides a real-time online version and a high-quality offline version. Comprehensive experiments in various metrics demonstrate the superior performance of our method over the state-of-the-art methods. The code will be publicly available.

</details>

#### [AV2AV: Direct Audio-Visual Speech to Audio-Visual Speech Translation with Unified Audio-Visual Speech Representation](https://arxiv.org/abs/2312.02512)
**Jeongsoo Choi, Se Jin Park, Minsu Kim, Yong Man Ro** · 2023-12-05

<details>
<summary>Abstract</summary>

This paper proposes a novel direct Audio-Visual Speech to Audio-Visual Speech Translation (AV2AV) framework, where the input and output of the system are multimodal (i.e., audio and visual speech). With the proposed AV2AV, two key advantages can be brought: 1) We can perform real-like conversations with individuals worldwide in a virtual meeting by utilizing our own primary languages. In contrast to Speech-to-Speech Translation (A2A), which solely translates between audio modalities, the proposed AV2AV directly translates between audio-visual speech. This capability enhances the dialogue experience by presenting synchronized lip movements along with the translated speech. 2) We can improve the robustness of the spoken language translation system. By employing the complementary information of audio-visual speech, the system can effectively translate spoken language even in the presence of acoustic noise, showcasing robust performance. To mitigate the problem of the absence of a parallel AV2AV translation dataset, we propose to train our spoken language translation system with the audio-only dataset of A2A. This is done by learning unified audio-visual speech representations through self-supervised learning in advance to train the translation system. Moreover, we propose an AV-Renderer that can generate raw audio and video in parallel. It is designed with zero-shot speaker modeling, thus the speaker in source audio-visual speech can be maintained at the target translated audio-visual speech. The effectiveness of AV2AV is evaluated with extensive experiments in a many-to-many language translation setting. Demo page is available on https://choijeongsoo.github.io/av2av.

</details>

#### [SyncTalk: The Devil is in the Synchronization for Talking Head Synthesis](https://arxiv.org/abs/2311.17590)
**Ziqiao Peng, Wentao Hu, Yue Shi, Xiangyu Zhu et al.** · 2023-11-29

<details>
<summary>Abstract</summary>

Achieving high synchronization in the synthesis of realistic, speech-driven talking head videos presents a significant challenge. Traditional Generative Adversarial Networks (GAN) struggle to maintain consistent facial identity, while Neural Radiance Fields (NeRF) methods, although they can address this issue, often produce mismatched lip movements, inadequate facial expressions, and unstable head poses. A lifelike talking head requires synchronized coordination of subject identity, lip movements, facial expressions, and head poses. The absence of these synchronizations is a fundamental flaw, leading to unrealistic and artificial outcomes. To address the critical issue of synchronization, identified as the "devil" in creating realistic talking heads, we introduce SyncTalk. This NeRF-based method effectively maintains subject identity, enhancing synchronization and realism in talking head synthesis. SyncTalk employs a Face-Sync Controller to align lip movements with speech and innovatively uses a 3D facial blendshape model to capture accurate facial expressions. Our Head-Sync Stabilizer optimizes head poses, achieving more natural head movements. The Portrait-Sync Generator restores hair details and blends the generated head with the torso for a seamless visual experience. Extensive experiments and user studies demonstrate that SyncTalk outperforms state-of-the-art methods in synchronization and realism. We recommend watching the supplementary video: https://ziqiaopeng.github.io/synctalk

</details>

#### [Talking Head(?) Anime from a Single Image 4: Improved Model and Its Distillation](https://arxiv.org/abs/2311.17409)
**Pramook Khungurn** · 2023-11-29

<details>
<summary>Abstract</summary>

We study the problem of creating a character model that can be controlled in real time from a single image of an anime character. A solution to this problem would greatly reduce the cost of creating avatars, computer games, and other interactive applications. Talking Head Anime 3 (THA3) is an open source project that attempts to directly address the problem. It takes as input (1) an image of an anime character's upper body and (2) a 45-dimensional pose vector and outputs a new image of the same character taking the specified pose. The range of possible movements is expressive enough for personal avatars and certain types of game characters. However, the system is too slow to generate animations in real time on common PCs, and its image quality can be improved. In this paper, we improve THA3 in two ways. First, we propose new architectures for constituent networks that rotate the character's head and body based on U-Nets with attention that are widely used in modern generative models. The new architectures consistently yield better image quality than the THA3 baseline. Nevertheless, they also make the whole system much slower: it takes up to 150 milliseconds to generate a frame. Second, we propose a technique to distill the system into a small network (less than 2 MB) that can generate 512x512 animation frames in real time (under 30 FPS) using consumer gaming GPUs while keeping the image quality close to that of the full system. This improvement makes the whole system practical for real-time applications.

</details>

#### [THInImg: Cross-modal Steganography for Presenting Talking Heads in Images](https://arxiv.org/abs/2311.17177)
**Lin Zhao, Hongxuan Li, Xuefei Ning, Xinru Jiang** · 2023-11-28

<details>
<summary>Abstract</summary>

Cross-modal Steganography is the practice of concealing secret signals in publicly available cover signals (distinct from the modality of the secret signals) unobtrusively. While previous approaches primarily concentrated on concealing a relatively small amount of information, we propose THInImg, which manages to hide lengthy audio data (and subsequently decode talking head video) inside an identity image by leveraging the properties of human face, which can be effectively utilized for covert communication, transmission and copyright protection. THInImg consists of two parts: the encoder and decoder. Inside the encoder-decoder pipeline, we introduce a novel architecture that substantially increase the capacity of hiding audio in images. Moreover, our framework can be extended to iteratively hide multiple audio clips into an identity image, offering multiple levels of control over permissions. We conduct extensive experiments to prove the effectiveness of our method, demonstrating that THInImg can present up to 80 seconds of high quality talking-head video (including audio) in an identity image with 160x160 resolution.

</details>

#### [GAIA: Zero-shot Talking Avatar Generation](https://arxiv.org/abs/2311.15230)
**Tianyu He, Junliang Guo, Runyi Yu, Yuchi Wang et al.** · 2023-11-26

<details>
<summary>Abstract</summary>

Zero-shot talking avatar generation aims at synthesizing natural talking videos from speech and a single portrait image. Previous methods have relied on domain-specific heuristics such as warping-based motion representation and 3D Morphable Models, which limit the naturalness and diversity of the generated avatars. In this work, we introduce GAIA (Generative AI for Avatar), which eliminates the domain priors in talking avatar generation. In light of the observation that the speech only drives the motion of the avatar while the appearance of the avatar and the background typically remain the same throughout the entire video, we divide our approach into two stages: 1) disentangling each frame into motion and appearance representations; 2) generating motion sequences conditioned on the speech and reference portrait image. We collect a large-scale high-quality talking avatar dataset and train the model on it with different scales (up to 2B parameters). Experimental results verify the superiority, scalability, and flexibility of GAIA as 1) the resulting model beats previous baseline models in terms of naturalness, diversity, lip-sync quality, and visual quality; 2) the framework is scalable since larger models yield better results; 3) it is general and enables different applications like controllable talking avatar generation and text-instructed avatar generation.

</details>

#### [CP-EB: Talking Face Generation with Controllable Pose and Eye Blinking Embedding](https://arxiv.org/abs/2311.08673)
**Jianzong Wang, Yimin Deng, Ziqi Liang, Xulong Zhang et al.** · 2023-11-15

<details>
<summary>Abstract</summary>

This paper proposes a talking face generation method named "CP-EB" that takes an audio signal as input and a person image as reference, to synthesize a photo-realistic people talking video with head poses controlled by a short video clip and proper eye blinking embedding. It's noted that not only the head pose but also eye blinking are both important aspects for deep fake detection. The implicit control of poses by video has already achieved by the state-of-art work. According to recent research, eye blinking has weak correlation with input audio which means eye blinks extraction from audio and generation are possible. Hence, we propose a GAN-based architecture to extract eye blink feature from input audio and reference video respectively and employ contrastive training between them, then embed it into the concatenated features of identity and poses to generate talking face images. Experimental results show that the proposed method can generate photo-realistic talking face with synchronous lips motions, natural head poses and blinking eyes.

</details>

#### [Audiovisual Inputs for Learning Robust, Real-time Facial Animation with Lip Sync](https://www.semanticscholar.org/paper/54659fdee52c7a090e51ae4b2db50110e7aeba68)
**Iñaki Navarro, Dario Kneubuehler, Tijmen Verhulsdonck, Eloi Du Bois et al.** · 2023-11-15

<details>
<summary>Abstract</summary>

We present an approach for generating facial animation that combines video and audio input data in real time for low-end devices through deep learning. Our method produces control signals from audiovisual inputs separately, and mixes them to animate a character rig. The architecture relies on two specialized networks that are trained on a combination of synthetic and real world data and are highly engineered to be efficient in order to support quality avatar faces even on low-end devices. In addition, the system supports several levels of detail that degrade gracefully for additional scaling and efficiency. We showcase how user testing has been employed to improve performance and a comparison with state of the art.

</details>

#### [ChatAnything: Facetime Chat with LLM-Enhanced Personas](https://arxiv.org/abs/2311.06772)
**Yilin Zhao, Xinbin Yuan, Shanghua Gao, Zhijie Lin et al.** · 2023-11-12

<details>
<summary>Abstract</summary>

In this technical report, we target generating anthropomorphized personas for LLM-based characters in an online manner, including visual appearance, personality and tones, with only text descriptions. To achieve this, we first leverage the in-context learning capability of LLMs for personality generation by carefully designing a set of system prompts. We then propose two novel concepts: the mixture of voices (MoV) and the mixture of diffusers (MoD) for diverse voice and appearance generation. For MoV, we utilize the text-to-speech (TTS) algorithms with a variety of pre-defined tones and select the most matching one based on the user-provided text description automatically. For MoD, we combine the recent popular text-to-image generation techniques and talking head algorithms to streamline the process of generating talking objects. We termed the whole framework as ChatAnything. With it, users could be able to animate anything with any personas that are anthropomorphic using just a few text inputs. However, we have observed that the anthropomorphic objects produced by current generative models are often undetectable by pre-trained face landmark detectors, leading to failure of the face motion generation, even if these faces possess human-like appearances because those images are nearly seen during the training (e.g., OOD samples). To address this issue, we incorporate pixel-level guidance to infuse human face landmarks during the image generation phase. To benchmark these metrics, we have built an evaluation dataset. Based on it, we verify that the detection rate of the face landmark is significantly increased from 57.0% to 92.5% thus allowing automatic face animation based on generated speech content. The code and more results can be found at https://chatanything.github.io/.

</details>

#### [BakedAvatar: Baking Neural Fields for Real-Time Head Avatar Synthesis](https://arxiv.org/abs/2311.05521)
**Hao-Bin Duan, Miao Wang, Jin-Chuan Shi, Xu-Chuan Chen et al.** · 2023-11-09

<details>
<summary>Abstract</summary>

Synthesizing photorealistic 4D human head avatars from videos is essential for VR/AR, telepresence, and video game applications. Although existing Neural Radiance Fields (NeRF)-based methods achieve high-fidelity results, the computational expense limits their use in real-time applications. To overcome this limitation, we introduce BakedAvatar, a novel representation for real-time neural head avatar synthesis, deployable in a standard polygon rasterization pipeline. Our approach extracts deformable multi-layer meshes from learned isosurfaces of the head and computes expression-, pose-, and view-dependent appearances that can be baked into static textures for efficient rasterization. We thus propose a three-stage pipeline for neural head avatar synthesis, which includes learning continuous deformation, manifold, and radiance fields, extracting layered meshes and textures, and fine-tuning texture details with differential rasterization. Experimental results demonstrate that our representation generates synthesis results of comparable quality to other state-of-the-art methods while significantly reducing the inference time required. We further showcase various head avatar synthesis results from monocular videos, including view synthesis, face reenactment, expression editing, and pose editing, all at interactive frame rates.

</details>

#### [Synthetic Speaking Children -- Why We Need Them and How to Make Them](https://arxiv.org/abs/2311.06307)
**Muhammad Ali Farooq, Dan Bigioi, Rishabh Jain, Wang Yao et al.** · 2023-11-08

<details>
<summary>Abstract</summary>

Contemporary Human Computer Interaction (HCI) research relies primarily on neural network models for machine vision and speech understanding of a system user. Such models require extensively annotated training datasets for optimal performance and when building interfaces for users from a vulnerable population such as young children, GDPR introduces significant complexities in data collection, management, and processing. Motivated by the training needs of an Edge AI smart toy platform this research explores the latest advances in generative neural technologies and provides a working proof of concept of a controllable data generation pipeline for speech driven facial training data at scale. In this context, we demonstrate how StyleGAN2 can be finetuned to create a gender balanced dataset of children's faces. This dataset includes a variety of controllable factors such as facial expressions, age variations, facial poses, and even speech-driven animations with realistic lip synchronization. By combining generative text to speech models for child voice synthesis and a 3D landmark based talking heads pipeline, we can generate highly realistic, entirely synthetic, talking child video clips. These video clips can provide valuable, and controllable, synthetic training data for neural network models, bridging the gap when real data is scarce or restricted due to privacy regulations.

</details>

#### [DiffDub: Person-generic Visual Dubbing Using Inpainting Renderer with Diffusion Auto-encoder](https://arxiv.org/abs/2311.01811)
**Tao Liu, Chenpeng Du, Shuai Fan, Feilong Chen et al.** · 2023-11-03

<details>
<summary>Abstract</summary>

Generating high-quality and person-generic visual dubbing remains a challenge. Recent innovation has seen the advent of a two-stage paradigm, decoupling the rendering and lip synchronization process facilitated by intermediate representation as a conduit. Still, previous methodologies rely on rough landmarks or are confined to a single speaker, thus limiting their performance. In this paper, we propose DiffDub: Diffusion-based dubbing. We first craft the Diffusion auto-encoder by an inpainting renderer incorporating a mask to delineate editable zones and unaltered regions. This allows for seamless filling of the lower-face region while preserving the remaining parts. Throughout our experiments, we encountered several challenges. Primarily, the semantic encoder lacks robustness, constricting its ability to capture high-level features. Besides, the modeling ignored facial positioning, causing mouth or nose jitters across frames. To tackle these issues, we employ versatile strategies, including data augmentation and supplementary eye guidance. Moreover, we encapsulated a conformer-based reference encoder and motion generator fortified by a cross-attention mechanism. This enables our model to learn person-specific textures with varying references and reduces reliance on paired audio-visual data. Our rigorous experiments comprehensively highlight that our ground-breaking approach outpaces existing methods with considerable margins and delivers seamless, intelligible videos in person-generic and multilingual scenarios.

</details>

#### [Seeing Through the Conversation: Audio-Visual Speech Separation based on Diffusion Model](https://arxiv.org/abs/2310.19581)
**Suyeon Lee, Chaeyoung Jung, Youngjoon Jang, Jaehun Kim et al.** · 2023-10-30

<details>
<summary>Abstract</summary>

The objective of this work is to extract target speaker's voice from a mixture of voices using visual cues. Existing works on audio-visual speech separation have demonstrated their performance with promising intelligibility, but maintaining naturalness remains a challenge. To address this issue, we propose AVDiffuSS, an audio-visual speech separation model based on a diffusion mechanism known for its capability in generating natural samples. For an effective fusion of the two modalities for diffusion, we also propose a cross-attention-based feature fusion mechanism. This mechanism is specifically tailored for the speech domain to integrate the phonetic information from audio-visual correspondence in speech generation. In this way, the fusion process maintains the high temporal resolution of the features, without excessive computational requirements. We demonstrate that the proposed framework achieves state-of-the-art results on two benchmarks, including VoxCeleb2 and LRS3, producing speech with notably better naturalness.

</details>

#### [GestSync: Determining who is speaking without a talking head](https://arxiv.org/abs/2310.05304)
**Sindhu B Hegde, Andrew Zisserman** · 2023-10-08

<details>
<summary>Abstract</summary>

In this paper we introduce a new synchronisation task, Gesture-Sync: determining if a person's gestures are correlated with their speech or not. In comparison to Lip-Sync, Gesture-Sync is far more challenging as there is a far looser relationship between the voice and body movement than there is between voice and lip motion. We introduce a dual-encoder model for this task, and compare a number of input representations including RGB frames, keypoint images, and keypoint vectors, assessing their performance and advantages. We show that the model can be trained using self-supervised learning alone, and evaluate its performance on the LRS3 dataset. Finally, we demonstrate applications of Gesture-Sync for audio-visual synchronisation, and in determining who is the speaker in a crowd, without seeing their faces. The code, datasets and pre-trained models can be found at: \url{https://www.robots.ox.ac.uk/~vgg/research/gestsync}.

</details>

#### [DiffPoseTalk: Speech-Driven Stylistic 3D Facial Animation and Head Pose Generation via Diffusion Models](https://arxiv.org/abs/2310.00434)
**Zhiyao Sun, Tian Lv, Sheng Ye, Matthieu Lin et al.** · 2023-09-30

<details>
<summary>Abstract</summary>

The generation of stylistic 3D facial animations driven by speech presents a significant challenge as it requires learning a many-to-many mapping between speech, style, and the corresponding natural facial motion. However, existing methods either employ a deterministic model for speech-to-motion mapping or encode the style using a one-hot encoding scheme. Notably, the one-hot encoding approach fails to capture the complexity of the style and thus limits generalization ability. In this paper, we propose DiffPoseTalk, a generative framework based on the diffusion model combined with a style encoder that extracts style embeddings from short reference videos. During inference, we employ classifier-free guidance to guide the generation process based on the speech and style. In particular, our style includes the generation of head poses, thereby enhancing user perception. Additionally, we address the shortage of scanned 3D talking face data by training our model on reconstructed 3DMM parameters from a high-quality, in-the-wild audio-visual dataset. Extensive experiments and user study demonstrate that our approach outperforms state-of-the-art methods. The code and dataset are at https://diffposetalk.github.io .

</details>

#### [DT-NeRF: Decomposed Triplane-Hash Neural Radiance Fields for High-Fidelity Talking Portrait Synthesis](https://arxiv.org/abs/2309.07752)
**Yaoyu Su, Shaohui Wang, Haoqian Wang** · 2023-09-14

<details>
<summary>Abstract</summary>

In this paper, we present the decomposed triplane-hash neural radiance fields (DT-NeRF), a framework that significantly improves the photorealistic rendering of talking faces and achieves state-of-the-art results on key evaluation datasets. Our architecture decomposes the facial region into two specialized triplanes: one specialized for representing the mouth, and the other for the broader facial features. We introduce audio features as residual terms and integrate them as query vectors into our model through an audio-mouth-face transformer. Additionally, our method leverages the capabilities of Neural Radiance Fields (NeRF) to enrich the volumetric representation of the entire face through additive volumetric rendering techniques. Comprehensive experimental evaluations corroborate the effectiveness and superiority of our proposed approach.

</details>

#### [DiffTalker: Co-driven audio-image diffusion for talking faces via intermediate landmarks](https://arxiv.org/abs/2309.07509)
**Zipeng Qi, Xulong Zhang, Ning Cheng, Jing Xiao et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

Generating realistic talking faces is a complex and widely discussed task with numerous applications. In this paper, we present DiffTalker, a novel model designed to generate lifelike talking faces through audio and landmark co-driving. DiffTalker addresses the challenges associated with directly applying diffusion models to audio control, which are traditionally trained on text-image pairs. DiffTalker consists of two agent networks: a transformer-based landmarks completion network for geometric accuracy and a diffusion-based face generation network for texture details. Landmarks play a pivotal role in establishing a seamless connection between the audio and image domains, facilitating the incorporation of knowledge from pre-trained diffusion models. This innovative approach efficiently produces articulate-speaking faces. Experimental results showcase DiffTalker's superior performance in producing clear and geometrically accurate talking faces, all without the need for additional alignment between audio and image features.

</details>

#### [AV2Wav: Diffusion-Based Re-synthesis from Continuous Self-supervised Features for Audio-Visual Speech Enhancement](https://arxiv.org/abs/2309.08030)
**Ju-Chieh Chou, Chung-Ming Chien, Karen Livescu** · 2023-09-14

<details>
<summary>Abstract</summary>

Speech enhancement systems are typically trained using pairs of clean and noisy speech. In audio-visual speech enhancement (AVSE), there is not as much ground-truth clean data available; most audio-visual datasets are collected in real-world environments with background noise and reverberation, hampering the development of AVSE. In this work, we introduce AV2Wav, a resynthesis-based audio-visual speech enhancement approach that can generate clean speech despite the challenges of real-world training data. We obtain a subset of nearly clean speech from an audio-visual corpus using a neural quality estimator, and then train a diffusion model on this subset to generate waveforms conditioned on continuous speech representations from AV-HuBERT with noise-robust training. We use continuous rather than discrete representations to retain prosody and speaker information. With this vocoding task alone, the model can perform speech enhancement better than a masking-based baseline. We further fine-tune the diffusion model on clean/noisy utterance pairs to improve the performance. Our approach outperforms a masking-based baseline in terms of both automatic metrics and a human listening test and is close in quality to the target speech in the listening test. Audio samples can be found at https://home.ttic.edu/~jcchou/demo/avse/avse_demo.html.

</details>

#### [DF-TransFusion: Multimodal Deepfake Detection via Lip-Audio Cross-Attention and Facial Self-Attention](https://arxiv.org/abs/2309.06511)
**Aaditya Kharel, Manas Paranjape, Aniket Bera** · 2023-09-12

<details>
<summary>Abstract</summary>

With the rise in manipulated media, deepfake detection has become an imperative task for preserving the authenticity of digital content. In this paper, we present a novel multi-modal audio-video framework designed to concurrently process audio and video inputs for deepfake detection tasks. Our model capitalizes on lip synchronization with input audio through a cross-attention mechanism while extracting visual cues via a fine-tuned VGG-16 network. Subsequently, a transformer encoder network is employed to perform facial self-attention. We conduct multiple ablation studies highlighting different strengths of our approach. Our multi-modal methodology outperforms state-of-the-art multi-modal deepfake detection techniques in terms of F-1 and per-video AUC scores.

</details>

#### [Efficient Emotional Adaptation for Audio-Driven Talking-Head Generation](https://arxiv.org/abs/2309.04946)
**Yuan Gan, Zongxin Yang, Xihang Yue, Lingyun Sun et al.** · 2023-09-10

<details>
<summary>Abstract</summary>

Audio-driven talking-head synthesis is a popular research topic for virtual human-related applications. However, the inflexibility and inefficiency of existing methods, which necessitate expensive end-to-end training to transfer emotions from guidance videos to talking-head predictions, are significant limitations. In this work, we propose the Emotional Adaptation for Audio-driven Talking-head (EAT) method, which transforms emotion-agnostic talking-head models into emotion-controllable ones in a cost-effective and efficient manner through parameter-efficient adaptations. Our approach utilizes a pretrained emotion-agnostic talking-head transformer and introduces three lightweight adaptations (the Deep Emotional Prompts, Emotional Deformation Network, and Emotional Adaptation Module) from different perspectives to enable precise and realistic emotion controls. Our experiments demonstrate that our approach achieves state-of-the-art performance on widely-used benchmarks, including LRW and MEAD. Additionally, our parameter-efficient adaptations exhibit remarkable generalization ability, even in scenarios where emotional training videos are scarce or nonexistent. Project website: https://yuangan.github.io/eat/

</details>

#### [From Pixels to Portraits: A Comprehensive Survey of Talking Head Generation Techniques and Applications](https://arxiv.org/abs/2308.16041)
**Shreyank N Gowda, Dheeraj Pandey, Shashank Narayana Gowda** · 2023-08-30

<details>
<summary>Abstract</summary>

Recent advancements in deep learning and computer vision have led to a surge of interest in generating realistic talking heads. This paper presents a comprehensive survey of state-of-the-art methods for talking head generation. We systematically categorises them into four main approaches: image-driven, audio-driven, video-driven and others (including neural radiance fields (NeRF), and 3D-based methods). We provide an in-depth analysis of each method, highlighting their unique contributions, strengths, and limitations. Furthermore, we thoroughly compare publicly available models, evaluating them on key aspects such as inference time and human-rated quality of the generated outputs. Our aim is to provide a clear and concise overview of the current landscape in talking head generation, elucidating the relationships between different approaches and identifying promising directions for future research. This survey will serve as a valuable reference for researchers and practitioners interested in this rapidly evolving field.

</details>

#### [ToonTalker: Cross-Domain Face Reenactment](https://arxiv.org/abs/2308.12866)
**Yuan Gong, Yong Zhang, Xiaodong Cun, Fei Yin et al.** · 2023-08-24

<details>
<summary>Abstract</summary>

We target cross-domain face reenactment in this paper, i.e., driving a cartoon image with the video of a real person and vice versa. Recently, many works have focused on one-shot talking face generation to drive a portrait with a real video, i.e., within-domain reenactment. Straightforwardly applying those methods to cross-domain animation will cause inaccurate expression transfer, blur effects, and even apparent artifacts due to the domain shift between cartoon and real faces. Only a few works attempt to settle cross-domain face reenactment. The most related work AnimeCeleb requires constructing a dataset with pose vector and cartoon image pairs by animating 3D characters, which makes it inapplicable anymore if no paired data is available. In this paper, we propose a novel method for cross-domain reenactment without paired data. Specifically, we propose a transformer-based framework to align the motions from different domains into a common latent space where motion transfer is conducted via latent code addition. Two domain-specific motion encoders and two learnable motion base memories are used to capture domain properties. A source query transformer and a driving one are exploited to project domain-specific motion to the canonical space. The edited motion is projected back to the domain of the source with a transformer. Moreover, since no paired data is provided, we propose a novel cross-domain training scheme using data from two domains with the designed analogy constraint. Besides, we contribute a cartoon dataset in Disney style. Extensive evaluations demonstrate the superiority of our method over competing methods.

</details>

#### [Diff2Lip: Audio Conditioned Diffusion Models for Lip-Synchronization](https://arxiv.org/abs/2308.09716)
**Soumik Mukhopadhyay, Saksham Suri, Ravi Teja Gadde, Abhinav Shrivastava** · 2023-08-18

<details>
<summary>Abstract</summary>

The task of lip synchronization (lip-sync) seeks to match the lips of human faces with different audio. It has various applications in the film industry as well as for creating virtual avatars and for video conferencing. This is a challenging problem as one needs to simultaneously introduce detailed, realistic lip movements while preserving the identity, pose, emotions, and image quality. Many of the previous methods trying to solve this problem suffer from image quality degradation due to a lack of complete contextual information. In this paper, we present Diff2Lip, an audio-conditioned diffusion-based model which is able to do lip synchronization in-the-wild while preserving these qualities. We train our model on Voxceleb2, a video dataset containing in-the-wild talking face videos. Extensive studies show that our method outperforms popular methods like Wav2Lip and PC-AVS in Fréchet inception distance (FID) metric and Mean Opinion Scores (MOS) of the users. We show results on both reconstruction (same audio-video inputs) as well as cross (different audio-video inputs) settings on Voxceleb2 and LRW datasets. Video results and code can be accessed from our project page ( https://soumik-kanad.github.io/diff2lip ).

</details>

#### [A Survey on Deep Multi-modal Learning for Body Language Recognition and Generation](https://arxiv.org/abs/2308.08849)
**Li Liu, Lufei Gao, Wentao Lei, Fengji Ma et al.** · 2023-08-17

<details>
<summary>Abstract</summary>

Body language (BL) refers to the non-verbal communication expressed through physical movements, gestures, facial expressions, and postures. It is a form of communication that conveys information, emotions, attitudes, and intentions without the use of spoken or written words. It plays a crucial role in interpersonal interactions and can complement or even override verbal communication. Deep multi-modal learning techniques have shown promise in understanding and analyzing these diverse aspects of BL. The survey emphasizes their applications to BL generation and recognition. Several common BLs are considered i.e., Sign Language (SL), Cued Speech (CS), Co-speech (CoS), and Talking Head (TH), and we have conducted an analysis and established the connections among these four BL for the first time. Their generation and recognition often involve multi-modal approaches. Benchmark datasets for BL research are well collected and organized, along with the evaluation of SOTA methods on these datasets. The survey highlights challenges such as limited labeled data, multi-modal learning, and the need for domain adaptation to generalize models to unseen speakers or languages. Future research directions are presented, including exploring self-supervised learning techniques, integrating contextual information from other modalities, and exploiting large-scale pre-trained multi-modal models. In summary, this survey paper provides a comprehensive understanding of deep multi-modal learning for various BL generations and recognitions for the first time. By analyzing advancements, challenges, and future directions, it serves as a valuable resource for researchers and practitioners in advancing this field. n addition, we maintain a continuously updated paper list for deep multi-modal learning for BL recognition and generation: https://github.com/wentaoL86/awesome-body-language.

</details>

#### [IIANet: An Intra- and Inter-Modality Attention Network for Audio-Visual Speech Separation](https://arxiv.org/abs/2308.08143)
**Kai Li, Runxuan Yang, Fuchun Sun, Xiaolin Hu** · 2023-08-16

<details>
<summary>Abstract</summary>

Recent research has made significant progress in designing fusion modules for audio-visual speech separation. However, they predominantly focus on multi-modal fusion at a single temporal scale of auditory and visual features without employing selective attention mechanisms, which is in sharp contrast with the brain. To address this issue, We propose a novel model called Intra- and Inter-Attention Network (IIANet), which leverages the attention mechanism for efficient audio-visual feature fusion. IIANet consists of two types of attention blocks: intra-attention (IntraA) and inter-attention (InterA) blocks, where the InterA blocks are distributed at the top, middle and bottom of IIANet. Heavily inspired by the way how human brain selectively focuses on relevant content at various temporal scales, these blocks maintain the ability to learn modality-specific features and enable the extraction of different semantics from audio-visual features. Comprehensive experiments on three standard audio-visual separation benchmarks (LRS2, LRS3, and VoxCeleb2) demonstrate the effectiveness of IIANet, outperforming previous state-of-the-art methods while maintaining comparable inference time. In particular, the fast version of IIANet (IIANet-fast) has only 7% of CTCNet's MACs and is 40% faster than CTCNet on CPUs while achieving better separation quality, showing the great potential of attention mechanism for efficient and effective multimodal fusion.

</details>

#### [Context-Aware Talking-Head Video Editing](https://arxiv.org/abs/2308.00462)
**Songlin Yang, Wei Wang, Jun Ling, Bo Peng et al.** · 2023-08-01

<details>
<summary>Abstract</summary>

Talking-head video editing aims to efficiently insert, delete, and substitute the word of a pre-recorded video through a text transcript editor. The key challenge for this task is obtaining an editing model that generates new talking-head video clips which simultaneously have accurate lip synchronization and motion smoothness. Previous approaches, including 3DMM-based (3D Morphable Model) methods and NeRF-based (Neural Radiance Field) methods, are sub-optimal in that they either require minutes of source videos and days of training time or lack the disentangled control of verbal (e.g., lip motion) and non-verbal (e.g., head pose and expression) representations for video clip insertion. In this work, we fully utilize the video context to design a novel framework for talking-head video editing, which achieves efficiency, disentangled motion control, and sequential smoothness. Specifically, we decompose this framework to motion prediction and motion-conditioned rendering: (1) We first design an animation prediction module that efficiently obtains smooth and lip-sync motion sequences conditioned on the driven speech. This module adopts a non-autoregressive network to obtain context prior and improve the prediction efficiency, and it learns a speech-animation mapping prior with better generalization to novel speech from a multi-identity video dataset. (2) We then introduce a neural rendering module to synthesize the photo-realistic and full-head video frames given the predicted motion sequence. This module adopts a pre-trained head topology and uses only few frames for efficient fine-tuning to obtain a person-specific rendering model. Extensive experiments demonstrate that our method efficiently achieves smoother editing results with higher image quality and lip accuracy using less data than previous methods.

</details>

#### [HyperReenact: One-Shot Reenactment via Jointly Learning to Refine and Retarget Faces](https://arxiv.org/abs/2307.10797)
**Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras et al.** · 2023-07-20

<details>
<summary>Abstract</summary>

In this paper, we present our method for neural face reenactment, called HyperReenact, that aims to generate realistic talking head images of a source identity, driven by a target facial pose. Existing state-of-the-art face reenactment methods train controllable generative models that learn to synthesize realistic facial images, yet producing reenacted faces that are prone to significant visual artifacts, especially under the challenging condition of extreme head pose changes, or requiring expensive few-shot fine-tuning to better preserve the source identity characteristics. We propose to address these limitations by leveraging the photorealistic generation ability and the disentangled properties of a pretrained StyleGAN2 generator, by first inverting the real images into its latent space and then using a hypernetwork to perform: (i) refinement of the source identity characteristics and (ii) facial pose re-targeting, eliminating this way the dependence on external editing methods that typically produce artifacts. Our method operates under the one-shot setting (i.e., using a single source frame) and allows for cross-subject reenactment, without requiring any subject-specific fine-tuning. We compare our method both quantitatively and qualitatively against several state-of-the-art techniques on the standard benchmarks of VoxCeleb1 and VoxCeleb2, demonstrating the superiority of our approach in producing artifact-free images, exhibiting remarkable robustness even under extreme head pose changes. We make the code and the pretrained models publicly available at: https://github.com/StelaBou/HyperReenact .

</details>

#### [FACTS: Facial Animation Creation using the Transfer of Styles](https://arxiv.org/abs/2307.09480)
**Jack Saunders, Steven Caulkin, Vinay Namboodiri** · 2023-07-18

<details>
<summary>Abstract</summary>

The ability to accurately capture and express emotions is a critical aspect of creating believable characters in video games and other forms of entertainment. Traditionally, this animation has been achieved with artistic effort or performance capture, both requiring costs in time and labor. More recently, audio-driven models have seen success, however, these often lack expressiveness in areas not correlated to the audio signal. In this paper, we present a novel approach to facial animation by taking existing animations and allowing for the modification of style characteristics. Specifically, we explore the use of a StarGAN to enable the conversion of 3D facial animations into different emotions and person-specific styles. We are able to maintain the lip-sync of the animations with this method thanks to the use of a novel viseme-preserving loss.

</details>

#### [OPHAvatars: One-shot Photo-realistic Head Avatars](https://arxiv.org/abs/2307.09153)
**Shaoxu Li** · 2023-07-18

<details>
<summary>Abstract</summary>

We propose a method for synthesizing photo-realistic digital avatars from only one portrait as the reference. Given a portrait, our method synthesizes a coarse talking head video using driving keypoints features. And with the coarse video, our method synthesizes a coarse talking head avatar with a deforming neural radiance field. With rendered images of the coarse avatar, our method updates the low-quality images with a blind face restoration model. With updated images, we retrain the avatar for higher quality. After several iterations, our method can synthesize a photo-realistic animatable 3D neural head avatar. The motivation of our method is deformable neural radiance field can eliminate the unnatural distortion caused by the image2video method. Our method outperforms state-of-the-art methods in quantitative and qualitative studies on various subjects.

</details>

#### [On the Vulnerability of DeepFake Detectors to Attacks Generated by Denoising Diffusion Models](https://arxiv.org/abs/2307.05397)
**Marija Ivanovska, Vitomir Štruc** · 2023-07-11

<details>
<summary>Abstract</summary>

The detection of malicious deepfakes is a constantly evolving problem that requires continuous monitoring of detectors to ensure they can detect image manipulations generated by the latest emerging models. In this paper, we investigate the vulnerability of single-image deepfake detectors to black-box attacks created by the newest generation of generative methods, namely Denoising Diffusion Models (DDMs). Our experiments are run on FaceForensics++, a widely used deepfake benchmark consisting of manipulated images generated with various techniques for face identity swapping and face reenactment. Attacks are crafted through guided reconstruction of existing deepfakes with a proposed DDM approach for face restoration. Our findings indicate that employing just a single denoising diffusion step in the reconstruction process of a deepfake can significantly reduce the likelihood of detection, all without introducing any perceptible image modifications. While training detectors using attack examples demonstrated some effectiveness, it was observed that discriminators trained on fully diffusion-based deepfakes exhibited limited generalizability when presented with our attacks.

</details>

#### [A Comprehensive Multi-scale Approach for Speech and Dynamics Synchrony in Talking Head Generation](https://arxiv.org/abs/2307.03270)
**Louis Airale, Dominique Vaufreydaz, Xavier Alameda-Pineda** · 2023-07-04

<details>
<summary>Abstract</summary>

Animating still face images with deep generative models using a speech input signal is an active research topic and has seen important recent progress.However, much of the effort has been put into lip syncing and rendering quality while the generation of natural head motion, let alone the audio-visual correlation between head motion and speech, has often been neglected.In this work, we propose a multi-scale audio-visual synchrony loss and a multi-scale autoregressive GAN to better handle short and long-term correlation between speech and the dynamics of the head and lips.In particular, we train a stack of syncer models on multimodal input pyramids and use these models as guidance in a multi-scale generator network to produce audio-aligned motion unfolding over diverse time scales.Both the pyramid of audio-visual syncers and the generative models are trained in a low-dimensional space that fully preserves dynamics cues.The experiments show significant improvements over the state-of-the-art in head motion dynamics quality and especially in multi-scale audio-visual synchrony on a collection of benchmark datasets.

</details>

#### [RobustL2S: Speaker-Specific Lip-to-Speech Synthesis exploiting Self-Supervised Representations](https://arxiv.org/abs/2307.01233)
**Neha Sahipjohn, Neil Shah, Vishal Tambrahalli, Vineet Gandhi** · 2023-07-03

<details>
<summary>Abstract</summary>

Significant progress has been made in speaker dependent Lip-to-Speech synthesis, which aims to generate speech from silent videos of talking faces. Current state-of-the-art approaches primarily employ non-autoregressive sequence-to-sequence architectures to directly predict mel-spectrograms or audio waveforms from lip representations. We hypothesize that the direct mel-prediction hampers training/model efficiency due to the entanglement of speech content with ambient information and speaker characteristics. To this end, we propose RobustL2S, a modularized framework for Lip-to-Speech synthesis. First, a non-autoregressive sequence-to-sequence model maps self-supervised visual features to a representation of disentangled speech content. A vocoder then converts the speech features into raw waveforms. Extensive evaluations confirm the effectiveness of our setup, achieving state-of-the-art performance on the unconstrained Lip2Wav dataset and the constrained GRID and TCD-TIMIT datasets. Speech samples from RobustL2S can be found at https://neha-sherin.github.io/RobustL2S/

</details>

#### [Instruct-NeuralTalker: Editing Audio-Driven Talking Radiance Fields with Instructions](https://arxiv.org/abs/2306.10813)
**Yuqi Sun, Ruian He, Weimin Tan, Bo Yan** · 2023-06-19

<details>
<summary>Abstract</summary>

Recent neural talking radiance field methods have shown great success in photorealistic audio-driven talking face synthesis. In this paper, we propose a novel interactive framework that utilizes human instructions to edit such implicit neural representations to achieve real-time personalized talking face generation. Given a short speech video, we first build an efficient talking radiance field, and then apply the latest conditional diffusion model for image editing based on the given instructions and guiding implicit representation optimization towards the editing target. To ensure audio-lip synchronization during the editing process, we propose an iterative dataset updating strategy and utilize a lip-edge loss to constrain changes in the lip region. We also introduce a lightweight refinement network for complementing image details and achieving controllable detail generation in the final rendered image. Our method also enables real-time rendering at up to 30FPS on consumer hardware. Multiple metrics and user verification show that our approach provides a significant improvement in rendering quality compared to state-of-the-art methods.

</details>

#### [SelfTalk: A Self-Supervised Commutative Training Diagram to Comprehend 3D Talking Faces](https://arxiv.org/abs/2306.10799)
**Ziqiao Peng, Yihao Luo, Yue Shi, Hao Xu et al.** · 2023-06-19

<details>
<summary>Abstract</summary>

Speech-driven 3D face animation technique, extending its applications to various multimedia fields. Previous research has generated promising realistic lip movements and facial expressions from audio signals. However, traditional regression models solely driven by data face several essential problems, such as difficulties in accessing precise labels and domain gaps between different modalities, leading to unsatisfactory results lacking precision and coherence. To enhance the visual accuracy of generated lip movement while reducing the dependence on labeled data, we propose a novel framework SelfTalk, by involving self-supervision in a cross-modals network system to learn 3D talking faces. The framework constructs a network system consisting of three modules: facial animator, speech recognizer, and lip-reading interpreter. The core of SelfTalk is a commutative training diagram that facilitates compatible features exchange among audio, text, and lip shape, enabling our models to learn the intricate connection between these factors. The proposed framework leverages the knowledge learned from the lip-reading interpreter to generate more plausible lip shapes. Extensive experiments and user studies demonstrate that our proposed approach achieves state-of-the-art performance both qualitatively and quantitatively. We recommend watching the supplementary video.

</details>

#### [Parametric Implicit Face Representation for Audio-Driven Facial Reenactment](https://arxiv.org/abs/2306.07579)
**Ricong Huang, Peiwen Lai, Yipeng Qin, Guanbin Li** · 2023-06-13

<details>
<summary>Abstract</summary>

Audio-driven facial reenactment is a crucial technique that has a range of applications in film-making, virtual avatars and video conferences. Existing works either employ explicit intermediate face representations (e.g., 2D facial landmarks or 3D face models) or implicit ones (e.g., Neural Radiance Fields), thus suffering from the trade-offs between interpretability and expressive power, hence between controllability and quality of the results. In this work, we break these trade-offs with our novel parametric implicit face representation and propose a novel audio-driven facial reenactment framework that is both controllable and can generate high-quality talking heads. Specifically, our parametric implicit representation parameterizes the implicit representation with interpretable parameters of 3D face models, thereby taking the best of both explicit and implicit methods. In addition, we propose several new techniques to improve the three components of our framework, including i) incorporating contextual information into the audio-to-expression parameters encoding; ii) using conditional image synthesis to parameterize the implicit representation and implementing it with an innovative tri-plane structure for efficient learning; iii) formulating facial reenactment as a conditional image inpainting problem and proposing a novel data augmentation technique to improve model generalizability. Extensive experiments demonstrate that our method can generate more realistic results than previous methods with greater fidelity to the identities and talking styles of speakers.

</details>

#### [NPVForensics: Jointing Non-critical Phonemes and Visemes for Deepfake Detection](https://arxiv.org/abs/2306.06885)
**Yu Chen, Yang Yu, Rongrong Ni, Yao Zhao et al.** · 2023-06-12

<details>
<summary>Abstract</summary>

Deepfake technologies empowered by deep learning are rapidly evolving, creating new security concerns for society. Existing multimodal detection methods usually capture audio-visual inconsistencies to expose Deepfake videos. More seriously, the advanced Deepfake technology realizes the audio-visual calibration of the critical phoneme-viseme regions, achieving a more realistic tampering effect, which brings new challenges. To address this problem, we propose a novel Deepfake detection method to mine the correlation between Non-critical Phonemes and Visemes, termed NPVForensics. Firstly, we propose the Local Feature Aggregation block with Swin Transformer (LFA-ST) to construct non-critical phoneme-viseme and corresponding facial feature streams effectively. Secondly, we design a loss function for the fine-grained motion of the talking face to measure the evolutionary consistency of non-critical phoneme-viseme. Next, we design a phoneme-viseme awareness module for cross-modal feature fusion and representation alignment, so that the modality gap can be reduced and the intrinsic complementarity of the two modalities can be better explored. Finally, a self-supervised pre-training strategy is leveraged to thoroughly learn the audio-visual correspondences in natural videos. In this manner, our model can be easily adapted to the downstream Deepfake datasets with fine-tuning. Extensive experiments on existing benchmarks demonstrate that the proposed approach outperforms state-of-the-art methods.

</details>

#### [Ada-TTA: Towards Adaptive High-Quality Text-to-Talking Avatar Synthesis](https://arxiv.org/abs/2306.03504)
**Zhenhui Ye, Ziyue Jiang, Yi Ren, Jinglin Liu et al.** · 2023-06-06

<details>
<summary>Abstract</summary>

We are interested in a novel task, namely low-resource text-to-talking avatar. Given only a few-minute-long talking person video with the audio track as the training data and arbitrary texts as the driving input, we aim to synthesize high-quality talking portrait videos corresponding to the input text. This task has broad application prospects in the digital human industry but has not been technically achieved yet due to two challenges: (1) It is challenging to mimic the timbre from out-of-domain audio for a traditional multi-speaker Text-to-Speech system. (2) It is hard to render high-fidelity and lip-synchronized talking avatars with limited training data. In this paper, we introduce Adaptive Text-to-Talking Avatar (Ada-TTA), which (1) designs a generic zero-shot multi-speaker TTS model that well disentangles the text content, timbre, and prosody; and (2) embraces recent advances in neural rendering to achieve realistic audio-driven talking face video generation. With these designs, our method overcomes the aforementioned two challenges and achieves to generate identity-preserving speech and realistic talking person video. Experiments demonstrate that our method could synthesize realistic, identity-preserving, and audio-visual synchronized talking avatar videos.

</details>

#### [Audio-Driven Talking Head Video Generation with Diffusion Model](https://www.semanticscholar.org/paper/6e6d3daeb11675414391bd935a9e4e84dcff8d47)
**Yizhe Zhu, Chunhui Zhang, Qiong Liu, Xi Zhou** · 2023-06-04

<details>
<summary>Abstract</summary>

Synthesizing high-fidelity talking head videos by fitting input audio sequences is a highly anticipated technique in many applications, such as digital humans, virtual video conferences, and human-computer interaction. Popular GAN-based methods aim to align speech audio with lip motions and head poses. However, existing methods are prone to training instability and even mode collapse, resulting in low-quality video generation. In this paper, we propose a novel audio-driven diffusion method for generating high-resolution realistic videos of talking heads with the help of the denoising diffusion model. Specifically, the face attribute disentanglement module is proposed to disentangle eye blinking and lip motion features, where the lip motion features are synchronized with audio features via the contrastive learning strategy, and the disentangled motion features are aligned well with the talking head. Furthermore, the denoising diffusion model takes the source image and the warped motion features as input to generate the high-resolution realistic talking head with diverse head poses. Extensive evaluations using multiple metrics demonstrate that our method outperforms the current techniques both qualitatively and quantitatively.

</details>

#### [Audio-Visual Speech Separation in Noisy Environments with a Lightweight Iterative Model](https://arxiv.org/abs/2306.00160)
**Héctor Martel, Julius Richter, Kai Li, Xiaolin Hu et al.** · 2023-05-31

<details>
<summary>Abstract</summary>

We propose Audio-Visual Lightweight ITerative model (AVLIT), an effective and lightweight neural network that uses Progressive Learning (PL) to perform audio-visual speech separation in noisy environments. To this end, we adopt the Asynchronous Fully Recurrent Convolutional Neural Network (A-FRCNN), which has shown successful results in audio-only speech separation. Our architecture consists of an audio branch and a video branch, with iterative A-FRCNN blocks sharing weights for each modality. We evaluated our model in a controlled environment using the NTCD-TIMIT dataset and in-the-wild using a synthetic dataset that combines LRS3 and WHAM!. The experiments demonstrate the superiority of our model in both settings with respect to various audio-only and audio-visual baselines. Furthermore, the reduced footprint of our model makes it suitable for low resource applications.

</details>

#### [AV-TranSpeech: Audio-Visual Robust Speech-to-Speech Translation](https://arxiv.org/abs/2305.15403)
**Rongjie Huang, Huadai Liu, Xize Cheng, Yi Ren et al.** · 2023-05-24

<details>
<summary>Abstract</summary>

Direct speech-to-speech translation (S2ST) aims to convert speech from one language into another, and has demonstrated significant progress to date. Despite the recent success, current S2ST models still suffer from distinct degradation in noisy environments and fail to translate visual speech (i.e., the movement of lips and teeth). In this work, we present AV-TranSpeech, the first audio-visual speech-to-speech (AV-S2ST) translation model without relying on intermediate text. AV-TranSpeech complements the audio stream with visual information to promote system robustness and opens up a host of practical applications: dictation or dubbing archival films. To mitigate the data scarcity with limited parallel AV-S2ST data, we 1) explore self-supervised pre-training with unlabeled audio-visual data to learn contextual representation, and 2) introduce cross-modal distillation with S2ST models trained on the audio-only corpus to further reduce the requirements of visual data. Experimental results on two language pairs demonstrate that AV-TranSpeech outperforms audio-only models under all settings regardless of the type of noise. With low-resource audio-visual data (10h, 30h), cross-modal distillation yields an improvement of 7.6 BLEU on average compared with baselines. Audio samples are available at https://AV-TranSpeech.github.io

</details>

#### [CPNet: Exploiting CLIP-based Attention Condenser and Probability Map Guidance for High-fidelity Talking Face Generation](https://arxiv.org/abs/2305.13962)
**Jingning Xu, Benlai Tang, Mingjie Wang, Minghao Li et al.** · 2023-05-23

<details>
<summary>Abstract</summary>

Recently, talking face generation has drawn ever-increasing attention from the research community in computer vision due to its arduous challenges and widespread application scenarios, e.g. movie animation and virtual anchor. Although persevering efforts have been undertaken to enhance the fidelity and lip-sync quality of generated talking face videos, there is still large room for further improvements of synthesis quality and efficiency. Actually, these attempts somewhat ignore the explorations of fine-granularity feature extraction/integration and the consistency between probability distributions of landmarks, thereby recurring the issues of local details blurring and degraded fidelity. To mitigate these dilemmas, in this paper, a novel CLIP-based Attention and Probability Map Guided Network (CPNet) is delicately designed for inferring high-fidelity talking face videos. Specifically, considering the demands of fine-grained feature recalibration, a clip-based attention condenser is exploited to transfer knowledge with rich semantic priors from the prevailing CLIP model. Moreover, to guarantee the consistency in probability space and suppress the landmark ambiguity, we creatively propose the density map of facial landmark as auxiliary supervisory signal to guide the landmark distribution learning of generated frame. Extensive experiments on the widely-used benchmark dataset demonstrate the superiority of our CPNet against state of the arts in terms of image and lip-sync quality. In addition, a cohort of studies are also conducted to ablate the impacts of the individual pivotal components.

</details>

#### [RenderMe-360: A Large Digital Asset Library and Benchmarks Towards High-fidelity Head Avatars](https://arxiv.org/abs/2305.13353)
**Dongwei Pan, Long Zhuo, Jingtan Piao, Huiwen Luo et al.** · 2023-05-22

<details>
<summary>Abstract</summary>

Synthesizing high-fidelity head avatars is a central problem for computer vision and graphics. While head avatar synthesis algorithms have advanced rapidly, the best ones still face great obstacles in real-world scenarios. One of the vital causes is inadequate datasets -- 1) current public datasets can only support researchers to explore high-fidelity head avatars in one or two task directions; 2) these datasets usually contain digital head assets with limited data volume, and narrow distribution over different attributes. In this paper, we present RenderMe-360, a comprehensive 4D human head dataset to drive advance in head avatar research. It contains massive data assets, with 243+ million complete head frames, and over 800k video sequences from 500 different identities captured by synchronized multi-view cameras at 30 FPS. It is a large-scale digital library for head avatars with three key attributes: 1) High Fidelity: all subjects are captured by 60 synchronized, high-resolution 2K cameras in 360 degrees. 2) High Diversity: The collected subjects vary from different ages, eras, ethnicities, and cultures, providing abundant materials with distinctive styles in appearance and geometry. Moreover, each subject is asked to perform various motions, such as expressions and head rotations, which further extend the richness of assets. 3) Rich Annotations: we provide annotations with different granularities: cameras' parameters, matting, scan, 2D/3D facial landmarks, FLAME fitting, and text description. Based on the dataset, we build a comprehensive benchmark for head avatar research, with 16 state-of-the-art methods performed on five main tasks: novel view synthesis, novel expression synthesis, hair rendering, hair editing, and talking head generation. Our experiments uncover the strengths and weaknesses of current methods. RenderMe-360 opens the door for future exploration in head avatars.

</details>

#### [LPMM: Intuitive Pose Control for Neural Talking-Head Model via Landmark-Parameter Morphable Model](https://arxiv.org/abs/2305.10456)
**Kwangho Lee, Patrick Kwon, Myung Ki Lee, Namhyuk Ahn et al.** · 2023-05-17

<details>
<summary>Abstract</summary>

While current talking head models are capable of generating photorealistic talking head videos, they provide limited pose controllability. Most methods require specific video sequences that should exactly contain the head pose desired, being far from user-friendly pose control. Three-dimensional morphable models (3DMM) offer semantic pose control, but they fail to capture certain expressions. We present a novel method that utilizes parametric control of head orientation and facial expression over a pre-trained neural-talking head model. To enable this, we introduce a landmark-parameter morphable model (LPMM), which offers control over the facial landmark domain through a set of semantic parameters. Using LPMM, it is possible to adjust specific head pose factors, without distorting other facial attributes. The results show our approach provides intuitive rig-like control over neural talking head models, allowing both parameter and image-based inputs.

</details>

#### [Identity-Preserving Talking Face Generation with Landmark and Appearance Priors](https://arxiv.org/abs/2305.08293)
**Weizhi Zhong, Chaowei Fang, Yinqi Cai, Pengxu Wei et al.** · 2023-05-15

<details>
<summary>Abstract</summary>

Generating talking face videos from audio attracts lots of research interest. A few person-specific methods can generate vivid videos but require the target speaker's videos for training or fine-tuning. Existing person-generic methods have difficulty in generating realistic and lip-synced videos while preserving identity information. To tackle this problem, we propose a two-stage framework consisting of audio-to-landmark generation and landmark-to-video rendering procedures. First, we devise a novel Transformer-based landmark generator to infer lip and jaw landmarks from the audio. Prior landmark characteristics of the speaker's face are employed to make the generated landmarks coincide with the facial outline of the speaker. Then, a video rendering model is built to translate the generated landmarks into face images. During this stage, prior appearance information is extracted from the lower-half occluded target face and static reference images, which helps generate realistic and identity-preserving visual content. For effectively exploring the prior information of static reference images, we align static reference images with the target face's pose and expression based on motion fields. Moreover, auditory features are reused to guarantee that the generated face images are well synchronized with the audio. Extensive experiments demonstrate that our method can produce more realistic, lip-synced, and identity-preserving videos than existing person-generic talking face generation methods.

</details>

#### [DaGAN++: Depth-Aware Generative Adversarial Network for Talking Head Video Generation](https://arxiv.org/abs/2305.06225)
**Fa-Ting Hong, Li Shen, Dan Xu** · 2023-05-10

<details>
<summary>Abstract</summary>

Predominant techniques on talking head generation largely depend on 2D information, including facial appearances and motions from input face images. Nevertheless, dense 3D facial geometry, such as pixel-wise depth, plays a critical role in constructing accurate 3D facial structures and suppressing complex background noises for generation. However, dense 3D annotations for facial videos is prohibitively costly to obtain. In this work, firstly, we present a novel self-supervised method for learning dense 3D facial geometry (ie, depth) from face videos, without requiring camera parameters and 3D geometry annotations in training. We further propose a strategy to learn pixel-level uncertainties to perceive more reliable rigid-motion pixels for geometry learning. Secondly, we design an effective geometry-guided facial keypoint estimation module, providing accurate keypoints for generating motion fields. Lastly, we develop a 3D-aware cross-modal (ie, appearance and depth) attention mechanism, which can be applied to each generation layer, to capture facial geometries in a coarse-to-fine manner. Extensive experiments are conducted on three challenging benchmarks (ie, VoxCeleb1, VoxCeleb2, and HDTF). The results demonstrate that our proposed framework can generate highly realistic-looking reenacted talking videos, with new state-of-the-art performances established on these benchmarks. The codes and trained models are publicly available on the GitHub project page at https://github.com/harlanhong/CVPR2022-DaGAN

</details>

#### [A multimodal dynamical variational autoencoder for audiovisual speech representation learning](https://arxiv.org/abs/2305.03582)
**Samir Sadok, Simon Leglaive, Laurent Girin, Xavier Alameda-Pineda et al.** · 2023-05-05

<details>
<summary>Abstract</summary>

In this paper, we present a multimodal and dynamical VAE (MDVAE) applied to unsupervised audio-visual speech representation learning. The latent space is structured to dissociate the latent dynamical factors that are shared between the modalities from those that are specific to each modality. A static latent variable is also introduced to encode the information that is constant over time within an audiovisual speech sequence. The model is trained in an unsupervised manner on an audiovisual emotional speech dataset, in two stages. In the first stage, a vector quantized VAE (VQ-VAE) is learned independently for each modality, without temporal modeling. The second stage consists in learning the MDVAE model on the intermediate representation of the VQ-VAEs before quantization. The disentanglement between static versus dynamical and modality-specific versus modality-common information occurs during this second training stage. Extensive experiments are conducted to investigate how audiovisual speech latent factors are encoded in the latent space of MDVAE. These experiments include manipulating audiovisual speech, audiovisual facial image denoising, and audiovisual speech emotion recognition. The results show that MDVAE effectively combines the audio and visual information in its latent space. They also show that the learned static representation of audiovisual speech can be used for emotion recognition with few labeled data, and with better accuracy compared with unimodal baselines and a state-of-the-art supervised model based on an audiovisual transformer architecture.

</details>

#### [Multimodal-driven Talking Face Generation via a Unified Diffusion-based Generator](https://arxiv.org/abs/2305.02594)
**Chao Xu, Shaoting Zhu, Junwei Zhu, Tianxin Huang et al.** · 2023-05-04

<details>
<summary>Abstract</summary>

Multimodal-driven talking face generation refers to animating a portrait with the given pose, expression, and gaze transferred from the driving image and video, or estimated from the text and audio. However, existing methods ignore the potential of text modal, and their generators mainly follow the source-oriented feature rearrange paradigm coupled with unstable GAN frameworks. In this work, we first represent the emotion in the text prompt, which could inherit rich semantics from the CLIP, allowing flexible and generalized emotion control. We further reorganize these tasks as the target-oriented texture transfer and adopt the Diffusion Models. More specifically, given a textured face as the source and the rendered face projected from the desired 3DMM coefficients as the target, our proposed Texture-Geometry-aware Diffusion Model decomposes the complex transfer problem into multi-conditional denoising process, where a Texture Attention-based module accurately models the correspondences between appearance and geometry cues contained in source and target conditions, and incorporate extra implicit information for high-fidelity talking face generation. Additionally, TGDM can be gracefully tailored for face swapping. We derive a novel paradigm free of unstable seesaw-style optimization, resulting in simple, stable, and effective training and inference schemes. Extensive experiments demonstrate the superiority of our method.

</details>

#### [GeneFace++: Generalized and Stable Real-Time Audio-Driven 3D Talking Face Generation](https://arxiv.org/abs/2305.00787)
**Zhenhui Ye, Jinzheng He, Ziyue Jiang, Rongjie Huang et al.** · 2023-05-01

<details>
<summary>Abstract</summary>

Generating talking person portraits with arbitrary speech audio is a crucial problem in the field of digital human and metaverse. A modern talking face generation method is expected to achieve the goals of generalized audio-lip synchronization, good video quality, and high system efficiency. Recently, neural radiance field (NeRF) has become a popular rendering technique in this field since it could achieve high-fidelity and 3D-consistent talking face generation with a few-minute-long training video. However, there still exist several challenges for NeRF-based methods: 1) as for the lip synchronization, it is hard to generate a long facial motion sequence of high temporal consistency and audio-lip accuracy; 2) as for the video quality, due to the limited data used to train the renderer, it is vulnerable to out-of-domain input condition and produce bad rendering results occasionally; 3) as for the system efficiency, the slow training and inference speed of the vanilla NeRF severely obstruct its usage in real-world applications. In this paper, we propose GeneFace++ to handle these challenges by 1) utilizing the pitch contour as an auxiliary feature and introducing a temporal loss in the facial motion prediction process; 2) proposing a landmark locally linear embedding method to regulate the outliers in the predicted motion sequence to avoid robustness issues; 3) designing a computationally efficient NeRF-based motion-to-video renderer to achieves fast training and real-time inference. With these settings, GeneFace++ becomes the first NeRF-based method that achieves stable and real-time talking face generation with generalized audio-lip synchronization. Extensive experiments show that our method outperforms state-of-the-art baselines in terms of subjective and objective evaluation. Video samples are available at https://genefaceplusplus.github.io .

</details>

#### [StyleAvatar: Real-time Photo-realistic Portrait Avatar from a Single Video](https://arxiv.org/abs/2305.00942)
**Lizhen Wang, Xiaochen Zhao, Jingxiang Sun, Yuxiang Zhang et al.** · 2023-05-01

<details>
<summary>Abstract</summary>

Face reenactment methods attempt to restore and re-animate portrait videos as realistically as possible. Existing methods face a dilemma in quality versus controllability: 2D GAN-based methods achieve higher image quality but suffer in fine-grained control of facial attributes compared with 3D counterparts. In this work, we propose StyleAvatar, a real-time photo-realistic portrait avatar reconstruction method using StyleGAN-based networks, which can generate high-fidelity portrait avatars with faithful expression control. We expand the capabilities of StyleGAN by introducing a compositional representation and a sliding window augmentation method, which enable faster convergence and improve translation generalization. Specifically, we divide the portrait scenes into three parts for adaptive adjustments: facial region, non-facial foreground region, and the background. Besides, our network leverages the best of UNet, StyleGAN and time coding for video learning, which enables high-quality video generation. Furthermore, a sliding window augmentation method together with a pre-training strategy are proposed to improve translation generalization and training performance, respectively. The proposed network can converge within two hours while ensuring high image quality and a forward rendering time of only 20 milliseconds. Furthermore, we propose a real-time live system, which further pushes research into applications. Results and experiments demonstrate the superiority of our method in terms of image quality, full portrait video generation, and real-time re-animation compared to existing facial reenactment methods. Training and inference code for this paper are at https://github.com/LizhenWangT/StyleAvatar.

</details>

#### [StyleLipSync: Style-based Personalized Lip-sync Video Generation](https://arxiv.org/abs/2305.00521)
**Taekyung Ki, Dongchan Min** · 2023-04-30

<details>
<summary>Abstract</summary>

In this paper, we present StyleLipSync, a style-based personalized lip-sync video generative model that can generate identity-agnostic lip-synchronizing video from arbitrary audio. To generate a video of arbitrary identities, we leverage expressive lip prior from the semantically rich latent space of a pre-trained StyleGAN, where we can also design a video consistency with a linear transformation. In contrast to the previous lip-sync methods, we introduce pose-aware masking that dynamically locates the mask to improve the naturalness over frames by utilizing a 3D parametric mesh predictor frame by frame. Moreover, we propose a few-shot lip-sync adaptation method for an arbitrary person by introducing a sync regularizer that preserves lip-sync generalization while enhancing the person-specific visual information. Extensive experiments demonstrate that our model can generate accurate lip-sync videos even with the zero-shot setting and enhance characteristics of an unseen face using a few seconds of target video through the proposed adaptation method.

</details>

#### [High-Fidelity and Freely Controllable Talking Head Video Generation](https://arxiv.org/abs/2304.10168)
**Yue Gao, Yuan Zhou, Jinglu Wang, Xiao Li et al.** · 2023-04-20

<details>
<summary>Abstract</summary>

Talking head generation is to generate video based on a given source identity and target motion. However, current methods face several challenges that limit the quality and controllability of the generated videos. First, the generated face often has unexpected deformation and severe distortions. Second, the driving image does not explicitly disentangle movement-relevant information, such as poses and expressions, which restricts the manipulation of different attributes during generation. Third, the generated videos tend to have flickering artifacts due to the inconsistency of the extracted landmarks between adjacent frames. In this paper, we propose a novel model that produces high-fidelity talking head videos with free control over head pose and expression. Our method leverages both self-supervised learned landmarks and 3D face model-based landmarks to model the motion. We also introduce a novel motion-aware multi-scale feature alignment module to effectively transfer the motion without face distortion. Furthermore, we enhance the smoothness of the synthesized talking head videos with a feature context adaptation and propagation module. We evaluate our model on challenging datasets and demonstrate its state-of-the-art performance.

</details>

#### [Audio-Driven Talking Face Generation with Diverse yet Realistic Facial Animations](https://arxiv.org/abs/2304.08945)
**Rongliang Wu, Yingchen Yu, Fangneng Zhan, Jiahui Zhang et al.** · 2023-04-18

<details>
<summary>Abstract</summary>

Audio-driven talking face generation, which aims to synthesize talking faces with realistic facial animations (including accurate lip movements, vivid facial expression details and natural head poses) corresponding to the audio, has achieved rapid progress in recent years. However, most existing work focuses on generating lip movements only without handling the closely correlated facial expressions, which degrades the realism of the generated faces greatly. This paper presents DIRFA, a novel method that can generate talking faces with diverse yet realistic facial animations from the same driving audio. To accommodate fair variation of plausible facial animations for the same audio, we design a transformer-based probabilistic mapping network that can model the variational facial animation distribution conditioned upon the input audio and autoregressively convert the audio signals into a facial animation sequence. In addition, we introduce a temporally-biased mask into the mapping network, which allows to model the temporal dependency of facial animations and produce temporally smooth facial animation sequence. With the generated facial animation sequence and a source image, photo-realistic talking faces can be synthesized with a generic generation network. Extensive experiments show that DIRFA can generate talking faces with realistic facial animations effectively.

</details>

#### [One-Shot High-Fidelity Talking-Head Synthesis with Deformable Neural Radiance Field](https://arxiv.org/abs/2304.05097)
**Weichuang Li, Longhao Zhang, Dong Wang, Bin Zhao et al.** · 2023-04-11

<details>
<summary>Abstract</summary>

Talking head generation aims to generate faces that maintain the identity information of the source image and imitate the motion of the driving image. Most pioneering methods rely primarily on 2D representations and thus will inevitably suffer from face distortion when large head rotations are encountered. Recent works instead employ explicit 3D structural representations or implicit neural rendering to improve performance under large pose changes. Nevertheless, the fidelity of identity and expression is not so desirable, especially for novel-view synthesis. In this paper, we propose HiDe-NeRF, which achieves high-fidelity and free-view talking-head synthesis. Drawing on the recently proposed Deformable Neural Radiance Fields, HiDe-NeRF represents the 3D dynamic scene into a canonical appearance field and an implicit deformation field, where the former comprises the canonical source face and the latter models the driving pose and expression. In particular, we improve fidelity from two aspects: (i) to enhance identity expressiveness, we design a generalized appearance module that leverages multi-scale volume features to preserve face shape and details; (ii) to improve expression preciseness, we propose a lightweight deformation module that explicitly decouples the pose and expression to enable precise expression modeling. Extensive experiments demonstrate that our proposed approach can generate better results than previous works. Project page: https://www.waytron.net/hidenerf/

</details>

#### [That's What I Said: Fully-Controllable Talking Face Generation](https://arxiv.org/abs/2304.03275)
**Youngjoon Jang, Kyeongha Rho, Jong-Bin Woo, Hyeongkeun Lee et al.** · 2023-04-06

<details>
<summary>Abstract</summary>

The goal of this paper is to synthesise talking faces with controllable facial motions. To achieve this goal, we propose two key ideas. The first is to establish a canonical space where every face has the same motion patterns but different identities. The second is to navigate a multimodal motion space that only represents motion-related features while eliminating identity information. To disentangle identity and motion, we introduce an orthogonality constraint between the two different latent spaces. From this, our method can generate natural-looking talking faces with fully controllable facial attributes and accurate lip synchronisation. Extensive experiments demonstrate that our method achieves state-of-the-art results in terms of both visual quality and lip-sync score. To the best of our knowledge, we are the first to develop a talking face generation framework that can accurately manifest full target facial motions including lip, head pose, and eye movements in the generated video without any additional supervision beyond RGB video with audio.

</details>

#### [DAE-Talker: High Fidelity Speech-Driven Talking Face Generation with Diffusion Autoencoder](https://arxiv.org/abs/2303.17550)
**Chenpeng Du, Qi Chen, Tianyu He, Xu Tan et al.** · 2023-03-30

<details>
<summary>Abstract</summary>

While recent research has made significant progress in speech-driven talking face generation, the quality of the generated video still lags behind that of real recordings. One reason for this is the use of handcrafted intermediate representations like facial landmarks and 3DMM coefficients, which are designed based on human knowledge and are insufficient to precisely describe facial movements. Additionally, these methods require an external pretrained model for extracting these representations, whose performance sets an upper bound on talking face generation. To address these limitations, we propose a novel method called DAE-Talker that leverages data-driven latent representations obtained from a diffusion autoencoder (DAE). DAE contains an image encoder that encodes an image into a latent vector and a DDIM image decoder that reconstructs the image from it. We train our DAE on talking face video frames and then extract their latent representations as the training target for a Conformer-based speech2latent model. This allows DAE-Talker to synthesize full video frames and produce natural head movements that align with the content of speech, rather than relying on a predetermined head pose from a template video. We also introduce pose modelling in speech2latent for pose controllability. Additionally, we propose a novel method for generating continuous video frames with the DDIM image decoder trained on individual frames, eliminating the need for modelling the joint distribution of consecutive frames directly. Our experiments show that DAE-Talker outperforms existing popular methods in lip-sync, video fidelity, and pose naturalness. We also conduct ablation studies to analyze the effectiveness of the proposed techniques and demonstrate the pose controllability of DAE-Talker.

</details>

#### [Seeing What You Said: Talking Face Generation Guided by a Lip Reading Expert](https://arxiv.org/abs/2303.17480)
**Jiadong Wang, Xinyuan Qian, Malu Zhang, Robby T. Tan et al.** · 2023-03-29

<details>
<summary>Abstract</summary>

Talking face generation, also known as speech-to-lip generation, reconstructs facial motions concerning lips given coherent speech input. The previous studies revealed the importance of lip-speech synchronization and visual quality. Despite much progress, they hardly focus on the content of lip movements i.e., the visual intelligibility of the spoken words, which is an important aspect of generation quality. To address the problem, we propose using a lip-reading expert to improve the intelligibility of the generated lip regions by penalizing the incorrect generation results. Moreover, to compensate for data scarcity, we train the lip-reading expert in an audio-visual self-supervised manner. With a lip-reading expert, we propose a novel contrastive learning to enhance lip-speech synchronization, and a transformer to encode audio synchronically with video, while considering global temporal dependency of audio. For evaluation, we propose a new strategy with two different lip-reading experts to measure intelligibility of the generated videos. Rigorous experiments show that our proposal is superior to other State-of-the-art (SOTA) methods, such as Wav2Lip, in reading intelligibility i.e., over 38% Word Error Rate (WER) on LRS2 dataset and 27.8% accuracy on LRW dataset. We also achieve the SOTA performance in lip-speech synchronization and comparable performances in visual quality.

</details>

#### [OTAvatar: One-shot Talking Face Avatar with Controllable Tri-plane Rendering](https://arxiv.org/abs/2303.14662)
**Zhiyuan Ma, Xiangyu Zhu, Guojun Qi, Zhen Lei et al.** · 2023-03-26

<details>
<summary>Abstract</summary>

Controllability, generalizability and efficiency are the major objectives of constructing face avatars represented by neural implicit field. However, existing methods have not managed to accommodate the three requirements simultaneously. They either focus on static portraits, restricting the representation ability to a specific subject, or suffer from substantial computational cost, limiting their flexibility. In this paper, we propose One-shot Talking face Avatar (OTAvatar), which constructs face avatars by a generalized controllable tri-plane rendering solution so that each personalized avatar can be constructed from only one portrait as the reference. Specifically, OTAvatar first inverts a portrait image to a motion-free identity code. Second, the identity code and a motion code are utilized to modulate an efficient CNN to generate a tri-plane formulated volume, which encodes the subject in the desired motion. Finally, volume rendering is employed to generate an image in any view. The core of our solution is a novel decoupling-by-inverting strategy that disentangles identity and motion in the latent code via optimization-based inversion. Benefiting from the efficient tri-plane representation, we achieve controllable rendering of generalized face avatar at $35$ FPS on A100. Experiments show promising performance of cross-identity reenactment on subjects out of the training set and better 3D consistency.

</details>

#### [EmoTalk: Speech-Driven Emotional Disentanglement for 3D Face Animation](https://arxiv.org/abs/2303.11089)
**Ziqiao Peng, Haoyu Wu, Zhenbo Song, Hao Xu et al.** · 2023-03-20

<details>
<summary>Abstract</summary>

Speech-driven 3D face animation aims to generate realistic facial expressions that match the speech content and emotion. However, existing methods often neglect emotional facial expressions or fail to disentangle them from speech content. To address this issue, this paper proposes an end-to-end neural network to disentangle different emotions in speech so as to generate rich 3D facial expressions. Specifically, we introduce the emotion disentangling encoder (EDE) to disentangle the emotion and content in the speech by cross-reconstructed speech signals with different emotion labels. Then an emotion-guided feature fusion decoder is employed to generate a 3D talking face with enhanced emotion. The decoder is driven by the disentangled identity, emotional, and content embeddings so as to generate controllable personal and emotional styles. Finally, considering the scarcity of the 3D emotional talking face data, we resort to the supervision of facial blendshapes, which enables the reconstruction of plausible 3D faces from 2D emotional data, and contribute a large-scale 3D emotional talking face dataset (3D-ETF) to train the network. Our experiments and user studies demonstrate that our approach outperforms state-of-the-art methods and exhibits more diverse facial movements. We recommend watching the supplementary video: https://ziqiaopeng.github.io/emotalk

</details>

#### [DisCoHead: Audio-and-Video-Driven Talking Head Generation by Disentangled Control of Head Pose and Facial Expressions](https://arxiv.org/abs/2303.07697)
**Geumbyeol Hwang, Sunwon Hong, Seunghyun Lee, Sungwoo Park et al.** · 2023-03-14

<details>
<summary>Abstract</summary>

For realistic talking head generation, creating natural head motion while maintaining accurate lip synchronization is essential. To fulfill this challenging task, we propose DisCoHead, a novel method to disentangle and control head pose and facial expressions without supervision. DisCoHead uses a single geometric transformation as a bottleneck to isolate and extract head motion from a head-driving video. Either an affine or a thin-plate spline transformation can be used and both work well as geometric bottlenecks. We enhance the efficiency of DisCoHead by integrating a dense motion estimator and the encoder of a generator which are originally separate modules. Taking a step further, we also propose a neural mix approach where dense motion is estimated and applied implicitly by the encoder. After applying the disentangled head motion to a source identity, DisCoHead controls the mouth region according to speech audio, and it blinks eyes and moves eyebrows following a separate driving video of the eye region, via the weight modulation of convolutional neural networks. The experiments using multiple datasets show that DisCoHead successfully generates realistic audio-and-video-driven talking heads and outperforms state-of-the-art methods. Project page: https://deepbrainai-research.github.io/discohead/

</details>

#### [Learning Cross-lingual Visual Speech Representations](https://arxiv.org/abs/2303.09455)
**Andreas Zinonos, Alexandros Haliassos, Pingchuan Ma, Stavros Petridis et al.** · 2023-03-14

<details>
<summary>Abstract</summary>

Cross-lingual self-supervised learning has been a growing research topic in the last few years. However, current works only explored the use of audio signals to create representations. In this work, we study cross-lingual self-supervised visual representation learning. We use the recently-proposed Raw Audio-Visual Speech Encoders (RAVEn) framework to pre-train an audio-visual model with unlabelled multilingual data, and then fine-tune the visual model on labelled transcriptions. Our experiments show that: (1) multi-lingual models with more data outperform monolingual ones, but, when keeping the amount of data fixed, monolingual models tend to reach better performance; (2) multi-lingual outperforms English-only pre-training; (3) using languages which are more similar yields better results; and (4) fine-tuning on unseen languages is competitive to using the target language in the pre-training set. We hope our study inspires future research on non-English-only speech representation learning.

</details>

#### [Memory-augmented Contrastive Learning for Talking Head Generation](https://arxiv.org/abs/2302.13469)
**Jianrong Wang, Yaxin Zhao, Li Liu, Hongkai Fan et al.** · 2023-02-27

<details>
<summary>Abstract</summary>

Given one reference facial image and a piece of speech as input, talking head generation aims to synthesize a realistic-looking talking head video. However, generating a lip-synchronized video with natural head movements is challenging. The same speech clip can generate multiple possible lip and head movements, that is, there is no one-to-one mapping relationship between them. To overcome this problem, we propose a Speech Feature Extractor (SFE) based on memory-augmented self-supervised contrastive learning, which introduces the memory module to store multiple different speech mapping results. In addition, we introduce the Mixed Density Networks (MDN) into the landmark regression task to generate multiple predicted facial landmarks. Extensive qualitative and quantitative experiments show that the quality of our facial animation is significantly superior to that of the state-of-the-art (SOTA). The code has been released at https://github.com/Yaxinzhao97/MACL.git.

</details>

#### [Pose-Controllable 3D Facial Animation Synthesis using Hierarchical Audio-Vertex Attention](https://arxiv.org/abs/2302.12532)
**Bin Liu, Xiaolin Wei, Bo Li, Junjie Cao et al.** · 2023-02-24

<details>
<summary>Abstract</summary>

Most of the existing audio-driven 3D facial animation methods suffered from the lack of detailed facial expression and head pose, resulting in unsatisfactory experience of human-robot interaction. In this paper, a novel pose-controllable 3D facial animation synthesis method is proposed by utilizing hierarchical audio-vertex attention. To synthesize real and detailed expression, a hierarchical decomposition strategy is proposed to encode the audio signal into both a global latent feature and a local vertex-wise control feature. Then the local and global audio features combined with vertex spatial features are used to predict the final consistent facial animation via a graph convolutional neural network by fusing the intrinsic spatial topology structure of the face model and the corresponding semantic feature of the audio. To accomplish pose-controllable animation, we introduce a novel pose attribute augmentation method by utilizing the 2D talking face technique. Experimental results indicate that the proposed method can produce more realistic facial expressions and head posture movements. Qualitative and quantitative experiments show that the proposed method achieves competitive performance against state-of-the-art methods.

</details>

#### [Deep Learning Technique to generate lip-sync for live 2-D Animation](https://www.semanticscholar.org/paper/7f61d57df02bfeb59057f49944b79b14c1e0aea0)
**Ashish Soni, Janhvi Deshmukh, Ayush Shende, R. Gawande et al.** · 2023-02-18

<details>
<summary>Abstract</summary>

Currently, there are a couple of major trends in live 2-D animation like Immersive User Experience, Next-Gen Software, Mobile 2D Animation, VR 2D Animation, AR/VR Live Action Animation, and Web 2D Animation that are getting a lot of attention. For the industries like advertisement, entertainment as well as education, this new technology has become very important as each of them needs to reach their target audience through it. With the help of live 2-D animation, these industries can now reach out to new audiences through something that has never been done before, creating original content that is something that has never been done before. This has now become possible due to the rise of social media. With the advent of social media, it is now possible for anyone in the world to communicate with people who have never been contacted by any advertising or marketing agency before. The solution we are proposing is a deep learning technique for creating animated characters that can make lips synchronized just the way humans do without any assistance and intervention. This can save many working hours that are needed to make an animated character feel real while dialog delivery. The main requirement here is the exact lip sync as that of the human performs while talking the lip movement should get exactly matched. This is possible with the help of LSTM model [5].

</details>

#### [GeneFace: Generalized and High-Fidelity Audio-Driven 3D Talking Face Synthesis](https://arxiv.org/abs/2301.13430)
**Zhenhui Ye, Ziyue Jiang, Yi Ren, Jinglin Liu et al.** · 2023-01-31

<details>
<summary>Abstract</summary>

Generating photo-realistic video portrait with arbitrary speech audio is a crucial problem in film-making and virtual reality. Recently, several works explore the usage of neural radiance field in this task to improve 3D realness and image fidelity. However, the generalizability of previous NeRF-based methods to out-of-domain audio is limited by the small scale of training data. In this work, we propose GeneFace, a generalized and high-fidelity NeRF-based talking face generation method, which can generate natural results corresponding to various out-of-domain audio. Specifically, we learn a variaitional motion generator on a large lip-reading corpus, and introduce a domain adaptative post-net to calibrate the result. Moreover, we learn a NeRF-based renderer conditioned on the predicted facial motion. A head-aware torso-NeRF is proposed to eliminate the head-torso separation problem. Extensive experiments show that our method achieves more generalized and high-fidelity talking face generation compared to previous methods.

</details>

#### [DPE: Disentanglement of Pose and Expression for General Video Portrait Editing](https://arxiv.org/abs/2301.06281)
**Youxin Pang, Yong Zhang, Weize Quan, Yanbo Fan et al.** · 2023-01-16

<details>
<summary>Abstract</summary>

One-shot video-driven talking face generation aims at producing a synthetic talking video by transferring the facial motion from a video to an arbitrary portrait image. Head pose and facial expression are always entangled in facial motion and transferred simultaneously. However, the entanglement sets up a barrier for these methods to be used in video portrait editing directly, where it may require to modify the expression only while maintaining the pose unchanged. One challenge of decoupling pose and expression is the lack of paired data, such as the same pose but different expressions. Only a few methods attempt to tackle this challenge with the feat of 3D Morphable Models (3DMMs) for explicit disentanglement. But 3DMMs are not accurate enough to capture facial details due to the limited number of Blenshapes, which has side effects on motion transfer. In this paper, we introduce a novel self-supervised disentanglement framework to decouple pose and expression without 3DMMs and paired data, which consists of a motion editing module, a pose generator, and an expression generator. The editing module projects faces into a latent space where pose motion and expression motion can be disentangled, and the pose or expression transfer can be performed in the latent space conveniently via addition. The two generators render the modified latent codes to images, respectively. Moreover, to guarantee the disentanglement, we propose a bidirectional cyclic training strategy with well-designed constraints. Evaluations demonstrate our method can control pose or expression independently and be used for general video editing.

</details>

#### [DiffTalk: Crafting Diffusion Models for Generalized Audio-Driven Portraits Animation](https://arxiv.org/abs/2301.03786)
**Shuai Shen, Wenliang Zhao, Zibin Meng, Wanhua Li et al.** · 2023-01-10

<details>
<summary>Abstract</summary>

Talking head synthesis is a promising approach for the video production industry. Recently, a lot of effort has been devoted in this research area to improve the generation quality or enhance the model generalization. However, there are few works able to address both issues simultaneously, which is essential for practical applications. To this end, in this paper, we turn attention to the emerging powerful Latent Diffusion Models, and model the Talking head generation as an audio-driven temporally coherent denoising process (DiffTalk). More specifically, instead of employing audio signals as the single driving factor, we investigate the control mechanism of the talking face, and incorporate reference face images and landmarks as conditions for personality-aware generalized synthesis. In this way, the proposed DiffTalk is capable of producing high-quality talking head videos in synchronization with the source audio, and more importantly, it can be naturally generalized across different identities without any further fine-tuning. Additionally, our DiffTalk can be gracefully tailored for higher-resolution synthesis with negligible extra computational cost. Extensive experiments show that the proposed DiffTalk efficiently synthesizes high-fidelity audio-driven talking head videos for generalized novel identities. For more video results, please refer to \url{https://sstzal.github.io/DiffTalk/}.

</details>

#### [Diffused Heads: Diffusion Models Beat GANs on Talking-Face Generation](https://arxiv.org/abs/2301.03396)
**Michał Stypułkowski, Konstantinos Vougioukas, Sen He, Maciej Zięba et al.** · 2023-01-06

<details>
<summary>Abstract</summary>

Talking face generation has historically struggled to produce head movements and natural facial expressions without guidance from additional reference videos. Recent developments in diffusion-based generative models allow for more realistic and stable data synthesis and their performance on image and video generation has surpassed that of other generative models. In this work, we present an autoregressive diffusion model that requires only one identity image and audio sequence to generate a video of a realistic talking human head. Our solution is capable of hallucinating head movements, facial expressions, such as blinks, and preserving a given background. We evaluate our model on two different datasets, achieving state-of-the-art results on both of them.

</details>

#### [Expressive Speech-driven Facial Animation with controllable emotions](https://arxiv.org/abs/2301.02008)
**Yutong Chen, Junhong Zhao, Wei-Qiang Zhang** · 2023-01-05

<details>
<summary>Abstract</summary>

It is in high demand to generate facial animation with high realism, but it remains a challenging task. Existing approaches of speech-driven facial animation can produce satisfactory mouth movement and lip synchronization, but show weakness in dramatic emotional expressions and flexibility in emotion control. This paper presents a novel deep learning-based approach for expressive facial animation generation from speech that can exhibit wide-spectrum facial expressions with controllable emotion type and intensity. We propose an emotion controller module to learn the relationship between the emotion variations (e.g., types and intensity) and the corresponding facial expression parameters. It enables emotion-controllable facial animation, where the target expression can be continuously adjusted as desired. The qualitative and quantitative evaluations show that the animation generated by our method is rich in facial emotional expressiveness while retaining accurate lip movement, outperforming other state-of-the-art methods.

</details>

#### [LipNeRF: What is the right feature space to lip-sync a NeRF?](https://www.semanticscholar.org/paper/5d082bc5968b7138509758f88069288076227d42)
**Aggelina Chatziagapi, ShahRukh Athar, Abhinav Jain, M. Rohith et al.** · 2023-01-05

<details>
<summary>Abstract</summary>

Synthesizing high-fidelity talking head videos of an arbitrary identity, lip-synced to a target speech segment, is a challenging problem. Recent GAN-based methods succeed by training a model on a large amount of videos, allowing the generator to learn a variety of audio-lip representations. However, they are unable to handle head pose changes. On the other hand, Neural Radiance Fields (NeRFs) model the 3D face geometry more accurately. Current audio-conditioned NeRFs are not as good in lip synchronization as GANs, since they are trained on limited video data of a single identity. In this work, we propose LipNeRF, a lip-syncing NeRF that bridges the gap between the accurate lip synchronization of GAN-based methods and the accurate 3D face modeling of NeRFs. LipNeRF is conditioned on the expression space of a 3DMM, instead of the audio feature space. We experimentally demonstrate that the expression space gives a better representation for the lip shape than the audio feature space. LipNeRF shows a significant improvement in lip-sync quality over the current state-of-the-art, especially in high-definition videos of cinematic content, with challenging pose, illumination and expression variations.

</details>

#### [StyleTalk: One-shot Talking Head Generation with Controllable Speaking Styles](https://arxiv.org/abs/2301.01081)
**Yifeng Ma, Suzhen Wang, Zhipeng Hu, Changjie Fan et al.** · 2023-01-03

<details>
<summary>Abstract</summary>

Different people speak with diverse personalized speaking styles. Although existing one-shot talking head methods have made significant progress in lip sync, natural facial expressions, and stable head motions, they still cannot generate diverse speaking styles in the final talking head videos. To tackle this problem, we propose a one-shot style-controllable talking face generation framework. In a nutshell, we aim to attain a speaking style from an arbitrary reference speaking video and then drive the one-shot portrait to speak with the reference speaking style and another piece of audio. Specifically, we first develop a style encoder to extract dynamic facial motion patterns of a style reference video and then encode them into a style code. Afterward, we introduce a style-controllable decoder to synthesize stylized facial animations from the speech content and style code. In order to integrate the reference speaking style into generated videos, we design a style-aware adaptive transformer, which enables the encoded style code to adjust the weights of the feed-forward layers accordingly. Thanks to the style-aware adaptation mechanism, the reference speaking style can be better embedded into synthesized videos during decoding. Extensive experiments demonstrate that our method is capable of generating talking head videos with diverse speaking styles from only one portrait image and an audio clip while achieving authentic visual effects. Project Page: https://github.com/FuxiVirtualHuman/styletalk.

</details>

#### [A Simple and Efficient method for Dubbed Audio Sync Detection using Compressive Sensing](https://www.semanticscholar.org/paper/e0dcef74307d12f0b757c5a914a0925bf818bfcb)
**Avijit Vajpayee, Zhikang Zhang, Abhinav Jain, Vimal Bhat** · 2023-01-01

<details>
<summary>Abstract</summary>

Lack of temporal synchronization between audio and video streams represents one of the major quality defects in videos. The defect is more prominent in dubbed media due to errors in post-production such as improper audio overlay. Prior works in Audio-Video sync detection rely on either lip synchronization methods, which cannot be applied to dubbed media, or on self-supervised embeddings for general sound events, which are not accurate. In this paper, we present a novel, accurate and efficient method for temporal sync detection between dubbed audio tracks and corresponding non-dubbed original-language audio tracks. Using the availability of non-dubbed audio tracks and existing lip sync methods, we can simplify the problem of “Dubbed Audio-to-Video” sync detection to that of “Dubbed Audio-to-Original Audio” sync detection. Our method finds and compares matching frames in compressed audio signatures, achieving near perfect classification with 99.4 F1 score in less than 1 minute of processing time per hour of audio, along with ≈ 99.6% relative reduction in memory footprint compared to an uncompressed full audio spectrogram. We believe this is the first work to tackle temporal sync detection in dubbed media.

</details>

#### [DreamTalk: When Expressive Talking Head Generation Meets Diffusion Probabilistic Models](https://www.semanticscholar.org/paper/ccfaf773a4c4d6ac3e3da2c573846488cabfe449)
**Yifeng Ma, Shiwei Zhang, Jiayu Wang, Xiang Wang et al.** · 2023-01-01


</details>

<details open>
<summary><h3>2022</h3></summary>

#### [All's well that FID's well? Result quality and metric scores in GAN models for lip-sychronization tasks](https://arxiv.org/abs/2212.13810)
**Carina Geldhauser, Johan Liljegren, Pontus Nordqvist** · 2022-12-28

<details>
<summary>Abstract</summary>

We test the performance of GAN models for lip-synchronization. For this, we reimplement LipGAN in Pytorch, train it on the dataset GRID and compare it to our own variation, L1WGAN-GP, adapted to the LipGAN architecture and also trained on GRID.

</details>

#### [An Audio-Visual Speech Separation Model Inspired by Cortico-Thalamo-Cortical Circuits](https://arxiv.org/abs/2212.10744)
**Kai Li, Fenghua Xie, Hang Chen, Kexin Yuan et al.** · 2022-12-21

<details>
<summary>Abstract</summary>

Audio-visual approaches involving visual inputs have laid the foundation for recent progress in speech separation. However, the optimization of the concurrent usage of auditory and visual inputs is still an active research area. Inspired by the cortico-thalamo-cortical circuit, in which the sensory processing mechanisms of different modalities modulate one another via the non-lemniscal sensory thalamus, we propose a novel cortico-thalamo-cortical neural network (CTCNet) for audio-visual speech separation (AVSS). First, the CTCNet learns hierarchical auditory and visual representations in a bottom-up manner in separate auditory and visual subnetworks, mimicking the functions of the auditory and visual cortical areas. Then, inspired by the large number of connections between cortical regions and the thalamus, the model fuses the auditory and visual information in a thalamic subnetwork through top-down connections. Finally, the model transmits this fused information back to the auditory and visual subnetworks, and the above process is repeated several times. The results of experiments on three speech separation benchmark datasets show that CTCNet remarkably outperforms existing AVSS methods with considerably fewer parameters. These results suggest that mimicking the anatomical connectome of the mammalian brain has great potential for advancing the development of deep neural networks. Project repo is https://github.com/JusperLee/CTCNet.

</details>

#### [Masked Lip-Sync Prediction by Audio-Visual Contextual Exploitation in Transformers](https://arxiv.org/abs/2212.04970)
**Yasheng Sun, Hang Zhou, Kaisiyuan Wang, Qianyi Wu et al.** · 2022-12-09

<details>
<summary>Abstract</summary>

Previous studies have explored generating accurately lip-synced talking faces for arbitrary targets given audio conditions. However, most of them deform or generate the whole facial area, leading to non-realistic results. In this work, we delve into the formulation of altering only the mouth shapes of the target person. This requires masking a large percentage of the original image and seamlessly inpainting it with the aid of audio and reference frames. To this end, we propose the Audio-Visual Context-Aware Transformer (AV-CAT) framework, which produces accurate lip-sync with photo-realistic quality by predicting the masked mouth shapes. Our key insight is to exploit desired contextual information provided in audio and visual modalities thoroughly with delicately designed Transformers. Specifically, we propose a convolution-Transformer hybrid backbone and design an attention-based fusion strategy for filling the masked parts. It uniformly attends to the textural information on the unmasked regions and the reference frame. Then the semantic audio information is involved in enhancing the self-attention computation. Additionally, a refinement network with audio injection improves both image and lip-sync quality. Extensive experiments validate that our model can generate high-fidelity lip-synced results for arbitrary subjects.

</details>

#### [Memories are One-to-Many Mapping Alleviators in Talking Face Generation](https://arxiv.org/abs/2212.05005)
**Anni Tang, Tianyu He, Xu Tan, Jun Ling et al.** · 2022-12-09

<details>
<summary>Abstract</summary>

Talking face generation aims at generating photo-realistic video portraits of a target person driven by input audio. Due to its nature of one-to-many mapping from the input audio to the output video (e.g., one speech content may have multiple feasible visual appearances), learning a deterministic mapping like previous works brings ambiguity during training, and thus causes inferior visual results. Although this one-to-many mapping could be alleviated in part by a two-stage framework (i.e., an audio-to-expression model followed by a neural-rendering model), it is still insufficient since the prediction is produced without enough information (e.g., emotions, wrinkles, etc.). In this paper, we propose MemFace to complement the missing information with an implicit memory and an explicit memory that follow the sense of the two stages respectively. More specifically, the implicit memory is employed in the audio-to-expression model to capture high-level semantics in the audio-expression shared space, while the explicit memory is employed in the neural-rendering model to help synthesize pixel-level details. Our experimental results show that our proposed MemFace surpasses all the state-of-the-art results across multiple scenarios consistently and significantly.

</details>

#### [Talking Head Generation with Probabilistic Audio-to-Visual Diffusion Priors](https://arxiv.org/abs/2212.04248)
**Zhentao Yu, Zixin Yin, Deyu Zhou, Duomin Wang et al.** · 2022-12-07

<details>
<summary>Abstract</summary>

In this paper, we introduce a simple and novel framework for one-shot audio-driven talking head generation. Unlike prior works that require additional driving sources for controlled synthesis in a deterministic manner, we instead probabilistically sample all the holistic lip-irrelevant facial motions (i.e. pose, expression, blink, gaze, etc.) to semantically match the input audio while still maintaining both the photo-realism of audio-lip synchronization and the overall naturalness. This is achieved by our newly proposed audio-to-visual diffusion prior trained on top of the mapping between audio and disentangled non-lip facial representations. Thanks to the probabilistic nature of the diffusion prior, one big advantage of our framework is it can synthesize diverse facial motion sequences given the same audio clip, which is quite user-friendly for many real applications. Through comprehensive evaluations on public benchmarks, we conclude that (1) our diffusion prior outperforms auto-regressive prior significantly on almost all the concerned metrics; (2) our overall system is competitive with prior works in terms of audio-lip synchronization but can effectively sample rich and natural-looking lip-irrelevant facial motions while still semantically harmonized with the audio input.

</details>

#### [Self-Supervised Audio-Visual Speech Representations Learning By Multimodal Self-Distillation](https://arxiv.org/abs/2212.02782)
**Jing-Xuan Zhang, Genshun Wan, Zhen-Hua Ling, Jia Pan et al.** · 2022-12-06

<details>
<summary>Abstract</summary>

In this work, we present a novel method, named AV2vec, for learning audio-visual speech representations by multimodal self-distillation. AV2vec has a student and a teacher module, in which the student performs a masked latent feature regression task using the multimodal target features generated online by the teacher. The parameters of the teacher model are a momentum update of the student. Since our target features are generated online, AV2vec needs no iteration step like AV-HuBERT and the total training time cost is reduced to less than one-fifth. We further propose AV2vec-MLM in this study, which augments AV2vec with a masked language model (MLM)-style loss using multitask learning. Our experimental results show that AV2vec achieved comparable performance to the AV-HuBERT baseline. When combined with an MLM-style loss, AV2vec-MLM outperformed baselines and achieved the best performance on the downstream tasks.

</details>

#### [High-fidelity Facial Avatar Reconstruction from Monocular Video with Generative Priors](https://arxiv.org/abs/2211.15064)
**Yunpeng Bai, Yanbo Fan, Xuan Wang, Yong Zhang et al.** · 2022-11-28

<details>
<summary>Abstract</summary>

High-fidelity facial avatar reconstruction from a monocular video is a significant research problem in computer graphics and computer vision. Recently, Neural Radiance Field (NeRF) has shown impressive novel view rendering results and has been considered for facial avatar reconstruction. However, the complex facial dynamics and missing 3D information in monocular videos raise significant challenges for faithful facial reconstruction. In this work, we propose a new method for NeRF-based facial avatar reconstruction that utilizes 3D-aware generative prior. Different from existing works that depend on a conditional deformation field for dynamic modeling, we propose to learn a personalized generative prior, which is formulated as a local and low dimensional subspace in the latent space of 3D-GAN. We propose an efficient method to construct the personalized generative prior based on a small set of facial images of a given individual. After learning, it allows for photo-realistic rendering with novel views and the face reenactment can be realized by performing navigation in the latent space. Our proposed method is applicable for different driven signals, including RGB images, 3DMM coefficients, and audios. Compared with existing works, we obtain superior novel view synthesis results and faithfully face reenactment performance.

</details>

#### [VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild](https://arxiv.org/abs/2211.14758)
**Kun Cheng, Xiaodong Cun, Yong Zhang, Menghan Xia et al.** · 2022-11-27

<details>
<summary>Abstract</summary>

We present VideoReTalking, a new system to edit the faces of a real-world talking head video according to input audio, producing a high-quality and lip-syncing output video even with a different emotion. Our system disentangles this objective into three sequential tasks: (1) face video generation with a canonical expression; (2) audio-driven lip-sync; and (3) face enhancement for improving photo-realism. Given a talking-head video, we first modify the expression of each frame according to the same expression template using the expression editing network, resulting in a video with the canonical expression. This video, together with the given audio, is then fed into the lip-sync network to generate a lip-syncing video. Finally, we improve the photo-realism of the synthesized faces through an identity-aware face enhancement network and post-processing. We use learning-based approaches for all three steps and all our modules can be tackled in a sequential pipeline without any user intervention. Furthermore, our system is a generic approach that does not need to be retrained to a specific person. Evaluations on two widely-used datasets and in-the-wild examples demonstrate the superiority of our framework over other state-of-the-art methods in terms of lip-sync accuracy and visual quality.

</details>

#### [LA-VocE: Low-SNR Audio-visual Speech Enhancement using Neural Vocoders](https://arxiv.org/abs/2211.10999)
**Rodrigo Mira, Buye Xu, Jacob Donley, Anurag Kumar et al.** · 2022-11-20

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement aims to extract clean speech from a noisy environment by leveraging not only the audio itself but also the target speaker's lip movements. This approach has been shown to yield improvements over audio-only speech enhancement, particularly for the removal of interfering speech. Despite recent advances in speech synthesis, most audio-visual approaches continue to use spectral mapping/masking to reproduce the clean audio, often resulting in visual backbones added to existing speech enhancement architectures. In this work, we propose LA-VocE, a new two-stage approach that predicts mel-spectrograms from noisy audio-visual speech via a transformer-based architecture, and then converts them into waveform audio using a neural vocoder (HiFi-GAN). We train and evaluate our framework on thousands of speakers and 11+ different languages, and study our model's ability to adapt to different levels of background noise and speech interference. Our experiments show that LA-VocE outperforms existing methods according to multiple metrics, particularly under very noisy scenarios.

</details>

#### [MARLIN: Masked Autoencoder for facial video Representation LearnINg](https://arxiv.org/abs/2211.06627)
**Zhixi Cai, Shreya Ghosh, Kalin Stefanov, Abhinav Dhall et al.** · 2022-11-12

<details>
<summary>Abstract</summary>

This paper proposes a self-supervised approach to learn universal facial representations from videos, that can transfer across a variety of facial analysis tasks such as Facial Attribute Recognition (FAR), Facial Expression Recognition (FER), DeepFake Detection (DFD), and Lip Synchronization (LS). Our proposed framework, named MARLIN, is a facial video masked autoencoder, that learns highly robust and generic facial embeddings from abundantly available non-annotated web crawled facial videos. As a challenging auxiliary task, MARLIN reconstructs the spatio-temporal details of the face from the densely masked facial regions which mainly include eyes, nose, mouth, lips, and skin to capture local and global aspects that in turn help in encoding generic and transferable features. Through a variety of experiments on diverse downstream tasks, we demonstrate MARLIN to be an excellent facial video encoder as well as feature extractor, that performs consistently well across a variety of downstream tasks including FAR (1.13% gain over supervised benchmark), FER (2.64% gain over unsupervised benchmark), DFD (1.86% gain over unsupervised benchmark), LS (29.36% gain for Frechet Inception Distance), and even in low data regime. Our code and models are available at https://github.com/ControlNet/MARLIN .

</details>

#### [Lip Sync Matters: A Novel Multimodal Forgery Detector](https://www.semanticscholar.org/paper/71c614bd54f89d0d618e2a917349c37a875eedab)
**Sahibzada Adil Shahzad, Ammarah Hashmi, S. Khan, Yan-Tsung Peng et al.** · 2022-11-07

<details>
<summary>Abstract</summary>

Deepfake technology has advanced a lot, but it is a double-sided sword for the community. One can use it for beneficial purposes, such as restoring vintage content in old movies, or for nefarious purposes, such as creating fake footage to manipulate the public and distribute non-consensual pornography. A lot of work has been done to combat its improper use by detecting fake footage with good performance thanks to the availability of numerous public datasets and unimodal deep learning-based models. However, these methods are insufficient to detect multimodal manipulations, such as both visual and acoustic. This work proposes a novel lip-reading-based multi-modal Deepfake detection method called “Lip Sync Matters.” It targets high-level semantic features to exploit the mismatch between the lip sequence extracted from the video and the synthetic lip sequence generated from the audio by the Wav2lip model to detect forged videos. Experimental results show that the proposed method outperforms several existing unimodal, ensemble, and multimodal methods on the publicly available multimodal FakeAVCeleb dataset.

</details>

#### [Autoregressive GAN for Semantic Unconditional Head Motion Generation](https://arxiv.org/abs/2211.00987)
**Louis Airale, Xavier Alameda-Pineda, Stéphane Lathuilière, Dominique Vaufreydaz** · 2022-11-02

<details>
<summary>Abstract</summary>

In this work, we address the task of unconditional head motion generation to animate still human faces in a low-dimensional semantic space from a single reference pose. Different from traditional audio-conditioned talking head generation that seldom puts emphasis on realistic head motions, we devise a GAN-based architecture that learns to synthesize rich head motion sequences over long duration while maintaining low error accumulation levels.In particular, the autoregressive generation of incremental outputs ensures smooth trajectories, while a multi-scale discriminator on input pairs drives generation toward better handling of high- and low-frequency signals and less mode collapse.We experimentally demonstrate the relevance of the proposed method and show its superiority compared to models that attained state-of-the-art performances on similar tasks.

</details>

#### [Audio-visual speech enhancement with a deep Kalman filter generative model](https://arxiv.org/abs/2211.00988)
**Ali Golmakani, Mostafa Sadeghi, Romain Serizel** · 2022-11-02

<details>
<summary>Abstract</summary>

Deep latent variable generative models based on variational autoencoder (VAE) have shown promising performance for audiovisual speech enhancement (AVSE). The underlying idea is to learn a VAEbased audiovisual prior distribution for clean speech data, and then combine it with a statistical noise model to recover a speech signal from a noisy audio recording and video (lip images) of the target speaker. Existing generative models developed for AVSE do not take into account the sequential nature of speech data, which prevents them from fully incorporating the power of visual data. In this paper, we present an audiovisual deep Kalman filter (AV-DKF) generative model which assumes a first-order Markov chain model for the latent variables and effectively fuses audiovisual data. Moreover, we develop an efficient inference methodology to estimate speech signals at test time. We conduct a set of experiments to compare different variants of generative models for speech enhancement. The results demonstrate the superiority of the AV-DKF model compared with both its audio-only version and the non-sequential audio-only and audiovisual VAE-based models.

</details>

#### [A Novel Frame Structure for Cloud-Based Audio-Visual Speech Enhancement in Multimodal Hearing-aids](https://arxiv.org/abs/2210.13127)
**Abhijeet Bishnu, Ankit Gupta, Mandar Gogate, Kia Dashtipour et al.** · 2022-10-24

<details>
<summary>Abstract</summary>

In this paper, we design a first of its kind transceiver (PHY layer) prototype for cloud-based audio-visual (AV) speech enhancement (SE) complying with high data rate and low latency requirements of future multimodal hearing assistive technology. The innovative design needs to meet multiple challenging constraints including up/down link communications, delay of transmission and signal processing, and real-time AV SE models processing. The transceiver includes device detection, frame detection, frequency offset estimation, and channel estimation capabilities. We develop both uplink (hearing aid to the cloud) and downlink (cloud to hearing aid) frame structures based on the data rate and latency requirements. Due to the varying nature of uplink information (audio and lip-reading), the uplink channel supports multiple data rate frame structure, while the downlink channel has a fixed data rate frame structure. In addition, we evaluate the latency of different PHY layer blocks of the transceiver for developed frame structures using LabVIEW NXG. This can be used with software defined radio (such as Universal Software Radio Peripheral) for real-time demonstration scenarios.

</details>

#### [Sparse in Space and Time: Audio-visual Synchronisation with Trainable Selectors](https://arxiv.org/abs/2210.07055)
**Vladimir Iashin, Weidi Xie, Esa Rahtu, Andrew Zisserman** · 2022-10-13

<details>
<summary>Abstract</summary>

The objective of this paper is audio-visual synchronisation of general videos 'in the wild'. For such videos, the events that may be harnessed for synchronisation cues may be spatially small and may occur only infrequently during a many seconds-long video clip, i.e. the synchronisation signal is 'sparse in space and time'. This contrasts with the case of synchronising videos of talking heads, where audio-visual correspondence is dense in both time and space. We make four contributions: (i) in order to handle longer temporal sequences required for sparse synchronisation signals, we design a multi-modal transformer model that employs 'selectors' to distil the long audio and visual streams into small sequences that are then used to predict the temporal offset between streams. (ii) We identify artefacts that can arise from the compression codecs used for audio and video and can be used by audio-visual models in training to artificially solve the synchronisation task. (iii) We curate a dataset with only sparse in time and space synchronisation signals; and (iv) the effectiveness of the proposed model is shown on both dense and sparse datasets quantitatively and qualitatively. Project page: v-iashin.github.io/SparseSync

</details>

#### [StyleMask: Disentangling the Style Space of StyleGAN2 for Neural Face Reenactment](https://arxiv.org/abs/2209.13375)
**Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras et al.** · 2022-09-27

<details>
<summary>Abstract</summary>

In this paper we address the problem of neural face reenactment, where, given a pair of a source and a target facial image, we need to transfer the target's pose (defined as the head pose and its facial expressions) to the source image, by preserving at the same time the source's identity characteristics (e.g., facial shape, hair style, etc), even in the challenging case where the source and the target faces belong to different identities. In doing so, we address some of the limitations of the state-of-the-art works, namely, a) that they depend on paired training data (i.e., source and target faces have the same identity), b) that they rely on labeled data during inference, and c) that they do not preserve identity in large head pose changes. More specifically, we propose a framework that, using unpaired randomly generated facial images, learns to disentangle the identity characteristics of the face from its pose by incorporating the recently introduced style space $\mathcal{S}$ of StyleGAN2, a latent representation space that exhibits remarkable disentanglement properties. By capitalizing on this, we learn to successfully mix a pair of source and target style codes using supervision from a 3D model. The resulting latent code, that is subsequently used for reenactment, consists of latent units corresponding to the facial pose of the target only and of units corresponding to the identity of the source only, leading to notable improvement in the reenactment performance compared to recent state-of-the-art methods. In comparison to state of the art, we quantitatively and qualitatively show that the proposed method produces higher quality results even on extreme pose variations. Finally, we report results on real images by first embedding them on the latent space of the pretrained generator. We make the code and pretrained models publicly available at: https://github.com/StelaBou/StyleMask

</details>

#### [Gemino: Practical and Robust Neural Compression for Video Conferencing](https://arxiv.org/abs/2209.10507)
**Vibhaalakshmi Sivaraman, Pantea Karimi, Vedantha Venkatapathy, Mehrdad Khani et al.** · 2022-09-21

<details>
<summary>Abstract</summary>

Video conferencing systems suffer from poor user experience when network conditions deteriorate because current video codecs simply cannot operate at extremely low bitrates. Recently, several neural alternatives have been proposed that reconstruct talking head videos at very low bitrates using sparse representations of each frame such as facial landmark information. However, these approaches produce poor reconstructions in scenarios with major movement or occlusions over the course of a call, and do not scale to higher resolutions. We design Gemino, a new neural compression system for video conferencing based on a novel high-frequency-conditional super-resolution pipeline. Gemino upsamples a very low-resolution version of each target frame while enhancing high-frequency details (e.g., skin texture, hair, etc.) based on information extracted from a single high-resolution reference image. We use a multi-scale architecture that runs different components of the model at different resolutions, allowing it to scale to resolutions comparable to 720p, and we personalize the model to learn specific details of each person, achieving much better fidelity at low bitrates. We implement Gemino atop aiortc, an open-source Python implementation of WebRTC, and show that it operates on 1024x1024 videos in real-time on a Titan X GPU, and achieves 2.2-5x lower bitrate than traditional video codecs for the same perceptual quality.

</details>

#### [Continuously Controllable Facial Expression Editing in Talking Face Videos](https://arxiv.org/abs/2209.08289)
**Zhiyao Sun, Yu-Hui Wen, Tian Lv, Yanan Sun et al.** · 2022-09-17

<details>
<summary>Abstract</summary>

Recently audio-driven talking face video generation has attracted considerable attention. However, very few researches address the issue of emotional editing of these talking face videos with continuously controllable expressions, which is a strong demand in the industry. The challenge is that speech-related expressions and emotion-related expressions are often highly coupled. Meanwhile, traditional image-to-image translation methods cannot work well in our application due to the coupling of expressions with other attributes such as poses, i.e., translating the expression of the character in each frame may simultaneously change the head pose due to the bias of the training data distribution. In this paper, we propose a high-quality facial expression editing method for talking face videos, allowing the user to control the target emotion in the edited video continuously. We present a new perspective for this task as a special case of motion information editing, where we use a 3DMM to capture major facial movements and an associated texture map modeled by a StyleGAN to capture appearance details. Both representations (3DMM and texture map) contain emotional information and can be continuously modified by neural networks and easily smoothed by averaging in coefficient/latent spaces, making our method simple yet effective. We also introduce a mouth shape preservation loss to control the trade-off between lip synchronization and the degree of exaggeration of the edited expression. Extensive experiments and a user study show that our method achieves state-of-the-art performance across various evaluation criteria.

</details>

#### [Talking Head from Speech Audio using a Pre-trained Image Generator](https://arxiv.org/abs/2209.04252)
**Mohammed M. Alghamdi, He Wang, Andrew J. Bulpitt, David C. Hogg** · 2022-09-09

<details>
<summary>Abstract</summary>

We propose a novel method for generating high-resolution videos of talking-heads from speech audio and a single 'identity' image. Our method is based on a convolutional neural network model that incorporates a pre-trained StyleGAN generator. We model each frame as a point in the latent space of StyleGAN so that a video corresponds to a trajectory through the latent space. Training the network is in two stages. The first stage is to model trajectories in the latent space conditioned on speech utterances. To do this, we use an existing encoder to invert the generator, mapping from each video frame into the latent space. We train a recurrent neural network to map from speech utterances to displacements in the latent space of the image generator. These displacements are relative to the back-projection into the latent space of an identity image chosen from the individuals depicted in the training dataset. In the second stage, we improve the visual quality of the generated videos by tuning the image generator on a single image or a short video of any chosen identity. We evaluate our model on standard measures (PSNR, SSIM, FID and LMD) and show that it significantly outperforms recent state-of-the-art methods on one of two commonly used datasets and gives comparable performance on the other. Finally, we report on ablation experiments that validate the components of the model. The code and videos from experiments can be found at https://mohammedalghamdi.github.io/talking-heads-acm-mm

</details>

#### [Multimodal Speech Enhancement Using Burst Propagation](https://arxiv.org/abs/2209.03275)
**Mohsin Raza, Leandro A. Passos, Ahmed Khubaib, Ahsan Adeel** · 2022-09-07

<details>
<summary>Abstract</summary>

This paper proposes the MBURST, a novel multimodal solution for audio-visual speech enhancements that consider the most recent neurological discoveries regarding pyramidal cells of the prefrontal cortex and other brain regions. The so-called burst propagation implements several criteria to address the credit assignment problem in a more biologically plausible manner: steering the sign and magnitude of plasticity through feedback, multiplexing the feedback and feedforward information across layers through different weight connections, approximating feedback and feedforward connections, and linearizing the feedback signals. MBURST benefits from such capabilities to learn correlations between the noisy signal and the visual stimuli, thus attributing meaning to the speech by amplifying relevant information and suppressing noise. Experiments conducted over a Grid Corpus and CHiME3-based dataset show that MBURST can reproduce similar mask reconstructions to the multimodal backpropagation-based baseline while demonstrating outstanding energy efficiency management, reducing the neuron firing rates to values up to \textbf{$70\%$} lower. Such a feature implies more sustainable implementations, suitable and desirable for hearing aids or any other similar embedded systems.

</details>

#### [StableFace: Analyzing and Improving Motion Stability for Talking Face Generation](https://arxiv.org/abs/2208.13717)
**Jun Ling, Xu Tan, Liyang Chen, Runnan Li et al.** · 2022-08-29

<details>
<summary>Abstract</summary>

While previous speech-driven talking face generation methods have made significant progress in improving the visual quality and lip-sync quality of the synthesized videos, they pay less attention to lip motion jitters which greatly undermine the realness of talking face videos. What causes motion jitters, and how to mitigate the problem? In this paper, we conduct systematic analyses on the motion jittering problem based on a state-of-the-art pipeline that uses 3D face representations to bridge the input audio and output video, and improve the motion stability with a series of effective designs. We find that several issues can lead to jitters in synthesized talking face video: 1) jitters from the input 3D face representations; 2) training-inference mismatch; 3) lack of dependency modeling among video frames. Accordingly, we propose three effective solutions to address this issue: 1) we propose a gaussian-based adaptive smoothing module to smooth the 3D face representations to eliminate jitters in the input; 2) we add augmented erosions on the input data of the neural renderer in training to simulate the distortion in inference to reduce mismatch; 3) we develop an audio-fused transformer generator to model dependency among video frames. Besides, considering there is no off-the-shelf metric for measuring motion jitters in talking face video, we devise an objective metric (Motion Stability Index, MSI), to quantitatively measure the motion jitters by calculating the reciprocal of variance acceleration. Extensive experimental results show the superiority of our method on motion-stable face video generation, with better quality than previous systems.

</details>

#### [Towards MOOCs for Lipreading: Using Synthetic Talking Heads to Train Humans in Lipreading at Scale](https://arxiv.org/abs/2208.09796)
**Aditya Agarwal, Bipasha Sen, Rudrabha Mukhopadhyay, Vinay Namboodiri et al.** · 2022-08-21

<details>
<summary>Abstract</summary>

Many people with some form of hearing loss consider lipreading as their primary mode of day-to-day communication. However, finding resources to learn or improve one's lipreading skills can be challenging. This is further exacerbated in the COVID19 pandemic due to restrictions on direct interactions with peers and speech therapists. Today, online MOOCs platforms like Coursera and Udemy have become the most effective form of training for many types of skill development. However, online lipreading resources are scarce as creating such resources is an extensive process needing months of manual effort to record hired actors. Because of the manual pipeline, such platforms are also limited in vocabulary, supported languages, accents, and speakers and have a high usage cost. In this work, we investigate the possibility of replacing real human talking videos with synthetically generated videos. Synthetic data can easily incorporate larger vocabularies, variations in accent, and even local languages and many speakers. We propose an end-to-end automated pipeline to develop such a platform using state-of-the-art talking head video generator networks, text-to-speech models, and computer vision techniques. We then perform an extensive human evaluation using carefully thought out lipreading exercises to validate the quality of our designed platform against the existing lipreading platforms. Our studies concretely point toward the potential of our approach in developing a large-scale lipreading MOOC platform that can impact millions of people with hearing loss.

</details>

#### [Free-HeadGAN: Neural Talking Head Synthesis with Explicit Gaze Control](https://arxiv.org/abs/2208.02210)
**Michail Christos Doukas, Evangelos Ververas, Viktoriia Sharmanska, Stefanos Zafeiriou** · 2022-08-03

<details>
<summary>Abstract</summary>

We present Free-HeadGAN, a person-generic neural talking head synthesis system. We show that modeling faces with sparse 3D facial landmarks are sufficient for achieving state-of-the-art generative performance, without relying on strong statistical priors of the face, such as 3D Morphable Models. Apart from 3D pose and facial expressions, our method is capable of fully transferring the eye gaze, from a driving actor to a source identity. Our complete pipeline consists of three components: a canonical 3D key-point estimator that regresses 3D pose and expression-related deformations, a gaze estimation network and a generator that is built upon the architecture of HeadGAN. We further experiment with an extension of our generator to accommodate few-shot learning using an attention mechanism, in case more than one source images are available. Compared to the latest models for reenactment and motion transfer, our system achieves higher photo-realism combined with superior identity preservation, while offering explicit gaze control.

</details>

#### [Visual Speech-Aware Perceptual 3D Facial Expression Reconstruction from Videos](https://arxiv.org/abs/2207.11094)
**Panagiotis P. Filntisis, George Retsinas, Foivos Paraperas-Papantoniou, Athanasios Katsamanis et al.** · 2022-07-22

<details>
<summary>Abstract</summary>

The recent state of the art on monocular 3D face reconstruction from image data has made some impressive advancements, thanks to the advent of Deep Learning. However, it has mostly focused on input coming from a single RGB image, overlooking the following important factors: a) Nowadays, the vast majority of facial image data of interest do not originate from single images but rather from videos, which contain rich dynamic information. b) Furthermore, these videos typically capture individuals in some form of verbal communication (public talks, teleconferences, audiovisual human-computer interactions, interviews, monologues/dialogues in movies, etc). When existing 3D face reconstruction methods are applied in such videos, the artifacts in the reconstruction of the shape and motion of the mouth area are often severe, since they do not match well with the speech audio. To overcome the aforementioned limitations, we present the first method for visual speech-aware perceptual reconstruction of 3D mouth expressions. We do this by proposing a "lipread" loss, which guides the fitting process so that the elicited perception from the 3D reconstructed talking head resembles that of the original video footage. We demonstrate that, interestingly, the lipread loss is better suited for 3D reconstruction of mouth movements compared to traditional landmark losses, and even direct 3D supervision. Furthermore, the devised method does not rely on any text transcriptions or corresponding audio, rendering it ideal for training in unlabeled datasets. We verify the efficiency of our method through exhaustive objective evaluations on three large-scale datasets, as well as subjective evaluation with two web-based user studies.

</details>

#### [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](https://arxiv.org/abs/2207.03800)
**Yongqi Wang, Zhou Zhao** · 2022-07-08

<details>
<summary>Abstract</summary>

Unconstrained lip-to-speech synthesis aims to generate corresponding speeches from silent videos of talking faces with no restriction on head poses or vocabulary. Current works mainly use sequence-to-sequence models to solve this problem, either in an autoregressive architecture or a flow-based non-autoregressive architecture. However, these models suffer from several drawbacks: 1) Instead of directly generating audios, they use a two-stage pipeline that first generates mel-spectrograms and then reconstructs audios from the spectrograms. This causes cumbersome deployment and degradation of speech quality due to error propagation; 2) The audio reconstruction algorithm used by these models limits the inference speed and audio quality, while neural vocoders are not available for these models since their output spectrograms are not accurate enough; 3) The autoregressive model suffers from high inference latency, while the flow-based model has high memory occupancy: neither of them is efficient enough in both time and memory usage. To tackle these problems, we propose FastLTS, a non-autoregressive end-to-end model which can directly synthesize high-quality speech audios from unconstrained talking videos with low latency, and has a relatively small model size. Besides, different from the widely used 3D-CNN visual frontend for lip movement encoding, we for the first time propose a transformer-based visual frontend for this task. Experiments show that our model achieves $19.76\times$ speedup for audio waveform generation compared with the current autoregressive model on input sequences of 3 seconds, and obtains superior audio quality.

</details>

#### [Improving Visual Speech Enhancement Network by Learning Audio-visual Affinity with Multi-head Attention](https://arxiv.org/abs/2206.14964)
**Xinmeng Xu, Yang Wang, Jie Jia, Binbin Chen et al.** · 2022-06-30

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement system is regarded as one of promising solutions for isolating and enhancing speech of desired speaker. Typical methods focus on predicting clean speech spectrum via a naive convolution neural network based encoder-decoder architecture, and these methods a) are not adequate to use data fully, b) are unable to effectively balance audio-visual features. The proposed model alleviates these drawbacks by a) applying a model that fuses audio and visual features layer by layer in encoding phase, and that feeds fused audio-visual features to each corresponding decoder layer, and more importantly, b) introducing a 2-stage multi-head cross attention (MHCA) mechanism to infer audio-visual speech enhancement for balancing the fused audio-visual features and eliminating irrelevant features. This paper proposes attentional audio-visual multi-layer feature fusion model, in which MHCA units are applied to feature mapping at every layer of decoder. The proposed model demonstrates the superior performance of the network against the state-of-the-art models.

</details>

#### [Cut Inner Layers: A Structured Pruning Strategy for Efficient U-Net GANs](https://arxiv.org/abs/2206.14658)
**Bo-Kyeong Kim, Shinkook Choi, Hancheol Park** · 2022-06-29

<details>
<summary>Abstract</summary>

Pruning effectively compresses overparameterized models. Despite the success of pruning methods for discriminative models, applying them for generative models has been relatively rarely approached. This study conducts structured pruning on U-Net generators of conditional GANs. A per-layer sensitivity analysis confirms that many unnecessary filters exist in the innermost layers near the bottleneck and can be substantially pruned. Based on this observation, we prune these filters from multiple inner layers or suggest alternative architectures by completely eliminating the layers. We evaluate our approach with Pix2Pix for image-to-image translation and Wav2Lip for speech-driven talking face generation. Our method outperforms global pruning baselines, demonstrating the importance of properly considering where to prune for U-Net generators.

</details>

#### [Canonical Cortical Graph Neural Networks and its Application for Speech Enhancement in Audio-Visual Hearing Aids](https://arxiv.org/abs/2206.02671)
**Leandro A. Passos, João Paulo Papa, Amir Hussain, Ahsan Adeel** · 2022-06-06

<details>
<summary>Abstract</summary>

Despite the recent success of machine learning algorithms, most models face drawbacks when considering more complex tasks requiring interaction between different sources, such as multimodal input data and logical time sequences. On the other hand, the biological brain is highly sharpened in this sense, empowered to automatically manage and integrate such streams of information. In this context, this work draws inspiration from recent discoveries in brain cortical circuits to propose a more biologically plausible self-supervised machine learning approach. This combines multimodal information using intra-layer modulations together with Canonical Correlation Analysis, and a memory mechanism to keep track of temporal data, the overall approach termed Canonical Cortical Graph Neural networks. This is shown to outperform recent state-of-the-art models in terms of clean audio reconstruction and energy efficiency for a benchmark audio-visual speech dataset. The enhanced performance is demonstrated through a reduced and smother neuron firing rate distribution. suggesting that the proposed model is amenable for speech enhancement in future audio-visual hearing aid devices.

</details>

#### [Learning Speaker-specific Lip-to-Speech Generation](https://arxiv.org/abs/2206.02050)
**Munender Varshney, Ravindra Yadav, Vinay P. Namboodiri, R. Hegde** · 2022-06-04

<details>
<summary>Abstract</summary>

Understanding the lip movement and inferring the speech from it is notoriously difficult for the common person. The task of accurate lip-reading gets help from various cues of the speaker and its contextual or environmental setting. Every speaker has a different accent and speaking style, which can be inferred from their visual and speech features. This work aims to understand the correlation/mapping between speech and the sequence of lip movement of individual speakers in an unconstrained and large vocabulary. We model the frame sequence as a distribution of features from the transformer in an autoencoder setting and learn the embeddings jointly that exploits temporal properties of both audio and video. We learn temporal synchronization using deep metric learning, which guides the decoder to generate speech in sync with input lip movements. The predictive posterior thus gives us the generated speech in speaker speaking style. We have trained our model on the Grid and Lip2Wav Chemistry lecture dataset to evaluate single speaker natural speech generation tasks from lip movement in an unconstrained natural setting. Extensive evaluation using various qualitative and quantitative metrics with human evaluation also shows that our method outperforms on Lip2Wav Chemistry dataset (large vocabulary in an unconstrained setting) by a good margin across almost all evaluation metrics and marginally outperforms the state-of-the-art on GRID dataset.

</details>

#### [One-Shot Face Reenactment on Megapixels](https://arxiv.org/abs/2205.13368)
**Wonjun Kang, Geonsu Lee, Hyung Il Koo, Nam Ik Cho** · 2022-05-26

<details>
<summary>Abstract</summary>

The goal of face reenactment is to transfer a target expression and head pose to a source face while preserving the source identity. With the popularity of face-related applications, there has been much research on this topic. However, the results of existing methods are still limited to low-resolution and lack photorealism. In this work, we present a one-shot and high-resolution face reenactment method called MegaFR. To be precise, we leverage StyleGAN by using 3DMM-based rendering images and overcome the lack of high-quality video datasets by designing a loss function that works without high-quality videos. Also, we apply iterative refinement to deal with extreme poses and/or expressions. Since the proposed method controls source images through 3DMM parameters, we can explicitly manipulate source images. We apply MegaFR to various applications such as face frontalization, eye in-painting, and talking head generation. Experimental results show that our method successfully disentangles identity from expression and head pose, and outperforms conventional methods.

</details>

#### [Merkel Podcast Corpus: A Multimodal Dataset Compiled from 16 Years of Angela Merkel's Weekly Video Podcasts](https://arxiv.org/abs/2205.12194)
**Debjoy Saha, Shravan Nayak, Timo Baumann** · 2022-05-24

<details>
<summary>Abstract</summary>

We introduce the Merkel Podcast Corpus, an audio-visual-text corpus in German collected from 16 years of (almost) weekly Internet podcasts of former German chancellor Angela Merkel. To the best of our knowledge, this is the first single speaker corpus in the German language consisting of audio, visual and text modalities of comparable size and temporal extent. We describe the methods used with which we have collected and edited the data which involves downloading the videos, transcripts and other metadata, forced alignment, performing active speaker recognition and face detection to finally curate the single speaker dataset consisting of utterances spoken by Angela Merkel. The proposed pipeline is general and can be used to curate other datasets of similar nature, such as talk show contents. Through various statistical analyses and applications of the dataset in talking face generation and TTS, we show the utility of the dataset. We argue that it is a valuable contribution to the research community, in particular, due to its realistic and challenging material at the boundary between prepared and spontaneous speech.

</details>

#### [Meta Talk: Learning To Data-Efficiently Generate Audio-Driven Lip-Synchronized Talking Face With High Definition](https://www.semanticscholar.org/paper/e3d8c277a9a688d57ca1d33408ba36b2c3c4ec66)
**Yuhan Zhang, Weihua He, Minglei Li, Kun Tian et al.** · 2022-05-23

<details>
<summary>Abstract</summary>

Audio-driven talking face, driving talking face by audio, has received considerable attention in multi-modal learning due to its widespread use in virtual reality. However, long-time recording of target high-quality video is needed by most existing audio-driven talking face studies, which significantly increases customization costs. This paper proposes a novel data-efficient audio-driven talking face generation method, which uses just a short target video to produce both lip-synchronized and high-definition face video driven by arbitrary audio in the wild. Current methods suffer from many problems, such as low definition, asynchronization of lip movement and voice, and intense demands for videos for training. In this work, the original target character’s face images are decomposed into 3D face model parameters including expression, geometry, illumination, etc. Then, low-definition pseudo video generated by an adapted target face video bridges the powerful pre-trained audio-driven model to our audio-to-expression transformation network and help to transfer the ability of audio-identity disentanglement. The expression is replaced via an audio and then combined with other face parameters to render a synthetic face. Finally, a neural rendering network translates the synthetic face into talking face without loss of definition. Experimental results show that the proposed method has the best performance in high-definition image quality, and comparable performance in lip synchronization compared with the existing state-of-the-art methods.

</details>

#### [Learning Lip-Based Audio-Visual Speaker Embeddings with AV-HuBERT](https://arxiv.org/abs/2205.07180)
**Bowen Shi, Abdelrahman Mohamed, Wei-Ning Hsu** · 2022-05-15

<details>
<summary>Abstract</summary>

This paper investigates self-supervised pre-training for audio-visual speaker representation learning where a visual stream showing the speaker's mouth area is used alongside speech as inputs. Our study focuses on the Audio-Visual Hidden Unit BERT (AV-HuBERT) approach, a recently developed general-purpose audio-visual speech pre-training framework. We conducted extensive experiments probing the effectiveness of pre-training and visual modality. Experimental results suggest that AV-HuBERT generalizes decently to speaker related downstream tasks, improving label efficiency by roughly ten fold for both audio-only and audio-visual speaker verification. We also show that incorporating visual information, even just the lip area, greatly improves the performance and noise robustness, reducing EER by 38% in the clean condition and 75% in noisy conditions.

</details>

#### [Talking Face Generation with Multilingual TTS](https://arxiv.org/abs/2205.06421)
**Hyoung-Kyu Song, Sang Hoon Woo, Junhyeok Lee, Seungmin Yang et al.** · 2022-05-13

<details>
<summary>Abstract</summary>

In this work, we propose a joint system combining a talking face generation system with a text-to-speech system that can generate multilingual talking face videos from only the text input. Our system can synthesize natural multilingual speeches while maintaining the vocal identity of the speaker, as well as lip movements synchronized to the synthesized speech. We demonstrate the generalization capabilities of our system by selecting four languages (Korean, English, Japanese, and Chinese) each from a different language family. We also compare the outputs of our talking face generation model to outputs of a prior work that claims multilingual support. For our demo, we add a translation API to the preprocessing stage and present it in the form of a neural dubber so that users can utilize the multilingual property of our system more easily.

</details>

#### [Emotion-Controllable Generalized Talking Face Generation](https://arxiv.org/abs/2205.01155)
**Sanjana Sinha, Sandika Biswas, Ravindra Yadav, Brojeshwar Bhowmick** · 2022-05-02

<details>
<summary>Abstract</summary>

Despite the significant progress in recent years, very few of the AI-based talking face generation methods attempt to render natural emotions. Moreover, the scope of the methods is majorly limited to the characteristics of the training dataset, hence they fail to generalize to arbitrary unseen faces. In this paper, we propose a one-shot facial geometry-aware emotional talking face generation method that can generalize to arbitrary faces. We propose a graph convolutional neural network that uses speech content feature, along with an independent emotion input to generate emotion and speech-induced motion on facial geometry-aware landmark representation. This representation is further used in our optical flow-guided texture generation network for producing the texture. We propose a two-branch texture generation network, with motion and texture branches designed to consider the motion and texture content independently. Compared to the previous emotion talking face methods, our method can adapt to arbitrary faces captured in-the-wild by fine-tuning with only a single image of the target identity in neutral emotion.

</details>

#### [Talking Head Generation Driven by Speech-Related Facial Action Units and Audio- Based on Multimodal Representation Fusion](https://arxiv.org/abs/2204.12756)
**Sen Chen, Zhilei Liu, Jiaxing Liu, Longbiao Wang** · 2022-04-27

<details>
<summary>Abstract</summary>

Talking head generation is to synthesize a lip-synchronized talking head video by inputting an arbitrary face image and corresponding audio clips. Existing methods ignore not only the interaction and relationship of cross-modal information, but also the local driving information of the mouth muscles. In this study, we propose a novel generative framework that contains a dilated non-causal temporal convolutional self-attention network as a multimodal fusion module to promote the relationship learning of cross-modal features. In addition, our proposed method uses both audio- and speech-related facial action units (AUs) as driving information. Speech-related AU information can guide mouth movements more accurately. Because speech is highly correlated with speech-related AUs, we propose an audio-to-AU module to predict speech-related AU information. We utilize pre-trained AU classifier to ensure that the generated images contain correct AU information. We verify the effectiveness of the proposed model on the GRID and TCD-TIMIT datasets. An ablation study is also conducted to verify the contribution of each component. The results of quantitative and qualitative experiments demonstrate that our method outperforms existing methods in terms of both image quality and lip-sync accuracy.

</details>

#### [Dynamic Neural Textures: Generating Talking-Face Videos with Continuously Controllable Expressions](https://arxiv.org/abs/2204.06180)
**Zipeng Ye, Zhiyao Sun, Yu-Hui Wen, Yanan Sun et al.** · 2022-04-13

<details>
<summary>Abstract</summary>

Recently, talking-face video generation has received considerable attention. So far most methods generate results with neutral expressions or expressions that are implicitly determined by neural networks in an uncontrollable way. In this paper, we propose a method to generate talking-face videos with continuously controllable expressions in real-time. Our method is based on an important observation: In contrast to facial geometry of moderate resolution, most expression information lies in textures. Then we make use of neural textures to generate high-quality talking face videos and design a novel neural network that can generate neural textures for image frames (which we called dynamic neural textures) based on the input expression and continuous intensity expression coding (CIEC). Our method uses 3DMM as a 3D model to sample the dynamic neural texture. The 3DMM does not cover the teeth area, so we propose a teeth submodule to complete the details in teeth. Results and an ablation study show the effectiveness of our method in generating high-quality talking-face videos with continuously controllable expressions. We also set up four baseline methods by combining existing representative methods and compare them with our method. Experimental results including a user study show that our method has the best performance.

</details>

#### [Lip to Speech Synthesis with Visual Context Attentional GAN](https://arxiv.org/abs/2204.01726)
**Minsu Kim, Joanna Hong, Y. Ro** · 2022-04-04

<details>
<summary>Abstract</summary>

In this paper, we propose a novel lip-to-speech generative adversarial network, Visual Context Attentional GAN (VCA-GAN), which can jointly model local and global lip movements during speech synthesis. Specifically, the proposed VCA-GAN synthesizes the speech from local lip visual features by finding a mapping function of viseme-to-phoneme, while global visual context is embedded into the intermediate layers of the generator to clarify the ambiguity in the mapping induced by homophene. To achieve this, a visual context attention module is proposed where it encodes global representations from the local visual features, and provides the desired global visual context corresponding to the given coarse speech representation to the generator through audio-visual attention. In addition to the explicit modelling of local and global visual representations, synchronization learning is introduced as a form of contrastive learning that guides the generator to synthesize a speech in sync with the given input lip movements. Extensive experiments demonstrate that the proposed VCA-GAN outperforms existing state-of-the-art and is able to effectively synthesize the speech from multi-speaker that has been barely handled in the previous works.

</details>

#### [End to End Lip Synchronization with a Temporal AutoEncoder](https://arxiv.org/abs/2203.16224)
**Yoav Shalev, Lior Wolf** · 2022-03-30

<details>
<summary>Abstract</summary>

We study the problem of syncing the lip movement in a video with the audio stream. Our solution finds an optimal alignment using a dual-domain recurrent neural network that is trained on synthetic data we generate by dropping and duplicating video frames. Once the alignment is found, we modify the video in order to sync the two sources. Our method is shown to greatly outperform the literature methods on a variety of existing and new benchmarks. As an application, we demonstrate our ability to robustly align text-to-speech generated audio with an existing video stream. Our code and samples are available at https://github.com/itsyoavshalev/End-to-End-Lip-Synchronization-with-a-Temporal-AutoEncoder.

</details>

#### [Expressive Talking Head Video Encoding in StyleGAN2 Latent-Space](https://arxiv.org/abs/2203.14512)
**Trevine Oorloff, Yaser Yacoob** · 2022-03-28

<details>
<summary>Abstract</summary>

While the recent advances in research on video reenactment have yielded promising results, the approaches fall short in capturing the fine, detailed, and expressive facial features (e.g., lip-pressing, mouth puckering, mouth gaping, and wrinkles) which are crucial in generating realistic animated face videos. To this end, we propose an end-to-end expressive face video encoding approach that facilitates data-efficient high-quality video re-synthesis by optimizing low-dimensional edits of a single Identity-latent. The approach builds on StyleGAN2 image inversion and multi-stage non-linear latent-space editing to generate videos that are nearly comparable to input videos. While existing StyleGAN latent-based editing techniques focus on simply generating plausible edits of static images, we automate the latent-space editing to capture the fine expressive facial deformations in a sequence of frames using an encoding that resides in the Style-latent-space (StyleSpace) of StyleGAN2. The encoding thus obtained could be super-imposed on a single Identity-latent to facilitate re-enactment of face videos at $1024^2$. The proposed framework economically captures face identity, head-pose, and complex expressive facial motions at fine levels, and thereby bypasses training, person modeling, dependence on landmarks/ keypoints, and low-resolution synthesis which tend to hamper most re-enactment approaches. The approach is designed with maximum data efficiency, where a single $W+$ latent and 35 parameters per frame enable high-fidelity video rendering. This pipeline can also be used for puppeteering (i.e., motion transfer).

</details>

#### [DialogueNeRF: Towards Realistic Avatar Face-to-Face Conversation Video Generation](https://arxiv.org/abs/2203.07931)
**Yichao Yan, Zanwei Zhou, Zi Wang, Jingnan Gao et al.** · 2022-03-15

<details>
<summary>Abstract</summary>

Conversation is an essential component of virtual avatar activities in the metaverse. With the development of natural language processing, textual and vocal conversation generation has achieved a significant breakthrough. However, face-to-face conversations account for the vast majority of daily conversations, while most existing methods focused on single-person talking head generation. In this work, we take a step further and consider generating realistic face-to-face conversation videos. Conversation generation is more challenging than single-person talking head generation, since it not only requires generating photo-realistic individual talking heads but also demands the listener to respond to the speaker. In this paper, we propose a novel unified framework based on neural radiance field (NeRF) to address this task. Specifically, we model both the speaker and listener with a NeRF framework, with different conditions to control individual expressions. The speaker is driven by the audio signal, while the response of the listener depends on both visual and acoustic information. In this way, face-to-face conversation videos are generated between human avatars, with all the interlocutors modeled within the same network. Moreover, to facilitate future research on this task, we collect a new human conversation dataset containing 34 clips of videos. Quantitative and qualitative experiments evaluate our method in different aspects, e.g., image quality, pose sequence trend, and naturalness of the rendering videos. Experimental results demonstrate that the avatars in the resulting videos are able to perform a realistic conversation, and maintain individual styles. All the code, data, and models will be made publicly available.

</details>

#### [Depth-Aware Generative Adversarial Network for Talking Head Video Generation](https://arxiv.org/abs/2203.06605)
**Fa-Ting Hong, Longhao Zhang, Li Shen, Dan Xu** · 2022-03-13

<details>
<summary>Abstract</summary>

Talking head video generation aims to produce a synthetic human face video that contains the identity and pose information respectively from a given source image and a driving video.Existing works for this task heavily rely on 2D representations (e.g. appearance and motion) learned from the input images. However, dense 3D facial geometry (e.g. pixel-wise depth) is extremely important for this task as it is particularly beneficial for us to essentially generate accurate 3D face structures and distinguish noisy information from the possibly cluttered background. Nevertheless, dense 3D geometry annotations are prohibitively costly for videos and are typically not available for this video generation task. In this paper, we first introduce a self-supervised geometry learning method to automatically recover the dense 3D geometry (i.e.depth) from the face videos without the requirement of any expensive 3D annotation data. Based on the learned dense depth maps, we further propose to leverage them to estimate sparse facial keypoints that capture the critical movement of the human head. In a more dense way, the depth is also utilized to learn 3D-aware cross-modal (i.e. appearance and depth) attention to guide the generation of motion fields for warping source image representations. All these contributions compose a novel depth-aware generative adversarial network (DaGAN) for talking head generation. Extensive experiments conducted demonstrate that our proposed method can generate highly realistic faces, and achieve significant results on the unseen human faces.

</details>

#### [An Audio-Visual Attention Based Multimodal Network for Fake Talking Face Videos Detection](https://arxiv.org/abs/2203.05178)
**Ganglai Wang, Peng Zhang, Lei Xie, Wei Huang et al.** · 2022-03-10

<details>
<summary>Abstract</summary>

DeepFake based digital facial forgery is threatening the public media security, especially when lip manipulation has been used in talking face generation, the difficulty of fake video detection is further improved. By only changing lip shape to match the given speech, the facial features of identity is hard to be discriminated in such fake talking face videos. Together with the lack of attention on audio stream as the prior knowledge, the detection failure of fake talking face generation also becomes inevitable. Inspired by the decision-making mechanism of human multisensory perception system, which enables the auditory information to enhance post-sensory visual evidence for informed decisions output, in this study, a fake talking face detection framework FTFDNet is proposed by incorporating audio and visual representation to achieve more accurate fake talking face videos detection. Furthermore, an audio-visual attention mechanism (AVAM) is proposed to discover more informative features, which can be seamlessly integrated into any audio-visual CNN architectures by modularization. With the additional AVAM, the proposed FTFDNet is able to achieve a better detection performance on the established dataset (FTFDD). The evaluation of the proposed work has shown an excellent performance on the detection of fake talking face videos, which is able to arrive at a detection rate above 97%.

</details>

#### [StyleHEAT: One-Shot High-Resolution Editable Talking Face Generation via Pre-trained StyleGAN](https://arxiv.org/abs/2203.04036)
**Fei Yin, Yong Zhang, Xiaodong Cun, Mingdeng Cao et al.** · 2022-03-08

<details>
<summary>Abstract</summary>

One-shot talking face generation aims at synthesizing a high-quality talking face video from an arbitrary portrait image, driven by a video or an audio segment. One challenging quality factor is the resolution of the output video: higher resolution conveys more details. In this work, we investigate the latent feature space of a pre-trained StyleGAN and discover some excellent spatial transformation properties. Upon the observation, we explore the possibility of using a pre-trained StyleGAN to break through the resolution limit of training datasets. We propose a novel unified framework based on a pre-trained StyleGAN that enables a set of powerful functionalities, i.e., high-resolution video generation, disentangled control by driving video or audio, and flexible face editing. Our framework elevates the resolution of the synthesized talking face to 1024*1024 for the first time, even though the training dataset has a lower resolution. We design a video-based motion generation module and an audio-based one, which can be plugged into the framework either individually or jointly to drive the video generation. The predicted motion is used to transform the latent features of StyleGAN for visual animation. To compensate for the transformation distortion, we propose a calibration network as well as a domain loss to refine the features. Moreover, our framework allows two types of facial editing, i.e., global editing via GAN inversion and intuitive editing based on 3D morphable models. Comprehensive experiments show superior video quality, flexible controllability, and editability over state-of-the-art methods.

</details>

#### [FSGANv2: Improved Subject Agnostic Face Swapping and Reenactment](https://arxiv.org/abs/2202.12972)
**Yuval Nirkin, Yosi Keller, Tal Hassner** · 2022-02-25

<details>
<summary>Abstract</summary>

We present Face Swapping GAN (FSGAN) for face swapping and reenactment. Unlike previous work, we offer a subject agnostic swapping scheme that can be applied to pairs of faces without requiring training on those faces. We derive a novel iterative deep learning--based approach for face reenactment which adjusts significant pose and expression variations that can be applied to a single image or a video sequence. For video sequences, we introduce a continuous interpolation of the face views based on reenactment, Delaunay Triangulation, and barycentric coordinates. Occluded face regions are handled by a face completion network. Finally, we use a face blending network for seamless blending of the two faces while preserving the target skin color and lighting conditions. This network uses a novel Poisson blending loss combining Poisson optimization with a perceptual loss. We compare our approach to existing state-of-the-art systems and show our results to be both qualitatively and quantitatively superior. This work describes extensions of the FSGAN method, proposed in an earlier conference version of our work, as well as additional experiments and results.

</details>

#### [Thinking the Fusion Strategy of Multi-reference Face Reenactment](https://arxiv.org/abs/2202.10758)
**Takuya Yashima, Takuya Narihira, Tamaki Kojima** · 2022-02-22

<details>
<summary>Abstract</summary>

In recent advances of deep generative models, face reenactment -manipulating and controlling human face, including their head movement-has drawn much attention for its wide range of applicability. Despite its strong expressiveness, it is inevitable that the models fail to reconstruct or accurately generate unseen side of the face of a given single reference image. Most of existing methods alleviate this problem by learning appearances of human faces from large amount of data and generate realistic texture at inference time. Rather than completely relying on what generative models learn, we show that simple extension by using multiple reference images significantly improves generation quality. We show this by 1) conducting the reconstruction task on publicly available dataset, 2) conducting facial motion transfer on our original dataset which consists of multi-person's head movement video sequences, and 3) using a newly proposed evaluation metric to validate that our method achieves better quantitative results.

</details>

#### [The impact of removing head movements on audio-visual speech enhancement](https://arxiv.org/abs/2202.00538)
**Zhiqi Kang, Mostafa Sadeghi, Radu Horaud, Xavier Alameda-Pineda et al.** · 2022-02-01

<details>
<summary>Abstract</summary>

This paper investigates the impact of head movements on audio-visual speech enhancement (AVSE). Although being a common conversational feature, head movements have been ignored by past and recent studies: they challenge today's learning-based methods as they often degrade the performance of models that are trained on clean, frontal, and steady face images. To alleviate this problem, we propose to use robust face frontalization (RFF) in combination with an AVSE method based on a variational auto-encoder (VAE) model. We briefly describe the basic ingredients of the proposed pipeline and we perform experiments with a recently released audio-visual dataset. In the light of these experiments, and based on three standard metrics, namely STOI, PESQ and SI-SDR, we conclude that RFF improves the performance of AVSE by a considerable margin.

</details>

#### [Finding Directions in GAN's Latent Space for Neural Face Reenactment](https://arxiv.org/abs/2202.00046)
**Stella Bounareli, Vasileios Argyriou, Georgios Tzimiropoulos** · 2022-01-31

<details>
<summary>Abstract</summary>

This paper is on face/head reenactment where the goal is to transfer the facial pose (3D head orientation and expression) of a target face to a source face. Previous methods focus on learning embedding networks for identity and pose disentanglement which proves to be a rather hard task, degrading the quality of the generated images. We take a different approach, bypassing the training of such networks, by using (fine-tuned) pre-trained GANs which have been shown capable of producing high-quality facial images. Because GANs are characterized by weak controllability, the core of our approach is a method to discover which directions in latent GAN space are responsible for controlling facial pose and expression variations. We present a simple pipeline to learn such directions with the aid of a 3D shape model which, by construction, already captures disentangled directions for facial pose, identity and expression. Moreover, we show that by embedding real images in the GAN latent space, our method can be successfully used for the reenactment of real-world faces. Our method features several favorable properties including using a single source image (one-shot) and enabling cross-person reenactment. Our qualitative and quantitative results show that our approach often produces reenacted faces of significantly higher quality than those produced by state-of-the-art methods for the standard benchmarks of VoxCeleb1 & 2. Source code is available at: https://github.com/StelaBou/stylegan_directions_face_reenactment

</details>

#### [Stitch it in Time: GAN-Based Facial Editing of Real Videos](https://arxiv.org/abs/2201.08361)
**Rotem Tzaban, Ron Mokady, Rinon Gal, Amit H. Bermano et al.** · 2022-01-20

<details>
<summary>Abstract</summary>

The ability of Generative Adversarial Networks to encode rich semantics within their latent space has been widely adopted for facial image editing. However, replicating their success with videos has proven challenging. Sets of high-quality facial videos are lacking, and working with videos introduces a fundamental barrier to overcome - temporal coherency. We propose that this barrier is largely artificial. The source video is already temporally coherent, and deviations from this state arise in part due to careless treatment of individual components in the editing pipeline. We leverage the natural alignment of StyleGAN and the tendency of neural networks to learn low frequency functions, and demonstrate that they provide a strongly consistent prior. We draw on these insights and propose a framework for semantic editing of faces in videos, demonstrating significant improvements over the current state-of-the-art. Our method produces meaningful face manipulations, maintains a higher degree of temporal consistency, and can be applied to challenging, high quality, talking head videos which current methods struggle with.

</details>

#### [Leveraging Real Talking Faces via Self-Supervision for Robust Forgery Detection](https://arxiv.org/abs/2201.07131)
**Alexandros Haliassos, Rodrigo Mira, Stavros Petridis, Maja Pantic** · 2022-01-18

<details>
<summary>Abstract</summary>

One of the most pressing challenges for the detection of face-manipulated videos is generalising to forgery methods not seen during training while remaining effective under common corruptions such as compression. In this paper, we examine whether we can tackle this issue by harnessing videos of real talking faces, which contain rich information on natural facial appearance and behaviour and are readily available in large quantities online. Our method, termed RealForensics, consists of two stages. First, we exploit the natural correspondence between the visual and auditory modalities in real videos to learn, in a self-supervised cross-modal manner, temporally dense video representations that capture factors such as facial movements, expression, and identity. Second, we use these learned representations as targets to be predicted by our forgery detector along with the usual binary forgery classification task; this encourages it to base its real/fake decision on said factors. We show that our method achieves state-of-the-art performance on cross-manipulation generalisation and robustness experiments, and examine the factors that contribute to its performance. Our results suggest that leveraging natural and unlabelled videos is a promising direction for the development of more robust face forgery detectors.

</details>

#### [Audio-Driven Talking Face Video Generation with Dynamic Convolution Kernels](https://arxiv.org/abs/2201.05986)
**Zipeng Ye, Mengfei Xia, Ran Yi, Juyong Zhang et al.** · 2022-01-16

<details>
<summary>Abstract</summary>

In this paper, we present a dynamic convolution kernel (DCK) strategy for convolutional neural networks. Using a fully convolutional network with the proposed DCKs, high-quality talking-face video can be generated from multi-modal sources (i.e., unmatched audio and video) in real time, and our trained model is robust to different identities, head postures, and input audios. Our proposed DCKs are specially designed for audio-driven talking face video generation, leading to a simple yet effective end-to-end system. We also provide a theoretical analysis to interpret why DCKs work. Experimental results show that our method can generate high-quality talking-face video with background at 60 fps. Comparison and evaluation between our method and the state-of-the-art methods demonstrate the superiority of our method.

</details>

#### [DFA-NeRF: Personalized Talking Head Generation via Disentangled Face Attributes Neural Rendering](https://arxiv.org/abs/2201.00791)
**Shunyu Yao, RuiZhe Zhong, Yichao Yan, Guangtao Zhai et al.** · 2022-01-03

<details>
<summary>Abstract</summary>

While recent advances in deep neural networks have made it possible to render high-quality images, generating photo-realistic and personalized talking head remains challenging. With given audio, the key to tackling this task is synchronizing lip movement and simultaneously generating personalized attributes like head movement and eye blink. In this work, we observe that the input audio is highly correlated to lip motion while less correlated to other personalized attributes (e.g., head movements). Inspired by this, we propose a novel framework based on neural radiance field to pursue high-fidelity and personalized talking head generation. Specifically, neural radiance field takes lip movements features and personalized attributes as two disentangled conditions, where lip movements are directly predicted from the audio inputs to achieve lip-synchronized generation. In the meanwhile, personalized attributes are sampled from a probabilistic model, where we design a Transformer-based variational autoencoder sampled from Gaussian Process to learn plausible and natural-looking head pose and eye blink. Experiments on several benchmarks demonstrate that our method achieves significantly better results than state-of-the-art methods.

</details>

#### [Towards audio-visual deep learning methods for singing voice separation and lip synchronization](https://www.semanticscholar.org/paper/0a429a0cd79b2ce508f30550aba98dd8fb2289fa)
**V. S. Kadandale** · 2022-01-01


</details>

<details open>
<summary><h3>2021</h3></summary>

#### [Initiative Defense against Facial Manipulation](https://arxiv.org/abs/2112.10098)
**Qidong Huang, Jie Zhang, Wenbo Zhou, WeimingZhang et al.** · 2021-12-19

<details>
<summary>Abstract</summary>

Benefiting from the development of generative adversarial networks (GAN), facial manipulation has achieved significant progress in both academia and industry recently. It inspires an increasing number of entertainment applications but also incurs severe threats to individual privacy and even political security meanwhile. To mitigate such risks, many countermeasures have been proposed. However, the great majority methods are designed in a passive manner, which is to detect whether the facial images or videos are tampered after their wide propagation. These detection-based methods have a fatal limitation, that is, they only work for ex-post forensics but can not prevent the engendering of malicious behavior. To address the limitation, in this paper, we propose a novel framework of initiative defense to degrade the performance of facial manipulation models controlled by malicious users. The basic idea is to actively inject imperceptible venom into target facial data before manipulation. To this end, we first imitate the target manipulation model with a surrogate model, and then devise a poison perturbation generator to obtain the desired venom. An alternating training strategy are further leveraged to train both the surrogate model and the perturbation generator. Two typical facial manipulation tasks: face attribute editing and face reenactment, are considered in our initiative defense framework. Extensive experiments demonstrate the effectiveness and robustness of our framework in different settings. Finally, we hope this work can shed some light on initiative countermeasures against more adversarial scenarios.

</details>

#### [Towards Robust Real-time Audio-Visual Speech Enhancement](https://arxiv.org/abs/2112.09060)
**Mandar Gogate, Kia Dashtipour, Amir Hussain** · 2021-12-16

<details>
<summary>Abstract</summary>

The human brain contextually exploits heterogeneous sensory information to efficiently perform cognitive tasks including vision and hearing. For example, during the cocktail party situation, the human auditory cortex contextually integrates audio-visual (AV) cues in order to better perceive speech. Recent studies have shown that AV speech enhancement (SE) models can significantly improve speech quality and intelligibility in very low signal to noise ratio (SNR) environments as compared to audio-only SE models. However, despite significant research in the area of AV SE, development of real-time processing models with low latency remains a formidable technical challenge. In this paper, we present a novel framework for low latency speaker-independent AV SE that can generalise on a range of visual and acoustic noises. In particular, a generative adversarial networks (GAN) is proposed to address the practical issue of visual imperfections in AV SE. In addition, we propose a deep neural network based real-time AV SE model that takes into account the cleaned visual speech output from GAN to deliver more robust SE. The proposed framework is evaluated on synthetic and real noisy AV corpora using objective speech quality and intelligibility metrics and subjective listing tests. Comparative simulation results show that our real time AV SE framework outperforms state-of-the-art SE approaches, including recent DNN based SE models.

</details>

#### [One-shot Talking Face Generation from Single-speaker Audio-Visual Correlation Learning](https://arxiv.org/abs/2112.02749)
**Suzhen Wang, Lincheng Li, Yu Ding, Xin Yu** · 2021-12-06

<details>
<summary>Abstract</summary>

Audio-driven one-shot talking face generation methods are usually trained on video resources of various persons. However, their created videos often suffer unnatural mouth shapes and asynchronous lips because those methods struggle to learn a consistent speech style from different speakers. We observe that it would be much easier to learn a consistent speech style from a specific speaker, which leads to authentic mouth movements. Hence, we propose a novel one-shot talking face generation framework by exploring consistent correlations between audio and visual motions from a specific speaker and then transferring audio-driven motion fields to a reference image. Specifically, we develop an Audio-Visual Correlation Transformer (AVCT) that aims to infer talking motions represented by keypoint based dense motion fields from an input audio. In particular, considering audio may come from different identities in deployment, we incorporate phonemes to represent audio signals. In this manner, our AVCT can inherently generalize to audio spoken by other identities. Moreover, as face keypoints are used to represent speakers, AVCT is agnostic against appearances of the training speaker, and thus allows us to manipulate face images of different identities readily. Considering different face shapes lead to different motions, a motion field transfer module is exploited to reduce the audio-driven dense motion field gap between the training identity and the one-shot reference. Once we obtained the dense motion field of the reference image, we employ an image renderer to generate its talking face videos from an audio clip. Thanks to our learned consistent speaking style, our method generates authentic mouth shapes and vivid movements. Extensive experiments demonstrate that our synthesized videos outperform the state-of-the-art in terms of visual quality and lip-sync.

</details>

#### [Towards Intelligibility-Oriented Audio-Visual Speech Enhancement](https://arxiv.org/abs/2111.09642)
**Tassadaq Hussain, Mandar Gogate, Kia Dashtipour, Amir Hussain** · 2021-11-18

<details>
<summary>Abstract</summary>

Existing deep learning (DL) based speech enhancement approaches are generally optimised to minimise the distance between clean and enhanced speech features. These often result in improved speech quality however they suffer from a lack of generalisation and may not deliver the required speech intelligibility in real noisy situations. In an attempt to address these challenges, researchers have explored intelligibility-oriented (I-O) loss functions and integration of audio-visual (AV) information for more robust speech enhancement (SE). In this paper, we introduce DL based I-O SE algorithms exploiting AV information, which is a novel and previously unexplored research direction. Specifically, we present a fully convolutional AV SE model that uses a modified short-time objective intelligibility (STOI) metric as a training cost function. To the best of our knowledge, this is the first work that exploits the integration of AV modalities with an I-O based loss function for SE. Comparative experimental results demonstrate that our proposed I-O AV SE framework outperforms audio-only (AO) and AV models trained with conventional distance-based loss functions, in terms of standard objective evaluation measures when dealing with unseen speakers and noises.

</details>

#### [Talking Head Generation with Audio and Speech Related Facial Action Units](https://arxiv.org/abs/2110.09951)
**Sen Chen, Zhilei Liu, Jiaxing Liu, Zhengxiang Yan et al.** · 2021-10-19

<details>
<summary>Abstract</summary>

The task of talking head generation is to synthesize a lip synchronized talking head video by inputting an arbitrary face image and audio clips. Most existing methods ignore the local driving information of the mouth muscles. In this paper, we propose a novel recurrent generative network that uses both audio and speech-related facial action units (AUs) as the driving information. AU information related to the mouth can guide the movement of the mouth more accurately. Since speech is highly correlated with speech-related AUs, we propose an Audio-to-AU module in our system to predict the speech-related AU information from speech. In addition, we use AU classifier to ensure that the generated images contain correct AU information. Frame discriminator is also constructed for adversarial training to improve the realism of the generated face. We verify the effectiveness of our model on the GRID dataset and TCD-TIMIT dataset. We also conduct an ablation study to verify the contribution of each component in our model. Quantitative and qualitative experiments demonstrate that our method outperforms existing methods in both image quality and lip-sync accuracy.

</details>

#### [FACIAL: Synthesizing Dynamic Talking Face with Implicit Attribute Learning](https://arxiv.org/abs/2108.07938)
**Chenxu Zhang, Yifan Zhao, Yifei Huang, Ming Zeng et al.** · 2021-08-18

<details>
<summary>Abstract</summary>

In this paper, we propose a talking face generation method that takes an audio signal as input and a short target video clip as reference, and synthesizes a photo-realistic video of the target face with natural lip motions, head poses, and eye blinks that are in-sync with the input audio signal. We note that the synthetic face attributes include not only explicit ones such as lip motions that have high correlations with speech, but also implicit ones such as head poses and eye blinks that have only weak correlation with the input audio. To model such complicated relationships among different face attributes with input audio, we propose a FACe Implicit Attribute Learning Generative Adversarial Network (FACIAL-GAN), which integrates the phonetics-aware, context-aware, and identity-aware information to synthesize the 3D face animation with realistic motions of lips, head poses, and eye blinks. Then, our Rendering-to-Video network takes the rendered face images and the attention map of eye blinks as input to generate the photo-realistic output video frames. Experimental results and user studies show our method can generate realistic talking face videos with not only synchronized lip motions, but also natural head movements and eye blinks, with better qualities than the results of state-of-the-art methods.

</details>

#### [UniFaceGAN: A Unified Framework for Temporally Consistent Facial Video Editing](https://arxiv.org/abs/2108.05650)
**Meng Cao, Haozhi Huang, Hao Wang, Xuan Wang et al.** · 2021-08-12

<details>
<summary>Abstract</summary>

Recent research has witnessed advances in facial image editing tasks including face swapping and face reenactment. However, these methods are confined to dealing with one specific task at a time. In addition, for video facial editing, previous methods either simply apply transformations frame by frame or utilize multiple frames in a concatenated or iterative fashion, which leads to noticeable visual flickers. In this paper, we propose a unified temporally consistent facial video editing framework termed UniFaceGAN. Based on a 3D reconstruction model and a simple yet efficient dynamic training sample selection mechanism, our framework is designed to handle face swapping and face reenactment simultaneously. To enforce the temporal consistency, a novel 3D temporal loss constraint is introduced based on the barycentric coordinate interpolation. Besides, we propose a region-aware conditional normalization layer to replace the traditional AdaIN or SPADE to synthesize more context-harmonious results. Compared with the state-of-the-art facial image editing methods, our framework generates video portraits that are more photo-realistic and temporally smooth.

</details>

#### [FakeAVCeleb: A Novel Audio-Video Multimodal Deepfake Dataset](https://arxiv.org/abs/2108.05080)
**Hasam Khalid, Shahroz Tariq, Minha Kim, Simon S. Woo** · 2021-08-11

<details>
<summary>Abstract</summary>

While the significant advancements have made in the generation of deepfakes using deep learning technologies, its misuse is a well-known issue now. Deepfakes can cause severe security and privacy issues as they can be used to impersonate a person's identity in a video by replacing his/her face with another person's face. Recently, a new problem of generating synthesized human voice of a person is emerging, where AI-based deep learning models can synthesize any person's voice requiring just a few seconds of audio. With the emerging threat of impersonation attacks using deepfake audios and videos, a new generation of deepfake detectors is needed to focus on both video and audio collectively. To develop a competent deepfake detector, a large amount of high-quality data is typically required to capture real-world (or practical) scenarios. Existing deepfake datasets either contain deepfake videos or audios, which are racially biased as well. As a result, it is critical to develop a high-quality video and audio deepfake dataset that can be used to detect both audio and video deepfakes simultaneously. To fill this gap, we propose a novel Audio-Video Deepfake dataset, FakeAVCeleb, which contains not only deepfake videos but also respective synthesized lip-synced fake audios. We generate this dataset using the most popular deepfake generation methods. We selected real YouTube videos of celebrities with four ethnic backgrounds to develop a more realistic multimodal dataset that addresses racial bias, and further help develop multimodal deepfake detectors. We performed several experiments using state-of-the-art detection methods to evaluate our deepfake dataset and demonstrate the challenges and usefulness of our multimodal Audio-Video deepfake dataset.

</details>

#### [Audio2Head: Audio-driven One-shot Talking-head Generation with Natural Head Motion](https://arxiv.org/abs/2107.09293)
**Suzhen Wang, Lincheng Li, Yu Ding, Changjie Fan et al.** · 2021-07-20

<details>
<summary>Abstract</summary>

We propose an audio-driven talking-head method to generate photo-realistic talking-head videos from a single reference image. In this work, we tackle two key challenges: (i) producing natural head motions that match speech prosody, and (ii) maintaining the appearance of a speaker in a large head motion while stabilizing the non-face regions. We first design a head pose predictor by modeling rigid 6D head movements with a motion-aware recurrent neural network (RNN). In this way, the predicted head poses act as the low-frequency holistic movements of a talking head, thus allowing our latter network to focus on detailed facial movement generation. To depict the entire image motions arising from audio, we exploit a keypoint based dense motion field representation. Then, we develop a motion field generator to produce the dense motion fields from input audio, head poses, and a reference image. As this keypoint based representation models the motions of facial regions, head, and backgrounds integrally, our method can better constrain the spatial and temporal consistency of the generated videos. Finally, an image generation network is employed to render photo-realistic talking-head videos from the estimated keypoint based motion fields and the input reference image. Extensive experiments demonstrate that our method produces videos with plausible head motions, synchronized facial expressions, and stable backgrounds and outperforms the state-of-the-art.

</details>

#### [Speech2Video: Cross-Modal Distillation for Speech to Video Generation](https://arxiv.org/abs/2107.04806)
**Shijing Si, Jianzong Wang, Xiaoyang Qu, Ning Cheng et al.** · 2021-07-10

<details>
<summary>Abstract</summary>

This paper investigates a novel task of talking face video generation solely from speeches. The speech-to-video generation technique can spark interesting applications in entertainment, customer service, and human-computer-interaction industries. Indeed, the timbre, accent and speed in speeches could contain rich information relevant to speakers' appearance. The challenge mainly lies in disentangling the distinct visual attributes from audio signals. In this article, we propose a light-weight, cross-modal distillation method to extract disentangled emotional and identity information from unlabelled video inputs. The extracted features are then integrated by a generative adversarial network into talking face video clips. With carefully crafted discriminators, the proposed framework achieves realistic generation results. Experiments with observed individuals demonstrated that the proposed framework captures the emotional expressions solely from speeches, and produces spontaneous facial motion in the video output. Compared to the baseline method where speeches are combined with a static image of the speaker, the results of the proposed framework is almost indistinguishable. User studies also show that the proposed method outperforms the existing algorithms in terms of emotion expression in the generated videos.

</details>

#### [Multi-modality Deep Restoration of Extremely Compressed Face Videos](https://arxiv.org/abs/2107.05548)
**Xi Zhang, Xiaolin Wu** · 2021-07-05

<details>
<summary>Abstract</summary>

Arguably the most common and salient object in daily video communications is the talking head, as encountered in social media, virtual classrooms, teleconferences, news broadcasting, talk shows, etc. When communication bandwidth is limited by network congestions or cost effectiveness, compression artifacts in talking head videos are inevitable. The resulting video quality degradation is highly visible and objectionable due to high acuity of human visual system to faces. To solve this problem, we develop a multi-modality deep convolutional neural network method for restoring face videos that are aggressively compressed. The main innovation is a new DCNN architecture that incorporates known priors of multiple modalities: the video-synchronized speech signal and semantic elements of the compression code stream, including motion vectors, code partition map and quantization parameters. These priors strongly correlate with the latent video and hence they are able to enhance the capability of deep learning to remove compression artifacts. Ample empirical evidences are presented to validate the superior performance of the proposed DCNN method on face videos over the existing state-of-the-art methods.

</details>

#### [Txt2Vid: Ultra-Low Bitrate Compression of Talking-Head Videos via Text](https://arxiv.org/abs/2106.14014)
**Pulkit Tandon, Shubham Chandak, Pat Pataranutaporn, Yimeng Liu et al.** · 2021-06-26

<details>
<summary>Abstract</summary>

Video represents the majority of internet traffic today, driving a continual race between the generation of higher quality content, transmission of larger file sizes, and the development of network infrastructure. In addition, the recent COVID-19 pandemic fueled a surge in the use of video conferencing tools. Since videos take up considerable bandwidth (~100 Kbps to a few Mbps), improved video compression can have a substantial impact on network performance for live and pre-recorded content, providing broader access to multimedia content worldwide. We present a novel video compression pipeline, called Txt2Vid, which dramatically reduces data transmission rates by compressing webcam videos ("talking-head videos") to a text transcript. The text is transmitted and decoded into a realistic reconstruction of the original video using recent advances in deep learning based voice cloning and lip syncing models. Our generative pipeline achieves two to three orders of magnitude reduction in the bitrate as compared to the standard audio-video codecs (encoders-decoders), while maintaining equivalent Quality-of-Experience based on a subjective evaluation by users (n = 242) in an online study. The Txt2Vid framework opens up the potential for creating novel applications such as enabling audio-video communication during poor internet connectivity, or in remote terrains with limited bandwidth. The code for this work is available at https://github.com/tpulkit/txt2vid.git.

</details>

#### [Selective Listening by Synchronizing Speech with Lips](https://arxiv.org/abs/2106.07150)
**Zexu Pan, Ruijie Tao, Chenglin Xu, Haizhou Li** · 2021-06-14

<details>
<summary>Abstract</summary>

A speaker extraction algorithm seeks to extract the speech of a target speaker from a multi-talker speech mixture when given a cue that represents the target speaker, such as a pre-enrolled speech utterance, or an accompanying video track. Visual cues are particularly useful when a pre-enrolled speech is not available. In this work, we don't rely on the target speaker's pre-enrolled speech, but rather use the target speaker's face track as the speaker cue, that is referred to as the auxiliary reference, to form an attractor towards the target speaker. We advocate that the temporal synchronization between the speech and its accompanying lip movements is a direct and dominant audio-visual cue. Therefore, we propose a self-supervised pre-training strategy, to exploit the speech-lip synchronization cue for target speaker extraction, which allows us to leverage abundant unlabeled in-domain data. We transfer the knowledge from the pre-trained model to the attractor encoder of the speaker extraction network. We show that the proposed speaker extraction network outperforms various competitive baselines in terms of signal quality, perceptual quality, and intelligibility, achieving state-of-the-art performance.

</details>

#### [Learning Pose-Adaptive Lip Sync with Cascaded Temporal Convolutional Network](https://www.semanticscholar.org/paper/81ff564e6318ff01b00f9480ba1456798692201c)
**Ruobing Zheng, Bo Song, Changjiang Ji** · 2021-06-06

<details>
<summary>Abstract</summary>

Speech-driven lip sync has become a promising technique for generating and editing talking-head videos. These studies mainly use 3D morphable models or 2D facial landmarks as the intermediate face representations. However, 2D-based methods have been stagnant recently due to their inability to handle out-of-plane rotations, even though the 2D landmarks have the advantage of fast and accurate extraction. In this paper, we design a cascaded temporal convolutional network to successively generate mouth shapes and corresponding jawlines based on audio signals and template headposes. Instead of explicitly calibrating the rotation between the predicted mouth and the template face, we employ neural networks to learn the pose-adaptive mapping implicitly. We also propose an image-to-image translation-based neural rendering method for producing high-resolution and photo-realistic videos. Experiments show our solution improves both the mapping accuracy and visual performance than baselines. This work could benefit many real-world applications like virtual anchors, telepresence, and conversational agents.

</details>

#### [Text2Video: Text-driven Talking-head Video Synthesis with Personalized Phoneme-Pose Dictionary](https://arxiv.org/abs/2104.14631)
**Sibo Zhang, Jiahong Yuan, Miao Liao, Liangjun Zhang** · 2021-04-29

<details>
<summary>Abstract</summary>

With the advance of deep learning technology, automatic video generation from audio or text has become an emerging and promising research topic. In this paper, we present a novel approach to synthesize video from the text. The method builds a phoneme-pose dictionary and trains a generative adversarial network (GAN) to generate video from interpolated phoneme poses. Compared to audio-driven video generation algorithms, our approach has a number of advantages: 1) It only needs a fraction of the training data used by an audio-driven approach; 2) It is more flexible and not subject to vulnerability due to speaker variation; 3) It significantly reduces the preprocessing, training and inference time. We perform extensive experiments to compare the proposed method with state-of-the-art talking face generation methods on a benchmark dataset and datasets of our own. The results demonstrate the effectiveness and superiority of our approach.

</details>

#### [Learned Spatial Representations for Few-shot Talking-Head Synthesis](https://arxiv.org/abs/2104.14557)
**Moustafa Meshry, Saksham Suri, Larry S. Davis, Abhinav Shrivastava** · 2021-04-29

<details>
<summary>Abstract</summary>

We propose a novel approach for few-shot talking-head synthesis. While recent works in neural talking heads have produced promising results, they can still produce images that do not preserve the identity of the subject in source images. We posit this is a result of the entangled representation of each subject in a single latent code that models 3D shape information, identity cues, colors, lighting and even background details. In contrast, we propose to factorize the representation of a subject into its spatial and style components. Our method generates a target frame in two steps. First, it predicts a dense spatial layout for the target image. Second, an image generator utilizes the predicted layout for spatial denormalization and synthesizes the target frame. We experimentally show that this disentangled representation leads to a significant improvement over previous methods, both quantitatively and qualitatively.

</details>

#### [3D-TalkEmo: Learning to Synthesize 3D Emotional Talking Head](https://arxiv.org/abs/2104.12051)
**Qianyun Wang, Zhenfeng Fan, Shihong Xia** · 2021-04-25

<details>
<summary>Abstract</summary>

Impressive progress has been made in audio-driven 3D facial animation recently, but synthesizing 3D talking-head with rich emotion is still unsolved. This is due to the lack of 3D generative models and available 3D emotional dataset with synchronized audios. To address this, we introduce 3D-TalkEmo, a deep neural network that generates 3D talking head animation with various emotions. We also create a large 3D dataset with synchronized audios and videos, rich corpus, as well as various emotion states of different persons with the sophisticated 3D face reconstruction methods. In the emotion generation network, we propose a novel 3D face representation structure - geometry map by classical multi-dimensional scaling analysis. It maps the coordinates of vertices on a 3D face to a canonical image plane, while preserving the vertex-to-vertex geodesic distance metric in a least-square sense. This maintains the adjacency relationship of each vertex and holds the effective convolutional structure for the 3D facial surface. Taking a neutral 3D mesh and a speech signal as inputs, the 3D-TalkEmo is able to generate vivid facial animations. Moreover, it provides access to change the emotion state of the animated speaker. We present extensive quantitative and qualitative evaluation of our method, in addition to user studies, demonstrating the generated talking-heads of significantly higher quality compared to previous state-of-the-art methods.

</details>

#### [A cappella: Audio-visual Singing Voice Separation](https://arxiv.org/abs/2104.09946)
**Juan F. Montesinos, Venkatesh S. Kadandale, Gloria Haro** · 2021-04-20

<details>
<summary>Abstract</summary>

The task of isolating a target singing voice in music videos has useful applications. In this work, we explore the single-channel singing voice separation problem from a multimodal perspective, by jointly learning from audio and visual modalities. To do so, we present Acappella, a dataset spanning around 46 hours of a cappella solo singing videos sourced from YouTube. We also propose an audio-visual convolutional network based on graphs which achieves state-of-the-art singing voice separation results on our dataset and compare it against its audio-only counterpart, U-Net, and a state-of-the-art audio-visual speech separation model. We evaluate the models in the following challenging setups: i) presence of overlapping voices in the audio mixtures, ii) the target voice set to lower volume levels in the mix, and iii) combination of i) and ii). The third one being the most challenging evaluation setup. We demonstrate that our model outperforms the baseline models in the singing voice separation task in the most challenging evaluation setup. The code, the pre-trained models, and the dataset are publicly available at https://ipcv.github.io/Acappella/able at https://ipcv.github.io/Acappella/

</details>

#### [Single Source One Shot Reenactment using Weighted motion From Paired Feature Points](https://arxiv.org/abs/2104.03117)
**Soumya Tripathy, Juho Kannala, Esa Rahtu** · 2021-04-07

<details>
<summary>Abstract</summary>

Image reenactment is a task where the target object in the source image imitates the motion represented in the driving image. One of the most common reenactment tasks is face image animation. The major challenge in the current face reenactment approaches is to distinguish between facial motion and identity. For this reason, the previous models struggle to produce high-quality animations if the driving and source identities are different (cross-person reenactment). We propose a new (face) reenactment model that learns shape-independent motion features in a self-supervised setup. The motion is represented using a set of paired feature points extracted from the source and driving images simultaneously. The model is generalised to multiple reenactment tasks including faces and non-face objects using only a single source image. The extensive experiments show that the model faithfully transfers the driving motion to the source while retaining the source identity intact.

</details>

#### [LI-Net: Large-Pose Identity-Preserving Face Reenactment Network](https://arxiv.org/abs/2104.02850)
**Jin Liu, Peng Chen, Tao Liang, Zhaoxing Li et al.** · 2021-04-07

<details>
<summary>Abstract</summary>

Face reenactment is a challenging task, as it is difficult to maintain accurate expression, pose and identity simultaneously. Most existing methods directly apply driving facial landmarks to reenact source faces and ignore the intrinsic gap between two identities, resulting in the identity mismatch issue. Besides, they neglect the entanglement of expression and pose features when encoding driving faces, leading to inaccurate expressions and visual artifacts on large-pose reenacted faces. To address these problems, we propose a Large-pose Identity-preserving face reenactment network, LI-Net. Specifically, the Landmark Transformer is adopted to adjust driving landmark images, which aims to narrow the identity gap between driving and source landmark images. Then the Face Rotation Module and the Expression Enhancing Generator decouple the transformed landmark image into pose and expression features, and reenact those attributes separately to generate identity-preserving faces with accurate expressions and poses. Both qualitative and quantitative experimental results demonstrate the superiority of our method.

</details>

#### [Looking into Your Speech: Learning Cross-modal Affinity for Audio-visual Speech Separation](https://arxiv.org/abs/2104.02775)
**Jiyoung Lee, Soo-Whan Chung, Sunok Kim, Hong-Goo Kang et al.** · 2021-03-25

<details>
<summary>Abstract</summary>

In this paper, we address the problem of separating individual speech signals from videos using audio-visual neural processing. Most conventional approaches utilize frame-wise matching criteria to extract shared information between co-occurring audio and video. Thus, their performance heavily depends on the accuracy of audio-visual synchronization and the effectiveness of their representations. To overcome the frame discontinuity problem between two modalities due to transmission delay mismatch or jitter, we propose a cross-modal affinity network (CaffNet) that learns global correspondence as well as locally-varying affinities between audio and visual streams. Given that the global term provides stability over a temporal sequence at the utterance-level, this resolves the label permutation problem characterized by inconsistent assignments. By extending the proposed cross-modal affinity on the complex network, we further improve the separation performance in the complex spectral domain. Experimental results verify that the proposed methods outperform conventional ones on various datasets, demonstrating their advantages in real-world scenarios.

</details>

#### [AD-NeRF: Audio Driven Neural Radiance Fields for Talking Head Synthesis](https://arxiv.org/abs/2103.11078)
**Yudong Guo, Keyu Chen, Sen Liang, Yong-Jin Liu et al.** · 2021-03-20

<details>
<summary>Abstract</summary>

Generating high-fidelity talking head video by fitting with the input audio sequence is a challenging problem that receives considerable attentions recently. In this paper, we address this problem with the aid of neural scene representation networks. Our method is completely different from existing methods that rely on intermediate representations like 2D landmarks or 3D face models to bridge the gap between audio input and video output. Specifically, the feature of input audio signal is directly fed into a conditional implicit function to generate a dynamic neural radiance field, from which a high-fidelity talking-head video corresponding to the audio signal is synthesized using volume rendering. Another advantage of our framework is that not only the head (with hair) region is synthesized as previous methods did, but also the upper body is generated via two individual neural radiance fields. Experimental results demonstrate that our novel framework can (1) produce high-fidelity and natural results, and (2) support free adjustment of audio signals, viewing directions, and background images. Code is available at https://github.com/YudongGuo/AD-NeRF.

</details>

#### [One Shot Audio to Animated Video Generation](https://arxiv.org/abs/2102.09737)
**Neeraj Kumar, Srishti Goel, Ankur Narang, Brejesh Lall et al.** · 2021-02-19

<details>
<summary>Abstract</summary>

We consider the challenging problem of audio to animated video generation. We propose a novel method OneShotAu2AV to generate an animated video of arbitrary length using an audio clip and a single unseen image of a person as an input. The proposed method consists of two stages. In the first stage, OneShotAu2AV generates the talking-head video in the human domain given an audio and a person's image. In the second stage, the talking-head video from the human domain is converted to the animated domain. The model architecture of the first stage consists of spatially adaptive normalization based multi-level generator and multiple multilevel discriminators along with multiple adversarial and non-adversarial losses. The second stage leverages attention based normalization driven GAN architecture along with temporal predictor based recycle loss and blink loss coupled with lipsync loss, for unsupervised generation of animated video. In our approach, the input audio clip is not restricted to any specific language, which gives the method multilingual applicability. OneShotAu2AV can generate animated videos that have: (a) lip movements that are in sync with the audio, (b) natural facial expressions such as blinks and eyebrow movements, (c) head movements. Experimental evaluation demonstrates superior performance of OneShotAu2AV as compared to U-GAT-IT and RecycleGan on multiple quantitative metrics including KID(Kernel Inception Distance), Word error rate, blinks/sec

</details>

#### [Switching Variational Auto-Encoders for Noise-Agnostic Audio-visual Speech Enhancement](https://arxiv.org/abs/2102.04144)
**Mostafa Sadeghi, Xavier Alameda-Pineda** · 2021-02-08

<details>
<summary>Abstract</summary>

Recently, audio-visual speech enhancement has been tackled in the unsupervised settings based on variational auto-encoders (VAEs), where during training only clean data is used to train a generative model for speech, which at test time is combined with a noise model, e.g. nonnegative matrix factorization (NMF), whose parameters are learned without supervision. Consequently, the proposed model is agnostic to the noise type. When visual data are clean, audio-visual VAE-based architectures usually outperform the audio-only counterpart. The opposite happens when the visual data are corrupted by clutter, e.g. the speaker not facing the camera. In this paper, we propose to find the optimal combination of these two architectures through time. More precisely, we introduce the use of a latent sequential variable with Markovian dependencies to switch between different VAE architectures through time in an unsupervised manner: leading to switching variational auto-encoder (SwVAE). We propose a variational factorization to approximate the computationally intractable posterior distribution. We also derive the corresponding variational expectation-maximization algorithm to estimate the parameters of the model and enhance the speech signal. Our experiments demonstrate the promising performance of SwVAE.

</details>

#### [One-shot Face Reenactment Using Appearance Adaptive Normalization](https://arxiv.org/abs/2102.03984)
**Guangming Yao, Yi Yuan, Tianjia Shao, Shuang Li et al.** · 2021-02-08

<details>
<summary>Abstract</summary>

The paper proposes a novel generative adversarial network for one-shot face reenactment, which can animate a single face image to a different pose-and-expression (provided by a driving image) while keeping its original appearance. The core of our network is a novel mechanism called appearance adaptive normalization, which can effectively integrate the appearance information from the input image into our face generator by modulating the feature maps of the generator using the learned adaptive parameters. Furthermore, we specially design a local net to reenact the local facial components (i.e., eyes, nose and mouth) first, which is a much easier task for the network to learn and can in turn provide explicit anchors to guide our face generator to learn the global appearance and pose-and-expression. Extensive quantitative and qualitative experiments demonstrate the significant efficacy of our model compared with prior one-shot methods.

</details>

#### [AMFFCN: Attentional Multi-layer Feature Fusion Convolution Network for Audio-visual Speech Enhancement](https://arxiv.org/abs/2101.06268)
**Xinmeng Xu, Jianjun Hao** · 2021-01-15

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement system is regarded to be one of promising solutions for isolating and enhancing speech of desired speaker. Conventional methods focus on predicting clean speech spectrum via a naive convolution neural network based encoder-decoder architecture, and these methods a) not adequate to use data fully and effectively, b) cannot process features selectively. The proposed model addresses these drawbacks, by a) applying a model that fuses audio and visual features layer by layer in encoding phase, and that feeds fused audio-visual features to each corresponding decoder layer, and more importantly, b) introducing soft threshold attention into the model to select the informative modality softly. This paper proposes attentional audio-visual multi-layer feature fusion model, in which soft threshold attention unit are applied on feature mapping at every layer of decoder. The proposed model demonstrates the superior performance of the network against the state-of-the-art models.

</details>

#### [Multi-layer Feature Fusion Convolution Network for Audio-visual Speech Enhancement](https://arxiv.org/abs/2101.05975)
**Xinmeng Xu, Jianjun Hao** · 2021-01-15

<details>
<summary>Abstract</summary>

Speech enhancement can potentially benefit from the visual information from the target speaker, such as lip movement and facial expressions, because the visual aspect of speech is essentially unaffected by acoustic environment. In this paper, we address the problem of enhancing corrupted speech signal from videos by using audio-visual (AV) neural processing. Most of recent AV speech enhancement approaches separately process the acoustic and visual features and fuse them via a simple concatenation operation. Although this strategy is convenient and easy to implement, it comes with two major drawbacks: 1) evidence in speech perception suggests that in humans the AV integration occurs at a very early stage, in contrast to previous models that process the two modalities separately at early stage and combine them only at a later stage, thus making the system less robust, and 2) a simple concatenation does not allow to control how the information from the acoustic and the visual modalities is treated. To overcome these drawbacks, we propose a multi-layer feature fusion convolution network (MFFCN), which separately process acoustic and visual modalities for preserving each modality features while fusing both modalities' features layer by layer in encoding phase for enjoying the human AV speech perception. In addition, considering the balance between the two modalities, we design channel and spectral attention mechanisms to provide additional flexibility in dealing with different types of information expanding the representational ability of the convolution neural network. Experimental results show that the proposed MFFCN demonstrates the performance of the network superior to the state-of-the-art models.

</details>

#### [Fast Facial Landmark Detection and Applications: A Survey](https://arxiv.org/abs/2101.10808)
**Kostiantyn Khabarlak, Larysa Koriashkina** · 2021-01-12

<details>
<summary>Abstract</summary>

Dense facial landmark detection is one of the key elements of face processing pipeline. It is used in virtual face reenactment, emotion recognition, driver status tracking, etc. Early approaches were suitable for facial landmark detection in controlled environments only, which is clearly insufficient. Neural networks have shown an astonishing qualitative improvement for in-the-wild face landmark detection problem, and are now being studied by many researchers in the field. Numerous bright ideas are proposed, often complimentary to each other. However, exploration of the whole volume of novel approaches is quite challenging. Therefore, we present this survey, where we summarize state-of-the-art algorithms into categories, provide a comparison of recently introduced in-the-wild datasets (e.g., 300W, AFLW, COFW, WFLW) that contain images with large pose, face occlusion, taken in unconstrained conditions. In addition to quality, applications require fast inference, and preferably on mobile devices. Hence, we include information about algorithm inference speed both on desktop and mobile hardware, which is rarely studied. Importantly, we highlight problems of algorithms, their applications, vulnerabilities, and briefly touch on established methods. We hope that the reader will find many novel ideas, will see how the algorithms are used in applications, which will enable further research.

</details>

</details>

<details open>
<summary><h3>2020</h3></summary>

#### [Multi Modal Adaptive Normalization for Audio to Video Generation](https://arxiv.org/abs/2012.07304)
**Neeraj Kumar, Srishti Goel, Ankur Narang, Brejesh Lall** · 2020-12-14

<details>
<summary>Abstract</summary>

Speech-driven facial video generation has been a complex problem due to its multi-modal aspects namely audio and video domain. The audio comprises lots of underlying features such as expression, pitch, loudness, prosody(speaking style) and facial video has lots of variability in terms of head movement, eye blinks, lip synchronization and movements of various facial action units along with temporal smoothness. Synthesizing highly expressive facial videos from the audio input and static image is still a challenging task for generative adversarial networks. In this paper, we propose a multi-modal adaptive normalization(MAN) based architecture to synthesize a talking person video of arbitrary length using as input: an audio signal and a single image of a person. The architecture uses the multi-modal adaptive normalization, keypoint heatmap predictor, optical flow predictor and class activation map[58] based layers to learn movements of expressive facial components and hence generates a highly expressive talking-head video of the given person. The multi-modal adaptive normalization uses the various features of audio and video such as Mel spectrogram, pitch, energy from audio signals and predicted keypoint heatmap/optical flow and a single image to learn the respective affine parameters to generate highly expressive video. Experimental evaluation demonstrates superior performance of the proposed method as compared to Realistic Speech-Driven Facial Animation with GANs(RSDGAN) [53], Speech2Vid [10], and other approaches, on multiple quantitative metrics including: SSIM (structural similarity index), PSNR (peak signal to noise ratio), CPBD (image sharpness), WER(word error rate), blinks/sec and LMD(landmark distance). Further, qualitative evaluation and Online Turing tests demonstrate the efficacy of our approach.

</details>

#### [Robust One Shot Audio to Video Generation](https://arxiv.org/abs/2012.07842)
**Neeraj Kumar, Srishti Goel, Ankur Narang, Mujtaba Hasan** · 2020-12-14

<details>
<summary>Abstract</summary>

Audio to Video generation is an interesting problem that has numerous applications across industry verticals including film making, multi-media, marketing, education and others. High-quality video generation with expressive facial movements is a challenging problem that involves complex learning steps for generative adversarial networks. Further, enabling one-shot learning for an unseen single image increases the complexity of the problem while simultaneously making it more applicable to practical scenarios. In the paper, we propose a novel approach OneShotA2V to synthesize a talking person video of arbitrary length using as input: an audio signal and a single unseen image of a person. OneShotA2V leverages curriculum learning to learn movements of expressive facial components and hence generates a high-quality talking-head video of the given person. Further, it feeds the features generated from the audio input directly into a generative adversarial network and it adapts to any given unseen selfie by applying fewshot learning with only a few output updation epochs. OneShotA2V leverages spatially adaptive normalization based multi-level generator and multiple multi-level discriminators based architecture. The input audio clip is not restricted to any specific language, which gives the method multilingual applicability. Experimental evaluation demonstrates superior performance of OneShotA2V as compared to Realistic Speech-Driven Facial Animation with GANs(RSDGAN) [43], Speech2Vid [8], and other approaches, on multiple quantitative metrics including: SSIM (structural similarity index), PSNR (peak signal to noise ratio) and CPBD (image sharpness). Further, qualitative evaluation and Online Turing tests demonstrate the efficacy of our approach.

</details>

#### [An Empirical Study of Visual Features for DNN based Audio-Visual Speech Enhancement in Multi-talker Environments](https://arxiv.org/abs/2011.04359)
**Shrishti Saha Shetu, Soumitro Chakrabarty, Emanuël A. P. Habets** · 2020-11-09

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement (AVSE) methods use both audio and visual features for the task of speech enhancement and the use of visual features has been shown to be particularly effective in multi-speaker scenarios. In the majority of deep neural network (DNN) based AVSE methods, the audio and visual data are first processed separately using different sub-networks, and then the learned features are fused to utilize the information from both modalities. There have been various studies on suitable audio input features and network architectures, however, to the best of our knowledge, there is no published study that has investigated which visual features are best suited for this specific task. In this work, we perform an empirical study of the most commonly used visual features for DNN based AVSE, the pre-processing requirements for each of these features, and investigate their influence on the performance. Our study shows that despite the overall better performance of embedding-based features, their computationally intensive pre-processing make their use difficult in low resource systems. For such systems, optical flow or raw pixels-based features might be better suited.

</details>

#### [FACEGAN: Facial Attribute Controllable rEenactment GAN](https://arxiv.org/abs/2011.04439)
**Soumya Tripathy, Juho Kannala, Esa Rahtu** · 2020-11-09

<details>
<summary>Abstract</summary>

The face reenactment is a popular facial animation method where the person's identity is taken from the source image and the facial motion from the driving image. Recent works have demonstrated high quality results by combining the facial landmark based motion representations with the generative adversarial networks. These models perform best if the source and driving images depict the same person or if the facial structures are otherwise very similar. However, if the identity differs, the driving facial structures leak to the output distorting the reenactment result. We propose a novel Facial Attribute Controllable rEenactment GAN (FACEGAN), which transfers the facial motion from the driving face via the Action Unit (AU) representation. Unlike facial landmarks, the AUs are independent of the facial structure preventing the identity leak. Moreover, AUs provide a human interpretable way to control the reenactment. FACEGAN processes background and face regions separately for optimized output quality. The extensive quantitative and qualitative comparisons show a clear improvement over the state-of-the-art in a single source reenactment task. The results are best illustrated in the reenactment video provided in the supplementary material. The source code will be made available upon publication of the paper.

</details>

#### [Audio-Visual Speech Inpainting with Deep Learning](https://arxiv.org/abs/2010.04556)
**Giovanni Morrone, Daniel Michelsanti, Zheng-Hua Tan, Jesper Jensen** · 2020-10-09

<details>
<summary>Abstract</summary>

In this paper, we present a deep-learning-based framework for audio-visual speech inpainting, i.e., the task of restoring the missing parts of an acoustic speech signal from reliable audio context and uncorrupted visual information. Recent work focuses solely on audio-only methods and generally aims at inpainting music signals, which show highly different structure than speech. Instead, we inpaint speech signals with gaps ranging from 100 ms to 1600 ms to investigate the contribution that vision can provide for gaps of different duration. We also experiment with a multi-task learning approach where a phone recognition task is learned together with speech inpainting. Results show that the performance of audio-only speech inpainting approaches degrades rapidly when gaps get large, while the proposed audio-visual approach is able to plausibly restore missing information. In addition, we show that multi-task learning is effective, although the largest contribution to performance comes from vision.

</details>

#### [Improved Lite Audio-Visual Speech Enhancement](https://arxiv.org/abs/2008.13222)
**Shang-Yi Chuang, Hsin-Min Wang, Yu Tsao** · 2020-08-30

<details>
<summary>Abstract</summary>

Numerous studies have investigated the effectiveness of audio-visual multimodal learning for speech enhancement (AVSE) tasks, seeking a solution that uses visual data as auxiliary and complementary input to reduce the noise of noisy speech signals. Recently, we proposed a lite audio-visual speech enhancement (LAVSE) algorithm for a car-driving scenario. Compared to conventional AVSE systems, LAVSE requires less online computation and to some extent solves the user privacy problem on facial data. In this study, we extend LAVSE to improve its ability to address three practical issues often encountered in implementing AVSE systems, namely, the additional cost of processing visual data, audio-visual asynchronization, and low-quality visual data. The proposed system is termed improved LAVSE (iLAVSE), which uses a convolutional recurrent neural network architecture as the core AVSE model. We evaluate iLAVSE on the Taiwan Mandarin speech with video dataset. Experimental results confirm that compared to conventional AVSE systems, iLAVSE can effectively overcome the aforementioned three practical issues and can improve enhancement performance. The results also confirm that iLAVSE is suitable for real-world scenarios, where high-quality audio-visual sensors may not always be available.

</details>

#### [An Overview of Deep-Learning-Based Audio-Visual Speech Enhancement and Separation](https://arxiv.org/abs/2008.09586)
**Daniel Michelsanti, Zheng-Hua Tan, Shi-Xiong Zhang, Yong Xu et al.** · 2020-08-21

<details>
<summary>Abstract</summary>

Speech enhancement and speech separation are two related tasks, whose purpose is to extract either one or more target speech signals, respectively, from a mixture of sounds generated by several sources. Traditionally, these tasks have been tackled using signal processing and machine learning techniques applied to the available acoustic signals. Since the visual aspect of speech is essentially unaffected by the acoustic environment, visual information from the target speakers, such as lip movements and facial expressions, has also been used for speech enhancement and speech separation systems. In order to efficiently fuse acoustic and visual information, researchers have exploited the flexibility of data-driven approaches, specifically deep learning, achieving strong performance. The ceaseless proposal of a large number of techniques to extract features and fuse multimodal information has highlighted the need for an overview that comprehensively describes and discusses audio-visual speech enhancement and separation based on deep learning. In this paper, we provide a systematic survey of this research topic, focusing on the main elements that characterise the systems in the literature: acoustic features; visual features; deep learning methods; fusion techniques; training targets and objective functions. In addition, we review deep-learning-based methods for speech reconstruction from silent videos and audio-visual sound source separation for non-speech signals, since these methods can be more or less directly applied to audio-visual speech enhancement and separation. Finally, we survey commonly employed audio-visual speech datasets, given their central role in the development of data-driven approaches, and evaluation methods, because they are generally used to compare different systems and determine their performance.

</details>

#### [Deep Variational Generative Models for Audio-visual Speech Separation](https://arxiv.org/abs/2008.07191)
**Viet-Nhat Nguyen, Mostafa Sadeghi, Elisa Ricci, Xavier Alameda-Pineda** · 2020-08-17

<details>
<summary>Abstract</summary>

In this paper, we are interested in audio-visual speech separation given a single-channel audio recording as well as visual information (lips movements) associated with each speaker. We propose an unsupervised technique based on audio-visual generative modeling of clean speech. More specifically, during training, a latent variable generative model is learned from clean speech spectrograms using a variational auto-encoder (VAE). To better utilize the visual information, the posteriors of the latent variables are inferred from mixed speech (instead of clean speech) as well as the visual data. The visual modality also serves as a prior for latent variables, through a visual network. At test time, the learned generative model (both for speaker-independent and speaker-dependent scenarios) is combined with an unsupervised non-negative matrix factorization (NMF) variance model for background noise. All the latent variables and noise parameters are then estimated by a Monte Carlo expectation-maximization algorithm. Our experiments show that the proposed unsupervised VAE-based method yields better separation performance than NMF-based approaches as well as a supervised deep learning-based technique.

</details>

#### [Audiovisual Speech Synthesis using Tacotron2](https://arxiv.org/abs/2008.00620)
**Ahmed Hussen Abdelaziz, Anushree Prasanna Kumar, Chloe Seivwright, Gabriele Fanelli et al.** · 2020-08-03

<details>
<summary>Abstract</summary>

Audiovisual speech synthesis is the problem of synthesizing a talking face while maximizing the coherency of the acoustic and visual speech. In this paper, we propose and compare two audiovisual speech synthesis systems for 3D face models. The first system is the AVTacotron2, which is an end-to-end text-to-audiovisual speech synthesizer based on the Tacotron2 architecture. AVTacotron2 converts a sequence of phonemes representing the sentence to synthesize into a sequence of acoustic features and the corresponding controllers of a face model. The output acoustic features are used to condition a WaveRNN to reconstruct the speech waveform, and the output facial controllers are used to generate the corresponding video of the talking face. The second audiovisual speech synthesis system is modular, where acoustic speech is synthesized from text using the traditional Tacotron2. The reconstructed acoustic speech signal is then used to drive the facial controls of the face model using an independently trained audio-to-facial-animation neural network. We further condition both the end-to-end and modular approaches on emotion embeddings that encode the required prosody to generate emotional audiovisual speech. We analyze the performance of the two systems and compare them to the ground truth videos using subjective evaluation tests. The end-to-end and modular systems are able to synthesize close to human-like audiovisual speech with mean opinion scores (MOS) of 4.1 and 3.9, respectively, compared to a MOS of 4.1 for the ground truth generated from professionally recorded videos. While the end-to-end system gives a better overall quality, the modular approach is more flexible and the quality of acoustic speech and visual speech synthesis is almost independent of each other.

</details>

#### [Deep Multi-modality Soft-decoding of Very Low Bit-rate Face Videos](https://arxiv.org/abs/2008.01652)
**Yanhui Guo, Xi Zhang, Xiaolin Wu** · 2020-08-02

<details>
<summary>Abstract</summary>

We propose a novel deep multi-modality neural network for restoring very low bit rate videos of talking heads. Such video contents are very common in social media, teleconferencing, distance education, tele-medicine, etc., and often need to be transmitted with limited bandwidth. The proposed CNN method exploits the correlations among three modalities, video, audio and emotion state of the speaker, to remove the video compression artifacts caused by spatial down sampling and quantization. The deep learning approach turns out to be ideally suited for the video restoration task, as the complex non-linear cross-modality correlations are very difficult to model analytically and explicitly. The new method is a video post processor that can significantly boost the perceptual quality of aggressively compressed talking head videos, while being fully compatible with all existing video compression standards.

</details>

#### [Talking-head Generation with Rhythmic Head Motion](https://arxiv.org/abs/2007.08547)
**Lele Chen, Guofeng Cui, Celong Liu, Zhong Li et al.** · 2020-07-16

<details>
<summary>Abstract</summary>

When people deliver a speech, they naturally move heads, and this rhythmic head motion conveys prosodic information. However, generating a lip-synced video while moving head naturally is challenging. While remarkably successful, existing works either generate still talkingface videos or rely on landmark/video frames as sparse/dense mapping guidance to generate head movements, which leads to unrealistic or uncontrollable video synthesis. To overcome the limitations, we propose a 3D-aware generative network along with a hybrid embedding module and a non-linear composition module. Through modeling the head motion and facial expressions1 explicitly, manipulating 3D animation carefully, and embedding reference images dynamically, our approach achieves controllable, photo-realistic, and temporally coherent talking-head videos with natural head movements. Thoughtful experiments on several standard benchmarks demonstrate that our method achieves significantly better results than the state-of-the-art methods in both quantitative and qualitative comparisons. The code is available on https://github.com/ lelechen63/Talking-head-Generation-with-Rhythmic-Head-Motion.

</details>

#### [Learning Speech Representations from Raw Audio by Joint Audiovisual Self-Supervision](https://arxiv.org/abs/2007.04134)
**Abhinav Shukla, Stavros Petridis, Maja Pantic** · 2020-07-08

<details>
<summary>Abstract</summary>

The intuitive interaction between the audio and visual modalities is valuable for cross-modal self-supervised learning. This concept has been demonstrated for generic audiovisual tasks like video action recognition and acoustic scene classification. However, self-supervision remains under-explored for audiovisual speech. We propose a method to learn self-supervised speech representations from the raw audio waveform. We train a raw audio encoder by combining audio-only self-supervision (by predicting informative audio attributes) with visual self-supervision (by generating talking faces from audio). The visual pretext task drives the audio representations to capture information related to lip movements. This enriches the audio encoder with visual information and the encoder can be used for evaluation without the visual modality. Our method attains competitive performance with respect to existing self-supervised audio features on established isolated word classification benchmarks, and significantly outperforms other methods at learning from fewer labels. Notably, our method also outperforms fully supervised training, thus providing a strong initialization for speech related tasks. Our results demonstrate the potential of multimodal self-supervision in audiovisual speech for learning good audio representations.

</details>

#### [Modality Dropout for Improved Performance-driven Talking Faces](https://arxiv.org/abs/2005.13616)
**Ahmed Hussen Abdelaziz, Barry-John Theobald, Paul Dixon, Reinhard Knothe et al.** · 2020-05-27

<details>
<summary>Abstract</summary>

We describe our novel deep learning approach for driving animated faces using both acoustic and visual information. In particular, speech-related facial movements are generated using audiovisual information, and non-speech facial movements are generated using only visual information. To ensure that our model exploits both modalities during training, batches are generated that contain audio-only, video-only, and audiovisual input features. The probability of dropping a modality allows control over the degree to which the model exploits audio and visual information during training. Our trained model runs in real-time on resource limited hardware (e.g.\ a smart phone), it is user agnostic, and it is not dependent on a potentially error-prone transcription of the speech. We use subjective testing to demonstrate: 1) the improvement of audiovisual-driven animation over the equivalent video-only approach, and 2) the improvement in the animation of speech-related facial movements after introducing modality dropout. Before introducing dropout, viewers prefer audiovisual-driven animation in 51% of the test sequences compared with only 18% for video-driven. After introducing dropout viewer preference for audiovisual-driven animation increases to 74%, but decreases to 8% for video-only.

</details>

#### [Identity-Preserving Realistic Talking Face Generation](https://arxiv.org/abs/2005.12318)
**Sanjana Sinha, Sandika Biswas, Brojeshwar Bhowmick** · 2020-05-25

<details>
<summary>Abstract</summary>

Speech-driven facial animation is useful for a variety of applications such as telepresence, chatbots, etc. The necessary attributes of having a realistic face animation are 1) audio-visual synchronization (2) identity preservation of the target individual (3) plausible mouth movements (4) presence of natural eye blinks. The existing methods mostly address the audio-visual lip synchronization, and few recent works have addressed the synthesis of natural eye blinks for overall video realism. In this paper, we propose a method for identity-preserving realistic facial animation from speech. We first generate person-independent facial landmarks from audio using DeepSpeech features for invariance to different voices, accents, etc. To add realism, we impose eye blinks on facial landmarks using unsupervised learning and retargets the person-independent landmarks to person-specific landmarks to preserve the identity-related facial structure which helps in the generation of plausible mouth shapes of the target identity. Finally, we use LSGAN to generate the facial texture from person-specific facial landmarks, using an attention mechanism that helps to preserve identity-related texture. An extensive comparison of our proposed method with the current state-of-the-art methods demonstrates a significant improvement in terms of lip synchronization accuracy, image reconstruction quality, sharpness, and identity-preservation. A user study also reveals improved realism of our animation results over the state-of-the-art methods. To the best of our knowledge, this is the first work in speech-driven 2D facial animation that simultaneously addresses all the above-mentioned attributes of a realistic speech-driven face animation.

</details>

#### [End-to-End Lip Synchronisation Based on Pattern Classification](https://arxiv.org/abs/2005.08606)
**You Jin Kim, Hee Soo Heo, Soo-Whan Chung, Bong-Jin Lee** · 2020-05-18

<details>
<summary>Abstract</summary>

The goal of this work is to synchronise audio and video of a talking face using deep neural network models. Existing works have trained networks on proxy tasks such as cross-modal similarity learning, and then computed similarities between audio and video frames using a sliding window approach. While these methods demonstrate satisfactory performance, the networks are not trained directly on the task. To this end, we propose an end-to-end trained network that can directly predict the offset between an audio stream and the corresponding video stream. The similarity matrix between the two modalities is first computed from the features, then the inference of the offset can be considered to be a pattern recognition problem where the matrix is considered equivalent to an image. The feature extractor and the classifier are trained jointly. We demonstrate that the proposed approach outperforms the previous work by a large margin on LRS2 and LRS3 datasets.

</details>

#### [FaR-GAN for One-Shot Face Reenactment](https://arxiv.org/abs/2005.06402)
**Hanxiang Hao, Sriram Baireddy, Amy R. Reibman, Edward J. Delp** · 2020-05-13

<details>
<summary>Abstract</summary>

Animating a static face image with target facial expressions and movements is important in the area of image editing and movie production. This face reenactment process is challenging due to the complex geometry and movement of human faces. Previous work usually requires a large set of images from the same person to model the appearance. In this paper, we present a one-shot face reenactment model, FaR-GAN, that takes only one face image of any given source identity and a target expression as input, and then produces a face image of the same source identity but with the target expression. The proposed method makes no assumptions about the source identity, facial expression, head pose, or even image background. We evaluate our method on the VoxCeleb1 dataset and show that our method is able to generate a higher quality face image than the compared methods.

</details>

#### [What comprises a good talking-head video generation?: A Survey and Benchmark](https://arxiv.org/abs/2005.03201)
**Lele Chen, Guofeng Cui, Ziyi Kou, Haitian Zheng et al.** · 2020-05-07

<details>
<summary>Abstract</summary>

Over the years, performance evaluation has become essential in computer vision, enabling tangible progress in many sub-fields. While talking-head video generation has become an emerging research topic, existing evaluations on this topic present many limitations. For example, most approaches use human subjects (e.g., via Amazon MTurk) to evaluate their research claims directly. This subjective evaluation is cumbersome, unreproducible, and may impend the evolution of new research. In this work, we present a carefully-designed benchmark for evaluating talking-head video generation with standardized dataset pre-processing strategies. As for evaluation, we either propose new metrics or select the most appropriate ones to evaluate results in what we consider as desired properties for a good talking-head video, namely, identity preserving, lip synchronization, high video quality, and natural-spontaneous motion. By conducting a thoughtful analysis across several state-of-the-art talking-head generation approaches, we aim to uncover the merits and drawbacks of current methods and point out promising directions for future work. All the evaluation code is available at: https://github.com/lelechen63/talking-head-generation-survey.

</details>

#### [APB2Face: Audio-guided face reenactment with auxiliary pose and blink signals](https://arxiv.org/abs/2004.14569)
**Jiangning Zhang, Liang Liu, Zhucun Xue, Yong Liu** · 2020-04-30

<details>
<summary>Abstract</summary>

Audio-guided face reenactment aims at generating photorealistic faces using audio information while maintaining the same facial movement as when speaking to a real person. However, existing methods can not generate vivid face images or only reenact low-resolution faces, which limits the application value. To solve those problems, we propose a novel deep neural network named APB2Face, which consists of GeometryPredictor and FaceReenactor modules. GeometryPredictor uses extra head pose and blink state signals as well as audio to predict the latent landmark geometry information, while FaceReenactor inputs the face landmark image to reenact the photorealistic face. A new dataset AnnVI collected from YouTube is presented to support the approach, and experimental results indicate the superiority of our method than state-of-the-arts, whether in authenticity or controllability.

</details>

#### [ActGAN: Flexible and Efficient One-shot Face Reenactment](https://arxiv.org/abs/2003.13840)
**Ivan Kosarevych, Marian Petruk, Markian Kostiv, Orest Kupyn et al.** · 2020-03-30

<details>
<summary>Abstract</summary>

This paper introduces ActGAN - a novel end-to-end generative adversarial network (GAN) for one-shot face reenactment. Given two images, the goal is to transfer the facial expression of the source actor onto a target person in a photo-realistic fashion. While existing methods require target identity to be predefined, we address this problem by introducing a "many-to-many" approach, which allows arbitrary persons both for source and target without additional retraining. To this end, we employ the Feature Pyramid Network (FPN) as a core generator building block - the first application of FPN in face reenactment, producing finer results. We also introduce a solution to preserve a person's identity between synthesized and target person by adopting the state-of-the-art approach in deep face recognition domain. The architecture readily supports reenactment in different scenarios: "many-to-many", "one-to-one", "one-to-another" in terms of expression accuracy, identity preservation, and overall image quality. We demonstrate that ActGAN achieves competitive performance against recent works concerning visual quality.

</details>

#### [Realistic Face Reenactment via Self-Supervised Disentangling of Identity and Pose](https://arxiv.org/abs/2003.12957)
**Xianfang Zeng, Yusu Pan, Mengmeng Wang, Jiangning Zhang et al.** · 2020-03-29

<details>
<summary>Abstract</summary>

Recent works have shown how realistic talking face images can be obtained under the supervision of geometry guidance, e.g., facial landmark or boundary. To alleviate the demand for manual annotations, in this paper, we propose a novel self-supervised hybrid model (DAE-GAN) that learns how to reenact face naturally given large amounts of unlabeled videos. Our approach combines two deforming autoencoders with the latest advances in the conditional generation. On the one hand, we adopt the deforming autoencoder to disentangle identity and pose representations. A strong prior in talking face videos is that each frame can be encoded as two parts: one for video-specific identity and the other for various poses. Inspired by that, we utilize a multi-frame deforming autoencoder to learn a pose-invariant embedded face for each video. Meanwhile, a multi-scale deforming autoencoder is proposed to extract pose-related information for each frame. On the other hand, the conditional generator allows for enhancing fine details and overall reality. It leverages the disentangled features to generate photo-realistic and pose-alike face images. We evaluate our model on VoxCeleb1 and RaFD dataset. Experiment results demonstrate the superior quality of reenacted images and the flexibility of transferring facial movements between identities.

</details>

#### [Audio-driven Talking Face Video Generation with Learning-based Personalized Head Pose](https://arxiv.org/abs/2002.10137)
**Ran Yi, Zipeng Ye, Juyong Zhang, Hujun Bao et al.** · 2020-02-24

<details>
<summary>Abstract</summary>

Real-world talking faces often accompany with natural head movement. However, most existing talking face video generation methods only consider facial animation with fixed head pose. In this paper, we address this problem by proposing a deep neural network model that takes an audio signal A of a source person and a very short video V of a target person as input, and outputs a synthesized high-quality talking face video with personalized head pose (making use of the visual information in V), expression and lip synchronization (by considering both A and V). The most challenging issue in our work is that natural poses often cause in-plane and out-of-plane head rotations, which makes synthesized talking face video far from realistic. To address this challenge, we reconstruct 3D face animation and re-render it into synthesized frames. To fine tune these frames into realistic ones with smooth background transition, we propose a novel memory-augmented GAN module. By first training a general mapping based on a publicly available dataset and fine-tuning the mapping using the input short video of target person, we develop an effective strategy that only requires a small number of frames (about 300 frames) to learn personalized talking behavior including head pose. Extensive experiments and two user studies show that our method can generate high-quality (i.e., personalized head movements, expressions and good lip synchronization) talking face videos, which are naturally looking with more distinguishing head movement effects than the state-of-the-art methods.

</details>

#### [A Neural Lip-Sync Framework for Synthesizing Photorealistic Virtual News Anchors](https://arxiv.org/abs/2002.08700)
**Ruobing Zheng, Zhou Zhu, Bo Song, Changjiang Ji** · 2020-02-20

<details>
<summary>Abstract</summary>

Lip sync has emerged as a promising technique for generating mouth movements from audio signals. However, synthesizing a high-resolution and photorealistic virtual news anchor is still challenging. Lack of natural appearance, visual consistency, and processing efficiency are the main problems with existing methods. This paper presents a novel lip-sync framework specially designed for producing high-fidelity virtual news anchors. A pair of Temporal Convolutional Networks are used to learn the cross-modal sequential mapping from audio signals to mouth movements, followed by a neural rendering network that translates the synthetic facial map into a high-resolution and photorealistic appearance. This fully trainable framework provides end-to-end processing that outperforms traditional graphics-based methods in many low-delay applications. Experiments also show the framework has advantages over modern neural-based methods in both visual appearance and efficiency.

</details>

#### [Disentangled Speech Embeddings using Cross-modal Self-supervision](https://arxiv.org/abs/2002.08742)
**Arsha Nagrani, Joon Son Chung, Samuel Albanie, Andrew Zisserman** · 2020-02-20

<details>
<summary>Abstract</summary>

The objective of this paper is to learn representations of speaker identity without access to manually annotated data. To do so, we develop a self-supervised learning objective that exploits the natural cross-modal synchrony between faces and audio in video. The key idea behind our approach is to tease apart--without annotation--the representations of linguistic content and speaker identity. We construct a two-stream architecture which: (1) shares low-level features common to both representations; and (2) provides a natural mechanism for explicitly disentangling these factors, offering the potential for greater generalisation to novel combinations of content and identity and ultimately producing speaker identity representations that are more robust. We train our method on a large-scale audio-visual dataset of talking heads `in the wild', and demonstrate its efficacy by evaluating the learned speaker representations for standard speaker recognition performance.

</details>

</details>
<!-- PAPERS_TABLE_END -->
