# 2026

55 papers in this year.

### [Enhancing Self-Supervised Talking Head Forgery Detection via a Training-Free Dual-System Framework](2605.03390.md)
**Ke Liu, Jiwei Wei, Shuchang Zhou, Yutong Xiao et al.** · 2026-05-05

<details>
<summary>Abstract</summary>

Supervised talking head forgery detection faces severe generalization challenges due to the continuous evolution of generators. By reducing reliance on generator-specific forgery patterns, self-supervised detectors offer stronger cross-generator robustness. However, existing research has mainly focused on building stronger detectors, while the discriminative capacity of trained detectors remains insufficiently exploited. In particular, for score-based self-supervised detectors, the limited discriminative ability on hard cases is often reflected in unreliable anomaly ordering, leaving room for further refinement. Motivated by this observation, we draw inspiration from the dual-system theory of human cognition and propose a Training-Free Dual-System (TFDS) framework to further exploit the latent discriminative capacity of existing score-based self-supervised detectors. TFDS treats anomaly-like scores as the basis of System-1, using lightweight threshold-based routing to partition samples into confident and uncertain subsets. System-2 then revisits only the uncertain subset, performing fine-grained evidence-guided reasoning to refine the relative ordering of ambiguous samples within the original score distribution. Extensive experiments demonstrate consistent improvements across datasets and perturbation settings, with the gains arising mainly from corrected ordering within the uncertain subset. These findings show that existing self-supervised talking head forgery detectors still contain underexploited discriminative cues that can be effectively unlocked through training-free dual-system reasoning.

</details>

### [Omni-Fake: Benchmarking Unified Multimodal Social Media Deepfake Detection](2605.01638.md)
**Tianxiao Li, Zhenglin Huang, Haiquan Wen, Yiwei He et al.** · 2026-05-02

<details>
<summary>Abstract</summary>

Multimodal deepfakes are proliferating on social media and threaten authenticity, information integrity, and digital forensics. Existing benchmarks are constrained by their single-modality scope, simplified manipulations, or unrealistic distributions, which limit their ability to assess real-world robustness. To address these limitations, we present Omni-Fake, a unified omni-dataset for comprehensive multimodal deepfake detection in social-media settings. It comprises Omni-Fake-Set, a large-scale, high-quality dataset with 1M+ samples, and Omni-Fake-OOD, an out-of-distribution benchmark with 200k+ samples intentionally excluded from training to evaluate generalization. Omni-Fake spans four modalities (image, audio, video, and audio-video talking head) and supports a joint detection-localization-explanation protocol. On top of Omni-Fake, we further propose Omni-Fake-R1, a reinforcement-learning-driven multimodal detector that adaptively integrates visual and auditory cues and outputs structured decisions, localization, and natural-language explanations. Extensive experiments show significant gains in detection accuracy, cross-modal generalization, and explainability over state-of-the-art baselines. Project page: https://tianxiao1201.github.io/omni-fake-project-page/

</details>

### [Audio-to-3D: One-shot talking face generation with disentangled latent codes and diffusion control](s2:f779cc81439b6ab6ea76bd98e415381c8cd9a489.md)
**Peixu Zhang, Xinyu Yang** · 2026-05-01

### [AsymK-Talker: Real-Time and Long-Horizon Talking Head Generation via Asymmetric Kernel Distillation](2605.02948.md)
**Yuxin Lu, Qian Qiao, Jiayang Sun, Min Cao et al.** · 2026-05-01

<details>
<summary>Abstract</summary>

Recent advances in diffusion models have markedly enhanced the visual fidelity of audio-driven talking head generation. Nevertheless, existing methods are constrained by three critical limitations: causal inefficiency that impedes real-time inference, incompatibility with temporally coherent conditioning, and progressive drift over long-horizon generation, collectively hindering their deployment in real-time applications. To overcome these challenges, we introduce AsymK-Talker, a novel diffusion-distillation method designed for real-time and long-horizon talking head generation. AsymK-Talker comprises three key components: (1) Kernel-Conditioned Loop Generation (KCLG), a causal, chunk-wise generation paradigm that leverages motion kernels to enable temporally consistent propagation; (2) Temporal Reference Encoding (TRE), which converts a static identity reference into a time-aware latent representation to enhance audio-visual synchronization; and (3) Asymmetric Kernel Distillation (AKD), a teacher-student distillation framework wherein the teacher model conditions on ground-truth motion kernels for supervision, while the student learns to generate from generated kernels, thereby ensuring robustness during extended generation sequences. AsymK-Talker achieves promising results on both visual fidelity and lip synchronization metrics.

</details>

### [Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](2604.23586.md)
**Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin et al.** · 2026-04-26

<details>
<summary>Abstract</summary>

Joint audio-video generation models have shown that unified generation yields stronger cross-modal coherence than cascaded approaches. However, existing models couple modalities throughout denoising via pervasive attention, treating high-level semantics and low-level details in a fully entangled manner. This is suboptimal for talking head synthesis: while audio and facial motion are semantically correlated, their low-level realizations (acoustic signals and visual textures) follow distinct rendering processes. Enforcing joint modeling across all levels causes unnecessary entanglement and reduces efficiency. We propose Talker-T2AV, an autoregressive diffusion framework where high-level cross-modal modeling occurs in a shared backbone, while low-level refinement uses modality-specific decoders. A shared autoregressive language model jointly reasons over audio and video in a unified patch-level token space. Two lightweight diffusion transformer heads decode the hidden states into frame-level audio and video latents. Experiments on talking portrait benchmarks show Talker-T2AV outperforms dual-branch baselines in lip-sync accuracy, video quality, and audio quality, achieving stronger cross-modal consistency than cascaded pipelines.

</details>

### [Do Protective Perturbations Really Protect Portrait Privacy under Real-world Image Transformations?](2604.23688.md)
**Ruiqing Sun, Xingshan Yao, Zhijing Wu, Tian Lan et al.** · 2026-04-26

<details>
<summary>Abstract</summary>

Proactive defense methods protect portrait images from unauthorized editing or talking face generation (TFG) by introducing pixel-level protective perturbations, and have already attracted increasing attention for privacy protection. In real-world scenarios, images inevitably undergo various transformations during cross-device display and dissemination--such as scale transformations and color compression--that directly alter pixel values. However, it remains unclear whether such pixel-level modifications affect the effectiveness of existing proactive defense methods that rely on pixel-level perturbations. To solve this problem, we conduct a systematic evaluation of representative proactive defenses under image transformation. The evaluated methods are selected to span different generation architectures such as diffusion and GAN-based models, as well as defense scopes covering both portrait and natural images, and are assessed using both qualitative and quantitative metrics for subjective and objective comparison. Experimental results indicate that defense methods based on pixel-level perturbations struggle to withstand common image transformations, posing a risk of defense failure in real-world applications. To further highlight this risk, we propose a simple yet effective purification framework by leveraging the vulnerabilities induced by real-world image transformations. Experimental results demonstrate that the proposed method can efficiently remove protective perturbations with low computational cost, highlighting previously overlooked risks to the research community.

</details>

### [Talking Slide Avatars: Open-Source Multimodal Communication Approach for Teaching](2604.23703.md)
**Xinxing Wu** · 2026-04-26

<details>
<summary>Abstract</summary>

Slide-based teaching is widely used in higher education, yet in online, hybrid, and asynchronous contexts, slides often lose the instructor presence, narrative continuity, and expressive framing that help learners connect with content. Full lecture video can partly restore these qualities, but it is time-consuming to record, revise, and reuse. This study addresses that pedagogical and production challenge by presenting a practice-based analysis of an open-source workflow for creating talking slide avatars for slide-based teaching. The workflow integrates OpenVoice for text-to-speech generation and voice cloning with Ditto-TalkingHead for audio-driven talking-image synthesis, enabling instructors to transform a script and a static portrait into a short narrated video that can be embedded in slide decks or HTML-based lecture materials. Rather than treating this workflow merely as a technical solution, the study frames talking slide avatars as multimodal communication artifacts at the intersection of digital pedagogy, aesthetic education, and art-technology practice. Using a practice-based implementation and analytic reflection approach, the study documents the production pipeline, examines its communicative and aesthetic affordances, and proposes practical guidelines for script length, image selection, pacing, disclosure, accessibility, and ethical use. The study makes three primary contributions: it presents an educator-oriented open-source production model, reframes talking avatars as an educational communication design problem, and proposes a responsible pathway for incorporating generative synthetic media into teaching. It concludes that short, transparent, and carefully designed avatars can humanize slide-based instruction while providing a reusable communicative layer for introductions, transitions, reminders, and recaps across online, hybrid, and asynchronous learning environments.

</details>

### [PortraitDirector: A Hierarchical Disentanglement Framework for Controllable and Real-time Facial Reenactment](2604.19129.md)
**Chaonan Ji, Jinwei Qi, Sheng Xu, Peng Zhang et al.** · 2026-04-21

<details>
<summary>Abstract</summary>

Existing facial reenactment methods struggle with a trade-off between expressiveness and fine-grained controllability. Holistic facial reenactment models often sacrifice granular control for expressiveness, while methods designed for control may struggle with fidelity and robust disentanglement. Instead of treating facial motion as a monolithic signal, we explore an alternative compositional perspective. In this paper, we introduce PortraitDirector, a novel framework that formulates face reenactment as a hierarchical composition task, achieving high-fidelity and controllable results. We employ a Hierarchical Motion Disentanglement and Composition strategy, deconstructing facial motion into a Spatial Layer for physical movements and a Semantic Layer for emotional content. The Spatial Layer comprises: (i) global head pose, managed via a dedicated representation and injection pathway; (ii) spatially separated local facial expressions, distilled from cropped facial regions and purged of emotional cues via Emotion-Filtering Module leveraging an information bottleneck. The Semantic Layer contains a derived global emotion. The disentangled components are then recomposed into an expressive motion latent. Furthermore, we engineer the framework for real-time performance through a suite of optimizations, including diffusion distillation, causal attention and VAE acceleration. PortraitDirector achieves streaming, high-fidelity, controllable 512 x 512 face reenactment at 20 FPS with a end-to-end 800 ms latency on a single 5090 GPU.

</details>

### [Polyglot: Multilingual Style Preserving Speech-Driven Facial Animation](2604.16108.md)
**Federico Nocentini, Kwang-duck Seo, Qingju Liu, C. Ferrari et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Speech-Driven Facial Animation (SDFA) has gained significant attention due to its applications in movies, video games, and virtual reality. However, most existing models are trained on single-language data, limiting their effectiveness in real-world multilingual scenarios. In this work, we address multilingual SDFA, which is essential for realistic generation since language influences phonetics, rhythm, intonation, and facial expressions. Speaking style is also shaped by individual differences, not only by language. Existing methods typically rely on either language-specific or speaker-specific conditioning, but not both, limiting their ability to model their interaction. We introduce Polyglot, a unified diffusion-based architecture for personalized multilingual SDFA. Our method uses transcript embeddings to encode language information and style embeddings extracted from reference facial sequences to capture individual speaking characteristics. Polyglot does not require predefined language or speaker labels, enabling generalization across languages and speakers through self-supervised learning. By jointly conditioning on language and style, it captures expressive traits such as rhythm, articulation, and habitual facial movements, producing temporally coherent and realistic animations. Experiments show improved performance in both monolingual and multilingual settings, providing a unified framework for modeling language and personal style in SDFA.

</details>

### [TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](2604.14580.md)
**Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang et al.** · 2026-04-16

<details>
<summary>Abstract</summary>

Existing audio-driven video digital human generation models rely on multi-step denoising, resulting in substantial computational overhead that severely limits their deployment in real-world settings. While one-step distillation approaches can significantly accelerate inference, they often suffer from training instability. To address this challenge, we propose TurboTalk, a two-stage progressive distillation framework that effectively compresses a multi-step audio-driven video diffusion model into a single-step generator. We first adopt Distribution Matching Distillation to obtain a strong and stable 4-step student, and then progressively reduce the denoising steps from 4 to 1 through adversarial distillation. To ensure stable training under extreme step reduction, we introduce a progressive timestep sampling strategy and a self-compare adversarial objective that provides an intermediate adversarial reference that stabilizes progressive distillation. Our method achieve single-step generation of video talking avatar, boosting inference speed by 120 times while maintaining high generation quality.

</details>

### [DiffMagicFace: Identity Consistent Facial Editing of Real Videos](2604.13841.md)
**Huanghao Yin, Shenkun Xu, Kanle Shi, Junhai Yong et al.** · 2026-04-15

<details>
<summary>Abstract</summary>

Text-conditioned image editing has greatly benefitted from the advancements in Image Diffusion Models. However, extending these techniques to facial video editing introduces challenges in preserving facial identity throughout the source video and ensuring consistency of the edited subject across frames. In this paper, we introduce DiffMagicFace, a unique video editing framework that integrates two fine-tuned models for text and image control. These models operate concurrently during inference to produce video frames that maintain identity features while seamlessly aligning with the editing semantics. To ensure the consistency of the edited videos, we develop a dataset comprising images showcasing various facial perspectives for each edited subject. The creation of a data set is achieved through rendering techniques and the subsequent application of optimization algorithms. Remarkably, our approach does not depend on video datasets but still delivers high-quality results in both consistency and content. The excellent effect holds even for complex tasks like talking head videos and distinguishing closely related categories. The videos edited using our framework exhibit parity with videos that are made using traditional rendering software. Through comparative analysis with current state-of-the-art methods, our framework demonstrates superior performance in both visual appeal and quantitative metrics.

</details>

### [CoSyncDiT: Cognitive Synchronous Diffusion Transformer for Movie Dubbing](2604.12292.md)
**Gaoxiang Cong, Liang Li, Jiaxin Ye, Zhedong Zhang et al.** · 2026-04-14

<details>
<summary>Abstract</summary>

Movie dubbing aims to synthesize speech that preserves the vocal identity of a reference audio while synchronizing with the lip movements in a target video. Existing methods fail to achieve precise lip-sync and lack naturalness due to explicit alignment at the duration level. While implicit alignment solutions have emerged, they remain susceptible to interference from the reference audio, triggering timbre and pronunciation degradation in in-the-wild scenarios. In this paper, we propose a novel flow matching-based movie dubbing framework driven by the Cognitive Synchronous Diffusion Transformer (CoSync-DiT), inspired by the cognitive process of professional actors. This architecture progressively guides the noise-to-speech generative trajectory by executing acoustic style adapting, fine-grained visual calibrating, and time-aware context aligning. Furthermore, we design the Joint Semantic and Alignment Regularization (JSAR) mechanism to simultaneously constrain frame-level temporal consistency on the contextual outputs and semantic consistency on the flow hidden states, ensuring robust alignment. Extensive experiments on both standard benchmarks and challenging in-the-wild dubbing benchmarks demonstrate that our method achieves the state-of-the-art performance across multiple metrics.

</details>

### [SEDTalker: Emotion-Aware 3D Facial Animation Using Frame-Level Speech Emotion Diarization](2604.13335.md)
**Farzaneh Jafari, Stefano Berretti, Anup Basu** · 2026-04-14

<details>
<summary>Abstract</summary>

We introduce SEDTalker, an emotion-aware framework for speech-driven 3D facial animation that leverages frame-level speech emotion diarization to achieve fine-grained expressive control. Unlike prior approaches that rely on utterance-level or manually specified emotion labels, our method predicts temporally dense emotion categories and intensities directly from speech, enabling continuous modulation of facial expressions over time. The diarized emotion signals are encoded as learned embeddings and used to condition a speech-driven 3D animation model based on a hybrid Transformer-Mamba architecture. This design allows effective disentanglement of linguistic content and emotional style while preserving identity and temporal coherence. We evaluate our approach on a large-scale multi-corpus dataset for speech emotion diarization and on the EmoVOCA dataset for emotional 3D facial animation. Quantitative results demonstrate strong frame-level emotion recognition performance and low geometric and temporal reconstruction errors, while qualitative results show smooth emotion transitions and consistent expression control. These findings highlight the effectiveness of frame-level emotion diarization for expressive and controllable 3D talking head generation.

</details>

### [SyncBreaker:Stage-Aware Multimodal Adversarial Attacks on Audio-Driven Talking Head Generation](2604.08405.md)
**Wenli Zhang, Xianglong Shi, Sirui Zhao, Xinqi Chen et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

Diffusion-based audio-driven talking-head generation enables realistic portrait animation, but also introduces risks of misuse, such as fraud and misinformation. Existing protection methods are largely limited to a single modality, and neither image-only nor audio-only attacks can effectively suppress speech-driven facial dynamics. To address this gap, we propose SyncBreaker, a stage-aware multimodal protection framework that jointly perturbs portrait and audio inputs under modality-specific perceptual constraints. Our key contributions are twofold. First, for the image stream, we introduce nullifying supervision with Multi-Interval Sampling (MIS) across diffusion stages to steer the generation toward the static reference portrait by aggregating guidance from multiple denoising intervals. Second, for the audio stream, we propose Cross-Attention Fooling (CAF), which suppresses interval-specific audio-conditioned cross-attention responses. Both streams are optimized independently and combined at inference time to enable flexible deployment. We evaluate SyncBreaker in a white-box proactive protection setting. Extensive experiments demonstrate that SyncBreaker more effectively degrades lip synchronization and facial dynamics than strong single-modality baselines, while preserving input perceptual quality and remaining robust under purification. Code: https://github.com/kitty384/SyncBreaker.

</details>

### [Cross-Modal Emotion Transfer for Emotion Editing in Talking Face Video](2604.07786.md)
**Chanhyuk Choi, Taesoo Kim, Donggyu Lee, Siyeol Jung et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

Talking face generation has gained significant attention as a core application of generative models. To enhance the expressiveness and realism of synthesized videos, emotion editing in talking face video plays a crucial role. However, existing approaches often limit expressive flexibility and struggle to generate extended emotions. Label-based methods represent emotions with discrete categories, which fail to capture a wide range of emotions. Audio-based methods can leverage emotionally rich speech signals - and even benefit from expressive text-to-speech (TTS) synthesis - but they fail to express the target emotions because emotions and linguistic contents are entangled in emotional speeches. Images-based methods, on the other hand, rely on target reference images to guide emotion transfer, yet they require high-quality frontal views and face challenges in acquiring reference data for extended emotions (e.g., sarcasm). To address these limitations, we propose Cross-Modal Emotion Transfer (C-MET), a novel approach that generates facial expressions based on speeches by modeling emotion semantic vectors between speech and visual feature spaces. C-MET leverages a large-scale pretrained audio encoder and a disentangled facial expression encoder to learn emotion semantic vectors that represent the difference between two different emotional embeddings across modalities. Extensive experiments on the MEAD and CREMA-D datasets demonstrate that our method improves emotion accuracy by 14% over state-of-the-art methods, while generating expressive talking face videos - even for unseen extended emotions. Code, checkpoint, and demo are available at https://chanhyeok-choi.github.io/C-MET/

</details>

### [Multimodal AI in education: an avatar-based intelligent learning system for the Kazakh language](s2:cc4c9cc6f66ac5f4ecfff5028a0cd8e4761c9d6d.md)
**Aru Ukenova, G. Bekmanova, B. Yergesh, Sadok Ben Yahia et al.** · 2026-04-08

<details>
<summary>Abstract</summary>

This article describes the development of a multimodal learning system for the Kazakh language intended for digital educational environments. The study focuses on the lack of avatar-based learning systems adapted to the linguistic properties of the Kazakh language and the limited integration of verbal and non-verbal components in existing solutions. The proposed system combines syntactic and morphological text analysis with sentiment processing and intonation control. Speech synthesis, gesture generation, facial expression control, and lip synchronization are implemented within a single system architecture. Prosodic parameters are formed based on sentence structure and sentence-level emotional indicators, while visual articulation is synchronized with audio output. The system was tested in speech synthesis scenarios relevant to interactive educational use. The results show that the system can be used for automated lecture narration, voice-over of instructional materials, and basic learner interaction in avatar-based educational settings.

</details>

### [MMTalker: Multiresolution 3D Talking Head Synthesis with Multimodal Feature Fusion](2604.02941.md)
**Bin Liu, Zhixiang Xiong, Zhifen He, Bo Li** · 2026-04-03

<details>
<summary>Abstract</summary>

Speech-driven three-dimensional (3D) facial animation synthesis aims to build a mapping from one-dimensional (1D) speech signals to time-varying 3D facial motion signals. Current methods still face challenges in maintaining lip-sync accuracy and producing realistic facial expressions, primarily due to the highly ill-posed nature of this cross-modal mapping. In this paper, we introduce a novel 3D audio-driven facial animation synthesis method through multi-resolution representation and multi-modal feature fusion, called MMTalker which can accurately reconstruct the rich details of 3D facial motion. We first achieve the continuous representation of 3D face with details by mesh parameterization and non-uniform differentiable sampling. The mesh parameterization technique establishes the correspondence between UV plane and 3D facial mesh and is used to offer ground truth for the continuous learning. Differentiable non-uniform sampling enables precise facial detail acquisition by setting learnable sampling probability in each triangular face. Next, we employ residual graph convolutional network and dual cross-attention mechanism to extract discriminative facial motion feature from multiple input modalities. This proposed multimodal fusion strategy takes full use of the hierarchical features of speech and the explicit spatiotemporal geometric features of facial mesh. Finally, a lightweight regression network predicts the vertex-wise geometric displacements of the synthesized talking face by jointly processing the sampled points in the canonical UV space and the encoded facial motion features. Comprehensive experiments demonstrate that significant improvements are achieved over state-of-the-art methods, especially in the synchronization accuracy of lip and eye movements.

</details>

### [Precise Speech-driven Talking-Face Synthesis with Realistic Speaker-Emulated Facil Expressions](s2:98adc42cb44096970eea8474b43ffd8087df0f6b.md)
**Jhing-Fa Wang, Din-Yuen Chan, Shu-Yan Liou, Hsin-Chun Tsai** · 2026-04-03

<details>
<summary>Abstract</summary>

Traditional facial animation models do not particularly stress on the naturalness of imitating the dynamic facial expressions including eye movements, dynamic eyebrow deformation and head motion naturalness. Hence, in this paper, a speech-driven talking-face synthesizer (SDTS) is proposed for generating the dynamic talking video of given static face for semantically mimicking the speech of any real person. The SDTS can lead the static digital-twin face to vividly mimic the expressive motions of face and lip-synced mouth of various speakers with the personalized accent with high distinctiveness. The SDTS framework has two stages. In first stage, one branch termed the dynamic fused-features generation module (DFGM) contains cross-modal speech-facial fusion module (CSFF) and temporal convolutional network (TCN). The CSFF is the core to seamlessly align the speech features and facial features. The second branch is the self-designed adaptive identity extractor (AIE) where a series of the residual blocks using partial batch normalization unit (PBN-ResNet blocks) and the residual blocks with the squeeze-and-excitation unit (SE-ResNet blocks) are cascaded to precisely capture the key features of face in a static reference image. In the second stage of SDTS, the diffusion model termed diffusion-based rendering model (DIRM) is applied to generate the high-resolution video reconstruction with the consistencies of appearance and emotion via fusing the driving speech features and the referred facial features. The extensive experiments demonstrate that SDTS can significantly promote the lip-synchronization, enrich the upper facial expression, and exhibit the naturalness of the head movements. Moreover, the SDTS can steadily maintain the facial identity consistency and the facial expression coherence for varying speaking speeds and emotions. Hence, it can attain less than 5.26 FID, 0.72 LSE-D and 0.56 LME than the StyleTalk model which is a well-known talking-face synthesis model.

</details>

### [SAVe: Self-Supervised Audio-visual Deepfake Detection Exploiting Visual Artifacts and Audio-visual Misalignment](2603.25140.md)
**Sahibzada Adil Shahzad, Ammarah Hashmi, Junichi Yamagishi, Yusuke Yasuda et al.** · 2026-03-26

<details>
<summary>Abstract</summary>

Multimodal deepfakes can exhibit subtle visual artifacts and cross-modal inconsistencies, which remain challenging to detect, especially when detectors are trained primarily on curated synthetic forgeries. Such synthetic dependence can introduce dataset and generator bias, limiting scalability and robustness to unseen manipulations. We propose SAVe, a self-supervised audio-visual deepfake detection framework that learns entirely on authentic videos. SAVe generates on-the-fly, identity-preserving, region-aware self-blended pseudo-manipulations to emulate tampering artifacts, enabling the model to learn complementary visual cues across multiple facial granularities. To capture cross-modal evidence, SAVe also models lip-speech synchronization via an audio-visual alignment component that detects temporal misalignment patterns characteristic of audio-visual forgeries. Experiments on FakeAVCeleb and AV-LipSync-TIMIT demonstrate competitive in-domain performance and strong cross-dataset generalization, highlighting self-supervised learning as a scalable paradigm for multimodal deepfake detection.

</details>

### [InterDyad: Interactive Dyadic Speech-to-Video Generation by Querying Intermediate Visual Guidance](2603.23132.md)
**Dongwei Pan, Longwei Guo, Jiazhi Guan, Luying Huang et al.** · 2026-03-24

<details>
<summary>Abstract</summary>

Despite progress in speech-to-video synthesis, existing methods often struggle to capture cross-individual dependencies and provide fine-grained control over reactive behaviors in dyadic settings. To address these challenges, we propose InterDyad, a framework that enables naturalistic interactive dynamics synthesis via querying structural motion guidance. Specifically, we first design an Interactivity Injector that achieves video reenactment based on identity-agnostic motion priors extracted from reference videos. Building upon this, we introduce a MetaQuery-based modality alignment mechanism to bridge the gap between conversational audio and these motion priors. By leveraging a Multimodal Large Language Model (MLLM), our framework is able to distill linguistic intent from audio to dictate the precise timing and appropriateness of reactions. To further improve lip-sync quality under extreme head poses, we propose Role-aware Dyadic Gaussian Guidance (RoDG) for enhanced lip-synchronization and spatial consistency. Finally, we introduce a dedicated evaluation suite with novelly designed metrics to quantify dyadic interaction. Comprehensive experiments demonstrate that InterDyad significantly outperforms state-of-the-art methods in producing natural and contextually grounded two-person interactions. Please refer to our project page for demo videos: https://interdyad.github.io/.

</details>

### [EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](2603.21332.md)
**Haolan Xu, Keli Cheng, Lei Wang, Ning Bi et al.** · 2026-03-22

<details>
<summary>Abstract</summary>

Audio-driven 3D talking head synthesis has advanced rapidly with Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). By leveraging rich pre-trained priors, few-shot methods enable instant personalization from just a few seconds of video. However, under expressive facial motion, existing few-shot approaches often suffer from geometric instability and audio-emotion mismatch, highlighting the need for more effective emotion-aware motion modeling. In this work, we present EmoTaG, a few-shot emotion-aware 3D talking head synthesis framework built on the Pretrain-and-Adapt paradigm. Our key insight is to reformulate motion prediction in a structured FLAME parameter space rather than directly deforming 3D Gaussians, thereby introducing explicit geometric priors that improve motion stability. Building upon this, we propose a Gated Residual Motion Network (GRMN), which captures emotional prosody from audio while supplementing head pose and upper-face cues absent from audio, enabling expressive and coherent motion generation. Extensive experiments demonstrate that EmoTaG achieves state-of-the-art performance in emotional expressiveness, lip synchronization, visual realism, and motion stability.

</details>

### [Real-Time Multi Model Synchronization of TTS, Lip Sync, and Caption Generation using Deep Learning](s2:fed7460b81f31dc2f11a904110a7283afd760241.md)
**Abhay Gupta, Aditi Kesarwani, Ashish Kumar Mishra, Shubha Mishra** · 2026-03-20

<details>
<summary>Abstract</summary>

Abstract: Real-time multimodal communication systems require seamless synchronization between speech generation, lip movements, and textual captions to create natural, accessible, and interactive digital experiences. This work proposes a unified deep-learning–based framework for real-time multimodal synchronization of Text-to-Speech (TTS), lipsync animation, and caption generation. The system integrates a streaming neural TTS model, an audio/text-driven lipsync module, and a low-latency caption generator built on streaming ASR. A central synchronization engine aligns phoneme timestamps, viseme transitions, and caption token timings using adaptive buffering and drift-correction strategies. This ensures that all three modalities—audio, visual articulation, and text output—remain synchronized within perceptually acceptable thresholds (<40 ms). The proposed pipeline improves temporal coherence, reduces caption lag, and enhances user experience in applications such as virtual presenters, digital avatars, assistive technologies, and human–AI communication. Experimental evaluation demonstrates significant improvements in alignment accuracy and latency over baseline independent systems. The framework sets a scalable foundation for future advancements in expressive avatars, multilingual communication, and low-resource real-time deployment. Keywords: Real-time synchronization, Text-to-Speech (TTS), Lipsync, Caption generation, Multimodal deep learning, Phoneme–viseme alignment, Streaming ASR, Neural vocoder, Human–computer interaction, Virtual avatar systems.

</details>

### [EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](2603.20307.md)
**Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du et al.** · 2026-03-19

<details>
<summary>Abstract</summary>

Audio-driven talking head generation aims to create vivid and realistic videos from a static portrait and speech. Existing AR-based methods rely on intermediate facial representations, which limit their expressiveness and realism. Meanwhile, diffusion-based methods generate clip-by-clip, lacking fine-grained control and causing inherent latency due to overall denoising across the window. To address these limitations, we propose EARTalking, a novel end-to-end, GPT-style autoregressive model for interactive audio-driven talking head generation. Our method introduces a novel frame-by-frame, in-context, audio-driven streaming generation paradigm. For inherently supporting variable-length video generation with identity consistency, we propose the Sink Frame Window Attention (SFA) mechanism. Furthermore, to avoid the complex, separate networks that prior works required for diverse control signals, we propose a streaming Frame Condition In-Context (FCIC) scheme. This scheme efficiently injects diverse control signals in a streaming, in-context manner, enabling interactive control at every frame and at arbitrary moments. Experiments demonstrate that EARTalking outperforms existing autoregressive methods and achieves performance comparable to diffusion-based methods. Our work demonstrates the feasibility of in-context streaming autoregressive control, unlocking a scalable direction for flexible, efficient generation. The code will be released for reproducibility.

</details>

### [AvatarForcing: One-Step Streaming Talking Avatars via Local-Future Sliding-Window Denoising](2603.14331.md)
**Liyuan Cui, Wentao Hu, Wenyuan Zhang, Zesong Yang et al.** · 2026-03-15

<details>
<summary>Abstract</summary>

Real-time talking avatar generation requires low latency and minute-level temporal stability. Autoregressive (AR) forcing enables streaming inference but suffers from exposure bias, which causes errors to accumulate and become irreversible over long rollouts. In contrast, full-sequence diffusion transformers mitigate drift but remain computationally prohibitive for real-time long-form synthesis. We present AvatarForcing, a one-step streaming diffusion framework that denoises a fixed local-future window with heterogeneous noise levels and emits one clean block per step under constant per-step cost. To stabilize unbounded streams, the method introduces dual-anchor temporal forcing: a style anchor that re-indexes RoPE to maintain a fixed relative position with respect to the active window and applies anchor-audio zero-padding, and a temporal anchor that reuses recently emitted clean blocks to ensure smooth transitions. Real-time one-step inference is enabled by two-stage streaming distillation with offline ODE backfill and distribution matching. Experiments on standard benchmarks and a new 400-video long-form benchmark show strong visual quality and lip synchronization at 34 ms/frame using a 1.3B-parameter student model for realtime streaming. Our page is available at: https://cuiliyuan121.github.io/AvatarForcing/

</details>

### [DiFlowDubber: Discrete Flow Matching for Automated Video Dubbing via Cross-Modal Alignment and Synchronization](2603.14267.md)
**Ngoc-Son Nguyen, Thanh V. T. Tran, Jeongsoo Choi, Hieu-Nghia Huynh-Nguyen et al.** · 2026-03-15

<details>
<summary>Abstract</summary>

Video dubbing has broad applications in filmmaking, multimedia creation, and assistive speech technology. Existing approaches either train directly on limited dubbing datasets or adopt a two-stage pipeline that adapts pre-trained text-to-speech (TTS) models, which often struggle to produce expressive prosody, rich acoustic characteristics, and precise synchronization. To address these issues, we propose DiFlowDubber with a novel two-stage training framework that effectively transfers knowledge from a pre-trained TTS model to video-driven dubbing, with a discrete flow matching generative backbone. Specifically, we design a FaPro module that captures global prosody and stylistic cues from facial expressions and leverages this information to guide the modeling of subsequent speech attributes. To ensure precise speech-lip synchronization, we introduce a Synchronizer module that bridges the modality gap among text, video, and speech, thereby improving cross-modal alignment and generating speech that is temporally synchronized with lip movements. Experiments on two primary benchmark datasets demonstrate that DiFlowDubber outperforms previous methods across multiple metrics.

</details>

### [Emotion-Conditioned Motion Sub-spaces with Flow Matching for Real-Time Audio-Driven Talking Heads](s2:ca037d58a95f1448e433fe8e8e21e003cfbd7fa8.md)
**Haoyu Wang, Xiaozhe Xin, Xiaoyu Qin, Meiguang Jin et al.** · 2026-03-14

<details>
<summary>Abstract</summary>

Recent advances in audio-driven talking-head synthesis have brought lip-sync precision close to human perception, yet emotional fidelity and real-time inference remain open challenges. Existing pipelines typically disentangle lip articulation, facial expression, and head pose in latent space; this rigid factorization ignores the intrinsic coupling between articulation and affect — e.g., downward lip corners when sad—thus limiting expressiveness. We cast speech-conditioned facial motion as a sample from an emotion-conditioned distribution in a motion latent space. Concretely, we (i) learn a motion dictionary of orthogonal bases with an autoencoder via self-supervision, (ii) construct emotion-conditioned sub-spaces within the latent space, and (iii) design a layer-progressive cross-attention fusion module that modulates a flow-matching sampler with both audio and emotion signals. Only ten reverse ODE steps are required to generate a motion-latent trajectory, enabling real-time end-to-end latency. Extensive experiments on MEAD and RAVDESS show that our method outperforms recent GAN- and diffusion-based baselines in emotion accuracy while running at around 75 FPS on a single desktop GPU. The proposed framework delivers the first emotionally expressive Audio2Face system that simultaneously achieves lip-sync accuracy, affective realism, and real-time performance.

</details>

### [Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback](s2:a69575793b10289587dc5a63e4779186c1466f81.md)
**Xingpei Ma, Shenneng Huang, Jiaran Cai, Yuansheng Guan et al.** · 2026-03-14

<details>
<summary>Abstract</summary>

Recent advances in diffusion models have significantly improved audio-driven human video generation, surpassing traditional methods in both quality and controllability. However, existing approaches still face challenges in lip-sync accuracy, temporal coherence for long video generation, and multi-character animation. In this work, we propose a diffusion transformer (DiT)-based framework for generating lifelike talking videos of arbitrary length, and introduce a training-free method for multi-character audio-driven animation. First, we employ a LoRA-based training strategy combined with a position shift inference approach, which enables efficient long video generation while preserving the capabilities of the foundation model. Moreover, we combine partial parameter updates with reward feedback to enhance both lip synchronization and natural body motion. Finally, we propose a training-free approach, Mask Classifier-Free Guidance (Mask-CFG), for multi-character animation, which requires no specialized datasets or model modifications and supports audio-driven animation for three or more characters. Experimental results demonstrate that our method outperforms existing state-of-the-art approaches, achieving high-quality, temporally coherent, and multi-character audio-driven video generation in a simple, efficient, and cost-effective manner.

</details>

### [OmniEdit: A Training-free framework for Lip Synchronization and Audio-Visual Editing](2603.09084.md)
**Lixiang Lin, Siyuan Jin, Jinshan Zhang** · 2026-03-10

<details>
<summary>Abstract</summary>

Lip synchronization and audio-visual editing have emerged as fundamental challenges in multimodal learning, underpinning a wide range of applications, including film production, virtual avatars, and telepresence. Despite recent progress, most existing methods for lip synchronization and audio-visual editing depend on supervised fine-tuning of pre-trained models, leading to considerable computational overhead and data requirements. In this paper, we present OmniEdit, a training-free framework designed for both lip synchronization and audio-visual editing. Our approach reformulates the editing paradigm by substituting the edit sequence in FlowEdit with the target sequence, yielding an unbiased estimation of the desired output. Moreover, by removing stochastic elements from the generation process, we establish a smooth and stable editing trajectory. Extensive experimental results validate the effectiveness and robustness of the proposed framework. Code is available at https://github.com/l1346792580123/OmniEdit.

</details>

### [EmbedTalk: Triplane-Free Talking Head Synthesis using Embedding-Driven Gaussian Deformation](2603.07604.md)
**Arpita Saggar, Jonathan C. Darling, Duygu Sarikaya, David C. Hogg** · 2026-03-08

<details>
<summary>Abstract</summary>

Real-time talking head synthesis increasingly relies on deformable 3D Gaussian Splatting (3DGS) due to its low latency. Tri-planes are the standard choice for encoding Gaussians prior to deformation, since they provide a continuous domain with explicit spatial relationships. However, tri-plane representations are limited by grid resolution and approximation errors introduced by projecting 3D volumetric fields onto 2D subspaces. Recent work has shown the superiority of learnt embeddings for driving temporal deformations in 4D scene reconstruction. We introduce $\textbf{EmbedTalk}$, which shows how such embeddings can be leveraged for modelling speech deformations in talking head synthesis. Through comprehensive experiments, we show that EmbedTalk outperforms existing 3DGS-based methods in rendering quality, lip synchronisation, and motion consistency, while remaining competitive with state-of-the-art generative models. Moreover, replacing the tri-plane encoding with learnt embeddings enables significantly more compact models that achieve over 60 FPS on a mobile GPU (RTX 2060 6 GB). Our code will be placed in the public domain on acceptance.

</details>

### [TempoSyncDiff: Distilled Temporally-Consistent Diffusion for Low-Latency Audio-Driven Talking Head Generation](2603.06057.md)
**Soumya Mazumdar, Vineet Kumar Rakesh** · 2026-03-06

<details>
<summary>Abstract</summary>

Diffusion models have recently advanced photorealistic human synthesis, although practical talking-head generation (THG) remains constrained by high inference latency, temporal instability such as flicker and identity drift, and imperfect audio-visual alignment under challenging speech conditions. This paper introduces TempoSyncDiff, a reference-conditioned latent diffusion framework that explores few-step inference for efficient audio-driven talking-head generation. The approach adopts a teacher-student distillation formulation in which a diffusion teacher trained with a standard noise prediction objective guides a lightweight student denoiser capable of operating with significantly fewer inference steps to improve generation stability. The framework incorporates identity anchoring and temporal regularization designed to mitigate identity drift and frame-to-frame flicker during synthesis, while viseme-based audio conditioning provides coarse lip motion control. Experiments on the LRS3 dataset report denoising-stage component-level metrics relative to VAE reconstructions and preliminary latency characterization, including CPU-only and edge computing measurements and feasibility estimates for edge deployment. The results suggest that distilled diffusion models can retain much of the reconstruction behaviour of a stronger teacher while enabling substantially lower latency inference. The study is positioned as an initial step toward practical diffusion-based talking-head generation under constrained computational settings. GitHub: https://mazumdarsoumya.github.io/TempoSyncDiff

</details>

### [FlowPortrait: Reinforcement Learning for Audio-Driven Portrait Video Generation](2603.00159.md)
**Weiting Tan, Andy T. Liu, Ming Tu, Xinghua Qu et al.** · 2026-02-25

<details>
<summary>Abstract</summary>

Generating realistic talking-head videos remains challenging due to persistent issues such as imperfect lip synchronization, unnatural motion, and evaluation metrics that correlate poorly with human perception. We propose FlowPortrait, a reinforcement-learning framework for audio-driven portrait animation built on a multimodal backbone for autoregressive audio-to-video generation. FlowPortrait introduces a human-aligned evaluation system based on Multimodal Large Language Models (MLLMs) to assess lip-sync accuracy, expressiveness, and motion quality. These signals are combined with perceptual and temporal consistency regularizers to form a stable composite reward, which is used to post-train the generator via Group Relative Policy Optimization (GRPO). Extensive experiments, including both automatic evaluations and human preference studies, demonstrate that FlowPortrait consistently produces higher-quality talking-head videos, highlighting the effectiveness of reinforcement learning for portrait animation.

</details>

### [EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](2602.13669.md)
**Rang Meng, Weipeng Wu, Yingjie Yin, Yuming Li et al.** · 2026-02-14

<details>
<summary>Abstract</summary>

Recent multi-modal video generation models have achieved high visual quality, but their prohibitive latency and limited temporal stability hinder real-time deployment. Streaming inference exacerbates these issues, leading to pronounced multimodal degradation, such as spatial blurring, temporal drift, and lip desynchronization, which creates an unresolved efficiency-performance trade-off. To this end, we propose EchoTorrent, a novel schema with a fourfold design: (1) Multi-Teacher Training fine-tunes a pre-trained model on distinct preference domains to obtain specialized domain experts, which sequentially transfer domain-specific knowledge to a student model; (2) Adaptive CFG Calibration (ACC-DMD), which calibrates the audio CFG augmentation errors in DMD via a phased spatiotemporal schedule, eliminating redundant CFG computations and enabling single-pass inference per step; (3) Hybrid Long Tail Forcing, which enforces alignment exclusively on tail frames during long-horizon self-rollout training via a causal-bidirectional hybrid architecture, effectively mitigates spatiotemporal degradation in streaming mode while enhancing fidelity to reference frames; and (4) VAE Decoder Refiner through pixel-domain optimization of the VAE decoder to recover high-frequency details while circumventing latent-space ambiguities. Extensive experiments and analysis demonstrate that EchoTorrent achieves few-pass autoregressive generation with substantially extended temporal consistency, identity preservation, and audio-lip synchronization.

</details>

### [3DXTalker: Unifying Identity, Lip Sync, Emotion, and Spatial Dynamics in Expressive 3D Talking Avatars](2602.10516.md)
**Zhongju Wang, Zhenhong Sun, Beier Wang, Yifu Wang et al.** · 2026-02-11

<details>
<summary>Abstract</summary>

Audio-driven 3D talking avatar generation is increasingly important in virtual communication, digital humans, and interactive media, where avatars must preserve identity, synchronize lip motion with speech, express emotion, and exhibit lifelike spatial dynamics, collectively defining a broader objective of expressivity. However, achieving this remains challenging due to insufficient training data with limited subject identities, narrow audio representations, and restricted explicit controllability. In this paper, we propose 3DXTalker, an expressive 3D talking avatar through data-curated identity modeling, audio-rich representations, and spatial dynamics controllability. 3DXTalker enables scalable identity modeling via 2D-to-3D data curation pipeline and disentangled representations, alleviating data scarcity and improving identity generalization. Then, we introduce frame-wise amplitude and emotional cues beyond standard speech embeddings, ensuring superior lip synchronization and nuanced expression modulation. These cues are unified by a flow-matching-based transformer for coherent facial dynamics. Moreover, 3DXTalker also enables natural head-pose motion generation while supporting stylized control via prompt-based conditioning. Extensive experiments show that 3DXTalker integrates lip synchronization, emotional expression, and head-pose dynamics within a unified framework, achieves superior performance in 3D talking avatar generation.

</details>

### [AUHead: Realistic Emotional Talking Head Generation via Action Units Control](2602.09534.md)
**Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang et al.** · 2026-02-10

<details>
<summary>Abstract</summary>

Realistic talking-head video generation is critical for virtual avatars, film production, and interactive systems. Current methods struggle with nuanced emotional expressions due to the lack of fine-grained emotion control. To address this issue, we introduce a novel two-stage method (AUHead) to disentangle fine-grained emotion control, i.e. , Action Units (AUs), from audio and achieve controllable generation. In the first stage, we explore the AU generation abilities of large audio-language models (ALMs), by spatial-temporal AU tokenization and an "emotion-then-AU" chain-of-thought mechanism. It aims to disentangle AUs from raw speech, effectively capturing subtle emotional cues. In the second stage, we propose an AU-driven controllable diffusion model that synthesizes realistic talking-head videos conditioned on AU sequences. Specifically, we first map the AU sequences into the structured 2D facial representation to enhance spatial fidelity, and then model the AU-vision interaction within cross-attention modules. To achieve flexible AU-quality trade-off control, we introduce an AU disentanglement guidance strategy during inference, further refining the emotional expressiveness and identity consistency of the generated videos. Results on benchmark datasets demonstrate that our approach achieves competitive performance in emotional realism, accurate lip synchronization, and visual coherence, significantly surpassing existing techniques. Our implementation is available at https://github.com/laura990501/AUHead_ICLR

</details>

### [MOVA: Towards Scalable and Synchronized Video-Audio Generation](2602.08794.md)
**SII-OpenMOSS Team, :, Donghua Yu, Mingshu Chen et al.** · 2026-02-09

<details>
<summary>Abstract</summary>

Audio is indispensable for real-world video, yet generation models have largely overlooked audio components. Current approaches to producing audio-visual content often rely on cascaded pipelines, which increase cost, accumulate errors, and degrade overall quality. While systems such as Veo 3 and Sora 2 emphasize the value of simultaneous generation, joint multimodal modeling introduces unique challenges in architecture, data, and training. Moreover, the closed-source nature of existing systems limits progress in the field. In this work, we introduce MOVA (MOSS Video and Audio), an open-source model capable of generating high-quality, synchronized audio-visual content, including realistic lip-synced speech, environment-aware sound effects, and content-aligned music. MOVA employs a Mixture-of-Experts (MoE) architecture, with a total of 32B parameters, of which 18B are active during inference. It supports IT2VA (Image-Text to Video-Audio) generation task. By releasing the model weights and code, we aim to advance research and foster a vibrant community of creators. The released codebase features comprehensive support for efficient inference, LoRA fine-tuning, and prompt enhancement.

</details>

### [From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](2602.06122.md)
**Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro et al.** · 2026-02-05

<details>
<summary>Abstract</summary>

Creating high-fidelity, animatable 3D talking heads is crucial for immersive applications, yet often hindered by the prevalence of low-quality image or video sources, which yield poor 3D reconstructions. In this paper, we introduce SuperHead, a novel framework for enhancing low-resolution, animatable 3D head avatars. The core challenge lies in synthesizing high-quality geometry and textures, while ensuring both 3D and temporal consistency during animation and preserving subject identity. Despite recent progress in image, video and 3D-based super-resolution (SR), existing SR techniques are ill-equipped to handle dynamic 3D inputs. To address this, SuperHead leverages the rich priors from pre-trained 3D generative models via a novel dynamics-aware 3D inversion scheme. This process optimizes the latent representation of the generative model to produce a super-resolved 3D Gaussian Splatting (3DGS) head model, which is subsequently rigged to an underlying parametric head model (e.g., FLAME) for animation. The inversion is jointly supervised using a sparse collection of upscaled 2D face renderings and corresponding depth maps, captured from diverse facial expressions and camera viewpoints, to ensure realism under dynamic facial motions. Experiments demonstrate that SuperHead generates avatars with fine-grained facial details under dynamic motions, significantly outperforming baseline methods in visual quality.

</details>

### [A$^2$-LLM: An End-to-end Conversational Audio Avatar Large Language Model](2602.04913.md)
**Xiaolin Hu, Hang Yuan, Xinzhu Sang, Binbin Yan et al.** · 2026-02-04

<details>
<summary>Abstract</summary>

Developing expressive and responsive conversational digital humans is a cornerstone of next-generation human-computer interaction. While large language models (LLMs) have significantly enhanced dialogue capabilities, most current systems still rely on cascaded architectures that connect independent modules. These pipelines are often plagued by accumulated errors, high latency, and poor real-time performance. Lacking access to the underlying conversational context, these pipelines inherently prioritize rigid lip-sync over emotional depth. To address these challenges, we propose A$^2$-LLM, an end-to-end conversational audio avatar large language model that jointly reasons about language, audio prosody, and 3D facial motion within a unified framework. To facilitate training, we introduce FLAME-QA, a high-quality multimodal dataset designed to align semantic intent with expressive facial dynamics within a QA format. By leveraging deep semantic understanding, A$^2$-LLM generates emotionally rich facial movements beyond simple lip-synchronization. Experimental results demonstrate that our system achieves superior emotional expressiveness while maintaining real-time efficiency (500 ms latency, 0.7 RTF).

</details>

### [MIRRORTALK: Forging Personalized Avatars Via Disentangled Style and Hierarchical Motion Control](2601.22501.md)
**Renjie Lu, Xulong Zhang, Xiaoyang Qu, Jianzong Wang et al.** · 2026-01-30

<details>
<summary>Abstract</summary>

Synthesizing personalized talking faces that uphold and highlight a speaker's unique style while maintaining lip-sync accuracy remains a significant challenge. A primary limitation of existing approaches is the intrinsic confounding of speaker-specific talking style and semantic content within facial motions, which prevents the faithful transfer of a speaker's unique persona to arbitrary speech. In this paper, we propose MirrorTalk, a generative framework based on a conditional diffusion model, combined with a Semantically-Disentangled Style Encoder (SDSE) that can distill pure style representations from a brief reference video. To effectively utilize this representation, we further introduce a hierarchical modulation strategy within the diffusion process. This mechanism guides the synthesis by dynamically balancing the contributions of audio and style features across distinct facial regions, ensuring both precise lip-sync accuracy and expressive full-face dynamics. Extensive experiments demonstrate that MirrorTalk achieves significant improvements over state-of-the-art methods in terms of lip-sync accuracy and personalization preservation.

</details>

### [JUST-DUB-IT: Video Dubbing via Joint Audio-Visual Diffusion](2601.22143.md)
**Anthony Chen, Naomi Ken Korem, Tavi Halperin, Matan Ben Yosef et al.** · 2026-01-29

<details>
<summary>Abstract</summary>

Audio-Visual Foundation Models, which are pretrained to jointly generate sound and visual content, have recently shown an unprecedented ability to model multi-modal generation and editing, opening new opportunities for downstream tasks. Among these tasks, video dubbing could greatly benefit from such priors, yet most existing solutions still rely on complex, task-specific pipelines that struggle in real-world settings. In this work, we introduce a single-model approach that adapts a foundational audio-video diffusion model for video-to-video dubbing via a lightweight LoRA. The LoRA enables the model to condition on an input audio-video while jointly generating translated audio and synchronized facial motion. To train this LoRA, we leverage the generative model itself to synthesize paired multilingual videos of the same speaker. Specifically, we generate multilingual videos with language switches within a single clip, and then inpaint the face and audio in each half to match the language of the other half. By leveraging the rich generative prior of the audio-visual model, our approach preserves speaker identity and lip synchronization while remaining robust to complex motion and real-world dynamics. We demonstrate that our approach produces high-quality dubbed videos with improved visual fidelity, lip synchronization, and robustness compared to existing dubbing pipelines.

</details>

### [EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers](2601.22127.md)
**John Flynn, Wolfgang Paier, Dimitar Dinev, Sam Nhut Nguyen et al.** · 2026-01-29

<details>
<summary>Abstract</summary>

Current generative video models excel at producing novel content from text and image prompts, but leave a critical gap in editing existing pre-recorded videos, where minor alterations to the spoken script require preserving motion, temporal coherence, speaker identity, and accurate lip synchronization. We introduce EditYourself, a DiT-based framework for audio-driven video-to-video (V2V) editing that enables transcript-based modification of talking head videos, including the seamless addition, removal, and retiming of visually spoken content. Building on a general-purpose video diffusion model, EditYourself augments its V2V capabilities with audio conditioning and region-aware, edit-focused training extensions. This enables precise lip synchronization and temporally coherent restructuring of existing performances via spatiotemporal inpainting, including the synthesis of realistic human motion in newly added segments, while maintaining visual fidelity and identity consistency over long durations. This work represents a foundational step toward generative video models as practical tools for professional video post-production.

</details>

### [Lightweight High-Fidelity Low-Bitrate Talking Face Compression for 3D Video Conference](2601.21269.md)
**Jianglong Li, Jun Xu, Bingcong Lu, Zhengxue Cheng et al.** · 2026-01-29

<details>
<summary>Abstract</summary>

The demand for immersive and interactive communication has driven advancements in 3D video conferencing, yet achieving high-fidelity 3D talking face representation at low bitrates remains a challenge. Traditional 2D video compression techniques fail to preserve fine-grained geometric and appearance details, while implicit neural rendering methods like NeRF suffer from prohibitive computational costs. To address these challenges, we propose a lightweight, high-fidelity, low-bitrate 3D talking face compression framework that integrates FLAME-based parametric modeling with 3DGS neural rendering. Our approach transmits only essential facial metadata in real time, enabling efficient reconstruction with a Gaussian-based head model. Additionally, we introduce a compact representation and compression scheme, including Gaussian attribute compression and MLP optimization, to enhance transmission efficiency. Experimental results demonstrate that our method achieves superior rate-distortion performance, delivering high-quality facial rendering at extremely low bitrates, making it well-suited for real-time 3D video conferencing applications.

</details>

### [Audio-Driven Talking Face Generation with Blink Embedding and Hash Grid Landmarks Encoding](2601.18849.md)
**Yuhui Zhang, Hui Yu, Wei Liang, Sunjie Zhang** · 2026-01-26

<details>
<summary>Abstract</summary>

Dynamic Neural Radiance Fields (NeRF) have demonstrated considerable success in generating high-fidelity 3D models of talking portraits. Despite significant advancements in the rendering speed and generation quality, challenges persist in accurately and efficiently capturing mouth movements in talking portraits. To tackle this challenge, we propose an automatic method based on blink embedding and hash grid landmarks encoding in this study, which can substantially enhance the fidelity of talking faces. Specifically, we leverage facial features encoded as conditional features and integrate audio features as residual terms into our model through a Dynamic Landmark Transformer. Furthermore, we employ neural radiance fields to model the entire face, resulting in a lifelike face representation. Experimental evaluations have validated the superiority of our approach to existing methods.

</details>

### [FunCineForge: A Unified Dataset Toolkit and Model for Zero-Shot Movie Dubbing in Diverse Cinematic Scenes](2601.14777.md)
**Jiaxuan Liu, Yang Xiang, Han Zhao, Xiangang Li et al.** · 2026-01-21

<details>
<summary>Abstract</summary>

Movie dubbing is the task of synthesizing speech from scripts conditioned on video scenes, requiring accurate lip sync, faithful timbre transfer, and proper modeling of character identity and emotion. However, existing methods face two major limitations: (1) high-quality multimodal dubbing datasets are limited in scale, suffer from high word error rates, contain sparse annotations, rely on costly manual labeling, and are restricted to monologue scenes, all of which hinder effective model training; (2) existing dubbing models rely solely on the lip region to learn audio-visual alignment, which limits their applicability to complex live-action cinematic scenes, and exhibit suboptimal performance in lip sync, speech quality, and emotional expressiveness. To address these issues, we propose FunCineForge, which comprises an end-to-end production pipeline for large-scale dubbing datasets and an MLLM-based dubbing model designed for diverse cinematic scenes. Using the pipeline, we construct the first Chinese television dubbing dataset with rich annotations, and demonstrate the high quality of these data. Experiments across monologue, narration, dialogue, and multi-speaker scenes show that our dubbing model consistently outperforms SOTA methods in audio quality, lip sync, timbre transfer, and instruction following. Code and demos are available at https://anonymous.4open.science/w/FunCineForge.

</details>

### [Audio-driven single image talking face animation with transformers](s2:8728bdcb4f6492c5cd9541df88d1b79ad351ded8.md)
**Yixin Li, Xizhong Shen** · 2026-01-19

<details>
<summary>Abstract</summary>

Audio-driven talking-head video generation is a critical task in cross-modal expressive synthesis, with applications in virtual humans, digital content creation, and human-computer interaction. Existing methods, however, often suffer from unnatural lip movements and distortions in non-speech facial regions, especially under exaggerated expressions or emotional variations. These issues arise due to the entanglement of linguistic content, prosodic emotion, and speaker-specific attributes within the audio signal. To address these challenges, we propose ExpNet, a Transformer-based expression regression framework that decouples global head motion from local facial expressions using 3DMM coefficients. The method employs a conditional VAE for robust head pose coefficient generation, while a CNN-Transformer architecture regresses expression coefficients. ExpNet introduces ALiBi-based relative positional bias in the self-attention mechanism, which captures long-range dependencies while focusing on local temporal context. It also conditions on the first-frame expression coefficient to preserve identity and emotion consistency throughout the video. Experimental evaluations on multiple datasets, including HDTF, MEAD, and LRS3, demonstrate that the method presented in this paper outperforms existing methods in terms of expression realism, lip synchronization, and video quality. Ablation studies reveal that key components such as ALiBi, landmark supervision, and the Transformer module are crucial for improving temporal stability, reducing lip jitter, and enhancing overall facial animation consistency.

</details>

### [Now You See Me, Now You Don't: A Unified Framework for Expression Consistent Anonymization in Talking Head Videos](2601.11635.md)
**Anil Egin, Andrea Tangherloni, Antitza Dantcheva** · 2026-01-14

<details>
<summary>Abstract</summary>

Face video anonymization is aimed at privacy preservation while allowing for the analysis of videos in a number of computer vision downstream tasks such as expression recognition, people tracking, and action recognition. We propose here a novel unified framework referred to as Anon-NET, streamlined to de-identify facial videos, while preserving age, gender, race, pose, and expression of the original video. Specifically, we inpaint faces by a diffusion-based generative model guided by high-level attribute recognition and motion-aware expression transfer. We then animate deidentified faces by video-driven animation, which accepts the de-identified face and the original video as input. Extensive experiments on the datasets VoxCeleb2, CelebV-HQ, and HDTF, which include diverse facial dynamics, demonstrate the effectiveness of AnonNET in obfuscating identity while retaining visual realism and temporal consistency. The code of AnonNet will be publicly released.

</details>

### [MANGO:Natural Multi-speaker 3D Talking Head Generation via 2D-Lifted Enhancement](2601.01749.md)
**Lei Zhu, Lijian Lin, Ye Zhu, Jiahao Wu et al.** · 2026-01-05

<details>
<summary>Abstract</summary>

Current audio-driven 3D head generation methods mainly focus on single-speaker scenarios, lacking natural, bidirectional listen-and-speak interaction. Achieving seamless conversational behavior, where speaking and listening states transition fluidly remains a key challenge. Existing 3D conversational avatar approaches rely on error-prone pseudo-3D labels that fail to capture fine-grained facial dynamics. To address these limitations, we introduce a novel two-stage framework MANGO, which leveraging pure image-level supervision by alternately training to mitigate the noise introduced by pseudo-3D labels, thereby achieving better alignment with real-world conversational behaviors. Specifically, in the first stage, a diffusion-based transformer with a dual-audio interaction module models natural 3D motion from multi-speaker audio. In the second stage, we use a fast 3D Gaussian Renderer to generate high-fidelity images and provide 2D-level photometric supervision for the 3D motions through alternate training. Additionally, we introduce MANGO-Dialog, a high-quality dataset with over 50 hours of aligned 2D-3D conversational data across 500+ identities. Extensive experiments demonstrate that our method achieves exceptional accuracy and realism in modeling two-person 3D dialogue motion, significantly advancing the fidelity and controllability of audio-driven talking heads.

</details>

### [MM-Sonate: Multimodal Controllable Audio-Video Generation with Zero-Shot Voice Cloning](2601.01568.md)
**Chunyu Qiang, Jun Wang, Xiaopeng Wang, Kang Yin et al.** · 2026-01-04

<details>
<summary>Abstract</summary>

Joint audio-video generation aims to synthesize synchronized multisensory content, yet current unified models struggle with fine-grained acoustic control, particularly for identity-preserving speech. Existing approaches either suffer from temporal misalignment due to cascaded generation or lack the capability to perform zero-shot voice cloning within a joint synthesis framework. In this work, we present MM-Sonate, a multimodal flow-matching framework that unifies controllable audio-video joint generation with zero-shot voice cloning capabilities. Unlike prior works that rely on coarse semantic descriptions, MM-Sonate utilizes a unified instruction-phoneme input to enforce strict linguistic and temporal alignment. To enable zero-shot voice cloning, we introduce a timbre injection mechanism that effectively decouples speaker identity from linguistic content. Furthermore, addressing the limitations of standard classifier-free guidance in multimodal settings, we propose a noise-based negative conditioning strategy that utilizes natural noise priors to significantly enhance acoustic fidelity. Empirical evaluations demonstrate that MM-Sonate establishes new state-of-the-art performance in joint generation benchmarks, significantly outperforming baselines in lip synchronization and speech intelligibility, while achieving voice cloning fidelity comparable to specialized Text-to-Speech systems.

</details>

### [Emotionally Controllable Audio-driven Talking Face Generation](s2:599c27a3333605649161d905c21060d190becf2d.md)
**Yifan Xu, Sirui Zhao, Shifeng Liu, Tong Xu et al.** · 2026-01-03

<details>
<summary>Abstract</summary>

Talking face generation is a technique that synthesizes realistic, speech-synchronized facial animations from static images driven by audio or textual input. In recent years, notable advancements have been achieved in the generation of realistic lip-synchronized talking face videos. Although these methods have demonstrated highly realistic results in lip-sync generation, they rarely focus on the expression of emotions, which is essential for achieving emotionally rich and lifelike talking face videos. In this article, we propose a novel emotionally controllable audio-driven talking face generation framework, termed ECATFG. Specifically, the proposed ECATFG mainly consists of three modules: template video generator, landmark generator, and rendering module. Firstly, we integrate a customized motion transfer module into StyleGAN to generate template videos that encapsulate the target emotions and head movements. Subsequently, a Mamba-based landmark generator is proposed to accurately model the correlation between input audio and facial landmarks. Afterwards, in the rendering module, we employ a framework that combines both AdaIN and SPADE layers to transform audio-predicted landmarks into highly realistic images, guided by reference images and facial contour landmarks. Finally, comprehensive experiments validate the effectiveness of ECATFG, demonstrating its capability to generate high-quality talking face videos that not only achieve exceptional lip-synchronization accuracy but also effectively convey a wide range of emotions.

</details>

### [Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation](2601.00664.md)
**Taekyung Ki, Sangwon Jang, Jaehyeong Jo, Jaehong Yoon et al.** · 2026-01-02

<details>
<summary>Abstract</summary>

Talking head generation creates lifelike avatars from static portraits for virtual communication and content creation. However, current models do not yet convey the feeling of truly interactive communication, often generating one-way responses that lack emotional engagement. We identify two key challenges toward truly interactive avatars: generating motion in real-time under causal constraints and learning expressive, vibrant reactions without additional labeled data. To address these challenges, we propose Avatar Forcing, a new framework for interactive head avatar generation that models real-time user-avatar interactions through diffusion forcing. This design allows the avatar to process real-time multimodal inputs, including the user's audio and motion, with low latency for instant reactions to both verbal and non-verbal cues such as speech, nods, and laughter. Furthermore, we introduce a direct preference optimization method that leverages synthetic losing samples constructed by dropping user conditions, enabling label-free learning of expressive interaction. Experimental results demonstrate that our framework enables real-time interaction with low latency (approximately 500ms), achieving 6.8X speedup compared to the baseline, and produces reactive and expressive avatar motion, which is preferred over 80% against the baseline.

</details>

### [EMTA: End-to-End Multi-Task Audio-Driven Talking-Head Animation](s2:1c5597407caf0c273264e4ba1283cb9722cb3c54.md)
**L. Venkatesan, Divya Choudhary, Sai G, Subhajeet Lahiri et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

: Audio-Driven facial animation has advanced rapidly, yet most methods remain task-specific (e.g., reenactment, dubbing) and domain-locked (2D or 3D). This fragmentation limits flexibility across applications like telep-resence and AR/VR. We introduce EMTA , an end-to-end, identity-preserving framework that unifies multiple audio-driven tasks within a unified architecture. EMTA decouples audio-to-geometry from geometry-to-appearance generation: (1) Audio2Mesh predicts expressive, temporally coherent 3D facial landmarks from audio and employs a novel rotation decoder module, directly usable for 3D avatars; and (2) LaPix-GAN synthesizes photorealistic 2D frames through an identity-aware generator, a novel Audio-Gated Spatial Attention (AGSA) module, and enhanced Facial-Inpainted Landmark (FIL) sketches. EMTA achieves robust and competitive results across 3D mesh prediction, 2D reenactment, talking portraits, and dubbing tasks against baselines on multiple datasets, validating it as a flexible and practical solution (25 FPS).

</details>

### [High-fidelity and Lip-synced Talking Face Synthesis via Landmark-based Diffusion Model](s2:d3e3159653a29ff817335f8db6da5ef03409a191.md)
**Wei‐Tao Zhong, Junfan Lin, Peixin Chen, Feng Gao et al.** · 2026-01-01

### [Enhanced Audio-Visual Speech Synthesis via Multi-Discriminative Learning](s2:aad984cc65c272b2610d4f852fe05062a71bfa30.md)
**Subhayu Ghosh, Frank Zalkow, N. D. Jana** · 2026-01-01

<details>
<summary>Abstract</summary>

Audio-visual speech synthesis (AVSS) aims to produce an audio-visual stream that conveys a target speaker’s speech. In this study, the AVSS system takes the input speech of a source speaker and generates the audio-visual stream of the target speaker while preserving the linguistic content of the source speech. The process involves two main components: voice conversion (VC), which adapts the vocal features from the source to the target speaker, and audio-visual synthesis (AVS), which generates the synchronized audio-visual stream from the transformed speech. This paper presents a novel generative framework based on multi-discriminative learning to enhance the realism and quality of AVSS outputs. The proposed approach integrates multiple discriminators, including capsule networks, co-occurrence neural networks, and vision transformers (ViTs), within the VC model to leverage their unique strengths in capturing diverse speech features. Additionally, the AVS model incorporates a co-occurrence neural network to improve video quality and achieve better temporal alignment between audio and visual data. Experimental evaluations on standard benchmarks demonstrate that the proposed method achieves significant improvements in both audio and video quality, offering a substantial advancement in AVSS technology.

</details>

### [Viseme-Gated Multilayer Cross-Attentional Feature Fusion for Cognitively-Inspired Multimodal Speech Enhancement](s2:c2772c139c0efc437de2fe000580c6d0a0519a2b.md)
**Nasir Saleem, Adeel Hussain, K. Dashtipour, Eamon Sheikh et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

Human speech perception naturally integrates visual and auditory cues, with lip movements providing critical disambiguation in noisy environments where audio signals are degraded (SNR $\leq$ −5 dB). While existing audio-visual speech enhancement (AVSE) models use this multimodal synergy, they often fail to exploit phoneme-specific viseme correlations. We propose VG-MCA-AVSENet, a cognitively inspired architecture that introduces a viseme-gated multilayer cross-attention mechanism within a convolutional encoder-decoder framework. The model dynamically weights visual features using auditory context and learned viseme importance (prioritizing lip closures for plosives), while maintaining efficiency through depthwise separable convolutions and MobileNetV3-based visual encoding. Our AVSE system comprises an audio encoder, visual encoder with temporal modeling, separation module with 3-layer viseme-aware attention, and neural vocoder decoder. Evaluated on GRID-CHiME, NTCD-TIMIT, and LRS3 datasets, the model achieves 72.58% STOI (+12.28% over baseline), 2.56 PESQ, and 7.80 dB SI-SDR in extreme noise conditions (SNR$\leq$ -6 dB). The viseme gating specifically improves plosive intelligibility by 7% with a few additional parameters, showing that explicit phoneme-viseme modeling significantly outperforms conventional approaches.

</details>

### [Audiovisual speech enhancement and voice activity detection using generative and regressive visual features](s2:39f39c0552dada9cc7cef73426ef4adde6a9a344.md)
**Cheng Yu, Vahid Ahmadi Kalkhorani, Buye Xu, DeLiang Wang** · 2026-01-01

### [Noise Aware Audio-Visual Speech Denoising](s2:dbcded4bcf7c4268ff42855798170765cec7767e.md)
**Kranti K. Parida, Siddharth Srivastava, Gaurav Sharma** · 2026-01-01

<details>
<summary>Abstract</summary>

We address the problem of speech denoising where the goal is to extract clean speech signal from a noisy signal. Traditionally, the task of denoising has been performed using audio modality only. However, human speech perception is inherently multimodal where cues from visual modality are used to understand the speech better in a noisy environment. Similar observation has been made with computational denoising methods, i.e., performance of audio only model improves after adding visual modality. Inspired by these findings we propose a novel audio-visual network for adaptively combining both modalities for the task of speech audio denoising. We show that extracting noise from mixed audio and using it as a conditioning signal, improves speech denoising performance. To estimate the noise, we use both audio and visual modalities, i.e., lip region of the speaker, to extract the non-speech/silent regions from it. The silent regions enable us to estimate better noise profile to eliminate from the signal. Our proposed network uses self and cross attention framework between audio and video features, along the temporal dimension, to model correlations between the two modalities. We evaluate the proposed approach on a large scale audio-visual dataset VoxCeleb2 and obtain state-of-the-art results. We also demonstrate generalization to unseen speakers at test time.

</details>

