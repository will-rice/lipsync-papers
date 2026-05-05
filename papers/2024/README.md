# 2024

113 papers in this year.

### [Seeing the Sound: Multilingual Lip Sync for Real-Time Face-to-Face Translation](s2:b3ad6e15a53015028e88171e6baf21bca5eb5682.md)
**A. Oskooei, Mehmet S. Aktas, Mustafa Keles** · 2024-12-28

<details>
<summary>Abstract</summary>

Imagine a future where language is no longer a barrier to real-time conversations, enabling instant and lifelike communication across the globe. As cultural boundaries blur, the demand for seamless multilingual communication has become a critical technological challenge. This paper addresses the lack of robust solutions for real-time face-to-face translation, particularly for low-resource languages, by introducing a comprehensive framework that not only translates language but also replicates voice nuances and synchronized facial expressions. Our research tackles the primary challenge of achieving accurate lip synchronization across culturally diverse languages, filling a significant gap in the literature by evaluating the generalizability of lip sync models beyond English. Specifically, we develop a novel evaluation framework combining quantitative lip sync error metrics and qualitative assessments by human observers. This framework is applied to assess two state-of-the-art lip sync models with different architectures for Turkish, Persian, and Arabic languages, using a newly collected dataset. Based on these findings, we propose and implement a modular system that integrates language-agnostic lip sync models with neural networks to deliver a fully functional face-to-face translation experience. Inference Time Analysis shows this system achieves highly realistic, face-translated talking heads in real time, with a throughput as low as 0.381 s. This transformative framework is primed for deployment in immersive environments such as VR/AR, Metaverse ecosystems, and advanced video conferencing platforms. It offers substantial benefits to developers and businesses aiming to build next-generation multilingual communication systems for diverse applications. While this work focuses on three languages, its modular design allows scalability to additional languages. However, further testing in broader linguistic and cultural contexts is required to confirm its universal applicability, paving the way for a more interconnected and inclusive world where language ceases to hinder human connection.

</details>

### [Joint Co-Speech Gesture and Expressive Talking Face Generation using Diffusion with Adapters](2412.14333.md)
**Steven Hogue, Chenxu Zhang, Yapeng Tian, Xiaohu Guo** · 2024-12-18

<details>
<summary>Abstract</summary>

Recent advances in co-speech gesture and talking head generation have been impressive, yet most methods focus on only one of the two tasks. Those that attempt to generate both often rely on separate models or network modules, increasing training complexity and ignoring the inherent relationship between face and body movements. To address the challenges, in this paper, we propose a novel model architecture that jointly generates face and body motions within a single network. This approach leverages shared weights between modalities, facilitated by adapters that enable adaptation to a common latent space. Our experiments demonstrate that the proposed framework not only maintains state-of-the-art co-speech gesture and talking head generation performance but also significantly reduces the number of parameters required.

</details>

### [GLCF: A Global-Local Multimodal Coherence Analysis Framework for Talking Face Generation Detection](2412.13656.md)
**Xiaocan Chen, Qilin Yin, Jiarui Liu, Wei Lu et al.** · 2024-12-18

<details>
<summary>Abstract</summary>

Talking face generation (TFG) allows for producing lifelike talking videos of any character using only facial images and accompanying text. Abuse of this technology could pose significant risks to society, creating the urgent need for research into corresponding detection methods. However, research in this field has been hindered by the lack of public datasets. In this paper, we construct the first large-scale multi-scenario talking face dataset (MSTF), which contains 22 audio and video forgery techniques, filling the gap of datasets in this field. The dataset covers 11 generation scenarios and more than 20 semantic scenarios, closer to the practical application scenario of TFG. Besides, we also propose a TFG detection framework, which leverages the analysis of both global and local coherence in the multimodal content of TFG videos. Therefore, a region-focused smoothness detection module (RSFDM) and a discrepancy capture-time frame aggregation module (DCTAM) are introduced to evaluate the global temporal coherence of TFG videos, aggregating multi-grained spatial information. Additionally, a visual-audio fusion module (V-AFM) is designed to evaluate audiovisual coherence within a localized temporal perspective. Comprehensive experiments demonstrate the reasonableness and challenges of our datasets, while also indicating the superiority of our proposed method compared to the state-of-the-art deepfake detection approaches.

</details>

### [GRS-Wav2lip: General Speech-Driven Lip Synthesis in the Wild](s2:5b6e1322be854160160f8f8201a478fc5839be3c.md)
**Junda Wu, Donghan Ye, Lijun Fu, Zixuan Zhang** · 2024-12-13

<details>
<summary>Abstract</summary>

In recent years, advancements in virtual digital human technology have accelerated considerably; however, many existing lip synchronization models lack adequate focus on lip details, often leading to asynchrony between speech and lip movements. This paper introduces a novel method, GRS- Wav2Lip, designed to enhance the naturalness and synchronization of generated talking face videos. We have restructured the convolutional layers of the identity encoder within the generator, replacing standard convolutional layers with gated convolutions to improve the model's ability to capture lip-related details and motion-specific features effectively. Additionally, we introduce the SAC module to dynamically adjust the receptive field, enabling the effective capture of both global and local features. To improve resolution and image detail, we integrate the RRDB module, which significantly enhances image quality even with low-resolution inputs. Finally, we employ the LPIPS loss function to accurately measure the perceptual quality of generated images. Experimental results show that our approach not only strengthens the model's generative capacity but also leads to substantial improvements in lip synchronization and image detail quality.

</details>

### [LatentSync: Taming Audio-Conditioned Latent Diffusion Models for Lip Sync with SyncNet Supervision](2412.09262.md)
**Chunyu Li, Chao Zhang, Weikai Xu, Jingyu Lin et al.** · 2024-12-12

<details>
<summary>Abstract</summary>

End-to-end audio-conditioned latent diffusion models (LDMs) have been widely adopted for audio-driven portrait animation, demonstrating their effectiveness in generating lifelike and high-resolution talking videos. However, direct application of audio-conditioned LDMs to lip-synchronization (lip-sync) tasks results in suboptimal lip-sync accuracy. Through an in-depth analysis, we identified the underlying cause as the "shortcut learning problem", wherein the model predominantly learns visual-visual shortcuts while neglecting the critical audio-visual correlations. To address this issue, we explored different approaches for integrating SyncNet supervision into audio-conditioned LDMs to explicitly enforce the learning of audio-visual correlations. Since the performance of SyncNet directly influences the lip-sync accuracy of the supervised model, the training of a well-converged SyncNet becomes crucial. We conducted the first comprehensive empirical studies to identify key factors affecting SyncNet convergence. Based on our analysis, we introduce StableSyncNet, with an architecture designed for stable convergence. Our StableSyncNet achieved a significant improvement in accuracy, increasing from 91% to 94% on the HDTF test set. Additionally, we introduce a novel Temporal Representation Alignment (TREPA) mechanism to enhance temporal consistency in the generated videos. Experimental results show that our method surpasses state-of-the-art lip-sync approaches across various evaluation metrics on the HDTF and VoxCeleb2 datasets.

</details>

### [GoHD: Gaze-oriented and Highly Disentangled Portrait Animation with Rhythmic Poses and Realistic Expression](2412.09296.md)
**Ziqi Zhou, Weize Quan, Hailin Shi, Wei Li et al.** · 2024-12-12

<details>
<summary>Abstract</summary>

Audio-driven talking head generation necessitates seamless integration of audio and visual data amidst the challenges posed by diverse input portraits and intricate correlations between audio and facial motions. In response, we propose a robust framework GoHD designed to produce highly realistic, expressive, and controllable portrait videos from any reference identity with any motion. GoHD innovates with three key modules: Firstly, an animation module utilizing latent navigation is introduced to improve the generalization ability across unseen input styles. This module achieves high disentanglement of motion and identity, and it also incorporates gaze orientation to rectify unnatural eye movements that were previously overlooked. Secondly, a conformer-structured conditional diffusion model is designed to guarantee head poses that are aware of prosody. Thirdly, to estimate lip-synchronized and realistic expressions from the input audio within limited training data, a two-stage training strategy is devised to decouple frequent and frame-wise lip motion distillation from the generation of other more temporally dependent but less audio-related motions, e.g., blinks and frowns. Extensive experiments validate GoHD's advanced generalization capabilities, demonstrating its effectiveness in generating realistic talking face results on arbitrary subjects.

</details>

### [PortraitTalk: Towards Customizable One-Shot Audio-to-Talking Face Generation](2412.07754.md)
**Fatemeh Nazarieh, Zhenhua Feng, Diptesh Kanojia, Muhammad Awais et al.** · 2024-12-10

<details>
<summary>Abstract</summary>

Audio-driven talking face generation is a challenging task in digital communication. Despite significant progress in the area, most existing methods concentrate on audio-lip synchronization, often overlooking aspects such as visual quality, customization, and generalization that are crucial to producing realistic talking faces. To address these limitations, we introduce a novel, customizable one-shot audio-driven talking face generation framework, named PortraitTalk. Our proposed method utilizes a latent diffusion framework consisting of two main components: IdentityNet and AnimateNet. IdentityNet is designed to preserve identity features consistently across the generated video frames, while AnimateNet aims to enhance temporal coherence and motion consistency. This framework also integrates an audio input with the reference images, thereby reducing the reliance on reference-style videos prevalent in existing approaches. A key innovation of PortraitTalk is the incorporation of text prompts through decoupled cross-attention mechanisms, which significantly expands creative control over the generated videos. Through extensive experiments, including a newly developed evaluation metric, our model demonstrates superior performance over the state-of-the-art methods, setting a new standard for the generation of customizable realistic talking faces suitable for real-world applications.

</details>

### [Emotional Synchronization for Audio-Driven Talking-Head Generation](s2:2db415c4afcf4caa5ba6d3402e2a9a839fc5f3d0.md)
**Zhao Zhang, Yan Luo, Zhichao Zuo, Richang Hong et al.** · 2024-12-09

<details>
<summary>Abstract</summary>

Audio-driven talking-head synthesis has become a significant focus in the field of virtual human applications. However, existing methodologies face challenges in effectively synchronizing audio and video, especially in maintaining emotional consistency. Additionally, there is a notable inefficiency in leveraging emotional prompts to guide expression generation. To address these limitations, this paper introduces an Emotion Synchronized audio-driven Talking-head synthesis (EST) approach. The EST approach aims to enhance the emotion-agnostic talking-head models by enabling emotion control, and it incorporates a diffusion module to learn diverse latent rep-resentations. Furthermore, EST utilizes null-text embedding to align the latent code with emotional prompts. Additionally, a novel Sync Attention Block (SAB) is developed to broaden the spatial perceptual field, thus preventing the loss of critical information. Extensive experiments demonstrate the effectiveness of the EST method, showcasing state-of-the-art performance across widely-adopted datasets. Moreover, the EST approach exhibits exceptional generalization capabilities, even in scenarios where emotional training videos are unavailable.

</details>

### [MEMO: Memory-Guided Diffusion for Expressive Talking Video Generation](2412.04448.md)
**Longtao Zheng, Yifan Zhang, Hanzhong Guo, Jiachun Pan et al.** · 2024-12-05

<details>
<summary>Abstract</summary>

Recent advances in video diffusion models have unlocked new potential for realistic audio-driven talking video generation. However, achieving seamless audio-lip synchronization, maintaining long-term identity consistency, and producing natural, audio-aligned expressions in generated talking videos remain significant challenges. To address these challenges, we propose Memory-guided EMOtion-aware diffusion (MEMO), an end-to-end audio-driven portrait animation approach to generate identity-consistent and expressive talking videos. Our approach is built around two key modules: (1) a memory-guided temporal module, which enhances long-term identity consistency and motion smoothness by developing memory states to store information from a longer past context to guide temporal modeling via linear attention; and (2) an emotion-aware audio module, which replaces traditional cross attention with multi-modal attention to enhance audio-video interaction, while detecting emotions from audio to refine facial expressions via emotion adaptive layer norm. Extensive quantitative and qualitative results demonstrate that MEMO generates more realistic talking videos across diverse image and audio types, outperforming state-of-the-art methods in overall quality, audio-lip synchronization, identity consistency, and expression-emotion alignment.

</details>

### [IF-MDM: Implicit Face Motion Diffusion Model for High-Fidelity Realtime Talking Head Generation](2412.04000.md)
**Sejong Yang, Seoung Wug Oh, Yang Zhou, Seon Joo Kim** · 2024-12-05

<details>
<summary>Abstract</summary>

We introduce a novel approach for high-resolution talking head generation from a single image and audio input. Prior methods using explicit face models, like 3D morphable models (3DMM) and facial landmarks, often fall short in generating high-fidelity videos due to their lack of appearance-aware motion representation. While generative approaches such as video diffusion models achieve high video quality, their slow processing speeds limit practical application. Our proposed model, Implicit Face Motion Diffusion Model (IF-MDM), employs implicit motion to encode human faces into appearance-aware compressed facial latents, enhancing video generation. Although implicit motion lacks the spatial disentanglement of explicit models, which complicates alignment with subtle lip movements, we introduce motion statistics to help capture fine-grained motion information. Additionally, our model provides motion controllability to optimize the trade-off between motion intensity and visual quality during inference. IF-MDM supports real-time generation of 512x512 resolution videos at up to 45 frames per second (fps). Extensive evaluations demonstrate its superior performance over existing diffusion and explicit face models. The code will be released publicly, available alongside supplementary materials. The video results can be found on https://bit.ly/ifmdm_supplementary.

</details>

### [SINGER: Vivid Audio-driven Singing Video Generation with Multi-scale Spectral Diffusion Model](2412.03430.md)
**Yan Li, Ziya Zhou, Zhiqiang Wang, Wei Xue et al.** · 2024-12-04

<details>
<summary>Abstract</summary>

Recent advancements in generative models have significantly enhanced talking face video generation, yet singing video generation remains underexplored. The differences between human talking and singing limit the performance of existing talking face video generation models when applied to singing. The fundamental differences between talking and singing-specifically in audio characteristics and behavioral expressions-limit the effectiveness of existing models. We observe that the differences between singing and talking audios manifest in terms of frequency and amplitude. To address this, we have designed a multi-scale spectral module to help the model learn singing patterns in the spectral domain. Additionally, we develop a spectral-filtering module that aids the model in learning the human behaviors associated with singing audio. These two modules are integrated into the diffusion model to enhance singing video generation performance, resulting in our proposed model, SINGER. Furthermore, the lack of high-quality real-world singing face videos has hindered the development of the singing video generation community. To address this gap, we have collected an in-the-wild audio-visual singing dataset to facilitate research in this area. Our experiments demonstrate that SINGER is capable of generating vivid singing videos and outperforms state-of-the-art methods in both objective and subjective evaluations.

</details>

### [Synergizing Motion and Appearance: Multi-Scale Compensatory Codebooks for Talking Head Video Generation](2412.00719.md)
**Shuling Zhao, Fa-Ting Hong, Xiaoshui Huang, Dan Xu** · 2024-12-01

<details>
<summary>Abstract</summary>

Talking head video generation aims to generate a realistic talking head video that preserves the person's identity from a source image and the motion from a driving video. Despite the promising progress made in the field, it remains a challenging and critical problem to generate videos with accurate poses and fine-grained facial details simultaneously. Essentially, facial motion is often highly complex to model precisely, and the one-shot source face image cannot provide sufficient appearance guidance during generation due to dynamic pose changes. To tackle the problem, we propose to jointly learn motion and appearance codebooks and perform multi-scale codebook compensation to effectively refine both the facial motion conditions and appearance features for talking face image decoding. Specifically, the designed multi-scale motion and appearance codebooks are learned simultaneously in a unified framework to store representative global facial motion flow and appearance patterns. Then, we present a novel multi-scale motion and appearance compensation module, which utilizes a transformer-based codebook retrieval strategy to query complementary information from the two codebooks for joint motion and appearance compensation. The entire process produces motion flows of greater flexibility and appearance features with fewer distortions across different scales, resulting in a high-quality talking head video generation framework. Extensive experiments on various benchmarks validate the effectiveness of our approach and demonstrate superior generation results from both qualitative and quantitative perspectives when compared to state-of-the-art competitors.

</details>

### [LokiTalk: Learning Fine-Grained and Generalizable Correspondences to Enhance NeRF-based Talking Head Synthesis](2411.19525.md)
**Tianqi Li, Ruobing Zheng, Bonan Li, Zicheng Zhang et al.** · 2024-11-29

<details>
<summary>Abstract</summary>

Despite significant progress in talking head synthesis since the introduction of Neural Radiance Fields (NeRF), visual artifacts and high training costs persist as major obstacles to large-scale commercial adoption. We propose that identifying and establishing fine-grained and generalizable correspondences between driving signals and generated results can simultaneously resolve both problems. Here we present LokiTalk, a novel framework designed to enhance NeRF-based talking heads with lifelike facial dynamics and improved training efficiency. To achieve fine-grained correspondences, we introduce Region-Specific Deformation Fields, which decompose the overall portrait motion into lip movements, eye blinking, head pose, and torso movements. By hierarchically modeling the driving signals and their associated regions through two cascaded deformation fields, we significantly improve dynamic accuracy and minimize synthetic artifacts. Furthermore, we propose ID-Aware Knowledge Transfer, a plug-and-play module that learns generalizable dynamic and static correspondences from multi-identity videos, while simultaneously extracting ID-specific dynamic and static features to refine the depiction of individual characters. Comprehensive evaluations demonstrate that LokiTalk delivers superior high-fidelity results and training efficiency compared to previous methods. The code will be released upon acceptance.

</details>

### [Ditto: Motion-Space Diffusion for Controllable Realtime Talking Head Synthesis](2411.19509.md)
**Tianqi Li, Ruobing Zheng, Minghui Yang, Jingdong Chen et al.** · 2024-11-29

<details>
<summary>Abstract</summary>

Recent advances in diffusion models have endowed talking head synthesis with subtle expressions and vivid head movements, but have also led to slow inference speed and insufficient control over generated results. To address these issues, we propose Ditto, a diffusion-based talking head framework that enables fine-grained controls and real-time inference. Specifically, we utilize an off-the-shelf motion extractor and devise a diffusion transformer to generate representations in a specific motion space. We optimize the model architecture and training strategy to address the issues in generating motion representations, including insufficient disentanglement between motion and identity, and large internal discrepancies within the representation. Besides, we employ diverse conditional signals while establishing a mapping between motion representation and facial semantics, enabling control over the generation process and correction of the results. Moreover, we jointly optimize the holistic framework to enable streaming processing, real-time inference, and low first-frame delay, offering functionalities crucial for interactive applications such as AI assistants. Extensive experimental results demonstrate that Ditto generates compelling talking head videos and exhibits superiority in both controllability and real-time performance.

</details>

### [V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow](2411.19486.md)
**Jeongsoo Choi, Ji-Hoon Kim, Jinyu Li, Joon Son Chung et al.** · 2024-11-29

<details>
<summary>Abstract</summary>

In this paper, we introduce V2SFlow, a novel Video-to-Speech (V2S) framework designed to generate natural and intelligible speech directly from silent talking face videos. While recent V2S systems have shown promising results on constrained datasets with limited speakers and vocabularies, their performance often degrades on real-world, unconstrained datasets due to the inherent variability and complexity of speech signals. To address these challenges, we decompose the speech signal into manageable subspaces (content, pitch, and speaker information), each representing distinct speech attributes, and predict them directly from the visual input. To generate coherent and realistic speech from these predicted attributes, we employ a rectified flow matching decoder built on a Transformer architecture, which models efficient probabilistic pathways from random noise to the target speech distribution. Extensive experiments demonstrate that V2SFlow significantly outperforms state-of-the-art methods, even surpassing the naturalness of ground truth utterances. Code and models are available at: https://github.com/kaistmm/V2SFlow

</details>

### [EmotiveTalk: Expressive Talking Head Generation through Audio Information Decoupling and Emotional Video Diffusion](2411.16726.md)
**Haotian Wang, Yuzhe Weng, Yueyan Li, Zilu Guo et al.** · 2024-11-23

<details>
<summary>Abstract</summary>

Diffusion models have revolutionized the field of talking head generation, yet still face challenges in expressiveness, controllability, and stability in long-time generation. In this research, we propose an EmotiveTalk framework to address these issues. Firstly, to realize better control over the generation of lip movement and facial expression, a Vision-guided Audio Information Decoupling (V-AID) approach is designed to generate audio-based decoupled representations aligned with lip movements and expression. Specifically, to achieve alignment between audio and facial expression representation spaces, we present a Diffusion-based Co-speech Temporal Expansion (Di-CTE) module within V-AID to generate expression-related representations under multi-source emotion condition constraints. Then we propose a well-designed Emotional Talking Head Diffusion (ETHD) backbone to efficiently generate highly expressive talking head videos, which contains an Expression Decoupling Injection (EDI) module to automatically decouple the expressions from reference portraits while integrating the target expression information, achieving more expressive generation performance. Experimental results show that EmotiveTalk can generate expressive talking head videos, ensuring the promised controllability of emotions and stability during long-time generation, yielding state-of-the-art performance compared to existing methods.

</details>

### [ConsistentAvatar: Learning to Diffuse Fully Consistent Talking Head Avatar with Temporal Guidance](2411.15436.md)
**Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian et al.** · 2024-11-23

<details>
<summary>Abstract</summary>

Diffusion models have shown impressive potential on talking head generation. While plausible appearance and talking effect are achieved, these methods still suffer from temporal, 3D or expression inconsistency due to the error accumulation and inherent limitation of single-image generation ability. In this paper, we propose ConsistentAvatar, a novel framework for fully consistent and high-fidelity talking avatar generation. Instead of directly employing multi-modal conditions to the diffusion process, our method learns to first model the temporal representation for stability between adjacent frames. Specifically, we propose a Temporally-Sensitive Detail (TSD) map containing high-frequency feature and contours that vary significantly along the time axis. Using a temporal consistent diffusion module, we learn to align TSD of the initial result to that of the video frame ground truth. The final avatar is generated by a fully consistent diffusion module, conditioned on the aligned TSD, rough head normal, and emotion prompt embedding. We find that the aligned TSD, which represents the temporal patterns, constrains the diffusion process to generate temporally stable talking head. Further, its reliable guidance complements the inaccuracy of other conditions, suppressing the accumulated error while improving the consistency on various aspects. Extensive experiments demonstrate that ConsistentAvatar outperforms the state-of-the-art methods on the generated appearance, 3D, expression and temporal consistency. Project page: https://njust-yang.github.io/ConsistentAvatar.github.io/

</details>

### [Specialized Face Encoder for Audio-based Speech to Lip Generation](s2:3cce025710c271851749ef988b732151d7becee6.md)
**Miaoyi Li, Dawei Dai, Lanyu Xue, Pengju Tang** · 2024-11-22

<details>
<summary>Abstract</summary>

Videos that are directly translated and dubbed often fail to provide a natural audiovisual experience, making it crucial to develop methods that can accurately generate lip movements to match the audio. Self-supervised learning models like MAE have proven their robust transfer capabilities. This paper employs the pretraining method of MAE and proposes a new automatic lip-sync network. Additionally, we introduce a separate perceptual loss for the lip region of the generated faces to ensure accurate and clear lip movements. Our automatic lip-sync network consists of four components: video preprocessing, audio preprocessing, generator, and lip-sync discriminator, using facial images and audio features as inputs. We trained an MAE encoder and integrated it into the lip generator. The system was tested on two audiovisual datasets, and the results demonstrate that our proposed method achieves superior performance in both the visual quality of generated talking faces and their synchronization with the audio.

</details>

### [LES-Talker: Fine-Grained Emotion Editing for Talking Head Generation in Linear Emotion Space](2411.09268.md)
**Guanwen Feng, Zhihao Qian, Yunan Li, Siyu Jin et al.** · 2024-11-14

<details>
<summary>Abstract</summary>

While existing one-shot talking head generation models have achieved progress in coarse-grained emotion editing, there is still a lack of fine-grained emotion editing models with high interpretability. We argue that for an approach to be considered fine-grained, it needs to provide clear definitions and sufficiently detailed differentiation. We present LES-Talker, a novel one-shot talking head generation model with high interpretability, to achieve fine-grained emotion editing across emotion types, emotion levels, and facial units. We propose a Linear Emotion Space (LES) definition based on Facial Action Units to characterize emotion transformations as vector transformations. We design the Cross-Dimension Attention Net (CDAN) to deeply mine the correlation between LES representation and 3D model representation. Through mining multiple relationships across different feature and structure dimensions, we enable LES representation to guide the controllable deformation of 3D model. In order to adapt the multimodal data with deviations to the LES and enhance visual quality, we utilize specialized network design and training strategies. Experiments show that our method provides high visual quality along with multilevel and interpretable fine-grained emotion editing, outperforming mainstream methods.

</details>

### [Audio-Semantic Enhanced Pose-Driven Talking Head Generation](s2:43826e0f83cfedf6806325e950e8cbecf833b892.md)
**Meng Liu, Da Li, Yongqiang Li, Xuemeng Song et al.** · 2024-11-01

<details>
<summary>Abstract</summary>

Talking head generation, aiming to create photo-realistic videos from a single reference image and audio input, has emerged as a vibrant area of interest within the computer vision community. Despite notable advancements, several challenges remain unaddressed. For instance, many existing approaches overlook the nuanced relationship between audio semantics and head movement, such as nodding in agreement during affirmative expressions. Additionally, the visual quality of generated content, particularly in depicting teeth, often falls short of achieving authentic realism. To address these limitations, we introduce a groundbreaking audio-semantic enhanced pose-driven talking head generation method. Our approach encompasses a multimodal 3DMM parameter prediction network alongside a high-fidelity video synthesis network, meticulously designed to produce authentic and high-quality talking head videos. The multimodal 3DMM parameter prediction network harnesses both acoustic and audio-deduced semantic information, facilitating accurate head pose predictions that resonate with the semantics of spoken words. Furthermore, to significantly improve the depiction of the mouth area, especially the teeth, our video synthesis stage incorporates a mouth-enhanced network augmented by both local and global discriminators. Comprehensive evaluations across diverse metrics affirm the superiority of our method.

</details>

### [Stereo-Talker: Audio-driven 3D Human Synthesis with Prior-Guided Mixture-of-Experts](2410.23836.md)
**Xiang Deng, Youxin Pang, Xiaochen Zhao, Chao Xu et al.** · 2024-10-31

<details>
<summary>Abstract</summary>

This paper introduces Stereo-Talker, a novel one-shot audio-driven human video synthesis system that generates 3D talking videos with precise lip synchronization, expressive body gestures, temporally consistent photo-realistic quality, and continuous viewpoint control. The process follows a two-stage approach. In the first stage, the system maps audio input to high-fidelity motion sequences, encompassing upper-body gestures and facial expressions. To enrich motion diversity and authenticity, large language model (LLM) priors are integrated with text-aligned semantic audio features, leveraging LLMs' cross-modal generalization power to enhance motion quality. In the second stage, we improve diffusion-based video generation models by incorporating a prior-guided Mixture-of-Experts (MoE) mechanism: a view-guided MoE focuses on view-specific attributes, while a mask-guided MoE enhances region-based rendering stability. Additionally, a mask prediction module is devised to derive human masks from motion data, enhancing the stability and accuracy of masks and enabling mask guiding during inference. We also introduce a comprehensive human video dataset with 2,203 identities, covering diverse body gestures and detailed annotations, facilitating broad generalization. The code, data, and pre-trained models will be released for research purposes.

</details>

### [Multimodal Semantic Communication for Generative Audio-Driven Video Conferencing](2410.22112.md)
**Haonan Tong, Haopeng Li, Hongyang Du, Zhaohui Yang et al.** · 2024-10-29

<details>
<summary>Abstract</summary>

This paper studies an efficient multimodal data communication scheme for video conferencing. In our considered system, a speaker gives a talk to the audiences, with talking head video and audio being transmitted. Since the speaker does not frequently change posture and high-fidelity transmission of audio (speech and music) is required, redundant visual video data exists and can be removed by generating the video from the audio. To this end, we propose a wave-to-video (Wav2Vid) system, an efficient video transmission framework that reduces transmitted data by generating talking head video from audio. In particular, full-duration audio and short-duration video data are synchronously transmitted through a wireless channel, with neural networks (NNs) extracting and encoding audio and video semantics. The receiver then combines the decoded audio and video data, as well as uses a generative adversarial network (GAN) based model to generate the lip movement videos of the speaker. Simulation results show that the proposed Wav2Vid system can reduce the amount of transmitted data by up to 83% while maintaining the perceptual quality of the generated conferencing video.

</details>

### [Real-time 3D-aware Portrait Video Relighting](2410.18355.md)
**Ziqi Cai, Kaiwen Jiang, Shu-Yu Chen, Yu-Kun Lai et al.** · 2024-10-24

<details>
<summary>Abstract</summary>

Synthesizing realistic videos of talking faces under custom lighting conditions and viewing angles benefits various downstream applications like video conferencing. However, most existing relighting methods are either time-consuming or unable to adjust the viewpoints. In this paper, we present the first real-time 3D-aware method for relighting in-the-wild videos of talking faces based on Neural Radiance Fields (NeRF). Given an input portrait video, our method can synthesize talking faces under both novel views and novel lighting conditions with a photo-realistic and disentangled 3D representation. Specifically, we infer an albedo tri-plane, as well as a shading tri-plane based on a desired lighting condition for each video frame with fast dual-encoders. We also leverage a temporal consistency network to ensure smooth transitions and reduce flickering artifacts. Our method runs at 32.98 fps on consumer-level hardware and achieves state-of-the-art results in terms of reconstruction quality, lighting error, lighting instability, temporal consistency and inference speed. We demonstrate the effectiveness and interactivity of our method on various portrait videos with diverse lighting and viewing conditions.

</details>

### [Dynamic Region Fusion Neural Radiance Fields for Audio-Driven Talking Head Generation](s2:1a3201b7b17d919513d915444858ab5434babcd2.md)
**Qiang He, Juan Cao, Haiyan Lu, Pengzhou Zhang** · 2024-10-18

<details>
<summary>Abstract</summary>

Since humans are sensitive to facial appearance and responsiveness, audio-driven talking head generation remains an ongoing challenge. The paper proposes DRMF-NeRF, a novel approach for generating audio-driven head generation by conditional Neural Radiance Fields (NeRF) audio, which can simultaneously achieve fast convergence of the model and generation of facial with natural motion. More specifically, we present an attention-based mechanism dynamic region fusion module that can effectively explore the potential connections and the degree of influence of audio on various face regions to generate a natural and accurate dynamic talking head. Furthermore, inspired by S3IM loss, we design an optimization function that combines the image pointwise loss and structural loss to enhance the quality of the generated image. Comprehensive experiments have shown that our method can generate realistic speech head videos, and its performance is superior to the baseline method.

</details>

### [DAWN: Dynamic Frame Avatar with Non-autoregressive Diffusion Framework for Talking Head Video Generation](2410.13726.md)
**Hanbo Cheng, Limin Lin, Chenyu Liu, Pengcheng Xia et al.** · 2024-10-17

<details>
<summary>Abstract</summary>

Talking head generation intends to produce vivid and realistic talking head videos from a single portrait and speech audio clip. Although significant progress has been made in diffusion-based talking head generation, almost all methods rely on autoregressive strategies, which suffer from limited context utilization beyond the current generation step, error accumulation, and slower generation speed. To address these challenges, we present DAWN (Dynamic frame Avatar With Non-autoregressive diffusion), a framework that enables all-at-once generation of dynamic-length video sequences. Specifically, it consists of two main components: (1) audio-driven holistic facial dynamics generation in the latent motion space, and (2) audio-driven head pose and blink generation. Extensive experiments demonstrate that our method generates authentic and vivid videos with precise lip motions, and natural pose/blink movements. Additionally, with a high generation speed, DAWN possesses strong extrapolation capabilities, ensuring the stable production of high-quality long videos. These results highlight the considerable promise and potential impact of DAWN in the field of talking head video generation. Furthermore, we hope that DAWN sparks further exploration of non-autoregressive approaches in diffusion models. Our code will be publicly available at https://github.com/Hanbo-Cheng/DAWN-pytorch.

</details>

### [Beyond Fixed Topologies: Unregistered Training and Comprehensive Evaluation Metrics for 3D Talking Heads](2410.11041.md)
**Federico Nocentini, Thomas Besnier, Claudio Ferrari, Sylvain Arguillere et al.** · 2024-10-14

<details>
<summary>Abstract</summary>

Generating speech-driven 3D talking heads presents numerous challenges; among those is dealing with varying mesh topologies where no point-wise correspondence exists across the meshes the model can animate. While previous literature works assume fixed mesh structures, in this work we present the first framework capable of animating 3D faces in arbitrary topologies, including real scanned data. Our approach leverages heat diffusion to predict features that are robust to the mesh topology. We explore two training settings: a registered one, in which meshes in a training sequences share a fixed topology but any mesh can be animated at test time, and an fully unregistered one, which allows effective training with varying mesh structures. Additionally, we highlight the limitations of current evaluation metrics and propose new metrics for better lip-syncing evaluation. An extensive evaluation shows our approach performs favorably compared to fixed topology techniques, setting a new benchmark by offering a versatile and high-fidelity solution for 3D talking heads where the topology constraint is dropped. The code along with the pre-trained model are available.

</details>

### [MuseTalk: Real-Time High-Fidelity Video Dubbing via Spatio-Temporal Sampling](2410.10122.md)
**Yue Zhang, Zhizhou Zhong, Minhao Liu, Zhaokang Chen et al.** · 2024-10-14

<details>
<summary>Abstract</summary>

Real-time video dubbing that preserves identity consistency while achieving accurate lip synchronization remains a critical challenge. Existing approaches face a trilemma: diffusion-based methods achieve high visual fidelity but suffer from prohibitive computational costs, while GAN-based solutions sacrifice lip-sync accuracy or dental details for real-time performance. We present MuseTalk, a novel two-stage training framework that resolves this trade-off through latent space optimization and spatio-temporal data sampling strategy. Our key innovations include: (1) During the Facial Abstract Pretraining stage, we propose Informative Frame Sampling to temporally align reference-source pose pairs, eliminating redundant feature interference while preserving identity cues. (2) In the Lip-Sync Adversarial Finetuning stage, we employ Dynamic Margin Sampling to spatially select the most suitable lip-movement-promoting regions, balancing audio-visual synchronization and dental clarity. (3) MuseTalk establishes an effective audio-visual feature fusion framework in the latent space, delivering 30 FPS output at 256*256 resolution on an NVIDIA V100 GPU. Extensive experiments demonstrate that MuseTalk outperforms state-of-the-art methods in visual fidelity while achieving comparable lip-sync accuracy. %The codes and models will be made publicly available upon acceptance. The code is made available at \href{https://github.com/TMElyralab/MuseTalk}{https://github.com/TMElyralab/MuseTalk}

</details>

### [MimicTalk: Mimicking a personalized and expressive 3D talking face in minutes](2410.06734.md)
**Zhenhui Ye, Tianyun Zhong, Yi Ren, Ziyue Jiang et al.** · 2024-10-09

<details>
<summary>Abstract</summary>

Talking face generation (TFG) aims to animate a target identity's face to create realistic talking videos. Personalized TFG is a variant that emphasizes the perceptual identity similarity of the synthesized result (from the perspective of appearance and talking style). While previous works typically solve this problem by learning an individual neural radiance field (NeRF) for each identity to implicitly store its static and dynamic information, we find it inefficient and non-generalized due to the per-identity-per-training framework and the limited training data. To this end, we propose MimicTalk, the first attempt that exploits the rich knowledge from a NeRF-based person-agnostic generic model for improving the efficiency and robustness of personalized TFG. To be specific, (1) we first come up with a person-agnostic 3D TFG model as the base model and propose to adapt it into a specific identity; (2) we propose a static-dynamic-hybrid adaptation pipeline to help the model learn the personalized static appearance and facial dynamic features; (3) To generate the facial motion of the personalized talking style, we propose an in-context stylized audio-to-motion model that mimics the implicit talking style provided in the reference video without information loss by an explicit style representation. The adaptation process to an unseen identity can be performed in 15 minutes, which is 47 times faster than previous person-dependent methods. Experiments show that our MimicTalk surpasses previous baselines regarding video quality, efficiency, and expressiveness. Source code and video samples are available at https://mimictalk.github.io .

</details>

### [EmoGene: Audio-Driven Emotional 3D Talking-Head Generation](2410.17262.md)
**Wenqing Wang, Yun Fu** · 2024-10-07

<details>
<summary>Abstract</summary>

Audio-driven talking-head generation is a crucial and useful technology for virtual human interaction and film-making. While recent advances have focused on improving image fidelity and lip synchronization, generating accurate emotional expressions remains underexplored. In this paper, we introduce EmoGene, a novel framework for synthesizing high-fidelity, audio-driven video portraits with accurate emotional expressions. Our approach employs a variational autoencoder (VAE)-based audio-to-motion module to generate facial landmarks, which are concatenated with emotional embedding in a motion-to-emotion module to produce emotional landmarks. These landmarks drive a Neural Radiance Fields (NeRF)-based emotion-to-video module to render realistic emotional talking-head videos. Additionally, we propose a pose sampling method to generate natural idle-state (non-speaking) videos for silent audio inputs. Extensive experiments demonstrate that EmoGene outperforms previous methods in generating high-fidelity emotional talking-head videos.

</details>

### [Diffusion-based Unsupervised Audio-visual Speech Enhancement](2410.05301.md)
**Jean-Eudes Ayilo, Mostafa Sadeghi, Romain Serizel, Xavier Alameda-Pineda** · 2024-10-04

<details>
<summary>Abstract</summary>

This paper proposes a new unsupervised audio-visual speech enhancement (AVSE) approach that combines a diffusion-based audio-visual speech generative model with a non-negative matrix factorization (NMF) noise model. First, the diffusion model is pre-trained on clean speech conditioned on corresponding video data to simulate the speech generative distribution. This pre-trained model is then paired with the NMF-based noise model to estimate clean speech iteratively. Specifically, a diffusion-based posterior sampling approach is implemented within the reverse diffusion process, where after each iteration, a speech estimate is obtained and used to update the noise parameters. Experimental results confirm that the proposed AVSE approach not only outperforms its audio-only counterpart but also generalizes better than a recent supervised-generative AVSE method. Additionally, the new inference algorithm offers a better balance between inference speed and performance compared to the previous diffusion-based method. Code and demo available at: https://jeaneudesayilo.github.io/fast_UdiffSE

</details>

### [Lipschitz-Driven Noise Robustness in VQ-AE for High-Frequency Texture Repair in ID-Specific Talking Heads](2410.00990.md)
**Jian Yang, Xukun Wang, Wentao Wang, Guoming Li et al.** · 2024-10-01

<details>
<summary>Abstract</summary>

Audio-driven IDentity-specific Talking Head Generation (ID-specific THG) has shown increasing promise for applications in filmmaking and virtual reality. Existing approaches are generally constructed as end-to-end paradigms, and have achieved significant progress. However, they often struggle to capture high-frequency textures due to limited model capacity. To address these limitations, we adopt a simple yet efficient post-processing framework -- unlike previous studies that focus solely on end-to-end training -- guided by our theoretical insights. Specifically, leveraging the \textit{Lipschitz Continuity Theory} of neural networks, we prove a crucial noise tolerance property for the Vector Quantized AutoEncoder (VQ-AE), and establish the existence of a Noise Robustness Upper Bound (NRoUB). This insight reveals that we can efficiently obtain an identity-specific denoiser by training an identity-specific neural discrete representation, without requiring an extra network. Based on this theoretical foundation, we propose a plug-and-play Space-Optimized VQ-AE (SOVQAE) with enhanced NRoUB to achieve temporally-consistent denoising. For practical deployment, we further introduce a cascade pipeline combining a pretrained Wav2Lip model with SOVQAE to perform ID-specific THG. Our experiments demonstrate that this pipeline achieves \textit{state-of-the-art} performance in video quality and robustness for out-of-distribution lip synchronization, surpassing existing identity-specific THG methods. In addition, the pipeline requires only a couple of consumer GPU hours and runs in real time, which is both efficient and practical for industry applications.

</details>

### [Diverse Code Query Learning for Speech-Driven Facial Animation](2409.19143.md)
**Chunzhi Gu, Shigeru Kuriyama, Katsuya Hotta** · 2024-09-27

<details>
<summary>Abstract</summary>

Speech-driven facial animation aims to synthesize lip-synchronized 3D talking faces following the given speech signal. Prior methods to this task mostly focus on pursuing realism with deterministic systems, yet characterizing the potentially stochastic nature of facial motions has been to date rarely studied. While generative modeling approaches can easily handle the one-to-many mapping by repeatedly drawing samples, ensuring a diverse mode coverage of plausible facial motions on small-scale datasets remains challenging and less explored. In this paper, we propose predicting multiple samples conditioned on the same audio signal and then explicitly encouraging sample diversity to address diverse facial animation synthesis. Our core insight is to guide our model to explore the expressive facial latent space with a diversity-promoting loss such that the desired latent codes for diversification can be ideally identified. To this end, building upon the rich facial prior learned with vector-quantized variational auto-encoding mechanism, our model temporally queries multiple stochastic codes which can be flexibly decoded into a diverse yet plausible set of speech-faithful facial motions. To further allow for control over different facial parts during generation, the proposed model is designed to predict different facial portions of interest in a sequential manner, and compose them to eventually form full-face motions. Our paradigm realizes both diverse and controllable facial animation synthesis in a unified formulation. We experimentally demonstrate that our method yields state-of-the-art performance both quantitatively and qualitatively, especially regarding sample diversity.

</details>

### [Stable Video Portraits](2409.18083.md)
**Mirela Ostrek, Justus Thies** · 2024-09-26

<details>
<summary>Abstract</summary>

Rapid advances in the field of generative AI and text-to-image methods in particular have transformed the way we interact with and perceive computer-generated imagery today. In parallel, much progress has been made in 3D face reconstruction, using 3D Morphable Models (3DMM). In this paper, we present SVP, a novel hybrid 2D/3D generation method that outputs photorealistic videos of talking faces leveraging a large pre-trained text-to-image prior (2D), controlled via a 3DMM (3D). Specifically, we introduce a person-specific fine-tuning of a general 2D stable diffusion model which we lift to a video model by providing temporal 3DMM sequences as conditioning and by introducing a temporal denoising procedure. As an output, this model generates temporally smooth imagery of a person with 3DMM-based controls, i.e., a person-specific avatar. The facial appearance of this person-specific avatar can be edited and morphed to text-defined celebrities, without any fine-tuning at test time. The method is analyzed quantitatively and qualitatively, and we show that our method outperforms state-of-the-art monocular head avatar methods.

</details>

### [DH-FaceVid-1K: A Large-Scale High-Quality Dataset for Face Video Generation](2410.07151.md)
**Donglin Di, He Feng, Wenzhang Sun, Yongjia Ma et al.** · 2024-09-23

<details>
<summary>Abstract</summary>

Human-centric generative models are becoming increasingly popular, giving rise to various innovative tools and applications, such as talking face videos conditioned on text or audio prompts. The core of these capabilities lies in powerful pre-trained foundation models, trained on large-scale, high-quality datasets. However, many advanced methods rely on in-house data subject to various constraints, and other current studies fail to generate high-resolution face videos, which is mainly attributed to the significant lack of large-scale, high-quality face video datasets. In this paper, we introduce a human face video dataset, \textbf{DH-FaceVid-1K}. Our collection spans 1,200 hours in total, encompassing 270,043 video clips from over 20,000 individuals. Each sample includes corresponding speech audio, facial keypoints, and text annotations. Compared to other publicly available datasets, ours distinguishes itself through its multi-ethnic coverage and high-quality, comprehensive individual attributes. We establish multiple face video generation models supporting tasks such as text-to-video and image-to-video generation. In addition, we develop comprehensive benchmarks to validate the scaling law when using different proportions of proposed dataset. Our primary aim is to contribute a face video dataset, particularly addressing the underrepresentation of Asian faces in existing curated datasets and thereby enriching the global spectrum of face-centric data and mitigating demographic biases. \textbf{Project Page:} https://luna-ai-lab.github.io/DH-FaceVid-1K/

</details>

### [JEAN: Joint Expression and Audio-guided NeRF-based Talking Face Generation](2409.12156.md)
**Sai Tanmay Reddy Chakkera, Aggelina Chatziagapi, Dimitris Samaras** · 2024-09-18

<details>
<summary>Abstract</summary>

We introduce a novel method for joint expression and audio-guided talking face generation. Recent approaches either struggle to preserve the speaker identity or fail to produce faithful facial expressions. To address these challenges, we propose a NeRF-based network. Since we train our network on monocular videos without any ground truth, it is essential to learn disentangled representations for audio and expression. We first learn audio features in a self-supervised manner, given utterances from multiple subjects. By incorporating a contrastive learning technique, we ensure that the learned audio features are aligned to the lip motion and disentangled from the muscle motion of the rest of the face. We then devise a transformer-based architecture that learns expression features, capturing long-range facial expressions and disentangling them from the speech-specific mouth movements. Through quantitative and qualitative evaluation, we demonstrate that our method can synthesize high-fidelity talking face videos, achieving state-of-the-art facial expression transfer along with lip synchronization to unseen audio.

</details>

### [DreamHead: Learning Spatial-Temporal Correspondence via Hierarchical Diffusion for Audio-driven Talking Head Synthesis](2409.10281.md)
**Fa-Ting Hong, Yunfei Liu, Yu Li, Changyin Zhou et al.** · 2024-09-16

<details>
<summary>Abstract</summary>

Audio-driven talking head synthesis strives to generate lifelike video portraits from provided audio. The diffusion model, recognized for its superior quality and robust generalization, has been explored for this task. However, establishing a robust correspondence between temporal audio cues and corresponding spatial facial expressions with diffusion models remains a significant challenge in talking head generation. To bridge this gap, we present DreamHead, a hierarchical diffusion framework that learns spatial-temporal correspondences in talking head synthesis without compromising the model's intrinsic quality and adaptability.~DreamHead learns to predict dense facial landmarks from audios as intermediate signals to model the spatial and temporal correspondences.~Specifically, a first hierarchy of audio-to-landmark diffusion is first designed to predict temporally smooth and accurate landmark sequences given audio sequence signals. Then, a second hierarchy of landmark-to-image diffusion is further proposed to produce spatially consistent facial portrait videos, by modeling spatial correspondences between the dense facial landmark and appearance. Extensive experiments show that proposed DreamHead can effectively learn spatial-temporal consistency with the designed hierarchical diffusion and produce high-fidelity audio-driven talking head videos for multiple identities.

</details>

### [ProbTalk3D: Non-Deterministic Emotion Controllable Speech-Driven 3D Facial Animation Synthesis Using VQ-VAE](2409.07966.md)
**Sichun Wu, Kazi Injamamul Haque, Zerrin Yumak** · 2024-09-12

<details>
<summary>Abstract</summary>

Audio-driven 3D facial animation synthesis has been an active field of research with attention from both academia and industry. While there are promising results in this area, recent approaches largely focus on lip-sync and identity control, neglecting the role of emotions and emotion control in the generative process. That is mainly due to the lack of emotionally rich facial animation data and algorithms that can synthesize speech animations with emotional expressions at the same time. In addition, majority of the models are deterministic, meaning given the same audio input, they produce the same output motion. We argue that emotions and non-determinism are crucial to generate diverse and emotionally-rich facial animations. In this paper, we propose ProbTalk3D a non-deterministic neural network approach for emotion controllable speech-driven 3D facial animation synthesis using a two-stage VQ-VAE model and an emotionally rich facial animation dataset 3DMEAD. We provide an extensive comparative analysis of our model against the recent 3D facial animation synthesis approaches, by evaluating the results objectively, qualitatively, and with a perceptual user study. We highlight several objective metrics that are more suitable for evaluating stochastic outputs and use both in-the-wild and ground truth data for subjective evaluation. To our knowledge, that is the first non-deterministic 3D facial animation synthesis method incorporating a rich emotion dataset and emotion control with emotion labels and intensity levels. Our evaluation demonstrates that the proposed model achieves superior performance compared to state-of-the-art emotion-controlled, deterministic and non-deterministic models. We recommend watching the supplementary video for quality judgement. The entire codebase is publicly available (https://github.com/uuembodiedsocialai/ProbTalk3D/).

</details>

### [EMOdiffhead: Continuously Emotional Control in Talking Head Generation via Diffusion](2409.07255.md)
**Jian Zhang, Weijian Mai, Zhijun Zhang** · 2024-09-11

<details>
<summary>Abstract</summary>

The task of audio-driven portrait animation involves generating a talking head video using an identity image and an audio track of speech. While many existing approaches focus on lip synchronization and video quality, few tackle the challenge of generating emotion-driven talking head videos. The ability to control and edit emotions is essential for producing expressive and realistic animations. In response to this challenge, we propose EMOdiffhead, a novel method for emotional talking head video generation that not only enables fine-grained control of emotion categories and intensities but also enables one-shot generation. Given the FLAME 3D model's linearity in expression modeling, we utilize the DECA method to extract expression vectors, that are combined with audio to guide a diffusion model in generating videos with precise lip synchronization and rich emotional expressiveness. This approach not only enables the learning of rich facial information from emotion-irrelevant data but also facilitates the generation of emotional videos. It effectively overcomes the limitations of emotional data, such as the lack of diversity in facial and background information, and addresses the absence of emotional details in emotion-irrelevant data. Extensive experiments and user studies demonstrate that our approach achieves state-of-the-art performance compared to other emotion portrait animation methods.

</details>

### [DiffTED: One-shot Audio-driven TED Talk Video Generation with Diffusion-based Co-speech Gestures](2409.07649.md)
**Steven Hogue, Chenxu Zhang, Hamza Daruger, Yapeng Tian et al.** · 2024-09-11

<details>
<summary>Abstract</summary>

Audio-driven talking video generation has advanced significantly, but existing methods often depend on video-to-video translation techniques and traditional generative networks like GANs and they typically generate taking heads and co-speech gestures separately, leading to less coherent outputs. Furthermore, the gestures produced by these methods often appear overly smooth or subdued, lacking in diversity, and many gesture-centric approaches do not integrate talking head generation. To address these limitations, we introduce DiffTED, a new approach for one-shot audio-driven TED-style talking video generation from a single image. Specifically, we leverage a diffusion model to generate sequences of keypoints for a Thin-Plate Spline motion model, precisely controlling the avatar's animation while ensuring temporally coherent and diverse gestures. This innovative approach utilizes classifier-free guidance, empowering the gestures to flow naturally with the audio input without relying on pre-trained classifiers. Experiments demonstrate that DiffTED generates temporally coherent talking videos with diverse co-speech gestures.

</details>

### [SegTalker: Segmentation-based Talking Face Generation with Mask-guided Local Editing](2409.03605.md)
**Lingyu Xiong, Xize Cheng, Jintao Tan, Xianjia Wu et al.** · 2024-09-05

<details>
<summary>Abstract</summary>

Audio-driven talking face generation aims to synthesize video with lip movements synchronized to input audio. However, current generative techniques face challenges in preserving intricate regional textures (skin, teeth). To address the aforementioned challenges, we propose a novel framework called SegTalker to decouple lip movements and image textures by introducing segmentation as intermediate representation. Specifically, given the mask of image employed by a parsing network, we first leverage the speech to drive the mask and generate talking segmentation. Then we disentangle semantic regions of image into style codes using a mask-guided encoder. Ultimately, we inject the previously generated talking segmentation and style codes into a mask-guided StyleGAN to synthesize video frame. In this way, most of textures are fully preserved. Moreover, our approach can inherently achieve background separation and facilitate mask-guided facial local editing. In particular, by editing the mask and swapping the region textures from a given reference image (e.g. hair, lip, eyebrows), our approach enables facial editing seamlessly when generating talking face video. Experiments demonstrate that our proposed approach can effectively preserve texture details and generate temporally consistent video while remaining competitive in lip synchronization. Quantitative and qualitative results on the HDTF and MEAD datasets illustrate the superior performance of our method over existing methods.

</details>

### [SVP: Style-Enhanced Vivid Portrait Talking Head Diffusion Model](2409.03270.md)
**Weipeng Tan, Chuming Lin, Chengming Xu, Xiaozhong Ji et al.** · 2024-09-05

<details>
<summary>Abstract</summary>

Talking Head Generation (THG), typically driven by audio, is an important and challenging task with broad application prospects in various fields such as digital humans, film production, and virtual reality. While diffusion model-based THG methods present high quality and stable content generation, they often overlook the intrinsic style which encompasses personalized features such as speaking habits and facial expressions of a video. As consequence, the generated video content lacks diversity and vividness, thus being limited in real life scenarios. To address these issues, we propose a novel framework named Style-Enhanced Vivid Portrait (SVP) which fully leverages style-related information in THG. Specifically, we first introduce the novel probabilistic style prior learning to model the intrinsic style as a Gaussian distribution using facial expressions and audio embedding. The distribution is learned through the 'bespoked' contrastive objective, effectively capturing the dynamic style information in each video. Then we finetune a pretrained Stable Diffusion (SD) model to inject the learned intrinsic style as a controlling signal via cross attention. Experiments show that our model generates diverse, vivid, and high-quality videos with flexible control over intrinsic styles, outperforming existing state-of-the-art methods.

</details>

### [PoseTalk: Text-and-Audio-based Pose Control and Motion Refinement for One-Shot Talking Head Generation](2409.02657.md)
**Jun Ling, Yiwen Wang, Han Xue, Rong Xie et al.** · 2024-09-04

<details>
<summary>Abstract</summary>

While previous audio-driven talking head generation (THG) methods generate head poses from driving audio, the generated poses or lips cannot match the audio well or are not editable. In this study, we propose \textbf{PoseTalk}, a THG system that can freely generate lip-synchronized talking head videos with free head poses conditioned on text prompts and audio. The core insight of our method is using head pose to connect visual, linguistic, and audio signals. First, we propose to generate poses from both audio and text prompts, where the audio offers short-term variations and rhythm correspondence of the head movements and the text prompts describe the long-term semantics of head motions. To achieve this goal, we devise a Pose Latent Diffusion (PLD) model to generate motion latent from text prompts and audio cues in a pose latent space. Second, we observe a loss-imbalance problem: the loss for the lip region contributes less than 4\% of the total reconstruction loss caused by both pose and lip, making optimization lean towards head movements rather than lip shapes. To address this issue, we propose a refinement-based learning strategy to synthesize natural talking videos using two cascaded networks, i.e., CoarseNet, and RefineNet. The CoarseNet estimates coarse motions to produce animated images in novel poses and the RefineNet focuses on learning finer lip motions by progressively estimating lip motions from low-to-high resolutions, yielding improved lip-synchronization performance. Experiments demonstrate our pose prediction strategy achieves better pose diversity and realness compared to text-only or audio-only, and our video generator model outperforms state-of-the-art methods in synthesizing talking videos with natural head motions. Project: https://junleen.github.io/projects/posetalk.

</details>

### [G3FA: Geometry-guided GAN for Face Animation](2408.13049.md)
**Alireza Javanmardi, Alain Pagani, Didier Stricker** · 2024-08-23

<details>
<summary>Abstract</summary>

Animating human face images aims to synthesize a desired source identity in a natural-looking way mimicking a driving video's facial movements. In this context, Generative Adversarial Networks have demonstrated remarkable potential in real-time face reenactment using a single source image, yet are constrained by limited geometry consistency compared to graphic-based approaches. In this paper, we introduce Geometry-guided GAN for Face Animation (G3FA) to tackle this limitation. Our novel approach empowers the face animation model to incorporate 3D information using only 2D images, improving the image generation capabilities of the talking head synthesis model. We integrate inverse rendering techniques to extract 3D facial geometry properties, improving the feedback loop to the generator through a weighted average ensemble of discriminators. In our face reenactment model, we leverage 2D motion warping to capture motion dynamics along with orthogonal ray sampling and volume rendering techniques to produce the ultimate visual output. To evaluate the performance of our G3FA, we conducted comprehensive experiments using various evaluation protocols on VoxCeleb2 and TalkingHead benchmarks to demonstrate the effectiveness of our proposed framework compared to the state-of-the-art real-time face animation methods.

</details>

### [DEGAS: Detailed Expressions on Full-Body Gaussian Avatars](2408.10588.md)
**Zhijing Shao, Duotun Wang, Qing-Yao Tian, Yao-Dong Yang et al.** · 2024-08-20

<details>
<summary>Abstract</summary>

Although neural rendering has made significant advances in creating lifelike, animatable full-body and head avatars, incorporating detailed expressions into full-body avatars remains largely unexplored. We present DEGAS, the first 3D Gaussian Splatting (3DGS)-based modeling method for full-body avatars with rich facial expressions. Trained on multiview videos of a given subject, our method learns a conditional variational autoencoder that takes both the body motion and facial expression as driving signals to generate Gaussian maps in the UV layout. To drive the facial expressions, instead of the commonly used 3D Morphable Models (3DMMs) in 3D head avatars, we propose to adopt the expression latent space trained solely on 2D portrait images, bridging the gap between 2D talking faces and 3D avatars. Leveraging the rendering capability of 3DGS and the rich expressiveness of the expression latent space, the learned avatars can be reenacted to reproduce photorealistic rendering images with subtle and accurate facial expressions. Experiments on an existing dataset and our newly proposed dataset of full-body talking avatars demonstrate the efficacy of our method. We also propose an audio-driven extension of our method with the help of 2D talking faces, opening new possibilities for interactive AI agents.

</details>

### [S^3D-NeRF: Single-Shot Speech-Driven Neural Radiance Field for High Fidelity Talking Head Synthesis](2408.09347.md)
**Dongze Li, Kang Zhao, Wei Wang, Yifeng Ma et al.** · 2024-08-18

<details>
<summary>Abstract</summary>

Talking head synthesis is a practical technique with wide applications. Current Neural Radiance Field (NeRF) based approaches have shown their superiority on driving one-shot talking heads with videos or signals regressed from audio. However, most of them failed to take the audio as driven information directly, unable to enjoy the flexibility and availability of speech. Since mapping audio signals to face deformation is non-trivial, we design a Single-Shot Speech-Driven Neural Radiance Field (S^3D-NeRF) method in this paper to tackle the following three difficulties: learning a representative appearance feature for each identity, modeling motion of different face regions with audio, and keeping the temporal consistency of the lip area. To this end, we introduce a Hierarchical Facial Appearance Encoder to learn multi-scale representations for catching the appearance of different speakers, and elaborate a Cross-modal Facial Deformation Field to perform speech animation according to the relationship between the audio signal and different face regions. Moreover, to enhance the temporal consistency of the important lip area, we introduce a lip-sync discriminator to penalize the out-of-sync audio-visual sequences. Extensive experiments have shown that our S^3D-NeRF surpasses previous arts on both video fidelity and audio-lip synchronization.

</details>

### [FD2Talk: Towards Generalized Talking Head Generation with Facial Decoupled Diffusion Model](2408.09384.md)
**Ziyu Yao, Xuxin Cheng, Zhiqi Huang** · 2024-08-18

<details>
<summary>Abstract</summary>

Talking head generation is a significant research topic that still faces numerous challenges. Previous works often adopt generative adversarial networks or regression models, which are plagued by generation quality and average facial shape problem. Although diffusion models show impressive generative ability, their exploration in talking head generation remains unsatisfactory. This is because they either solely use the diffusion model to obtain an intermediate representation and then employ another pre-trained renderer, or they overlook the feature decoupling of complex facial details, such as expressions, head poses and appearance textures. Therefore, we propose a Facial Decoupled Diffusion model for Talking head generation called FD2Talk, which fully leverages the advantages of diffusion models and decouples the complex facial details through multi-stages. Specifically, we separate facial details into motion and appearance. In the initial phase, we design the Diffusion Transformer to accurately predict motion coefficients from raw audio. These motions are highly decoupled from appearance, making them easier for the network to learn compared to high-dimensional RGB images. Subsequently, in the second phase, we encode the reference image to capture appearance textures. The predicted facial and head motions and encoded appearance then serve as the conditions for the Diffusion UNet, guiding the frame generation. Benefiting from decoupling facial details and fully leveraging diffusion models, extensive experiments substantiate that our approach excels in enhancing image quality and generating more accurate and diverse results compared to previous state-of-the-art methods.

</details>

### [Meta-Learning Empowered Meta-Face: Personalized Speaking Style Adaptation for Audio-Driven 3D Talking Face Animation](2408.09357.md)
**Xukun Zhou, Fengxin Li, Ziqiao Peng, Kejian Wu et al.** · 2024-08-18

<details>
<summary>Abstract</summary>

Audio-driven 3D face animation is increasingly vital in live streaming and augmented reality applications. While remarkable progress has been observed, most existing approaches are designed for specific individuals with predefined speaking styles, thus neglecting the adaptability to varied speaking styles. To address this limitation, this paper introduces MetaFace, a novel methodology meticulously crafted for speaking style adaptation. Grounded in the novel concept of meta-learning, MetaFace is composed of several key components: the Robust Meta Initialization Stage (RMIS) for fundamental speaking style adaptation, the Dynamic Relation Mining Neural Process (DRMN) for forging connections between observed and unobserved speaking styles, and the Low-rank Matrix Memory Reduction Approach to enhance the efficiency of model optimization as well as learning style details. Leveraging these novel designs, MetaFace not only significantly outperforms robust existing baselines but also establishes a new state-of-the-art, as substantiated by our experimental results.

</details>

### [High-fidelity and Lip-synced Talking Face Synthesis via Landmark-based Diffusion Model](2408.05416.md)
**Weizhi Zhong, Junfan Lin, Peixin Chen, Liang Lin et al.** · 2024-08-10

<details>
<summary>Abstract</summary>

Audio-driven talking face video generation has attracted increasing attention due to its huge industrial potential. Some previous methods focus on learning a direct mapping from audio to visual content. Despite progress, they often struggle with the ambiguity of the mapping process, leading to flawed results. An alternative strategy involves facial structural representations (e.g., facial landmarks) as intermediaries. This multi-stage approach better preserves the appearance details but suffers from error accumulation due to the independent optimization of different stages. Moreover, most previous methods rely on generative adversarial networks, prone to training instability and mode collapse. To address these challenges, our study proposes a novel landmark-based diffusion model for talking face generation, which leverages facial landmarks as intermediate representations while enabling end-to-end optimization. Specifically, we first establish the less ambiguous mapping from audio to landmark motion of lip and jaw. Then, we introduce an innovative conditioning module called TalkFormer to align the synthesized motion with the motion represented by landmarks via differentiable cross-attention, which enables end-to-end optimization for improved lip synchronization. Besides, TalkFormer employs implicit feature warping to align the reference image features with the target motion for preserving more appearance details. Extensive experiments demonstrate that our approach can synthesize high-fidelity and lip-synced talking face videos, preserving more subject appearance details from the reference image.

</details>

### [Style-Preserving Lip Sync via Audio-Aware Style Reference](2408.05412.md)
**Weizhi Zhong, Jichang Li, Yinqi Cai, Ming Li et al.** · 2024-08-10

<details>
<summary>Abstract</summary>

Audio-driven lip sync has recently drawn significant attention due to its widespread application in the multimedia domain. Individuals exhibit distinct lip shapes when speaking the same utterance, attributed to the unique speaking styles of individuals, posing a notable challenge for audio-driven lip sync. Earlier methods for such task often bypassed the modeling of personalized speaking styles, resulting in sub-optimal lip sync conforming to the general styles. Recent lip sync techniques attempt to guide the lip sync for arbitrary audio by aggregating information from a style reference video, yet they can not preserve the speaking styles well due to their inaccuracy in style aggregation. This work proposes an innovative audio-aware style reference scheme that effectively leverages the relationships between input audio and reference audio from style reference video to address the style-preserving audio-driven lip sync. Specifically, we first develop an advanced Transformer-based model adept at predicting lip motion corresponding to the input audio, augmented by the style information aggregated through cross-attention layers from style reference video. Afterwards, to better render the lip motion into realistic talking face video, we devise a conditional latent diffusion model, integrating lip motion through modulated convolutional layers and fusing reference facial images via spatial cross-attention layers. Extensive experiments validate the efficacy of the proposed approach in achieving precise lip sync, preserving speaking styles, and generating high-fidelity, realistic talking face videos.

</details>

### [The DeepSpeak Dataset](2408.05366.md)
**Sarah Barrington, Maty Bohacek, Hany Farid** · 2024-08-09

<details>
<summary>Abstract</summary>

Deepfakes represent a growing concern across domains such as disinformation, fraud, and non-consensual media. In particular, the rise of video conference and identity-driven attacks in high-stakes scenarios--such as impostor hiring--demands new forensic resources. Despite significant efforts to develop robust detection classifiers to distinguish the real from the fake, commonly used training datasets remain inadequate: relying on low-quality and outdated deepfake generators, consisting of content scraped from online repositories without participant consent, lacking in multimodal coverage, and rarely employing identity-matching protocols to ensure realistic fakes. To overcome these limitations, we present the DeepSpeak dataset, a diverse and multimodal dataset comprising over 100 hours of authentic and deepfake audiovisual content, specifically focused on the challenging and diverse talking heads context. We contribute: i) more than 50 hours of real, self-recorded data collected from 500 diverse and consenting participants, ii) more than 50 hours of state-of-the-art audio and visual deepfakes generated using 14 video synthesis engines and three voice cloning engines, and iii) an embedding-based, identity-matching approach to ensure the creation of convincing, high-quality identity face swaps that realistically simulate adversarial deepfake attacks. We also perform large-scale evaluations of state-of-the-art deepfake detectors and show that, without retraining, these detectors fail to generalize to this DeepSpeak dataset, highlighting the importance of a large and diverse dataset containing deepfakes from the latest generative-AI tools.

</details>

### [ReSyncer: Rewiring Style-based Generator for Unified Audio-Visually Synced Facial Performer](2408.03284.md)
**Jiazhi Guan, Zhiliang Xu, Hang Zhou, Kaisiyuan Wang et al.** · 2024-08-06

<details>
<summary>Abstract</summary>

Lip-syncing videos with given audio is the foundation for various applications including the creation of virtual presenters or performers. While recent studies explore high-fidelity lip-sync with different techniques, their task-orientated models either require long-term videos for clip-specific training or retain visible artifacts. In this paper, we propose a unified and effective framework ReSyncer, that synchronizes generalized audio-visual facial information. The key design is revisiting and rewiring the Style-based generator to efficiently adopt 3D facial dynamics predicted by a principled style-injected Transformer. By simply re-configuring the information insertion mechanisms within the noise and style space, our framework fuses motion and appearance with unified training. Extensive experiments demonstrate that ReSyncer not only produces high-fidelity lip-synced videos according to audio, but also supports multiple appealing properties that are suitable for creating virtual presenters and performers, including fast personalized fine-tuning, video-driven lip-syncing, the transfer of speaking styles, and even face swapping. Resources can be found at https://guanjz20.github.io/projects/ReSyncer.

</details>

### [GLDiTalker: Speech-Driven 3D Facial Animation with Graph Latent Diffusion Transformer](2408.01826.md)
**Yihong Lin, Zhaoxin Fan, Xianjia Wu, Lingyu Xiong et al.** · 2024-08-03

<details>
<summary>Abstract</summary>

Speech-driven talking head generation is a critical yet challenging task with applications in augmented reality and virtual human modeling. While recent approaches using autoregressive and diffusion-based models have achieved notable progress, they often suffer from modality inconsistencies, particularly misalignment between audio and mesh, leading to reduced motion diversity and lip-sync accuracy. To address this, we propose GLDiTalker, a novel speech-driven 3D facial animation model based on a Graph Latent Diffusion Transformer. GLDiTalker resolves modality misalignment by diffusing signals within a quantized spatiotemporal latent space. It employs a two-stage training pipeline: the Graph-Enhanced Quantized Space Learning Stage ensures lip-sync accuracy, while the Space-Time Powered Latent Diffusion Stage enhances motion diversity. Together, these stages enable GLDiTalker to generate realistic, temporally stable 3D facial animations. Extensive evaluations on standard benchmarks demonstrate that GLDiTalker outperforms existing methods, achieving superior results in both lip-sync accuracy and motion diversity.

</details>

### [JambaTalk: Speech-Driven 3D Talking Head Generation Based on Hybrid Transformer-Mamba Model](2408.01627.md)
**Farzaneh Jafari, Stefano Berretti, Anup Basu** · 2024-08-03

<details>
<summary>Abstract</summary>

In recent years, the talking head generation has become a focal point for researchers. Considerable effort is being made to refine lip-sync motion, capture expressive facial expressions, generate natural head poses, and achieve high-quality video. However, no single model has yet achieved equivalence across all quantitative and qualitative metrics. We introduce Jamba, a hybrid Transformer-Mamba model, to animate a 3D face. Mamba, a pioneering Structured State Space Model (SSM) architecture, was developed to overcome the limitations of conventional Transformer architectures, particularly in handling long sequences. This challenge has constrained traditional models. Jamba combines the advantages of both the Transformer and Mamba approaches, offering a comprehensive solution. Based on the foundational Jamba block, we present JambaTalk to enhance motion variety and lip sync through multimodal integration. Extensive experiments reveal that our method achieves performance comparable or superior to state-of-the-art models.

</details>

### [Landmark-guided Diffusion Model for High-fidelity and Temporally Coherent Talking Head Generation](2408.01732.md)
**Jintao Tan, Xize Cheng, Lingyu Xiong, Lei Zhu et al.** · 2024-08-03

<details>
<summary>Abstract</summary>

Audio-driven talking head generation is a significant and challenging task applicable to various fields such as virtual avatars, film production, and online conferences. However, the existing GAN-based models emphasize generating well-synchronized lip shapes but overlook the visual quality of generated frames, while diffusion-based models prioritize generating high-quality frames but neglect lip shape matching, resulting in jittery mouth movements. To address the aforementioned problems, we introduce a two-stage diffusion-based model. The first stage involves generating synchronized facial landmarks based on the given speech. In the second stage, these generated landmarks serve as a condition in the denoising process, aiming to optimize mouth jitter issues and generate high-fidelity, well-synchronized, and temporally coherent talking head videos. Extensive experiments demonstrate that our model yields the best performance.

</details>

### [LinguaLinker: Audio-Driven Portraits Animation with Implicit Facial Control Enhancement](2407.18595.md)
**Rui Zhang, Yixiao Fang, Zhengnan Lu, Pei Cheng et al.** · 2024-07-26

<details>
<summary>Abstract</summary>

This study delves into the intricacies of synchronizing facial dynamics with multilingual audio inputs, focusing on the creation of visually compelling, time-synchronized animations through diffusion-based techniques. Diverging from traditional parametric models for facial animation, our approach, termed LinguaLinker, adopts a holistic diffusion-based framework that integrates audio-driven visual synthesis to enhance the synergy between auditory stimuli and visual responses. We process audio features separately and derive the corresponding control gates, which implicitly govern the movements in the mouth, eyes, and head, irrespective of the portrait's origin. The advanced audio-driven visual synthesis mechanism provides nuanced control but keeps the compatibility of output video and input audio, allowing for a more tailored and effective portrayal of distinct personas across different languages. The significant improvements in the fidelity of animated portraits, the accuracy of lip-syncing, and the appropriate motion variations achieved by our method render it a versatile tool for animating any portrait in any language.

</details>

### [PAV: Personalized Head Avatar from Unstructured Video Collection](2407.21047.md)
**Akin Caliskan, Berkay Kicanaoglu, Hyeongwoo Kim** · 2024-07-22

<details>
<summary>Abstract</summary>

We propose PAV, Personalized Head Avatar for the synthesis of human faces under arbitrary viewpoints and facial expressions. PAV introduces a method that learns a dynamic deformable neural radiance field (NeRF), in particular from a collection of monocular talking face videos of the same character under various appearance and shape changes. Unlike existing head NeRF methods that are limited to modeling such input videos on a per-appearance basis, our method allows for learning multi-appearance NeRFs, introducing appearance embedding for each input video via learnable latent neural features attached to the underlying geometry. Furthermore, the proposed appearance-conditioned density formulation facilitates the shape variation of the character, such as facial hair and soft tissues, in the radiance field prediction. To the best of our knowledge, our approach is the first dynamic deformable NeRF framework to model appearance and shape variations in a single unified network for multi-appearances of the same subject. We demonstrate experimentally that PAV outperforms the baseline method in terms of visual rendering quality in our quantitative and qualitative studies on various subjects.

</details>

### [Anchored Diffusion for Video Face Reenactment](2407.15153.md)
**Idan Kligvasser, Regev Cohen, George Leifman, Ehud Rivlin et al.** · 2024-07-21

<details>
<summary>Abstract</summary>

Video generation has drawn significant interest recently, pushing the development of large-scale models capable of producing realistic videos with coherent motion. Due to memory constraints, these models typically generate short video segments that are then combined into long videos. The merging process poses a significant challenge, as it requires ensuring smooth transitions and overall consistency. In this paper, we introduce Anchored Diffusion, a novel method for synthesizing relatively long and seamless videos. We extend Diffusion Transformers (DiTs) to incorporate temporal information, creating our sequence-DiT (sDiT) model for generating short video segments. Unlike previous works, we train our model on video sequences with random non-uniform temporal spacing and incorporate temporal information via external guidance, increasing flexibility and allowing it to capture both short and long-term relationships. Furthermore, during inference, we leverage the transformer architecture to modify the diffusion process, generating a batch of non-uniform sequences anchored to a common frame, ensuring consistency regardless of temporal distance. To demonstrate our method, we focus on face reenactment, the task of creating a video from a source image that replicates the facial expressions and movements from a driving video. Through comprehensive experiments, we show our approach outperforms current techniques in producing longer consistent high-quality videos while offering editing capabilities.

</details>

### [Text-based Talking Video Editing with Cascaded Conditional Diffusion](2407.14841.md)
**Bo Han, Heqing Zou, Haoyang Li, Guangcong Wang et al.** · 2024-07-20

<details>
<summary>Abstract</summary>

Text-based talking-head video editing aims to efficiently insert, delete, and substitute segments of talking videos through a user-friendly text editing approach. It is challenging because of \textbf{1)} generalizable talking-face representation, \textbf{2)} seamless audio-visual transitions, and \textbf{3)} identity-preserved talking faces. Previous works either require minutes of talking-face video training data and expensive test-time optimization for customized talking video editing or directly generate a video sequence without considering in-context information, leading to a poor generalizable representation, or incoherent transitions, or even inconsistent identity. In this paper, we propose an efficient cascaded conditional diffusion-based framework, which consists of two stages: audio to dense-landmark motion and motion to video. \textit{\textbf{In the first stage}}, we first propose a dynamic weighted in-context diffusion module to synthesize dense-landmark motions given an edited audio. \textit{\textbf{In the second stage}}, we introduce a warping-guided conditional diffusion module. The module first interpolates between the start and end frames of the editing interval to generate smooth intermediate frames. Then, with the help of the audio-to-dense motion images, these intermediate frames are warped to obtain coarse intermediate frames. Conditioned on the warped intermedia frames, a diffusion model is adopted to generate detailed and high-resolution target frames, which guarantees coherent and identity-preserved transitions. The cascaded conditional diffusion model decomposes the complex talking editing task into two flexible generation tasks, which provides a generalizable talking-face representation, seamless audio-visual transitions, and identity-preserved faces on a small dataset. Experiments show the effectiveness and superiority of the proposed method.

</details>

### [RT-LA-VocE: Real-Time Low-SNR Audio-Visual Speech Enhancement](2407.07825.md)
**Honglie Chen, Rodrigo Mira, Stavros Petridis, Maja Pantic** · 2024-07-10

<details>
<summary>Abstract</summary>

In this paper, we aim to generate clean speech frame by frame from a live video stream and a noisy audio stream without relying on future inputs. To this end, we propose RT-LA-VocE, which completely re-designs every component of LA-VocE, a state-of-the-art non-causal audio-visual speech enhancement model, to perform causal real-time inference with a 40ms input frame. We do so by devising new visual and audio encoders that rely solely on past frames, replacing the Transformer encoder with the Emformer, and designing a new causal neural vocoder C-HiFi-GAN. On the popular AVSpeech dataset, we show that our algorithm achieves state-of-the-art results in all real-time scenarios. More importantly, each component is carefully tuned to minimize the algorithm latency to the theoretical minimum (40ms) while maintaining a low end-to-end processing latency of 28.15ms per frame, enabling real-time frame-by-frame enhancement with minimal delay.

</details>

### [Audio-driven High-resolution Seamless Talking Head Video Editing via StyleGAN](2407.05577.md)
**Jiacheng Su, Kunhong Liu, Liyan Chen, Junfeng Yao et al.** · 2024-07-08

<details>
<summary>Abstract</summary>

The existing methods for audio-driven talking head video editing have the limitations of poor visual effects. This paper tries to tackle this problem through editing talking face images seamless with different emotions based on two modules: (1) an audio-to-landmark module, consisting of the CrossReconstructed Emotion Disentanglement and an alignment network module. It bridges the gap between speech and facial motions by predicting corresponding emotional landmarks from speech; (2) a landmark-based editing module edits face videos via StyleGAN. It aims to generate the seamless edited video consisting of the emotion and content components from the input audio. Extensive experiments confirm that compared with state-of-the-arts methods, our method provides high-resolution videos with high visual quality.

</details>

### [Enhancing Speech-Driven 3D Facial Animation with Audio-Visual Guidance from Lip Reading Expert](2407.01034.md)
**Han EunGi, Oh Hyun-Bin, Kim Sung-Bin, Corentin Nivelet Etcheberry et al.** · 2024-07-01

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation has recently garnered attention due to its cost-effective usability in multimedia production. However, most current advances overlook the intelligibility of lip movements, limiting the realism of facial expressions. In this paper, we introduce a method for speech-driven 3D facial animation to generate accurate lip movements, proposing an audio-visual multimodal perceptual loss. This loss provides guidance to train the speech-driven 3D facial animators to generate plausible lip motions aligned with the spoken transcripts. Furthermore, to incorporate the proposed audio-visual perceptual loss, we devise an audio-visual lip reading expert leveraging its prior knowledge about correlations between speech and lip motions. We validate the effectiveness of our approach through broad experiments, showing noticeable improvements in lip synchronization and lip readability performance. Codes are available at https://3d-talking-head-avguide.github.io/.

</details>

### [Editing Audio-Driven Talking Head Based on Audio Information](s2:6ec08eb464be74f258806ba9ab499abfdb041150.md)
**Rui Lang** · 2024-06-30

<details>
<summary>Abstract</summary>

Editing audio-driven talking head is a relatively new direction in the field of computer vision and still faces many challenges. First, the existing methods do not fully take into account the information contained in the driving audio, which can easily lead to the problem of mismatch between audio and video features (for example, the driving audio emotion is happy, but the corresponding facial emotion is calm). Second, existing face editing methods are often limited to one mode, and the variety they can produce is limited. Finally, we would like the final generated facial animation to be undistorted and to retain some of the identity of the original image. To address the above problems, this paper proposes a novel talking head editing method based on audio information. Specifically, we obtain comprehensive audio information by introducing multiple audio feature classifiers and use it to guide facial editing. We generate more diverse and detailed facial features by combining two different dimensional face editors. To ensure that the edited face retains as much of its original identity features as possible, we use a 3D head model to drive a single image, rather than introducing latent space or establishing complex cross-modal associations between audio and video frames, which can easily lead to facial distortion. Extensive experiments demonstrate the superiority of our method for audio-driven talking head editing. Please go to the link below to view detailed video results: https://drive.google.com/drive/folders/10T1nIktZciG6Cih_UEUOrg0YKXG6KM-C?usp=sharing

</details>

### [RealTalk: Real-time and Realistic Audio-driven Face Generation with 3D Facial Prior-guided Identity Alignment Network](2406.18284.md)
**Xiaozhong Ji, Chuming Lin, Zhonggan Ding, Ying Tai et al.** · 2024-06-26

<details>
<summary>Abstract</summary>

Person-generic audio-driven face generation is a challenging task in computer vision. Previous methods have achieved remarkable progress in audio-visual synchronization, but there is still a significant gap between current results and practical applications. The challenges are two-fold: 1) Preserving unique individual traits for achieving high-precision lip synchronization. 2) Generating high-quality facial renderings in real-time performance. In this paper, we propose a novel generalized audio-driven framework RealTalk, which consists of an audio-to-expression transformer and a high-fidelity expression-to-face renderer. In the first component, we consider both identity and intra-personal variation features related to speaking lip movements. By incorporating cross-modal attention on the enriched facial priors, we can effectively align lip movements with audio, thus attaining greater precision in expression prediction. In the second component, we design a lightweight facial identity alignment (FIA) module which includes a lip-shape control structure and a face texture reference structure. This novel design allows us to generate fine details in real-time, without depending on sophisticated and inefficient feature alignment modules. Our experimental results, both quantitative and qualitative, on public datasets demonstrate the clear advantages of our method in terms of lip-speech synchronization and generation quality. Furthermore, our method is efficient and requires fewer computational resources, making it well-suited to meet the needs of practical applications.

</details>

### [NLDF: Neural Light Dynamic Fields for Efficient 3D Talking Head Generation](2406.11259.md)
**Niu Guanchen** · 2024-06-17

<details>
<summary>Abstract</summary>

Talking head generation based on the neural radiation fields model has shown promising visual effects. However, the slow rendering speed of NeRF seriously limits its application, due to the burdensome calculation process over hundreds of sampled points to synthesize one pixel. In this work, a novel Neural Light Dynamic Fields model is proposed aiming to achieve generating high quality 3D talking face with significant speedup. The NLDF represents light fields based on light segments, and a deep network is used to learn the entire light beam's information at once. In learning the knowledge distillation is applied and the NeRF based synthesized result is used to guide the correct coloration of light segments in NLDF. Furthermore, a novel active pool training strategy is proposed to focus on high frequency movements, particularly on the speaker mouth and eyebrows. The propose method effectively represents the facial light dynamics in 3D talking video generation, and it achieves approximately 30 times faster speed compared to state of the art NeRF based method, with comparable generation visual quality.

</details>

### [A Comprehensive Taxonomy and Analysis of Talking Head Synthesis: Techniques for Portrait Generation, Driving Mechanisms, and Editing](2406.10553.md)
**Ming Meng, Yufei Zhao, Bo Zhang, Yonggui Zhu et al.** · 2024-06-15

<details>
<summary>Abstract</summary>

Talking head synthesis, an advanced method for generating portrait videos from a still image driven by specific content, has garnered widespread attention in virtual reality, augmented reality and game production. Recently, significant breakthroughs have been made with the introduction of novel models such as the transformer and the diffusion model. Current methods can not only generate new content but also edit the generated material. This survey systematically reviews the technology, categorizing it into three pivotal domains: portrait generation, driven mechanisms, and editing techniques. We summarize milestone studies and critically analyze their innovations and shortcomings within each domain. Additionally, we organize an extensive collection of datasets and provide a thorough performance analysis of current methodologies based on various evaluation metrics, aiming to furnish a clear framework and robust data support for future research. Finally, we explore application scenarios of talking head synthesis, illustrate them with specific cases, and examine potential future directions.

</details>

### [Hallo: Hierarchical Audio-Driven Visual Synthesis for Portrait Image Animation](2406.08801.md)
**Mingwang Xu, Hui Li, Qingkun Su, Hanlin Shang et al.** · 2024-06-13

<details>
<summary>Abstract</summary>

The field of portrait image animation, driven by speech audio input, has experienced significant advancements in the generation of realistic and dynamic portraits. This research delves into the complexities of synchronizing facial movements and creating visually appealing, temporally consistent animations within the framework of diffusion-based methodologies. Moving away from traditional paradigms that rely on parametric models for intermediate facial representations, our innovative approach embraces the end-to-end diffusion paradigm and introduces a hierarchical audio-driven visual synthesis module to enhance the precision of alignment between audio inputs and visual outputs, encompassing lip, expression, and pose motion. Our proposed network architecture seamlessly integrates diffusion-based generative models, a UNet-based denoiser, temporal alignment techniques, and a reference network. The proposed hierarchical audio-driven visual synthesis offers adaptive control over expression and pose diversity, enabling more effective personalization tailored to different identities. Through a comprehensive evaluation that incorporates both qualitative and quantitative analyses, our approach demonstrates obvious enhancements in image and video quality, lip synchronization precision, and motion diversity. Further visualization and access to the source code can be found at: https://fudan-generative-vision.github.io/hallo.

</details>

### [FlowAVSE: Efficient Audio-Visual Speech Enhancement with Conditional Flow Matching](2406.09286.md)
**Chaeyoung Jung, Suyeon Lee, Ji-Hoon Kim, Joon Son Chung** · 2024-06-13

<details>
<summary>Abstract</summary>

This work proposes an efficient method to enhance the quality of corrupted speech signals by leveraging both acoustic and visual cues. While existing diffusion-based approaches have demonstrated remarkable quality, their applicability is limited by slow inference speeds and computational complexity. To address this issue, we present FlowAVSE which enhances the inference speed and reduces the number of learnable parameters without degrading the output quality. In particular, we employ a conditional flow matching algorithm that enables the generation of high-quality speech in a single sampling step. Moreover, we increase efficiency by optimizing the underlying U-net architecture of diffusion-based systems. Our experiments demonstrate that FlowAVSE achieves 22 times faster inference speed and reduces the model size by half while maintaining the output quality. The demo page is available at: https://cyongong.github.io/FlowAVSE.github.io/

</details>

### [Make Your Actor Talk: Generalizable and High-Fidelity Lip Sync with Motion and Appearance Disentanglement](2406.08096.md)
**Runyi Yu, Tianyu He, Ailing Zhang, Yuchi Wang et al.** · 2024-06-12

<details>
<summary>Abstract</summary>

We aim to edit the lip movements in talking video according to the given speech while preserving the personal identity and visual details. The task can be decomposed into two sub-problems: (1) speech-driven lip motion generation and (2) visual appearance synthesis. Current solutions handle the two sub-problems within a single generative model, resulting in a challenging trade-off between lip-sync quality and visual details preservation. Instead, we propose to disentangle the motion and appearance, and then generate them one by one with a speech-to-motion diffusion model and a motion-conditioned appearance generation model. However, there still remain challenges in each stage, such as motion-aware identity preservation in (1) and visual details preservation in (2). Therefore, to preserve personal identity, we adopt landmarks to represent the motion, and further employ a landmark-based identity loss. To capture motion-agnostic visual details, we use separate encoders to encode the lip, non-lip appearance and motion, and then integrate them with a learned fusion module. We train MyTalk on a large-scale and diverse dataset. Experiments show that our method generalizes well to the unknown, even out-of-domain person, in terms of both lip sync and visual detail preservation. We encourage the readers to watch the videos on our project page (https://Ingrid789.github.io/MyTalk/).

</details>

### [Emotional Conversation: Empowering Talking Faces with Cohesive Expression, Gaze and Pose Generation](2406.07895.md)
**Jiadong Liang, Feng Lu** · 2024-06-12

<details>
<summary>Abstract</summary>

Vivid talking face generation holds immense potential applications across diverse multimedia domains, such as film and game production. While existing methods accurately synchronize lip movements with input audio, they typically ignore crucial alignments between emotion and facial cues, which include expression, gaze, and head pose. These alignments are indispensable for synthesizing realistic videos. To address these issues, we propose a two-stage audio-driven talking face generation framework that employs 3D facial landmarks as intermediate variables. This framework achieves collaborative alignment of expression, gaze, and pose with emotions through self-supervised learning. Specifically, we decompose this task into two key steps, namely speech-to-landmarks synthesis and landmarks-to-face generation. The first step focuses on simultaneously synthesizing emotionally aligned facial cues, including normalized landmarks that represent expressions, gaze, and head pose. These cues are subsequently reassembled into relocated facial landmarks. In the second step, these relocated landmarks are mapped to latent key points using self-supervised learning and then input into a pretrained model to create high-quality face images. Extensive experiments on the MEAD dataset demonstrate that our model significantly advances the state-of-the-art performance in both visual quality and emotional alignment.

</details>

### [Let's Go Real Talk: Spoken Dialogue Model for Face-to-Face Conversation](2406.07867.md)
**Se Jin Park, Chae Won Kim, Hyeongseop Rha, Minsu Kim et al.** · 2024-06-12

<details>
<summary>Abstract</summary>

In this paper, we introduce a novel Face-to-Face spoken dialogue model. It processes audio-visual speech from user input and generates audio-visual speech as the response, marking the initial step towards creating an avatar chatbot system without relying on intermediate text. To this end, we newly introduce MultiDialog, the first large-scale multimodal (i.e., audio and visual) spoken dialogue corpus containing 340 hours of approximately 9,000 dialogues, recorded based on the open domain dialogue dataset, TopicalChat. The MultiDialog contains parallel audio-visual recordings of conversation partners acting according to the given script with emotion annotations, which we expect to open up research opportunities in multimodal synthesis. Our Face-to-Face spoken dialogue model incorporates a textually pretrained large language model and adapts it into the audio-visual spoken dialogue domain by incorporating speech-text joint pretraining. Through extensive experiments, we validate the effectiveness of our model in facilitating a face-to-face conversation. Demo and data are available at https://multidialog.github.io and https://huggingface.co/datasets/IVLLab/MultiDialog, respectively.

</details>

### [Audio2Rig: Artist-oriented deep learning tool for facial animation](2405.20412.md)
**Bastien Arcelin, Nicolas Chaverou** · 2024-05-30

<details>
<summary>Abstract</summary>

Creating realistic or stylized facial and lip sync animation is a tedious task. It requires lot of time and skills to sync the lips with audio and convey the right emotion to the character's face. To allow animators to spend more time on the artistic and creative part of the animation, we present Audio2Rig: a new deep learning based tool leveraging previously animated sequences of a show, to generate facial and lip sync rig animation from an audio file. Based in Maya, it learns from any production rig without any adjustment and generates high quality and stylized animations which mimic the style of the show. Audio2Rig fits in the animator workflow: since it generates keys on the rig controllers, the animation can be easily retaken. The method is based on 3 neural network modules which can learn an arbitrary number of controllers. Hence, different configurations can be created for specific parts of the face (such as the tongue, lips or eyes). With Audio2Rig, animators can also pick different emotions and adjust their intensities to experiment or customize the output, and have high level controls on the keyframes setting. Our method shows excellent results, generating fine animation details while respecting the show style. Finally, as the training relies on the studio data and is done internally, it ensures data privacy and prevents from copyright infringement.

</details>

### [EAT-Face: Emotion-Controllable Audio-Driven Talking Face Generation via Diffusion Model](s2:7b142d08b1319ab1d759083ff65b153400c907cb.md)
**Haodi Wang, Xiaojun Jia, Xiaochun Cao** · 2024-05-27

<details>
<summary>Abstract</summary>

Audio-driven talking face generation is a promising task with a lot of attention. Despite abundant efforts are devoted to video quality and lip synchronization, most existing works do not take the unignorable aspect of facial emotional expression into account during generation. In this paper, we propose an Emotion-controllable Audio-driven Talking Face generation framework called EAT-Face that enables us to control multiple types of emotions. Specifically, the proposed method consists of a Talking Face Reconstructor (TFR) and a Facial Emotion Controller (FEC), utilizing fused multimodal information including audio signals, visual images, and textual emotions for synthesis. Firstly, TFR predicts face images synchronized with given audios from random noises, leveraging external guidances comprised of audio features, character references, and face masks as conditions. Then, FEC further manipulates the facial emotions based on TFR, leveraging the emotion embeddings extracted from emotion texts. However, a semantic misalignment problem lies in the emotion-texts and character images. To tackle this issue, we additionally propose a strategy called joint Emotion-Visual Embedding (EVE) to mitigate the misalignment. In this way, the proposed EAT-Face is captive to control emotion more precisely. Extensive experiments involving both objective evaluations and subjective investigations demonstrate the effectiveness of our framework in synthesizing high-fidelity and emotional talking face videos.

</details>

### [InstructAvatar: Text-Guided Emotion and Motion Control for Avatar Generation](2405.15758.md)
**Yuchi Wang, Junliang Guo, Jianhong Bai, Runyi Yu et al.** · 2024-05-24

<details>
<summary>Abstract</summary>

Recent talking avatar generation models have made strides in achieving realistic and accurate lip synchronization with the audio, but often fall short in controlling and conveying detailed expressions and emotions of the avatar, making the generated video less vivid and controllable. In this paper, we propose a novel text-guided approach for generating emotionally expressive 2D avatars, offering fine-grained control, improved interactivity, and generalizability to the resulting video. Our framework, named InstructAvatar, leverages a natural language interface to control the emotion as well as the facial motion of avatars. Technically, we design an automatic annotation pipeline to construct an instruction-video paired training dataset, equipped with a novel two-branch diffusion-based generator to predict avatars with audio and text instructions at the same time. Experimental results demonstrate that InstructAvatar produces results that align well with both conditions, and outperforms existing methods in fine-grained emotion control, lip-sync quality, and naturalness. Our project page is https://wangyuchi369.github.io/InstructAvatar/.

</details>

### [OpFlowTalker: Realistic and Natural Talking Face Generation via Optical Flow Guidance](2405.14709.md)
**Shuheng Ge, Haoyu Xing, Li Zhang, Xiangqian Wu** · 2024-05-23

<details>
<summary>Abstract</summary>

Creating realistic, natural, and lip-readable talking face videos remains a formidable challenge. Previous research primarily concentrated on generating and aligning single-frame images while overlooking the smoothness of frame-to-frame transitions and temporal dependencies. This often compromised visual quality and effects in practical settings, particularly when handling complex facial data and audio content, which frequently led to semantically incongruent visual illusions. Specifically, synthesized videos commonly featured disorganized lip movements, making them difficult to understand and recognize. To overcome these limitations, this paper introduces the application of optical flow to guide facial image generation, enhancing inter-frame continuity and semantic consistency. We propose "OpFlowTalker", a novel approach that utilizes predicted optical flow changes from audio inputs rather than direct image predictions. This method smooths image transitions and aligns changes with semantic content. Moreover, it employs a sequence fusion technique to replace the independent generation of single frames, thus preserving contextual information and maintaining temporal coherence. We also developed an optical flow synchronization module that regulates both full-face and lip movements, optimizing visual synthesis by balancing regional dynamics. Furthermore, we introduce a Visual Text Consistency Score (VTCS) that accurately measures lip-readability in synthesized videos. Extensive empirical evidence validates the effectiveness of our approach.

</details>

### [Face Adapter for Pre-Trained Diffusion Models with Fine-Grained ID and Attribute Control](2405.12970.md)
**Yue Han, Junwei Zhu, Keke He, Xu Chen et al.** · 2024-05-21

<details>
<summary>Abstract</summary>

Current face reenactment and swapping methods mainly rely on GAN frameworks, but recent focus has shifted to pre-trained diffusion models for their superior generation capabilities. However, training these models is resource-intensive, and the results have not yet achieved satisfactory performance levels. To address this issue, we introduce Face-Adapter, an efficient and effective adapter designed for high-precision and high-fidelity face editing for pre-trained diffusion models. We observe that both face reenactment/swapping tasks essentially involve combinations of target structure, ID and attribute. We aim to sufficiently decouple the control of these factors to achieve both tasks in one model. Specifically, our method contains: 1) A Spatial Condition Generator that provides precise landmarks and background; 2) A Plug-and-play Identity Encoder that transfers face embeddings to the text space by a transformer decoder. 3) An Attribute Controller that integrates spatial conditions and detailed attributes. Face-Adapter achieves comparable or even superior performance in terms of motion control precision, ID retention capability, and generation quality compared to fully fine-tuned face reenactment/swapping models. Additionally, Face-Adapter seamlessly integrates with various StableDiffusion models.

</details>

### [Faces that Speak: Jointly Synthesising Talking Face and Speech from Text](2405.10272.md)
**Youngjoon Jang, Ji-Hoon Kim, Junseok Ahn, Doyeop Kwak et al.** · 2024-05-16

<details>
<summary>Abstract</summary>

The goal of this work is to simultaneously generate natural talking faces and speech outputs from text. We achieve this by integrating Talking Face Generation (TFG) and Text-to-Speech (TTS) systems into a unified framework. We address the main challenges of each task: (1) generating a range of head poses representative of real-world scenarios, and (2) ensuring voice consistency despite variations in facial motion for the same identity. To tackle these issues, we introduce a motion sampler based on conditional flow matching, which is capable of high-quality motion code generation in an efficient way. Moreover, we introduce a novel conditioning method for the TTS system, which utilises motion-removed features from the TFG model to yield uniform speech outputs. Our extensive experiments demonstrate that our method effectively creates natural-looking talking faces and speech that accurately match the input text. To our knowledge, this is the first effort to build a multimodal synthesis system that can generalise to unseen identities.

</details>

### [NeRFFaceSpeech: One-shot Audio-driven 3D Talking Head Synthesis via Generative Prior](2405.05749.md)
**Gihoon Kim, Kwanggyoon Seo, Sihun Cha, Junyong Noh** · 2024-05-09

<details>
<summary>Abstract</summary>

Audio-driven talking head generation is advancing from 2D to 3D content. Notably, Neural Radiance Field (NeRF) is in the spotlight as a means to synthesize high-quality 3D talking head outputs. Unfortunately, this NeRF-based approach typically requires a large number of paired audio-visual data for each identity, thereby limiting the scalability of the method. Although there have been attempts to generate audio-driven 3D talking head animations with a single image, the results are often unsatisfactory due to insufficient information on obscured regions in the image. In this paper, we mainly focus on addressing the overlooked aspect of 3D consistency in the one-shot, audio-driven domain, where facial animations are synthesized primarily in front-facing perspectives. We propose a novel method, NeRFFaceSpeech, which enables to produce high-quality 3D-aware talking head. Using prior knowledge of generative models combined with NeRF, our method can craft a 3D-consistent facial feature space corresponding to a single image. Our spatial synchronization method employs audio-correlated vertex dynamics of a parametric face model to transform static image features into dynamic visuals through ray deformation, ensuring realistic 3D facial motion. Moreover, we introduce LipaintNet that can replenish the lacking information in the inner-mouth area, which can not be obtained from a given single image. The network is trained in a self-supervised manner by utilizing the generative capabilities without additional data. The comprehensive experiments demonstrate the superiority of our method in generating audio-driven talking heads from a single image with enhanced 3D consistency compared to previous approaches. In addition, we introduce a quantitative way of measuring the robustness of a model against pose changes for the first time, which has been possible only qualitatively.

</details>

### [AniTalker: Animate Vivid and Diverse Talking Faces through Identity-Decoupled Facial Motion Encoding](2405.03121.md)
**Tao Liu, Feilong Chen, Shuai Fan, Chenpeng Du et al.** · 2024-05-06

<details>
<summary>Abstract</summary>

The paper introduces AniTalker, an innovative framework designed to generate lifelike talking faces from a single portrait. Unlike existing models that primarily focus on verbal cues such as lip synchronization and fail to capture the complex dynamics of facial expressions and nonverbal cues, AniTalker employs a universal motion representation. This innovative representation effectively captures a wide range of facial dynamics, including subtle expressions and head movements. AniTalker enhances motion depiction through two self-supervised learning strategies: the first involves reconstructing target video frames from source frames within the same identity to learn subtle motion representations, and the second develops an identity encoder using metric learning while actively minimizing mutual information between the identity and motion encoders. This approach ensures that the motion representation is dynamic and devoid of identity-specific details, significantly reducing the need for labeled data. Additionally, the integration of a diffusion model with a variance adapter allows for the generation of diverse and controllable facial animations. This method not only demonstrates AniTalker's capability to create detailed and realistic facial movements but also underscores its potential in crafting dynamic avatars for real-world applications. Synthetic results can be viewed at https://github.com/X-LANCE/AniTalker.

</details>

### [Embedded Representation Learning Network for Animating Styled Video Portrait](2404.19038.md)
**Tianyong Wang, Xiangyu Liang, Wangguandong Zheng, Dan Niu et al.** · 2024-04-29

<details>
<summary>Abstract</summary>

The talking head generation recently attracted considerable attention due to its widespread application prospects, especially for digital avatars and 3D animation design. Inspired by this practical demand, several works explored Neural Radiance Fields (NeRF) to synthesize the talking heads. However, these methods based on NeRF face two challenges: (1) Difficulty in generating style-controllable talking heads. (2) Displacement artifacts around the neck in rendered images. To overcome these two challenges, we propose a novel generative paradigm \textit{Embedded Representation Learning Network} (ERLNet) with two learning stages. First, the \textit{ audio-driven FLAME} (ADF) module is constructed to produce facial expression and head pose sequences synchronized with content audio and style video. Second, given the sequence deduced by the ADF, one novel \textit{dual-branch fusion NeRF} (DBF-NeRF) explores these contents to render the final images. Extensive empirical studies demonstrate that the collaboration of these two stages effectively facilitates our method to render a more realistic talking head than the existing algorithms.

</details>

### [GaussianTalker: Speaker-specific Talking Head Synthesis via 3D Gaussian Splatting](2404.14037.md)
**Hongyun Yu, Zhan Qu, Qihang Yu, Jianchuan Chen et al.** · 2024-04-22

<details>
<summary>Abstract</summary>

Recent works on audio-driven talking head synthesis using Neural Radiance Fields (NeRF) have achieved impressive results. However, due to inadequate pose and expression control caused by NeRF implicit representation, these methods still have some limitations, such as unsynchronized or unnatural lip movements, and visual jitter and artifacts. In this paper, we propose GaussianTalker, a novel method for audio-driven talking head synthesis based on 3D Gaussian Splatting. With the explicit representation property of 3D Gaussians, intuitive control of the facial motion is achieved by binding Gaussians to 3D facial models. GaussianTalker consists of two modules, Speaker-specific Motion Translator and Dynamic Gaussian Renderer. Speaker-specific Motion Translator achieves accurate lip movements specific to the target speaker through universalized audio feature extraction and customized lip motion generation. Dynamic Gaussian Renderer introduces Speaker-specific BlendShapes to enhance facial detail representation via a latent pose, delivering stable and realistic rendered videos. Extensive experimental results suggest that GaussianTalker outperforms existing state-of-the-art methods in talking head synthesis, delivering precise lip synchronization and exceptional visual quality. Our method achieves rendering speeds of 130 FPS on NVIDIA RTX4090 GPU, significantly exceeding the threshold for real-time rendering performance, and can potentially be deployed on other hardware platforms.

</details>

### [FSRT: Facial Scene Representation Transformer for Face Reenactment from Factorized Appearance, Head-pose, and Facial Expression Features](2404.09736.md)
**Andre Rochow, Max Schwarz, Sven Behnke** · 2024-04-15

<details>
<summary>Abstract</summary>

The task of face reenactment is to transfer the head motion and facial expressions from a driving video to the appearance of a source image, which may be of a different person (cross-reenactment). Most existing methods are CNN-based and estimate optical flow from the source image to the current driving frame, which is then inpainted and refined to produce the output animation. We propose a transformer-based encoder for computing a set-latent representation of the source image(s). We then predict the output color of a query pixel using a transformer-based decoder, which is conditioned with keypoints and a facial expression vector extracted from the driving frame. Latent representations of the source person are learned in a self-supervised manner that factorize their appearance, head pose, and facial expressions. Thus, they are perfectly suited for cross-reenactment. In contrast to most related work, our method naturally extends to multiple source images and can thus adapt to person-specific facial dynamics. We also propose data augmentation and regularization schemes that are necessary to prevent overfitting and support generalizability of the learned representations. We evaluated our approach in a randomized user study. The results indicate superior performance compared to the state-of-the-art in terms of motion transfer quality and temporal consistency.

</details>

### [Talk3D: High-Fidelity Talking Portrait Synthesis via Personalized 3D Generative Prior](2403.20153.md)
**Jaehoon Ko, Kyusun Cho, Joungbin Lee, Heeji Yoon et al.** · 2024-03-29

<details>
<summary>Abstract</summary>

Recent methods for audio-driven talking head synthesis often optimize neural radiance fields (NeRF) on a monocular talking portrait video, leveraging its capability to render high-fidelity and 3D-consistent novel-view frames. However, they often struggle to reconstruct complete face geometry due to the absence of comprehensive 3D information in the input monocular videos. In this paper, we introduce a novel audio-driven talking head synthesis framework, called Talk3D, that can faithfully reconstruct its plausible facial geometries by effectively adopting the pre-trained 3D-aware generative prior. Given the personalized 3D generative model, we present a novel audio-guided attention U-Net architecture that predicts the dynamic face variations in the NeRF space driven by audio. Furthermore, our model is further modulated by audio-unrelated conditioning tokens which effectively disentangle variations unrelated to audio features. Compared to existing methods, our method excels in generating realistic facial geometries even under extreme head poses. We also conduct extensive experiments showing our approach surpasses state-of-the-art benchmarks in terms of both quantitative and qualitative evaluations.

</details>

### [MI-NeRF: Learning a Single Face NeRF from Multiple Identities](2403.19920.md)
**Aggelina Chatziagapi, Grigorios G. Chrysos, Dimitris Samaras** · 2024-03-29

<details>
<summary>Abstract</summary>

In this work, we introduce a method that learns a single dynamic neural radiance field (NeRF) from monocular talking face videos of multiple identities. NeRFs have shown remarkable results in modeling the 4D dynamics and appearance of human faces. However, they require per-identity optimization. Although recent approaches have proposed techniques to reduce the training and rendering time, increasing the number of identities can be expensive. We introduce MI-NeRF (multi-identity NeRF), a single unified network that models complex non-rigid facial motion for multiple identities, using only monocular videos of arbitrary length. The core premise in our method is to learn the non-linear interactions between identity and non-identity specific information with a multiplicative module. By training on multiple videos simultaneously, MI-NeRF not only reduces the total training time compared to standard single-identity NeRFs, but also demonstrates robustness in synthesizing novel expressions for any input identity. We present results for both facial expression transfer and talking face video synthesis. Our method can be further personalized for a target identity given only a short video.

</details>

### [MoDiTalker: Motion-Disentangled Diffusion Model for High-Fidelity Talking Head Generation](2403.19144.md)
**Seyeon Kim, Siyoon Jin, Jihye Park, Kihong Kim et al.** · 2024-03-28

<details>
<summary>Abstract</summary>

Conventional GAN-based models for talking head generation often suffer from limited quality and unstable training. Recent approaches based on diffusion models aimed to address these limitations and improve fidelity. However, they still face challenges, including extensive sampling times and difficulties in maintaining temporal consistency due to the high stochasticity of diffusion models. To overcome these challenges, we propose a novel motion-disentangled diffusion model for high-quality talking head generation, dubbed MoDiTalker. We introduce the two modules: audio-to-motion (AToM), designed to generate a synchronized lip motion from audio, and motion-to-video (MToV), designed to produce high-quality head video following the generated motion. AToM excels in capturing subtle lip movements by leveraging an audio attention mechanism. In addition, MToV enhances temporal consistency by leveraging an efficient tri-plane representation. Our experiments conducted on standard benchmarks demonstrate that our model achieves superior performance compared to existing models. We also provide comprehensive ablation studies and user study results.

</details>

### [Deepfake Generation and Detection: A Benchmark and Survey](2403.17881.md)
**Gan Pei, Jiangning Zhang, Menghan Hu, Zhenyu Zhang et al.** · 2024-03-26

<details>
<summary>Abstract</summary>

Deepfake is a technology dedicated to creating highly realistic facial images and videos under specific conditions, which has significant application potential in fields such as entertainment, movie production, digital human creation, to name a few. With the advancements in deep learning, techniques primarily represented by Variational Autoencoders and Generative Adversarial Networks have achieved impressive generation results. More recently, the emergence of diffusion models with powerful generation capabilities has sparked a renewed wave of research. In addition to deepfake generation, corresponding detection technologies continuously evolve to regulate the potential misuse of deepfakes, such as for privacy invasion and phishing attacks. This survey comprehensively reviews the latest developments in deepfake generation and detection, summarizing and analyzing current state-of-the-arts in this rapidly evolving field. We first unify task definitions, comprehensively introduce datasets and metrics, and discuss developing technologies. Then, we discuss the development of several related sub-fields and focus on researching four representative deepfake fields: face swapping, face reenactment, talking face generation, and facial attribute editing, as well as forgery detection. Subsequently, we comprehensively benchmark representative methods on popular datasets for each field, fully evaluating the latest and influential published works. Finally, we analyze challenges and future research directions of the discussed fields.

</details>

### [AniPortrait: Audio-Driven Synthesis of Photorealistic Portrait Animation](2403.17694.md)
**Huawei Wei, Zejun Yang, Zhisheng Wang** · 2024-03-26

<details>
<summary>Abstract</summary>

In this study, we propose AniPortrait, a novel framework for generating high-quality animation driven by audio and a reference portrait image. Our methodology is divided into two stages. Initially, we extract 3D intermediate representations from audio and project them into a sequence of 2D facial landmarks. Subsequently, we employ a robust diffusion model, coupled with a motion module, to convert the landmark sequence into photorealistic and temporally consistent portrait animation. Experimental results demonstrate the superiority of AniPortrait in terms of facial naturalness, pose diversity, and visual quality, thereby offering an enhanced perceptual experience. Moreover, our methodology exhibits considerable potential in terms of flexibility and controllability, which can be effectively applied in areas such as facial motion editing or face reenactment. We release code and model weights at https://github.com/scutzzj/AniPortrait

</details>

### [DiffusionAct: Controllable Diffusion Autoencoder for One-shot Face Reenactment](2403.17217.md)
**Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras et al.** · 2024-03-25

<details>
<summary>Abstract</summary>

Video-driven neural face reenactment aims to synthesize realistic facial images that successfully preserve the identity and appearance of a source face, while transferring the target head pose and facial expressions. Existing GAN-based methods suffer from either distortions and visual artifacts or poor reconstruction quality, i.e., the background and several important appearance details, such as hair style/color, glasses and accessories, are not faithfully reconstructed. Recent advances in Diffusion Probabilistic Models (DPMs) enable the generation of high-quality realistic images. To this end, in this paper we present DiffusionAct, a novel method that leverages the photo-realistic image generation of diffusion models to perform neural face reenactment. Specifically, we propose to control the semantic space of a Diffusion Autoencoder (DiffAE), in order to edit the facial pose of the input images, defined as the head pose orientation and the facial expressions. Our method allows one-shot, self, and cross-subject reenactment, without requiring subject-specific fine-tuning. We compare against state-of-the-art GAN-, StyleGAN2-, and diffusion-based methods, showing better or on-par reenactment performance.

</details>

### [FG-EmoTalk: Talking Head Video Generation with Fine-Grained Controllable Facial Expressions](s2:78396d47cff7a5d2e1330d9f75a2619bb7e1b713.md)
**Zhaoxu Sun, Yuze Xuan, Fang Liu, Yang Xiang** · 2024-03-24

<details>
<summary>Abstract</summary>

Although deep generative models have greatly improved one-shot video-driven talking head generation, few studies address fine-grained controllable facial expression editing, which is crucial for practical applications. Existing methods rely on a fixed set of predefined discrete emotion labels or simply copy expressions from input videos. This is limiting as expressions are complex, and methods using only emotion labels cannot generate fine-grained, accurate or mixed expressions. Generating talking head video with precise expressions is also difficult using 3D model-based approaches, as 3DMM only models facial movements and tends to produce deviations. In this paper, we propose a novel framework enabling fine-grained facial expression editing in talking face generation. Our goal is to achieve expression control by manipulating the intensities of individual facial Action Units (AUs) or groups. First, compared with existing methods which decouple the face into pose and expression, we propose a disentanglement scheme to isolates three components from the human face, namely, appearance, pose, and expression. Second, we propose to use input AUs to control muscle group intensities in the generated face, and integrate the AUs features with the disentangled expression latent code. Finally, we present a self-supervised training strategy with well-designed constraints. Experiments show our method achieves fine-grained expression control, produces high-quality talking head videos and outperforms baseline methods.

</details>

### [ScanTalk: 3D Talking Heads from Unregistered Scans](2403.10942.md)
**Federico Nocentini, Thomas Besnier, Claudio Ferrari, Sylvain Arguillere et al.** · 2024-03-16

<details>
<summary>Abstract</summary>

Speech-driven 3D talking heads generation has emerged as a significant area of interest among researchers, presenting numerous challenges. Existing methods are constrained by animating faces with fixed topologies, wherein point-wise correspondence is established, and the number and order of points remains consistent across all identities the model can animate. In this work, we present \textbf{ScanTalk}, a novel framework capable of animating 3D faces in arbitrary topologies including scanned data. Our approach relies on the DiffusionNet architecture to overcome the fixed topology constraint, offering promising avenues for more flexible and realistic 3D animations. By leveraging the power of DiffusionNet, ScanTalk not only adapts to diverse facial structures but also maintains fidelity when dealing with scanned data, thereby enhancing the authenticity and versatility of generated 3D talking heads. Through comprehensive comparisons with state-of-the-art methods, we validate the efficacy of our approach, demonstrating its capacity to generate realistic talking heads comparable to existing techniques. While our primary objective is to develop a generic method free from topological constraints, all state-of-the-art methodologies are bound by such limitations. Code for reproducing our results, and the pre-trained model are available at https://github.com/miccunifi/ScanTalk .

</details>

### [Style2Talker: High-Resolution Talking Head Generation with Emotion Style and Art Style](2403.06365.md)
**Shuai Tan, Bin Ji, Ye Pan** · 2024-03-11

<details>
<summary>Abstract</summary>

Although automatically animating audio-driven talking heads has recently received growing interest, previous efforts have mainly concentrated on achieving lip synchronization with the audio, neglecting two crucial elements for generating expressive videos: emotion style and art style. In this paper, we present an innovative audio-driven talking face generation method called Style2Talker. It involves two stylized stages, namely Style-E and Style-A, which integrate text-controlled emotion style and picture-controlled art style into the final output. In order to prepare the scarce emotional text descriptions corresponding to the videos, we propose a labor-free paradigm that employs large-scale pretrained models to automatically annotate emotional text labels for existing audiovisual datasets. Incorporating the synthetic emotion texts, the Style-E stage utilizes a large-scale CLIP model to extract emotion representations, which are combined with the audio, serving as the condition for an efficient latent diffusion model designed to produce emotional motion coefficients of a 3DMM model. Moving on to the Style-A stage, we develop a coefficient-driven motion generator and an art-specific style path embedded in the well-known StyleGAN. This allows us to synthesize high-resolution artistically stylized talking head videos using the generated emotional motion coefficients and an art style source picture. Moreover, to better preserve image details and avoid artifacts, we provide StyleGAN with the multi-scale content features extracted from the identity image and refine its intermediate feature maps by the designed content encoder and refinement network, respectively. Extensive experimental results demonstrate our method outperforms existing state-of-the-art methods in terms of audio-lip synchronization and performance of both emotion style and art style.

</details>

### [Say Anything with Any Style](2403.06363.md)
**Shuai Tan, Bin Ji, Yu Ding, Ye Pan** · 2024-03-11

<details>
<summary>Abstract</summary>

Generating stylized talking head with diverse head motions is crucial for achieving natural-looking videos but still remains challenging. Previous works either adopt a regressive method to capture the speaking style, resulting in a coarse style that is averaged across all training data, or employ a universal network to synthesize videos with different styles which causes suboptimal performance. To address these, we propose a novel dynamic-weight method, namely Say Anything withAny Style (SAAS), which queries the discrete style representation via a generative model with a learned style codebook. Specifically, we develop a multi-task VQ-VAE that incorporates three closely related tasks to learn a style codebook as a prior for style extraction. This discrete prior, along with the generative model, enhances the precision and robustness when extracting the speaking styles of the given style clips. By utilizing the extracted style, a residual architecture comprising a canonical branch and style-specific branch is employed to predict the mouth shapes conditioned on any driving audio while transferring the speaking style from the source to any desired one. To adapt to different speaking styles, we steer clear of employing a universal network by exploring an elaborate HyperStyle to produce the style-specific weights offset for the style branch. Furthermore, we construct a pose generator and a pose codebook to store the quantized pose representation, allowing us to sample diverse head motions aligned with the audio and the extracted style. Experiments demonstrate that our approach surpasses state-of-theart methods in terms of both lip-synchronization and stylized expression. Besides, we extend our SAAS to video-driven style editing field and achieve satisfactory performance.

</details>

### [A Comparative Study of Perceptual Quality Metrics for Audio-driven Talking Head Videos](2403.06421.md)
**Weixia Zhang, Chengguang Zhu, Jingnan Gao, Yichao Yan et al.** · 2024-03-11

<details>
<summary>Abstract</summary>

The rapid advancement of Artificial Intelligence Generated Content (AIGC) technology has propelled audio-driven talking head generation, gaining considerable research attention for practical applications. However, performance evaluation research lags behind the development of talking head generation techniques. Existing literature relies on heuristic quantitative metrics without human validation, hindering accurate progress assessment. To address this gap, we collect talking head videos generated from four generative methods and conduct controlled psychophysical experiments on visual quality, lip-audio synchronization, and head movement naturalness. Our experiments validate consistency between model predictions and human annotations, identifying metrics that align better with human opinions than widely-used measures. We believe our work will facilitate performance evaluation and model development, providing insights into AIGC in a broader context. Code and data will be made available at https://github.com/zwx8981/ADTH-QA.

</details>

### [Audio–video syncing with lip movements using generative deep neural networks](s2:75327cbf02cd2343bdef4a69b93a2be3889b701f.md)
**Amal Mathew, Aaryl Saldanha, C. Babu** · 2024-03-11

### [FaceChain-ImagineID: Freely Crafting High-Fidelity Diverse Talking Faces from Disentangled Audio](2403.01901.md)
**Chao Xu, Yang Liu, Jiazheng Xing, Weida Wang et al.** · 2024-03-04

<details>
<summary>Abstract</summary>

In this paper, we abstract the process of people hearing speech, extracting meaningful cues, and creating various dynamically audio-consistent talking faces, termed Listening and Imagining, into the task of high-fidelity diverse talking faces generation from a single audio. Specifically, it involves two critical challenges: one is to effectively decouple identity, content, and emotion from entangled audio, and the other is to maintain intra-video diversity and inter-video consistency. To tackle the issues, we first dig out the intricate relationships among facial factors and simplify the decoupling process, tailoring a Progressive Audio Disentanglement for accurate facial geometry and semantics learning, where each stage incorporates a customized training module responsible for a specific factor. Secondly, to achieve visually diverse and audio-synchronized animation solely from input audio within a single model, we introduce the Controllable Coherent Frame generation, which involves the flexible integration of three trainable adapters with frozen Latent Diffusion Models (LDMs) to focus on maintaining facial geometry and semantics, as well as texture and temporal coherence between frames. In this way, we inherit high-quality diverse generation from LDMs while significantly improving their controllability at a low training cost. Extensive experiments demonstrate the flexibility and effectiveness of our method in handling this paradigm. The codes will be released at https://github.com/modelscope/facechain.

</details>

### [Context-aware Talking Face Video Generation](2402.18092.md)
**Meidai Xuanyuan, Yuwang Wang, Honglei Guo, Qionghai Dai** · 2024-02-28

<details>
<summary>Abstract</summary>

In this paper, we consider a novel and practical case for talking face video generation. Specifically, we focus on the scenarios involving multi-people interactions, where the talking context, such as audience or surroundings, is present. In these situations, the video generation should take the context into consideration in order to generate video content naturally aligned with driving audios and spatially coherent to the context. To achieve this, we provide a two-stage and cross-modal controllable video generation pipeline, taking facial landmarks as an explicit and compact control signal to bridge the driving audio, talking context and generated videos. Inside this pipeline, we devise a 3D video diffusion model, allowing for efficient contort of both spatial conditions (landmarks and context video), as well as audio condition for temporally coherent generation. The experimental results verify the advantage of the proposed method over other baselines in terms of audio-video synchronization, video fidelity and frame consistency.

</details>

### [Learning Dynamic Tetrahedra for High-Quality Talking Head Synthesis](2402.17364.md)
**Zicheng Zhang, Ruobing Zheng, Ziwen Liu, Congying Han et al.** · 2024-02-27

<details>
<summary>Abstract</summary>

Recent works in implicit representations, such as Neural Radiance Fields (NeRF), have advanced the generation of realistic and animatable head avatars from video sequences. These implicit methods are still confronted by visual artifacts and jitters, since the lack of explicit geometric constraints poses a fundamental challenge in accurately modeling complex facial deformations. In this paper, we introduce Dynamic Tetrahedra (DynTet), a novel hybrid representation that encodes explicit dynamic meshes by neural networks to ensure geometric consistency across various motions and viewpoints. DynTet is parameterized by the coordinate-based networks which learn signed distance, deformation, and material texture, anchoring the training data into a predefined tetrahedra grid. Leveraging Marching Tetrahedra, DynTet efficiently decodes textured meshes with a consistent topology, enabling fast rendering through a differentiable rasterizer and supervision via a pixel loss. To enhance training efficiency, we incorporate classical 3D Morphable Models to facilitate geometry learning and define a canonical space for simplifying texture learning. These advantages are readily achievable owing to the effective geometric representation employed in DynTet. Compared with prior works, DynTet demonstrates significant improvements in fidelity, lip synchronization, and real-time performance according to various metrics. Beyond producing stable and visually appealing synthesis videos, our method also outputs the dynamic meshes which is promising to enable many emerging applications.

</details>

### [EMO: Emote Portrait Alive -- Generating Expressive Portrait Videos with Audio2Video Diffusion Model under Weak Conditions](2402.17485.md)
**Linrui Tian, Qi Wang, Bang Zhang, Liefeng Bo** · 2024-02-27

<details>
<summary>Abstract</summary>

In this work, we tackle the challenge of enhancing the realism and expressiveness in talking head video generation by focusing on the dynamic and nuanced relationship between audio cues and facial movements. We identify the limitations of traditional techniques that often fail to capture the full spectrum of human expressions and the uniqueness of individual facial styles. To address these issues, we propose EMO, a novel framework that utilizes a direct audio-to-video synthesis approach, bypassing the need for intermediate 3D models or facial landmarks. Our method ensures seamless frame transitions and consistent identity preservation throughout the video, resulting in highly expressive and lifelike animations. Experimental results demonsrate that EMO is able to produce not only convincing speaking videos but also singing videos in various styles, significantly outperforming existing state-of-the-art methodologies in terms of expressiveness and realism.

</details>

### [Resolution-Agnostic Neural Compression for High-Fidelity Portrait Video Conferencing via Implicit Radiance Fields](2402.16599.md)
**Yifei Li, Xiaohong Liu, Yicong Peng, Guangtao Zhai et al.** · 2024-02-26

<details>
<summary>Abstract</summary>

Video conferencing has caught much more attention recently. High fidelity and low bandwidth are two major objectives of video compression for video conferencing applications. Most pioneering methods rely on classic video compression codec without high-level feature embedding and thus can not reach the extremely low bandwidth. Recent works instead employ model-based neural compression to acquire ultra-low bitrates using sparse representations of each frame such as facial landmark information, while these approaches can not maintain high fidelity due to 2D image-based warping. In this paper, we propose a novel low bandwidth neural compression approach for high-fidelity portrait video conferencing using implicit radiance fields to achieve both major objectives. We leverage dynamic neural radiance fields to reconstruct high-fidelity talking head with expression features, which are represented as frame substitution for transmission. The overall system employs deep model to encode expression features at the sender and reconstruct portrait at the receiver with volume rendering as decoder for ultra-low bandwidth. In particular, with the characteristic of neural radiance fields based model, our compression approach is resolution-agnostic, which means that the low bandwidth achieved by our approach is independent of video resolution, while maintaining fidelity for higher resolution reconstruction. Experimental results demonstrate that our novel framework can (1) construct ultra-low bandwidth video conferencing, (2) maintain high fidelity portrait and (3) have better performance on high-resolution video compression than previous works.

</details>

### [Audio-Visual Speech Enhancement in Noisy Environments via Emotion-Based Contextual Cues](2402.16394.md)
**Tassadaq Hussain, Kia Dashtipour, Yu Tsao, Amir Hussain** · 2024-02-26

<details>
<summary>Abstract</summary>

In real-world environments, background noise significantly degrades the intelligibility and clarity of human speech. Audio-visual speech enhancement (AVSE) attempts to restore speech quality, but existing methods often fall short, particularly in dynamic noise conditions. This study investigates the inclusion of emotion as a novel contextual cue within AVSE, hypothesizing that incorporating emotional understanding can improve speech enhancement performance. We propose a novel emotion-aware AVSE system that leverages both auditory and visual information. It extracts emotional features from the facial landmarks of the speaker and fuses them with corresponding audio and visual modalities. This enriched data serves as input to a deep UNet-based encoder-decoder network, specifically designed to orchestrate the fusion of multimodal information enhanced with emotion. The network iteratively refines the enhanced speech representation through an encoder-decoder architecture, guided by perceptually-inspired loss functions for joint learning and optimization. We train and evaluate the model on the CMU Multimodal Opinion Sentiment and Emotion Intensity (CMU-MOSEI) dataset, a rich repository of audio-visual recordings with annotated emotions. Our comprehensive evaluation demonstrates the effectiveness of emotion as a contextual cue for AVSE. By integrating emotional features, the proposed system achieves significant improvements in both objective and subjective assessments of speech quality and intelligibility, especially in challenging noise environments. Compared to baseline AVSE and audio-only speech enhancement systems, our approach exhibits a noticeable increase in PESQ and STOI, indicating higher perceptual quality and intelligibility. Large-scale listening tests corroborate these findings, suggesting improved human understanding of enhanced speech.

</details>

### [AVI-Talking: Learning Audio-Visual Instructions for Expressive 3D Talking Face Generation](2402.16124.md)
**Yasheng Sun, Wenqing Chu, Hang Zhou, Kaisiyuan Wang et al.** · 2024-02-25

<details>
<summary>Abstract</summary>

While considerable progress has been made in achieving accurate lip synchronization for 3D speech-driven talking face generation, the task of incorporating expressive facial detail synthesis aligned with the speaker's speaking status remains challenging. Our goal is to directly leverage the inherent style information conveyed by human speech for generating an expressive talking face that aligns with the speaking status. In this paper, we propose AVI-Talking, an Audio-Visual Instruction system for expressive Talking face generation. This system harnesses the robust contextual reasoning and hallucination capability offered by Large Language Models (LLMs) to instruct the realistic synthesis of 3D talking faces. Instead of directly learning facial movements from human speech, our two-stage strategy involves the LLMs first comprehending audio information and generating instructions implying expressive facial details seamlessly corresponding to the speech. Subsequently, a diffusion-based generative network executes these instructions. This two-stage process, coupled with the incorporation of LLMs, enhances model interpretability and provides users with flexibility to comprehend instructions and specify desired operations or modifications. Extensive experiments showcase the effectiveness of our approach in producing vivid talking faces with expressive facial movements and consistent emotional status.

</details>

### [Lip Synchronization Model For Sinhala Language Using Machine Learning](s2:20e6ef1cae962c4bf37c906cb6049664b18a24af.md)
**Dilani Ranaweera, R. Weerasinghe, R. Dinalankara** · 2024-02-21

<details>
<summary>Abstract</summary>

Realistic lip-synchronized animations can be produced by the appropriately timed voice and lip motions of the cartoon character. This process is called as “lip synchronization”. Building a talking face for languages such as English, Korean, and Portuguese has been subject of numerous studies. Compared to other languages, Sinhala is a low-resource language due to less contribution in these researches. This research study focuses to build a frontal view of a synthetic mouth part with smooth lip movements rather than opening and closing while speaking Sinhala sentences. The most difficult challenge is to match the basic sounds, “phonemes” with the lip movement called “visemes”. This study has been used static viseme approach by deriving twenty three (23) Sinhala viseme classes and a deep learning model has been developed to map visemes with Sinhala letters. In system implementation, text input is provided first, after which the system produces audio and the deep learning model generates a collection of visemes based on the given text. The system interface then offers three options for playing the visemes at various speeds, including fast, normal, and slow. The user interface was created in Python, and the deep learning model is integrated into the system. This model will be very helpful to use in cartoon industry to build Sinhala speaking cartoon characters and also be used to train deaf people to read lips.

</details>

### [StyleDubber: Towards Multi-Scale Style Learning for Movie Dubbing](2402.12636.md)
**Gaoxiang Cong, Yuankai Qi, Liang Li, Amin Beheshti et al.** · 2024-02-20

<details>
<summary>Abstract</summary>

Given a script, the challenge in Movie Dubbing (Visual Voice Cloning, V2C) is to generate speech that aligns well with the video in both time and emotion, based on the tone of a reference audio track. Existing state-of-the-art V2C models break the phonemes in the script according to the divisions between video frames, which solves the temporal alignment problem but leads to incomplete phoneme pronunciation and poor identity stability. To address this problem, we propose StyleDubber, which switches dubbing learning from the frame level to phoneme level. It contains three main components: (1) A multimodal style adaptor operating at the phoneme level to learn pronunciation style from the reference audio, and generate intermediate representations informed by the facial emotion presented in the video; (2) An utterance-level style learning module, which guides both the mel-spectrogram decoding and the refining processes from the intermediate embeddings to improve the overall style expression; And (3) a phoneme-guided lip aligner to maintain lip sync. Extensive experiments on two of the primary benchmarks, V2C and Grid, demonstrate the favorable performance of the proposed method as compared to the current stateof-the-art. The code will be made available at https://github.com/GalaxyCong/StyleDubber.

</details>

### [AnnoTheia: A Semi-Automatic Annotation Toolkit for Audio-Visual Speech Technologies](2402.13152.md)
**José-M. Acosta-Triana, David Gimeno-Gómez, Carlos-D. Martínez-Hinarejos** · 2024-02-20

<details>
<summary>Abstract</summary>

More than 7,000 known languages are spoken around the world. However, due to the lack of annotated resources, only a small fraction of them are currently covered by speech technologies. Albeit self-supervised speech representations, recent massive speech corpora collections, as well as the organization of challenges, have alleviated this inequality, most studies are mainly benchmarked on English. This situation is aggravated when tasks involving both acoustic and visual speech modalities are addressed. In order to promote research on low-resource languages for audio-visual speech technologies, we present AnnoTheia, a semi-automatic annotation toolkit that detects when a person speaks on the scene and the corresponding transcription. In addition, to show the complete process of preparing AnnoTheia for a language of interest, we also describe the adaptation of a pre-trained model for active speaker detection to Spanish, using a database not initially conceived for this type of task. The AnnoTheia toolkit, tutorials, and pre-trained models are available on GitHub.

</details>

### [DiffSpeaker: Speech-Driven 3D Facial Animation with Diffusion Transformer](2402.05712.md)
**Zhiyuan Ma, Xiangyu Zhu, Guojun Qi, Chen Qian et al.** · 2024-02-08

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation is important for many multimedia applications. Recent work has shown promise in using either Diffusion models or Transformer architectures for this task. However, their mere aggregation does not lead to improved performance. We suspect this is due to a shortage of paired audio-4D data, which is crucial for the Transformer to effectively perform as a denoiser within the Diffusion framework. To tackle this issue, we present DiffSpeaker, a Transformer-based network equipped with novel biased conditional attention modules. These modules serve as substitutes for the traditional self/cross-attention in standard Transformers, incorporating thoughtfully designed biases that steer the attention mechanisms to concentrate on both the relevant task-specific and diffusion-related conditions. We also explore the trade-off between accurate lip synchronization and non-verbal facial expressions within the Diffusion paradigm. Experiments show our model not only achieves state-of-the-art performance on existing benchmarks, but also fast inference speed owing to its ability to generate facial motions in parallel.

</details>

### [One-shot Neural Face Reenactment via Finding Directions in GAN's Latent Space](2402.03553.md)
**Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras et al.** · 2024-02-05

<details>
<summary>Abstract</summary>

In this paper, we present our framework for neural face/head reenactment whose goal is to transfer the 3D head orientation and expression of a target face to a source face. Previous methods focus on learning embedding networks for identity and head pose/expression disentanglement which proves to be a rather hard task, degrading the quality of the generated images. We take a different approach, bypassing the training of such networks, by using (fine-tuned) pre-trained GANs which have been shown capable of producing high-quality facial images. Because GANs are characterized by weak controllability, the core of our approach is a method to discover which directions in latent GAN space are responsible for controlling head pose and expression variations. We present a simple pipeline to learn such directions with the aid of a 3D shape model which, by construction, inherently captures disentangled directions for head pose, identity, and expression. Moreover, we show that by embedding real images in the GAN latent space, our method can be successfully used for the reenactment of real-world faces. Our method features several favorable properties including using a single source image (one-shot) and enabling cross-person reenactment. Extensive qualitative and quantitative results show that our approach typically produces reenacted faces of notably higher quality than those produced by state-of-the-art methods for the standard benchmarks of VoxCeleb1 & 2.

</details>

### [EmoSpeaker: One-shot Fine-grained Emotion-Controlled Talking Face Generation](2402.01422.md)
**Guanwen Feng, Haoran Cheng, Yunan Li, Zhiyuan Ma et al.** · 2024-02-02

<details>
<summary>Abstract</summary>

Implementing fine-grained emotion control is crucial for emotion generation tasks because it enhances the expressive capability of the generative model, allowing it to accurately and comprehensively capture and express various nuanced emotional states, thereby improving the emotional quality and personalization of generated content. Generating fine-grained facial animations that accurately portray emotional expressions using only a portrait and an audio recording presents a challenge. In order to address this challenge, we propose a visual attribute-guided audio decoupler. This enables the obtention of content vectors solely related to the audio content, enhancing the stability of subsequent lip movement coefficient predictions. To achieve more precise emotional expression, we introduce a fine-grained emotion coefficient prediction module. Additionally, we propose an emotion intensity control method using a fine-grained emotion matrix. Through these, effective control over emotional expression in the generated videos and finer classification of emotion intensity are accomplished. Subsequently, a series of 3DMM coefficient generation networks are designed to predict 3D coefficients, followed by the utilization of a rendering network to generate the final video. Our experimental results demonstrate that our proposed method, EmoSpeaker, outperforms existing emotional talking face generation methods in terms of expression variation and lip synchronization. Project page: https://peterfanfan.github.io/EmoSpeaker/

</details>

### [NeRF-AD: Neural Radiance Field with Attention-based Disentanglement for Talking Face Synthesis](2401.12568.md)
**Chongke Bi, Xiaoxing Liu, Zhilei Liu** · 2024-01-23

<details>
<summary>Abstract</summary>

Talking face synthesis driven by audio is one of the current research hotspots in the fields of multidimensional signal processing and multimedia. Neural Radiance Field (NeRF) has recently been brought to this research field in order to enhance the realism and 3D effect of the generated faces. However, most existing NeRF-based methods either burden NeRF with complex learning tasks while lacking methods for supervised multimodal feature fusion, or cannot precisely map audio to the facial region related to speech movements. These reasons ultimately result in existing methods generating inaccurate lip shapes. This paper moves a portion of NeRF learning tasks ahead and proposes a talking face synthesis method via NeRF with attention-based disentanglement (NeRF-AD). In particular, an Attention-based Disentanglement module is introduced to disentangle the face into Audio-face and Identity-face using speech-related facial action unit (AU) information. To precisely regulate how audio affects the talking face, we only fuse the Audio-face with audio feature. In addition, AU information is also utilized to supervise the fusion of these two modalities. Extensive qualitative and quantitative experiments demonstrate that our NeRF-AD outperforms state-of-the-art methods in generating realistic talking face videos, including image quality and lip synchronization. To view video results, please refer to https://xiaoxingliu02.github.io/NeRF-AD.

</details>

### [Real3D-Portrait: One-shot Realistic 3D Talking Portrait Synthesis](2401.08503.md)
**Zhenhui Ye, Tianyun Zhong, Yi Ren, Jiaqi Yang et al.** · 2024-01-16

<details>
<summary>Abstract</summary>

One-shot 3D talking portrait generation aims to reconstruct a 3D avatar from an unseen image, and then animate it with a reference video or audio to generate a talking portrait video. The existing methods fail to simultaneously achieve the goals of accurate 3D avatar reconstruction and stable talking face animation. Besides, while the existing works mainly focus on synthesizing the head part, it is also vital to generate natural torso and background segments to obtain a realistic talking portrait video. To address these limitations, we present Real3D-Potrait, a framework that (1) improves the one-shot 3D reconstruction power with a large image-to-plane model that distills 3D prior knowledge from a 3D face generative model; (2) facilitates accurate motion-conditioned animation with an efficient motion adapter; (3) synthesizes realistic video with natural torso movement and switchable background using a head-torso-background super-resolution model; and (4) supports one-shot audio-driven talking face generation with a generalizable audio-to-motion model. Extensive experiments show that Real3D-Portrait generalizes well to unseen identities and generates more realistic talking portrait videos compared to previous methods. Video samples and source code are available at https://real3dportrait.github.io .

</details>

### [EmoTalker: Emotionally Editable Talking Face Generation via Diffusion Model](2401.08049.md)
**Bingyuan Zhang, Xulong Zhang, Ning Cheng, Jun Yu et al.** · 2024-01-16

<details>
<summary>Abstract</summary>

In recent years, the field of talking faces generation has attracted considerable attention, with certain methods adept at generating virtual faces that convincingly imitate human expressions. However, existing methods face challenges related to limited generalization, particularly when dealing with challenging identities. Furthermore, methods for editing expressions are often confined to a singular emotion, failing to adapt to intricate emotions. To overcome these challenges, this paper proposes EmoTalker, an emotionally editable portraits animation approach based on the diffusion model. EmoTalker modifies the denoising process to ensure preservation of the original portrait's identity during inference. To enhance emotion comprehension from text input, Emotion Intensity Block is introduced to analyze fine-grained emotions and strengths derived from prompts. Additionally, a crafted dataset is harnessed to enhance emotion comprehension within prompts. Experiments show the effectiveness of EmoTalker in generating high-quality, emotionally customizable facial expressions.

</details>

### [Towards a Simultaneous and Granular Identity-Expression Control in Personalized Face Generation](2401.01207.md)
**Renshuai Liu, Bowen Ma, Wei Zhang, Zhipeng Hu et al.** · 2024-01-02

<details>
<summary>Abstract</summary>

In human-centric content generation, the pre-trained text-to-image models struggle to produce user-wanted portrait images, which retain the identity of individuals while exhibiting diverse expressions. This paper introduces our efforts towards personalized face generation. To this end, we propose a novel multi-modal face generation framework, capable of simultaneous identity-expression control and more fine-grained expression synthesis. Our expression control is so sophisticated that it can be specialized by the fine-grained emotional vocabulary. We devise a novel diffusion model that can undertake the task of simultaneously face swapping and reenactment. Due to the entanglement of identity and expression, it's nontrivial to separately and precisely control them in one framework, thus has not been explored yet. To overcome this, we propose several innovative designs in the conditional diffusion model, including balancing identity and expression encoder, improved midpoint sampling, and explicitly background conditioning. Extensive experiments have demonstrated the controllability and scalability of the proposed framework, in comparison with state-of-the-art text-to-image, face swapping, and face reenactment methods.

</details>

### [LatentSync: Audio Conditioned Latent Diffusion Models for Lip Sync](s2:a9ec5c7585a50a5b9cc4458f6b5506693b658be4.md)
**Chunyu Li, Chao Zhang, Weikai Xu, Jinghui Xie et al.** · 2024-01-01

### [SD-NeRF: Towards Lifelike Talking Head Animation via Spatially-Adaptive Dual-Driven NeRFs](s2:e3ad82f6d53d582e03d51bd017f47fcd157fe4ba.md)
**Shuai Shen, Wanhua Li, Xiaoke Huang, Zhengbiao Zhu et al.** · 2024-01-01

<details>
<summary>Abstract</summary>

Recent years have witnessed great progress in audio-driven talking head animation. Among these methods, the 3D-based ones better preserve the 3D consistency of the generated head and produce more natural results compared with 2D-based approaches. However, most 3D-based methods employ 3D morphable face models as the intermediate representation and involve multi-stage training, which may lead to error accumulation. To alleviate this problem, in this article, we propose a fully end-to-end talking head animation method, which implicitly grasps the 3D structures by learning a conditional Neural Radiance Field (NeRF). As NeRF has proven to be an effective tool for 3D modeling, one can learn dynamic neural radiance fields conditioned on audio signals for talking head synthesis. Furthermore, we argue that audio signals cannot fully drive a lifelike talking head. When people are talking, they usually show many spontaneous facial movements like blinks and brow movements, which makes talkers natural and real. These movements cannot be fully driven by the audio signals since they are highly unrelated to the audio. Therefore, we incorporate motion information as another driving factor and develop an audio-motion dual-driven NeRF model to take a step toward more lifelike talking head synthesis. On this basis, as audio and motion mainly affect different regions of the human face, we propose a Spatially-adaptive Dual-driven NeRF (SD-NeRF), which fuses these two driven factors with a spatially-adaptive cross-attention mechanism. Quantitative and qualitative results demonstrate that, with finer facial controls, our method produces more realistic talking head videos compared with existing advanced works.

</details>

### [MergeTalk: Audio-Driven Talking Head Generation From Single Image With Feature Merge](s2:3c6249961137d5262a1f874ea9837918b3ebb946.md)
**Jian Gao, Chang Shu, Ximin Zheng, Zheng Lu et al.** · 2024-01-01

<details>
<summary>Abstract</summary>

Audio-driven talking head generation has wide real world applications but remains challenging due to the problems such as audio-lip synchronization, head poses, identity preservation, video quality, etc. We propose a novel two-stage framework that uses explicit 3D face images rendered from a 3D model based on the audio input, as intermediate features. We devise two independent 3D motion parameter generation networks to generate expression and pose parameters for the popular 3DMM model to solve the audio-lip synchronization problem and natural head poses without losing identity information. To improve the final talking head quality such as avoiding facial distortion and artifacts, we propose a novel face feature merge network to accurately extract and fuse the background, identity information, facial texture from the source image, and the lip movements and head poses from the 3D face images, and generate the final videos based on generative adversarial networks. Extensive experiments show that our framework outperforms the SOTA methods in several aspects and has good generalization ability.

</details>

