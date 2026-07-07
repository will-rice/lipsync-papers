# 2023

85 papers in this year.

### [EFHQ: Multi-purpose ExtremePose-Face-HQ dataset](2312.17205.md)
**Trung Tuan Dao, Duc Hong Vu, Cuong Pham, Anh Tran** · 2023-12-28

<details>
<summary>Abstract</summary>

The existing facial datasets, while having plentiful images at near frontal views, lack images with extreme head poses, leading to the downgraded performance of deep learning models when dealing with profile or pitched faces. This work aims to address this gap by introducing a novel dataset named Extreme Pose Face High-Quality Dataset (EFHQ), which includes a maximum of 450k high-quality images of faces at extreme poses. To produce such a massive dataset, we utilize a novel and meticulous dataset processing pipeline to curate two publicly available datasets, VFHQ and CelebV-HQ, which contain many high-resolution face videos captured in various settings. Our dataset can complement existing datasets on various facial-related tasks, such as facial synthesis with 2D/3D-aware GAN, diffusion-based text-to-image face generation, and face reenactment. Specifically, training with EFHQ helps models generalize well across diverse poses, significantly improving performance in scenarios involving extreme views, confirmed by extensive experiments. Additionally, we utilize EFHQ to define a challenging cross-view face verification benchmark, in which the performance of SOTA face recognition models drops 5-37% compared to frontal-to-frontal scenarios, aiming to stimulate studies on face recognition under severe pose conditions in the wild.

</details>

### [SAiD: Speech-driven Blendshape Facial Animation with Diffusion](2401.08655.md)
**Inkyu Park, Jaewoong Cho** · 2023-12-25

<details>
<summary>Abstract</summary>

Speech-driven 3D facial animation is challenging due to the scarcity of large-scale visual-audio datasets despite extensive research. Most prior works, typically focused on learning regression models on a small dataset using the method of least squares, encounter difficulties generating diverse lip movements from speech and require substantial effort in refining the generated outputs. To address these issues, we propose a speech-driven 3D facial animation with a diffusion model (SAiD), a lightweight Transformer-based U-Net with a cross-modality alignment bias between audio and visual to enhance lip synchronization. Moreover, we introduce BlendVOCA, a benchmark dataset of pairs of speech audio and parameters of a blendshape facial model, to address the scarcity of public resources. Our experimental results demonstrate that the proposed approach achieves comparable or superior performance in lip synchronization to baselines, ensures more diverse lip movements, and streamlines the animation editing process.

</details>

### [TransFace: Unit-Based Audio-Visual Speech Synthesizer for Talking Head Translation](2312.15197.md)
**Xize Cheng, Rongjie Huang, Linjun Li, Tao Jin et al.** · 2023-12-23

<details>
<summary>Abstract</summary>

Direct speech-to-speech translation achieves high-quality results through the introduction of discrete units obtained from self-supervised learning. This approach circumvents delays and cascading errors associated with model cascading. However, talking head translation, converting audio-visual speech (i.e., talking head video) from one language into another, still confronts several challenges compared to audio speech: (1) Existing methods invariably rely on cascading, synthesizing via both audio and text, resulting in delays and cascading errors. (2) Talking head translation has a limited set of reference frames. If the generated translation exceeds the length of the original speech, the video sequence needs to be supplemented by repeating frames, leading to jarring video transitions. In this work, we propose a model for talking head translation, \textbf{TransFace}, which can directly translate audio-visual speech into audio-visual speech in other languages. It consists of a speech-to-unit translation model to convert audio speech into discrete units and a unit-based audio-visual speech synthesizer, Unit2Lip, to re-synthesize synchronized audio-visual speech from discrete units in parallel. Furthermore, we introduce a Bounded Duration Predictor, ensuring isometric talking head translation and preventing duplicate reference frames. Experiments demonstrate that our proposed Unit2Lip model significantly improves synchronization (1.601 and 0.982 on LSE-C for the original and generated audio speech, respectively) and boosts inference speed by a factor of 4.35 on LRS2. Additionally, TransFace achieves impressive BLEU scores of 61.93 and 47.55 for Es-En and Fr-En on LRS3-T and 100% isochronous translations.

</details>

### [DREAM-Talk: Diffusion-based Realistic Emotional Audio-driven Method for Single Image Talking Face Generation](2312.13578.md)
**Chenxu Zhang, Chao Wang, Jianfeng Zhang, Hongyi Xu et al.** · 2023-12-21

<details>
<summary>Abstract</summary>

The generation of emotional talking faces from a single portrait image remains a significant challenge. The simultaneous achievement of expressive emotional talking and accurate lip-sync is particularly difficult, as expressiveness is often compromised for the accuracy of lip-sync. As widely adopted by many prior works, the LSTM network often fails to capture the subtleties and variations of emotional expressions. To address these challenges, we introduce DREAM-Talk, a two-stage diffusion-based audio-driven framework, tailored for generating diverse expressions and accurate lip-sync concurrently. In the first stage, we propose EmoDiff, a novel diffusion module that generates diverse highly dynamic emotional expressions and head poses in accordance with the audio and the referenced emotion style. Given the strong correlation between lip motion and audio, we then refine the dynamics with enhanced lip-sync accuracy using audio features and emotion style. To this end, we deploy a video-to-video rendering module to transfer the expressions and lip motions from our proxy 3D avatar to an arbitrary portrait. Both quantitatively and qualitatively, DREAM-Talk outperforms state-of-the-art methods in terms of expressiveness, lip-sync accuracy and perceptual quality.

</details>

### [AE-NeRF: Audio Enhanced Neural Radiance Field for Few Shot Talking Head Synthesis](2312.10921.md)
**Dongze Li, Kang Zhao, Wei Wang, Bo Peng et al.** · 2023-12-18

<details>
<summary>Abstract</summary>

Audio-driven talking head synthesis is a promising topic with wide applications in digital human, film making and virtual reality. Recent NeRF-based approaches have shown superiority in quality and fidelity compared to previous studies. However, when it comes to few-shot talking head generation, a practical scenario where only few seconds of talking video is available for one identity, two limitations emerge: 1) they either have no base model, which serves as a facial prior for fast convergence, or ignore the importance of audio when building the prior; 2) most of them overlook the degree of correlation between different face regions and audio, e.g., mouth is audio related, while ear is audio independent. In this paper, we present Audio Enhanced Neural Radiance Field (AE-NeRF) to tackle the above issues, which can generate realistic portraits of a new speaker with fewshot dataset. Specifically, we introduce an Audio Aware Aggregation module into the feature fusion stage of the reference scheme, where the weight is determined by the similarity of audio between reference and target image. Then, an Audio-Aligned Face Generation strategy is proposed to model the audio related and audio independent regions respectively, with a dual-NeRF framework. Extensive experiments have shown AE-NeRF surpasses the state-of-the-art on image fidelity, audio-lip synchronization, and generalization ability, even in limited training set or training iterations.

</details>

### [VectorTalker: SVG Talking Face Generation with Progressive Vectorisation](2312.11568.md)
**Hao Hu, Xuan Wang, Jingxiang Sun, Yanbo Fan et al.** · 2023-12-18

<details>
<summary>Abstract</summary>

High-fidelity and efficient audio-driven talking head generation has been a key research topic in computer graphics and computer vision. In this work, we study vector image based audio-driven talking head generation. Compared with directly animating the raster image that most widely used in existing works, vector image enjoys its excellent scalability being used for many applications. There are two main challenges for vector image based talking head generation: the high-quality vector image reconstruction w.r.t. the source portrait image and the vivid animation w.r.t. the audio signal. To address these, we propose a novel scalable vector graphic reconstruction and animation method, dubbed VectorTalker. Specifically, for the highfidelity reconstruction, VectorTalker hierarchically reconstructs the vector image in a coarse-to-fine manner. For the vivid audio-driven facial animation, we propose to use facial landmarks as intermediate motion representation and propose an efficient landmark-driven vector image deformation module. Our approach can handle various styles of portrait images within a unified framework, including Japanese manga, cartoon, and photorealistic images. We conduct extensive quantitative and qualitative evaluations and the experimental results demonstrate the superiority of VectorTalker in both vector graphic reconstruction and audio-driven animation.

</details>

### [Learning Dense Correspondence for NeRF-Based Face Reenactment](2312.10422.md)
**Songlin Yang, Wei Wang, Yushi Lan, Xiangyu Fan et al.** · 2023-12-16

<details>
<summary>Abstract</summary>

Face reenactment is challenging due to the need to establish dense correspondence between various face representations for motion transfer. Recent studies have utilized Neural Radiance Field (NeRF) as fundamental representation, which further enhanced the performance of multi-view face reenactment in photo-realism and 3D consistency. However, establishing dense correspondence between different face NeRFs is non-trivial, because implicit representations lack ground-truth correspondence annotations like mesh-based 3D parametric models (e.g., 3DMM) with index-aligned vertexes. Although aligning 3DMM space with NeRF-based face representations can realize motion control, it is sub-optimal for their limited face-only modeling and low identity fidelity. Therefore, we are inspired to ask: Can we learn the dense correspondence between different NeRF-based face representations without a 3D parametric model prior? To address this challenge, we propose a novel framework, which adopts tri-planes as fundamental NeRF representation and decomposes face tri-planes into three components: canonical tri-planes, identity deformations, and motion. In terms of motion control, our key contribution is proposing a Plane Dictionary (PlaneDict) module, which efficiently maps the motion conditions to a linear weighted addition of learnable orthogonal plane bases. To the best of our knowledge, our framework is the first method that achieves one-shot multi-view face reenactment without a 3D parametric model prior. Extensive experiments demonstrate that we produce better results in fine-grained motion control and identity preservation than previous methods.

</details>

### [DreamTalk: When Emotional Talking Head Generation Meets Diffusion Probabilistic Models](2312.09767.md)
**Yifeng Ma, Shiwei Zhang, Jiayu Wang, Xiang Wang et al.** · 2023-12-15

<details>
<summary>Abstract</summary>

Emotional talking head generation has attracted growing attention. Previous methods, which are mainly GAN-based, still struggle to consistently produce satisfactory results across diverse emotions and cannot conveniently specify personalized emotions. In this work, we leverage powerful diffusion models to address the issue and propose DreamTalk, a framework that employs meticulous design to unlock the potential of diffusion models in generating emotional talking heads. Specifically, DreamTalk consists of three crucial components: a denoising network, a style-aware lip expert, and a style predictor. The diffusion-based denoising network can consistently synthesize high-quality audio-driven face motions across diverse emotions. To enhance lip-motion accuracy and emotional fullness, we introduce a style-aware lip expert that can guide lip-sync while preserving emotion intensity. To more conveniently specify personalized emotions, a diffusion-based style predictor is utilized to predict the personalized emotion directly from the audio, eliminating the need for extra emotion reference. By this means, DreamTalk can consistently generate vivid talking faces across diverse emotions and conveniently specify personalized emotions. Extensive experiments validate DreamTalk's effectiveness and superiority. The code is available at https://github.com/ali-vilab/dreamtalk.

</details>

### [Speech to Lip Sync generation using Deep learning Algorithm](s2:114f13f0af15e596b7e6828a35c827b51f9a0a5f.md)
**P. Hirishikesh, Mvs Yaswanth, H. A.** · 2023-12-13

<details>
<summary>Abstract</summary>

The emerging growth of artificial intelligence (AI) technology created a way for many innovative developments. Speech to lip synchronization (STLS) is one of the key requirement in applications related to film making, voice modulation, video creation etc. The identification of speaking face synchronized with the voice need to be done accurately to improve the quality of the video. Many existing systems face the problem while imposing the new audio into the existing video files. The movement of lips dynamically changes according to the speaking faces. To solve the missing synchronization problem of existing videos to retrieve the original quality from the video input, the proposed system is focused on creating accurate lip synchronization model using Deep SyncNet (DSN) using Deep learning convolution architecture. The timing accuracy of the video synchronization extensively improve the quality of the video and demands real time experience from the video footage. Detection of facial variations without extracting the features are particularly challenging. The proposed system considers the existing challenges like misclassification, delayed synchronization and evaluated the SyncNet achieved the accuracy of 95% on lip synchronization with labelled dataset.

</details>

### [GSmoothFace: Generalized Smooth Talking Face Generation via Fine Grained 3D Face Guidance](2312.07385.md)
**Haiming Zhang, Zhihao Yuan, Chaoda Zheng, Xu Yan et al.** · 2023-12-12

<details>
<summary>Abstract</summary>

Although existing speech-driven talking face generation methods achieve significant progress, they are far from real-world application due to the avatar-specific training demand and unstable lip movements. To address the above issues, we propose the GSmoothFace, a novel two-stage generalized talking face generation model guided by a fine-grained 3d face model, which can synthesize smooth lip dynamics while preserving the speaker's identity. Our proposed GSmoothFace model mainly consists of the Audio to Expression Prediction (A2EP) module and the Target Adaptive Face Translation (TAFT) module. Specifically, we first develop the A2EP module to predict expression parameters synchronized with the driven speech. It uses a transformer to capture the long-term audio context and learns the parameters from the fine-grained 3D facial vertices, resulting in accurate and smooth lip-synchronization performance. Afterward, the well-designed TAFT module, empowered by Morphology Augmented Face Blending (MAFB), takes the predicted expression parameters and target video as inputs to modify the facial region of the target video without distorting the background content. The TAFT effectively exploits the identity appearance and background context in the target video, which makes it possible to generalize to different speakers without retraining. Both quantitative and qualitative experiments confirm the superiority of our method in terms of realism, lip synchronization, and visual quality. See the project page for code, data, and request pre-trained models: https://zhanghm1995.github.io/GSmoothFace.

</details>

### [Neural Text to Articulate Talk: Deep Text to Audiovisual Speech Synthesis achieving both Auditory and Photo-realism](2312.06613.md)
**Georgios Milis, Panagiotis P. Filntisis, Anastasios Roussos, Petros Maragos** · 2023-12-11

<details>
<summary>Abstract</summary>

Recent advances in deep learning for sequential data have given rise to fast and powerful models that produce realistic videos of talking humans. The state of the art in talking face generation focuses mainly on lip-syncing, being conditioned on audio clips. However, having the ability to synthesize talking humans from text transcriptions rather than audio is particularly beneficial for many applications and is expected to receive more and more attention, following the recent breakthroughs in large language models. For that, most methods implement a cascaded 2-stage architecture of a text-to-speech module followed by an audio-driven talking face generator, but this ignores the highly complex interplay between audio and visual streams that occurs during speaking. In this paper, we propose the first, to the best of our knowledge, text-driven audiovisual speech synthesizer that uses Transformers and does not follow a cascaded approach. Our method, which we call NEUral Text to ARticulate Talk (NEUTART), is a talking face generator that uses a joint audiovisual feature space, as well as speech-informed 3D facial reconstructions and a lip-reading loss for visual supervision. The proposed model produces photorealistic talking face videos with human-like articulation and well-synced audiovisual streams. Our experiments on audiovisual datasets as well as in-the-wild videos reveal state-of-the-art generation quality both in terms of objective metrics and human evaluation.

</details>

### [DiT-Head: High-Resolution Talking Head Synthesis using Diffusion Transformers](2312.06400.md)
**Aaron Mir, Eduardo Alonso, Esther Mondragón** · 2023-12-11

<details>
<summary>Abstract</summary>

We propose a novel talking head synthesis pipeline called "DiT-Head", which is based on diffusion transformers and uses audio as a condition to drive the denoising process of a diffusion model. Our method is scalable and can generalise to multiple identities while producing high-quality results. We train and evaluate our proposed approach and compare it against existing methods of talking head synthesis. We show that our model can compete with these methods in terms of visual quality and lip-sync accuracy. Our results highlight the potential of our proposed approach to be used for a wide range of applications, including virtual assistants, entertainment, and education. For a video demonstration of the results and our user study, please refer to our supplementary material.

</details>

### [FT2TF: First-Person Statement Text-To-Talking Face Generation](2312.05430.md)
**Xingjian Diao, Ming Cheng, Wayner Barrios, SouYoung Jin** · 2023-12-09

<details>
<summary>Abstract</summary>

Talking face generation has gained immense popularity in the computer vision community, with various applications including AR, VR, teleconferencing, digital assistants, and avatars. Traditional methods are mainly audio-driven, which have to deal with the inevitable resource-intensive nature of audio storage and processing. To address such a challenge, we propose FT2TF - First-Person Statement Text-To-Talking Face Generation, a novel one-stage end-to-end pipeline for talking face generation driven by first-person statement text. Different from previous work, our model only leverages visual and textual information without any other sources (e.g., audio/landmark/pose) during inference. Extensive experiments are conducted on LRS2 and LRS3 datasets, and results on multi-dimensional evaluation metrics are reported. Both quantitative and qualitative results showcase that FT2TF outperforms existing relevant methods and reaches the state-of-the-art. This achievement highlights our model's capability to bridge first-person statements and dynamic face generation, providing insightful guidance for future work.

</details>

### [MyPortrait: Morphable Prior-Guided Personalized Portrait Generation](2312.02703.md)
**Bo Ding, Zhenfeng Fan, Shuang Yang, Shihong Xia** · 2023-12-05

<details>
<summary>Abstract</summary>

Generating realistic talking faces is an interesting and long-standing topic in the field of computer vision. Although significant progress has been made, it is still challenging to generate high-quality dynamic faces with personalized details. This is mainly due to the inability of the general model to represent personalized details and the generalization problem to unseen controllable parameters. In this work, we propose Myportrait, a simple, general, and flexible framework for neural portrait generation. We incorporate personalized prior in a monocular video and morphable prior in 3D face morphable space for generating personalized details under novel controllable parameters. Our proposed framework supports both video-driven and audio-driven face animation given a monocular video of a single person. Distinguished by whether the test data is sent to training or not, our method provides a real-time online version and a high-quality offline version. Comprehensive experiments in various metrics demonstrate the superior performance of our method over the state-of-the-art methods. The code will be publicly available.

</details>

### [AV2AV: Direct Audio-Visual Speech to Audio-Visual Speech Translation with Unified Audio-Visual Speech Representation](2312.02512.md)
**Jeongsoo Choi, Se Jin Park, Minsu Kim, Yong Man Ro** · 2023-12-05

<details>
<summary>Abstract</summary>

This paper proposes a novel direct Audio-Visual Speech to Audio-Visual Speech Translation (AV2AV) framework, where the input and output of the system are multimodal (i.e., audio and visual speech). With the proposed AV2AV, two key advantages can be brought: 1) We can perform real-like conversations with individuals worldwide in a virtual meeting by utilizing our own primary languages. In contrast to Speech-to-Speech Translation (A2A), which solely translates between audio modalities, the proposed AV2AV directly translates between audio-visual speech. This capability enhances the dialogue experience by presenting synchronized lip movements along with the translated speech. 2) We can improve the robustness of the spoken language translation system. By employing the complementary information of audio-visual speech, the system can effectively translate spoken language even in the presence of acoustic noise, showcasing robust performance. To mitigate the problem of the absence of a parallel AV2AV translation dataset, we propose to train our spoken language translation system with the audio-only dataset of A2A. This is done by learning unified audio-visual speech representations through self-supervised learning in advance to train the translation system. Moreover, we propose an AV-Renderer that can generate raw audio and video in parallel. It is designed with zero-shot speaker modeling, thus the speaker in source audio-visual speech can be maintained at the target translated audio-visual speech. The effectiveness of AV2AV is evaluated with extensive experiments in a many-to-many language translation setting. Demo page is available on https://choijeongsoo.github.io/av2av.

</details>

### [SyncTalk: The Devil is in the Synchronization for Talking Head Synthesis](2311.17590.md)
**Ziqiao Peng, Wentao Hu, Yue Shi, Xiangyu Zhu et al.** · 2023-11-29

<details>
<summary>Abstract</summary>

Achieving high synchronization in the synthesis of realistic, speech-driven talking head videos presents a significant challenge. Traditional Generative Adversarial Networks (GAN) struggle to maintain consistent facial identity, while Neural Radiance Fields (NeRF) methods, although they can address this issue, often produce mismatched lip movements, inadequate facial expressions, and unstable head poses. A lifelike talking head requires synchronized coordination of subject identity, lip movements, facial expressions, and head poses. The absence of these synchronizations is a fundamental flaw, leading to unrealistic and artificial outcomes. To address the critical issue of synchronization, identified as the "devil" in creating realistic talking heads, we introduce SyncTalk. This NeRF-based method effectively maintains subject identity, enhancing synchronization and realism in talking head synthesis. SyncTalk employs a Face-Sync Controller to align lip movements with speech and innovatively uses a 3D facial blendshape model to capture accurate facial expressions. Our Head-Sync Stabilizer optimizes head poses, achieving more natural head movements. The Portrait-Sync Generator restores hair details and blends the generated head with the torso for a seamless visual experience. Extensive experiments and user studies demonstrate that SyncTalk outperforms state-of-the-art methods in synchronization and realism. We recommend watching the supplementary video: https://ziqiaopeng.github.io/synctalk

</details>

### [Talking Head(?) Anime from a Single Image 4: Improved Model and Its Distillation](2311.17409.md)
**Pramook Khungurn** · 2023-11-29

<details>
<summary>Abstract</summary>

We study the problem of creating a character model that can be controlled in real time from a single image of an anime character. A solution to this problem would greatly reduce the cost of creating avatars, computer games, and other interactive applications. Talking Head Anime 3 (THA3) is an open source project that attempts to directly address the problem. It takes as input (1) an image of an anime character's upper body and (2) a 45-dimensional pose vector and outputs a new image of the same character taking the specified pose. The range of possible movements is expressive enough for personal avatars and certain types of game characters. However, the system is too slow to generate animations in real time on common PCs, and its image quality can be improved. In this paper, we improve THA3 in two ways. First, we propose new architectures for constituent networks that rotate the character's head and body based on U-Nets with attention that are widely used in modern generative models. The new architectures consistently yield better image quality than the THA3 baseline. Nevertheless, they also make the whole system much slower: it takes up to 150 milliseconds to generate a frame. Second, we propose a technique to distill the system into a small network (less than 2 MB) that can generate 512x512 animation frames in real time (under 30 FPS) using consumer gaming GPUs while keeping the image quality close to that of the full system. This improvement makes the whole system practical for real-time applications.

</details>

### [THInImg: Cross-modal Steganography for Presenting Talking Heads in Images](2311.17177.md)
**Lin Zhao, Hongxuan Li, Xuefei Ning, Xinru Jiang** · 2023-11-28

<details>
<summary>Abstract</summary>

Cross-modal Steganography is the practice of concealing secret signals in publicly available cover signals (distinct from the modality of the secret signals) unobtrusively. While previous approaches primarily concentrated on concealing a relatively small amount of information, we propose THInImg, which manages to hide lengthy audio data (and subsequently decode talking head video) inside an identity image by leveraging the properties of human face, which can be effectively utilized for covert communication, transmission and copyright protection. THInImg consists of two parts: the encoder and decoder. Inside the encoder-decoder pipeline, we introduce a novel architecture that substantially increase the capacity of hiding audio in images. Moreover, our framework can be extended to iteratively hide multiple audio clips into an identity image, offering multiple levels of control over permissions. We conduct extensive experiments to prove the effectiveness of our method, demonstrating that THInImg can present up to 80 seconds of high quality talking-head video (including audio) in an identity image with 160x160 resolution.

</details>

### [GAIA: Zero-shot Talking Avatar Generation](2311.15230.md)
**Tianyu He, Junliang Guo, Runyi Yu, Yuchi Wang et al.** · 2023-11-26

<details>
<summary>Abstract</summary>

Zero-shot talking avatar generation aims at synthesizing natural talking videos from speech and a single portrait image. Previous methods have relied on domain-specific heuristics such as warping-based motion representation and 3D Morphable Models, which limit the naturalness and diversity of the generated avatars. In this work, we introduce GAIA (Generative AI for Avatar), which eliminates the domain priors in talking avatar generation. In light of the observation that the speech only drives the motion of the avatar while the appearance of the avatar and the background typically remain the same throughout the entire video, we divide our approach into two stages: 1) disentangling each frame into motion and appearance representations; 2) generating motion sequences conditioned on the speech and reference portrait image. We collect a large-scale high-quality talking avatar dataset and train the model on it with different scales (up to 2B parameters). Experimental results verify the superiority, scalability, and flexibility of GAIA as 1) the resulting model beats previous baseline models in terms of naturalness, diversity, lip-sync quality, and visual quality; 2) the framework is scalable since larger models yield better results; 3) it is general and enables different applications like controllable talking avatar generation and text-instructed avatar generation.

</details>

### [CP-EB: Talking Face Generation with Controllable Pose and Eye Blinking Embedding](2311.08673.md)
**Jianzong Wang, Yimin Deng, Ziqi Liang, Xulong Zhang et al.** · 2023-11-15

<details>
<summary>Abstract</summary>

This paper proposes a talking face generation method named "CP-EB" that takes an audio signal as input and a person image as reference, to synthesize a photo-realistic people talking video with head poses controlled by a short video clip and proper eye blinking embedding. It's noted that not only the head pose but also eye blinking are both important aspects for deep fake detection. The implicit control of poses by video has already achieved by the state-of-art work. According to recent research, eye blinking has weak correlation with input audio which means eye blinks extraction from audio and generation are possible. Hence, we propose a GAN-based architecture to extract eye blink feature from input audio and reference video respectively and employ contrastive training between them, then embed it into the concatenated features of identity and poses to generate talking face images. Experimental results show that the proposed method can generate photo-realistic talking face with synchronous lips motions, natural head poses and blinking eyes.

</details>

### [Audiovisual Inputs for Learning Robust, Real-time Facial Animation with Lip Sync](s2:54659fdee52c7a090e51ae4b2db50110e7aeba68.md)
**Iñaki Navarro, Dario Kneubuehler, Tijmen Verhulsdonck, Eloi Du Bois et al.** · 2023-11-15

<details>
<summary>Abstract</summary>

We present an approach for generating facial animation that combines video and audio input data in real time for low-end devices through deep learning. Our method produces control signals from audiovisual inputs separately, and mixes them to animate a character rig. The architecture relies on two specialized networks that are trained on a combination of synthetic and real world data and are highly engineered to be efficient in order to support quality avatar faces even on low-end devices. In addition, the system supports several levels of detail that degrade gracefully for additional scaling and efficiency. We showcase how user testing has been employed to improve performance and a comparison with state of the art.

</details>

### [ChatAnything: Facetime Chat with LLM-Enhanced Personas](2311.06772.md)
**Yilin Zhao, Xinbin Yuan, Shanghua Gao, Zhijie Lin et al.** · 2023-11-12

<details>
<summary>Abstract</summary>

In this technical report, we target generating anthropomorphized personas for LLM-based characters in an online manner, including visual appearance, personality and tones, with only text descriptions. To achieve this, we first leverage the in-context learning capability of LLMs for personality generation by carefully designing a set of system prompts. We then propose two novel concepts: the mixture of voices (MoV) and the mixture of diffusers (MoD) for diverse voice and appearance generation. For MoV, we utilize the text-to-speech (TTS) algorithms with a variety of pre-defined tones and select the most matching one based on the user-provided text description automatically. For MoD, we combine the recent popular text-to-image generation techniques and talking head algorithms to streamline the process of generating talking objects. We termed the whole framework as ChatAnything. With it, users could be able to animate anything with any personas that are anthropomorphic using just a few text inputs. However, we have observed that the anthropomorphic objects produced by current generative models are often undetectable by pre-trained face landmark detectors, leading to failure of the face motion generation, even if these faces possess human-like appearances because those images are nearly seen during the training (e.g., OOD samples). To address this issue, we incorporate pixel-level guidance to infuse human face landmarks during the image generation phase. To benchmark these metrics, we have built an evaluation dataset. Based on it, we verify that the detection rate of the face landmark is significantly increased from 57.0% to 92.5% thus allowing automatic face animation based on generated speech content. The code and more results can be found at https://chatanything.github.io/.

</details>

### [BakedAvatar: Baking Neural Fields for Real-Time Head Avatar Synthesis](2311.05521.md)
**Hao-Bin Duan, Miao Wang, Jin-Chuan Shi, Xu-Chuan Chen et al.** · 2023-11-09

<details>
<summary>Abstract</summary>

Synthesizing photorealistic 4D human head avatars from videos is essential for VR/AR, telepresence, and video game applications. Although existing Neural Radiance Fields (NeRF)-based methods achieve high-fidelity results, the computational expense limits their use in real-time applications. To overcome this limitation, we introduce BakedAvatar, a novel representation for real-time neural head avatar synthesis, deployable in a standard polygon rasterization pipeline. Our approach extracts deformable multi-layer meshes from learned isosurfaces of the head and computes expression-, pose-, and view-dependent appearances that can be baked into static textures for efficient rasterization. We thus propose a three-stage pipeline for neural head avatar synthesis, which includes learning continuous deformation, manifold, and radiance fields, extracting layered meshes and textures, and fine-tuning texture details with differential rasterization. Experimental results demonstrate that our representation generates synthesis results of comparable quality to other state-of-the-art methods while significantly reducing the inference time required. We further showcase various head avatar synthesis results from monocular videos, including view synthesis, face reenactment, expression editing, and pose editing, all at interactive frame rates.

</details>

### [Synthetic Speaking Children -- Why We Need Them and How to Make Them](2311.06307.md)
**Muhammad Ali Farooq, Dan Bigioi, Rishabh Jain, Wang Yao et al.** · 2023-11-08

<details>
<summary>Abstract</summary>

Contemporary Human Computer Interaction (HCI) research relies primarily on neural network models for machine vision and speech understanding of a system user. Such models require extensively annotated training datasets for optimal performance and when building interfaces for users from a vulnerable population such as young children, GDPR introduces significant complexities in data collection, management, and processing. Motivated by the training needs of an Edge AI smart toy platform this research explores the latest advances in generative neural technologies and provides a working proof of concept of a controllable data generation pipeline for speech driven facial training data at scale. In this context, we demonstrate how StyleGAN2 can be finetuned to create a gender balanced dataset of children's faces. This dataset includes a variety of controllable factors such as facial expressions, age variations, facial poses, and even speech-driven animations with realistic lip synchronization. By combining generative text to speech models for child voice synthesis and a 3D landmark based talking heads pipeline, we can generate highly realistic, entirely synthetic, talking child video clips. These video clips can provide valuable, and controllable, synthetic training data for neural network models, bridging the gap when real data is scarce or restricted due to privacy regulations.

</details>

### [DiffDub: Person-generic Visual Dubbing Using Inpainting Renderer with Diffusion Auto-encoder](2311.01811.md)
**Tao Liu, Chenpeng Du, Shuai Fan, Feilong Chen et al.** · 2023-11-03

<details>
<summary>Abstract</summary>

Generating high-quality and person-generic visual dubbing remains a challenge. Recent innovation has seen the advent of a two-stage paradigm, decoupling the rendering and lip synchronization process facilitated by intermediate representation as a conduit. Still, previous methodologies rely on rough landmarks or are confined to a single speaker, thus limiting their performance. In this paper, we propose DiffDub: Diffusion-based dubbing. We first craft the Diffusion auto-encoder by an inpainting renderer incorporating a mask to delineate editable zones and unaltered regions. This allows for seamless filling of the lower-face region while preserving the remaining parts. Throughout our experiments, we encountered several challenges. Primarily, the semantic encoder lacks robustness, constricting its ability to capture high-level features. Besides, the modeling ignored facial positioning, causing mouth or nose jitters across frames. To tackle these issues, we employ versatile strategies, including data augmentation and supplementary eye guidance. Moreover, we encapsulated a conformer-based reference encoder and motion generator fortified by a cross-attention mechanism. This enables our model to learn person-specific textures with varying references and reduces reliance on paired audio-visual data. Our rigorous experiments comprehensively highlight that our ground-breaking approach outpaces existing methods with considerable margins and delivers seamless, intelligible videos in person-generic and multilingual scenarios.

</details>

### [Seeing Through the Conversation: Audio-Visual Speech Separation based on Diffusion Model](2310.19581.md)
**Suyeon Lee, Chaeyoung Jung, Youngjoon Jang, Jaehun Kim et al.** · 2023-10-30

<details>
<summary>Abstract</summary>

The objective of this work is to extract target speaker's voice from a mixture of voices using visual cues. Existing works on audio-visual speech separation have demonstrated their performance with promising intelligibility, but maintaining naturalness remains a challenge. To address this issue, we propose AVDiffuSS, an audio-visual speech separation model based on a diffusion mechanism known for its capability in generating natural samples. For an effective fusion of the two modalities for diffusion, we also propose a cross-attention-based feature fusion mechanism. This mechanism is specifically tailored for the speech domain to integrate the phonetic information from audio-visual correspondence in speech generation. In this way, the fusion process maintains the high temporal resolution of the features, without excessive computational requirements. We demonstrate that the proposed framework achieves state-of-the-art results on two benchmarks, including VoxCeleb2 and LRS3, producing speech with notably better naturalness.

</details>

### [GestSync: Determining who is speaking without a talking head](2310.05304.md)
**Sindhu B Hegde, Andrew Zisserman** · 2023-10-08

<details>
<summary>Abstract</summary>

In this paper we introduce a new synchronisation task, Gesture-Sync: determining if a person's gestures are correlated with their speech or not. In comparison to Lip-Sync, Gesture-Sync is far more challenging as there is a far looser relationship between the voice and body movement than there is between voice and lip motion. We introduce a dual-encoder model for this task, and compare a number of input representations including RGB frames, keypoint images, and keypoint vectors, assessing their performance and advantages. We show that the model can be trained using self-supervised learning alone, and evaluate its performance on the LRS3 dataset. Finally, we demonstrate applications of Gesture-Sync for audio-visual synchronisation, and in determining who is the speaker in a crowd, without seeing their faces. The code, datasets and pre-trained models can be found at: \url{https://www.robots.ox.ac.uk/~vgg/research/gestsync}.

</details>

### [DiffPoseTalk: Speech-Driven Stylistic 3D Facial Animation and Head Pose Generation via Diffusion Models](2310.00434.md)
**Zhiyao Sun, Tian Lv, Sheng Ye, Matthieu Lin et al.** · 2023-09-30

<details>
<summary>Abstract</summary>

The generation of stylistic 3D facial animations driven by speech presents a significant challenge as it requires learning a many-to-many mapping between speech, style, and the corresponding natural facial motion. However, existing methods either employ a deterministic model for speech-to-motion mapping or encode the style using a one-hot encoding scheme. Notably, the one-hot encoding approach fails to capture the complexity of the style and thus limits generalization ability. In this paper, we propose DiffPoseTalk, a generative framework based on the diffusion model combined with a style encoder that extracts style embeddings from short reference videos. During inference, we employ classifier-free guidance to guide the generation process based on the speech and style. In particular, our style includes the generation of head poses, thereby enhancing user perception. Additionally, we address the shortage of scanned 3D talking face data by training our model on reconstructed 3DMM parameters from a high-quality, in-the-wild audio-visual dataset. Extensive experiments and user study demonstrate that our approach outperforms state-of-the-art methods. The code and dataset are at https://diffposetalk.github.io .

</details>

### [DT-NeRF: Decomposed Triplane-Hash Neural Radiance Fields for High-Fidelity Talking Portrait Synthesis](2309.07752.md)
**Yaoyu Su, Shaohui Wang, Haoqian Wang** · 2023-09-14

<details>
<summary>Abstract</summary>

In this paper, we present the decomposed triplane-hash neural radiance fields (DT-NeRF), a framework that significantly improves the photorealistic rendering of talking faces and achieves state-of-the-art results on key evaluation datasets. Our architecture decomposes the facial region into two specialized triplanes: one specialized for representing the mouth, and the other for the broader facial features. We introduce audio features as residual terms and integrate them as query vectors into our model through an audio-mouth-face transformer. Additionally, our method leverages the capabilities of Neural Radiance Fields (NeRF) to enrich the volumetric representation of the entire face through additive volumetric rendering techniques. Comprehensive experimental evaluations corroborate the effectiveness and superiority of our proposed approach.

</details>

### [DiffTalker: Co-driven audio-image diffusion for talking faces via intermediate landmarks](2309.07509.md)
**Zipeng Qi, Xulong Zhang, Ning Cheng, Jing Xiao et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

Generating realistic talking faces is a complex and widely discussed task with numerous applications. In this paper, we present DiffTalker, a novel model designed to generate lifelike talking faces through audio and landmark co-driving. DiffTalker addresses the challenges associated with directly applying diffusion models to audio control, which are traditionally trained on text-image pairs. DiffTalker consists of two agent networks: a transformer-based landmarks completion network for geometric accuracy and a diffusion-based face generation network for texture details. Landmarks play a pivotal role in establishing a seamless connection between the audio and image domains, facilitating the incorporation of knowledge from pre-trained diffusion models. This innovative approach efficiently produces articulate-speaking faces. Experimental results showcase DiffTalker's superior performance in producing clear and geometrically accurate talking faces, all without the need for additional alignment between audio and image features.

</details>

### [AV2Wav: Diffusion-Based Re-synthesis from Continuous Self-supervised Features for Audio-Visual Speech Enhancement](2309.08030.md)
**Ju-Chieh Chou, Chung-Ming Chien, Karen Livescu** · 2023-09-14

<details>
<summary>Abstract</summary>

Speech enhancement systems are typically trained using pairs of clean and noisy speech. In audio-visual speech enhancement (AVSE), there is not as much ground-truth clean data available; most audio-visual datasets are collected in real-world environments with background noise and reverberation, hampering the development of AVSE. In this work, we introduce AV2Wav, a resynthesis-based audio-visual speech enhancement approach that can generate clean speech despite the challenges of real-world training data. We obtain a subset of nearly clean speech from an audio-visual corpus using a neural quality estimator, and then train a diffusion model on this subset to generate waveforms conditioned on continuous speech representations from AV-HuBERT with noise-robust training. We use continuous rather than discrete representations to retain prosody and speaker information. With this vocoding task alone, the model can perform speech enhancement better than a masking-based baseline. We further fine-tune the diffusion model on clean/noisy utterance pairs to improve the performance. Our approach outperforms a masking-based baseline in terms of both automatic metrics and a human listening test and is close in quality to the target speech in the listening test. Audio samples can be found at https://home.ttic.edu/~jcchou/demo/avse/avse_demo.html.

</details>

### [DF-TransFusion: Multimodal Deepfake Detection via Lip-Audio Cross-Attention and Facial Self-Attention](2309.06511.md)
**Aaditya Kharel, Manas Paranjape, Aniket Bera** · 2023-09-12

<details>
<summary>Abstract</summary>

With the rise in manipulated media, deepfake detection has become an imperative task for preserving the authenticity of digital content. In this paper, we present a novel multi-modal audio-video framework designed to concurrently process audio and video inputs for deepfake detection tasks. Our model capitalizes on lip synchronization with input audio through a cross-attention mechanism while extracting visual cues via a fine-tuned VGG-16 network. Subsequently, a transformer encoder network is employed to perform facial self-attention. We conduct multiple ablation studies highlighting different strengths of our approach. Our multi-modal methodology outperforms state-of-the-art multi-modal deepfake detection techniques in terms of F-1 and per-video AUC scores.

</details>

### [Efficient Emotional Adaptation for Audio-Driven Talking-Head Generation](2309.04946.md)
**Yuan Gan, Zongxin Yang, Xihang Yue, Lingyun Sun et al.** · 2023-09-10

<details>
<summary>Abstract</summary>

Audio-driven talking-head synthesis is a popular research topic for virtual human-related applications. However, the inflexibility and inefficiency of existing methods, which necessitate expensive end-to-end training to transfer emotions from guidance videos to talking-head predictions, are significant limitations. In this work, we propose the Emotional Adaptation for Audio-driven Talking-head (EAT) method, which transforms emotion-agnostic talking-head models into emotion-controllable ones in a cost-effective and efficient manner through parameter-efficient adaptations. Our approach utilizes a pretrained emotion-agnostic talking-head transformer and introduces three lightweight adaptations (the Deep Emotional Prompts, Emotional Deformation Network, and Emotional Adaptation Module) from different perspectives to enable precise and realistic emotion controls. Our experiments demonstrate that our approach achieves state-of-the-art performance on widely-used benchmarks, including LRW and MEAD. Additionally, our parameter-efficient adaptations exhibit remarkable generalization ability, even in scenarios where emotional training videos are scarce or nonexistent. Project website: https://yuangan.github.io/eat/

</details>

### [From Pixels to Portraits: A Comprehensive Survey of Talking Head Generation Techniques and Applications](2308.16041.md)
**Shreyank N Gowda, Dheeraj Pandey, Shashank Narayana Gowda** · 2023-08-30

<details>
<summary>Abstract</summary>

Recent advancements in deep learning and computer vision have led to a surge of interest in generating realistic talking heads. This paper presents a comprehensive survey of state-of-the-art methods for talking head generation. We systematically categorises them into four main approaches: image-driven, audio-driven, video-driven and others (including neural radiance fields (NeRF), and 3D-based methods). We provide an in-depth analysis of each method, highlighting their unique contributions, strengths, and limitations. Furthermore, we thoroughly compare publicly available models, evaluating them on key aspects such as inference time and human-rated quality of the generated outputs. Our aim is to provide a clear and concise overview of the current landscape in talking head generation, elucidating the relationships between different approaches and identifying promising directions for future research. This survey will serve as a valuable reference for researchers and practitioners interested in this rapidly evolving field.

</details>

### [ToonTalker: Cross-Domain Face Reenactment](2308.12866.md)
**Yuan Gong, Yong Zhang, Xiaodong Cun, Fei Yin et al.** · 2023-08-24

<details>
<summary>Abstract</summary>

We target cross-domain face reenactment in this paper, i.e., driving a cartoon image with the video of a real person and vice versa. Recently, many works have focused on one-shot talking face generation to drive a portrait with a real video, i.e., within-domain reenactment. Straightforwardly applying those methods to cross-domain animation will cause inaccurate expression transfer, blur effects, and even apparent artifacts due to the domain shift between cartoon and real faces. Only a few works attempt to settle cross-domain face reenactment. The most related work AnimeCeleb requires constructing a dataset with pose vector and cartoon image pairs by animating 3D characters, which makes it inapplicable anymore if no paired data is available. In this paper, we propose a novel method for cross-domain reenactment without paired data. Specifically, we propose a transformer-based framework to align the motions from different domains into a common latent space where motion transfer is conducted via latent code addition. Two domain-specific motion encoders and two learnable motion base memories are used to capture domain properties. A source query transformer and a driving one are exploited to project domain-specific motion to the canonical space. The edited motion is projected back to the domain of the source with a transformer. Moreover, since no paired data is provided, we propose a novel cross-domain training scheme using data from two domains with the designed analogy constraint. Besides, we contribute a cartoon dataset in Disney style. Extensive evaluations demonstrate the superiority of our method over competing methods.

</details>

### [Diff2Lip: Audio Conditioned Diffusion Models for Lip-Synchronization](2308.09716.md)
**Soumik Mukhopadhyay, Saksham Suri, Ravi Teja Gadde, Abhinav Shrivastava** · 2023-08-18

<details>
<summary>Abstract</summary>

The task of lip synchronization (lip-sync) seeks to match the lips of human faces with different audio. It has various applications in the film industry as well as for creating virtual avatars and for video conferencing. This is a challenging problem as one needs to simultaneously introduce detailed, realistic lip movements while preserving the identity, pose, emotions, and image quality. Many of the previous methods trying to solve this problem suffer from image quality degradation due to a lack of complete contextual information. In this paper, we present Diff2Lip, an audio-conditioned diffusion-based model which is able to do lip synchronization in-the-wild while preserving these qualities. We train our model on Voxceleb2, a video dataset containing in-the-wild talking face videos. Extensive studies show that our method outperforms popular methods like Wav2Lip and PC-AVS in Fréchet inception distance (FID) metric and Mean Opinion Scores (MOS) of the users. We show results on both reconstruction (same audio-video inputs) as well as cross (different audio-video inputs) settings on Voxceleb2 and LRW datasets. Video results and code can be accessed from our project page ( https://soumik-kanad.github.io/diff2lip ).

</details>

### [A Survey on Deep Multi-modal Learning for Body Language Recognition and Generation](2308.08849.md)
**Li Liu, Lufei Gao, Wentao Lei, Fengji Ma et al.** · 2023-08-17

<details>
<summary>Abstract</summary>

Body language (BL) refers to the non-verbal communication expressed through physical movements, gestures, facial expressions, and postures. It is a form of communication that conveys information, emotions, attitudes, and intentions without the use of spoken or written words. It plays a crucial role in interpersonal interactions and can complement or even override verbal communication. Deep multi-modal learning techniques have shown promise in understanding and analyzing these diverse aspects of BL. The survey emphasizes their applications to BL generation and recognition. Several common BLs are considered i.e., Sign Language (SL), Cued Speech (CS), Co-speech (CoS), and Talking Head (TH), and we have conducted an analysis and established the connections among these four BL for the first time. Their generation and recognition often involve multi-modal approaches. Benchmark datasets for BL research are well collected and organized, along with the evaluation of SOTA methods on these datasets. The survey highlights challenges such as limited labeled data, multi-modal learning, and the need for domain adaptation to generalize models to unseen speakers or languages. Future research directions are presented, including exploring self-supervised learning techniques, integrating contextual information from other modalities, and exploiting large-scale pre-trained multi-modal models. In summary, this survey paper provides a comprehensive understanding of deep multi-modal learning for various BL generations and recognitions for the first time. By analyzing advancements, challenges, and future directions, it serves as a valuable resource for researchers and practitioners in advancing this field. n addition, we maintain a continuously updated paper list for deep multi-modal learning for BL recognition and generation: https://github.com/wentaoL86/awesome-body-language.

</details>

### [IIANet: An Intra- and Inter-Modality Attention Network for Audio-Visual Speech Separation](2308.08143.md)
**Kai Li, Runxuan Yang, Fuchun Sun, Xiaolin Hu** · 2023-08-16

<details>
<summary>Abstract</summary>

Recent research has made significant progress in designing fusion modules for audio-visual speech separation. However, they predominantly focus on multi-modal fusion at a single temporal scale of auditory and visual features without employing selective attention mechanisms, which is in sharp contrast with the brain. To address this issue, We propose a novel model called Intra- and Inter-Attention Network (IIANet), which leverages the attention mechanism for efficient audio-visual feature fusion. IIANet consists of two types of attention blocks: intra-attention (IntraA) and inter-attention (InterA) blocks, where the InterA blocks are distributed at the top, middle and bottom of IIANet. Heavily inspired by the way how human brain selectively focuses on relevant content at various temporal scales, these blocks maintain the ability to learn modality-specific features and enable the extraction of different semantics from audio-visual features. Comprehensive experiments on three standard audio-visual separation benchmarks (LRS2, LRS3, and VoxCeleb2) demonstrate the effectiveness of IIANet, outperforming previous state-of-the-art methods while maintaining comparable inference time. In particular, the fast version of IIANet (IIANet-fast) has only 7% of CTCNet's MACs and is 40% faster than CTCNet on CPUs while achieving better separation quality, showing the great potential of attention mechanism for efficient and effective multimodal fusion.

</details>

### [Context-Aware Talking-Head Video Editing](2308.00462.md)
**Songlin Yang, Wei Wang, Jun Ling, Bo Peng et al.** · 2023-08-01

<details>
<summary>Abstract</summary>

Talking-head video editing aims to efficiently insert, delete, and substitute the word of a pre-recorded video through a text transcript editor. The key challenge for this task is obtaining an editing model that generates new talking-head video clips which simultaneously have accurate lip synchronization and motion smoothness. Previous approaches, including 3DMM-based (3D Morphable Model) methods and NeRF-based (Neural Radiance Field) methods, are sub-optimal in that they either require minutes of source videos and days of training time or lack the disentangled control of verbal (e.g., lip motion) and non-verbal (e.g., head pose and expression) representations for video clip insertion. In this work, we fully utilize the video context to design a novel framework for talking-head video editing, which achieves efficiency, disentangled motion control, and sequential smoothness. Specifically, we decompose this framework to motion prediction and motion-conditioned rendering: (1) We first design an animation prediction module that efficiently obtains smooth and lip-sync motion sequences conditioned on the driven speech. This module adopts a non-autoregressive network to obtain context prior and improve the prediction efficiency, and it learns a speech-animation mapping prior with better generalization to novel speech from a multi-identity video dataset. (2) We then introduce a neural rendering module to synthesize the photo-realistic and full-head video frames given the predicted motion sequence. This module adopts a pre-trained head topology and uses only few frames for efficient fine-tuning to obtain a person-specific rendering model. Extensive experiments demonstrate that our method efficiently achieves smoother editing results with higher image quality and lip accuracy using less data than previous methods.

</details>

### [HyperReenact: One-Shot Reenactment via Jointly Learning to Refine and Retarget Faces](2307.10797.md)
**Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras et al.** · 2023-07-20

<details>
<summary>Abstract</summary>

In this paper, we present our method for neural face reenactment, called HyperReenact, that aims to generate realistic talking head images of a source identity, driven by a target facial pose. Existing state-of-the-art face reenactment methods train controllable generative models that learn to synthesize realistic facial images, yet producing reenacted faces that are prone to significant visual artifacts, especially under the challenging condition of extreme head pose changes, or requiring expensive few-shot fine-tuning to better preserve the source identity characteristics. We propose to address these limitations by leveraging the photorealistic generation ability and the disentangled properties of a pretrained StyleGAN2 generator, by first inverting the real images into its latent space and then using a hypernetwork to perform: (i) refinement of the source identity characteristics and (ii) facial pose re-targeting, eliminating this way the dependence on external editing methods that typically produce artifacts. Our method operates under the one-shot setting (i.e., using a single source frame) and allows for cross-subject reenactment, without requiring any subject-specific fine-tuning. We compare our method both quantitatively and qualitatively against several state-of-the-art techniques on the standard benchmarks of VoxCeleb1 and VoxCeleb2, demonstrating the superiority of our approach in producing artifact-free images, exhibiting remarkable robustness even under extreme head pose changes. We make the code and the pretrained models publicly available at: https://github.com/StelaBou/HyperReenact .

</details>

### [FACTS: Facial Animation Creation using the Transfer of Styles](2307.09480.md)
**Jack Saunders, Steven Caulkin, Vinay Namboodiri** · 2023-07-18

<details>
<summary>Abstract</summary>

The ability to accurately capture and express emotions is a critical aspect of creating believable characters in video games and other forms of entertainment. Traditionally, this animation has been achieved with artistic effort or performance capture, both requiring costs in time and labor. More recently, audio-driven models have seen success, however, these often lack expressiveness in areas not correlated to the audio signal. In this paper, we present a novel approach to facial animation by taking existing animations and allowing for the modification of style characteristics. Specifically, we explore the use of a StarGAN to enable the conversion of 3D facial animations into different emotions and person-specific styles. We are able to maintain the lip-sync of the animations with this method thanks to the use of a novel viseme-preserving loss.

</details>

### [OPHAvatars: One-shot Photo-realistic Head Avatars](2307.09153.md)
**Shaoxu Li** · 2023-07-18

<details>
<summary>Abstract</summary>

We propose a method for synthesizing photo-realistic digital avatars from only one portrait as the reference. Given a portrait, our method synthesizes a coarse talking head video using driving keypoints features. And with the coarse video, our method synthesizes a coarse talking head avatar with a deforming neural radiance field. With rendered images of the coarse avatar, our method updates the low-quality images with a blind face restoration model. With updated images, we retrain the avatar for higher quality. After several iterations, our method can synthesize a photo-realistic animatable 3D neural head avatar. The motivation of our method is deformable neural radiance field can eliminate the unnatural distortion caused by the image2video method. Our method outperforms state-of-the-art methods in quantitative and qualitative studies on various subjects.

</details>

### [On the Vulnerability of DeepFake Detectors to Attacks Generated by Denoising Diffusion Models](2307.05397.md)
**Marija Ivanovska, Vitomir Štruc** · 2023-07-11

<details>
<summary>Abstract</summary>

The detection of malicious deepfakes is a constantly evolving problem that requires continuous monitoring of detectors to ensure they can detect image manipulations generated by the latest emerging models. In this paper, we investigate the vulnerability of single-image deepfake detectors to black-box attacks created by the newest generation of generative methods, namely Denoising Diffusion Models (DDMs). Our experiments are run on FaceForensics++, a widely used deepfake benchmark consisting of manipulated images generated with various techniques for face identity swapping and face reenactment. Attacks are crafted through guided reconstruction of existing deepfakes with a proposed DDM approach for face restoration. Our findings indicate that employing just a single denoising diffusion step in the reconstruction process of a deepfake can significantly reduce the likelihood of detection, all without introducing any perceptible image modifications. While training detectors using attack examples demonstrated some effectiveness, it was observed that discriminators trained on fully diffusion-based deepfakes exhibited limited generalizability when presented with our attacks.

</details>

### [A Comprehensive Multi-scale Approach for Speech and Dynamics Synchrony in Talking Head Generation](2307.03270.md)
**Louis Airale, Dominique Vaufreydaz, Xavier Alameda-Pineda** · 2023-07-04

<details>
<summary>Abstract</summary>

Animating still face images with deep generative models using a speech input signal is an active research topic and has seen important recent progress.However, much of the effort has been put into lip syncing and rendering quality while the generation of natural head motion, let alone the audio-visual correlation between head motion and speech, has often been neglected.In this work, we propose a multi-scale audio-visual synchrony loss and a multi-scale autoregressive GAN to better handle short and long-term correlation between speech and the dynamics of the head and lips.In particular, we train a stack of syncer models on multimodal input pyramids and use these models as guidance in a multi-scale generator network to produce audio-aligned motion unfolding over diverse time scales.Both the pyramid of audio-visual syncers and the generative models are trained in a low-dimensional space that fully preserves dynamics cues.The experiments show significant improvements over the state-of-the-art in head motion dynamics quality and especially in multi-scale audio-visual synchrony on a collection of benchmark datasets.

</details>

### [RobustL2S: Speaker-Specific Lip-to-Speech Synthesis exploiting Self-Supervised Representations](2307.01233.md)
**Neha Sahipjohn, Neil Shah, Vishal Tambrahalli, Vineet Gandhi** · 2023-07-03

<details>
<summary>Abstract</summary>

Significant progress has been made in speaker dependent Lip-to-Speech synthesis, which aims to generate speech from silent videos of talking faces. Current state-of-the-art approaches primarily employ non-autoregressive sequence-to-sequence architectures to directly predict mel-spectrograms or audio waveforms from lip representations. We hypothesize that the direct mel-prediction hampers training/model efficiency due to the entanglement of speech content with ambient information and speaker characteristics. To this end, we propose RobustL2S, a modularized framework for Lip-to-Speech synthesis. First, a non-autoregressive sequence-to-sequence model maps self-supervised visual features to a representation of disentangled speech content. A vocoder then converts the speech features into raw waveforms. Extensive evaluations confirm the effectiveness of our setup, achieving state-of-the-art performance on the unconstrained Lip2Wav dataset and the constrained GRID and TCD-TIMIT datasets. Speech samples from RobustL2S can be found at https://neha-sherin.github.io/RobustL2S/

</details>

### [Instruct-NeuralTalker: Editing Audio-Driven Talking Radiance Fields with Instructions](2306.10813.md)
**Yuqi Sun, Ruian He, Weimin Tan, Bo Yan** · 2023-06-19

<details>
<summary>Abstract</summary>

Recent neural talking radiance field methods have shown great success in photorealistic audio-driven talking face synthesis. In this paper, we propose a novel interactive framework that utilizes human instructions to edit such implicit neural representations to achieve real-time personalized talking face generation. Given a short speech video, we first build an efficient talking radiance field, and then apply the latest conditional diffusion model for image editing based on the given instructions and guiding implicit representation optimization towards the editing target. To ensure audio-lip synchronization during the editing process, we propose an iterative dataset updating strategy and utilize a lip-edge loss to constrain changes in the lip region. We also introduce a lightweight refinement network for complementing image details and achieving controllable detail generation in the final rendered image. Our method also enables real-time rendering at up to 30FPS on consumer hardware. Multiple metrics and user verification show that our approach provides a significant improvement in rendering quality compared to state-of-the-art methods.

</details>

### [SelfTalk: A Self-Supervised Commutative Training Diagram to Comprehend 3D Talking Faces](2306.10799.md)
**Ziqiao Peng, Yihao Luo, Yue Shi, Hao Xu et al.** · 2023-06-19

<details>
<summary>Abstract</summary>

Speech-driven 3D face animation technique, extending its applications to various multimedia fields. Previous research has generated promising realistic lip movements and facial expressions from audio signals. However, traditional regression models solely driven by data face several essential problems, such as difficulties in accessing precise labels and domain gaps between different modalities, leading to unsatisfactory results lacking precision and coherence. To enhance the visual accuracy of generated lip movement while reducing the dependence on labeled data, we propose a novel framework SelfTalk, by involving self-supervision in a cross-modals network system to learn 3D talking faces. The framework constructs a network system consisting of three modules: facial animator, speech recognizer, and lip-reading interpreter. The core of SelfTalk is a commutative training diagram that facilitates compatible features exchange among audio, text, and lip shape, enabling our models to learn the intricate connection between these factors. The proposed framework leverages the knowledge learned from the lip-reading interpreter to generate more plausible lip shapes. Extensive experiments and user studies demonstrate that our proposed approach achieves state-of-the-art performance both qualitatively and quantitatively. We recommend watching the supplementary video.

</details>

### [Parametric Implicit Face Representation for Audio-Driven Facial Reenactment](2306.07579.md)
**Ricong Huang, Peiwen Lai, Yipeng Qin, Guanbin Li** · 2023-06-13

<details>
<summary>Abstract</summary>

Audio-driven facial reenactment is a crucial technique that has a range of applications in film-making, virtual avatars and video conferences. Existing works either employ explicit intermediate face representations (e.g., 2D facial landmarks or 3D face models) or implicit ones (e.g., Neural Radiance Fields), thus suffering from the trade-offs between interpretability and expressive power, hence between controllability and quality of the results. In this work, we break these trade-offs with our novel parametric implicit face representation and propose a novel audio-driven facial reenactment framework that is both controllable and can generate high-quality talking heads. Specifically, our parametric implicit representation parameterizes the implicit representation with interpretable parameters of 3D face models, thereby taking the best of both explicit and implicit methods. In addition, we propose several new techniques to improve the three components of our framework, including i) incorporating contextual information into the audio-to-expression parameters encoding; ii) using conditional image synthesis to parameterize the implicit representation and implementing it with an innovative tri-plane structure for efficient learning; iii) formulating facial reenactment as a conditional image inpainting problem and proposing a novel data augmentation technique to improve model generalizability. Extensive experiments demonstrate that our method can generate more realistic results than previous methods with greater fidelity to the identities and talking styles of speakers.

</details>

### [NPVForensics: Jointing Non-critical Phonemes and Visemes for Deepfake Detection](2306.06885.md)
**Yu Chen, Yang Yu, Rongrong Ni, Yao Zhao et al.** · 2023-06-12

<details>
<summary>Abstract</summary>

Deepfake technologies empowered by deep learning are rapidly evolving, creating new security concerns for society. Existing multimodal detection methods usually capture audio-visual inconsistencies to expose Deepfake videos. More seriously, the advanced Deepfake technology realizes the audio-visual calibration of the critical phoneme-viseme regions, achieving a more realistic tampering effect, which brings new challenges. To address this problem, we propose a novel Deepfake detection method to mine the correlation between Non-critical Phonemes and Visemes, termed NPVForensics. Firstly, we propose the Local Feature Aggregation block with Swin Transformer (LFA-ST) to construct non-critical phoneme-viseme and corresponding facial feature streams effectively. Secondly, we design a loss function for the fine-grained motion of the talking face to measure the evolutionary consistency of non-critical phoneme-viseme. Next, we design a phoneme-viseme awareness module for cross-modal feature fusion and representation alignment, so that the modality gap can be reduced and the intrinsic complementarity of the two modalities can be better explored. Finally, a self-supervised pre-training strategy is leveraged to thoroughly learn the audio-visual correspondences in natural videos. In this manner, our model can be easily adapted to the downstream Deepfake datasets with fine-tuning. Extensive experiments on existing benchmarks demonstrate that the proposed approach outperforms state-of-the-art methods.

</details>

### [Ada-TTA: Towards Adaptive High-Quality Text-to-Talking Avatar Synthesis](2306.03504.md)
**Zhenhui Ye, Ziyue Jiang, Yi Ren, Jinglin Liu et al.** · 2023-06-06

<details>
<summary>Abstract</summary>

We are interested in a novel task, namely low-resource text-to-talking avatar. Given only a few-minute-long talking person video with the audio track as the training data and arbitrary texts as the driving input, we aim to synthesize high-quality talking portrait videos corresponding to the input text. This task has broad application prospects in the digital human industry but has not been technically achieved yet due to two challenges: (1) It is challenging to mimic the timbre from out-of-domain audio for a traditional multi-speaker Text-to-Speech system. (2) It is hard to render high-fidelity and lip-synchronized talking avatars with limited training data. In this paper, we introduce Adaptive Text-to-Talking Avatar (Ada-TTA), which (1) designs a generic zero-shot multi-speaker TTS model that well disentangles the text content, timbre, and prosody; and (2) embraces recent advances in neural rendering to achieve realistic audio-driven talking face video generation. With these designs, our method overcomes the aforementioned two challenges and achieves to generate identity-preserving speech and realistic talking person video. Experiments demonstrate that our method could synthesize realistic, identity-preserving, and audio-visual synchronized talking avatar videos.

</details>

### [Audio-Driven Talking Head Video Generation with Diffusion Model](s2:6e6d3daeb11675414391bd935a9e4e84dcff8d47.md)
**Yizhe Zhu, Chunhui Zhang, Qiong Liu, Xi Zhou** · 2023-06-04

<details>
<summary>Abstract</summary>

Synthesizing high-fidelity talking head videos by fitting input audio sequences is a highly anticipated technique in many applications, such as digital humans, virtual video conferences, and human-computer interaction. Popular GAN-based methods aim to align speech audio with lip motions and head poses. However, existing methods are prone to training instability and even mode collapse, resulting in low-quality video generation. In this paper, we propose a novel audio-driven diffusion method for generating high-resolution realistic videos of talking heads with the help of the denoising diffusion model. Specifically, the face attribute disentanglement module is proposed to disentangle eye blinking and lip motion features, where the lip motion features are synchronized with audio features via the contrastive learning strategy, and the disentangled motion features are aligned well with the talking head. Furthermore, the denoising diffusion model takes the source image and the warped motion features as input to generate the high-resolution realistic talking head with diverse head poses. Extensive evaluations using multiple metrics demonstrate that our method outperforms the current techniques both qualitatively and quantitatively.

</details>

### [Audio-Visual Speech Separation in Noisy Environments with a Lightweight Iterative Model](2306.00160.md)
**Héctor Martel, Julius Richter, Kai Li, Xiaolin Hu et al.** · 2023-05-31

<details>
<summary>Abstract</summary>

We propose Audio-Visual Lightweight ITerative model (AVLIT), an effective and lightweight neural network that uses Progressive Learning (PL) to perform audio-visual speech separation in noisy environments. To this end, we adopt the Asynchronous Fully Recurrent Convolutional Neural Network (A-FRCNN), which has shown successful results in audio-only speech separation. Our architecture consists of an audio branch and a video branch, with iterative A-FRCNN blocks sharing weights for each modality. We evaluated our model in a controlled environment using the NTCD-TIMIT dataset and in-the-wild using a synthetic dataset that combines LRS3 and WHAM!. The experiments demonstrate the superiority of our model in both settings with respect to various audio-only and audio-visual baselines. Furthermore, the reduced footprint of our model makes it suitable for low resource applications.

</details>

### [AV-TranSpeech: Audio-Visual Robust Speech-to-Speech Translation](2305.15403.md)
**Rongjie Huang, Huadai Liu, Xize Cheng, Yi Ren et al.** · 2023-05-24

<details>
<summary>Abstract</summary>

Direct speech-to-speech translation (S2ST) aims to convert speech from one language into another, and has demonstrated significant progress to date. Despite the recent success, current S2ST models still suffer from distinct degradation in noisy environments and fail to translate visual speech (i.e., the movement of lips and teeth). In this work, we present AV-TranSpeech, the first audio-visual speech-to-speech (AV-S2ST) translation model without relying on intermediate text. AV-TranSpeech complements the audio stream with visual information to promote system robustness and opens up a host of practical applications: dictation or dubbing archival films. To mitigate the data scarcity with limited parallel AV-S2ST data, we 1) explore self-supervised pre-training with unlabeled audio-visual data to learn contextual representation, and 2) introduce cross-modal distillation with S2ST models trained on the audio-only corpus to further reduce the requirements of visual data. Experimental results on two language pairs demonstrate that AV-TranSpeech outperforms audio-only models under all settings regardless of the type of noise. With low-resource audio-visual data (10h, 30h), cross-modal distillation yields an improvement of 7.6 BLEU on average compared with baselines. Audio samples are available at https://AV-TranSpeech.github.io

</details>

### [CPNet: Exploiting CLIP-based Attention Condenser and Probability Map Guidance for High-fidelity Talking Face Generation](2305.13962.md)
**Jingning Xu, Benlai Tang, Mingjie Wang, Minghao Li et al.** · 2023-05-23

<details>
<summary>Abstract</summary>

Recently, talking face generation has drawn ever-increasing attention from the research community in computer vision due to its arduous challenges and widespread application scenarios, e.g. movie animation and virtual anchor. Although persevering efforts have been undertaken to enhance the fidelity and lip-sync quality of generated talking face videos, there is still large room for further improvements of synthesis quality and efficiency. Actually, these attempts somewhat ignore the explorations of fine-granularity feature extraction/integration and the consistency between probability distributions of landmarks, thereby recurring the issues of local details blurring and degraded fidelity. To mitigate these dilemmas, in this paper, a novel CLIP-based Attention and Probability Map Guided Network (CPNet) is delicately designed for inferring high-fidelity talking face videos. Specifically, considering the demands of fine-grained feature recalibration, a clip-based attention condenser is exploited to transfer knowledge with rich semantic priors from the prevailing CLIP model. Moreover, to guarantee the consistency in probability space and suppress the landmark ambiguity, we creatively propose the density map of facial landmark as auxiliary supervisory signal to guide the landmark distribution learning of generated frame. Extensive experiments on the widely-used benchmark dataset demonstrate the superiority of our CPNet against state of the arts in terms of image and lip-sync quality. In addition, a cohort of studies are also conducted to ablate the impacts of the individual pivotal components.

</details>

### [RenderMe-360: A Large Digital Asset Library and Benchmarks Towards High-fidelity Head Avatars](2305.13353.md)
**Dongwei Pan, Long Zhuo, Jingtan Piao, Huiwen Luo et al.** · 2023-05-22

<details>
<summary>Abstract</summary>

Synthesizing high-fidelity head avatars is a central problem for computer vision and graphics. While head avatar synthesis algorithms have advanced rapidly, the best ones still face great obstacles in real-world scenarios. One of the vital causes is inadequate datasets -- 1) current public datasets can only support researchers to explore high-fidelity head avatars in one or two task directions; 2) these datasets usually contain digital head assets with limited data volume, and narrow distribution over different attributes. In this paper, we present RenderMe-360, a comprehensive 4D human head dataset to drive advance in head avatar research. It contains massive data assets, with 243+ million complete head frames, and over 800k video sequences from 500 different identities captured by synchronized multi-view cameras at 30 FPS. It is a large-scale digital library for head avatars with three key attributes: 1) High Fidelity: all subjects are captured by 60 synchronized, high-resolution 2K cameras in 360 degrees. 2) High Diversity: The collected subjects vary from different ages, eras, ethnicities, and cultures, providing abundant materials with distinctive styles in appearance and geometry. Moreover, each subject is asked to perform various motions, such as expressions and head rotations, which further extend the richness of assets. 3) Rich Annotations: we provide annotations with different granularities: cameras' parameters, matting, scan, 2D/3D facial landmarks, FLAME fitting, and text description. Based on the dataset, we build a comprehensive benchmark for head avatar research, with 16 state-of-the-art methods performed on five main tasks: novel view synthesis, novel expression synthesis, hair rendering, hair editing, and talking head generation. Our experiments uncover the strengths and weaknesses of current methods. RenderMe-360 opens the door for future exploration in head avatars.

</details>

### [LPMM: Intuitive Pose Control for Neural Talking-Head Model via Landmark-Parameter Morphable Model](2305.10456.md)
**Kwangho Lee, Patrick Kwon, Myung Ki Lee, Namhyuk Ahn et al.** · 2023-05-17

<details>
<summary>Abstract</summary>

While current talking head models are capable of generating photorealistic talking head videos, they provide limited pose controllability. Most methods require specific video sequences that should exactly contain the head pose desired, being far from user-friendly pose control. Three-dimensional morphable models (3DMM) offer semantic pose control, but they fail to capture certain expressions. We present a novel method that utilizes parametric control of head orientation and facial expression over a pre-trained neural-talking head model. To enable this, we introduce a landmark-parameter morphable model (LPMM), which offers control over the facial landmark domain through a set of semantic parameters. Using LPMM, it is possible to adjust specific head pose factors, without distorting other facial attributes. The results show our approach provides intuitive rig-like control over neural talking head models, allowing both parameter and image-based inputs.

</details>

### [Identity-Preserving Talking Face Generation with Landmark and Appearance Priors](2305.08293.md)
**Weizhi Zhong, Chaowei Fang, Yinqi Cai, Pengxu Wei et al.** · 2023-05-15

<details>
<summary>Abstract</summary>

Generating talking face videos from audio attracts lots of research interest. A few person-specific methods can generate vivid videos but require the target speaker's videos for training or fine-tuning. Existing person-generic methods have difficulty in generating realistic and lip-synced videos while preserving identity information. To tackle this problem, we propose a two-stage framework consisting of audio-to-landmark generation and landmark-to-video rendering procedures. First, we devise a novel Transformer-based landmark generator to infer lip and jaw landmarks from the audio. Prior landmark characteristics of the speaker's face are employed to make the generated landmarks coincide with the facial outline of the speaker. Then, a video rendering model is built to translate the generated landmarks into face images. During this stage, prior appearance information is extracted from the lower-half occluded target face and static reference images, which helps generate realistic and identity-preserving visual content. For effectively exploring the prior information of static reference images, we align static reference images with the target face's pose and expression based on motion fields. Moreover, auditory features are reused to guarantee that the generated face images are well synchronized with the audio. Extensive experiments demonstrate that our method can produce more realistic, lip-synced, and identity-preserving videos than existing person-generic talking face generation methods.

</details>

### [DaGAN++: Depth-Aware Generative Adversarial Network for Talking Head Video Generation](2305.06225.md)
**Fa-Ting Hong, Li Shen, Dan Xu** · 2023-05-10

<details>
<summary>Abstract</summary>

Predominant techniques on talking head generation largely depend on 2D information, including facial appearances and motions from input face images. Nevertheless, dense 3D facial geometry, such as pixel-wise depth, plays a critical role in constructing accurate 3D facial structures and suppressing complex background noises for generation. However, dense 3D annotations for facial videos is prohibitively costly to obtain. In this work, firstly, we present a novel self-supervised method for learning dense 3D facial geometry (ie, depth) from face videos, without requiring camera parameters and 3D geometry annotations in training. We further propose a strategy to learn pixel-level uncertainties to perceive more reliable rigid-motion pixels for geometry learning. Secondly, we design an effective geometry-guided facial keypoint estimation module, providing accurate keypoints for generating motion fields. Lastly, we develop a 3D-aware cross-modal (ie, appearance and depth) attention mechanism, which can be applied to each generation layer, to capture facial geometries in a coarse-to-fine manner. Extensive experiments are conducted on three challenging benchmarks (ie, VoxCeleb1, VoxCeleb2, and HDTF). The results demonstrate that our proposed framework can generate highly realistic-looking reenacted talking videos, with new state-of-the-art performances established on these benchmarks. The codes and trained models are publicly available on the GitHub project page at https://github.com/harlanhong/CVPR2022-DaGAN

</details>

### [A multimodal dynamical variational autoencoder for audiovisual speech representation learning](2305.03582.md)
**Samir Sadok, Simon Leglaive, Laurent Girin, Xavier Alameda-Pineda et al.** · 2023-05-05

<details>
<summary>Abstract</summary>

In this paper, we present a multimodal and dynamical VAE (MDVAE) applied to unsupervised audio-visual speech representation learning. The latent space is structured to dissociate the latent dynamical factors that are shared between the modalities from those that are specific to each modality. A static latent variable is also introduced to encode the information that is constant over time within an audiovisual speech sequence. The model is trained in an unsupervised manner on an audiovisual emotional speech dataset, in two stages. In the first stage, a vector quantized VAE (VQ-VAE) is learned independently for each modality, without temporal modeling. The second stage consists in learning the MDVAE model on the intermediate representation of the VQ-VAEs before quantization. The disentanglement between static versus dynamical and modality-specific versus modality-common information occurs during this second training stage. Extensive experiments are conducted to investigate how audiovisual speech latent factors are encoded in the latent space of MDVAE. These experiments include manipulating audiovisual speech, audiovisual facial image denoising, and audiovisual speech emotion recognition. The results show that MDVAE effectively combines the audio and visual information in its latent space. They also show that the learned static representation of audiovisual speech can be used for emotion recognition with few labeled data, and with better accuracy compared with unimodal baselines and a state-of-the-art supervised model based on an audiovisual transformer architecture.

</details>

### [Multimodal-driven Talking Face Generation via a Unified Diffusion-based Generator](2305.02594.md)
**Chao Xu, Shaoting Zhu, Junwei Zhu, Tianxin Huang et al.** · 2023-05-04

<details>
<summary>Abstract</summary>

Multimodal-driven talking face generation refers to animating a portrait with the given pose, expression, and gaze transferred from the driving image and video, or estimated from the text and audio. However, existing methods ignore the potential of text modal, and their generators mainly follow the source-oriented feature rearrange paradigm coupled with unstable GAN frameworks. In this work, we first represent the emotion in the text prompt, which could inherit rich semantics from the CLIP, allowing flexible and generalized emotion control. We further reorganize these tasks as the target-oriented texture transfer and adopt the Diffusion Models. More specifically, given a textured face as the source and the rendered face projected from the desired 3DMM coefficients as the target, our proposed Texture-Geometry-aware Diffusion Model decomposes the complex transfer problem into multi-conditional denoising process, where a Texture Attention-based module accurately models the correspondences between appearance and geometry cues contained in source and target conditions, and incorporate extra implicit information for high-fidelity talking face generation. Additionally, TGDM can be gracefully tailored for face swapping. We derive a novel paradigm free of unstable seesaw-style optimization, resulting in simple, stable, and effective training and inference schemes. Extensive experiments demonstrate the superiority of our method.

</details>

### [GeneFace++: Generalized and Stable Real-Time Audio-Driven 3D Talking Face Generation](2305.00787.md)
**Zhenhui Ye, Jinzheng He, Ziyue Jiang, Rongjie Huang et al.** · 2023-05-01

<details>
<summary>Abstract</summary>

Generating talking person portraits with arbitrary speech audio is a crucial problem in the field of digital human and metaverse. A modern talking face generation method is expected to achieve the goals of generalized audio-lip synchronization, good video quality, and high system efficiency. Recently, neural radiance field (NeRF) has become a popular rendering technique in this field since it could achieve high-fidelity and 3D-consistent talking face generation with a few-minute-long training video. However, there still exist several challenges for NeRF-based methods: 1) as for the lip synchronization, it is hard to generate a long facial motion sequence of high temporal consistency and audio-lip accuracy; 2) as for the video quality, due to the limited data used to train the renderer, it is vulnerable to out-of-domain input condition and produce bad rendering results occasionally; 3) as for the system efficiency, the slow training and inference speed of the vanilla NeRF severely obstruct its usage in real-world applications. In this paper, we propose GeneFace++ to handle these challenges by 1) utilizing the pitch contour as an auxiliary feature and introducing a temporal loss in the facial motion prediction process; 2) proposing a landmark locally linear embedding method to regulate the outliers in the predicted motion sequence to avoid robustness issues; 3) designing a computationally efficient NeRF-based motion-to-video renderer to achieves fast training and real-time inference. With these settings, GeneFace++ becomes the first NeRF-based method that achieves stable and real-time talking face generation with generalized audio-lip synchronization. Extensive experiments show that our method outperforms state-of-the-art baselines in terms of subjective and objective evaluation. Video samples are available at https://genefaceplusplus.github.io .

</details>

### [StyleAvatar: Real-time Photo-realistic Portrait Avatar from a Single Video](2305.00942.md)
**Lizhen Wang, Xiaochen Zhao, Jingxiang Sun, Yuxiang Zhang et al.** · 2023-05-01

<details>
<summary>Abstract</summary>

Face reenactment methods attempt to restore and re-animate portrait videos as realistically as possible. Existing methods face a dilemma in quality versus controllability: 2D GAN-based methods achieve higher image quality but suffer in fine-grained control of facial attributes compared with 3D counterparts. In this work, we propose StyleAvatar, a real-time photo-realistic portrait avatar reconstruction method using StyleGAN-based networks, which can generate high-fidelity portrait avatars with faithful expression control. We expand the capabilities of StyleGAN by introducing a compositional representation and a sliding window augmentation method, which enable faster convergence and improve translation generalization. Specifically, we divide the portrait scenes into three parts for adaptive adjustments: facial region, non-facial foreground region, and the background. Besides, our network leverages the best of UNet, StyleGAN and time coding for video learning, which enables high-quality video generation. Furthermore, a sliding window augmentation method together with a pre-training strategy are proposed to improve translation generalization and training performance, respectively. The proposed network can converge within two hours while ensuring high image quality and a forward rendering time of only 20 milliseconds. Furthermore, we propose a real-time live system, which further pushes research into applications. Results and experiments demonstrate the superiority of our method in terms of image quality, full portrait video generation, and real-time re-animation compared to existing facial reenactment methods. Training and inference code for this paper are at https://github.com/LizhenWangT/StyleAvatar.

</details>

### [StyleLipSync: Style-based Personalized Lip-sync Video Generation](2305.00521.md)
**Taekyung Ki, Dongchan Min** · 2023-04-30

<details>
<summary>Abstract</summary>

In this paper, we present StyleLipSync, a style-based personalized lip-sync video generative model that can generate identity-agnostic lip-synchronizing video from arbitrary audio. To generate a video of arbitrary identities, we leverage expressive lip prior from the semantically rich latent space of a pre-trained StyleGAN, where we can also design a video consistency with a linear transformation. In contrast to the previous lip-sync methods, we introduce pose-aware masking that dynamically locates the mask to improve the naturalness over frames by utilizing a 3D parametric mesh predictor frame by frame. Moreover, we propose a few-shot lip-sync adaptation method for an arbitrary person by introducing a sync regularizer that preserves lip-sync generalization while enhancing the person-specific visual information. Extensive experiments demonstrate that our model can generate accurate lip-sync videos even with the zero-shot setting and enhance characteristics of an unseen face using a few seconds of target video through the proposed adaptation method.

</details>

### [High-Fidelity and Freely Controllable Talking Head Video Generation](2304.10168.md)
**Yue Gao, Yuan Zhou, Jinglu Wang, Xiao Li et al.** · 2023-04-20

<details>
<summary>Abstract</summary>

Talking head generation is to generate video based on a given source identity and target motion. However, current methods face several challenges that limit the quality and controllability of the generated videos. First, the generated face often has unexpected deformation and severe distortions. Second, the driving image does not explicitly disentangle movement-relevant information, such as poses and expressions, which restricts the manipulation of different attributes during generation. Third, the generated videos tend to have flickering artifacts due to the inconsistency of the extracted landmarks between adjacent frames. In this paper, we propose a novel model that produces high-fidelity talking head videos with free control over head pose and expression. Our method leverages both self-supervised learned landmarks and 3D face model-based landmarks to model the motion. We also introduce a novel motion-aware multi-scale feature alignment module to effectively transfer the motion without face distortion. Furthermore, we enhance the smoothness of the synthesized talking head videos with a feature context adaptation and propagation module. We evaluate our model on challenging datasets and demonstrate its state-of-the-art performance.

</details>

### [Audio-Driven Talking Face Generation with Diverse yet Realistic Facial Animations](2304.08945.md)
**Rongliang Wu, Yingchen Yu, Fangneng Zhan, Jiahui Zhang et al.** · 2023-04-18

<details>
<summary>Abstract</summary>

Audio-driven talking face generation, which aims to synthesize talking faces with realistic facial animations (including accurate lip movements, vivid facial expression details and natural head poses) corresponding to the audio, has achieved rapid progress in recent years. However, most existing work focuses on generating lip movements only without handling the closely correlated facial expressions, which degrades the realism of the generated faces greatly. This paper presents DIRFA, a novel method that can generate talking faces with diverse yet realistic facial animations from the same driving audio. To accommodate fair variation of plausible facial animations for the same audio, we design a transformer-based probabilistic mapping network that can model the variational facial animation distribution conditioned upon the input audio and autoregressively convert the audio signals into a facial animation sequence. In addition, we introduce a temporally-biased mask into the mapping network, which allows to model the temporal dependency of facial animations and produce temporally smooth facial animation sequence. With the generated facial animation sequence and a source image, photo-realistic talking faces can be synthesized with a generic generation network. Extensive experiments show that DIRFA can generate talking faces with realistic facial animations effectively.

</details>

### [One-Shot High-Fidelity Talking-Head Synthesis with Deformable Neural Radiance Field](2304.05097.md)
**Weichuang Li, Longhao Zhang, Dong Wang, Bin Zhao et al.** · 2023-04-11

<details>
<summary>Abstract</summary>

Talking head generation aims to generate faces that maintain the identity information of the source image and imitate the motion of the driving image. Most pioneering methods rely primarily on 2D representations and thus will inevitably suffer from face distortion when large head rotations are encountered. Recent works instead employ explicit 3D structural representations or implicit neural rendering to improve performance under large pose changes. Nevertheless, the fidelity of identity and expression is not so desirable, especially for novel-view synthesis. In this paper, we propose HiDe-NeRF, which achieves high-fidelity and free-view talking-head synthesis. Drawing on the recently proposed Deformable Neural Radiance Fields, HiDe-NeRF represents the 3D dynamic scene into a canonical appearance field and an implicit deformation field, where the former comprises the canonical source face and the latter models the driving pose and expression. In particular, we improve fidelity from two aspects: (i) to enhance identity expressiveness, we design a generalized appearance module that leverages multi-scale volume features to preserve face shape and details; (ii) to improve expression preciseness, we propose a lightweight deformation module that explicitly decouples the pose and expression to enable precise expression modeling. Extensive experiments demonstrate that our proposed approach can generate better results than previous works. Project page: https://www.waytron.net/hidenerf/

</details>

### [That's What I Said: Fully-Controllable Talking Face Generation](2304.03275.md)
**Youngjoon Jang, Kyeongha Rho, Jong-Bin Woo, Hyeongkeun Lee et al.** · 2023-04-06

<details>
<summary>Abstract</summary>

The goal of this paper is to synthesise talking faces with controllable facial motions. To achieve this goal, we propose two key ideas. The first is to establish a canonical space where every face has the same motion patterns but different identities. The second is to navigate a multimodal motion space that only represents motion-related features while eliminating identity information. To disentangle identity and motion, we introduce an orthogonality constraint between the two different latent spaces. From this, our method can generate natural-looking talking faces with fully controllable facial attributes and accurate lip synchronisation. Extensive experiments demonstrate that our method achieves state-of-the-art results in terms of both visual quality and lip-sync score. To the best of our knowledge, we are the first to develop a talking face generation framework that can accurately manifest full target facial motions including lip, head pose, and eye movements in the generated video without any additional supervision beyond RGB video with audio.

</details>

### [DAE-Talker: High Fidelity Speech-Driven Talking Face Generation with Diffusion Autoencoder](2303.17550.md)
**Chenpeng Du, Qi Chen, Tianyu He, Xu Tan et al.** · 2023-03-30

<details>
<summary>Abstract</summary>

While recent research has made significant progress in speech-driven talking face generation, the quality of the generated video still lags behind that of real recordings. One reason for this is the use of handcrafted intermediate representations like facial landmarks and 3DMM coefficients, which are designed based on human knowledge and are insufficient to precisely describe facial movements. Additionally, these methods require an external pretrained model for extracting these representations, whose performance sets an upper bound on talking face generation. To address these limitations, we propose a novel method called DAE-Talker that leverages data-driven latent representations obtained from a diffusion autoencoder (DAE). DAE contains an image encoder that encodes an image into a latent vector and a DDIM image decoder that reconstructs the image from it. We train our DAE on talking face video frames and then extract their latent representations as the training target for a Conformer-based speech2latent model. This allows DAE-Talker to synthesize full video frames and produce natural head movements that align with the content of speech, rather than relying on a predetermined head pose from a template video. We also introduce pose modelling in speech2latent for pose controllability. Additionally, we propose a novel method for generating continuous video frames with the DDIM image decoder trained on individual frames, eliminating the need for modelling the joint distribution of consecutive frames directly. Our experiments show that DAE-Talker outperforms existing popular methods in lip-sync, video fidelity, and pose naturalness. We also conduct ablation studies to analyze the effectiveness of the proposed techniques and demonstrate the pose controllability of DAE-Talker.

</details>

### [Seeing What You Said: Talking Face Generation Guided by a Lip Reading Expert](2303.17480.md)
**Jiadong Wang, Xinyuan Qian, Malu Zhang, Robby T. Tan et al.** · 2023-03-29

<details>
<summary>Abstract</summary>

Talking face generation, also known as speech-to-lip generation, reconstructs facial motions concerning lips given coherent speech input. The previous studies revealed the importance of lip-speech synchronization and visual quality. Despite much progress, they hardly focus on the content of lip movements i.e., the visual intelligibility of the spoken words, which is an important aspect of generation quality. To address the problem, we propose using a lip-reading expert to improve the intelligibility of the generated lip regions by penalizing the incorrect generation results. Moreover, to compensate for data scarcity, we train the lip-reading expert in an audio-visual self-supervised manner. With a lip-reading expert, we propose a novel contrastive learning to enhance lip-speech synchronization, and a transformer to encode audio synchronically with video, while considering global temporal dependency of audio. For evaluation, we propose a new strategy with two different lip-reading experts to measure intelligibility of the generated videos. Rigorous experiments show that our proposal is superior to other State-of-the-art (SOTA) methods, such as Wav2Lip, in reading intelligibility i.e., over 38% Word Error Rate (WER) on LRS2 dataset and 27.8% accuracy on LRW dataset. We also achieve the SOTA performance in lip-speech synchronization and comparable performances in visual quality.

</details>

### [OTAvatar: One-shot Talking Face Avatar with Controllable Tri-plane Rendering](2303.14662.md)
**Zhiyuan Ma, Xiangyu Zhu, Guojun Qi, Zhen Lei et al.** · 2023-03-26

<details>
<summary>Abstract</summary>

Controllability, generalizability and efficiency are the major objectives of constructing face avatars represented by neural implicit field. However, existing methods have not managed to accommodate the three requirements simultaneously. They either focus on static portraits, restricting the representation ability to a specific subject, or suffer from substantial computational cost, limiting their flexibility. In this paper, we propose One-shot Talking face Avatar (OTAvatar), which constructs face avatars by a generalized controllable tri-plane rendering solution so that each personalized avatar can be constructed from only one portrait as the reference. Specifically, OTAvatar first inverts a portrait image to a motion-free identity code. Second, the identity code and a motion code are utilized to modulate an efficient CNN to generate a tri-plane formulated volume, which encodes the subject in the desired motion. Finally, volume rendering is employed to generate an image in any view. The core of our solution is a novel decoupling-by-inverting strategy that disentangles identity and motion in the latent code via optimization-based inversion. Benefiting from the efficient tri-plane representation, we achieve controllable rendering of generalized face avatar at $35$ FPS on A100. Experiments show promising performance of cross-identity reenactment on subjects out of the training set and better 3D consistency.

</details>

### [EmoTalk: Speech-Driven Emotional Disentanglement for 3D Face Animation](2303.11089.md)
**Ziqiao Peng, Haoyu Wu, Zhenbo Song, Hao Xu et al.** · 2023-03-20

<details>
<summary>Abstract</summary>

Speech-driven 3D face animation aims to generate realistic facial expressions that match the speech content and emotion. However, existing methods often neglect emotional facial expressions or fail to disentangle them from speech content. To address this issue, this paper proposes an end-to-end neural network to disentangle different emotions in speech so as to generate rich 3D facial expressions. Specifically, we introduce the emotion disentangling encoder (EDE) to disentangle the emotion and content in the speech by cross-reconstructed speech signals with different emotion labels. Then an emotion-guided feature fusion decoder is employed to generate a 3D talking face with enhanced emotion. The decoder is driven by the disentangled identity, emotional, and content embeddings so as to generate controllable personal and emotional styles. Finally, considering the scarcity of the 3D emotional talking face data, we resort to the supervision of facial blendshapes, which enables the reconstruction of plausible 3D faces from 2D emotional data, and contribute a large-scale 3D emotional talking face dataset (3D-ETF) to train the network. Our experiments and user studies demonstrate that our approach outperforms state-of-the-art methods and exhibits more diverse facial movements. We recommend watching the supplementary video: https://ziqiaopeng.github.io/emotalk

</details>

### [DisCoHead: Audio-and-Video-Driven Talking Head Generation by Disentangled Control of Head Pose and Facial Expressions](2303.07697.md)
**Geumbyeol Hwang, Sunwon Hong, Seunghyun Lee, Sungwoo Park et al.** · 2023-03-14

<details>
<summary>Abstract</summary>

For realistic talking head generation, creating natural head motion while maintaining accurate lip synchronization is essential. To fulfill this challenging task, we propose DisCoHead, a novel method to disentangle and control head pose and facial expressions without supervision. DisCoHead uses a single geometric transformation as a bottleneck to isolate and extract head motion from a head-driving video. Either an affine or a thin-plate spline transformation can be used and both work well as geometric bottlenecks. We enhance the efficiency of DisCoHead by integrating a dense motion estimator and the encoder of a generator which are originally separate modules. Taking a step further, we also propose a neural mix approach where dense motion is estimated and applied implicitly by the encoder. After applying the disentangled head motion to a source identity, DisCoHead controls the mouth region according to speech audio, and it blinks eyes and moves eyebrows following a separate driving video of the eye region, via the weight modulation of convolutional neural networks. The experiments using multiple datasets show that DisCoHead successfully generates realistic audio-and-video-driven talking heads and outperforms state-of-the-art methods. Project page: https://deepbrainai-research.github.io/discohead/

</details>

### [Learning Cross-lingual Visual Speech Representations](2303.09455.md)
**Andreas Zinonos, Alexandros Haliassos, Pingchuan Ma, Stavros Petridis et al.** · 2023-03-14

<details>
<summary>Abstract</summary>

Cross-lingual self-supervised learning has been a growing research topic in the last few years. However, current works only explored the use of audio signals to create representations. In this work, we study cross-lingual self-supervised visual representation learning. We use the recently-proposed Raw Audio-Visual Speech Encoders (RAVEn) framework to pre-train an audio-visual model with unlabelled multilingual data, and then fine-tune the visual model on labelled transcriptions. Our experiments show that: (1) multi-lingual models with more data outperform monolingual ones, but, when keeping the amount of data fixed, monolingual models tend to reach better performance; (2) multi-lingual outperforms English-only pre-training; (3) using languages which are more similar yields better results; and (4) fine-tuning on unseen languages is competitive to using the target language in the pre-training set. We hope our study inspires future research on non-English-only speech representation learning.

</details>

### [Memory-augmented Contrastive Learning for Talking Head Generation](2302.13469.md)
**Jianrong Wang, Yaxin Zhao, Li Liu, Hongkai Fan et al.** · 2023-02-27

<details>
<summary>Abstract</summary>

Given one reference facial image and a piece of speech as input, talking head generation aims to synthesize a realistic-looking talking head video. However, generating a lip-synchronized video with natural head movements is challenging. The same speech clip can generate multiple possible lip and head movements, that is, there is no one-to-one mapping relationship between them. To overcome this problem, we propose a Speech Feature Extractor (SFE) based on memory-augmented self-supervised contrastive learning, which introduces the memory module to store multiple different speech mapping results. In addition, we introduce the Mixed Density Networks (MDN) into the landmark regression task to generate multiple predicted facial landmarks. Extensive qualitative and quantitative experiments show that the quality of our facial animation is significantly superior to that of the state-of-the-art (SOTA). The code has been released at https://github.com/Yaxinzhao97/MACL.git.

</details>

### [Pose-Controllable 3D Facial Animation Synthesis using Hierarchical Audio-Vertex Attention](2302.12532.md)
**Bin Liu, Xiaolin Wei, Bo Li, Junjie Cao et al.** · 2023-02-24

<details>
<summary>Abstract</summary>

Most of the existing audio-driven 3D facial animation methods suffered from the lack of detailed facial expression and head pose, resulting in unsatisfactory experience of human-robot interaction. In this paper, a novel pose-controllable 3D facial animation synthesis method is proposed by utilizing hierarchical audio-vertex attention. To synthesize real and detailed expression, a hierarchical decomposition strategy is proposed to encode the audio signal into both a global latent feature and a local vertex-wise control feature. Then the local and global audio features combined with vertex spatial features are used to predict the final consistent facial animation via a graph convolutional neural network by fusing the intrinsic spatial topology structure of the face model and the corresponding semantic feature of the audio. To accomplish pose-controllable animation, we introduce a novel pose attribute augmentation method by utilizing the 2D talking face technique. Experimental results indicate that the proposed method can produce more realistic facial expressions and head posture movements. Qualitative and quantitative experiments show that the proposed method achieves competitive performance against state-of-the-art methods.

</details>

### [Deep Learning Technique to generate lip-sync for live 2-D Animation](s2:7f61d57df02bfeb59057f49944b79b14c1e0aea0.md)
**Ashish Soni, Janhvi Deshmukh, Ayush Shende, R. Gawande et al.** · 2023-02-18

<details>
<summary>Abstract</summary>

Currently, there are a couple of major trends in live 2-D animation like Immersive User Experience, Next-Gen Software, Mobile 2D Animation, VR 2D Animation, AR/VR Live Action Animation, and Web 2D Animation that are getting a lot of attention. For the industries like advertisement, entertainment as well as education, this new technology has become very important as each of them needs to reach their target audience through it. With the help of live 2-D animation, these industries can now reach out to new audiences through something that has never been done before, creating original content that is something that has never been done before. This has now become possible due to the rise of social media. With the advent of social media, it is now possible for anyone in the world to communicate with people who have never been contacted by any advertising or marketing agency before. The solution we are proposing is a deep learning technique for creating animated characters that can make lips synchronized just the way humans do without any assistance and intervention. This can save many working hours that are needed to make an animated character feel real while dialog delivery. The main requirement here is the exact lip sync as that of the human performs while talking the lip movement should get exactly matched. This is possible with the help of LSTM model [5].

</details>

### [GeneFace: Generalized and High-Fidelity Audio-Driven 3D Talking Face Synthesis](2301.13430.md)
**Zhenhui Ye, Ziyue Jiang, Yi Ren, Jinglin Liu et al.** · 2023-01-31

<details>
<summary>Abstract</summary>

Generating photo-realistic video portrait with arbitrary speech audio is a crucial problem in film-making and virtual reality. Recently, several works explore the usage of neural radiance field in this task to improve 3D realness and image fidelity. However, the generalizability of previous NeRF-based methods to out-of-domain audio is limited by the small scale of training data. In this work, we propose GeneFace, a generalized and high-fidelity NeRF-based talking face generation method, which can generate natural results corresponding to various out-of-domain audio. Specifically, we learn a variaitional motion generator on a large lip-reading corpus, and introduce a domain adaptative post-net to calibrate the result. Moreover, we learn a NeRF-based renderer conditioned on the predicted facial motion. A head-aware torso-NeRF is proposed to eliminate the head-torso separation problem. Extensive experiments show that our method achieves more generalized and high-fidelity talking face generation compared to previous methods.

</details>

### [DPE: Disentanglement of Pose and Expression for General Video Portrait Editing](2301.06281.md)
**Youxin Pang, Yong Zhang, Weize Quan, Yanbo Fan et al.** · 2023-01-16

<details>
<summary>Abstract</summary>

One-shot video-driven talking face generation aims at producing a synthetic talking video by transferring the facial motion from a video to an arbitrary portrait image. Head pose and facial expression are always entangled in facial motion and transferred simultaneously. However, the entanglement sets up a barrier for these methods to be used in video portrait editing directly, where it may require to modify the expression only while maintaining the pose unchanged. One challenge of decoupling pose and expression is the lack of paired data, such as the same pose but different expressions. Only a few methods attempt to tackle this challenge with the feat of 3D Morphable Models (3DMMs) for explicit disentanglement. But 3DMMs are not accurate enough to capture facial details due to the limited number of Blenshapes, which has side effects on motion transfer. In this paper, we introduce a novel self-supervised disentanglement framework to decouple pose and expression without 3DMMs and paired data, which consists of a motion editing module, a pose generator, and an expression generator. The editing module projects faces into a latent space where pose motion and expression motion can be disentangled, and the pose or expression transfer can be performed in the latent space conveniently via addition. The two generators render the modified latent codes to images, respectively. Moreover, to guarantee the disentanglement, we propose a bidirectional cyclic training strategy with well-designed constraints. Evaluations demonstrate our method can control pose or expression independently and be used for general video editing.

</details>

### [DiffTalk: Crafting Diffusion Models for Generalized Audio-Driven Portraits Animation](2301.03786.md)
**Shuai Shen, Wenliang Zhao, Zibin Meng, Wanhua Li et al.** · 2023-01-10

<details>
<summary>Abstract</summary>

Talking head synthesis is a promising approach for the video production industry. Recently, a lot of effort has been devoted in this research area to improve the generation quality or enhance the model generalization. However, there are few works able to address both issues simultaneously, which is essential for practical applications. To this end, in this paper, we turn attention to the emerging powerful Latent Diffusion Models, and model the Talking head generation as an audio-driven temporally coherent denoising process (DiffTalk). More specifically, instead of employing audio signals as the single driving factor, we investigate the control mechanism of the talking face, and incorporate reference face images and landmarks as conditions for personality-aware generalized synthesis. In this way, the proposed DiffTalk is capable of producing high-quality talking head videos in synchronization with the source audio, and more importantly, it can be naturally generalized across different identities without any further fine-tuning. Additionally, our DiffTalk can be gracefully tailored for higher-resolution synthesis with negligible extra computational cost. Extensive experiments show that the proposed DiffTalk efficiently synthesizes high-fidelity audio-driven talking head videos for generalized novel identities. For more video results, please refer to \url{https://sstzal.github.io/DiffTalk/}.

</details>

### [Diffused Heads: Diffusion Models Beat GANs on Talking-Face Generation](2301.03396.md)
**Michał Stypułkowski, Konstantinos Vougioukas, Sen He, Maciej Zięba et al.** · 2023-01-06

<details>
<summary>Abstract</summary>

Talking face generation has historically struggled to produce head movements and natural facial expressions without guidance from additional reference videos. Recent developments in diffusion-based generative models allow for more realistic and stable data synthesis and their performance on image and video generation has surpassed that of other generative models. In this work, we present an autoregressive diffusion model that requires only one identity image and audio sequence to generate a video of a realistic talking human head. Our solution is capable of hallucinating head movements, facial expressions, such as blinks, and preserving a given background. We evaluate our model on two different datasets, achieving state-of-the-art results on both of them.

</details>

### [Expressive Speech-driven Facial Animation with controllable emotions](2301.02008.md)
**Yutong Chen, Junhong Zhao, Wei-Qiang Zhang** · 2023-01-05

<details>
<summary>Abstract</summary>

It is in high demand to generate facial animation with high realism, but it remains a challenging task. Existing approaches of speech-driven facial animation can produce satisfactory mouth movement and lip synchronization, but show weakness in dramatic emotional expressions and flexibility in emotion control. This paper presents a novel deep learning-based approach for expressive facial animation generation from speech that can exhibit wide-spectrum facial expressions with controllable emotion type and intensity. We propose an emotion controller module to learn the relationship between the emotion variations (e.g., types and intensity) and the corresponding facial expression parameters. It enables emotion-controllable facial animation, where the target expression can be continuously adjusted as desired. The qualitative and quantitative evaluations show that the animation generated by our method is rich in facial emotional expressiveness while retaining accurate lip movement, outperforming other state-of-the-art methods.

</details>

### [LipNeRF: What is the right feature space to lip-sync a NeRF?](s2:5d082bc5968b7138509758f88069288076227d42.md)
**Aggelina Chatziagapi, ShahRukh Athar, Abhinav Jain, M. Rohith et al.** · 2023-01-05

<details>
<summary>Abstract</summary>

Synthesizing high-fidelity talking head videos of an arbitrary identity, lip-synced to a target speech segment, is a challenging problem. Recent GAN-based methods succeed by training a model on a large amount of videos, allowing the generator to learn a variety of audio-lip representations. However, they are unable to handle head pose changes. On the other hand, Neural Radiance Fields (NeRFs) model the 3D face geometry more accurately. Current audio-conditioned NeRFs are not as good in lip synchronization as GANs, since they are trained on limited video data of a single identity. In this work, we propose LipNeRF, a lip-syncing NeRF that bridges the gap between the accurate lip synchronization of GAN-based methods and the accurate 3D face modeling of NeRFs. LipNeRF is conditioned on the expression space of a 3DMM, instead of the audio feature space. We experimentally demonstrate that the expression space gives a better representation for the lip shape than the audio feature space. LipNeRF shows a significant improvement in lip-sync quality over the current state-of-the-art, especially in high-definition videos of cinematic content, with challenging pose, illumination and expression variations.

</details>

### [StyleTalk: One-shot Talking Head Generation with Controllable Speaking Styles](2301.01081.md)
**Yifeng Ma, Suzhen Wang, Zhipeng Hu, Changjie Fan et al.** · 2023-01-03

<details>
<summary>Abstract</summary>

Different people speak with diverse personalized speaking styles. Although existing one-shot talking head methods have made significant progress in lip sync, natural facial expressions, and stable head motions, they still cannot generate diverse speaking styles in the final talking head videos. To tackle this problem, we propose a one-shot style-controllable talking face generation framework. In a nutshell, we aim to attain a speaking style from an arbitrary reference speaking video and then drive the one-shot portrait to speak with the reference speaking style and another piece of audio. Specifically, we first develop a style encoder to extract dynamic facial motion patterns of a style reference video and then encode them into a style code. Afterward, we introduce a style-controllable decoder to synthesize stylized facial animations from the speech content and style code. In order to integrate the reference speaking style into generated videos, we design a style-aware adaptive transformer, which enables the encoded style code to adjust the weights of the feed-forward layers accordingly. Thanks to the style-aware adaptation mechanism, the reference speaking style can be better embedded into synthesized videos during decoding. Extensive experiments demonstrate that our method is capable of generating talking head videos with diverse speaking styles from only one portrait image and an audio clip while achieving authentic visual effects. Project Page: https://github.com/FuxiVirtualHuman/styletalk.

</details>

### [A Simple and Efficient method for Dubbed Audio Sync Detection using Compressive Sensing](s2:e0dcef74307d12f0b757c5a914a0925bf818bfcb.md)
**Avijit Vajpayee, Zhikang Zhang, Abhinav Jain, Vimal Bhat** · 2023-01-01

<details>
<summary>Abstract</summary>

Lack of temporal synchronization between audio and video streams represents one of the major quality defects in videos. The defect is more prominent in dubbed media due to errors in post-production such as improper audio overlay. Prior works in Audio-Video sync detection rely on either lip synchronization methods, which cannot be applied to dubbed media, or on self-supervised embeddings for general sound events, which are not accurate. In this paper, we present a novel, accurate and efficient method for temporal sync detection between dubbed audio tracks and corresponding non-dubbed original-language audio tracks. Using the availability of non-dubbed audio tracks and existing lip sync methods, we can simplify the problem of “Dubbed Audio-to-Video” sync detection to that of “Dubbed Audio-to-Original Audio” sync detection. Our method finds and compares matching frames in compressed audio signatures, achieving near perfect classification with 99.4 F1 score in less than 1 minute of processing time per hour of audio, along with ≈ 99.6% relative reduction in memory footprint compared to an uncompressed full audio spectrogram. We believe this is the first work to tackle temporal sync detection in dubbed media.

</details>

### [DreamTalk: When Expressive Talking Head Generation Meets Diffusion Probabilistic Models](s2:ccfaf773a4c4d6ac3e3da2c573846488cabfe449.md)
**Yifeng Ma, Shiwei Zhang, Jiayu Wang, Xiang Wang et al.** · 2023-01-01

