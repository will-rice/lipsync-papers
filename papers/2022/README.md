# 2022

53 papers in this year.

### [All's well that FID's well? Result quality and metric scores in GAN models for lip-sychronization tasks](2212.13810.md)
**Carina Geldhauser, Johan Liljegren, Pontus Nordqvist** · 2022-12-28

<details>
<summary>Abstract</summary>

We test the performance of GAN models for lip-synchronization. For this, we reimplement LipGAN in Pytorch, train it on the dataset GRID and compare it to our own variation, L1WGAN-GP, adapted to the LipGAN architecture and also trained on GRID.

</details>

### [An Audio-Visual Speech Separation Model Inspired by Cortico-Thalamo-Cortical Circuits](2212.10744.md)
**Kai Li, Fenghua Xie, Hang Chen, Kexin Yuan et al.** · 2022-12-21

<details>
<summary>Abstract</summary>

Audio-visual approaches involving visual inputs have laid the foundation for recent progress in speech separation. However, the optimization of the concurrent usage of auditory and visual inputs is still an active research area. Inspired by the cortico-thalamo-cortical circuit, in which the sensory processing mechanisms of different modalities modulate one another via the non-lemniscal sensory thalamus, we propose a novel cortico-thalamo-cortical neural network (CTCNet) for audio-visual speech separation (AVSS). First, the CTCNet learns hierarchical auditory and visual representations in a bottom-up manner in separate auditory and visual subnetworks, mimicking the functions of the auditory and visual cortical areas. Then, inspired by the large number of connections between cortical regions and the thalamus, the model fuses the auditory and visual information in a thalamic subnetwork through top-down connections. Finally, the model transmits this fused information back to the auditory and visual subnetworks, and the above process is repeated several times. The results of experiments on three speech separation benchmark datasets show that CTCNet remarkably outperforms existing AVSS methods with considerably fewer parameters. These results suggest that mimicking the anatomical connectome of the mammalian brain has great potential for advancing the development of deep neural networks. Project repo is https://github.com/JusperLee/CTCNet.

</details>

### [Masked Lip-Sync Prediction by Audio-Visual Contextual Exploitation in Transformers](2212.04970.md)
**Yasheng Sun, Hang Zhou, Kaisiyuan Wang, Qianyi Wu et al.** · 2022-12-09

<details>
<summary>Abstract</summary>

Previous studies have explored generating accurately lip-synced talking faces for arbitrary targets given audio conditions. However, most of them deform or generate the whole facial area, leading to non-realistic results. In this work, we delve into the formulation of altering only the mouth shapes of the target person. This requires masking a large percentage of the original image and seamlessly inpainting it with the aid of audio and reference frames. To this end, we propose the Audio-Visual Context-Aware Transformer (AV-CAT) framework, which produces accurate lip-sync with photo-realistic quality by predicting the masked mouth shapes. Our key insight is to exploit desired contextual information provided in audio and visual modalities thoroughly with delicately designed Transformers. Specifically, we propose a convolution-Transformer hybrid backbone and design an attention-based fusion strategy for filling the masked parts. It uniformly attends to the textural information on the unmasked regions and the reference frame. Then the semantic audio information is involved in enhancing the self-attention computation. Additionally, a refinement network with audio injection improves both image and lip-sync quality. Extensive experiments validate that our model can generate high-fidelity lip-synced results for arbitrary subjects.

</details>

### [Memories are One-to-Many Mapping Alleviators in Talking Face Generation](2212.05005.md)
**Anni Tang, Tianyu He, Xu Tan, Jun Ling et al.** · 2022-12-09

<details>
<summary>Abstract</summary>

Talking face generation aims at generating photo-realistic video portraits of a target person driven by input audio. Due to its nature of one-to-many mapping from the input audio to the output video (e.g., one speech content may have multiple feasible visual appearances), learning a deterministic mapping like previous works brings ambiguity during training, and thus causes inferior visual results. Although this one-to-many mapping could be alleviated in part by a two-stage framework (i.e., an audio-to-expression model followed by a neural-rendering model), it is still insufficient since the prediction is produced without enough information (e.g., emotions, wrinkles, etc.). In this paper, we propose MemFace to complement the missing information with an implicit memory and an explicit memory that follow the sense of the two stages respectively. More specifically, the implicit memory is employed in the audio-to-expression model to capture high-level semantics in the audio-expression shared space, while the explicit memory is employed in the neural-rendering model to help synthesize pixel-level details. Our experimental results show that our proposed MemFace surpasses all the state-of-the-art results across multiple scenarios consistently and significantly.

</details>

### [Talking Head Generation with Probabilistic Audio-to-Visual Diffusion Priors](2212.04248.md)
**Zhentao Yu, Zixin Yin, Deyu Zhou, Duomin Wang et al.** · 2022-12-07

<details>
<summary>Abstract</summary>

In this paper, we introduce a simple and novel framework for one-shot audio-driven talking head generation. Unlike prior works that require additional driving sources for controlled synthesis in a deterministic manner, we instead probabilistically sample all the holistic lip-irrelevant facial motions (i.e. pose, expression, blink, gaze, etc.) to semantically match the input audio while still maintaining both the photo-realism of audio-lip synchronization and the overall naturalness. This is achieved by our newly proposed audio-to-visual diffusion prior trained on top of the mapping between audio and disentangled non-lip facial representations. Thanks to the probabilistic nature of the diffusion prior, one big advantage of our framework is it can synthesize diverse facial motion sequences given the same audio clip, which is quite user-friendly for many real applications. Through comprehensive evaluations on public benchmarks, we conclude that (1) our diffusion prior outperforms auto-regressive prior significantly on almost all the concerned metrics; (2) our overall system is competitive with prior works in terms of audio-lip synchronization but can effectively sample rich and natural-looking lip-irrelevant facial motions while still semantically harmonized with the audio input.

</details>

### [Self-Supervised Audio-Visual Speech Representations Learning By Multimodal Self-Distillation](2212.02782.md)
**Jing-Xuan Zhang, Genshun Wan, Zhen-Hua Ling, Jia Pan et al.** · 2022-12-06

<details>
<summary>Abstract</summary>

In this work, we present a novel method, named AV2vec, for learning audio-visual speech representations by multimodal self-distillation. AV2vec has a student and a teacher module, in which the student performs a masked latent feature regression task using the multimodal target features generated online by the teacher. The parameters of the teacher model are a momentum update of the student. Since our target features are generated online, AV2vec needs no iteration step like AV-HuBERT and the total training time cost is reduced to less than one-fifth. We further propose AV2vec-MLM in this study, which augments AV2vec with a masked language model (MLM)-style loss using multitask learning. Our experimental results show that AV2vec achieved comparable performance to the AV-HuBERT baseline. When combined with an MLM-style loss, AV2vec-MLM outperformed baselines and achieved the best performance on the downstream tasks.

</details>

### [High-fidelity Facial Avatar Reconstruction from Monocular Video with Generative Priors](2211.15064.md)
**Yunpeng Bai, Yanbo Fan, Xuan Wang, Yong Zhang et al.** · 2022-11-28

<details>
<summary>Abstract</summary>

High-fidelity facial avatar reconstruction from a monocular video is a significant research problem in computer graphics and computer vision. Recently, Neural Radiance Field (NeRF) has shown impressive novel view rendering results and has been considered for facial avatar reconstruction. However, the complex facial dynamics and missing 3D information in monocular videos raise significant challenges for faithful facial reconstruction. In this work, we propose a new method for NeRF-based facial avatar reconstruction that utilizes 3D-aware generative prior. Different from existing works that depend on a conditional deformation field for dynamic modeling, we propose to learn a personalized generative prior, which is formulated as a local and low dimensional subspace in the latent space of 3D-GAN. We propose an efficient method to construct the personalized generative prior based on a small set of facial images of a given individual. After learning, it allows for photo-realistic rendering with novel views and the face reenactment can be realized by performing navigation in the latent space. Our proposed method is applicable for different driven signals, including RGB images, 3DMM coefficients, and audios. Compared with existing works, we obtain superior novel view synthesis results and faithfully face reenactment performance.

</details>

### [VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild](2211.14758.md)
**Kun Cheng, Xiaodong Cun, Yong Zhang, Menghan Xia et al.** · 2022-11-27

<details>
<summary>Abstract</summary>

We present VideoReTalking, a new system to edit the faces of a real-world talking head video according to input audio, producing a high-quality and lip-syncing output video even with a different emotion. Our system disentangles this objective into three sequential tasks: (1) face video generation with a canonical expression; (2) audio-driven lip-sync; and (3) face enhancement for improving photo-realism. Given a talking-head video, we first modify the expression of each frame according to the same expression template using the expression editing network, resulting in a video with the canonical expression. This video, together with the given audio, is then fed into the lip-sync network to generate a lip-syncing video. Finally, we improve the photo-realism of the synthesized faces through an identity-aware face enhancement network and post-processing. We use learning-based approaches for all three steps and all our modules can be tackled in a sequential pipeline without any user intervention. Furthermore, our system is a generic approach that does not need to be retrained to a specific person. Evaluations on two widely-used datasets and in-the-wild examples demonstrate the superiority of our framework over other state-of-the-art methods in terms of lip-sync accuracy and visual quality.

</details>

### [LA-VocE: Low-SNR Audio-visual Speech Enhancement using Neural Vocoders](2211.10999.md)
**Rodrigo Mira, Buye Xu, Jacob Donley, Anurag Kumar et al.** · 2022-11-20

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement aims to extract clean speech from a noisy environment by leveraging not only the audio itself but also the target speaker's lip movements. This approach has been shown to yield improvements over audio-only speech enhancement, particularly for the removal of interfering speech. Despite recent advances in speech synthesis, most audio-visual approaches continue to use spectral mapping/masking to reproduce the clean audio, often resulting in visual backbones added to existing speech enhancement architectures. In this work, we propose LA-VocE, a new two-stage approach that predicts mel-spectrograms from noisy audio-visual speech via a transformer-based architecture, and then converts them into waveform audio using a neural vocoder (HiFi-GAN). We train and evaluate our framework on thousands of speakers and 11+ different languages, and study our model's ability to adapt to different levels of background noise and speech interference. Our experiments show that LA-VocE outperforms existing methods according to multiple metrics, particularly under very noisy scenarios.

</details>

### [MARLIN: Masked Autoencoder for facial video Representation LearnINg](2211.06627.md)
**Zhixi Cai, Shreya Ghosh, Kalin Stefanov, Abhinav Dhall et al.** · 2022-11-12

<details>
<summary>Abstract</summary>

This paper proposes a self-supervised approach to learn universal facial representations from videos, that can transfer across a variety of facial analysis tasks such as Facial Attribute Recognition (FAR), Facial Expression Recognition (FER), DeepFake Detection (DFD), and Lip Synchronization (LS). Our proposed framework, named MARLIN, is a facial video masked autoencoder, that learns highly robust and generic facial embeddings from abundantly available non-annotated web crawled facial videos. As a challenging auxiliary task, MARLIN reconstructs the spatio-temporal details of the face from the densely masked facial regions which mainly include eyes, nose, mouth, lips, and skin to capture local and global aspects that in turn help in encoding generic and transferable features. Through a variety of experiments on diverse downstream tasks, we demonstrate MARLIN to be an excellent facial video encoder as well as feature extractor, that performs consistently well across a variety of downstream tasks including FAR (1.13% gain over supervised benchmark), FER (2.64% gain over unsupervised benchmark), DFD (1.86% gain over unsupervised benchmark), LS (29.36% gain for Frechet Inception Distance), and even in low data regime. Our code and models are available at https://github.com/ControlNet/MARLIN .

</details>

### [Lip Sync Matters: A Novel Multimodal Forgery Detector](s2:71c614bd54f89d0d618e2a917349c37a875eedab.md)
**Sahibzada Adil Shahzad, Ammarah Hashmi, S. Khan, Yan-Tsung Peng et al.** · 2022-11-07

<details>
<summary>Abstract</summary>

Deepfake technology has advanced a lot, but it is a double-sided sword for the community. One can use it for beneficial purposes, such as restoring vintage content in old movies, or for nefarious purposes, such as creating fake footage to manipulate the public and distribute non-consensual pornography. A lot of work has been done to combat its improper use by detecting fake footage with good performance thanks to the availability of numerous public datasets and unimodal deep learning-based models. However, these methods are insufficient to detect multimodal manipulations, such as both visual and acoustic. This work proposes a novel lip-reading-based multi-modal Deepfake detection method called “Lip Sync Matters.” It targets high-level semantic features to exploit the mismatch between the lip sequence extracted from the video and the synthetic lip sequence generated from the audio by the Wav2lip model to detect forged videos. Experimental results show that the proposed method outperforms several existing unimodal, ensemble, and multimodal methods on the publicly available multimodal FakeAVCeleb dataset.

</details>

### [Autoregressive GAN for Semantic Unconditional Head Motion Generation](2211.00987.md)
**Louis Airale, Xavier Alameda-Pineda, Stéphane Lathuilière, Dominique Vaufreydaz** · 2022-11-02

<details>
<summary>Abstract</summary>

In this work, we address the task of unconditional head motion generation to animate still human faces in a low-dimensional semantic space from a single reference pose. Different from traditional audio-conditioned talking head generation that seldom puts emphasis on realistic head motions, we devise a GAN-based architecture that learns to synthesize rich head motion sequences over long duration while maintaining low error accumulation levels.In particular, the autoregressive generation of incremental outputs ensures smooth trajectories, while a multi-scale discriminator on input pairs drives generation toward better handling of high- and low-frequency signals and less mode collapse.We experimentally demonstrate the relevance of the proposed method and show its superiority compared to models that attained state-of-the-art performances on similar tasks.

</details>

### [Audio-visual speech enhancement with a deep Kalman filter generative model](2211.00988.md)
**Ali Golmakani, Mostafa Sadeghi, Romain Serizel** · 2022-11-02

<details>
<summary>Abstract</summary>

Deep latent variable generative models based on variational autoencoder (VAE) have shown promising performance for audiovisual speech enhancement (AVSE). The underlying idea is to learn a VAEbased audiovisual prior distribution for clean speech data, and then combine it with a statistical noise model to recover a speech signal from a noisy audio recording and video (lip images) of the target speaker. Existing generative models developed for AVSE do not take into account the sequential nature of speech data, which prevents them from fully incorporating the power of visual data. In this paper, we present an audiovisual deep Kalman filter (AV-DKF) generative model which assumes a first-order Markov chain model for the latent variables and effectively fuses audiovisual data. Moreover, we develop an efficient inference methodology to estimate speech signals at test time. We conduct a set of experiments to compare different variants of generative models for speech enhancement. The results demonstrate the superiority of the AV-DKF model compared with both its audio-only version and the non-sequential audio-only and audiovisual VAE-based models.

</details>

### [A Novel Frame Structure for Cloud-Based Audio-Visual Speech Enhancement in Multimodal Hearing-aids](2210.13127.md)
**Abhijeet Bishnu, Ankit Gupta, Mandar Gogate, Kia Dashtipour et al.** · 2022-10-24

<details>
<summary>Abstract</summary>

In this paper, we design a first of its kind transceiver (PHY layer) prototype for cloud-based audio-visual (AV) speech enhancement (SE) complying with high data rate and low latency requirements of future multimodal hearing assistive technology. The innovative design needs to meet multiple challenging constraints including up/down link communications, delay of transmission and signal processing, and real-time AV SE models processing. The transceiver includes device detection, frame detection, frequency offset estimation, and channel estimation capabilities. We develop both uplink (hearing aid to the cloud) and downlink (cloud to hearing aid) frame structures based on the data rate and latency requirements. Due to the varying nature of uplink information (audio and lip-reading), the uplink channel supports multiple data rate frame structure, while the downlink channel has a fixed data rate frame structure. In addition, we evaluate the latency of different PHY layer blocks of the transceiver for developed frame structures using LabVIEW NXG. This can be used with software defined radio (such as Universal Software Radio Peripheral) for real-time demonstration scenarios.

</details>

### [Sparse in Space and Time: Audio-visual Synchronisation with Trainable Selectors](2210.07055.md)
**Vladimir Iashin, Weidi Xie, Esa Rahtu, Andrew Zisserman** · 2022-10-13

<details>
<summary>Abstract</summary>

The objective of this paper is audio-visual synchronisation of general videos 'in the wild'. For such videos, the events that may be harnessed for synchronisation cues may be spatially small and may occur only infrequently during a many seconds-long video clip, i.e. the synchronisation signal is 'sparse in space and time'. This contrasts with the case of synchronising videos of talking heads, where audio-visual correspondence is dense in both time and space. We make four contributions: (i) in order to handle longer temporal sequences required for sparse synchronisation signals, we design a multi-modal transformer model that employs 'selectors' to distil the long audio and visual streams into small sequences that are then used to predict the temporal offset between streams. (ii) We identify artefacts that can arise from the compression codecs used for audio and video and can be used by audio-visual models in training to artificially solve the synchronisation task. (iii) We curate a dataset with only sparse in time and space synchronisation signals; and (iv) the effectiveness of the proposed model is shown on both dense and sparse datasets quantitatively and qualitatively. Project page: v-iashin.github.io/SparseSync

</details>

### [StyleMask: Disentangling the Style Space of StyleGAN2 for Neural Face Reenactment](2209.13375.md)
**Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras et al.** · 2022-09-27

<details>
<summary>Abstract</summary>

In this paper we address the problem of neural face reenactment, where, given a pair of a source and a target facial image, we need to transfer the target's pose (defined as the head pose and its facial expressions) to the source image, by preserving at the same time the source's identity characteristics (e.g., facial shape, hair style, etc), even in the challenging case where the source and the target faces belong to different identities. In doing so, we address some of the limitations of the state-of-the-art works, namely, a) that they depend on paired training data (i.e., source and target faces have the same identity), b) that they rely on labeled data during inference, and c) that they do not preserve identity in large head pose changes. More specifically, we propose a framework that, using unpaired randomly generated facial images, learns to disentangle the identity characteristics of the face from its pose by incorporating the recently introduced style space $\mathcal{S}$ of StyleGAN2, a latent representation space that exhibits remarkable disentanglement properties. By capitalizing on this, we learn to successfully mix a pair of source and target style codes using supervision from a 3D model. The resulting latent code, that is subsequently used for reenactment, consists of latent units corresponding to the facial pose of the target only and of units corresponding to the identity of the source only, leading to notable improvement in the reenactment performance compared to recent state-of-the-art methods. In comparison to state of the art, we quantitatively and qualitatively show that the proposed method produces higher quality results even on extreme pose variations. Finally, we report results on real images by first embedding them on the latent space of the pretrained generator. We make the code and pretrained models publicly available at: https://github.com/StelaBou/StyleMask

</details>

### [Gemino: Practical and Robust Neural Compression for Video Conferencing](2209.10507.md)
**Vibhaalakshmi Sivaraman, Pantea Karimi, Vedantha Venkatapathy, Mehrdad Khani et al.** · 2022-09-21

<details>
<summary>Abstract</summary>

Video conferencing systems suffer from poor user experience when network conditions deteriorate because current video codecs simply cannot operate at extremely low bitrates. Recently, several neural alternatives have been proposed that reconstruct talking head videos at very low bitrates using sparse representations of each frame such as facial landmark information. However, these approaches produce poor reconstructions in scenarios with major movement or occlusions over the course of a call, and do not scale to higher resolutions. We design Gemino, a new neural compression system for video conferencing based on a novel high-frequency-conditional super-resolution pipeline. Gemino upsamples a very low-resolution version of each target frame while enhancing high-frequency details (e.g., skin texture, hair, etc.) based on information extracted from a single high-resolution reference image. We use a multi-scale architecture that runs different components of the model at different resolutions, allowing it to scale to resolutions comparable to 720p, and we personalize the model to learn specific details of each person, achieving much better fidelity at low bitrates. We implement Gemino atop aiortc, an open-source Python implementation of WebRTC, and show that it operates on 1024x1024 videos in real-time on a Titan X GPU, and achieves 2.2-5x lower bitrate than traditional video codecs for the same perceptual quality.

</details>

### [Continuously Controllable Facial Expression Editing in Talking Face Videos](2209.08289.md)
**Zhiyao Sun, Yu-Hui Wen, Tian Lv, Yanan Sun et al.** · 2022-09-17

<details>
<summary>Abstract</summary>

Recently audio-driven talking face video generation has attracted considerable attention. However, very few researches address the issue of emotional editing of these talking face videos with continuously controllable expressions, which is a strong demand in the industry. The challenge is that speech-related expressions and emotion-related expressions are often highly coupled. Meanwhile, traditional image-to-image translation methods cannot work well in our application due to the coupling of expressions with other attributes such as poses, i.e., translating the expression of the character in each frame may simultaneously change the head pose due to the bias of the training data distribution. In this paper, we propose a high-quality facial expression editing method for talking face videos, allowing the user to control the target emotion in the edited video continuously. We present a new perspective for this task as a special case of motion information editing, where we use a 3DMM to capture major facial movements and an associated texture map modeled by a StyleGAN to capture appearance details. Both representations (3DMM and texture map) contain emotional information and can be continuously modified by neural networks and easily smoothed by averaging in coefficient/latent spaces, making our method simple yet effective. We also introduce a mouth shape preservation loss to control the trade-off between lip synchronization and the degree of exaggeration of the edited expression. Extensive experiments and a user study show that our method achieves state-of-the-art performance across various evaluation criteria.

</details>

### [Talking Head from Speech Audio using a Pre-trained Image Generator](2209.04252.md)
**Mohammed M. Alghamdi, He Wang, Andrew J. Bulpitt, David C. Hogg** · 2022-09-09

<details>
<summary>Abstract</summary>

We propose a novel method for generating high-resolution videos of talking-heads from speech audio and a single 'identity' image. Our method is based on a convolutional neural network model that incorporates a pre-trained StyleGAN generator. We model each frame as a point in the latent space of StyleGAN so that a video corresponds to a trajectory through the latent space. Training the network is in two stages. The first stage is to model trajectories in the latent space conditioned on speech utterances. To do this, we use an existing encoder to invert the generator, mapping from each video frame into the latent space. We train a recurrent neural network to map from speech utterances to displacements in the latent space of the image generator. These displacements are relative to the back-projection into the latent space of an identity image chosen from the individuals depicted in the training dataset. In the second stage, we improve the visual quality of the generated videos by tuning the image generator on a single image or a short video of any chosen identity. We evaluate our model on standard measures (PSNR, SSIM, FID and LMD) and show that it significantly outperforms recent state-of-the-art methods on one of two commonly used datasets and gives comparable performance on the other. Finally, we report on ablation experiments that validate the components of the model. The code and videos from experiments can be found at https://mohammedalghamdi.github.io/talking-heads-acm-mm

</details>

### [Multimodal Speech Enhancement Using Burst Propagation](2209.03275.md)
**Mohsin Raza, Leandro A. Passos, Ahmed Khubaib, Ahsan Adeel** · 2022-09-07

<details>
<summary>Abstract</summary>

This paper proposes the MBURST, a novel multimodal solution for audio-visual speech enhancements that consider the most recent neurological discoveries regarding pyramidal cells of the prefrontal cortex and other brain regions. The so-called burst propagation implements several criteria to address the credit assignment problem in a more biologically plausible manner: steering the sign and magnitude of plasticity through feedback, multiplexing the feedback and feedforward information across layers through different weight connections, approximating feedback and feedforward connections, and linearizing the feedback signals. MBURST benefits from such capabilities to learn correlations between the noisy signal and the visual stimuli, thus attributing meaning to the speech by amplifying relevant information and suppressing noise. Experiments conducted over a Grid Corpus and CHiME3-based dataset show that MBURST can reproduce similar mask reconstructions to the multimodal backpropagation-based baseline while demonstrating outstanding energy efficiency management, reducing the neuron firing rates to values up to \textbf{$70\%$} lower. Such a feature implies more sustainable implementations, suitable and desirable for hearing aids or any other similar embedded systems.

</details>

### [StableFace: Analyzing and Improving Motion Stability for Talking Face Generation](2208.13717.md)
**Jun Ling, Xu Tan, Liyang Chen, Runnan Li et al.** · 2022-08-29

<details>
<summary>Abstract</summary>

While previous speech-driven talking face generation methods have made significant progress in improving the visual quality and lip-sync quality of the synthesized videos, they pay less attention to lip motion jitters which greatly undermine the realness of talking face videos. What causes motion jitters, and how to mitigate the problem? In this paper, we conduct systematic analyses on the motion jittering problem based on a state-of-the-art pipeline that uses 3D face representations to bridge the input audio and output video, and improve the motion stability with a series of effective designs. We find that several issues can lead to jitters in synthesized talking face video: 1) jitters from the input 3D face representations; 2) training-inference mismatch; 3) lack of dependency modeling among video frames. Accordingly, we propose three effective solutions to address this issue: 1) we propose a gaussian-based adaptive smoothing module to smooth the 3D face representations to eliminate jitters in the input; 2) we add augmented erosions on the input data of the neural renderer in training to simulate the distortion in inference to reduce mismatch; 3) we develop an audio-fused transformer generator to model dependency among video frames. Besides, considering there is no off-the-shelf metric for measuring motion jitters in talking face video, we devise an objective metric (Motion Stability Index, MSI), to quantitatively measure the motion jitters by calculating the reciprocal of variance acceleration. Extensive experimental results show the superiority of our method on motion-stable face video generation, with better quality than previous systems.

</details>

### [Towards MOOCs for Lipreading: Using Synthetic Talking Heads to Train Humans in Lipreading at Scale](2208.09796.md)
**Aditya Agarwal, Bipasha Sen, Rudrabha Mukhopadhyay, Vinay Namboodiri et al.** · 2022-08-21

<details>
<summary>Abstract</summary>

Many people with some form of hearing loss consider lipreading as their primary mode of day-to-day communication. However, finding resources to learn or improve one's lipreading skills can be challenging. This is further exacerbated in the COVID19 pandemic due to restrictions on direct interactions with peers and speech therapists. Today, online MOOCs platforms like Coursera and Udemy have become the most effective form of training for many types of skill development. However, online lipreading resources are scarce as creating such resources is an extensive process needing months of manual effort to record hired actors. Because of the manual pipeline, such platforms are also limited in vocabulary, supported languages, accents, and speakers and have a high usage cost. In this work, we investigate the possibility of replacing real human talking videos with synthetically generated videos. Synthetic data can easily incorporate larger vocabularies, variations in accent, and even local languages and many speakers. We propose an end-to-end automated pipeline to develop such a platform using state-of-the-art talking head video generator networks, text-to-speech models, and computer vision techniques. We then perform an extensive human evaluation using carefully thought out lipreading exercises to validate the quality of our designed platform against the existing lipreading platforms. Our studies concretely point toward the potential of our approach in developing a large-scale lipreading MOOC platform that can impact millions of people with hearing loss.

</details>

### [Free-HeadGAN: Neural Talking Head Synthesis with Explicit Gaze Control](2208.02210.md)
**Michail Christos Doukas, Evangelos Ververas, Viktoriia Sharmanska, Stefanos Zafeiriou** · 2022-08-03

<details>
<summary>Abstract</summary>

We present Free-HeadGAN, a person-generic neural talking head synthesis system. We show that modeling faces with sparse 3D facial landmarks are sufficient for achieving state-of-the-art generative performance, without relying on strong statistical priors of the face, such as 3D Morphable Models. Apart from 3D pose and facial expressions, our method is capable of fully transferring the eye gaze, from a driving actor to a source identity. Our complete pipeline consists of three components: a canonical 3D key-point estimator that regresses 3D pose and expression-related deformations, a gaze estimation network and a generator that is built upon the architecture of HeadGAN. We further experiment with an extension of our generator to accommodate few-shot learning using an attention mechanism, in case more than one source images are available. Compared to the latest models for reenactment and motion transfer, our system achieves higher photo-realism combined with superior identity preservation, while offering explicit gaze control.

</details>

### [Visual Speech-Aware Perceptual 3D Facial Expression Reconstruction from Videos](2207.11094.md)
**Panagiotis P. Filntisis, George Retsinas, Foivos Paraperas-Papantoniou, Athanasios Katsamanis et al.** · 2022-07-22

<details>
<summary>Abstract</summary>

The recent state of the art on monocular 3D face reconstruction from image data has made some impressive advancements, thanks to the advent of Deep Learning. However, it has mostly focused on input coming from a single RGB image, overlooking the following important factors: a) Nowadays, the vast majority of facial image data of interest do not originate from single images but rather from videos, which contain rich dynamic information. b) Furthermore, these videos typically capture individuals in some form of verbal communication (public talks, teleconferences, audiovisual human-computer interactions, interviews, monologues/dialogues in movies, etc). When existing 3D face reconstruction methods are applied in such videos, the artifacts in the reconstruction of the shape and motion of the mouth area are often severe, since they do not match well with the speech audio. To overcome the aforementioned limitations, we present the first method for visual speech-aware perceptual reconstruction of 3D mouth expressions. We do this by proposing a "lipread" loss, which guides the fitting process so that the elicited perception from the 3D reconstructed talking head resembles that of the original video footage. We demonstrate that, interestingly, the lipread loss is better suited for 3D reconstruction of mouth movements compared to traditional landmark losses, and even direct 3D supervision. Furthermore, the devised method does not rely on any text transcriptions or corresponding audio, rendering it ideal for training in unlabeled datasets. We verify the efficiency of our method through exhaustive objective evaluations on three large-scale datasets, as well as subjective evaluation with two web-based user studies.

</details>

### [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](2207.03800.md)
**Yongqi Wang, Zhou Zhao** · 2022-07-08

<details>
<summary>Abstract</summary>

Unconstrained lip-to-speech synthesis aims to generate corresponding speeches from silent videos of talking faces with no restriction on head poses or vocabulary. Current works mainly use sequence-to-sequence models to solve this problem, either in an autoregressive architecture or a flow-based non-autoregressive architecture. However, these models suffer from several drawbacks: 1) Instead of directly generating audios, they use a two-stage pipeline that first generates mel-spectrograms and then reconstructs audios from the spectrograms. This causes cumbersome deployment and degradation of speech quality due to error propagation; 2) The audio reconstruction algorithm used by these models limits the inference speed and audio quality, while neural vocoders are not available for these models since their output spectrograms are not accurate enough; 3) The autoregressive model suffers from high inference latency, while the flow-based model has high memory occupancy: neither of them is efficient enough in both time and memory usage. To tackle these problems, we propose FastLTS, a non-autoregressive end-to-end model which can directly synthesize high-quality speech audios from unconstrained talking videos with low latency, and has a relatively small model size. Besides, different from the widely used 3D-CNN visual frontend for lip movement encoding, we for the first time propose a transformer-based visual frontend for this task. Experiments show that our model achieves $19.76\times$ speedup for audio waveform generation compared with the current autoregressive model on input sequences of 3 seconds, and obtains superior audio quality.

</details>

### [Improving Visual Speech Enhancement Network by Learning Audio-visual Affinity with Multi-head Attention](2206.14964.md)
**Xinmeng Xu, Yang Wang, Jie Jia, Binbin Chen et al.** · 2022-06-30

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement system is regarded as one of promising solutions for isolating and enhancing speech of desired speaker. Typical methods focus on predicting clean speech spectrum via a naive convolution neural network based encoder-decoder architecture, and these methods a) are not adequate to use data fully, b) are unable to effectively balance audio-visual features. The proposed model alleviates these drawbacks by a) applying a model that fuses audio and visual features layer by layer in encoding phase, and that feeds fused audio-visual features to each corresponding decoder layer, and more importantly, b) introducing a 2-stage multi-head cross attention (MHCA) mechanism to infer audio-visual speech enhancement for balancing the fused audio-visual features and eliminating irrelevant features. This paper proposes attentional audio-visual multi-layer feature fusion model, in which MHCA units are applied to feature mapping at every layer of decoder. The proposed model demonstrates the superior performance of the network against the state-of-the-art models.

</details>

### [Cut Inner Layers: A Structured Pruning Strategy for Efficient U-Net GANs](2206.14658.md)
**Bo-Kyeong Kim, Shinkook Choi, Hancheol Park** · 2022-06-29

<details>
<summary>Abstract</summary>

Pruning effectively compresses overparameterized models. Despite the success of pruning methods for discriminative models, applying them for generative models has been relatively rarely approached. This study conducts structured pruning on U-Net generators of conditional GANs. A per-layer sensitivity analysis confirms that many unnecessary filters exist in the innermost layers near the bottleneck and can be substantially pruned. Based on this observation, we prune these filters from multiple inner layers or suggest alternative architectures by completely eliminating the layers. We evaluate our approach with Pix2Pix for image-to-image translation and Wav2Lip for speech-driven talking face generation. Our method outperforms global pruning baselines, demonstrating the importance of properly considering where to prune for U-Net generators.

</details>

### [Canonical Cortical Graph Neural Networks and its Application for Speech Enhancement in Audio-Visual Hearing Aids](2206.02671.md)
**Leandro A. Passos, João Paulo Papa, Amir Hussain, Ahsan Adeel** · 2022-06-06

<details>
<summary>Abstract</summary>

Despite the recent success of machine learning algorithms, most models face drawbacks when considering more complex tasks requiring interaction between different sources, such as multimodal input data and logical time sequences. On the other hand, the biological brain is highly sharpened in this sense, empowered to automatically manage and integrate such streams of information. In this context, this work draws inspiration from recent discoveries in brain cortical circuits to propose a more biologically plausible self-supervised machine learning approach. This combines multimodal information using intra-layer modulations together with Canonical Correlation Analysis, and a memory mechanism to keep track of temporal data, the overall approach termed Canonical Cortical Graph Neural networks. This is shown to outperform recent state-of-the-art models in terms of clean audio reconstruction and energy efficiency for a benchmark audio-visual speech dataset. The enhanced performance is demonstrated through a reduced and smother neuron firing rate distribution. suggesting that the proposed model is amenable for speech enhancement in future audio-visual hearing aid devices.

</details>

### [Learning Speaker-specific Lip-to-Speech Generation](2206.02050.md)
**Munender Varshney, Ravindra Yadav, Vinay P. Namboodiri, R. Hegde** · 2022-06-04

<details>
<summary>Abstract</summary>

Understanding the lip movement and inferring the speech from it is notoriously difficult for the common person. The task of accurate lip-reading gets help from various cues of the speaker and its contextual or environmental setting. Every speaker has a different accent and speaking style, which can be inferred from their visual and speech features. This work aims to understand the correlation/mapping between speech and the sequence of lip movement of individual speakers in an unconstrained and large vocabulary. We model the frame sequence as a distribution of features from the transformer in an autoencoder setting and learn the embeddings jointly that exploits temporal properties of both audio and video. We learn temporal synchronization using deep metric learning, which guides the decoder to generate speech in sync with input lip movements. The predictive posterior thus gives us the generated speech in speaker speaking style. We have trained our model on the Grid and Lip2Wav Chemistry lecture dataset to evaluate single speaker natural speech generation tasks from lip movement in an unconstrained natural setting. Extensive evaluation using various qualitative and quantitative metrics with human evaluation also shows that our method outperforms on Lip2Wav Chemistry dataset (large vocabulary in an unconstrained setting) by a good margin across almost all evaluation metrics and marginally outperforms the state-of-the-art on GRID dataset.

</details>

### [One-Shot Face Reenactment on Megapixels](2205.13368.md)
**Wonjun Kang, Geonsu Lee, Hyung Il Koo, Nam Ik Cho** · 2022-05-26

<details>
<summary>Abstract</summary>

The goal of face reenactment is to transfer a target expression and head pose to a source face while preserving the source identity. With the popularity of face-related applications, there has been much research on this topic. However, the results of existing methods are still limited to low-resolution and lack photorealism. In this work, we present a one-shot and high-resolution face reenactment method called MegaFR. To be precise, we leverage StyleGAN by using 3DMM-based rendering images and overcome the lack of high-quality video datasets by designing a loss function that works without high-quality videos. Also, we apply iterative refinement to deal with extreme poses and/or expressions. Since the proposed method controls source images through 3DMM parameters, we can explicitly manipulate source images. We apply MegaFR to various applications such as face frontalization, eye in-painting, and talking head generation. Experimental results show that our method successfully disentangles identity from expression and head pose, and outperforms conventional methods.

</details>

### [Merkel Podcast Corpus: A Multimodal Dataset Compiled from 16 Years of Angela Merkel's Weekly Video Podcasts](2205.12194.md)
**Debjoy Saha, Shravan Nayak, Timo Baumann** · 2022-05-24

<details>
<summary>Abstract</summary>

We introduce the Merkel Podcast Corpus, an audio-visual-text corpus in German collected from 16 years of (almost) weekly Internet podcasts of former German chancellor Angela Merkel. To the best of our knowledge, this is the first single speaker corpus in the German language consisting of audio, visual and text modalities of comparable size and temporal extent. We describe the methods used with which we have collected and edited the data which involves downloading the videos, transcripts and other metadata, forced alignment, performing active speaker recognition and face detection to finally curate the single speaker dataset consisting of utterances spoken by Angela Merkel. The proposed pipeline is general and can be used to curate other datasets of similar nature, such as talk show contents. Through various statistical analyses and applications of the dataset in talking face generation and TTS, we show the utility of the dataset. We argue that it is a valuable contribution to the research community, in particular, due to its realistic and challenging material at the boundary between prepared and spontaneous speech.

</details>

### [Meta Talk: Learning To Data-Efficiently Generate Audio-Driven Lip-Synchronized Talking Face With High Definition](s2:e3d8c277a9a688d57ca1d33408ba36b2c3c4ec66.md)
**Yuhan Zhang, Weihua He, Minglei Li, Kun Tian et al.** · 2022-05-23

<details>
<summary>Abstract</summary>

Audio-driven talking face, driving talking face by audio, has received considerable attention in multi-modal learning due to its widespread use in virtual reality. However, long-time recording of target high-quality video is needed by most existing audio-driven talking face studies, which significantly increases customization costs. This paper proposes a novel data-efficient audio-driven talking face generation method, which uses just a short target video to produce both lip-synchronized and high-definition face video driven by arbitrary audio in the wild. Current methods suffer from many problems, such as low definition, asynchronization of lip movement and voice, and intense demands for videos for training. In this work, the original target character’s face images are decomposed into 3D face model parameters including expression, geometry, illumination, etc. Then, low-definition pseudo video generated by an adapted target face video bridges the powerful pre-trained audio-driven model to our audio-to-expression transformation network and help to transfer the ability of audio-identity disentanglement. The expression is replaced via an audio and then combined with other face parameters to render a synthetic face. Finally, a neural rendering network translates the synthetic face into talking face without loss of definition. Experimental results show that the proposed method has the best performance in high-definition image quality, and comparable performance in lip synchronization compared with the existing state-of-the-art methods.

</details>

### [Learning Lip-Based Audio-Visual Speaker Embeddings with AV-HuBERT](2205.07180.md)
**Bowen Shi, Abdelrahman Mohamed, Wei-Ning Hsu** · 2022-05-15

<details>
<summary>Abstract</summary>

This paper investigates self-supervised pre-training for audio-visual speaker representation learning where a visual stream showing the speaker's mouth area is used alongside speech as inputs. Our study focuses on the Audio-Visual Hidden Unit BERT (AV-HuBERT) approach, a recently developed general-purpose audio-visual speech pre-training framework. We conducted extensive experiments probing the effectiveness of pre-training and visual modality. Experimental results suggest that AV-HuBERT generalizes decently to speaker related downstream tasks, improving label efficiency by roughly ten fold for both audio-only and audio-visual speaker verification. We also show that incorporating visual information, even just the lip area, greatly improves the performance and noise robustness, reducing EER by 38% in the clean condition and 75% in noisy conditions.

</details>

### [Talking Face Generation with Multilingual TTS](2205.06421.md)
**Hyoung-Kyu Song, Sang Hoon Woo, Junhyeok Lee, Seungmin Yang et al.** · 2022-05-13

<details>
<summary>Abstract</summary>

In this work, we propose a joint system combining a talking face generation system with a text-to-speech system that can generate multilingual talking face videos from only the text input. Our system can synthesize natural multilingual speeches while maintaining the vocal identity of the speaker, as well as lip movements synchronized to the synthesized speech. We demonstrate the generalization capabilities of our system by selecting four languages (Korean, English, Japanese, and Chinese) each from a different language family. We also compare the outputs of our talking face generation model to outputs of a prior work that claims multilingual support. For our demo, we add a translation API to the preprocessing stage and present it in the form of a neural dubber so that users can utilize the multilingual property of our system more easily.

</details>

### [Emotion-Controllable Generalized Talking Face Generation](2205.01155.md)
**Sanjana Sinha, Sandika Biswas, Ravindra Yadav, Brojeshwar Bhowmick** · 2022-05-02

<details>
<summary>Abstract</summary>

Despite the significant progress in recent years, very few of the AI-based talking face generation methods attempt to render natural emotions. Moreover, the scope of the methods is majorly limited to the characteristics of the training dataset, hence they fail to generalize to arbitrary unseen faces. In this paper, we propose a one-shot facial geometry-aware emotional talking face generation method that can generalize to arbitrary faces. We propose a graph convolutional neural network that uses speech content feature, along with an independent emotion input to generate emotion and speech-induced motion on facial geometry-aware landmark representation. This representation is further used in our optical flow-guided texture generation network for producing the texture. We propose a two-branch texture generation network, with motion and texture branches designed to consider the motion and texture content independently. Compared to the previous emotion talking face methods, our method can adapt to arbitrary faces captured in-the-wild by fine-tuning with only a single image of the target identity in neutral emotion.

</details>

### [Talking Head Generation Driven by Speech-Related Facial Action Units and Audio- Based on Multimodal Representation Fusion](2204.12756.md)
**Sen Chen, Zhilei Liu, Jiaxing Liu, Longbiao Wang** · 2022-04-27

<details>
<summary>Abstract</summary>

Talking head generation is to synthesize a lip-synchronized talking head video by inputting an arbitrary face image and corresponding audio clips. Existing methods ignore not only the interaction and relationship of cross-modal information, but also the local driving information of the mouth muscles. In this study, we propose a novel generative framework that contains a dilated non-causal temporal convolutional self-attention network as a multimodal fusion module to promote the relationship learning of cross-modal features. In addition, our proposed method uses both audio- and speech-related facial action units (AUs) as driving information. Speech-related AU information can guide mouth movements more accurately. Because speech is highly correlated with speech-related AUs, we propose an audio-to-AU module to predict speech-related AU information. We utilize pre-trained AU classifier to ensure that the generated images contain correct AU information. We verify the effectiveness of the proposed model on the GRID and TCD-TIMIT datasets. An ablation study is also conducted to verify the contribution of each component. The results of quantitative and qualitative experiments demonstrate that our method outperforms existing methods in terms of both image quality and lip-sync accuracy.

</details>

### [Dynamic Neural Textures: Generating Talking-Face Videos with Continuously Controllable Expressions](2204.06180.md)
**Zipeng Ye, Zhiyao Sun, Yu-Hui Wen, Yanan Sun et al.** · 2022-04-13

<details>
<summary>Abstract</summary>

Recently, talking-face video generation has received considerable attention. So far most methods generate results with neutral expressions or expressions that are implicitly determined by neural networks in an uncontrollable way. In this paper, we propose a method to generate talking-face videos with continuously controllable expressions in real-time. Our method is based on an important observation: In contrast to facial geometry of moderate resolution, most expression information lies in textures. Then we make use of neural textures to generate high-quality talking face videos and design a novel neural network that can generate neural textures for image frames (which we called dynamic neural textures) based on the input expression and continuous intensity expression coding (CIEC). Our method uses 3DMM as a 3D model to sample the dynamic neural texture. The 3DMM does not cover the teeth area, so we propose a teeth submodule to complete the details in teeth. Results and an ablation study show the effectiveness of our method in generating high-quality talking-face videos with continuously controllable expressions. We also set up four baseline methods by combining existing representative methods and compare them with our method. Experimental results including a user study show that our method has the best performance.

</details>

### [Lip to Speech Synthesis with Visual Context Attentional GAN](2204.01726.md)
**Minsu Kim, Joanna Hong, Y. Ro** · 2022-04-04

<details>
<summary>Abstract</summary>

In this paper, we propose a novel lip-to-speech generative adversarial network, Visual Context Attentional GAN (VCA-GAN), which can jointly model local and global lip movements during speech synthesis. Specifically, the proposed VCA-GAN synthesizes the speech from local lip visual features by finding a mapping function of viseme-to-phoneme, while global visual context is embedded into the intermediate layers of the generator to clarify the ambiguity in the mapping induced by homophene. To achieve this, a visual context attention module is proposed where it encodes global representations from the local visual features, and provides the desired global visual context corresponding to the given coarse speech representation to the generator through audio-visual attention. In addition to the explicit modelling of local and global visual representations, synchronization learning is introduced as a form of contrastive learning that guides the generator to synthesize a speech in sync with the given input lip movements. Extensive experiments demonstrate that the proposed VCA-GAN outperforms existing state-of-the-art and is able to effectively synthesize the speech from multi-speaker that has been barely handled in the previous works.

</details>

### [End to End Lip Synchronization with a Temporal AutoEncoder](2203.16224.md)
**Yoav Shalev, Lior Wolf** · 2022-03-30

<details>
<summary>Abstract</summary>

We study the problem of syncing the lip movement in a video with the audio stream. Our solution finds an optimal alignment using a dual-domain recurrent neural network that is trained on synthetic data we generate by dropping and duplicating video frames. Once the alignment is found, we modify the video in order to sync the two sources. Our method is shown to greatly outperform the literature methods on a variety of existing and new benchmarks. As an application, we demonstrate our ability to robustly align text-to-speech generated audio with an existing video stream. Our code and samples are available at https://github.com/itsyoavshalev/End-to-End-Lip-Synchronization-with-a-Temporal-AutoEncoder.

</details>

### [Expressive Talking Head Video Encoding in StyleGAN2 Latent-Space](2203.14512.md)
**Trevine Oorloff, Yaser Yacoob** · 2022-03-28

<details>
<summary>Abstract</summary>

While the recent advances in research on video reenactment have yielded promising results, the approaches fall short in capturing the fine, detailed, and expressive facial features (e.g., lip-pressing, mouth puckering, mouth gaping, and wrinkles) which are crucial in generating realistic animated face videos. To this end, we propose an end-to-end expressive face video encoding approach that facilitates data-efficient high-quality video re-synthesis by optimizing low-dimensional edits of a single Identity-latent. The approach builds on StyleGAN2 image inversion and multi-stage non-linear latent-space editing to generate videos that are nearly comparable to input videos. While existing StyleGAN latent-based editing techniques focus on simply generating plausible edits of static images, we automate the latent-space editing to capture the fine expressive facial deformations in a sequence of frames using an encoding that resides in the Style-latent-space (StyleSpace) of StyleGAN2. The encoding thus obtained could be super-imposed on a single Identity-latent to facilitate re-enactment of face videos at $1024^2$. The proposed framework economically captures face identity, head-pose, and complex expressive facial motions at fine levels, and thereby bypasses training, person modeling, dependence on landmarks/ keypoints, and low-resolution synthesis which tend to hamper most re-enactment approaches. The approach is designed with maximum data efficiency, where a single $W+$ latent and 35 parameters per frame enable high-fidelity video rendering. This pipeline can also be used for puppeteering (i.e., motion transfer).

</details>

### [DialogueNeRF: Towards Realistic Avatar Face-to-Face Conversation Video Generation](2203.07931.md)
**Yichao Yan, Zanwei Zhou, Zi Wang, Jingnan Gao et al.** · 2022-03-15

<details>
<summary>Abstract</summary>

Conversation is an essential component of virtual avatar activities in the metaverse. With the development of natural language processing, textual and vocal conversation generation has achieved a significant breakthrough. However, face-to-face conversations account for the vast majority of daily conversations, while most existing methods focused on single-person talking head generation. In this work, we take a step further and consider generating realistic face-to-face conversation videos. Conversation generation is more challenging than single-person talking head generation, since it not only requires generating photo-realistic individual talking heads but also demands the listener to respond to the speaker. In this paper, we propose a novel unified framework based on neural radiance field (NeRF) to address this task. Specifically, we model both the speaker and listener with a NeRF framework, with different conditions to control individual expressions. The speaker is driven by the audio signal, while the response of the listener depends on both visual and acoustic information. In this way, face-to-face conversation videos are generated between human avatars, with all the interlocutors modeled within the same network. Moreover, to facilitate future research on this task, we collect a new human conversation dataset containing 34 clips of videos. Quantitative and qualitative experiments evaluate our method in different aspects, e.g., image quality, pose sequence trend, and naturalness of the rendering videos. Experimental results demonstrate that the avatars in the resulting videos are able to perform a realistic conversation, and maintain individual styles. All the code, data, and models will be made publicly available.

</details>

### [Depth-Aware Generative Adversarial Network for Talking Head Video Generation](2203.06605.md)
**Fa-Ting Hong, Longhao Zhang, Li Shen, Dan Xu** · 2022-03-13

<details>
<summary>Abstract</summary>

Talking head video generation aims to produce a synthetic human face video that contains the identity and pose information respectively from a given source image and a driving video.Existing works for this task heavily rely on 2D representations (e.g. appearance and motion) learned from the input images. However, dense 3D facial geometry (e.g. pixel-wise depth) is extremely important for this task as it is particularly beneficial for us to essentially generate accurate 3D face structures and distinguish noisy information from the possibly cluttered background. Nevertheless, dense 3D geometry annotations are prohibitively costly for videos and are typically not available for this video generation task. In this paper, we first introduce a self-supervised geometry learning method to automatically recover the dense 3D geometry (i.e.depth) from the face videos without the requirement of any expensive 3D annotation data. Based on the learned dense depth maps, we further propose to leverage them to estimate sparse facial keypoints that capture the critical movement of the human head. In a more dense way, the depth is also utilized to learn 3D-aware cross-modal (i.e. appearance and depth) attention to guide the generation of motion fields for warping source image representations. All these contributions compose a novel depth-aware generative adversarial network (DaGAN) for talking head generation. Extensive experiments conducted demonstrate that our proposed method can generate highly realistic faces, and achieve significant results on the unseen human faces.

</details>

### [An Audio-Visual Attention Based Multimodal Network for Fake Talking Face Videos Detection](2203.05178.md)
**Ganglai Wang, Peng Zhang, Lei Xie, Wei Huang et al.** · 2022-03-10

<details>
<summary>Abstract</summary>

DeepFake based digital facial forgery is threatening the public media security, especially when lip manipulation has been used in talking face generation, the difficulty of fake video detection is further improved. By only changing lip shape to match the given speech, the facial features of identity is hard to be discriminated in such fake talking face videos. Together with the lack of attention on audio stream as the prior knowledge, the detection failure of fake talking face generation also becomes inevitable. Inspired by the decision-making mechanism of human multisensory perception system, which enables the auditory information to enhance post-sensory visual evidence for informed decisions output, in this study, a fake talking face detection framework FTFDNet is proposed by incorporating audio and visual representation to achieve more accurate fake talking face videos detection. Furthermore, an audio-visual attention mechanism (AVAM) is proposed to discover more informative features, which can be seamlessly integrated into any audio-visual CNN architectures by modularization. With the additional AVAM, the proposed FTFDNet is able to achieve a better detection performance on the established dataset (FTFDD). The evaluation of the proposed work has shown an excellent performance on the detection of fake talking face videos, which is able to arrive at a detection rate above 97%.

</details>

### [StyleHEAT: One-Shot High-Resolution Editable Talking Face Generation via Pre-trained StyleGAN](2203.04036.md)
**Fei Yin, Yong Zhang, Xiaodong Cun, Mingdeng Cao et al.** · 2022-03-08

<details>
<summary>Abstract</summary>

One-shot talking face generation aims at synthesizing a high-quality talking face video from an arbitrary portrait image, driven by a video or an audio segment. One challenging quality factor is the resolution of the output video: higher resolution conveys more details. In this work, we investigate the latent feature space of a pre-trained StyleGAN and discover some excellent spatial transformation properties. Upon the observation, we explore the possibility of using a pre-trained StyleGAN to break through the resolution limit of training datasets. We propose a novel unified framework based on a pre-trained StyleGAN that enables a set of powerful functionalities, i.e., high-resolution video generation, disentangled control by driving video or audio, and flexible face editing. Our framework elevates the resolution of the synthesized talking face to 1024*1024 for the first time, even though the training dataset has a lower resolution. We design a video-based motion generation module and an audio-based one, which can be plugged into the framework either individually or jointly to drive the video generation. The predicted motion is used to transform the latent features of StyleGAN for visual animation. To compensate for the transformation distortion, we propose a calibration network as well as a domain loss to refine the features. Moreover, our framework allows two types of facial editing, i.e., global editing via GAN inversion and intuitive editing based on 3D morphable models. Comprehensive experiments show superior video quality, flexible controllability, and editability over state-of-the-art methods.

</details>

### [FSGANv2: Improved Subject Agnostic Face Swapping and Reenactment](2202.12972.md)
**Yuval Nirkin, Yosi Keller, Tal Hassner** · 2022-02-25

<details>
<summary>Abstract</summary>

We present Face Swapping GAN (FSGAN) for face swapping and reenactment. Unlike previous work, we offer a subject agnostic swapping scheme that can be applied to pairs of faces without requiring training on those faces. We derive a novel iterative deep learning--based approach for face reenactment which adjusts significant pose and expression variations that can be applied to a single image or a video sequence. For video sequences, we introduce a continuous interpolation of the face views based on reenactment, Delaunay Triangulation, and barycentric coordinates. Occluded face regions are handled by a face completion network. Finally, we use a face blending network for seamless blending of the two faces while preserving the target skin color and lighting conditions. This network uses a novel Poisson blending loss combining Poisson optimization with a perceptual loss. We compare our approach to existing state-of-the-art systems and show our results to be both qualitatively and quantitatively superior. This work describes extensions of the FSGAN method, proposed in an earlier conference version of our work, as well as additional experiments and results.

</details>

### [Thinking the Fusion Strategy of Multi-reference Face Reenactment](2202.10758.md)
**Takuya Yashima, Takuya Narihira, Tamaki Kojima** · 2022-02-22

<details>
<summary>Abstract</summary>

In recent advances of deep generative models, face reenactment -manipulating and controlling human face, including their head movement-has drawn much attention for its wide range of applicability. Despite its strong expressiveness, it is inevitable that the models fail to reconstruct or accurately generate unseen side of the face of a given single reference image. Most of existing methods alleviate this problem by learning appearances of human faces from large amount of data and generate realistic texture at inference time. Rather than completely relying on what generative models learn, we show that simple extension by using multiple reference images significantly improves generation quality. We show this by 1) conducting the reconstruction task on publicly available dataset, 2) conducting facial motion transfer on our original dataset which consists of multi-person's head movement video sequences, and 3) using a newly proposed evaluation metric to validate that our method achieves better quantitative results.

</details>

### [The impact of removing head movements on audio-visual speech enhancement](2202.00538.md)
**Zhiqi Kang, Mostafa Sadeghi, Radu Horaud, Xavier Alameda-Pineda et al.** · 2022-02-01

<details>
<summary>Abstract</summary>

This paper investigates the impact of head movements on audio-visual speech enhancement (AVSE). Although being a common conversational feature, head movements have been ignored by past and recent studies: they challenge today's learning-based methods as they often degrade the performance of models that are trained on clean, frontal, and steady face images. To alleviate this problem, we propose to use robust face frontalization (RFF) in combination with an AVSE method based on a variational auto-encoder (VAE) model. We briefly describe the basic ingredients of the proposed pipeline and we perform experiments with a recently released audio-visual dataset. In the light of these experiments, and based on three standard metrics, namely STOI, PESQ and SI-SDR, we conclude that RFF improves the performance of AVSE by a considerable margin.

</details>

### [Finding Directions in GAN's Latent Space for Neural Face Reenactment](2202.00046.md)
**Stella Bounareli, Vasileios Argyriou, Georgios Tzimiropoulos** · 2022-01-31

<details>
<summary>Abstract</summary>

This paper is on face/head reenactment where the goal is to transfer the facial pose (3D head orientation and expression) of a target face to a source face. Previous methods focus on learning embedding networks for identity and pose disentanglement which proves to be a rather hard task, degrading the quality of the generated images. We take a different approach, bypassing the training of such networks, by using (fine-tuned) pre-trained GANs which have been shown capable of producing high-quality facial images. Because GANs are characterized by weak controllability, the core of our approach is a method to discover which directions in latent GAN space are responsible for controlling facial pose and expression variations. We present a simple pipeline to learn such directions with the aid of a 3D shape model which, by construction, already captures disentangled directions for facial pose, identity and expression. Moreover, we show that by embedding real images in the GAN latent space, our method can be successfully used for the reenactment of real-world faces. Our method features several favorable properties including using a single source image (one-shot) and enabling cross-person reenactment. Our qualitative and quantitative results show that our approach often produces reenacted faces of significantly higher quality than those produced by state-of-the-art methods for the standard benchmarks of VoxCeleb1 & 2. Source code is available at: https://github.com/StelaBou/stylegan_directions_face_reenactment

</details>

### [Stitch it in Time: GAN-Based Facial Editing of Real Videos](2201.08361.md)
**Rotem Tzaban, Ron Mokady, Rinon Gal, Amit H. Bermano et al.** · 2022-01-20

<details>
<summary>Abstract</summary>

The ability of Generative Adversarial Networks to encode rich semantics within their latent space has been widely adopted for facial image editing. However, replicating their success with videos has proven challenging. Sets of high-quality facial videos are lacking, and working with videos introduces a fundamental barrier to overcome - temporal coherency. We propose that this barrier is largely artificial. The source video is already temporally coherent, and deviations from this state arise in part due to careless treatment of individual components in the editing pipeline. We leverage the natural alignment of StyleGAN and the tendency of neural networks to learn low frequency functions, and demonstrate that they provide a strongly consistent prior. We draw on these insights and propose a framework for semantic editing of faces in videos, demonstrating significant improvements over the current state-of-the-art. Our method produces meaningful face manipulations, maintains a higher degree of temporal consistency, and can be applied to challenging, high quality, talking head videos which current methods struggle with.

</details>

### [Leveraging Real Talking Faces via Self-Supervision for Robust Forgery Detection](2201.07131.md)
**Alexandros Haliassos, Rodrigo Mira, Stavros Petridis, Maja Pantic** · 2022-01-18

<details>
<summary>Abstract</summary>

One of the most pressing challenges for the detection of face-manipulated videos is generalising to forgery methods not seen during training while remaining effective under common corruptions such as compression. In this paper, we examine whether we can tackle this issue by harnessing videos of real talking faces, which contain rich information on natural facial appearance and behaviour and are readily available in large quantities online. Our method, termed RealForensics, consists of two stages. First, we exploit the natural correspondence between the visual and auditory modalities in real videos to learn, in a self-supervised cross-modal manner, temporally dense video representations that capture factors such as facial movements, expression, and identity. Second, we use these learned representations as targets to be predicted by our forgery detector along with the usual binary forgery classification task; this encourages it to base its real/fake decision on said factors. We show that our method achieves state-of-the-art performance on cross-manipulation generalisation and robustness experiments, and examine the factors that contribute to its performance. Our results suggest that leveraging natural and unlabelled videos is a promising direction for the development of more robust face forgery detectors.

</details>

### [Audio-Driven Talking Face Video Generation with Dynamic Convolution Kernels](2201.05986.md)
**Zipeng Ye, Mengfei Xia, Ran Yi, Juyong Zhang et al.** · 2022-01-16

<details>
<summary>Abstract</summary>

In this paper, we present a dynamic convolution kernel (DCK) strategy for convolutional neural networks. Using a fully convolutional network with the proposed DCKs, high-quality talking-face video can be generated from multi-modal sources (i.e., unmatched audio and video) in real time, and our trained model is robust to different identities, head postures, and input audios. Our proposed DCKs are specially designed for audio-driven talking face video generation, leading to a simple yet effective end-to-end system. We also provide a theoretical analysis to interpret why DCKs work. Experimental results show that our method can generate high-quality talking-face video with background at 60 fps. Comparison and evaluation between our method and the state-of-the-art methods demonstrate the superiority of our method.

</details>

### [DFA-NeRF: Personalized Talking Head Generation via Disentangled Face Attributes Neural Rendering](2201.00791.md)
**Shunyu Yao, RuiZhe Zhong, Yichao Yan, Guangtao Zhai et al.** · 2022-01-03

<details>
<summary>Abstract</summary>

While recent advances in deep neural networks have made it possible to render high-quality images, generating photo-realistic and personalized talking head remains challenging. With given audio, the key to tackling this task is synchronizing lip movement and simultaneously generating personalized attributes like head movement and eye blink. In this work, we observe that the input audio is highly correlated to lip motion while less correlated to other personalized attributes (e.g., head movements). Inspired by this, we propose a novel framework based on neural radiance field to pursue high-fidelity and personalized talking head generation. Specifically, neural radiance field takes lip movements features and personalized attributes as two disentangled conditions, where lip movements are directly predicted from the audio inputs to achieve lip-synchronized generation. In the meanwhile, personalized attributes are sampled from a probabilistic model, where we design a Transformer-based variational autoencoder sampled from Gaussian Process to learn plausible and natural-looking head pose and eye blink. Experiments on several benchmarks demonstrate that our method achieves significantly better results than state-of-the-art methods.

</details>

### [Towards audio-visual deep learning methods for singing voice separation and lip synchronization](s2:0a429a0cd79b2ce508f30550aba98dd8fb2289fa.md)
**V. S. Kadandale** · 2022-01-01

