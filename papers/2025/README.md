# 2025

158 papers in this year.

### [From Inpainting to Editing: A Self-Bootstrapping Framework for Context-Rich Visual Dubbing](2512.25066.md)
**Xu He, Haoxian Zhang, Hejia Chen, Changyuan Zheng et al.** · 2025-12-31

<details>
<summary>Abstract</summary>

Audio-driven visual dubbing aims to synchronize a video's lip movements with new speech, but is fundamentally challenged by the lack of ideal training data: paired videos where only a subject's lip movements differ while all other visual conditions are identical. Existing methods circumvent this with a mask-based inpainting paradigm, where an incomplete visual conditioning forces models to simultaneously hallucinate missing content and sync lips, leading to visual artifacts, identity drift, and poor synchronization. In this work, we propose a novel self-bootstrapping framework that reframes visual dubbing from an ill-posed inpainting task into a well-conditioned video-to-video editing problem. Our approach employs a Diffusion Transformer, first as a data generator, to synthesize ideal training data: a lip-altered companion video for each real sample, forming visually aligned video pairs. A DiT-based audio-driven editor is then trained on these pairs end-to-end, leveraging the complete and aligned input video frames to focus solely on precise, audio-driven lip modifications. This complete, frame-aligned input conditioning forms a rich visual context for the editor, providing it with complete identity cues, scene interactions, and continuous spatiotemporal dynamics. Leveraging this rich context fundamentally enables our method to achieve highly accurate lip sync, faithful identity preservation, and exceptional robustness against challenging in-the-wild scenarios. We further introduce a timestep-adaptive multi-phase learning strategy as a necessary component to disentangle conflicting editing objectives across diffusion timesteps, thereby facilitating stable training and yielding enhanced lip synchronization and visual fidelity. Additionally, we propose ContextDubBench, a comprehensive benchmark dataset for robust evaluation in diverse and challenging practical application scenarios.

</details>

### [DyStream: Streaming Dyadic Talking Heads Generation via Flow Matching-based Autoregressive Model](2512.24408.md)
**Bohong Chen, Haiyang Liu** · 2025-12-30

<details>
<summary>Abstract</summary>

Generating realistic, dyadic talking head video requires ultra-low latency. Existing chunk-based methods require full non-causal context windows, introducing significant delays. This high latency critically prevents the immediate, non-verbal feedback required for a realistic listener. To address this, we present DyStream, a flow matching-based autoregressive model that could generate video in real-time from both speaker and listener audio. Our method contains two key designs: (1) we adopt a stream-friendly autoregressive framework with flow-matching heads for probabilistic modeling, and (2) We propose a causal encoder enhanced by a lookahead module to incorporate short future context (e.g., 60 ms) to improve quality while maintaining low latency. Our analysis shows this simple-and-effective method significantly surpass alternative causal strategies, including distillation and generative encoder. Extensive experiments show that DyStream could generate video within 34 ms per frame, guaranteeing the entire system latency remains under 100 ms. Besides, it achieves state-of-the-art lip-sync quality, with offline and online LipSync Confidence scores of 8.13 and 7.61 on HDTF, respectively. The model, weights and codes are available.

</details>

### [Accelerating LatentSync Lip-Synchronization via OmniQuant-Inspired Post-Training Quantization](s2:b2a9ada0ddddf56534fc4d6822f442ea1d93edea.md)
**Guolin Wang** · 2025-12-26

<details>
<summary>Abstract</summary>

Lip-synchronization models play an important role in audio-driven facial animation and virtual human applications. LatentSync is a representative latent-based lip synchronization model that achieves high-quality temporal alignment between audio and visual modalities. However, the inference process of LatentSync relies on deep neural network components with considerable computational cost, which limits its deployment in real-time and resource-constrained scenarios. In this paper, we investigate an OmniQuant-inspired posttraining quantization (PTQ) strategy to accelerate the inference of the LatentSync lip-synchronization model. By applying INT8 weight-only quantization to the core generative backbone, the proposed method significantly reduces model size and inference latency without requiring retraining. The proposed approach follows the calibration principles of OmniQuant, including adaptive weight clipping and equivalent transformation, to mitigate quantization-induced performance degradation. Experimental results show that the proposed approach achieves noticeable inference acceleration and model compression, with no obvious functional degradation observed during empirical evaluation. These results demonstrate that OmniQuant-inspired post-training quantization provides a practical and efficient solution for accelerating lip-synchronization models in real-world applications.

</details>

### [SyncAnyone: Implicit Disentanglement via Progressive Self-Correction for Lip-Syncing in the wild](2512.21736.md)
**Xindi Zhang, Dechao Meng, Steven Xiao, Qi Wang et al.** · 2025-12-25

<details>
<summary>Abstract</summary>

High-quality AI-powered video dubbing demands precise audio-lip synchronization, high-fidelity visual generation, and faithful preservation of identity and background. Most existing methods rely on a mask-based training strategy, where the mouth region is masked in talking-head videos, and the model learns to synthesize lip movements from corrupted inputs and target audios. While this facilitates lip-sync accuracy, it disrupts spatiotemporal context, impairing performance on dynamic facial motions and causing instability in facial structure and background consistency. To overcome this limitation, we propose SyncAnyone, a novel two-stage learning framework that achieves accurate motion modeling and high visual fidelity simultaneously. In Stage 1, we train a diffusion-based video transformer for masked mouth inpainting, leveraging its strong spatiotemporal modeling to generate accurate, audio-driven lip movements. However, due to input corruption, minor artifacts may arise in the surrounding facial regions and the background. In Stage 2, we develop a mask-free tuning pipeline to address mask-induced artifacts. Specifically, on the basis of the Stage 1 model, we develop a data generation pipeline that creates pseudo-paired training samples by synthesizing lip-synced videos from the source video and random sampled audio. We further tune the stage 2 model on this synthetic data, achieving precise lip editing and better background consistency. Extensive experiments show that our method achieves state-of-the-art results in visual quality, temporal coherence, and identity preservation under in-the wild lip-syncing scenarios.

</details>

### [TAVID: Text-Driven Audio-Visual Interactive Dialogue Generation](2512.20296.md)
**Ji-Hoon Kim, Junseok Ahn, Doyeop Kwak, Joon Son Chung et al.** · 2025-12-23

<details>
<summary>Abstract</summary>

The objective of this paper is to jointly synthesize interactive videos and conversational speech from text and reference images. With the ultimate goal of building human-like conversational systems, recent studies have explored talking or listening head generation as well as conversational speech generation. However, these works are typically studied in isolation, overlooking the multimodal nature of human conversation, which involves tightly coupled audio-visual interactions. In this paper, we introduce TAVID, a unified framework that generates both interactive faces and conversational speech in a synchronized manner. TAVID integrates face and speech generation pipelines through two cross-modal mappers (i.e., a motion mapper and a speaker mapper), which enable bidirectional exchange of complementary information between the audio and visual modalities. We evaluate our system across four dimensions: talking face realism, listening head responsiveness, dyadic interaction fluency, and speech quality. Extensive experiments demonstrate the effectiveness of our approach across all these aspects.

</details>

### [In-Context Audio Control of Video Diffusion Transformers](2512.18772.md)
**Wenze Liu, Weicai Ye, Minghong Cai, Quande Liu et al.** · 2025-12-21

<details>
<summary>Abstract</summary>

Recent advancements in video generation have seen a shift towards unified, transformer-based foundation models that can handle multiple conditional inputs in-context. However, these models have primarily focused on modalities like text, images, and depth maps, while strictly time-synchronous signals like audio have been underexplored. This paper introduces In-Context Audio Control of video diffusion transformers (ICAC), a framework that investigates the integration of audio signals for speech-driven video generation within a unified full-attention architecture, akin to FullDiT. We systematically explore three distinct mechanisms for injecting audio conditions: standard cross-attention, 2D self-attention, and unified 3D self-attention. Our findings reveal that while 3D attention offers the highest potential for capturing spatio-temporal audio-visual correlations, it presents significant training challenges. To overcome this, we propose a Masked 3D Attention mechanism that constrains the attention pattern to enforce temporal alignment, enabling stable training and superior performance. Our experiments demonstrate that this approach achieves strong lip synchronization and video quality, conditioned on an audio stream and reference images.

</details>

### [Asynchronous Pipeline Parallelism for Real-Time Multilingual Lip Synchronization in Video Communication Systems](2512.18318.md)
**Eren Caglar, Amirkia Rafiei Oskooei, Mehmet Kutanoglu, Mustafa Keles et al.** · 2025-12-20

<details>
<summary>Abstract</summary>

This paper introduces a parallel and asynchronous Transformer framework designed for efficient and accurate multilingual lip synchronization in real-time video conferencing systems. The proposed architecture integrates translation, speech processing, and lip-synchronization modules within a pipeline-parallel design that enables concurrent module execution through message-queue-based decoupling, reducing end-to-end latency by up to 3.1 times compared to sequential approaches. To enhance computational efficiency and throughput, the inference workflow of each module is optimized through low-level graph compilation, mixed-precision quantization, and hardware-accelerated kernel fusion. These optimizations provide substantial gains in efficiency while preserving model accuracy and visual quality. In addition, a context-adaptive silence-detection component segments the input speech stream at semantically coherent boundaries, improving translation consistency and temporal alignment across languages. Experimental results demonstrate that the proposed parallel architecture outperforms conventional sequential pipelines in processing speed, synchronization stability, and resource utilization. The modular, message-oriented design makes this work applicable to resource-constrained IoT communication scenarios including telemedicine, multilingual kiosks, and remote assistance systems. Overall, this work advances the development of low-latency, resource-efficient multimodal communication frameworks for next-generation AIoT systems.

</details>

### [3D Face Animation Generation Method Based on Self-Supervised Speech Coding and Lattice Convolutional Architecture](s2:40f7cbd9952048787b5ae47712473017f2927ff5.md)
**Yunying Wang** · 2025-12-20

<details>
<summary>Abstract</summary>

Existing 3D face animation generation methods focus on lip movement and audio synchronization, ignoring the ability to synchronize expressions and poses. To address this problem, the study proposes a Self-Supervised Speech-Driven 3D Face Animation via Lattice Convolution Networks. The study first selected students from a certain school to read aloud the same corpus and record audio and video as the dataset. Through self-supervised learning and encoder-decoder structure, the speech features were extracted and mapped, and the obtained facial parameters were applied to the Face Latent Animated Mesh Estimator model to achieve lip-sync. Then, by combining the optical flow information in the video stream with the changes of facial key points, the grid convolutional network is used to model the expression dynamics and head postures, achieving multimodal feature fusion. In the experiment of analyzing the naturalness and accuracy of the generated animation, the lip shape vertex error, naturalness score, lip reading character error rate, and pixel error rate of the proposed method were only 2.54mm ², 9.45, 2.34%, and 2.53% respectively. In the performance analysis experiment of the emotion and posture recognition model, the accuracy rate of expression recognition and the posture offset error were 92.34% and 1.2° respectively. The lighting sensitivity, micro-expression fidelity and rendering frame rate of the generated face animation were 5.01, 93.48% and 63.74FPS respectively. The proposed 3D face animation generation method can effectively improve the realism and synchronization of the animation and achieve more accurate face animation generation.

</details>

### [InstructDubber: Instruction-based Alignment for Zero-shot Movie Dubbing](2512.17154.md)
**Zhedong Zhang, Liang Li, Gaoxiang Cong, Chunshan Liu et al.** · 2025-12-19

<details>
<summary>Abstract</summary>

Movie dubbing seeks to synthesize speech from a given script using a specific voice, while ensuring accurate lip synchronization and emotion-prosody alignment with the character's visual performance. However, existing alignment approaches based on visual features face two key limitations: (1)they rely on complex, handcrafted visual preprocessing pipelines, including facial landmark detection and feature extraction; and (2) they generalize poorly to unseen visual domains, often resulting in degraded alignment and dubbing quality. To address these issues, we propose InstructDubber, a novel instruction-based alignment dubbing method for both robust in-domain and zero-shot movie dubbing. Specifically, we first feed the video, script, and corresponding prompts into a multimodal large language model to generate natural language dubbing instructions regarding the speaking rate and emotion state depicted in the video, which is robust to visual domain variations. Second, we design an instructed duration distilling module to mine discriminative duration cues from speaking rate instructions to predict lip-aligned phoneme-level pronunciation duration. Third, for emotion-prosody alignment, we devise an instructed emotion calibrating module, which finetunes an LLM-based instruction analyzer using ground truth dubbing emotion as supervision and predicts prosody based on the calibrated emotion analysis. Finally, the predicted duration and prosody, together with the script, are fed into the audio decoder to generate video-aligned dubbing. Extensive experiments on three major benchmarks demonstrate that InstructDubber outperforms state-of-the-art approaches across both in-domain and zero-shot scenarios.

</details>

### [SynergyWarpNet: Attention-Guided Cooperative Warping for Neural Portrait Animation](2512.17331.md)
**Shihang Li, Zhiqiang Gong, Minming Ye, Yue Gao et al.** · 2025-12-19

<details>
<summary>Abstract</summary>

Recent advances in neural portrait animation have demonstrated remarked potential for applications in virtual avatars, telepresence, and digital content creation. However, traditional explicit warping approaches often struggle with accurate motion transfer or recovering missing regions, while recent attention-based warping methods, though effective, frequently suffer from high complexity and weak geometric grounding. To address these issues, we propose SynergyWarpNet, an attention-guided cooperative warping framework designed for high-fidelity talking head synthesis. Given a source portrait, a driving image, and a set of reference images, our model progressively refines the animation in three stages. First, an explicit warping module performs coarse spatial alignment between the source and driving image using 3D dense optical flow. Next, a reference-augmented correction module leverages cross-attention across 3D keypoints and texture features from multiple reference images to semantically complete occluded or distorted regions. Finally, a confidence-guided fusion module integrates the warped outputs with spatially-adaptive fusing, using a learned confidence map to balance structural alignment and visual consistency. Comprehensive evaluations on benchmark datasets demonstrate state-of-the-art performance.

</details>

### [TalkPersonaDiff: High-Fidelity Speech-Driven 3D Facial Animation Generation via Unified Multimodal Synergistic Encoding and Dual-Style Modulation](s2:05fd46beb0bf6e21f12896e708fa6ea24afea52c.md)
**Ouyang Peng, Zhuoyuan Yu, Tong Wu, Zhiqiang Zhang** · 2025-12-19

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation is critical for virtual humans, yet balancing Long-term Identity Consistency and Fine-grained Lip-sync in long sequences remains challenging. We propose TalkPersonaDiff, a conditional diffusion framework featuring a Unified Multimodal Synergistic Encoder to align speech semantics and identity priors in a latent space. Furthermore, to mitigate condition forgetting, we design a Dual-Style Modulation Mechanism that employs global injection and local re-weighting to maintain conditional efficacy throughout the denoising process. Experiments on BIWI and VOCASET demonstrate that TalkPersonaDiff outperforms mainstream methods in identity distinctiveness, lip-sync accuracy, and temporal smoothness, achieving high-fidelity, personalized 3D animation .

</details>

### [FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling](2512.14056.md)
**Kim Sung-Bin, Joohyun Chang, David Harwath, Tae-Hyun Oh** · 2025-12-16

<details>
<summary>Abstract</summary>

Talking face editing and face generation have often been studied as distinct problems. In this work, we propose viewing both not as separate tasks but as subtasks of a unifying formulation, speech-conditional facial motion infilling. We explore facial motion infilling as a self-supervised pretext task that also serves as a unifying formulation of dynamic talking face synthesis. To instantiate this idea, we propose FacEDiT, a speech-conditional Diffusion Transformer trained with flow matching. Inspired by masked autoencoders, FacEDiT learns to synthesize masked facial motions conditioned on surrounding motions and speech. This formulation enables both localized generation and edits, such as substitution, insertion, and deletion, while ensuring seamless transitions with unedited regions. In addition, biased attention and temporal smoothness constraints enhance boundary continuity and lip synchronization. To address the lack of a standard editing benchmark, we introduce FacEDiTBench, the first dataset for talking face editing, featuring diverse edit types and lengths, along with new evaluation metrics. Extensive experiments validate that talking face editing and generation emerge as subtasks of speech-conditional motion infilling; FacEDiT produces accurate, speech-aligned facial edits with strong identity preservation and smooth visual continuity while generalizing effectively to talking face generation.

</details>

### [JoVA: Unified Multimodal Learning for Joint Video-Audio Generation](2512.13677.md)
**Xiaohu Huang, Hao Zhou, Qiangpeng Yang, Shilei Wen et al.** · 2025-12-15

<details>
<summary>Abstract</summary>

In this paper, we present JoVA, a unified framework for joint video-audio generation. Despite recent encouraging advances, existing methods face two critical limitations. First, most existing approaches can only generate ambient sounds and lack the capability to produce human speech synchronized with lip movements. Second, recent attempts at unified human video-audio generation typically rely on explicit fusion or modality-specific alignment modules, which introduce additional architecture design and weaken the model simplicity of the original transformers. To address these issues, JoVA employs joint self-attention across video and audio tokens within each transformer layer, enabling direct and efficient cross-modal interaction without the need for additional alignment modules. Furthermore, to enable high-quality lip-speech synchronization, we introduce a simple yet effective mouth-area loss based on facial keypoint detection, which enhances supervision on the critical mouth region during training without compromising architectural simplicity. Extensive experiments on benchmarks demonstrate that JoVA outperforms or is competitive with both unified and audio-driven state-of-the-art methods in lip-sync accuracy, speech quality, and overall video-audio generation fidelity. Our results establish JoVA as an elegant framework for high-quality multimodal generation.

</details>

### [Soul: Breathe Life into Digital Human for High-fidelity Long-term Multimodal Animation](2512.13495.md)
**Jiangning Zhang, Junwei Zhu, Zhenye Gan, Donghao Luo et al.** · 2025-12-15

<details>
<summary>Abstract</summary>

We propose a multimodal-driven framework for high-fidelity long-term digital human animation termed $\textbf{Soul}$, which generates semantically coherent videos from a single-frame portrait image, text prompts, and audio, achieving precise lip synchronization, vivid facial expressions, and robust identity preservation. We construct Soul-1M, containing 1 million finely annotated samples with a precise automated annotation pipeline (covering portrait, upper-body, full-body, and multi-person scenes) to mitigate data scarcity, and we carefully curate Soul-Bench for comprehensive and fair evaluation of audio-/text-guided animation methods. The model is built on the Wan2.2-5B backbone, integrating audio-injection layers and multiple training strategies together with threshold-aware codebook replacement to ensure long-term generation consistency. Meanwhile, step/CFG distillation and a lightweight VAE are used to optimize inference efficiency, achieving an 11.4$\times$ speedup with negligible quality loss. Extensive experiments show that Soul significantly outperforms current leading open-source and commercial models on video quality, video-text alignment, identity preservation, and lip-synchronization accuracy, demonstrating broad applicability in real-world scenarios such as virtual anchors and film production. Project page at https://zhangzjn.github.io/projects/Soul/

</details>

### [KlingAvatar 2.0 Technical Report](2512.13313.md)
**Kling Team, Jialu Chen, Yikang Ding, Zhixue Fang et al.** · 2025-12-15

<details>
<summary>Abstract</summary>

Avatar video generation models have achieved remarkable progress in recent years. However, prior work exhibits limited efficiency in generating long-duration high-resolution videos, suffering from temporal drifting, quality degradation, and weak prompt following as video length increases. To address these challenges, we propose KlingAvatar 2.0, a spatio-temporal cascade framework that performs upscaling in both spatial resolution and temporal dimension. The framework first generates low-resolution blueprint video keyframes that capture global semantics and motion, and then refines them into high-resolution, temporally coherent sub-clips using a first-last frame strategy, while retaining smooth temporal transitions in long-form videos. To enhance cross-modal instruction fusion and alignment in extended videos, we introduce a Co-Reasoning Director composed of three modality-specific large language model (LLM) experts. These experts reason about modality priorities and infer underlying user intent, converting inputs into detailed storylines through multi-turn dialogue. A Negative Director further refines negative prompts to improve instruction alignment. Building on these components, we extend the framework to support ID-specific multi-character control. Extensive experiments demonstrate that our model effectively addresses the challenges of efficient, multimodally aligned long-form high-resolution video generation, delivering enhanced visual clarity, realistic lip-teeth rendering with accurate lip synchronization, strong identity preservation, and coherent multimodal instruction following.

</details>

### [JoyAvatar-Flash: Real-time and Infinite Audio-Driven Avatar Generation with Autoregressive Diffusion](2512.11423.md)
**Chaochao Li, Ruikui Wang, Liangbo Zhou, Jinheng Feng et al.** · 2025-12-12

<details>
<summary>Abstract</summary>

Existing DiT-based audio-driven avatar generation methods have achieved considerable progress, yet their broader application is constrained by limitations such as high computational overhead and the inability to synthesize long-duration videos. Autoregressive methods address this problem by applying block-wise autoregressive diffusion methods. However, these methods suffer from the problem of error accumulation and quality degradation. To address this, we propose JoyAvatar-Flash, an audio-driven autoregressive model capable of real-time inference and infinite-length video generation with the following contributions: (1) Progressive Step Bootstrapping (PSB), which allocates more denoising steps to initial frames to stabilize generation and reduce error accumulation; (2) Motion Condition Injection (MCI), enhancing temporal coherence by injecting noise-corrupted previous frames as motion condition; and (3) Unbounded RoPE via Cache-Resetting (URCR), enabling infinite-length generation through dynamic positional encoding. Our 1.3B-parameter causal model achieves 16 FPS on a single GPU and achieves competitive results in visual quality, temporal consistency, and lip synchronization.

</details>

### [REST: Diffusion-based Real-time End-to-end Streaming Talking Head Generation via ID-Context Caching and Asynchronous Streaming Distillation](2512.11229.md)
**Haotian Wang, Yuzhe Weng, Jun Du, Haoran Xu et al.** · 2025-12-12

<details>
<summary>Abstract</summary>

Diffusion models have significantly advanced the field of talking head generation (THG). However, slow inference speeds and prevalent non-autoregressive paradigms severely constrain the application of diffusion-based THG models. In this study, we propose REST, a pioneering diffusion-based, real-time, end-to-end streaming audio-driven talking head generation framework. To support real-time end-to-end generation, a compact video latent space is first learned through a spatiotemporal variational autoencoder with a high compression ratio. Additionally, to enable semi-autoregressive streaming within the compact video latent space, we introduce an ID-Context Cache mechanism, which integrates ID-Sink and Context-Cache principles into key-value caching for maintaining identity consistency and temporal coherence during long-term streaming generation. Furthermore, an Asynchronous Streaming Distillation (ASD) strategy is proposed to mitigate error accumulation and enhance temporal consistency in streaming generation, leveraging a non-streaming teacher with an asynchronous noise schedule to supervise the streaming student. REST bridges the gap between autoregressive and diffusion-based approaches, achieving a breakthrough in efficiency for applications requiring real-time THG. Experimental results demonstrate that REST outperforms state-of-the-art methods in both generation speed and overall performance.

</details>

### [GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](2512.10939.md)
**Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh** · 2025-12-11

<details>
<summary>Abstract</summary>

Speech-driven talking heads have recently emerged and enable interactive avatars. However, real-world applications are limited, as current methods achieve high visual fidelity but slow or fast yet temporally unstable. Diffusion methods provide realistic image generation, yet struggle with oneshot settings. Gaussian Splatting approaches are real-time, yet inaccuracies in facial tracking, or inconsistent Gaussian mappings, lead to unstable outputs and video artifacts that are detrimental to realistic use cases. We address this problem by mapping Gaussian Splatting using 3D Morphable Models to generate person-specific avatars. We introduce transformer-based prediction of model parameters, directly from audio, to drive temporal consistency. From monocular video and independent audio speech inputs, our method enables generation of real-time talking head videos where we report competitive quantitative and qualitative performance.

</details>

### [FlowTalk: Real-Time Audio-Driven Talking Head Synthesis via Motion-Space Flow Matching](s2:90b687acd9b3b1df39583c9cbf9a36e41fd13538.md)
**Kaijun Deng, Yuhang Guo, Linlin Shen** · 2025-12-08

<details>
<summary>Abstract</summary>

Audio-driven talking head synthesis has achieved significant progress, yet existing methods face critical trade-offs among generation quality, inference efficiency, and cross-ethnic generalization. Diffusion-based approaches produce high-fidelity results but suffer from slow inference due to iterative denoising, while GAN-based methods achieve faster speed at the cost of reduced motion naturalness and limited generalization. To address these challenges, we propose FlowTalk, a novel framework that enables real-time high-fidelity talking head video synthesis. Our approach leverages Flow Matching technology to perform efficient motion modeling in a decoupled motion space rather than pixel space, achieving significant speedup while maintaining generation quality. Specifically, we adopt an off-the-shelf motion extractor to disentangle facial appearance from motion, and employ an OT-based flow matching model with a transformer architecture to predict identity-agnostic motion sequences conditioned on audio features. To improve cross-ethnic generalization, we train on a balanced combination of DH-FaceVid-1K and HDTF datasets with HuBert-CN as the audio encoder. Experimental results demonstrate that FlowTalk achieves over 100 FPS in motion-space inference with 32 ODE solver steps, approximately 5 times faster than diffusion-based baselines with 500 steps, while preserving comparable visual quality in lip synchronization, facial expressions, and head movements. This efficiency, further enhanced through TensorRT deployment, enables truly real-time generation. Our framework provides an effective and practical solution for real-time talking head generation applications.

</details>

### [Synchronization of Speech and Lip Motion with a Service Humanoid Robot](s2:0982ab995632b833b80b34147e62c8a00824f7d0.md)
**Qiaowen Wu, Huan Peng, Songji Chen, Mingcong Wang et al.** · 2025-12-03

<details>
<summary>Abstract</summary>

With the increasing deployment of humanoid service robots in presentation and narration scenarios, there is a growing demand for more natural and effective interactive capabilities. To enhance the expressiveness and motion coordination of robot-delivered narration, this study presents a lip-synchronized presentation system. The proposed system ensures precise synchronization among speech output, lip movements, and slide progression, thereby enhancing the naturalness and coherence of the narration process. It consists of three primary modules: a speech processing module for speech synthesis and recognition, a slide control module for intent recognition and presentation management, and a lip-synchronization module that aligns lip motions with spoken content. Experimental results demonstrate that the system achieves high synchronization accuracy and operational stability. This work provides a solid technical foundation for integrating humanoid service robots into multimodal narration tasks.

</details>

### [PhonemeNet: A Transformer Pipeline for Text-Driven Facial Animation](s2:26a484edbab96233b524fd429d76807a23c3e116.md)
**Philine Witzig, Barbara Solenthaler, Markus Gross, Rafael Wampfler** · 2025-12-02

<details>
<summary>Abstract</summary>

We present a fully text-driven framework for 3D facial animation that eliminates the need for audio input or explicit prosodic cues. Our architecture extracts rich phoneme embeddings from text using a pre-trained TTS encoder, aligns them with quantized motion embeddings via a transformer decoder, and decodes the result into mesh deformations through a pre-trained transformer decoder. We explore two scenarios of our pipeline: (1) In the single-subject setting, we find that phoneme embeddings alone can yield accurate lip motion. (2) In a multi-subject setting, where speaker articulation varies widely, we introduce stochastic latent modulation to model residual variability conditioned on both phoneme context and speaker identity. We evaluate our approach quantitatively and qualitatively: We demonstrate accurate lip sync in the single-subject case, and compare against audio-driven baselines on a large multi-subject dataset. Our results show that PhonemeNet not only achieves competitive lip sync and motion quality, but also offers flexibility, modularity, and scalability as an alternative to audio-driven facial animation.

</details>

### [Multilingual Speech-Driven Talking-Face Generation with Precise Lip Synchronization](s2:e716de5959076556b3c54bc846fb61ee9a29204d.md)
**Che-Wen Chen, Jhing-Fa Wang, Din-Yuen Chan, James Chao et al.** · 2025-12-01

<details>
<summary>Abstract</summary>

We propose a modular pipeline that converts Chinese text into Taiwanese Hokkien speech and synthesizes a photorealistic talking-face video. The system couples a Taiwanese-aware TTS front end (hybrid word segmentation, iTaigi Tâi-lô romanization with dynamic tone annotation, tone-aware Tacotron2) with a Seed-VC–style timbre converter and a two-stage speech-driven talking-face synthesizer using cross-modal fusion, temporal modeling, and diffusion rendering. On an internal set, the speech reaches MOS 4.602 and CER 2.01%. On talking-face benchmarks, we obtain FID 29.18, CPBD 0.498, and LSE-D 7.23, surpassing representative baselines in realism, sharpness, and lip-sync. The design is lightweight and modular, runs on a single RTX 3080, and is transferable to other low-resource tonal languages.

</details>

### [EmoDiffTalk:Emotion-aware Diffusion for Editable 3D Gaussian Talking Head](2512.05991.md)
**Chang Liu, Tianjiao Jing, Chengcheng Ma, Xuanqi Zhou et al.** · 2025-11-30

<details>
<summary>Abstract</summary>

Recent photo-realistic 3D talking head via 3D Gaussian Splatting still has significant shortcoming in emotional expression manipulation, especially for fine-grained and expansive dynamics emotional editing using multi-modal control. This paper introduces a new editable 3D Gaussian talking head, i.e. EmoDiffTalk. Our key idea is a novel Emotion-aware Gaussian Diffusion, which includes an action unit (AU) prompt Gaussian diffusion process for fine-grained facial animator, and moreover an accurate text-to-AU emotion controller to provide accurate and expansive dynamic emotional editing using text input. Experiments on public EmoTalk3D and RenderMe-360 datasets demonstrate superior emotional subtlety, lip-sync fidelity, and controllability of our EmoDiffTalk over previous works, establishing a principled pathway toward high-quality, diffusion-driven, multimodal editable 3D talking-head synthesis. To our best knowledge, our EmoDiffTalk is one of the first few 3D Gaussian Splatting talking-head generation framework, especially supporting continuous, multimodal emotional editing within the AU-based expression space.

</details>

### [Open-Source Lip-Sync Models in the Period 2020--2025: A Structured Comparative Analysis](s2:944e04e8799bbee4507ce55cfcadc179ba7064b5.md)
**Bilge Sağlam, Mustafa Keles, Mehmet Kutanoglu** · 2025-11-30

<details>
<summary>Abstract</summary>

Recent advancements in artificial intelligence have led to significant progress in the field of lip synchronization (lip-sync). This paper presents a systematic literature review focusing on popular open-source lip-sync models developed between 2020 and 2025, a period marked by the rapid evolution of deep generative models. Our aim was to examine and classify the prominent models of this era based on their architecture, performance, and technological approaches. To conduct our review, we searched the IEEE Xplore and Scopus databases. This study is based on three main methods most commonly used in the field: Generative Adversarial Networks (GANs), Transformers, and Diffusion Models. Each method was analyzed in detail using its popular representatives: Wav2Lip (GAN), GeneFace (Transformer/NeRF), and Diff2Lip (Diffusion). In this study, the training processes, architectural features, and performance metrics, such as video quality, synchronization accuracy, and computational cost, of these models were compared. Our findings indicate that diffusion models have recently gained prominence because they offer photorealistic outputs and stable training processes, although GAN-based models such as Wav2Lip are still widely used. This review serves as a comprehensive guide for researchers by summarizing the current state of the art in the field. Furthermore, it aims to contribute to new work by discussing the current challenges faced by lip-sync technologies and future research directions (e.g., real-time performance and multilingual support).

</details>

### [AnyTalker: Scaling Multi-Person Talking Video Generation with Interactivity Refinement](2511.23475.md)
**Zhizhou Zhong, Yicheng Ji, Zhe Kong, Yiying Liu et al.** · 2025-11-28

<details>
<summary>Abstract</summary>

Recently, multi-person video generation has started to gain prominence. While a few preliminary works have explored audio-driven multi-person talking video generation, they often face challenges due to the high costs of diverse multi-person data collection and the difficulty of driving multiple identities with coherent interactivity. To address these challenges, we propose AnyTalker, a multi-person generation framework that features an extensible multi-stream processing architecture. Specifically, we extend Diffusion Transformer's attention block with a novel identity-aware attention mechanism that iteratively processes identity-audio pairs, allowing arbitrary scaling of drivable identities. Besides, training multi-person generative models demands massive multi-person data. Our proposed training pipeline depends solely on single-person videos to learn multi-person speaking patterns and refines interactivity with only a few real multi-person clips. Furthermore, we contribute a targeted metric and dataset designed to evaluate the naturalness and interactivity of the generated multi-person videos. Extensive experiments demonstrate that AnyTalker achieves remarkable lip synchronization, visual quality, and natural interactivity, striking a favorable balance between data costs and identity scalability.

</details>

### [AI killed the video star. Audio-driven diffusion model for expressive talking head generation](2511.22488.md)
**Baptiste Chopin, Tashvik Dhamija, Pranav Balaji, Yaohui Wang et al.** · 2025-11-27

<details>
<summary>Abstract</summary>

We propose Dimitra++, a novel framework for audio-driven talking head generation, streamlined to learn lip motion, facial expression, as well as head pose motion. Specifically, we propose a conditional Motion Diffusion Transformer (cMDT) to model facial motion sequences, employing a 3D representation. The cMDT is conditioned on two inputs: a reference facial image, which determines appearance, as well as an audio sequence, which drives the motion. Quantitative and qualitative experiments, as well as a user study on two widely employed datasets, i.e., VoxCeleb2 and CelebV-HQ, suggest that Dimitra++ is able to outperform existing approaches in generating realistic talking heads imparting lip motion, facial expression, and head pose.

</details>

### [Towards Authentic Movie Dubbing with Retrieve-Augmented Director-Actor Interaction Learning](2511.14249.md)
**Rui Liu, Yuan Zhao, Zhenqi Jia** · 2025-11-18

<details>
<summary>Abstract</summary>

The automatic movie dubbing model generates vivid speech from given scripts, replicating a speaker's timbre from a brief timbre prompt while ensuring lip-sync with the silent video. Existing approaches simulate a simplified workflow where actors dub directly without preparation, overlooking the critical director-actor interaction. In contrast, authentic workflows involve a dynamic collaboration: directors actively engage with actors, guiding them to internalize the context cues, specifically emotion, before performance. To address this issue, we propose a new Retrieve-Augmented Director-Actor Interaction Learning scheme to achieve authentic movie dubbing, termed Authentic-Dubber, which contains three novel mechanisms: (1) We construct a multimodal Reference Footage library to simulate the learning footage provided by directors. Note that we integrate Large Language Models (LLMs) to achieve deep comprehension of emotional representations across multimodal signals. (2) To emulate how actors efficiently and comprehensively internalize director-provided footage during dubbing, we propose an Emotion-Similarity-based Retrieval-Augmentation strategy. This strategy retrieves the most relevant multimodal information that aligns with the target silent video. (3) We develop a Progressive Graph-based speech generation approach that incrementally incorporates the retrieved multimodal emotional knowledge, thereby simulating the actor's final dubbing process. The above mechanisms enable the Authentic-Dubber to faithfully replicate the authentic dubbing workflow, achieving comprehensive improvements in emotional expressiveness. Both subjective and objective evaluations on the V2C Animation benchmark dataset validate the effectiveness. The code and demos are available at https://github.com/AI-S2-Lab/Authentic-Dubber.

</details>

### [The Creation of Immersive Experiences in Transcultural Entertainment: An Action Design Process Focused on Neural Rendering](s2:60618f2e0144dad7862f144e02000e3e2a11fd55.md)
**Mike Seymour, Barney Tan, Yang Li** · 2025-11-13

<details>
<summary>Abstract</summary>

This study examines how artificial intelligence (AI), specifically neural facial reenactment (NFR), can address the limitations of dubbing and subtitling in adapting foreign films. Using action design research and guided by presence theory, we codeveloped and evaluated an NFR process during the English adaptation of the Polish feature film The Champion. Unlike conventional dubbing, which often disrupts immersion through poor lip-sync or script changes, NFR preserves the original actors’ performances, aligning them with new dialogue. Independent broadcast-quality assessments confirmed technical validity, and subsequent commercial distribution on a major streaming platform demonstrated scalability and audience acceptance. From this process, we derived six design principles: avoid forced script changes, respect creative intent, minimize intrusive technology, reduce training data requirements, enable flexible audience access, and codesign with existing creative structures. These principles offer a replicable template for the responsible researching and developing of AI in information systems. For practice, the findings show that NFR can improve cultural accessibility and create new creative and technical roles rather than displacing talent. For policy, the study highlights the importance of codesign, transparency, and preserving artistic integrity when integrating AI into global cultural products.

</details>

### [Lightweight Audio-Visual Networks for Real-Time Lip-Sync DeepFake Detection](s2:33c3ab9ce4d8fe0062d491667557f2b4f44103f6.md)
**Quoc-Dat Le, Vu-Hoang Tran, Viet-Dat Nguyen** · 2025-11-12

<details>
<summary>Abstract</summary>

Lip-sync DeepFakes, which manipulate lip movements to match tampered audio while preserving visual identity, pose significant challenges to digital content integrity due to their subtle temporal inconsistencies. Traditional detection methods focusing on spatial artifacts are often ineffective against these forgeries, while recent temporal correlation models, despite their accuracy, are computationally intensive and impractical for resource-constrained devices. This paper proposes a lightweight, real-time framework for lip-sync DeepFake detection, leveraging compact neural networks, temporal attention mechanisms, and knowledge distillation. Utilizing ShuffleNetV2x0.5 as the backbone, our model incorporates audio-visual temporal modeling and human-inspired perceptual cues, such as lip-speech synchronization, to achieve robust detection. Knowledge distillation transfers insights from a high-capacity teacher model to ensure high accuracy with a model size of only 18 MB and an inference speed of 20 FPS on standard CPUs, optimized for edge device deployment. Evaluated on the AVLIP and FakeAVCeleb datasets, our approach achieves 93.50% average precision on AVLIP and 99.23% average precision on FakeAVCeleb, rivaling state-of-the-art models while enabling real-time performance on edge devices. This framework is well-suited for applications like mobile video authentication, livestream monitoring, and content moderation, addressing the growing need for efficient and scalable DeepFake detection solutions.

</details>

### [Is It Truly Necessary to Process and Fit Minutes-Long Reference Videos for Personalized Talking Face Generation?](2511.07940.md)
**Rui-Qing Sun, Ang Li, Zhijing Wu, Tian Lan et al.** · 2025-11-11

<details>
<summary>Abstract</summary>

Talking Face Generation (TFG) aims to produce realistic and dynamic talking portraits, with broad applications in fields such as digital education, film and television production, e-commerce live streaming, and other related areas. Currently, TFG methods based on Neural Radiated Field (NeRF) or 3D Gaussian sputtering (3DGS) are received widespread attention. They learn and store personalized features from reference videos of each target individual to generate realistic speaking videos. To ensure models can capture sufficient 3D information and successfully learns the lip-audio mapping, previous studies usually require meticulous processing and fitting several minutes of reference video, which always takes hours. The computational burden of processing and fitting long reference videos severely limits the practical application value of these methods.However, is it really necessary to fit such minutes of reference video? Our exploratory case studies show that using some informative reference video segments of just a few seconds can achieve performance comparable to or even better than the full reference video. This indicates that video informative quality is much more important than its length. Inspired by this observation, we propose the ISExplore (short for Informative Segment Explore), a simple-yet-effective segment selection strategy that automatically identifies the informative 5-second reference video segment based on three key data quality dimensions: audio feature diversity, lip movement amplitude, and number of camera views. Extensive experiments demonstrate that our approach increases data processing and training speed by more than 5x for NeRF and 3DGS methods, while maintaining high-fidelity output. Project resources are available at xx.

</details>

### [ConsistTalk: Intensity Controllable Temporally Consistent Talking Head Generation with Diffusion Noise Search](2511.06833.md)
**Zhenjie Liu, Jianzhang Lu, Renjie Lu, Cong Liang et al.** · 2025-11-10

<details>
<summary>Abstract</summary>

Recent advancements in video diffusion models have significantly enhanced audio-driven portrait animation. However, current methods still suffer from flickering, identity drift, and poor audio-visual synchronization. These issues primarily stem from entangled appearance-motion representations and unstable inference strategies. In this paper, we introduce \textbf{ConsistTalk}, a novel intensity-controllable and temporally consistent talking head generation framework with diffusion noise search inference. First, we propose \textbf{an optical flow-guided temporal module (OFT)} that decouples motion features from static appearance by leveraging facial optical flow, thereby reducing visual flicker and improving temporal consistency. Second, we present an \textbf{Audio-to-Intensity (A2I) model} obtained through multimodal teacher-student knowledge distillation. By transforming audio and facial velocity features into a frame-wise intensity sequence, the A2I model enables joint modeling of audio and visual motion, resulting in more natural dynamics. This further enables fine-grained, frame-wise control of motion dynamics while maintaining tight audio-visual synchronization. Third, we introduce a \textbf{diffusion noise initialization strategy (IC-Init)}. By enforcing explicit constraints on background coherence and motion continuity during inference-time noise search, we achieve better identity preservation and refine motion dynamics compared to the current autoregressive strategy. Extensive experiments demonstrate that ConsistTalk significantly outperforms prior methods in reducing flicker, preserving identity, and delivering temporally stable, high-fidelity talking head videos.

</details>

### [THEval. Evaluation Framework for Talking Head Video Generation](2511.04520.md)
**Nabyl Quignon, Baptiste Chopin, Yaohui Wang, Antitza Dantcheva** · 2025-11-06

<details>
<summary>Abstract</summary>

Video generation has achieved remarkable progress, with generated videos increasingly resembling real ones. However, the rapid advance in generation has outpaced the development of adequate evaluation metrics. Currently, the assessment of talking head generation primarily relies on limited metrics, evaluating general video quality, lip synchronization, and on conducting user studies. Motivated by this, we propose a new evaluation framework comprising 8 metrics related to three dimensions (i) quality, (ii) naturalness, and (iii) synchronization. In selecting the metrics, we place emphasis on efficiency, as well as alignment with human preferences. Based on this considerations, we streamline to analyze fine-grained dynamics of head, mouth, and eyebrows, as well as face quality. Our extensive experiments on 85,000 videos generated by 17 state-of-the-art models suggest that while many algorithms excel in lip synchronization, they face challenges with generating expressiveness and artifact-free details. These videos were generated based on a novel real dataset, that we have curated, in order to mitigate bias of training data. Our proposed benchmark framework is aimed at evaluating the improvement of generative methods. Original code, dataset and leaderboards will be publicly released and regularly updated with new methods, in order to reflect progress in the field.

</details>

### [UniAVGen: Unified Audio and Video Generation with Asymmetric Cross-Modal Interactions](2511.03334.md)
**Guozhen Zhang, Zixiang Zhou, Teng Hu, Ziqiao Peng et al.** · 2025-11-05

<details>
<summary>Abstract</summary>

Due to the lack of effective cross-modal modeling, existing open-source audio-video generation methods often exhibit compromised lip synchronization and insufficient semantic consistency. To mitigate these drawbacks, we propose UniAVGen, a unified framework for joint audio and video generation. UniAVGen is anchored in a dual-branch joint synthesis architecture, incorporating two parallel Diffusion Transformers (DiTs) to build a cohesive cross-modal latent space. At its heart lies an Asymmetric Cross-Modal Interaction mechanism, which enables bidirectional, temporally aligned cross-attention, thus ensuring precise spatiotemporal synchronization and semantic consistency. Furthermore, this cross-modal interaction is augmented by a Face-Aware Modulation module, which dynamically prioritizes salient regions in the interaction process. To enhance generative fidelity during inference, we additionally introduce Modality-Aware Classifier-Free Guidance, a novel strategy that explicitly amplifies cross-modal correlation signals. Notably, UniAVGen's robust joint synthesis design enables seamless unification of pivotal audio-video tasks within a single model, such as joint audio-video generation and continuation, video-to-audio dubbing, and audio-driven video synthesis. Comprehensive experiments validate that, with far fewer training samples (1.3M vs. 30.1M), UniAVGen delivers overall advantages in audio-video synchronization, timbre consistency, and emotion consistency.

</details>

### [Densemarks: Learning Canonical Embeddings for Human Heads Images via Point Tracks](2511.02830.md)
**Dmitrii Pozdeev, Alexey Artemov, Ananta R. Bhattarai, Artem Sevastopolsky** · 2025-11-04

<details>
<summary>Abstract</summary>

We propose DenseMarks - a new learned representation for human heads, enabling high-quality dense correspondences of human head images. For a 2D image of a human head, a Vision Transformer network predicts a 3D embedding for each pixel, which corresponds to a location in a 3D canonical unit cube. In order to train our network, we collect a dataset of pairwise point matches, estimated by a state-of-the-art point tracker over a collection of diverse in-the-wild talking heads videos, and guide the mapping via a contrastive loss, encouraging matched points to have close embeddings. We further employ multi-task learning with face landmarks and segmentation constraints, as well as imposing spatial continuity of embeddings through latent cube features, which results in an interpretable and queryable canonical space. The representation can be used for finding common semantic parts, face/head tracking, and stereo reconstruction. Due to the strong supervision, our method is robust to pose variations and covers the entire head, including hair. Additionally, the canonical space bottleneck makes sure the obtained representations are consistent across diverse poses and individuals. We demonstrate state-of-the-art results in geometry-aware point matching and monocular head tracking with 3D Morphable Models. The code and the model checkpoint will be made available to the public.

</details>

### [Immersive interactive intelligent patient educational system for venous thromboembolism](s2:64754368ff056b9a72c6e188261c73bff3dcd7a6.md)
**Y. Guo** · 2025-11-01

<details>
<summary>Abstract</summary>

Large language models (LLMs) can serve as virtual teaching assistants, providing patients with detailed and relevant information and perhaps eventually interactive simulations. This study explored the integration of LLMs into the education and patient-centered care for venous thromboembolism (VTE). We developed a immersive interactive intelligent patient educational system for patients with VTE using LLM，Qwen1.5-7B, Text-to-Speech(TTS)，and Lip Synchronization(Lip-Sync) technologies. The immersive interactive intelligent patient educational system (ChatVTE) consisted of four components (Figure 1): 1) Information Collection of Multimodal Optical Character Recognition Technology Based on Large Models, which collecting patient's clinical data. 2) Knowledge, Attitude/Belief, Practice and Health Belief Model, which capturing patient's health requirement. 3) VTE relevant data were systematically gathered from open-access Internet sources and indexed into a knowledge database. We leveraged Retrieval-Augmented Language Modeling to recall this information and utilized it for pretraining, which was then integrated into Qwen1.5-7B, creating an VTE-specific knowledge question & answer platform. 4) Based on intelligent question & answer, a digital virtual doctor created with TTS Lip-Sync technologies to facilities patient education （Figure 2）. ChatVTE generated fewer hallucinations and demonstrated greater consistency，improved the quality of doctor-patient interaction and enhance the effectiveness of knowledge dissemination. To the best of our knowledge, the digital virtual VTE doctor of ChatVTE was the first digital virtual doctor driven by specialty-specific VTE knowledge retrieval AI that utilizes the latest LLM. It appeared the promising for patient education and shared clinical decision support. Continued research and evaluation are necessary to ensure the optimal integration of AI-based interactive tools into patient-centered care.

</details>

### [Audio-Visual Speech Enhancement In Complex Scenarios With Separation And Dereverberation Joint Modeling](2510.26825.md)
**Jiarong Du, Zhan Jin, Peijun Yang, Juan Liu et al.** · 2025-10-29

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement (AVSE) is a task that uses visual auxiliary information to extract a target speaker's speech from mixed audio. In real-world scenarios, there often exist complex acoustic environments, accompanied by various interfering sounds and reverberation. Most previous methods struggle to cope with such complex conditions, resulting in poor perceptual quality of the extracted speech. In this paper, we propose an effective AVSE system that performs well in complex acoustic environments. Specifically, we design a "separation before dereverberation" pipeline that can be extended to other AVSE networks. The 4th COGMHEAR Audio-Visual Speech Enhancement Challenge (AVSEC) aims to explore new approaches to speech processing in multimodal complex environments. We validated the performance of our system in AVSEC-4: we achieved excellent results in the three objective metrics on the competition leaderboard, and ultimately secured first place in the human subjective listening test.

</details>

### [See the Speaker: Crafting High-Resolution Talking Faces from Speech with Prior Guidance and Region Refinement](2510.26819.md)
**Jinting Wang, Jun Wang, Hei Victor Cheng, Li Liu** · 2025-10-28

<details>
<summary>Abstract</summary>

Unlike existing methods that rely on source images as appearance references and use source speech to generate motion, this work proposes a novel approach that directly extracts information from the speech, addressing key challenges in speech-to-talking face. Specifically, we first employ a speech-to-face portrait generation stage, utilizing a speech-conditioned diffusion model combined with statistical facial prior and a sample-adaptive weighting module to achieve high-quality portrait generation. In the subsequent speech-driven talking face generation stage, we embed expressive dynamics such as lip movement, facial expressions, and eye movements into the latent space of the diffusion model and further optimize lip synchronization using a region-enhancement module. To generate high-resolution outputs, we integrate a pre-trained Transformer-based discrete codebook with an image rendering network, enhancing video frame details in an end-to-end manner. Experimental results demonstrate that our method outperforms existing approaches on the HDTF, VoxCeleb, and AVSpeech datasets. Notably, this is the first method capable of generating high-resolution, high-quality talking face videos exclusively from a single speech input.

</details>

### [MAGIC-Talk: Motion-aware Audio-Driven Talking Face Generation with Customizable Identity Control](2510.22810.md)
**Fatemeh Nazarieh, Zhenhua Feng, Diptesh Kanojia, Muhammad Awais et al.** · 2025-10-26

<details>
<summary>Abstract</summary>

Audio-driven talking face generation has gained significant attention for applications in digital media and virtual avatars. While recent methods improve audio-lip synchronization, they often struggle with temporal consistency, identity preservation, and customization, especially in long video generation. To address these issues, we propose MAGIC-Talk, a one-shot diffusion-based framework for customizable and temporally stable talking face generation. MAGIC-Talk consists of ReferenceNet, which preserves identity and enables fine-grained facial editing via text prompts, and AnimateNet, which enhances motion coherence using structured motion priors. Unlike previous methods requiring multiple reference images or fine-tuning, MAGIC-Talk maintains identity from a single image while ensuring smooth transitions across frames. Additionally, a progressive latent fusion strategy is introduced to improve long-form video quality by reducing motion inconsistencies and flickering. Extensive experiments demonstrate that MAGIC-Talk outperforms state-of-the-art methods in visual quality, identity preservation, and synchronization accuracy, offering a robust solution for talking face generation.

</details>

### [DeepfakeBench-MM: A Comprehensive Benchmark for Multimodal Deepfake Detection](2510.22622.md)
**Kangran Zhao, Yupeng Chen, Xiaoyu Zhang, Yize Chen et al.** · 2025-10-26

<details>
<summary>Abstract</summary>

The misuse of advanced generative AI models has resulted in the widespread proliferation of falsified data, particularly forged human-centric audiovisual content, which poses substantial societal risks (e.g., financial fraud and social instability). In response to this growing threat, several works have preliminarily explored countermeasures. However, the lack of sufficient and diverse training data, along with the absence of a standardized benchmark, hinder deeper exploration. To address this challenge, we first build Mega-MMDF, a large-scale, diverse, and high-quality dataset for multimodal deepfake detection. Specifically, we employ 21 forgery pipelines through the combination of 10 audio forgery methods, 12 visual forgery methods, and 6 audio-driven face reenactment methods. Mega-MMDF currently contains 0.1 million real samples and 1.1 million forged samples, making it one of the largest and most diverse multimodal deepfake datasets, with plans for continuous expansion. Building on it, we present DeepfakeBench-MM, the first unified benchmark for multimodal deepfake detection. It establishes standardized protocols across the entire detection pipeline and serves as a versatile platform for evaluating existing methods as well as exploring novel approaches. DeepfakeBench-MM currently supports 5 datasets and 11 multimodal deepfake detectors. Furthermore, our comprehensive evaluations and in-depth analyses uncover several key findings from multiple perspectives (e.g., augmentation, stacked forgery). We believe that DeepfakeBench-MM, together with our large-scale Mega-MMDF, will serve as foundational infrastructures for advancing multimodal deepfake detection.

</details>

### [Lip-Sync Analyzer for Deepfake Detection and Peeking Behind the Black Box with Explainable AI](s2:268dee604af0f25e9e5ad493fee603f6c39acde9.md)
**S. Sakib, S. Haque, Atanu Shome** · 2025-10-23

<details>
<summary>Abstract</summary>

The swift evolution of deepfake technology presents significant threats to the credibility and trustworthiness of digital media. This work presents a deepfake detection framework that combines spatial and audio-visual features, with a specific focus on lip-sync forgeries. We evaluate multiple state-of-the-art CNN architectures—DenseNet-121, EfficientNet-B0, InceptionV3, ResNet-50, and XceptionNet—alongside a Vision Transformer (ViT-B/32). Experiments on the AVLips dataset (3,396 real and 4,206 fake videos) show that ViT-B/32 achieves superior performance, with 96% F1-score, and 99% AUC. Audio-visual fusion consistently outperforms visual-only models, highlighting the strength of multimodal analysis. To enhance transparency, LIME-based explainable AI visualizations are employed to interpret model predictions. Unlike previous works that primarily rely on unimodal cues, our approach uniquely integrates audio waveforms with visual frames to expose subtle inconsistencies in lip synchronization. Given the potential misuse of deepfakes in misinformation, fraud, and political manipulation, this study emphasizes the urgent need for robust and interpretable detection methods. Our findings confirm the effectiveness of transformer-based models with XAI for dependable deepfake detection, with future work focusing on temporal modeling and scalability.

</details>

### [Playmate2: Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback](2510.12089.md)
**Xingpei Ma, Shenneng Huang, Jiaran Cai, Yuansheng Guan et al.** · 2025-10-14

<details>
<summary>Abstract</summary>

Recent advances in diffusion models have significantly improved audio-driven human video generation, surpassing traditional methods in both quality and controllability. However, existing approaches still face challenges in lip-sync accuracy, temporal coherence for long video generation, and multi-character animation. In this work, we propose a diffusion transformer (DiT)-based framework for generating lifelike talking videos of arbitrary length, and introduce a training-free method for multi-character audio-driven animation. First, we employ a LoRA-based training strategy combined with a position shift inference approach, which enables efficient long video generation while preserving the capabilities of the foundation model. Moreover, we combine partial parameter updates with reward feedback to enhance both lip synchronization and natural body motion. Finally, we propose a training-free approach, Mask Classifier-Free Guidance (Mask-CFG), for multi-character animation, which requires no specialized datasets or model modifications and supports audio-driven animation for three or more characters. Experimental results demonstrate that our method outperforms existing state-of-the-art approaches, achieving high-quality, temporally coherent, and multi-character audio-driven video generation in a simple, efficient, and cost-effective manner.

</details>

### [DEMO: Disentangled Motion Latent Flow Matching for Fine-Grained Controllable Talking Portrait Synthesis](2510.10650.md)
**Peiyin Chen, Zhuowei Yang, Hui Feng, Sheng Jiang et al.** · 2025-10-12

<details>
<summary>Abstract</summary>

Audio-driven talking-head generation has advanced rapidly with diffusion-based generative models, yet producing temporally coherent videos with fine-grained motion control remains challenging. We propose DEMO, a flow-matching generative framework for audio-driven talking-portrait video synthesis that delivers disentangled, high-fidelity control of lip motion, head pose, and eye gaze. The core contribution is a motion auto-encoder that builds a structured latent space in which motion factors are independently represented and approximately orthogonalized. On this disentangled motion space, we apply optimal-transport-based flow matching with a transformer predictor to generate temporally smooth motion trajectories conditioned on audio. Extensive experiments across multiple benchmarks show that DEMO outperforms prior methods in video realism, lip-audio synchronization, and motion fidelity. These results demonstrate that combining fine-grained motion disentanglement with flow-based generative modeling provides a powerful new paradigm for controllable talking-head video synthesis.

</details>

### [AUREXA-SE: Audio-Visual Unified Representation Exchange Architecture with Cross-Attention and Squeezeformer for Speech Enhancement](2510.05295.md)
**M. Sajid, Deepanshu Gupta, Yash Modi, Sanskriti Jain et al.** · 2025-10-06

<details>
<summary>Abstract</summary>

In this paper, we propose AUREXA-SE (Audio-Visual Unified Representation Exchange Architecture with Cross-Attention and Squeezeformer for Speech Enhancement), a progressive bimodal framework tailored for audio-visual speech enhancement (AVSE). AUREXA-SE jointly leverages raw audio waveforms and visual cues by employing a U-Net-based 1D convolutional encoder for audio and a Swin Transformer V2 for efficient and expressive visual feature extraction. Central to the architecture is a novel bidirectional cross-attention mechanism, which facilitates deep contextual fusion between modalities, enabling rich and complementary representation learning. To capture temporal dependencies within the fused embeddings, a stack of lightweight Squeezeformer blocks combining convolutional and attention modules is introduced. The enhanced embeddings are then decoded via a U-Net-style decoder for direct waveform reconstruction, ensuring perceptually consistent and intelligible speech output. Experimental evaluations demonstrate the effectiveness of AUREXA-SE, achieving significant performance improvements over noisy baselines, with STOI of 0.516, PESQ of 1.323, and SI-SDR of -4.322 dB. The source code of AUREXA-SE is available at https://github.com/mtanveer1/AVSEC-4-Challenge-2025.

</details>

### [Input-Aware Sparse Attention for Real-Time Co-Speech Video Generation](2510.02617.md)
**Beijia Lu, Ziyi Chen, Jing Xiao, Jun-Yan Zhu** · 2025-10-02

<details>
<summary>Abstract</summary>

Diffusion models can synthesize realistic co-speech video from audio for various applications, such as video creation and virtual agents. However, existing diffusion-based methods are slow due to numerous denoising steps and costly attention mechanisms, preventing real-time deployment. In this work, we distill a many-step diffusion video model into a few-step student model. Unfortunately, directly applying recent diffusion distillation methods degrades video quality and falls short of real-time performance. To address these issues, our new video distillation method leverages input human pose conditioning for both attention and loss functions. We first propose using accurate correspondence between input human pose keypoints to guide attention to relevant regions, such as the speaker's face, hands, and upper body. This input-aware sparse attention reduces redundant computations and strengthens temporal correspondences of body parts, improving inference efficiency and motion coherence. To further enhance visual quality, we introduce an input-aware distillation loss that improves lip synchronization and hand motion realism. By integrating our input-aware sparse attention and distillation loss, our method achieves real-time performance with improved visual quality compared to recent audio-driven and input-driven methods. We also conduct extensive experiments showing the effectiveness of our algorithmic design choices.

</details>

### [StableDub: Taming Diffusion Prior for Generalized and Efficient Visual Dubbing](2509.21887.md)
**Liyang Chen, Tianze Zhou, Xu He, Boshi Tang et al.** · 2025-09-26

<details>
<summary>Abstract</summary>

The visual dubbing task aims to generate mouth movements synchronized with the driving audio, which has seen significant progress in recent years. However, two critical deficiencies hinder their wide application: (1) Audio-only driving paradigms inadequately capture speaker-specific lip habits, which fail to generate lip movements similar to the target avatar; (2) Conventional blind-inpainting approaches frequently produce visual artifacts when handling obstructions (e.g., microphones, hands), limiting practical deployment. In this paper, we propose StableDub, a novel and concise framework integrating lip-habit-aware modeling with occlusion-robust synthesis. Specifically, building upon the Stable-Diffusion backbone, we develop a lip-habit-modulated mechanism that jointly models phonemic audio-visual synchronization and speaker-specific orofacial dynamics. To achieve plausible lip geometries and object appearances under occlusion, we introduce the occlusion-aware training strategy by explicitly exposing the occlusion objects to the inpainting process. By incorporating the proposed designs, the model eliminates the necessity for cost-intensive priors in previous methods, thereby exhibiting superior training efficiency on the computationally intensive diffusion-based backbone. To further optimize training efficiency from the perspective of model architecture, we introduce a hybrid Mamba-Transformer architecture, which demonstrates the enhanced applicability in low-resource research scenarios. Extensive experimental results demonstrate that StableDub achieves superior performance in lip habit resemblance and occlusion robustness. Our method also surpasses other methods in audio-lip sync, video quality, and resolution consistency. We expand the applicability of visual dubbing methods from comprehensive aspects, and demo videos can be found at https://stabledub.github.io.

</details>

### [Talking Head Generation via AU-Guided Landmark Prediction](2509.19749.md)
**Shao-Yu Chang, Jingyi Xu, Hieu Le, Dimitris Samaras** · 2025-09-24

<details>
<summary>Abstract</summary>

We propose a two-stage framework for audio-driven talking head generation with fine-grained expression control via facial Action Units (AUs). Unlike prior methods relying on emotion labels or implicit AU conditioning, our model explicitly maps AUs to 2D facial landmarks, enabling physically grounded, per-frame expression control. In the first stage, a variational motion generator predicts temporally coherent landmark sequences from audio and AU intensities. In the second stage, a diffusion-based synthesizer generates realistic, lip-synced videos conditioned on these landmarks and a reference image. This separation of motion and appearance improves expression accuracy, temporal stability, and visual realism. Experiments on the MEAD dataset show that our method outperforms state-of-the-art baselines across multiple metrics, demonstrating the effectiveness of explicit AU-to-landmark modeling for expressive talking head generation.

</details>

### [KSDiff: Keyframe-Augmented Speech-Aware Dual-Path Diffusion for Facial Animation](2509.20128.md)
**Tianle Lyu, Junchuan Zhao, Ye Wang** · 2025-09-24

<details>
<summary>Abstract</summary>

Audio-driven facial animation has made significant progress in multimedia applications, with diffusion models showing strong potential for talking-face synthesis. However, most existing works treat speech features as a monolithic representation and fail to capture their fine-grained roles in driving different facial motions, while also overlooking the importance of modeling keyframes with intense dynamics. To address these limitations, we propose KSDiff, a Keyframe-Augmented Speech-Aware Dual-Path Diffusion framework. Specifically, the raw audio and transcript are processed by a Dual-Path Speech Encoder (DPSE) to disentangle expression-related and head-pose-related features, while an autoregressive Keyframe Establishment Learning (KEL) module predicts the most salient motion frames. These components are integrated into a Dual-path Motion generator to synthesize coherent and realistic facial motions. Extensive experiments on HDTF and VoxCeleb demonstrate that KSDiff achieves state-of-the-art performance, with improvements in both lip synchronization accuracy and head-pose naturalness. Our results highlight the effectiveness of combining speech disentanglement with keyframe-aware diffusion for talking-head generation.

</details>

### [PGSTalker: Real-Time Audio-Driven Talking Head Generation via 3D Gaussian Splatting with Pixel-Aware Density Control](2509.16922.md)
**Tianheng Zhu, Yinfeng Yu, Liejun Wang, Fuchun Sun et al.** · 2025-09-21

<details>
<summary>Abstract</summary>

Audio-driven talking head generation is crucial for applications in virtual reality, digital avatars, and film production. While NeRF-based methods enable high-fidelity reconstruction, they suffer from low rendering efficiency and suboptimal audio-visual synchronization. This work presents PGSTalker, a real-time audio-driven talking head synthesis framework based on 3D Gaussian Splatting (3DGS). To improve rendering performance, we propose a pixel-aware density control strategy that adaptively allocates point density, enhancing detail in dynamic facial regions while reducing redundancy elsewhere. Additionally, we introduce a lightweight Multimodal Gated Fusion Module to effectively fuse audio and spatial features, thereby improving the accuracy of Gaussian deformation prediction. Extensive experiments on public datasets demonstrate that PGSTalker outperforms existing NeRF- and 3DGS-based approaches in rendering quality, lip-sync precision, and inference speed. Our method exhibits strong generalization capabilities and practical potential for real-world deployment.

</details>

### [Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior](2509.14379.md)
**Yochai Yemini, Rami Ben-Ari, Sharon Gannot, Ethan Fetaya** · 2025-09-17

<details>
<summary>Abstract</summary>

In this paper, we address the problem of single-microphone speech separation in the presence of ambient noise. We propose a generative unsupervised technique that directly models both clean speech and structured noise components, training exclusively on these individual signals rather than noisy mixtures. Our approach leverages an audio-visual score model that incorporates visual cues to serve as a strong generative speech prior. By explicitly modelling the noise distribution alongside the speech distribution, we enable effective decomposition through the inverse problem paradigm. We perform speech separation by sampling from the posterior distributions via a reverse diffusion process, which directly estimates and removes the modelled noise component to recover clean constituent signals. Experimental results demonstrate promising performance, highlighting the effectiveness of our direct noise modelling approach in challenging acoustic environments.

</details>

### [A Lightweight Pipeline for Noisy Speech Voice Cloning and Accurate Lip Sync Synthesis](2509.12831.md)
**Javeria Amir, Farwa Attaria, Mah Jabeen, Umara Noor et al.** · 2025-09-16

<details>
<summary>Abstract</summary>

Recent developments in voice cloning and talking head generation demonstrate impressive capabilities in synthesizing natural speech and realistic lip synchronization. Current methods typically require and are trained on large scale datasets and computationally intensive processes using clean studio recorded inputs that is infeasible in noisy or low resource environments. In this paper, we introduce a new modular pipeline comprising Tortoise text to speech. It is a transformer based latent diffusion model that can perform high fidelity zero shot voice cloning given only a few training samples. We use a lightweight generative adversarial network architecture for robust real time lip synchronization. The solution will contribute to many essential tasks concerning less reliance on massive pre training generation of emotionally expressive speech and lip synchronization in noisy and unconstrained scenarios. The modular structure of the pipeline allows an easy extension for future multi modal and text guided voice modulation and it could be used in real world systems.

</details>

### [Robust Audio-Visual Target Speaker Extraction with Emotion-Aware Multiple Enrollment Fusion](2509.12583.md)
**Zhan Jin, Bang Zeng, Peijun Yang, Jiarong Du et al.** · 2025-09-16

<details>
<summary>Abstract</summary>

Target Speaker Extraction (TSE) is a critical challenge in cocktail party scenarios. While leveraging multiple modalities, such as voice, lip, face, and expression embeddings, can enhance performance, real-world applications often suffer from intermittent modality dropout. This paper presents a comprehensive study on the interactions and robustness of various multimodal fusion strategies under varying degrees of modality dropout. We build upon a state-of-the-art audio-visual speech enhancement system and integrate four distinct speaker identity cues: lip embeddings for synchronized contextual information, a voice speaker embedding extracted via cross-attention for acoustic consistency, a static face embedding for speaker identity, and a novel dynamic expression embedding for frame-wise emotional features. We systematically evaluate different combinations of these modalities under two key training regimes: zero dropout and 80% modality dropout. Extensive experiments demonstrate that while a full multimodal ensemble achieves optimal performance under ideal (zero dropout) conditions, its effectiveness diminishes significantly when test-time dropout occurs without prior exposure during training. Crucially, we show that training with a high (80%) modality dropout rate dramatically enhances model robustness, enabling the system to maintain superior performance even under severe test-time missing modalities. Our findings highlight that voice embeddings exhibit consistent robustness, while the proposed expression embedding provides valuable complementary information. This work underscores the importance of training strategies that account for real-world imperfection, moving beyond pure performance maximization to achieve practical reliability in multimodal speech enhancement systems.

</details>

### [Kling-Avatar: Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis](2509.09595.md)
**Yikang Ding, Jiwen Liu, Wenyuan Zhang, Zekun Wang et al.** · 2025-09-11

<details>
<summary>Abstract</summary>

Recent advances in audio-driven avatar video generation have significantly enhanced audio-visual realism. However, existing methods treat instruction conditioning merely as low-level tracking driven by acoustic or visual cues, without modeling the communicative purpose conveyed by the instructions. This limitation compromises their narrative coherence and character expressiveness. To bridge this gap, we introduce Kling-Avatar, a novel cascaded framework that unifies multimodal instruction understanding with photorealistic portrait generation. Our approach adopts a two-stage pipeline. In the first stage, we design a multimodal large language model (MLLM) director that produces a blueprint video conditioned on diverse instruction signals, thereby governing high-level semantics such as character motion and emotions. In the second stage, guided by blueprint keyframes, we generate multiple sub-clips in parallel using a first-last frame strategy. This global-to-local framework preserves fine-grained details while faithfully encoding the high-level intent behind multimodal instructions. Our parallel architecture also enables fast and stable generation of long-duration videos, making it suitable for real-world applications such as digital human livestreaming and vlogging. To comprehensively evaluate our method, we construct a benchmark of 375 curated samples covering diverse instructions and challenging scenarios. Extensive experiments demonstrate that Kling-Avatar is capable of generating vivid, fluent, long-duration videos at up to 1080p and 48 fps, achieving superior performance in lip synchronization accuracy, emotion and dynamic expressiveness, instruction controllability, identity preservation, and cross-domain generalization. These results establish Kling-Avatar as a new benchmark for semantically grounded, high-fidelity audio-driven avatar synthesis.

</details>

### [Bitrate-Controlled Diffusion for Disentangling Motion and Content in Video](2509.08376.md)
**Xiao Li, Qi Chen, Xiulian Peng, Kai Yu et al.** · 2025-09-10

<details>
<summary>Abstract</summary>

We propose a novel and general framework to disentangle video data into its dynamic motion and static content components. Our proposed method is a self-supervised pipeline with less assumptions and inductive biases than previous works: it utilizes a transformer-based architecture to jointly generate flexible implicit features for frame-wise motion and clip-wise content, and incorporates a low-bitrate vector quantization as an information bottleneck to promote disentanglement and form a meaningful discrete motion space. The bitrate-controlled latent motion and content are used as conditional inputs to a denoising diffusion model to facilitate self-supervised representation learning. We validate our disentangled representation learning framework on real-world talking head videos with motion transfer and auto-regressive motion generation tasks. Furthermore, we also show that our method can generalize to other types of video data, such as pixel sprites of 2D cartoon characters. Our work presents a new perspective on self-supervised learning of disentangled video representations, contributing to the broader field of video analysis and generation.

</details>

### [NeRF-LipSync: A Diffusion Model for Speech-Driven and View-Consistent Lip Synchronization in Digital Avatars](s2:e63487520103d92b2c8eccaaa6b1f5784f679822.md)
**A. Axyonov, Mikhail Dolgushin, D. Ryumin** · 2025-09-04

<details>
<summary>Abstract</summary>

Abstract. Achieving natural, accurate, and identity-preserving lip synchronization in talking avatars is a fundamental problem in audio-visual synthesis. Existing methods often struggle to generalize across speakers, maintain temporal smoothness, or preserve view consistency due to architectural limitations. In this paper, we present NeRF-LipSync, a novel generative framework that synthesizes lip movements conditioned on speech audio while maintaining temporal coherence and view-consistent appearance through a combination of diffusion-based modeling and NeRF-based spatial alignment. Our model incorporates temporal attention and leverages rich audio-visual embeddings to produce expressive, speaker-specific articulation. We evaluate NeRF-LipSync on the VoxCeleb2 and LRW datasets and compare it against strong baselines including Wav2Lip, PC-AVS, and Diff2Lip. On VoxCeleb2, our method achieves an FID of 2.75, SSIM of 0.56, PSNR of 18.32, and LMD of 3.01, with synchronization accuracy (Syncc) reaching 9.06. On LRW, it yields an FID of 2.40, SSIM of 0.71, PSNR of 21.03, and LMD of 2.16. These results confirm the strong generalization ability and perceptual realism of our approach. Ablation studies highlight the contribution of NeRF alignment to identity consistency, diffusion to visual expressiveness, and temporal attention to motion stability. NeRF-LipSync thus offers a robust, scalable solution for high-quality, speech-driven avatar animation.

</details>

### [All’s Well That FID’s Well? Result Quality and Metric Scores in GAN Models for Lip-Synchronization Tasks](s2:f70029ecaf500aafde9906acb27fb830b4d22b21.md)
**Carina Geldhauser, Johan Liljegren, Pontus Nordqvist** · 2025-08-31

<details>
<summary>Abstract</summary>

This exploratory study investigates the usability of performance metrics for generative adversarial network (GAN)-based models for speech-driven facial animation. These models focus on the transfer of speech information from an audio file to a still image to generate talking-head videos in a small-scale “everyday usage” setting. Two models, LipGAN and a custom implementation of a Wasserstein GAN with gradient penalty (L1WGAN-GP), are examined for their visual performance and scoring according to commonly used metrics: Quantitative comparisons using FID, SSIM, and PSNR metrics on the GRIDTest dataset show mixed results, and metrics fail to capture local artifacts crucial for lip synchronization, pointing to limitations in their applicability for video animation tasks. The study points towards the inadequacy of current quantitative measures and emphasizes the continued necessity of human qualitative assessment for evaluating talking-head video quality.

</details>

### [EmoCAST: Emotional Talking Portrait via Emotive Text Description](2508.20615.md)
**Yiguo Jiang, Xiaodong Cun, Yong Zhang, Yudian Zheng et al.** · 2025-08-28

<details>
<summary>Abstract</summary>

Emotional talking head synthesis aims to generate talking portrait videos with vivid expressions. Existing methods still exhibit limitations in control flexibility, motion naturalness, and expression quality. Moreover, currently available datasets are mainly collected in lab settings, further exacerbating these shortcomings and hindering real-world deployment. To address these challenges, we propose EmoCAST, a diffusion-based talking head framework for precise, text-driven emotional synthesis. Its contributions are threefold: (1) architectural modules that enable effective text control; (2) an emotional talking-head dataset that expands the framework's ability; and (3) training strategies that further improve performance. Specifically, for appearance modeling, emotional prompts are integrated through a text-guided emotive attention module, enhancing spatial knowledge to improve emotion understanding. To strengthen audio-emotion alignment, we introduce an emotive audio attention module to capture the interplay between controlled emotion and driving audio, generating emotion-aware features to guide precise facial motion synthesis. Additionally, we construct a large-scale, in-the-wild emotional talking head dataset with emotive text descriptions to optimize the framework's performance. Based on this dataset, we propose an emotion-aware sampling strategy and a progressive functional training strategy that improve the model's ability to capture nuanced expressive features and achieve accurate lip-sync. Overall, EmoCAST achieves state-of-the-art performance in generating realistic, emotionally expressive, and audio-synchronized talking-head videos. Project Page: https://github.com/GVCLab/EmoCAST

</details>

### [Enhancing Visual Speaker Authentication using Dynamic Lip Movement and Meta-Learning](s2:a197b6d30b625f38a0355ba80433c99e69ad93bb.md)
**P. Pathare, Garima Bajwa** · 2025-08-26

<details>
<summary>Abstract</summary>

Visual speaker authentication (VSA) remains vulnerable to sophisticated spoofing methods, such as deepfakes. Traditional deep learning approaches require extensive userspecific enrollment data and show poor generalization to new speakers. In response, we employ a few-shot meta-learning technique, specifically Model-Agnostic Meta-Learning (MAML), integrated with dynamic lip movement analysis utilizing optical flow to develop a scalable anti-spoof VSA framework. We validated our model using the GRID audiovisual dataset, with spoofing attacks simulated via Wav2Lip for deepfake lip synchronization. The results demonstrate the model’s superior performance, evidenced by near-perfect classification accuracy and negligible error rates, addressing two key challenges of VSA: eliminating extensive training data while enabling rapid adaptation to unfamiliar speakers. Our approach significantly surpasses standard non-meta-learning approaches, substantiating its ability to address real-world scenarios.

</details>

### [Warm Chat: Diffuse Emotion-aware Interactive Talking Head Avatar with Tree-Structured Guidance](2508.18337.md)
**Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian et al.** · 2025-08-25

<details>
<summary>Abstract</summary>

Generative models have advanced rapidly, enabling impressive talking head generation that brings AI to life. However, most existing methods focus solely on one-way portrait animation. Even the few that support bidirectional conversational interactions lack precise emotion-adaptive capabilities, significantly limiting their practical applicability. In this paper, we propose Warm Chat, a novel emotion-aware talking head generation framework for dyadic interactions. Leveraging the dialogue generation capability of large language models (LLMs, e.g., GPT-4), our method produces temporally consistent virtual avatars with rich emotional variations that seamlessly transition between speaking and listening states. Specifically, we design a Transformer-based head mask generator that learns temporally consistent motion features in a latent mask space, capable of generating arbitrary-length, temporally consistent mask sequences to constrain head motions. Furthermore, we introduce an interactive talking tree structure to represent dialogue state transitions, where each tree node contains information such as child/parent/sibling nodes and the current character's emotional state. By performing reverse-level traversal, we extract rich historical emotional cues from the current node to guide expression synthesis. Extensive experiments demonstrate the superior performance and effectiveness of our method.

</details>

### [Lightning Fast Caching-based Parallel Denoising Prediction for Accelerating Talking Head Generation](2509.00052.md)
**Jianzhi Long, Wenhao Sun, Rongcheng Tu, Dacheng Tao** · 2025-08-25

<details>
<summary>Abstract</summary>

Diffusion-based talking head models generate high-quality, photorealistic videos but suffer from slow inference, limiting practical applications. Existing acceleration methods for general diffusion models fail to exploit the temporal and spatial redundancies unique to talking head generation. In this paper, we propose a task-specific framework addressing these inefficiencies through two key innovations. First, we introduce Lightning-fast Caching-based Parallel denoising prediction (LightningCP), caching static features to bypass most model layers in inference time. We also enable parallel prediction using cached features and estimated noisy latents as inputs, efficiently bypassing sequential sampling. Second, we propose Decoupled Foreground Attention (DFA) to further accelerate attention computations, exploiting the spatial decoupling in talking head videos to restrict attention to dynamic foreground regions. Additionally, we remove reference features in certain layers to bring extra speedup. Extensive experiments demonstrate that our framework significantly improves inference speed while preserving video quality.

</details>

### [Taming Transformer for Emotion-Controllable Talking Face Generation](2508.14359.md)
**Ziqi Zhang, Cheng Deng** · 2025-08-20

<details>
<summary>Abstract</summary>

Talking face generation is a novel and challenging generation task, aiming at synthesizing a vivid speaking-face video given a specific audio. To fulfill emotion-controllable talking face generation, current methods need to overcome two challenges: One is how to effectively model the multimodal relationship related to the specific emotion, and the other is how to leverage this relationship to synthesize identity preserving emotional videos. In this paper, we propose a novel method to tackle the emotion-controllable talking face generation task discretely. Specifically, we employ two pre-training strategies to disentangle audio into independent components and quantize videos into combinations of visual tokens. Subsequently, we propose the emotion-anchor (EA) representation that integrates the emotional information into visual tokens. Finally, we introduce an autoregressive transformer to model the global distribution of the visual tokens under the given conditions and further predict the index sequence for synthesizing the manipulated videos. We conduct experiments on the MEAD dataset that controls the emotion of videos conditioned on multiple emotional audios. Extensive experiments demonstrate the superiorities of our method both qualitatively and quantitatively.

</details>

### [RealTalk: Realistic Emotion-Aware Lifelike Talking-Head Synthesis](2508.12163.md)
**Wenqing Wang, Yun Fu** · 2025-08-16

<details>
<summary>Abstract</summary>

Emotion is a critical component of artificial social intelligence. However, while current methods excel in lip synchronization and image quality, they often fail to generate accurate and controllable emotional expressions while preserving the subject's identity. To address this challenge, we introduce RealTalk, a novel framework for synthesizing emotional talking heads with high emotion accuracy, enhanced emotion controllability, and robust identity preservation. RealTalk employs a variational autoencoder (VAE) to generate 3D facial landmarks from driving audio, which are concatenated with emotion-label embeddings using a ResNet-based landmark deformation model (LDM) to produce emotional landmarks. These landmarks and facial blendshape coefficients jointly condition a novel tri-plane attention Neural Radiance Field (NeRF) to synthesize highly realistic emotional talking heads. Extensive experiments demonstrate that RealTalk outperforms existing methods in emotion accuracy, controllability, and identity preservation, advancing the development of socially intelligent AI systems.

</details>

### [SpeechForensics: Audio-Visual Speech Representation Learning for Face Forgery Detection](2508.09913.md)
**Yachao Liang, Min Yu, Gang Li, Jianguo Jiang et al.** · 2025-08-13

<details>
<summary>Abstract</summary>

Detection of face forgery videos remains a formidable challenge in the field of digital forensics, especially the generalization to unseen datasets and common perturbations. In this paper, we tackle this issue by leveraging the synergy between audio and visual speech elements, embarking on a novel approach through audio-visual speech representation learning. Our work is motivated by the finding that audio signals, enriched with speech content, can provide precise information effectively reflecting facial movements. To this end, we first learn precise audio-visual speech representations on real videos via a self-supervised masked prediction task, which encodes both local and global semantic information simultaneously. Then, the derived model is directly transferred to the forgery detection task. Extensive experiments demonstrate that our method outperforms the state-of-the-art methods in terms of cross-dataset generalization and robustness, without the participation of any fake video in model training. Code is available at https://github.com/Eleven4AI/SpeechForensics.

</details>

### [Audio-Visual Speech Enhancement: Architectural Design and Deployment Strategies](2508.08468.md)
**Anis Hamadouche, Haifeng Luo, Mathini Sellathurai, Tharm Ratnarajah** · 2025-08-11

<details>
<summary>Abstract</summary>

This paper introduces a new AI-based Audio-Visual Speech Enhancement (AVSE) system and presents a comparative performance analysis of different deployment architectures. The proposed AVSE system employs convolutional neural networks (CNNs) for spectral feature extraction and long short-term memory (LSTM) networks for temporal modeling, enabling robust speech enhancement through multimodal fusion of audio and visual cues. Multiple deployment scenarios are investigated, including cloud-based, edge-assisted, and standalone device implementations. Their performance is evaluated in terms of speech quality improvement, latency, and computational overhead. Real-world experiments are conducted across various network conditions, including Ethernet, Wi-Fi, 4G, and 5G, to analyze the trade-offs between processing delay, communication latency, and perceptual speech quality. The results show that while cloud deployment achieves the highest enhancement quality, edge-assisted architectures offer the best balance between latency and intelligibility, meeting real-time requirements under 5G and Wi-Fi 6 conditions. These findings provide practical guidelines for selecting and optimizing AVSE deployment architectures in diverse applications, including assistive hearing devices, telepresence, and industrial communications.

</details>

### [KLASSify to Verify: Audio-Visual Deepfake Detection Using SSL-based Audio and Handcrafted Visual Features](2508.07337.md)
**Ivan Kukanov, Jun Wah Ng** · 2025-08-10

<details>
<summary>Abstract</summary>

The rapid development of audio-driven talking head generators and advanced Text-To-Speech (TTS) models has led to more sophisticated temporal deepfakes. These advances highlight the need for robust methods capable of detecting and localizing deepfakes, even under novel, unseen attack scenarios. Current state-of-the-art deepfake detectors, while accurate, are often computationally expensive and struggle to generalize to novel manipulation techniques. To address these challenges, we propose multimodal approaches for the AV-Deepfake1M 2025 challenge. For the visual modality, we leverage handcrafted features to improve interpretability and adaptability. For the audio modality, we adapt a self-supervised learning (SSL) backbone coupled with graph attention networks to capture rich audio representations, improving detection robustness. Our approach strikes a balance between performance and real-world deployment, focusing on resilience and potential interpretability. On the AV-Deepfake1M++ dataset, our multimodal system achieves AUC of 92.78% for deepfake classification task and IoU of 0.3536 for temporal localization using only the audio modality.

</details>

### [MotionSwap](2508.06430.md)
**Om Patil, Jinesh Modi, Suryabha Mukhopadhyay, Meghaditya Giri et al.** · 2025-08-08

<details>
<summary>Abstract</summary>

Face swapping technology has gained significant attention in both academic research and commercial applications. This paper presents our implementation and enhancement of SimSwap, an efficient framework for high fidelity face swapping. We introduce several improvements to the original model, including the integration of self and cross-attention mechanisms in the generator architecture, dynamic loss weighting, and cosine annealing learning rate scheduling. These enhancements lead to significant improvements in identity preservation, attribute consistency, and overall visual quality. Our experimental results, spanning 400,000 training iterations, demonstrate progressive improvements in generator and discriminator performance. The enhanced model achieves better identity similarity, lower FID scores, and visibly superior qualitative results compared to the baseline. Ablation studies confirm the importance of each architectural and training improvement. We conclude by identifying key future directions, such as integrating StyleGAN3, improving lip synchronization, incorporating 3D facial modeling, and introducing temporal consistency for video-based applications.

</details>

### [RAP: Real-time Audio-driven Portrait Animation with Video Diffusion Transformer](2508.05115.md)
**Fangyu Du, Taiqing Li, Qian Qiao, Tan Yu et al.** · 2025-08-07

<details>
<summary>Abstract</summary>

Audio-driven portrait animation aims to synthesize realistic and natural talking head videos from an input audio signal and a single reference image. While existing methods achieve high-quality results by leveraging high-dimensional intermediate representations and explicitly modeling motion dynamics, their computational complexity renders them unsuitable for real-time deployment. Real-time inference imposes stringent latency and memory constraints, often necessitating the use of highly compressed latent representations. However, operating in such compact spaces hinders the preservation of fine-grained spatiotemporal details, thereby complicating audio-visual synchronization RAP (Real-time Audio-driven Portrait animation), a unified framework for generating high-quality talking portraits under real-time constraints. Specifically, RAP introduces a hybrid attention mechanism for fine-grained audio control, and a static-dynamic training-inference paradigm that avoids explicit motion supervision. Through these techniques, RAP achieves precise audio-driven control, mitigates long-term temporal drift, and maintains high visual fidelity. Extensive experiments demonstrate that RAP achieves state-of-the-art performance while operating under real-time constraints.

</details>

### [READ: Real-time and Efficient Asynchronous Diffusion for Audio-driven Talking Head Generation](2508.03457.md)
**Haotian Wang, Yuzhe Weng, Jun Du, Haoran Xu et al.** · 2025-08-05

<details>
<summary>Abstract</summary>

The introduction of diffusion models has brought significant advances to the field of audio-driven talking head generation. However, the extremely slow inference speed severely limits the practical implementation of diffusion-based talking head generation models. In this study, we propose READ, a real-time diffusion-transformer-based talking head generation framework. Our approach first learns a spatiotemporal highly compressed video latent space via a temporal VAE, significantly reducing the token count to accelerate generation. To achieve better audio-visual alignment within this compressed latent space, a pre-trained Speech Autoencoder (SpeechAE) is proposed to generate temporally compressed speech latent codes corresponding to the video latent space. These latent representations are then modeled by a carefully designed Audio-to-Video Diffusion Transformer (A2V-DiT) backbone for efficient talking head synthesis. Furthermore, to ensure temporal consistency and accelerated inference in extended generation, we propose a novel asynchronous noise scheduler (ANS) for both the training and inference processes of our framework. The ANS leverages asynchronous add-noise and asynchronous motion-guided generation in the latent space, ensuring consistency in generated video clips. Experimental results demonstrate that READ outperforms state-of-the-art methods by generating competitive talking head videos with significantly reduced runtime, achieving an optimal balance between quality and speed while maintaining robust metric stability in long-time generation.

</details>

### [X-Actor: Emotional and Expressive Long-Range Portrait Acting from Audio](2508.02944.md)
**Chenxu Zhang, Zenan Li, Hongyi Xu, You Xie et al.** · 2025-08-04

<details>
<summary>Abstract</summary>

We present X-Actor, a novel audio-driven portrait animation framework that generates lifelike, emotionally expressive talking head videos from a single reference image and an input audio clip. Unlike prior methods that emphasize lip synchronization and short-range visual fidelity in constrained speaking scenarios, X-Actor enables actor-quality, long-form portrait performance capturing nuanced, dynamically evolving emotions that flow coherently with the rhythm and content of speech. Central to our approach is a two-stage decoupled generation pipeline: an audio-conditioned autoregressive diffusion model that predicts expressive yet identity-agnostic facial motion latent tokens within a long temporal context window, followed by a diffusion-based video synthesis module that translates these motions into high-fidelity video animations. By operating in a compact facial motion latent space decoupled from visual and identity cues, our autoregressive diffusion model effectively captures long-range correlations between audio and facial dynamics through a diffusion-forcing training paradigm, enabling infinite-length emotionally-rich motion prediction without error accumulation. Extensive experiments demonstrate that X-Actor produces compelling, cinematic-style performances that go beyond standard talking head animations and achieves state-of-the-art results in long-range, audio-driven emotional portrait acting.

</details>

### [Wav2Lip-HQ High-Resolution Audio-Driven Lip Synchronization for Realistic Virtual Avatars](s2:aca90d844d61baac040a8cf612d00a5532f33d4b.md)
**Mallikarjuna G D** · 2025-07-31

<details>
<summary>Abstract</summary>

High-quality lip synchronization is essential for creating realistic talking face videos in applications such as virtual interviews, online education, film dubbing, and digital avatars. Traditional lip-sync methods often struggle with maintaining high visual fidelity, especially in high-resolution outputs. To address this challenge, Wav2Lip-HQ introduces an advanced Generative Adversarial Network (GAN)[1]-based solution capable of generating photorealistic, high-resolution lip-synced videos with accurate mouth movements synchronized to any given speech audio. In this research, we evaluate the performance of Wav2Lip-HQ, leveraging its core components, including the lipsync_gan.pth[1] model trained on the LRS2 dataset[1] for precise audio-visual synchronization, the face_segmentation.pth[2] model trained on CelebAMask-HQ for accurate facial region parsing, and the esrgan_max.pth[3] enhancer utilizing DIV2K[3] and CelebA[2] datasets to upscale and refine facial details post-synchronization. We conducted extensive experiments using diverse video-audio pairs to assess the improvement in lip-sync accuracy and overall video quality. Our analysis demonstrates that Wav2Lip-HQ significantly outperforms traditional methods and the original Wav2Lip model by delivering sharper, more coherent, and highly realistic talking face videos. The findings of this study confirm that Wav2Lip-HQ is an effective solution for high-resolution, photorealistic lip synchronization, making it highly applicable for real-world use cases requiring professional-grade video quality. Future work will focus on enhancing emotional expressions and optimizing performance for real-time applications.

</details>

### [DiTalker: A Unified DiT-based Framework for High-Quality and Speaking Styles Controllable Portrait Animation](2508.06511.md)
**He Feng, Yongjia Ma, Donglin Di, Lei Fan et al.** · 2025-07-29

<details>
<summary>Abstract</summary>

Portrait animation aims to synthesize talking videos from a static reference face, conditioned on audio and style frame cues (e.g., emotion and head poses), while ensuring precise lip synchronization and faithful reproduction of speaking styles. Existing diffusion-based portrait animation methods primarily focus on lip synchronization or static emotion transformation, often overlooking dynamic styles such as head movements. Moreover, most of these methods rely on a dual U-Net architecture, which preserves identity consistency but incurs additional computational overhead. To this end, we propose DiTalker, a unified DiT-based framework for speaking style-controllable portrait animation. We design a Style-Emotion Encoding Module that employs two separate branches: a style branch extracting identity-specific style information (e.g., head poses and movements), and an emotion branch extracting identity-agnostic emotion features. We further introduce an Audio-Style Fusion Module that decouples audio and speaking styles via two parallel cross-attention layers, using these features to guide the animation process. To enhance the quality of results, we adopt and modify two optimization constraints: one to improve lip synchronization and the other to preserve fine-grained identity and background details. Extensive experiments demonstrate the superiority of DiTalker in terms of lip synchronization and speaking style controllability. Project Page: https://thenameishope.github.io/DiTalker/

</details>

### [MagicAnime: A Hierarchically Annotated, Multimodal and Multitasking Dataset with Benchmarks for Cartoon Animation Generation](2507.20368.md)
**Shuolin Xu, Bingyuan Wang, Zeyu Cai, Fangteng Fu et al.** · 2025-07-27

<details>
<summary>Abstract</summary>

Generating high-quality cartoon animations multimodal control is challenging due to the complexity of non-human characters, stylistically diverse motions and fine-grained emotions. There is a huge domain gap between real-world videos and cartoon animation, as cartoon animation is usually abstract and has exaggerated motion. Meanwhile, public multimodal cartoon data are extremely scarce due to the difficulty of large-scale automatic annotation processes compared with real-life scenarios. To bridge this gap, We propose the MagicAnime dataset, a large-scale, hierarchically annotated, and multimodal dataset designed to support multiple video generation tasks, along with the benchmarks it includes. Containing 400k video clips for image-to-video generation, 50k pairs of video clips and keypoints for whole-body annotation, 12k pairs of video clips for video-to-video face animation, and 2.9k pairs of video and audio clips for audio-driven face animation. Meanwhile, we also build a set of multi-modal cartoon animation benchmarks, called MagicAnime-Bench, to support the comparisons of different methods in the tasks above. Comprehensive experiments on four tasks, including video-driven face animation, audio-driven face animation, image-to-video animation, and pose-driven character animation, validate its effectiveness in supporting high-fidelity, fine-grained, and controllable generation.

</details>

### [Navigating Large-Pose Challenge for High-Fidelity Face Reenactment with Video Diffusion Model](2507.16341.md)
**Mingtao Guo, Guanyu Xing, Yanci Zhang, Yanli Liu** · 2025-07-22

<details>
<summary>Abstract</summary>

Face reenactment aims to generate realistic talking head videos by transferring motion from a driving video to a static source image while preserving the source identity. Although existing methods based on either implicit or explicit keypoints have shown promise, they struggle with large pose variations due to warping artifacts or the limitations of coarse facial landmarks. In this paper, we present the Face Reenactment Video Diffusion model (FRVD), a novel framework for high-fidelity face reenactment under large pose changes. Our method first employs a motion extractor to extract implicit facial keypoints from the source and driving images to represent fine-grained motion and to perform motion alignment through a warping module. To address the degradation introduced by warping, we introduce a Warping Feature Mapper (WFM) that maps the warped source image into the motion-aware latent space of a pretrained image-to-video (I2V) model. This latent space encodes rich priors of facial dynamics learned from large-scale video data, enabling effective warping correction and enhancing temporal coherence. Extensive experiments show that FRVD achieves superior performance over existing methods in terms of pose accuracy, identity preservation, and visual quality, especially in challenging scenarios with extreme pose variations.

</details>

### [ATL-Diff: Audio-Driven Talking Head Generation with Early Landmarks-Guide Noise Diffusion](2507.12804.md)
**Hoang-Son Vo, Quang-Vinh Nguyen, Seungwon Kim, Hyung-Jeong Yang et al.** · 2025-07-17

<details>
<summary>Abstract</summary>

Audio-driven talking head generation requires precise synchronization between facial animations and audio signals. This paper introduces ATL-Diff, a novel approach addressing synchronization limitations while reducing noise and computational costs. Our framework features three key components: a Landmark Generation Module converting audio to facial landmarks, a Landmarks-Guide Noise approach that decouples audio by distributing noise according to landmarks, and a 3D Identity Diffusion network preserving identity characteristics. Experiments on MEAD and CREMA-D datasets demonstrate that ATL-Diff outperforms state-of-the-art methods across all metrics. Our approach achieves near real-time processing with high-quality animations, computational efficiency, and exceptional preservation of facial nuances. This advancement offers promising applications for virtual assistants, education, medical communication, and digital platforms. The source code is available at: \href{https://github.com/sonvth/ATL-Diff}{https://github.com/sonvth/ATL-Diff}

</details>

### [Think-Before-Draw: Decomposing Emotion Semantics & Fine-Grained Controllable Expressive Talking Head Generation](2507.12761.md)
**Hanlei Shi, Leyuan Qu, Yu Liu, Di Gao et al.** · 2025-07-17

<details>
<summary>Abstract</summary>

Emotional talking-head generation has emerged as a pivotal research area at the intersection of computer vision and multimodal artificial intelligence, with its core value lying in enhancing human-computer interaction through immersive and empathetic engagement.With the advancement of multimodal large language models, the driving signals for emotional talking-head generation has shifted from audio and video to more flexible text. However, current text-driven methods rely on predefined discrete emotion label texts, oversimplifying the dynamic complexity of real facial muscle movements and thus failing to achieve natural emotional expressiveness.This study proposes the Think-Before-Draw framework to address two key challenges: (1) In-depth semantic parsing of emotions--by innovatively introducing Chain-of-Thought (CoT), abstract emotion labels are transformed into physiologically grounded facial muscle movement descriptions, enabling the mapping from high-level semantics to actionable motion features; and (2) Fine-grained expressiveness optimization--inspired by artists' portrait painting process, a progressive guidance denoising strategy is proposed, employing a "global emotion localization--local muscle control" mechanism to refine micro-expression dynamics in generated videos.Our experiments demonstrate that our approach achieves state-of-the-art performance on widely-used benchmarks, including MEAD and HDTF. Additionally, we collected a set of portrait images to evaluate our model's zero-shot generation capability.

</details>

### [Detecting Deepfake Talking Heads from Facial Biometric Anomalies](2507.08917.md)
**Justin D. Norman, Hany Farid** · 2025-07-11

<details>
<summary>Abstract</summary>

The combination of highly realistic voice cloning, along with visually compelling avatar, face-swap, or lip-sync deepfake video generation, makes it relatively easy to create a video of anyone saying anything. Today, such deepfake impersonations are often used to power frauds, scams, and political disinformation. We propose a novel forensic machine learning technique for the detection of deepfake video impersonations that leverages unnatural patterns in facial biometrics. We evaluate this technique across a large dataset of deepfake techniques and impersonations, as well as assess its reliability to video laundering and its generalization to previously unseen video deepfake generators.

</details>

### [MEDTalk: Multimodal Controlled 3D Facial Animation with Dynamic Emotions by Disentangled Embedding](2507.06071.md)
**Chang Liu, Ye Pan, Chenyang Ding, Susanto Rahardja et al.** · 2025-07-08

<details>
<summary>Abstract</summary>

Audio-driven emotional 3D facial animation aims to generate synchronized lip movements and vivid facial expressions. However, most existing approaches focus on static and predefined emotion labels, limiting their diversity and naturalness. To address these challenges, we propose MEDTalk, a novel framework for fine-grained and dynamic emotional talking head generation. Our approach first disentangles content and emotion embedding spaces from motion sequences using a carefully designed cross-reconstruction process, enabling independent control over lip movements and facial expressions. Beyond conventional audio-driven lip synchronization, we integrate audio and speech text, predicting frame-wise intensity variations and dynamically adjusting static emotion features to generate realistic emotional expressions. Furthermore, to enhance control and personalization, we incorporate multimodal inputs-including text descriptions and reference expression images-to guide the generation of user-specified facial expressions. With MetaHuman as the priority, our generated results can be conveniently integrated into the industrial production pipeline. The code is available at: https://github.com/SJTU-Lucy/MEDTalk.

</details>

### [MoDiT: Learning Highly Consistent 3D Motion Coefficients with Diffusion Transformer for Talking Head Generation](2507.05092.md)
**Yucheng Wang, Dan Xu** · 2025-07-07

<details>
<summary>Abstract</summary>

Audio-driven talking head generation is critical for applications such as virtual assistants, video games, and films, where natural lip movements are essential. Despite progress in this field, challenges remain in producing both consistent and realistic facial animations. Existing methods, often based on GANs or UNet-based diffusion models, face three major limitations: (i) temporal jittering caused by weak temporal constraints, resulting in frame inconsistencies; (ii) identity drift due to insufficient 3D information extraction, leading to poor preservation of facial identity; and (iii) unnatural blinking behavior due to inadequate modeling of realistic blink dynamics. To address these issues, we propose MoDiT, a novel framework that combines the 3D Morphable Model (3DMM) with a Diffusion-based Transformer. Our contributions include: (i) A hierarchical denoising strategy with revised temporal attention and biased self/cross-attention mechanisms, enabling the model to refine lip synchronization and progressively enhance full-face coherence, effectively mitigating temporal jittering. (ii) The integration of 3DMM coefficients to provide explicit spatial constraints, ensuring accurate 3D-informed optical flow prediction and improved lip synchronization using Wav2Lip results, thereby preserving identity consistency. (iii) A refined blinking strategy to model natural eye movements, with smoother and more realistic blinking behaviors.

</details>

### [MoDA: Multi-modal Diffusion Architecture for Talking Head Generation](2507.03256.md)
**Xinyang Li, Gen Li, Zhihui Lin, Yichen Qian et al.** · 2025-07-04

<details>
<summary>Abstract</summary>

Talking head generation with arbitrary identities and speech audio remains a crucial problem in the realm of the virtual metaverse. Recently, diffusion models have become a popular generative technique in this field with their strong generation capabilities. However, several challenges remain for diffusion-based methods: 1) inefficient inference and visual artifacts caused by the implicit latent space of Variational Auto-Encoders (VAE), which complicates the diffusion process; 2) a lack of authentic facial expressions and head movements due to inadequate multi-modal information fusion. In this paper, MoDA handles these challenges by: 1) defining a joint parameter space that bridges motion generation and neural rendering, and leveraging flow matching to simplify diffusion learning; 2) introducing a multi-modal diffusion architecture to model the interaction among noisy motion, audio, and auxiliary conditions, enhancing overall facial expressiveness. In addition, a coarse-to-fine fusion strategy is employed to progressively integrate different modalities, ensuring effective feature fusion. Experimental results demonstrate that MoDA improves video diversity, realism, and efficiency, making it suitable for real-world applications. Project Page: https://lixinyyang.github.io/MoDA.github.io/

</details>

### [Multimodal Feature-Guided Audio-Driven Emotional Talking Face Generation](s2:49c1bcd1d1eb546f2454dfaef7491897a1744a9c.md)
**Xueping Wang, Yuemeng Huo, Yanan Liu, Xueni Guo et al.** · 2025-07-02

<details>
<summary>Abstract</summary>

Audio-driven emotional talking face generation aims to generate talking face videos with rich facial expressions and temporal coherence. Current diffusion model-based approaches predominantly depend on either single-label emotion annotations or external video references, which often struggle to capture the complex relationships between modalities, resulting in less natural emotional expressions. To address these issues, we propose MF-ETalk, a multimodal feature-guided method for emotional talking face generation. Specifically, we design an emotion-aware multimodal feature disentanglement and fusion framework that leverages Action Units (AUs) to disentangle facial expressions and models the nonlinear relationships among AU features using a residual encoder. Furthermore, we introduce a hierarchical multimodal feature fusion module that enables dynamic interactions among audio, visual cues, AUs, and motion dynamics. This module is optimized through global motion modeling, lip synchronization, and expression subspace learning, enabling full-face dynamic generation. Finally, an emotion-consistency constraint module is employed to refine the generated results and ensure the naturalness of expressions. Extensive experiments on the MEAD and HDTF datasets demonstrate that MF-ETalk outperforms state-of-the-art methods in both expression naturalness and lip-sync accuracy. For example, it achieves an FID of 43.052 and E-FID of 2.403 on MEAD, along with strong synchronization performance (LSE-C of 6.781, LSE-D of 7.962), confirming the effectiveness of our approach in producing realistic and emotionally expressive talking face videos.

</details>

### [JAM-Flow: Joint Audio-Motion Synthesis with Flow Matching](2506.23552.md)
**Mingi Kwon, Joonghyuk Shin, Jaeseok Jung, Jaesik Park et al.** · 2025-06-30

<details>
<summary>Abstract</summary>

The intrinsic link between facial motion and speech is often overlooked in generative modeling, where talking head synthesis and text-to-speech (TTS) are typically addressed as separate tasks. This paper introduces JAM-Flow, a unified framework to simultaneously synthesize and condition on both facial motion and speech. Our approach leverages flow matching and a novel Multi-Modal Diffusion Transformer (MM-DiT) architecture, integrating specialized Motion-DiT and Audio-DiT modules. These are coupled via selective joint attention layers and incorporate key architectural choices, such as temporally aligned positional embeddings and localized joint attention masking, to enable effective cross-modal interaction while preserving modality-specific strengths. Trained with an inpainting-style objective, JAM-Flow supports a wide array of conditioning inputs-including text, reference audio, and reference motion-facilitating tasks such as synchronized talking head generation from text, audio-driven animation, and much more, within a single, coherent model. JAM-Flow significantly advances multi-modal generative modeling by providing a practical solution for holistic audio-visual synthesis. project page: https://joonghyuk.com/jamflow-web

</details>

### [ConAvatar: Harnessing Facial Mesh for Controllable Avatar Animation](s2:a862f36ce73d574aad5b4a06f70f05e440acc3f5.md)
**Zheng Tan, Wei Wei** · 2025-06-30

<details>
<summary>Abstract</summary>

Recent advancements in talking head generation have focused on temporal consistency and lip-sync accuracy, but controlling the head pose remains a challenge. Existing methods often rely on reference videos or random generation, leading to unrealistic results. In this paper, we propose ConAvatar, a novel framework that enables precise control over head pose while generating realistic talking heads. Our approach consists of two stages: first, converting control information (Euler angles and position) into 3D facial meshes; second, using these structured information to guide a diffusion model for realistic video generation. This allows the talking head to move in sync with both speech and pose, ensuring natural, controlled head movements. Extensive experiments show that our method delivers high-quality results with improved temporal consistency, accurate lip-sync, and controllable head pose, effectively demonstrating the validity and effectiveness of our approach in realistic talking head synthesis.

</details>

### [EmoHuman: Fine-Grained Emotion-Controlled Talking Head Generation via Audio-Text Multimodal Detangling](s2:001006557262952b7a5d58265206618f486d6ed6.md)
**Qifeng Dai, Huidong Feng, Wendi Cui, Xinqi Cai et al.** · 2025-06-30

<details>
<summary>Abstract</summary>

Audio-driven talking head generation has made significant strides in creating realistic and lip-synchronized portraits. However, most existing approaches overlook facial expressions, with only a few attempting to model facial emotions explicitly, often leading to unnatural results. To address this gap, we introduce EmoHuman, an audio-to-video synthesis method that generates emotionally nuanced talking head videos without relying on intermediate 3D representations or facial landmarks. EmoHuman decouples content, emotion, and emotional intensity from the multimodal information of the audio and the corresponding textual content through an Audio Emotion Decoupling Module. The content features are used to drive a powerful video diffusion model, generating synchronized lip movements, while emotion and emotional intensity govern the simulation of facial expressions, resulting in more realistic video outputs. Extensive experiments demonstrate that EmoHuman outperforms state-of-the-art methods in image and video quality, expression correlation, and lip-synchronization accuracy.

</details>

### [GE-Talker: Generalizable and Efficient Neural Rendering for Talking Head Generation](s2:ab7592118a4e5ba323dd9be80ba30f2ce810347f.md)
**Zixuan Wang, Li Fang, Fei Hu, L. Ye** · 2025-06-30

<details>
<summary>Abstract</summary>

Talking head generation aims to create videos that preserve a source character’s identity while replicating synchronized lip movements, facial expressions, and head gestures from audio inputs. While personalized methods have achieved impressive results by training neural radiance fields (NeRFs) for specific identities, they often face limitations in generalization and incur high computational costs due to identity-specific retraining. We propose GE-Talker, a Generalizable and Efficient NeRF for talking head generation, which addresses these challenges through two key innovations. First, we leverage FLAME-based full-head modeling as intermediate representations, conditioned on audio features, to achieve precise lip synchronization and natural facial movements. Second, we introduce a semantic-aware depth-guided sampling strategy that uses FLAME-generated depth maps to restrict sampling ranges and semantic segmentation to focus on human regions, improving rendering quality and efficiency. GE-Talker achieves high-quality outputs for unseen speaker identities with a 109% speed-up over baseline methods and enables rapid fine-tuning on new speakers within 14 minutes, establishing it as a powerful and adaptable solution for talking head generation.

</details>

### [Audio-Driven Emotion-Aware 3D Talking Face Generation from Single Image](s2:9fde057351c2841cfd3b47d3ed719e1b4f0012e2.md)
**Chun-Shuo Qiu, Feng-Lin Liu, Hongbo Fu, Fan Zhang et al.** · 2025-06-30

<details>
<summary>Abstract</summary>

Audio-driven talking face generation from a single source image is a popular research topic. There still exist many challenges for its practical applications, e.g., diverse motion generation, effective emotional control, and large view angle changes. In this work, we propose a novel one-shot emotion-controllable audio-driven 3D talking face generation framework, which creates free-view talking videos from one reference image. Firstly, to synchronize the motion with the input audio, we use a transformer-based motion generator to capture the context of the input audio and predict motion coefficient sequences, which are leveraged by a motion encoder to extract motion codes. Meanwhile, to reconstruct a 3D portrait from one reference image, an identity encoder is utilized to extract an identity code and generate emotion-dependent appearance with a specific emotion label. Finally, we introduce an emotion-controllable 3D portrait video generator to synthesize free-view talking videos using the disentangled motion and identity codes. Thanks to the audio-synchronized motion codes and emotion-aware identity code, we can render a talking face with realistic emotional expressions in novel views. Extensive experiments show that our method is capable of maintaining superior visual performance and motion accuracy in both front view and novel views.

</details>

### [Few-Shot Identity Adaptation for 3D Talking Heads via Global Gaussian Field](2506.22044.md)
**Hong Nie, Fuyuan Cao, Lu Chen, Fengxin Chen et al.** · 2025-06-27

<details>
<summary>Abstract</summary>

Reconstruction and rendering-based talking head synthesis methods achieve high-quality results with strong identity preservation but are limited by their dependence on identity-specific models. Each new identity requires training from scratch, incurring high computational costs and reduced scalability compared to generative model-based approaches. To overcome this limitation, we propose FIAG, a novel 3D speaking head synthesis framework that enables efficient identity-specific adaptation using only a few training footage. FIAG incorporates Global Gaussian Field, which supports the representation of multiple identities within a shared field, and Universal Motion Field, which captures the common motion dynamics across diverse identities. Benefiting from the shared facial structure information encoded in the Global Gaussian Field and the general motion priors learned in the motion field, our framework enables rapid adaptation from canonical identity representations to specific ones with minimal data. Extensive comparative and ablation experiments demonstrate that our method outperforms existing state-of-the-art approaches, validating both the effectiveness and generalizability of the proposed framework. Code is available at: \textit{https://github.com/gme-hong/FIAG}.

</details>

### [Advancing Talking Head Generation: A Comprehensive Survey of Multi-Modal Methodologies, Datasets, Evaluation Metrics, and Loss Functions](2507.02900.md)
**Vineet Kumar Rakesh, Soumya Mazumdar, Research Pratim Maity, Sarbajit Pal et al.** · 2025-06-23

<details>
<summary>Abstract</summary>

Talking Head Generation (THG) has emerged as a transformative technology in computer vision, enabling the synthesis of realistic human faces synchronized with image, audio, text, or video inputs. This paper provides a comprehensive review of methodologies and frameworks for talking head generation, categorizing approaches into 2D--based, 3D--based, Neural Radiance Fields (NeRF)--based, diffusion--based, parameter-driven techniques and many other techniques. It evaluates algorithms, datasets, and evaluation metrics while highlighting advancements in perceptual realism and technical efficiency critical for applications such as digital avatars, video dubbing, ultra-low bitrate video conferencing, and online education. The study identifies challenges such as reliance on pre--trained models, extreme pose handling, multilingual synthesis, and temporal consistency. Future directions include modular architectures, multilingual datasets, hybrid models blending pre--trained and task-specific layers, and innovative loss functions. By synthesizing existing research and exploring emerging trends, this paper aims to provide actionable insights for researchers and practitioners in the field of talking head generation. For the complete survey, code, and curated resource list, visit our GitHub repository: https://github.com/VineetKumarRakesh/thg.

</details>

### [Compressed Video Super-Resolution based on Hierarchical Encoding](2506.14381.md)
**Yuxuan Jiang, Siyue Teng, Qiang Zhu, Chen Feng et al.** · 2025-06-17

<details>
<summary>Abstract</summary>

This paper presents a general-purpose video super-resolution (VSR) method, dubbed VSR-HE, specifically designed to enhance the perceptual quality of compressed content. Targeting scenarios characterized by heavy compression, the method upscales low-resolution videos by a ratio of four, from 180p to 720p or from 270p to 1080p. VSR-HE adopts hierarchical encoding transformer blocks and has been sophisticatedly optimized to eliminate a wide range of compression artifacts commonly introduced by H.265/HEVC encoding across various quantization parameter (QP) levels. To ensure robustness and generalization, the model is trained and evaluated under diverse compression settings, allowing it to effectively restore fine-grained details and preserve visual fidelity. The proposed VSR-HE has been officially submitted to the ICME 2025 Grand Challenge on VSR for Video Conferencing (Team BVI-VSR), under both the Track 1 (General-Purpose Real-World Video Content) and Track 2 (Talking Head Videos).

</details>

### [Audio-Visual Driven Compression for Low-Bitrate Talking Head Videos](2506.13419.md)
**Riku Takahashi, Ryugo Morita, Jinjia Zhou** · 2025-06-16

<details>
<summary>Abstract</summary>

Talking head video compression has advanced with neural rendering and keypoint-based methods, but challenges remain, especially at low bit rates, including handling large head movements, suboptimal lip synchronization, and distorted facial reconstructions. To address these problems, we propose a novel audio-visual driven video codec that integrates compact 3D motion features and audio signals. This approach robustly models significant head rotations and aligns lip movements with speech, improving both compression efficiency and reconstruction quality. Experiments on the CelebV-HQ dataset show that our method reduces bitrate by 22% compared to VVC and by 8.5% over state-of-the-art learning-based codec. Furthermore, it provides superior lip-sync accuracy and visual fidelity at comparable bitrates, highlighting its effectiveness in bandwidth-constrained scenarios.

</details>

### [Viseme Morphing and Text-to-Speech Integration for Indonesian News Broadcasting](s2:de6942a79eaf13d3334a57729f09995a4851f822.md)
**Mirza Ardiana** · 2025-06-16

<details>
<summary>Abstract</summary>

Advancements in multimedia technology and artificial intelligence have driven innovation in digital broadcasting, including virtual newsreaders. This study proposes a text-to-speech-based lip-sync animation system specifically for the Indonesian language to improve synchronization between lip movements and speech. The primary challenge in developing this system lies in generating realistic lip animations that correspond with the phonetic structure of Indonesian. The system workflow involves text input, syllable parsing using the Finite State Automata (FSA) method, viseme conversion (viseme morphing), and web-based animation output. Test results show a viseme duration accuracy of 98.5%, voice-lip movement synchronization of 94.26%, and a Mean Opinion Score (MOS) of 77.12%, indicating that the system is reasonably feasible for implementation. Despite minor delays, the system demonstrates strong potential for further development through the integration of Natural Language Processing (NLP) and deep learning, which could improve viseme mapping accuracy and enhance system flexibility across various digital broadcasting platforms.

</details>

### [ICME 2025 Grand Challenge on Video Super-Resolution for Video Conferencing](2506.12269.md)
**Babak Naderi, Ross Cutler, Juhee Cho, Nabakumar Khongbantabam et al.** · 2025-06-13

<details>
<summary>Abstract</summary>

Super-Resolution (SR) is a critical task in computer vision, focusing on reconstructing high-resolution (HR) images from low-resolution (LR) inputs. The field has seen significant progress through various challenges, particularly in single-image SR. Video Super-Resolution (VSR) extends this to the temporal domain, aiming to enhance video quality using methods like local, uni-, bi-directional propagation, or traditional upscaling followed by restoration. This challenge addresses VSR for conferencing, where LR videos are encoded with H.265 at fixed QPs. The goal is to upscale videos by a specific factor, providing HR outputs with enhanced perceptual quality under a low-delay scenario using causal models. The challenge included three tracks: general-purpose videos, talking head videos, and screen content videos, with separate datasets provided by the organizers for training, validation, and testing. We open-sourced a new screen content dataset for the SR task in this challenge. Submissions were evaluated through subjective tests using a crowdsourced implementation of the ITU-T Rec P.910.

</details>

### [HunyuanVideo-HOMA: Generic Human-Object Interaction in Multimodal Driven Human Animation](2506.08797.md)
**Ziyao Huang, Zixiang Zhou, Juan Cao, Yifeng Ma et al.** · 2025-06-10

<details>
<summary>Abstract</summary>

To address key limitations in human-object interaction (HOI) video generation -- specifically the reliance on curated motion data, limited generalization to novel objects/scenarios, and restricted accessibility -- we introduce HunyuanVideo-HOMA, a weakly conditioned multimodal-driven framework. HunyuanVideo-HOMA enhances controllability and reduces dependency on precise inputs through sparse, decoupled motion guidance. It encodes appearance and motion signals into the dual input space of a multimodal diffusion transformer (MMDiT), fusing them within a shared context space to synthesize temporally consistent and physically plausible interactions. To optimize training, we integrate a parameter-space HOI adapter initialized from pretrained MMDiT weights, preserving prior knowledge while enabling efficient adaptation, and a facial cross-attention adapter for anatomically accurate audio-driven lip synchronization. Extensive experiments confirm state-of-the-art performance in interaction naturalness and generalization under weak supervision. Finally, HunyuanVideo-HOMA demonstrates versatility in text-conditioned generation and interactive object manipulation, supported by a user-friendly demo interface. The project page is at https://anonymous.4open.science/w/homa-page-0FBE/.

</details>

### [Hallo4: High-Fidelity Dynamic Portrait Animation via Direct Preference Optimization](2505.23525.md)
**Jiahao Cui, Yan Chen, Mingwang Xu, Hanlin Shang et al.** · 2025-05-29

<details>
<summary>Abstract</summary>

Generating highly dynamic and photorealistic portrait animations driven by audio and skeletal motion remains challenging due to the need for precise lip synchronization, natural facial expressions, and high-fidelity body motion dynamics. We propose a human-preference-aligned diffusion framework that addresses these challenges through two key innovations. First, we introduce direct preference optimization tailored for human-centric animation, leveraging a curated dataset of human preferences to align generated outputs with perceptual metrics for portrait motion-video alignment and naturalness of expression. Second, the proposed temporal motion modulation resolves spatiotemporal resolution mismatches by reshaping motion conditions into dimensionally aligned latent features through temporal channel redistribution and proportional feature expansion, preserving the fidelity of high-frequency motion details in diffusion-based synthesis. The proposed mechanism is complementary to existing UNet and DiT-based portrait diffusion approaches, and experiments demonstrate obvious improvements in lip-audio synchronization, expression vividness, body motion coherence over baseline methods, alongside notable gains in human preference metrics. Our model and source code can be found at: https://github.com/fudan-generative-vision/hallo4.

</details>

### [FaceEditTalker: Controllable Talking Head Generation with Facial Attribute Editing](2505.22141.md)
**Guanwen Feng, Zhiyuan Ma, Yunan Li, Jiahao Yang et al.** · 2025-05-28

<details>
<summary>Abstract</summary>

Recent advances in audio-driven talking head generation have achieved impressive results in lip synchronization and emotional expression. However, they largely overlook the crucial task of facial attribute editing. This capability is indispensable for achieving deep personalization and expanding the range of practical applications, including user-tailored digital avatars, engaging online education content, and brand-specific digital customer service. In these key domains, flexible adjustment of visual attributes, such as hairstyle, accessories, and subtle facial features, is essential for aligning with user preferences, reflecting diverse brand identities and adapting to varying contextual demands. In this paper, we present FaceEditTalker, a unified framework that enables controllable facial attribute manipulation while generating high-quality, audio-synchronized talking head videos. Our method consists of two key components: an image feature space editing module, which extracts semantic and detail features and allows flexible control over attributes like expression, hairstyle, and accessories; and an audio-driven video generation module, which fuses these edited features with audio-guided facial landmarks to drive a diffusion-based generator. This design ensures temporal coherence, visual fidelity, and identity preservation across frames. Extensive experiments on public datasets demonstrate that our method achieves comparable or superior performance to representative baseline methods in lip-sync accuracy, video quality, and attribute controllability. Project page: https://peterfanfan.github.io/FaceEditTalker/

</details>

### [OmniSync: Towards Universal Lip Synchronization via Diffusion Transformers](2505.21448.md)
**Ziqiao Peng, Jiwen Liu, Haoxian Zhang, Xiaoqiang Liu et al.** · 2025-05-27

<details>
<summary>Abstract</summary>

Lip synchronization is the task of aligning a speaker's lip movements in video with corresponding speech audio, and it is essential for creating realistic, expressive video content. However, existing methods often rely on reference frames and masked-frame inpainting, which limit their robustness to identity consistency, pose variations, facial occlusions, and stylized content. In addition, since audio signals provide weaker conditioning than visual cues, lip shape leakage from the original video will affect lip sync quality. In this paper, we present OmniSync, a universal lip synchronization framework for diverse visual scenarios. Our approach introduces a mask-free training paradigm using Diffusion Transformer models for direct frame editing without explicit masks, enabling unlimited-duration inference while maintaining natural facial dynamics and preserving character identity. During inference, we propose a flow-matching-based progressive noise initialization to ensure pose and identity consistency, while allowing precise mouth-region editing. To address the weak conditioning signal of audio, we develop a Dynamic Spatiotemporal Classifier-Free Guidance (DS-CFG) mechanism that adaptively adjusts guidance strength over time and space. We also establish the AIGC-LipSync Benchmark, the first evaluation suite for lip synchronization in diverse AI-generated videos. Extensive experiments demonstrate that OmniSync significantly outperforms prior methods in both visual quality and lip sync accuracy, achieving superior results in both real-world and AI-generated videos.

</details>

### [Total-Editing: Head Avatar with Editable Appearance, Motion, and Lighting](2505.20582.md)
**Yizhou Zhao, Chunjiang Liu, Haoyu Chen, Bhiksha Raj et al.** · 2025-05-26

<details>
<summary>Abstract</summary>

Face reenactment and portrait relighting are essential tasks in portrait editing, yet they are typically addressed independently, without much synergy. Most face reenactment methods prioritize motion control and multiview consistency, while portrait relighting focuses on adjusting shading effects. To take advantage of both geometric consistency and illumination awareness, we introduce Total-Editing, a unified portrait editing framework that enables precise control over appearance, motion, and lighting. Specifically, we design a neural radiance field decoder with intrinsic decomposition capabilities. This allows seamless integration of lighting information from portrait images or HDR environment maps into synthesized portraits. We also incorporate a moving least squares based deformation field to enhance the spatiotemporal coherence of avatar motion and shading effects. With these innovations, our unified framework significantly improves the quality and realism of portrait editing results. Further, the multi-source nature of Total-Editing supports more flexible applications, such as illumination transfer from one portrait to another, or portrait animation with customized backgrounds.

</details>

### [Research on lip synthesis of virtual digital humans based on the Spark large model](s2:4d808178b1a61adeb25368223adf92728e46cd5c.md)
**Yuqi Huang** · 2025-05-09

<details>
<summary>Abstract</summary>

In recent years, with the support of key technologies such as deep learning algorithms, computer vision, natural language processing, and graphics rendering, the production process of virtual digital humans has achieved revolutionary breakthroughs. Lip synthesis technology, as a crucial component, has also garnered widespread attention. Most existing lip synthesis models are trained on English datasets, resulting in poor synthesis effects in Chinese contexts. This paper, based on the study of the Wav2Lip lip synthesis model, constructs a Chinese lip-sync dataset and conducts a series of training fine-tunings to achieve better synthesis effects. By leveraging the multimodal capabilities of the Spark large model, it realizes efficient speech-driven facial animation generation. Furthermore, this paper explores the application potential of the Wav2Lip model, providing a solid theoretical foundation and technical support for future commercial applications.

</details>

### [OXSeg: Multidimensional attention UNet-based lip segmentation using semi-supervised lip contours](2505.05531.md)
**Hanie Moghaddasi, Christina Chambers, Sarah N. Mattson, Jeffrey R. Wozniak et al.** · 2025-05-08

<details>
<summary>Abstract</summary>

Lip segmentation plays a crucial role in various domains, such as lip synchronization, lipreading, and diagnostics. However, the effectiveness of supervised lip segmentation is constrained by the availability of lip contour in the training phase. A further challenge with lip segmentation is its reliance on image quality , lighting, and skin tone, leading to inaccuracies in the detected boundaries. To address these challenges, we propose a sequential lip segmentation method that integrates attention UNet and multidimensional input. We unravel the micro-patterns in facial images using local binary patterns to build multidimensional inputs. Subsequently, the multidimensional inputs are fed into sequential attention UNets, where the lip contour is reconstructed. We introduce a mask generation method that uses a few anatomical landmarks and estimates the complete lip contour to improve segmentation accuracy. This mask has been utilized in the training phase for lip segmentation. To evaluate the proposed method, we use facial images to segment the upper lips and subsequently assess lip-related facial anomalies in subjects with fetal alcohol syndrome (FAS). Using the proposed lip segmentation method, we achieved a mean dice score of 84.75%, and a mean pixel accuracy of 99.77% in upper lip segmentation. To further evaluate the method, we implemented classifiers to identify those with FAS. Using a generative adversarial network (GAN), we reached an accuracy of 98.55% in identifying FAS in one of the study populations. This method could be used to improve lip segmentation accuracy, especially around Cupid's bow, and shed light on distinct lip-related characteristics of FAS.

</details>

### [OT-Talk: Animating 3D Talking Head with Optimal Transportation](2505.01932.md)
**Xinmu Wang, Xiang Gao, Xiyun Song, Heather Yu et al.** · 2025-05-03

<details>
<summary>Abstract</summary>

Animating 3D head meshes using audio inputs has significant applications in AR/VR, gaming, and entertainment through 3D avatars. However, bridging the modality gap between speech signals and facial dynamics remains a challenge, often resulting in incorrect lip syncing and unnatural facial movements. To address this, we propose OT-Talk, the first approach to leverage optimal transportation to optimize the learning model in talking head animation. Building on existing learning frameworks, we utilize a pre-trained Hubert model to extract audio features and a transformer model to process temporal sequences. Unlike previous methods that focus solely on vertex coordinates or displacements, we introduce Chebyshev Graph Convolution to extract geometric features from triangulated meshes. To measure mesh dissimilarities, we go beyond traditional mesh reconstruction errors and velocity differences between adjacent frames. Instead, we represent meshes as probability measures and approximate their surfaces. This allows us to leverage the sliced Wasserstein distance for modeling mesh variations. This approach facilitates the learning of smooth and accurate facial motions, resulting in coherent and natural facial animations. Our experiments on two public audio-mesh datasets demonstrate that our method outperforms state-of-the-art techniques both quantitatively and qualitatively in terms of mesh reconstruction accuracy and temporal alignment. In addition, we conducted a user perception study with 20 volunteers to further assess the effectiveness of our approach.

</details>

### [Model See Model Do: Speech-Driven Facial Animation with Style Control](2505.01319.md)
**Yifang Pan, Karan Singh, Luiz Gustavo Hafemann** · 2025-05-02

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation plays a key role in applications such as virtual avatars, gaming, and digital content creation. While existing methods have made significant progress in achieving accurate lip synchronization and generating basic emotional expressions, they often struggle to capture and effectively transfer nuanced performance styles. We propose a novel example-based generation framework that conditions a latent diffusion model on a reference style clip to produce highly expressive and temporally coherent facial animations. To address the challenge of accurately adhering to the style reference, we introduce a novel conditioning mechanism called style basis, which extracts key poses from the reference and additively guides the diffusion generation process to fit the style without compromising lip synchronization quality. This approach enables the model to capture subtle stylistic cues while ensuring that the generated animations align closely with the input speech. Extensive qualitative, quantitative, and perceptual evaluations demonstrate the effectiveness of our method in faithfully reproducing the desired style while achieving superior lip synchronization across various speech scenarios.

</details>

### [Audio-Driven Talking Face Generation With Segmented Static Facial References for Customized Health Device Interactions](s2:dc0087781c32ad17f315f856e42f53af965bb8c3.md)
**Zige Wang, Yashuai Wang, Tianyu Liu, Peng Zhang et al.** · 2025-05-01

<details>
<summary>Abstract</summary>

In a variety of human-machine interaction (HMI) applications, the high-level techniques based on audio-driven talking face generation are often challenged by the issues of temporal misalignment and low-quality outputs. Recent solutions have sought to improve synchronization by maximizing the similarity between audio-visual pairs. However, the temporal disturbances introduced during the inference phase continue to limit the enhancement of generative performance. Inspired by the intrinsic connection between the segmented static facial image and the stable appearance representation, in this study, two strategies, Manual Temporal Segmentation (MTS) and Static Facial Reference (SFR), are proposed to improve performance during the inference stage. The corresponding functionality consists of: MTS involves segmenting the input video into several clips, effectively reducing the complexity of the inference process, and SFR utilizes static facial references to mitigate the temporal noise generated by dynamic sequences, thereby enhancing the quality of the generated outputs. Substantial experiments on the LRS2 and VoxCeleb2 datasets have demonstrated that the proposed strategies are able to significantly enhance inference performance with the LSE-C and LSE-D metrics, without altering the network architecture or training strategy. For effectiveness validation in realistic scenario applications, a deployment has also been conducted on the healthcare devices with the proposed solution.

</details>

### [MagicPortrait: Temporally Consistent Face Reenactment with 3D Geometric Guidance](2504.21497.md)
**Mengting Wei, Yante Li, Tuomas Varanka, Yan Jiang et al.** · 2025-04-30

<details>
<summary>Abstract</summary>

In this study, we propose a method for video face reenactment that integrates a 3D face parametric model into a latent diffusion framework, aiming to improve shape consistency and motion control in existing video-based face generation approaches. Our approach employs the FLAME (Faces Learned with an Articulated Model and Expressions) model as the 3D face parametric representation, providing a unified framework for modeling face expressions and head pose. This not only enables precise extraction of motion features from driving videos, but also contributes to the faithful preservation of face shape and geometry. Specifically, we enhance the latent diffusion model with rich 3D expression and detailed pose information by incorporating depth maps, normal maps, and rendering maps derived from FLAME sequences. These maps serve as motion guidance and are encoded into the denoising UNet through a specifically designed Geometric Guidance Encoder (GGE). A multi-layer feature fusion module with integrated self-attention mechanisms is used to combine facial appearance and motion latent features within the spatial domain. By utilizing the 3D face parametric model as motion guidance, our method enables parametric alignment of face identity between the reference image and the motion captured from the driving video. Experimental results on benchmark datasets show that our method excels at generating high-quality face animations with precise expression and head pose variation modeling. In addition, it demonstrates strong generalization performance on out-of-domain images. Code is publicly available at https://github.com/weimengting/MagicPortrait.

</details>

### [IM-Portrait: Learning 3D-aware Video Diffusion for Photorealistic Talking Heads from Monocular Videos](2504.19165.md)
**Yuan Li, Ziqian Bai, Feitong Tan, Zhaopeng Cui et al.** · 2025-04-27

<details>
<summary>Abstract</summary>

We propose a novel 3D-aware diffusion-based method for generating photorealistic talking head videos directly from a single identity image and explicit control signals (e.g., expressions). Our method generates Multiplane Images (MPIs) that ensure geometric consistency, making them ideal for immersive viewing experiences like binocular videos for VR headsets. Unlike existing methods that often require a separate stage or joint optimization to reconstruct a 3D representation (such as NeRF or 3D Gaussians), our approach directly generates the final output through a single denoising process, eliminating the need for post-processing steps to render novel views efficiently. To effectively learn from monocular videos, we introduce a training mechanism that reconstructs the output MPI randomly in either the target or the reference camera space. This approach enables the model to simultaneously learn sharp image details and underlying 3D information. Extensive experiments demonstrate the effectiveness of our method, which achieves competitive avatar quality and novel-view rendering capabilities, even without explicit 3D reconstruction or high-quality multi-view training data.

</details>

### [Disentangle Identity, Cooperate Emotion: Correlation-Aware Emotional Talking Portrait Generation](2504.18087.md)
**Weipeng Tan, Chuming Lin, Chengming Xu, FeiFan Xu et al.** · 2025-04-25

<details>
<summary>Abstract</summary>

Recent advances in Talking Head Generation (THG) have achieved impressive lip synchronization and visual quality through diffusion models; yet existing methods struggle to generate emotionally expressive portraits while preserving speaker identity. We identify three critical limitations in current emotional talking head generation: insufficient utilization of audio's inherent emotional cues, identity leakage in emotion representations, and isolated learning of emotion correlations. To address these challenges, we propose a novel framework dubbed as DICE-Talk, following the idea of disentangling identity with emotion, and then cooperating emotions with similar characteristics. First, we develop a disentangled emotion embedder that jointly models audio-visual emotional cues through cross-modal attention, representing emotions as identity-agnostic Gaussian distributions. Second, we introduce a correlation-enhanced emotion conditioning module with learnable Emotion Banks that explicitly capture inter-emotion relationships through vector quantization and attention-based feature aggregation. Third, we design an emotion discrimination objective that enforces affective consistency during the diffusion process through latent-space classification. Extensive experiments on MEAD and HDTF datasets demonstrate our method's superiority, outperforming state-of-the-art approaches in emotion accuracy while maintaining competitive lip-sync performance. Qualitative results and user studies further confirm our method's ability to generate identity-preserving portraits with rich, correlated emotional expressions that naturally adapt to unseen identities.

</details>

### [Supervising 3D Talking Head Avatars with Analysis-by-Audio-Synthesis](2504.13386.md)
**Radek Daněček, Carolin Schmitt, Senya Polikovsky, Michael J. Black** · 2025-04-18

<details>
<summary>Abstract</summary>

In order to be widely applicable, speech-driven 3D head avatars must articulate their lips in accordance with speech, while also conveying the appropriate emotions with dynamically changing facial expressions. The key problem is that deterministic models produce high-quality lip-sync but without rich expressions, whereas stochastic models generate diverse expressions but with lower lip-sync quality. To get the best of both, we seek a stochastic model with accurate lip-sync. To that end, we develop a new approach based on the following observation: if a method generates realistic 3D lip motions, it should be possible to infer the spoken audio from the lip motion. The inferred speech should match the original input audio, and erroneous predictions create a novel supervision signal for training 3D talking head avatars with accurate lip-sync. To demonstrate this effect, we propose THUNDER (Talking Heads Under Neural Differentiable Elocution Reconstruction), a 3D talking head avatar framework that introduces a novel supervision mechanism via differentiable sound production. First, we train a novel mesh-to-speech model that regresses audio from facial animation. Then, we incorporate this model into a diffusion-based talking avatar framework. During training, the mesh-to-speech model takes the generated animation and produces a sound that is compared to the input speech, creating a differentiable analysis-by-audio-synthesis supervision loop. Our extensive qualitative and quantitative experiments demonstrate that THUNDER significantly improves the quality of the lip-sync of talking head avatars while still allowing for generation of diverse, high-quality, expressive facial animations. The code and models will be available at https://thunder.is.tue.mpg.de/

</details>

### [Hierarchically Controlled Deformable 3D Gaussians for Talking Head Synthesis](s2:e4c1fe41a4249e205fe596b17e921199d5333b12.md)
**Zhenhua Wu, Linxuan Jiang, Xiang Li, Chaowei Fang et al.** · 2025-04-11

<details>
<summary>Abstract</summary>

Audio-driven talking head synthesis is a critical task in digital human modeling. While recent advances using diffusion models and Neural Radiance Fields (NeRF) have improved visual quality, they often require substantial computational resources, limiting practical deployment. We present a novel framework for audio-driven talking head synthesis, namely it Hierarchically Controlled Deformable 3D Gaussians (HiCoDe), which achieves state-of-the-art performance with significantly reduced computational costs. Our key contribution is a hierarchical control strategy that effectively bridges the gap between sparse audio features and dense 3D Gaussian point clouds. Specifically, this strategy comprises two control levels: i) coarse-level control based on a 3D Morphable Model (3DMM) and ii) fine-level control using facial landmarks. Extensive experiments on the HDTF dataset and additional test sets demonstrate that our method outperforms existing approaches in visual quality, facial landmark accuracy, and audio-visual synchronization while being more computationally efficient in both training and inference.

</details>

### [A Survey on Audio-Driven Talking Face Generation](s2:54112d0b2c9786c7e32504c08190f784cd891a67.md)
**Xue Bai, Xiangzhen He, Mengdi Ma, Xiang Wang et al.** · 2025-04-11

<details>
<summary>Abstract</summary>

In recent years, advancements in deep learning have driven the development of audio-driven talking face generation. This technology has widespread applications in virtual avatars, intelligent assistants, film and television special effects, remote education, digital human live streaming, and more. Audio-driven talking face generation methods synthesize synchronized talking videos based on input speech signals, ensuring that the mouth movements, facial expressions, and head poses of virtual characters naturally align with the speech content. This paper provides an overview of the major research progress in this field and analyzes the advantages and limitations of different techniques. Additionally, it introduces evaluation metrics used to assess model performance in detail. Finally, the paper summarizes current challenges and potential future research directions.

</details>

### [VideoSPatS: Video SPatiotemporal Splines for Disentangled Occlusion, Appearance and Motion Modeling and Editing](2504.07146.md)
**Juan Luis Gonzalez Bello, Xu Yao, Alex Whelan, Kyle Olszewski et al.** · 2025-04-08

<details>
<summary>Abstract</summary>

We present an implicit video representation for occlusions, appearance, and motion disentanglement from monocular videos, which we call Video SPatiotemporal Splines (VideoSPatS). Unlike previous methods that map time and coordinates to deformation and canonical colors, our VideoSPatS maps input coordinates into Spatial and Color Spline deformation fields $D_s$ and $D_c$, which disentangle motion and appearance in videos. With spline-based parametrization, our method naturally generates temporally consistent flow and guarantees long-term temporal consistency, which is crucial for convincing video editing. Using multiple prediction branches, our VideoSPatS model also performs layer separation between the latent video and the selected occluder. By disentangling occlusions, appearance, and motion, our method enables better spatiotemporal modeling and editing of diverse videos, including in-the-wild talking head videos with challenging occlusions, shadows, and specularities while maintaining an appropriate canonical space for editing. We also present general video modeling results on the DAVIS and CoDeF datasets, as well as our own talking head video dataset collected from open-source web videos. Extensive ablations show the combination of $D_s$ and $D_c$ under neural splines can overcome motion and appearance ambiguities, paving the way for more advanced video editing models.

</details>

### [FluentLip: A Phonemes-Based Two-stage Approach for Audio-Driven Lip Synthesis with Optical Flow Consistency](2504.04427.md)
**Shiyan Liu, Rui Qu, Yan Jin** · 2025-04-06

<details>
<summary>Abstract</summary>

Generating consecutive images of lip movements that align with a given speech in audio-driven lip synthesis is a challenging task. While previous studies have made strides in synchronization and visual quality, lip intelligibility and video fluency remain persistent challenges. This work proposes FluentLip, a two-stage approach for audio-driven lip synthesis, incorporating three featured strategies. To improve lip synchronization and intelligibility, we integrate a phoneme extractor and encoder to generate a fusion of audio and phoneme information for multimodal learning. Additionally, we employ optical flow consistency loss to ensure natural transitions between image frames. Furthermore, we incorporate a diffusion chain during the training of Generative Adversarial Networks (GANs) to improve both stability and efficiency. We evaluate our proposed FluentLip through extensive experiments, comparing it with five state-of-the-art (SOTA) approaches across five metrics, including a proposed metric called Phoneme Error Rate (PER) that evaluates lip pose intelligibility and video fluency. The experimental results demonstrate that our FluentLip approach is highly competitive, achieving significant improvements in smoothness and naturalness. In particular, it outperforms these SOTA approaches by approximately $\textbf{16.3%}$ in Fréchet Inception Distance (FID) and $\textbf{35.2%}$ in PER.

</details>

### [DFNeRF: Disentangled Facial Neural Radiance Fields for Text-based Editing of Free-view Talking Head](s2:93e8d0e52b07d26494bf4518a74c5c8fcc0e84eb.md)
**Benwang Chen, Xiaoyu Li, Xuan Wang, Qi Zhang et al.** · 2025-04-06

<details>
<summary>Abstract</summary>

In this paper, we propose a text-based approach that can edit the speech content of a free-view talking head based on its transcript. The core of our method is to establish the relationship between phonemes and head attributes. To avoid discontinuities in head pose and facial expressions caused by editing mouth shape. We design the disentangled facial neural radiance fields (DFNeRF) to automatically disentangle these attributes controlled by the learned latent codes. Using the free-view talking head synthesized by DFNeRF as the base corpus, we could re-assemble the latent codes based on the new content using the phoneme search method to produce a seamless edited result. Our phoneme search method with a discriminator could find the best-matched phonemes in the sequence and ensure a smooth transition of mouth shape between the adjacent phonemes. Extensive experiments demonstrate the effectiveness of our method both qualitatively and quantitatively.

</details>

### [Gaussian-Face: Talking Head Generation with Hybrid Density via 3D Gaussian Splatting](s2:eea6b50f30ec571eafc0cbea6aa04173cfb51201.md)
**Guanwen Feng, Yilin Zhang, Yunan Li, Siyu Jin et al.** · 2025-04-06

<details>
<summary>Abstract</summary>

In recent years, audio-driven neural radiance field (NeRF)-based talking head generation techniques have achieved impressive results. However, these methods still have some limitations, such as unsynchronized lip movements and visual jitter. Recently, 3D Gaussian splatting has gradually replaced NeRF. Compared to NeRF, 3D Gaussian offers notable advantages, including higher efficiency and better reconstruction quality. Based on this, we propose Gaussian-Face, an audio-driven Gaussian-based facial avatar. With just a few minutes of monocular video and audio, a high-fidelity, driveable facial avatar can be reconstructed within hours. To achieve this, we first use FLAME to obtain the 3D representation of the face and then design a Lip Motion Translator to map audio to 3D lip representations. To model higher-quality facial details, we propose a hybrid density modeling method that balances rendering speed and quality, enabling our approach to render high-fidelity facial avatars at more than 160 FPS. Project page: https://peterfanfan.github.io/Gaussian-Face/

</details>

### [Subjective Fidelity Assessment of Audio- and Video-Driven Talking Head Generation Methods](s2:b78b96a87356fe953bd7095007ea90acdac1c2c6.md)
**Anthony Trioux, Yusong Gao, Jiarun Song, Wenjie Wu et al.** · 2025-04-06

<details>
<summary>Abstract</summary>

Audio- and Video-Driven Talking Head Generation methods have attracted considerable research interest due to recent advances in Artificial Intelligence Generated Content (AIGC) technologies. In such approaches, a single image is artificially animated by leveraging audio and/or motion features extracted from video sources. Despite notable progress, current performance assessments rely primarily on traditional objective metrics, often neglecting subjective evaluation aspects. To address this issue, we propose in this paper a subjective fidelity assessment of recent Audio- and/or Video-Driven Talking Head Generation methods. This study aims to assess how accurately and convincingly the generated video reproduces the visual and behavioral characteristics of a real human face, as well as how closely the video aligns with expected natural human expressions, movements, and/or audio synchronization. In order to provide a detailed assessment of the fidelity in the context of talking heads, our study focuses on six key criteria: Overall Fidelity, Gaze Fidelity, Audio-Video Sync Fidelity, Head Pose Fidelity, Expression Fidelity, and Overall Visual Quality. Experiments results reveal a nuanced picture of the fidelity in this context, where the performance varies significantly depending on the video content itself as well as how the animation is generated, highlighting the needs for further research. This research represents an initial step towards the evaluation of Audio- and Video-Driven generative image animation methods for Talking heads while offering insights for improving the accuracy and realism of those techniques. The dataset and corresponding results are available at https://github.com/a-trioux/Subjective-Fidelity-Assessment-Talking-Head.

</details>

### [Diffused Poses and Distilled Expressions for Controllable Audio-driven Talking Face Generation](s2:374f3581e81548fed6775f732af5840889d75475.md)
**Ziqi Zhou, Weize Quan, Zhaojin Lu, Dong-Ming Yan** · 2025-04-06

<details>
<summary>Abstract</summary>

Audio-driven portrait animation is an emerging field in multi-modal generation that aims to create lifelike talking face videos from audio input. While significant progress has been made, accurately modeling the relationship between audio signals and various facial motions, such as head poses and expressions, remains a challenge. Existing methods have primarily focused on generating lip-synchronized movements, often neglecting the intricate correlations between audio and other facial dynamics like head movements and eye blinks. More recent approaches have attempted to address these limitations by introducing latent disentanglement of facial motions, though this often comes at the cost of reduced flexibility in motion control. In this work, we propose a novel framework for audio-driven talking portrait animation that allows for precise and controllable generation of head poses and facial expressions. Our approach includes two key components: an audio-conditional diffusion model for generating prosody-aware head poses and a noise-conditional, lip-distilling transformer for predicting synchronized facial expressions. We further introduce an innovative animation model that uses these generated poses and expressions to produce highly realistic and controllable talking head videos. Extensive experiments demonstrate that our method not only achieves superior performance in generating natural and synchronized facial motions but also outperforms state-of-the-art techniques in the field.

</details>

### [VoiceCraft-Dub: Automated Video Dubbing with Neural Codec Language Models](2504.02386.md)
**Kim Sung-Bin, Jeongsoo Choi, Puyuan Peng, Joon Son Chung et al.** · 2025-04-03

<details>
<summary>Abstract</summary>

We present VoiceCraft-Dub, a novel approach for automated video dubbing that synthesizes high-quality speech from text and facial cues. This task has broad applications in filmmaking, multimedia creation, and assisting voice-impaired individuals. Building on the success of Neural Codec Language Models (NCLMs) for speech synthesis, our method extends their capabilities by incorporating video features, ensuring that synthesized speech is time-synchronized and expressively aligned with facial movements while preserving natural prosody. To inject visual cues, we design adapters to align facial features with the NCLM token space and introduce audio-visual fusion layers to merge audio-visual information within the NCLM framework. Additionally, we curate CelebV-Dub, a new dataset of expressive, real-world videos specifically designed for automated video dubbing. Extensive experiments show that our model achieves high-quality, intelligible, and natural speech synthesis with accurate lip synchronization, outperforming existing methods in human perception and performing favorably in objective evaluations. We also adapt VoiceCraft-Dub for the video-to-speech task, demonstrating its versatility for various applications.

</details>

### [Audio-visual Controlled Video Diffusion with Masked Selective State Spaces Modeling for Natural Talking Head Generation](2504.02542.md)
**Fa-Ting Hong, Zunnan Xu, Zixiang Zhou, Jun Zhou et al.** · 2025-04-03

<details>
<summary>Abstract</summary>

Talking head synthesis is vital for virtual avatars and human-computer interaction. However, most existing methods are typically limited to accepting control from a single primary modality, restricting their practical utility. To this end, we introduce \textbf{ACTalker}, an end-to-end video diffusion framework that supports both multi-signals control and single-signal control for talking head video generation. For multiple control, we design a parallel mamba structure with multiple branches, each utilizing a separate driving signal to control specific facial regions. A gate mechanism is applied across all branches, providing flexible control over video generation. To ensure natural coordination of the controlled video both temporally and spatially, we employ the mamba structure, which enables driving signals to manipulate feature tokens across both dimensions in each branch. Additionally, we introduce a mask-drop strategy that allows each driving signal to independently control its corresponding facial region within the mamba structure, preventing control conflicts. Experimental results demonstrate that our method produces natural-looking facial videos driven by diverse signals and that the mamba layer seamlessly integrates multiple driving modalities without conflict. The project website can be found at https://harlanhong.github.io/publications/actalker/index.html.

</details>

### [OmniTalker: One-shot Real-time Text-Driven Talking Audio-Video Generation With Multimodal Style Mimicking](2504.02433.md)
**Zhongjian Wang, Peng Zhang, Jinwei Qi, Guangyuan Wang et al.** · 2025-04-03

<details>
<summary>Abstract</summary>

Although significant progress has been made in audio-driven talking head generation, text-driven methods remain underexplored. In this work, we present OmniTalker, a unified framework that jointly generates synchronized talking audio-video content from input text while emulating the speaking and facial movement styles of the target identity, including speech characteristics, head motion, and facial dynamics. Our framework adopts a dual-branch diffusion transformer (DiT) architecture, with one branch dedicated to audio generation and the other to video synthesis. At the shallow layers, cross-modal fusion modules are introduced to integrate information between the two modalities. In deeper layers, each modality is processed independently, with the generated audio decoded by a vocoder and the video rendered using a GAN-based high-quality visual renderer. Leveraging the in-context learning capability of DiT through a masked-infilling strategy, our model can simultaneously capture both audio and visual styles without requiring explicit style extraction modules. Thanks to the efficiency of the DiT backbone and the optimized visual renderer, OmniTalker achieves real-time inference at 25 FPS. To the best of our knowledge, OmniTalker is the first one-shot framework capable of jointly modeling speech and facial styles in real time. Extensive experiments demonstrate its superiority over existing methods in terms of generation quality, particularly in preserving style consistency and ensuring precise audio-video synchronization, all while maintaining efficient inference.

</details>

### [TransLip: AI-Driven Video Translation and Synchronization](s2:505f78f7846f2feae20a665472e5820e15ebda73.md)
**Adarsh Muralidharan, Minsa Aji, Rohan Jacob Jacob, Shasna Cherukat et al.** · 2025-04-03

<details>
<summary>Abstract</summary>

The increasing need for region-specific digital content has spurred progress in technologies like video translation and lip synchronization. This work introduces an innovative system for converting video and audio from English into Malayalam, a regional language while achieving precise lip synchronization. The process involves extracting audio and converting speech to text, translating the text and generating speech in the target language. The synchronized audio is then aligned with the speaker’s lip movements using the Generative Adversarial Network(GAN) powered Wav2Lip model. The result is a cohesive video where the translated audio and lip movement are in harmony, delivering a lifelike and engaging experience for viewers. This approach offers substantial benefits in sectors like entertainment, education, and media localization, broadening access to content while upholding the integrity of the original material.

</details>

### [Detecting Lip-Syncing Deepfakes: Vision Temporal Transformer for Analyzing Mouth Inconsistencies](2504.01470.md)
**Soumyya Kanti Datta, Shan Jia, Siwei Lyu** · 2025-04-02

<details>
<summary>Abstract</summary>

Deepfakes are AI-generated media in which the original content is digitally altered to create convincing but manipulated images, videos, or audio. Among the various types of deepfakes, lip-syncing deepfakes are one of the most challenging deepfakes to detect. In these videos, a person's lip movements are synthesized to match altered or entirely new audio using AI models. Therefore, unlike other types of deepfakes, the artifacts in lip-syncing deepfakes are confined to the mouth region, making them more subtle and, thus harder to discern. In this paper, we propose LIPINC-V2, a novel detection framework that leverages a combination of vision temporal transformer with multihead cross-attention to detect lip-syncing deepfakes by identifying spatiotemporal inconsistencies in the mouth region. These inconsistencies appear across adjacent frames and persist throughout the video. Our model can successfully capture both short-term and long-term variations in mouth movement, enhancing its ability to detect these inconsistencies. Additionally, we created a new lip-syncing deepfake dataset, LipSyncTIMIT, which was generated using five state-of-the-art lip-syncing models to simulate real-world scenarios. Extensive experiments on our proposed LipSyncTIMIT dataset and two other benchmark deepfake datasets demonstrate that our model achieves state-of-the-art performance. The code and the dataset are available at https://github.com/skrantidatta/LIPINC-V2 .

</details>

### [Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](2503.22225.md)
**Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian et al.** · 2025-03-28

<details>
<summary>Abstract</summary>

Pre-trained conditional diffusion models have demonstrated remarkable potential in image editing. However, they often face challenges with temporal consistency, particularly in the talking head domain, where continuous changes in facial expressions intensify the level of difficulty. These issues stem from the independent editing of individual images and the inherent loss of temporal continuity during the editing process. In this paper, we introduce Follow Your Motion (FYM), a generic framework for maintaining temporal consistency in portrait editing. Specifically, given portrait images rendered by a pre-trained 3D Gaussian Splatting model, we first develop a diffusion model that intuitively and inherently learns motion trajectory changes at different scales and pixel coordinates, from the first frame to each subsequent frame. This approach ensures that temporally inconsistent edited avatars inherit the motion information from the rendered avatars. Secondly, to maintain fine-grained expression temporal consistency in talking head editing, we propose a dynamic re-weighted attention mechanism. This mechanism assigns higher weight coefficients to landmark points in space and dynamically updates these weights based on landmark loss, achieving more consistent and refined facial expressions. Extensive experiments demonstrate that our method outperforms existing approaches in terms of temporal consistency and can be used to optimize and compensate for temporally inconsistent outputs in a range of applications, such as text-driven editing, relighting, and various other applications.

</details>

### [ChatAnyone: Stylized Real-time Portrait Video Generation with Hierarchical Motion Diffusion Model](2503.21144.md)
**Jinwei Qi, Chaonan Ji, Sheng Xu, Peng Zhang et al.** · 2025-03-27

<details>
<summary>Abstract</summary>

Real-time interactive video-chat portraits have been increasingly recognized as the future trend, particularly due to the remarkable progress made in text and voice chat technologies. However, existing methods primarily focus on real-time generation of head movements, but struggle to produce synchronized body motions that match these head actions. Additionally, achieving fine-grained control over the speaking style and nuances of facial expressions remains a challenge. To address these limitations, we introduce a novel framework for stylized real-time portrait video generation, enabling expressive and flexible video chat that extends from talking head to upper-body interaction. Our approach consists of the following two stages. The first stage involves efficient hierarchical motion diffusion models, that take both explicit and implicit motion representations into account based on audio inputs, which can generate a diverse range of facial expressions with stylistic control and synchronization between head and body movements. The second stage aims to generate portrait video featuring upper-body movements, including hand gestures. We inject explicit hand control signals into the generator to produce more detailed hand movements, and further perform face refinement to enhance the overall realism and expressiveness of the portrait video. Additionally, our approach supports efficient and continuous generation of upper-body portrait video in maximum 512 * 768 resolution at up to 30fps on 4090 GPU, supporting interactive video-chat in real-time. Experimental results demonstrate the capability of our approach to produce portrait videos with rich expressiveness and natural upper-body movements.

</details>

### [Dual Audio-Centric Modality Coupling for Talking Head Generation](2503.22728.md)
**Ao Fu, Ziqi Ni, Yi Zhou** · 2025-03-26

<details>
<summary>Abstract</summary>

The generation of audio-driven talking head videos is a key challenge in computer vision and graphics, with applications in virtual avatars and digital media. Traditional approaches often struggle with capturing the complex interaction between audio and facial dynamics, leading to lip synchronization and visual quality issues. In this paper, we propose a novel NeRF-based framework, Dual Audio-Centric Modality Coupling (DAMC), which effectively integrates content and dynamic features from audio inputs. By leveraging a dual encoder structure, DAMC captures semantic content through the Content-Aware Encoder and ensures precise visual synchronization through the Dynamic-Sync Encoder. These features are fused using a Cross-Synchronized Fusion Module (CSFM), enhancing content representation and lip synchronization. Extensive experiments show that our method outperforms existing state-of-the-art approaches in key metrics such as lip synchronization accuracy and image quality, demonstrating robust generalization across various audio inputs, including synthetic speech from text-to-speech (TTS) systems. Our results provide a promising solution for high-quality, audio-driven talking head generation and present a scalable approach for creating realistic talking heads.

</details>

### [MVPortrait: Text-Guided Motion and Emotion Control for Multi-view Vivid Portrait Animation](2503.19383.md)
**Yukang Lin, Hokit Fung, Jianjin Xu, Zeping Ren et al.** · 2025-03-25

<details>
<summary>Abstract</summary>

Recent portrait animation methods have made significant strides in generating realistic lip synchronization. However, they often lack explicit control over head movements and facial expressions, and cannot produce videos from multiple viewpoints, resulting in less controllable and expressive animations. Moreover, text-guided portrait animation remains underexplored, despite its user-friendly nature. We present a novel two-stage text-guided framework, MVPortrait (Multi-view Vivid Portrait), to generate expressive multi-view portrait animations that faithfully capture the described motion and emotion. MVPortrait is the first to introduce FLAME as an intermediate representation, effectively embedding facial movements, expressions, and view transformations within its parameter space. In the first stage, we separately train the FLAME motion and emotion diffusion models based on text input. In the second stage, we train a multi-view video generation model conditioned on a reference portrait image and multi-view FLAME rendering sequences from the first stage. Experimental results exhibit that MVPortrait outperforms existing methods in terms of motion and emotion control, as well as view consistency. Furthermore, by leveraging FLAME as a bridge, MVPortrait becomes the first controllable portrait animation framework that is compatible with text, speech, and video as driving signals.

</details>

### [EmoHead: Emotional Talking Head via Manipulating Semantic Expression Parameters](2503.19416.md)
**Xuli Shen, Hua Cai, Dingding Yu, Weilin Shen et al.** · 2025-03-25

<details>
<summary>Abstract</summary>

Generating emotion-specific talking head videos from audio input is an important and complex challenge for human-machine interaction. However, emotion is highly abstract concept with ambiguous boundaries, and it necessitates disentangled expression parameters to generate emotionally expressive talking head videos. In this work, we present EmoHead to synthesize talking head videos via semantic expression parameters. To predict expression parameter for arbitrary audio input, we apply an audio-expression module that can be specified by an emotion tag. This module aims to enhance correlation from audio input across various emotions. Furthermore, we leverage pre-trained hyperplane to refine facial movements by probing along the vertical direction. Finally, the refined expression parameters regularize neural radiance fields and facilitate the emotion-consistent generation of talking head videos. Experimental results demonstrate that semantic expression parameters lead to better reconstruction quality and controllability.

</details>

### [DisentTalk: Cross-lingual Talking Face Generation via Semantic Disentangled Diffusion Model](2503.19001.md)
**Kangwei Liu, Junwu Liu, Yun Cao, Jinlin Guo et al.** · 2025-03-24

<details>
<summary>Abstract</summary>

Recent advances in talking face generation have significantly improved facial animation synthesis. However, existing approaches face fundamental limitations: 3DMM-based methods maintain temporal consistency but lack fine-grained regional control, while Stable Diffusion-based methods enable spatial manipulation but suffer from temporal inconsistencies. The integration of these approaches is hindered by incompatible control mechanisms and semantic entanglement of facial representations. This paper presents DisentTalk, introducing a data-driven semantic disentanglement framework that decomposes 3DMM expression parameters into meaningful subspaces for fine-grained facial control. Building upon this disentangled representation, we develop a hierarchical latent diffusion architecture that operates in 3DMM parameter space, integrating region-aware attention mechanisms to ensure both spatial precision and temporal coherence. To address the scarcity of high-quality Chinese training data, we introduce CHDTF, a Chinese high-definition talking face dataset. Extensive experiments show superior performance over existing methods across multiple metrics, including lip synchronization, expression quality, and temporal consistency. Project Page: https://kangweiiliu.github.io/DisentTalk.

</details>

### [Teller: Real-Time Streaming Audio-Driven Portrait Animation with Autoregressive Motion Generation](2503.18429.md)
**Dingcheng Zhen, Shunshun Yin, Shiyang Qin, Hou Yi et al.** · 2025-03-24

<details>
<summary>Abstract</summary>

In this work, we introduce the first autoregressive framework for real-time, audio-driven portrait animation, a.k.a, talking head. Beyond the challenge of lengthy animation times, a critical challenge in realistic talking head generation lies in preserving the natural movement of diverse body parts. To this end, we propose Teller, the first streaming audio-driven protrait animation framework with autoregressive motion generation. Specifically, Teller first decomposes facial and body detail animation into two components: Facial Motion Latent Generation (FMLG) based on an autoregressive transfromer, and movement authenticity refinement using a Efficient Temporal Module (ETM).Concretely, FMLG employs a Residual VQ model to map the facial motion latent from the implicit keypoint-based model into discrete motion tokens, which are then temporally sliced with audio embeddings. This enables the AR tranformer to learn real-time, stream-based mappings from audio to motion. Furthermore, Teller incorporate ETM to capture finer motion details. This module ensures the physical consistency of body parts and accessories, such as neck muscles and earrings, improving the realism of these movements. Teller is designed to be efficient, surpassing the inference speed of diffusion-based models (Hallo 20.93s vs. Teller 0.92s for one second video generation), and achieves a real-time streaming performance of up to 25 FPS. Extensive experiments demonstrate that our method outperforms recent audio-driven portrait animation models, especially in small movements, as validated by human evaluations with a significant margin in quality and realism.

</details>

### [DiffusionTalker: Efficient and Compact Speech-Driven 3D Talking Head via Personalizer-Guided Distillation](2503.18159.md)
**Peng Chen, Xiaobao Wei, Ming Lu, Hui Chen et al.** · 2025-03-23

<details>
<summary>Abstract</summary>

Real-time speech-driven 3D facial animation has been attractive in academia and industry. Traditional methods mainly focus on learning a deterministic mapping from speech to animation. Recent approaches start to consider the nondeterministic fact of speech-driven 3D face animation and employ the diffusion model for the task. Existing diffusion-based methods can improve the diversity of facial animation. However, personalized speaking styles conveying accurate lip language is still lacking, besides, efficiency and compactness still need to be improved. In this work, we propose DiffusionTalker to address the above limitations via personalizer-guided distillation. In terms of personalization, we introduce a contrastive personalizer that learns identity and emotion embeddings to capture speaking styles from audio. We further propose a personalizer enhancer during distillation to enhance the influence of embeddings on facial animation. For efficiency, we use iterative distillation to reduce the steps required for animation generation and achieve more than 8x speedup in inference. To achieve compactness, we distill the large teacher model into a smaller student model, reducing our model's storage by 86.4\% while minimizing performance loss. After distillation, users can derive their identity and emotion embeddings from audio to quickly create personalized animations that reflect specific speaking styles. Extensive experiments are conducted to demonstrate that our method outperforms state-of-the-art methods. The code will be released at: https://github.com/ChenVoid/DiffusionTalker.

</details>

### [Unlock Pose Diversity: Accurate and Efficient Implicit Keypoint-based Spatiotemporal Diffusion for Audio-driven Talking Portrait](2503.12963.md)
**Chaolong Yang, Kai Yao, Yuyao Yan, Chenru Jiang et al.** · 2025-03-17

<details>
<summary>Abstract</summary>

Audio-driven single-image talking portrait generation plays a crucial role in virtual reality, digital human creation, and filmmaking. Existing approaches are generally categorized into keypoint-based and image-based methods. Keypoint-based methods effectively preserve character identity but struggle to capture fine facial details due to the fixed points limitation of the 3D Morphable Model. Moreover, traditional generative networks face challenges in establishing causality between audio and keypoints on limited datasets, resulting in low pose diversity. In contrast, image-based approaches produce high-quality portraits with diverse details using the diffusion network but incur identity distortion and expensive computational costs. In this work, we propose KDTalker, the first framework to combine unsupervised implicit 3D keypoint with a spatiotemporal diffusion model. Leveraging unsupervised implicit 3D keypoints, KDTalker adapts facial information densities, allowing the diffusion process to model diverse head poses and capture fine facial details flexibly. The custom-designed spatiotemporal attention mechanism ensures accurate lip synchronization, producing temporally consistent, high-quality animations while enhancing computational efficiency. Experimental results demonstrate that KDTalker achieves state-of-the-art performance regarding lip synchronization accuracy, head pose diversity, and execution efficiency.Our codes are available at https://github.com/chaolongy/KDTalker.

</details>

### [SyncDiff: Diffusion-based Talking Head Synthesis with Bottlenecked Temporal Visual Prior for Improved Synchronization](2503.13371.md)
**Xulin Fan, Heting Gao, Ziyi Chen, Peng Chang et al.** · 2025-03-17

<details>
<summary>Abstract</summary>

Talking head synthesis, also known as speech-to-lip synthesis, reconstructs the facial motions that align with the given audio tracks. The synthesized videos are evaluated on mainly two aspects, lip-speech synchronization and image fidelity. Recent studies demonstrate that GAN-based and diffusion-based models achieve state-of-the-art (SOTA) performance on this task, with diffusion-based models achieving superior image fidelity but experiencing lower synchronization compared to their GAN-based counterparts. To this end, we propose SyncDiff, a simple yet effective approach to improve diffusion-based models using a temporal pose frame with information bottleneck and facial-informative audio features extracted from AVHuBERT, as conditioning input into the diffusion process. We evaluate SyncDiff on two canonical talking head datasets, LRS2 and LRS3 for direct comparison with other SOTA models. Experiments on LRS2/LRS3 datasets show that SyncDiff achieves a synchronization score 27.7%/62.3% relatively higher than previous diffusion-based methods, while preserving their high-fidelity characteristics.

</details>

### [Cafe-Talk: Generating 3D Talking Face Animation with Multimodal Coarse- and Fine-grained Control](2503.14517.md)
**Hejia Chen, Haoxian Zhang, Shoulong Zhang, Xiaoqiang Liu et al.** · 2025-03-14

<details>
<summary>Abstract</summary>

Speech-driven 3D talking face method should offer both accurate lip synchronization and controllable expressions. Previous methods solely adopt discrete emotion labels to globally control expressions throughout sequences while limiting flexible fine-grained facial control within the spatiotemporal domain. We propose a diffusion-transformer-based 3D talking face generation model, Cafe-Talk, which simultaneously incorporates coarse- and fine-grained multimodal control conditions. Nevertheless, the entanglement of multiple conditions challenges achieving satisfying performance. To disentangle speech audio and fine-grained conditions, we employ a two-stage training pipeline. Specifically, Cafe-Talk is initially trained using only speech audio and coarse-grained conditions. Then, a proposed fine-grained control adapter gradually adds fine-grained instructions represented by action units (AUs), preventing unfavorable speech-lip synchronization. To disentangle coarse- and fine-grained conditions, we design a swap-label training mechanism, which enables the dominance of the fine-grained conditions. We also devise a mask-based CFG technique to regulate the occurrence and intensity of fine-grained control. In addition, a text-based detector is introduced with text-AU alignment to enable natural language user input and further support multimodal control. Extensive experimental results prove that Cafe-Talk achieves state-of-the-art lip synchronization and expressiveness performance and receives wide acceptance in fine-grained control in user studies. Project page: https://harryxd2018.github.io/cafe-talk/

</details>

### [EmoDiffusion: Enhancing Emotional 3D Facial Animation with Latent Diffusion Models](2503.11028.md)
**Yixuan Zhang, Qing Chang, Yuxi Wang, Guang Chen et al.** · 2025-03-14

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation seeks to produce lifelike facial expressions that are synchronized with the speech content and its emotional nuances, finding applications in various multimedia fields. However, previous methods often overlook emotional facial expressions or fail to disentangle them effectively from the speech content. To address these challenges, we present EmoDiffusion, a novel approach that disentangles different emotions in speech to generate rich 3D emotional facial expressions. Specifically, our method employs two Variational Autoencoders (VAEs) to separately generate the upper face region and mouth region, thereby learning a more refined representation of the facial sequence. Unlike traditional methods that use diffusion models to connect facial expression sequences with audio inputs, we perform the diffusion process in the latent space. Furthermore, we introduce an Emotion Adapter to evaluate upper face movements accurately. Given the paucity of 3D emotional talking face data in the animation industry, we capture facial expressions under the guidance of animation experts using LiveLinkFace on an iPhone. This effort results in the creation of an innovative 3D blendshape emotional talking face dataset (3D-BEF) used to train our network. Extensive experiments and perceptual evaluations validate the effectiveness of our approach, confirming its superiority in generating realistic and emotionally rich facial animations.

</details>

### [Bidirectional Learned Facial Animation Codec for Low Bitrate Talking Head Videos](2503.09787.md)
**Riku Takahashi, Ryugo Morita, Fuma Kimishima, Kosuke Iwama et al.** · 2025-03-12

<details>
<summary>Abstract</summary>

Existing deep facial animation coding techniques efficiently compress talking head videos by applying deep generative models. Instead of compressing the entire video sequence, these methods focus on compressing only the keyframe and the keypoints of non-keyframes (target frames). The target frames are then reconstructed by utilizing a single keyframe, and the keypoints of the target frame. Although these unidirectional methods can reduce the bitrate, they rely on a single keyframe and often struggle to capture large head movements accurately, resulting in distortions in the facial region. In this paper, we propose a novel bidirectional learned animation codec that generates natural facial videos using past and future keyframes. First, in the Bidirectional Reference-Guided Auxiliary Stream Enhancement (BRG-ASE) process, we introduce a compact auxiliary stream for non-keyframes, which is enhanced by adaptively selecting one of two keyframes (past and future). This stream improves video quality with a slight increase in bitrate. Then, in the Bidirectional Reference-Guided Video Reconstruction (BRG-VRec) process, we animate the adaptively selected keyframe and reconstruct the target frame using both the animated keyframe and the auxiliary frame. Extensive experiments demonstrate a 55% bitrate reduction compared to the latest animation based video codec, and a 35% bitrate reduction compared to the latest video coding standard, Versatile Video Coding (VVC) on a talking head video dataset. It showcases the efficiency of our approach in improving video quality while simultaneously decreasing bitrate.

</details>

### [Versatile Multimodal Controls for Expressive Talking Human Animation](2503.08714.md)
**Zheng Qin, Ruobing Zheng, Yabing Wang, Tianqi Li et al.** · 2025-03-10

<details>
<summary>Abstract</summary>

In filmmaking, directors typically allow actors to perform freely based on the script before providing specific guidance on how to present key actions. AI-generated content faces similar requirements, where users not only need automatic generation of lip synchronization and basic gestures from audio input but also desire semantically accurate and expressive body movement that can be ``directly guided'' through text descriptions. Therefore, we present VersaAnimator, a versatile framework that synthesizes expressive talking human videos from arbitrary portrait images. Specifically, we design a motion generator that produces basic rhythmic movements from audio input and supports text-prompt control for specific actions. The generated whole-body 3D motion tokens can animate portraits of various scales, producing talking heads, half-body gestures and even leg movements for whole-body images. Besides, we introduce a multi-modal controlled video diffusion that generates photorealistic videos, where speech signals govern lip synchronization, facial expressions, and head motions while body movements are guided by the 2D poses. Furthermore, we introduce a token2pose translator to smoothly map 3D motion tokens to 2D pose sequences. This design mitigates the stiffness resulting from direct 3D to 2D conversion and enhances the details of the generated body movements. Extensive experiments shows that VersaAnimator synthesizes lip-synced and identity-preserving videos while generating expressive and semantically meaningful whole-body motions.

</details>

### [Removing Averaging: Personalized Lip-Sync Driven Characters Based on Identity Adapter](2503.06397.md)
**Yanyu Zhu, Lichen Bai, Jintao Xu, Hai-tao Zheng** · 2025-03-09

<details>
<summary>Abstract</summary>

Recent advances in diffusion-based lip-syncing generative models have demonstrated their ability to produce highly synchronized talking face videos for visual dubbing. Although these models excel at lip synchronization, they often struggle to maintain fine-grained control over facial details in generated images. In this work, we identify "lip averaging" phenomenon where the model fails to preserve subtle facial details when dubbing unseen in-the-wild videos. This issue arises because the commonly used UNet backbone primarily integrates audio features into visual representations in the latent space via cross-attention mechanisms and multi-scale fusion, but it struggles to retain fine-grained lip details in the generated faces. To address this issue, we propose UnAvgLip, which extracts identity embeddings from reference videos to generate highly faithful facial sequences while maintaining accurate lip synchronization. Specifically, our method comprises two primary components: (1) an Identity Perceiver module that encodes facial embeddings to align with conditioned audio features; and (2) an ID-CrossAttn module that injects facial embeddings into the generation process, enhancing model's capability of identity retention. Extensive experiments demonstrate that, at a modest training and inference cost, UnAvgLip effectively mitigates the "averaging" phenomenon in lip inpainting, significantly preserving unique facial characteristics while maintaining precise lip synchronization. Compared with the original approach, our method demonstrates significant improvements of 5% on the identity consistency metric and 2% on the SSIM metric across two benchmark datasets (HDTF and LRW).

</details>

### [MagicInfinite: Generating Infinite Talking Videos with Your Words and Voice](2503.05978.md)
**Hongwei Yi, Tian Ye, Shitong Shao, Xuancheng Yang et al.** · 2025-03-07

<details>
<summary>Abstract</summary>

We present MagicInfinite, a novel diffusion Transformer (DiT) framework that overcomes traditional portrait animation limitations, delivering high-fidelity results across diverse character types-realistic humans, full-body figures, and stylized anime characters. It supports varied facial poses, including back-facing views, and animates single or multiple characters with input masks for precise speaker designation in multi-character scenes. Our approach tackles key challenges with three innovations: (1) 3D full-attention mechanisms with a sliding window denoising strategy, enabling infinite video generation with temporal coherence and visual quality across diverse character styles; (2) a two-stage curriculum learning scheme, integrating audio for lip sync, text for expressive dynamics, and reference images for identity preservation, enabling flexible multi-modal control over long sequences; and (3) region-specific masks with adaptive loss functions to balance global textual control and local audio guidance, supporting speaker-specific animations. Efficiency is enhanced via our innovative unified step and cfg distillation techniques, achieving a 20x inference speed boost over the basemodel: generating a 10 second 540x540p video in 10 seconds or 720x720p in 30 seconds on 8 H100 GPUs, without quality loss. Evaluations on our new benchmark demonstrate MagicInfinite's superiority in audio-lip synchronization, identity preservation, and motion naturalness across diverse scenarios. It is publicly available at https://www.hedra.com/, with examples at https://magicinfinite.github.io/.

</details>

### [FREAK: Frequency-modulated High-fidelity and Real-time Audio-driven Talking Portrait Synthesis](2503.04067.md)
**Ziqi Ni, Ao Fu, Yi Zhou** · 2025-03-06

<details>
<summary>Abstract</summary>

Achieving high-fidelity lip-speech synchronization in audio-driven talking portrait synthesis remains challenging. While multi-stage pipelines or diffusion models yield high-quality results, they suffer from high computational costs. Some approaches perform well on specific individuals with low resources, yet still exhibit mismatched lip movements. The aforementioned methods are modeled in the pixel domain. We observed that there are noticeable discrepancies in the frequency domain between the synthesized talking videos and natural videos. Currently, no research on talking portrait synthesis has considered this aspect. To address this, we propose a FREquency-modulated, high-fidelity, and real-time Audio-driven talKing portrait synthesis framework, named FREAK, which models talking portraits from the frequency domain perspective, enhancing the fidelity and naturalness of the synthesized portraits. FREAK introduces two novel frequency-based modules: 1) the Visual Encoding Frequency Modulator (VEFM) to couple multi-scale visual features in the frequency domain, better preserving visual frequency information and reducing the gap in the frequency spectrum between synthesized and natural frames. and 2) the Audio Visual Frequency Modulator (AVFM) to help the model learn the talking pattern in the frequency domain and improve audio-visual synchronization. Additionally, we optimize the model in both pixel domain and frequency domain jointly. Furthermore, FREAK supports seamless switching between one-shot and video dubbing settings, offering enhanced flexibility. Due to its superior performance, it can simultaneously support high-resolution video results and real-time inference. Extensive experiments demonstrate that our method synthesizes high-fidelity talking portraits with detailed facial textures and precise lip synchronization in real-time, outperforming state-of-the-art methods.

</details>

### [Realistic Lip-Sync Generation from Text for Multimodal Applications](s2:ea0ae8bc51add7570999bf6f8504cc9718349785.md)
**Doradla Kaushik, Konduru Praveen Karthik, Taduvai Satvik Gupta, Susmitha Vekkot** · 2025-03-06

<details>
<summary>Abstract</summary>

This paper explores an advanced framework for text-to-lip-sync generation, leveraging the integration of the Massively Multilingual Speech Text-to-Speech (MMS TTS) and Wav2Lip models. The MMS TTS model transforms text into natural, high-quality multilingual speech while preserving speaker identity, and the Wav2Lip model ensures accurate synchronization of lip movements with the generated audio. Using the GRID dataset for training, the Wav2Lip model achieves remarkable performance in audiovisual alignment, attaining high lip-sync confidence metrics with an LSE-C score of 6.701 and an LSE-D score of 7.362. The proposed solution has broad applicability in virtual assistants, media production, digital education, and accessibility, setting a new standard for immersive and realistic audiovisual experiences.

</details>

### [A Unified Deep Learning Framework for Lip Reading and Deep Fake Audio Classification](s2:384047c6c103814109d686cdaebe629b11cfd61c.md)
**Vijay A. Sangolgi, Mithun B. Patil, Omkar Nagnath Bhosale, Anurag Vivek Deshmukhe et al.** · 2025-03-06

<details>
<summary>Abstract</summary>

This study proposes a multimodal framework designed to enhance deepfake detection by integrating visual lip-reading analysis and audio signal processing for real-time applications. Leveraging LipNet—a deep learning model pre-trained on the GRID dataset—the system employs 3D convolutional neural networks (CNNs) combined with bidirectional long short-term memory (Bi-LSTM) layers to interpret lip movements and decode spoken words from visual inputs. Simultaneously, audio analysis modules evaluate acoustic features to detect synthetic or manipulated speech. By independently training these components and combining their outputs, the framework identifies inconsistencies between visual and auditory modalities, such as mismatched lip-audio synchronization or unnatural speech patterns. Experimental results demonstrate robust performance in both word-level lip-reading accuracy and deepfake detection reliability, achieving high precision in flagging fraudulent content. The system’s effectiveness in detecting audiovisual anomalies positions it as a practical tool for digital forensics and security applications, with potential to foster trust in digital media. Future work will expand the model’s adaptability to diverse datasets, including multilingual contexts, and refine its integration into real-world media authentication and accessibility tools.

</details>

### [KeyFace: Expressive Audio-Driven Facial Animation for Long Sequences via KeyFrame Interpolation](2503.01715.md)
**Antoni Bigata, Michał Stypułkowski, Rodrigo Mira, Stella Bounareli et al.** · 2025-03-03

<details>
<summary>Abstract</summary>

Current audio-driven facial animation methods achieve impressive results for short videos but suffer from error accumulation and identity drift when extended to longer durations. Existing methods attempt to mitigate this through external spatial control, increasing long-term consistency but compromising the naturalness of motion. We propose KeyFace, a novel two-stage diffusion-based framework, to address these issues. In the first stage, keyframes are generated at a low frame rate, conditioned on audio input and an identity frame, to capture essential facial expressions and movements over extended periods of time. In the second stage, an interpolation model fills in the gaps between keyframes, ensuring smooth transitions and temporal coherence. To further enhance realism, we incorporate continuous emotion representations and handle a wide range of non-speech vocalizations (NSVs), such as laughter and sighs. We also introduce two new evaluation metrics for assessing lip synchronization and NSV generation. Experimental results show that KeyFace outperforms state-of-the-art methods in generating natural, coherent facial animations over extended durations, successfully encompassing NSVs and continuous emotions.

</details>

### [Enhancing Video Conferencing Experience through Speech Activity Detection and Lip Synchronization with Deep Learning Models](s2:502b96013aaa764b105468a5b31fd3e63ab40bd2.md)
**Weikun Lin** · 2025-03-03

<details>
<summary>Abstract</summary>

As video conferencing becomes increasingly integral to modern communication, the need for high-quality synchronization between speech and visual elements is paramount. Speech Activity Detection (VAD) and lip synchronization technologies play crucial roles in ensuring accurate, real-time communication by distinguishing speech signals from noise and aligning lip movements with audio. This paper proposes a novel multimodal fusion approach based on deep learning models that significantly improves the accuracy of speech activity detection and the real-time performance of lip synchronization. Using open datasets such as AVSpeech and LRW, this study showcases the effectiveness of the proposed models in various real-world scenarios, such as multi-party conferences, noisy environments, and cross-lingual settings. Experimental results demonstrate that the LSTM-based VAD model achieves an accuracy of 92%, outperforming traditional methods, while the lip synchronization module ensures seamless audio-visual alignment with minimal delay.

</details>

### [Two-Stream Spatial-Temporal Transformer Framework for Person Identification via Natural Conversational Keypoints](2502.20803.md)
**Masoumeh Chapariniya, Hossein Ranjbar, Teodora Vukovic, Sarah Ebling et al.** · 2025-02-28

<details>
<summary>Abstract</summary>

In the age of AI-driven generative technologies, traditional biometric recognition systems face unprecedented challenges, particularly from sophisticated deepfake and face reenactment techniques. In this study, we propose a Two-Stream Spatial-Temporal Transformer Framework for person identification using upper body keypoints visible during online conversations, which we term conversational keypoints. Our framework processes both spatial relationships between keypoints and their temporal evolution through two specialized branches: a Spatial Transformer (STR) that learns distinctive structural patterns in keypoint configurations, and a Temporal Transformer (TTR) that captures sequential motion patterns. Using the state-of-the-art Sapiens pose estimator, we extract 133 keypoints (based on COCO-WholeBody format) representing facial features, head pose, and hand positions. The framework was evaluated on a dataset of 114 individuals engaged in natural conversations, achieving recognition accuracies of 80.12% for the spatial stream, 63.61% for the temporal stream. We then explored two fusion strategies: a shared loss function approach achieving 82.22% accuracy, and a feature-level fusion method that concatenates feature maps from both streams, significantly improving performance to 94.86%. By jointly modeling both static anatomical relationships and dynamic movement patterns, our approach learns comprehensive identity signatures that are more robust to spoofing than traditional appearance-based methods.

</details>

### [ARTalk: Speech-Driven 3D Head Animation via Autoregressive Model](2502.20323.md)
**Xuangeng Chu, Nabarun Goswami, Ziteng Cui, Hanqin Wang et al.** · 2025-02-27

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation aims to generate realistic lip movements and facial expressions for 3D head models from arbitrary audio clips. Although existing diffusion-based methods are capable of producing natural motions, their slow generation speed limits their application potential. In this paper, we introduce a novel autoregressive model that achieves real-time generation of highly synchronized lip movements and realistic head poses and eye blinks by learning a mapping from speech to a multi-scale motion codebook. Furthermore, our model can adapt to unseen speaking styles, enabling the creation of 3D talking avatars with unique personal styles beyond the identities seen during training. Extensive evaluations and user studies demonstrate that our method outperforms existing approaches in lip synchronization accuracy and perceived quality.

</details>

### [Talking Head Anime 4: Distillation for Real-Time Performance](s2:a332eebf8c0df968876be9263ee0925a0811b27e.md)
**Pramook Khungurn** · 2025-02-26

<details>
<summary>Abstract</summary>

We study the problem of creating a character model that can be controlled in real time from a single image of an anime character. A solution would greatly reduce the cost of creating avatars, computer games, and other interactive applications. Talking Head Anime 3 (THA3) is an open source project that attempts to directly address the problem [40]. It takes as input (1) an image of an anime character's upper body and (2) a 45-dimensional pose vector and outputs a new image of the same character taking the specified pose. The range of possible movements is expressive enough for personal avatars and certain types of game characters. THA3's main limitation is its speed. It can achieve interactive frame rates (~ 20 FPS) only if it is run on a very powerful GPU (Nvidia Titan RTX or better). Based on the insight that avatars and game characters do not need to change their appearance every so often, we propose a technique to distill the system into a small student neural network ( 2 MB) specific to a particular character. The student model can generate $512 \times 512$ animation frames in real time (> 30 FPS) using consumer gaming GPUs while preserving the image quality of the teacher model. For the first time, our technique makes the whole system practical for real-time applications.

</details>

### [Deep Face Gen: Speech-Driven Face Image Synthesis](s2:e08961b0f03e5d184e052253bec3771e0c7c41eb.md)
**P. K. Thai, P. Manisha, L. Reddy, M. Reddy** · 2025-02-25

<details>
<summary>Abstract</summary>

A framework based on Generative Adversarial Networks (GANs) is proposed to synthesize facial images from audio inputs. The system aims to automatically translate large volumes of audio into understandable facial images without human intervention. By using a GAN architecture, the model generates image features from audio waveforms to reconstruct facial images. It is trained on a dataset of labeled examples, producing facial images corresponding to the identities of the speakers. The method achieves an accuracy of 96.88% for ungrouped data and 93.91% for grouped data. This approach demonstrates its capability to generate accurate facial representations from audio, offering an automated solution for converting speech into intelligible visual data. Keywords: Generative Adversarial Networks, facial image synthesis, audio-to-image, speech-to-visual, automated reconstruction.

</details>

### [Dimitra: Audio-driven Diffusion model for Expressive Talking Head Generation](2502.17198.md)
**Baptiste Chopin, Tashvik Dhamija, Pranav Balaji, Yaohui Wang et al.** · 2025-02-24

<details>
<summary>Abstract</summary>

We propose Dimitra, a novel framework for audio-driven talking head generation, streamlined to learn lip motion, facial expression, as well as head pose motion. Specifically, we train a conditional Motion Diffusion Transformer (cMDT) by modeling facial motion sequences with 3D representation. We condition the cMDT with only two input signals, an audio-sequence, as well as a reference facial image. By extracting additional features directly from audio, Dimitra is able to increase quality and realism of generated videos. In particular, phoneme sequences contribute to the realism of lip motion, whereas text transcript to facial expression and head pose realism. Quantitative and qualitative experiments on two widely employed datasets, VoxCeleb2 and HDTF, showcase that Dimitra is able to outperform existing approaches for generating realistic talking heads imparting lip motion, facial expression, and head pose.

</details>

### [Audio-driven Talking-face Synthesis based on 3D Gaussian](s2:5f4cb16ff522da3007228ddd371c72b5d12d0602.md)
**Botao Xiong** · 2025-02-21

<details>
<summary>Abstract</summary>

Audio-driven talking-face synthesis is of significant importance in various application scenarios, such as remote meetings, AR/VR, and digital humans. Currently, the work in this field can be broadly divided into two categories: implicit representation-based methods and explicit representation-based methods. Implicit representation-based methods often use neural network models to represent human face. For example, NeRF (Neural Radiance Field) uses MLP (Multi-Layer Perceptron) to represent human face, and by inputting the camera pose, NeRF renders a face image from that viewpoint. When training with audio features, it can render face images with different facial movements. However, due to the lack of editability and slow rendering speed of implicit representations, the industry has been exploring new representation methods. Explicit representation-based methods commonly use 3D Gaussian representations of the face, which offers high editability and nearly real-time rendering speed, making these methods surpass implicit-based approaches in many metrics. However, it is difficult to incorporate other signals during the rendering optimization process. To address this issue, this paper combines 3D Gaussian representations with the 3D head model FLAME (Faces Learned with an Articulated Model and Expressions). The FLAME model represents the face's shape and facial movements with a set of parameters. In this paper, audio signals are first transformed into parameters representing facial movements, which are used to initialize the 3D model generated by the parameters, followed by rendering optimization. This paper proposes a 3D Gaussian-based audio-driven lip-sync video generation system. It consists of two main modules: the audio-to-facial movement module and the 3D Gaussian rendering module. The audio-to-facial movement module uses the extracted audio features to generate parameters that control the FLAME model, converting the audio input into natural and reasonable lip shapes and facial movements. The 3D Gaussian rendering module initializes the 3D Gaussian with the FLAME model, optimizes the rendered image from coarse to fine, and finally stitches the generated images together to create a continuous video. Experiments show that this system can generate lip-synchronized, accurate, high-fidelity videos.

</details>

### [NeRF-3DTalker: Neural Radiance Field with 3D Prior Aided Audio Disentanglement for Talking Head Synthesis](2502.14178.md)
**Xiaoxing Liu, Zhilei Liu, Chongke Bi** · 2025-02-20

<details>
<summary>Abstract</summary>

Talking head synthesis is to synthesize a lip-synchronized talking head video using audio. Recently, the capability of NeRF to enhance the realism and texture details of synthesized talking heads has attracted the attention of researchers. However, most current NeRF methods based on audio are exclusively concerned with the rendering of frontal faces. These methods are unable to generate clear talking heads in novel views. Another prevalent challenge in current 3D talking head synthesis is the difficulty in aligning acoustic and visual spaces, which often results in suboptimal lip-syncing of the generated talking heads. To address these issues, we propose Neural Radiance Field with 3D Prior Aided Audio Disentanglement for Talking Head Synthesis (NeRF-3DTalker). Specifically, the proposed method employs 3D prior information to synthesize clear talking heads with free views. Additionally, we propose a 3D Prior Aided Audio Disentanglement module, which is designed to disentangle the audio into two distinct categories: features related to 3D awarded speech movements and features related to speaking style. Moreover, to reposition the generated frames that are distant from the speaker's motion space in the real space, we have devised a local-global Standardized Space. This method normalizes the irregular positions in the generated frames from both global and local semantic perspectives. Through comprehensive qualitative and quantitative experiments, it has been demonstrated that our NeRF-3DTalker outperforms state-of-the-art in synthesizing realistic talking head videos, exhibiting superior image quality and lip synchronization. Project page: https://nerf-3dtalker.github.io/NeRF-3Dtalker.

</details>

### [SayAnything: Audio-Driven Lip Synchronization with Conditional Video Diffusion](2502.11515.md)
**Junxian Ma, Shiwen Wang, Jian Yang, Junyi Hu et al.** · 2025-02-17

<details>
<summary>Abstract</summary>

Recent advances in diffusion models have led to significant progress in audio-driven lip synchronization. However, existing methods typically rely on constrained audio-visual alignment priors or multi-stage learning of intermediate representations to force lip motion synthesis. This leads to complex training pipelines and limited motion naturalness. In this paper, we present SayAnything, a conditional video diffusion framework that directly synthesizes lip movements from audio input while preserving speaker identity. Specifically, we propose three specialized modules including identity preservation module, audio guidance module, and editing control module. Our novel design effectively balances different condition signals in the latent space, enabling precise control over appearance, motion, and region-specific generation without requiring additional supervision signals or intermediate representations. Extensive experiments demonstrate that SayAnything generates highly realistic videos with improved lip-teeth coherence, enabling unseen characters to say anything, while effectively generalizing to animated characters.

</details>

### [Long-Term TalkingFace Generation via Motion-Prior Conditional Diffusion Model](2502.09533.md)
**Fei Shen, Cong Wang, Junyao Gao, Qin Guo et al.** · 2025-02-13

<details>
<summary>Abstract</summary>

Recent advances in conditional diffusion models have shown promise for generating realistic TalkingFace videos, yet challenges persist in achieving consistent head movement, synchronized facial expressions, and accurate lip synchronization over extended generations. To address these, we introduce the \textbf{M}otion-priors \textbf{C}onditional \textbf{D}iffusion \textbf{M}odel (\textbf{MCDM}), which utilizes both archived and current clip motion priors to enhance motion prediction and ensure temporal consistency. The model consists of three key elements: (1) an archived-clip motion-prior that incorporates historical frames and a reference frame to preserve identity and context; (2) a present-clip motion-prior diffusion model that captures multimodal causality for accurate predictions of head movements, lip sync, and expressions; and (3) a memory-efficient temporal attention mechanism that mitigates error accumulation by dynamically storing and updating motion features. We also release the \textbf{TalkingFace-Wild} dataset, a multilingual collection of over 200 hours of footage across 10 languages. Experimental results demonstrate the effectiveness of MCDM in maintaining identity and motion continuity for long-term TalkingFace generation. Code, models, and datasets will be publicly available.

</details>

### [Playmate: Flexible Control of Portrait Animation via 3D-Implicit Space Guided Diffusion](2502.07203.md)
**Xingpei Ma, Jiaran Cai, Yuansheng Guan, Shenneng Huang et al.** · 2025-02-11

<details>
<summary>Abstract</summary>

Recent diffusion-based talking face generation models have demonstrated impressive potential in synthesizing videos that accurately match a speech audio clip with a given reference identity. However, existing approaches still encounter significant challenges due to uncontrollable factors, such as inaccurate lip-sync, inappropriate head posture and the lack of fine-grained control over facial expressions. In order to introduce more face-guided conditions beyond speech audio clips, a novel two-stage training framework Playmate is proposed to generate more lifelike facial expressions and talking faces. In the first stage, we introduce a decoupled implicit 3D representation along with a meticulously designed motion-decoupled module to facilitate more accurate attribute disentanglement and generate expressive talking videos directly from audio cues. Then, in the second stage, we introduce an emotion-control module to encode emotion control information into the latent space, enabling fine-grained control over emotions and thereby achieving the ability to generate talking videos with desired emotion. Extensive experiments demonstrate that Playmate not only outperforms existing state-of-the-art methods in terms of video quality, but also exhibits strong competitiveness in lip synchronization while offering improved flexibility in controlling emotion and head pose. The code will be available at https://github.com/Playmate111/Playmate.

</details>

### [EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](2502.00654.md)
**Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond et al.** · 2025-02-02

<details>
<summary>Abstract</summary>

3D Gaussian splatting-based talking head synthesis has recently gained attention for its ability to render high-fidelity images with real-time inference speed. However, since it is typically trained on only a short video that lacks the diversity in facial emotions, the resultant talking heads struggle to represent a wide range of emotions. To address this issue, we propose a lip-aligned emotional face generator and leverage it to train our EmoTalkingGaussian model. It is able to manipulate facial emotions conditioned on continuous emotion values (i.e., valence and arousal); while retaining synchronization of lip movements with input audio. Additionally, to achieve the accurate lip synchronization for in-the-wild audio, we introduce a self-supervised learning method that leverages a text-to-speech network and a visual-audio synchronization network. We experiment our EmoTalkingGaussian on publicly available videos and have obtained better results than state-of-the-arts in terms of image quality (measured in PSNR, SSIM, LPIPS), emotion expression (measured in V-RMSE, A-RMSE, V-SA, A-SA, Emotion Accuracy), and lip synchronization (measured in LMD, Sync-E, Sync-C), respectively.

</details>

### [Bridging The Multi-Modality Gaps of Audio, Visual and Linguistic for Speech Enhancement](2501.13375.md)
**Meng-Ping Lin, Jen-Cheng Hou, Chia-Wei Chen, Shao-Yi Chien et al.** · 2025-01-23

<details>
<summary>Abstract</summary>

Speech enhancement (SE) aims to improve the quality and intelligibility of speech in noisy environments. Recent studies have shown that incorporating visual cues in audio signal processing can enhance SE performance. Given that human speech communication naturally involves audio, visual, and linguistic modalities, it is reasonable to expect additional improvements by integrating linguistic information. However, effectively bridging these modality gaps, particularly during knowledge transfer remains a significant challenge. In this paper, we propose a novel multi-modal learning framework, termed DLAV-SE, which leverages a diffusion-based model integrating audio, visual, and linguistic information for audio-visual speech enhancement (AVSE). Within this framework, the linguistic modality is modeled using a pretrained language model (PLM), which transfers linguistic knowledge to the audio-visual domain through a cross-modal knowledge transfer (CMKT) mechanism during training. After training, the PLM is no longer required at inference, as its knowledge is embedded into the AVSE model through the CMKT process. We conduct a series of SE experiments to evaluate the effectiveness of our approach. Results show that the proposed DLAV-SE system significantly improves speech quality and reduces generative artifacts, such as phonetic confusion, compared to state-of-the-art (SOTA) methods. Furthermore, visualization analyses confirm that the CMKT method enhances the generation quality of the AVSE outputs. These findings highlight both the promise of diffusion-based methods for advancing AVSE and the value of incorporating linguistic information to further improve system performance.

</details>

### [EMO2: End-Effector Guided Audio-Driven Avatar Video Generation](2501.10687.md)
**Linrui Tian, Siqi Hu, Qi Wang, Bang Zhang et al.** · 2025-01-18

<details>
<summary>Abstract</summary>

In this paper, we propose a novel audio-driven talking head method capable of simultaneously generating highly expressive facial expressions and hand gestures. Unlike existing methods that focus on generating full-body or half-body poses, we investigate the challenges of co-speech gesture generation and identify the weak correspondence between audio features and full-body gestures as a key limitation. To address this, we redefine the task as a two-stage process. In the first stage, we generate hand poses directly from audio input, leveraging the strong correlation between audio signals and hand movements. In the second stage, we employ a diffusion model to synthesize video frames, incorporating the hand poses generated in the first stage to produce realistic facial expressions and body movements. Our experimental results demonstrate that the proposed method outperforms state-of-the-art approaches, such as CyberHost and Vlogger, in terms of both visual quality and synchronization accuracy. This work provides a new perspective on audio-driven gesture generation and a robust framework for creating expressive and natural talking head animations.

</details>

### [Joint Learning of Depth and Appearance for Portrait Image Animation](2501.08649.md)
**Xinya Ji, Gaspard Zoss, Prashanth Chandran, Lingchen Yang et al.** · 2025-01-15

<details>
<summary>Abstract</summary>

2D portrait animation has experienced significant advancements in recent years. Much research has utilized the prior knowledge embedded in large generative diffusion models to enhance high-quality image manipulation. However, most methods only focus on generating RGB images as output, and the co-generation of consistent visual plus 3D output remains largely under-explored. In our work, we propose to jointly learn the visual appearance and depth simultaneously in a diffusion-based portrait image generator. Our method embraces the end-to-end diffusion paradigm and introduces a new architecture suitable for learning this conditional joint distribution, consisting of a reference network and a channel-expanded diffusion backbone. Once trained, our framework can be efficiently adapted to various downstream applications, such as facial depth-to-image and image-to-depth generation, portrait relighting, and audio-driven talking head animation with consistent 3D output.

</details>

### [Identity-Preserving Video Dubbing Using Motion Warping](2501.04586.md)
**Runzhen Liu, Qinjie Lin, Yunfei Liu, Lijian Lin et al.** · 2025-01-08

<details>
<summary>Abstract</summary>

Video dubbing aims to synthesize realistic, lip-synced videos from a reference video and a driving audio signal. Although existing methods can accurately generate mouth shapes driven by audio, they often fail to preserve identity-specific features, largely because they do not effectively capture the nuanced interplay between audio cues and the visual attributes of reference identity . As a result, the generated outputs frequently lack fidelity in reproducing the unique textural and structural details of the reference identity. To address these limitations, we propose IPTalker, a novel and robust framework for video dubbing that achieves seamless alignment between driving audio and reference identity while ensuring both lip-sync accuracy and high-fidelity identity preservation. At the core of IPTalker is a transformer-based alignment mechanism designed to dynamically capture and model the correspondence between audio features and reference images, thereby enabling precise, identity-aware audio-visual integration. Building on this alignment, a motion warping strategy further refines the results by spatially deforming reference images to match the target audio-driven configuration. A dedicated refinement process then mitigates occlusion artifacts and enhances the preservation of fine-grained textures, such as mouth details and skin features. Extensive qualitative and quantitative evaluations demonstrate that IPTalker consistently outperforms existing approaches in terms of realism, lip synchronization, and identity retention, establishing a new state of the art for high-quality, identity-consistent video dubbing.

</details>

### [Generating and Detecting Various Types of Fake Image and Audio Content: A Review of Modern Deep Learning Technologies and Tools](2501.06227.md)
**Arash Dehghani, Hossein Saberi** · 2025-01-07

<details>
<summary>Abstract</summary>

This paper reviews the state-of-the-art in deepfake generation and detection, focusing on modern deep learning technologies and tools based on the latest scientific advancements. The rise of deepfakes, leveraging techniques like Variational Autoencoders (VAEs), Generative Adversarial Networks (GANs), Diffusion models and other generative models, presents significant threats to privacy, security, and democracy. This fake media can deceive individuals, discredit real people and organizations, facilitate blackmail, and even threaten the integrity of legal, political, and social systems. Therefore, finding appropriate solutions to counter the potential threats posed by this technology is essential. We explore various deepfake methods, including face swapping, voice conversion, reenactment and lip synchronization, highlighting their applications in both benign and malicious contexts. The review critically examines the ongoing "arms race" between deepfake generation and detection, analyzing the challenges in identifying manipulated contents. By examining current methods and highlighting future research directions, this paper contributes to a crucial understanding of this rapidly evolving field and the urgent need for robust detection strategies to counter the misuse of this powerful technology. While focusing primarily on audio, image, and video domains, this study allows the reader to easily grasp the latest advancements in deepfake generation and detection.

</details>

### [Multi-Level Feature Dynamic Fusion Neural Radiance Fields for Audio-Driven Talking Head Generation](s2:9e27ca01577afb9eba72b34aa9acfc6b61f93ee2.md)
**Wenchao Song, Qiong Liu, Yanchao Liu, Pengzhou Zhang et al.** · 2025-01-06

<details>
<summary>Abstract</summary>

Audio-driven cross-modal talking head generation has experienced significant advancement in the last several years, and it aims to generate a talking head video that corresponds to a given audio sequence. Out of these approaches, the NeRF-based method can generate videos featuring a specific person with more natural motion compared to the one-shot methods. However, previous approaches failed to distinguish the importance of different regions, resulting in the loss of information-rich region features. To alleviate the problem and improve video quality, we propose MLDF-NeRF, an end-to-end method for talking head generation, which can achieve better vector representation through multi-level feature dynamic fusion. Specifically, we designed two modules in MLDF-NeRF to enhance the cross-modal mapping ability between audio and different facial regions. We initially developed a multi-level tri-plane hash representation that uses three sets of tri-plane hash networks with varying resolutions of limitation to capture the dynamic information of the face more accurately. Then, we introduce the idea of multi-head attention and design an efficient audio-visual fusion module that explicitly fuses audio features with image features from different planes, thereby improving the mapping between audio features and spatial information. Meanwhile, the design helps to minimize interference from facial areas unrelated to audio, thereby improving the overall quality of the representation. The quantitative and qualitative results indicate that our proposed method can effectively generate talk heads with natural actions and realistic details. Compared with previous methods, it performs better in terms of image quality, lip sync, and other aspects.

</details>

### [MoEE: Mixture of Emotion Experts for Audio-Driven Portrait Animation](2501.01808.md)
**Huaize Liu, Wenzhang Sun, Donglin Di, Shibo Sun et al.** · 2025-01-03

<details>
<summary>Abstract</summary>

The generation of talking avatars has achieved significant advancements in precise audio synchronization. However, crafting lifelike talking head videos requires capturing a broad spectrum of emotions and subtle facial expressions. Current methods face fundamental challenges: a) the absence of frameworks for modeling single basic emotional expressions, which restricts the generation of complex emotions such as compound emotions; b) the lack of comprehensive datasets rich in human emotional expressions, which limits the potential of models. To address these challenges, we propose the following innovations: 1) the Mixture of Emotion Experts (MoEE) model, which decouples six fundamental emotions to enable the precise synthesis of both singular and compound emotional states; 2) the DH-FaceEmoVid-150 dataset, specifically curated to include six prevalent human emotional expressions as well as four types of compound emotions, thereby expanding the training potential of emotion-driven models. Furthermore, to enhance the flexibility of emotion control, we propose an emotion-to-latents module that leverages multimodal inputs, aligning diverse control signals-such as audio, text, and labels-to ensure more varied control inputs as well as the ability to control emotions using audio alone. Through extensive quantitative and qualitative evaluations, we demonstrate that the MoEE framework, in conjunction with the DH-FaceEmoVid-150 dataset, excels in generating complex emotional expressions and nuanced facial details, setting a new benchmark in the field. These datasets will be publicly released.

</details>

### [Decoupled Two-Stage Talking Head Generation via Gaussian-Landmark-Based Neural Radiance Fields](s2:64ce7c264dd66ece77fff4210891dd4aadc3d2bb.md)
**Bo-Yao Ma, Yuanping Cao, Lei Zhang** · 2025-01-01

<details>
<summary>Abstract</summary>

—Talking head generation based on neural radiance fields (NeRF) has gained prominence, primarily owing to its implicit 3D representation capabilities within neural networks. However, most NeRF-based methods often intertwine audio-to-video conversion in a joint training process, resulting in challenges such as inadequate lip synchronization, limited learning efficiency, large memory requirement and lack of editability. In response to these issues, this paper introduces a fully decoupled NeRF-based method for generating talking head. This method separates the audio-to-video conversion into two stages through the use of facial landmarks. Notably, the Transformer network is used to establish the cross-modal connection between audio and landmarks effectively and generate landmarks conforming to the distribution of training data. Then, these landmarks are combined with Gaussian relative position coding to refine the sampling points on the rays, thereby constructing a dynamic neural radiation field conditioned on these landmarks for rendering the generated head. This decoupled setup enhances both the fidelity and flexibility of mapping audio to video with two independent small-scale networks. Additionally, it supports the generation of the torso part from the head-only image with deformable convolution, further enhancing the realism of the generated talking head. The experimental results demonstrate that our method excels in producing lifelike talking head, and the lightweight neural network models also exhibit superior speed and learning efficiency with less memory requirement.

</details>

### [SynGauss: Real-Time 3D Gaussian Splatting for Audio-Driven Talking Head Synthesis](s2:6e6d84175ff8896354892e3f0c20a196bde8a9ab.md)
**Zhanyi Zhou, Quandong Feng, Hongjun Li** · 2025-01-01

<details>
<summary>Abstract</summary>

In the field of virtual human generation, Neural Radiance Fields (NeRF) have made significant strides in precise geometric modeling and color accuracy, establishing new benchmarks for complex viewpoint synthesis and 3D reconstruction. Despite these advancements, existing methods face substantial limitations in real-time dynamic facial expression capture and managing high-frequency details, particularly in rapid facial movements and accurate lip synchronization. These constraints are largely due to the high computational load and the dense data requirements hamper real-time rendering. Additionally, traditional radiance fields struggle to capture subtle facial changes driven by audio, often resulting in animations that lack expressiveness and naturalness. Building upon the foundation laid by TalkingGaussian,this paper introduces an advanced framework named SynGauss that employs 3D Gaussian Splatting to precisely decouple facial and lip movements. We have enhanced this approach by incorporating lip expression coefficients and a regional multi-head attention mechanism, which allow for detailed and controlled animation of complex facial dynamics. Our modifications provide a more refined control over lip movements and facial expressions, significantly improving the realism and expressiveness of the animations while maintaining the efficiency required for real-time applications. This approach holds great promise for real-time applications such as virtual assistants and immersive entertainment experiences, offering more realistic and controllable animation generation.(Project address https://github.com/zzyfight0703/SynGauss/tree/main)

</details>

