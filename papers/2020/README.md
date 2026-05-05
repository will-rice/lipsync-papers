# 2020

23 papers in this year.

### [Multi Modal Adaptive Normalization for Audio to Video Generation](2012.07304.md)
**Neeraj Kumar, Srishti Goel, Ankur Narang, Brejesh Lall** · 2020-12-14

<details>
<summary>Abstract</summary>

Speech-driven facial video generation has been a complex problem due to its multi-modal aspects namely audio and video domain. The audio comprises lots of underlying features such as expression, pitch, loudness, prosody(speaking style) and facial video has lots of variability in terms of head movement, eye blinks, lip synchronization and movements of various facial action units along with temporal smoothness. Synthesizing highly expressive facial videos from the audio input and static image is still a challenging task for generative adversarial networks. In this paper, we propose a multi-modal adaptive normalization(MAN) based architecture to synthesize a talking person video of arbitrary length using as input: an audio signal and a single image of a person. The architecture uses the multi-modal adaptive normalization, keypoint heatmap predictor, optical flow predictor and class activation map[58] based layers to learn movements of expressive facial components and hence generates a highly expressive talking-head video of the given person. The multi-modal adaptive normalization uses the various features of audio and video such as Mel spectrogram, pitch, energy from audio signals and predicted keypoint heatmap/optical flow and a single image to learn the respective affine parameters to generate highly expressive video. Experimental evaluation demonstrates superior performance of the proposed method as compared to Realistic Speech-Driven Facial Animation with GANs(RSDGAN) [53], Speech2Vid [10], and other approaches, on multiple quantitative metrics including: SSIM (structural similarity index), PSNR (peak signal to noise ratio), CPBD (image sharpness), WER(word error rate), blinks/sec and LMD(landmark distance). Further, qualitative evaluation and Online Turing tests demonstrate the efficacy of our approach.

</details>

### [Robust One Shot Audio to Video Generation](2012.07842.md)
**Neeraj Kumar, Srishti Goel, Ankur Narang, Mujtaba Hasan** · 2020-12-14

<details>
<summary>Abstract</summary>

Audio to Video generation is an interesting problem that has numerous applications across industry verticals including film making, multi-media, marketing, education and others. High-quality video generation with expressive facial movements is a challenging problem that involves complex learning steps for generative adversarial networks. Further, enabling one-shot learning for an unseen single image increases the complexity of the problem while simultaneously making it more applicable to practical scenarios. In the paper, we propose a novel approach OneShotA2V to synthesize a talking person video of arbitrary length using as input: an audio signal and a single unseen image of a person. OneShotA2V leverages curriculum learning to learn movements of expressive facial components and hence generates a high-quality talking-head video of the given person. Further, it feeds the features generated from the audio input directly into a generative adversarial network and it adapts to any given unseen selfie by applying fewshot learning with only a few output updation epochs. OneShotA2V leverages spatially adaptive normalization based multi-level generator and multiple multi-level discriminators based architecture. The input audio clip is not restricted to any specific language, which gives the method multilingual applicability. Experimental evaluation demonstrates superior performance of OneShotA2V as compared to Realistic Speech-Driven Facial Animation with GANs(RSDGAN) [43], Speech2Vid [8], and other approaches, on multiple quantitative metrics including: SSIM (structural similarity index), PSNR (peak signal to noise ratio) and CPBD (image sharpness). Further, qualitative evaluation and Online Turing tests demonstrate the efficacy of our approach.

</details>

### [An Empirical Study of Visual Features for DNN based Audio-Visual Speech Enhancement in Multi-talker Environments](2011.04359.md)
**Shrishti Saha Shetu, Soumitro Chakrabarty, Emanuël A. P. Habets** · 2020-11-09

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement (AVSE) methods use both audio and visual features for the task of speech enhancement and the use of visual features has been shown to be particularly effective in multi-speaker scenarios. In the majority of deep neural network (DNN) based AVSE methods, the audio and visual data are first processed separately using different sub-networks, and then the learned features are fused to utilize the information from both modalities. There have been various studies on suitable audio input features and network architectures, however, to the best of our knowledge, there is no published study that has investigated which visual features are best suited for this specific task. In this work, we perform an empirical study of the most commonly used visual features for DNN based AVSE, the pre-processing requirements for each of these features, and investigate their influence on the performance. Our study shows that despite the overall better performance of embedding-based features, their computationally intensive pre-processing make their use difficult in low resource systems. For such systems, optical flow or raw pixels-based features might be better suited.

</details>

### [FACEGAN: Facial Attribute Controllable rEenactment GAN](2011.04439.md)
**Soumya Tripathy, Juho Kannala, Esa Rahtu** · 2020-11-09

<details>
<summary>Abstract</summary>

The face reenactment is a popular facial animation method where the person's identity is taken from the source image and the facial motion from the driving image. Recent works have demonstrated high quality results by combining the facial landmark based motion representations with the generative adversarial networks. These models perform best if the source and driving images depict the same person or if the facial structures are otherwise very similar. However, if the identity differs, the driving facial structures leak to the output distorting the reenactment result. We propose a novel Facial Attribute Controllable rEenactment GAN (FACEGAN), which transfers the facial motion from the driving face via the Action Unit (AU) representation. Unlike facial landmarks, the AUs are independent of the facial structure preventing the identity leak. Moreover, AUs provide a human interpretable way to control the reenactment. FACEGAN processes background and face regions separately for optimized output quality. The extensive quantitative and qualitative comparisons show a clear improvement over the state-of-the-art in a single source reenactment task. The results are best illustrated in the reenactment video provided in the supplementary material. The source code will be made available upon publication of the paper.

</details>

### [Audio-Visual Speech Inpainting with Deep Learning](2010.04556.md)
**Giovanni Morrone, Daniel Michelsanti, Zheng-Hua Tan, Jesper Jensen** · 2020-10-09

<details>
<summary>Abstract</summary>

In this paper, we present a deep-learning-based framework for audio-visual speech inpainting, i.e., the task of restoring the missing parts of an acoustic speech signal from reliable audio context and uncorrupted visual information. Recent work focuses solely on audio-only methods and generally aims at inpainting music signals, which show highly different structure than speech. Instead, we inpaint speech signals with gaps ranging from 100 ms to 1600 ms to investigate the contribution that vision can provide for gaps of different duration. We also experiment with a multi-task learning approach where a phone recognition task is learned together with speech inpainting. Results show that the performance of audio-only speech inpainting approaches degrades rapidly when gaps get large, while the proposed audio-visual approach is able to plausibly restore missing information. In addition, we show that multi-task learning is effective, although the largest contribution to performance comes from vision.

</details>

### [Improved Lite Audio-Visual Speech Enhancement](2008.13222.md)
**Shang-Yi Chuang, Hsin-Min Wang, Yu Tsao** · 2020-08-30

<details>
<summary>Abstract</summary>

Numerous studies have investigated the effectiveness of audio-visual multimodal learning for speech enhancement (AVSE) tasks, seeking a solution that uses visual data as auxiliary and complementary input to reduce the noise of noisy speech signals. Recently, we proposed a lite audio-visual speech enhancement (LAVSE) algorithm for a car-driving scenario. Compared to conventional AVSE systems, LAVSE requires less online computation and to some extent solves the user privacy problem on facial data. In this study, we extend LAVSE to improve its ability to address three practical issues often encountered in implementing AVSE systems, namely, the additional cost of processing visual data, audio-visual asynchronization, and low-quality visual data. The proposed system is termed improved LAVSE (iLAVSE), which uses a convolutional recurrent neural network architecture as the core AVSE model. We evaluate iLAVSE on the Taiwan Mandarin speech with video dataset. Experimental results confirm that compared to conventional AVSE systems, iLAVSE can effectively overcome the aforementioned three practical issues and can improve enhancement performance. The results also confirm that iLAVSE is suitable for real-world scenarios, where high-quality audio-visual sensors may not always be available.

</details>

### [An Overview of Deep-Learning-Based Audio-Visual Speech Enhancement and Separation](2008.09586.md)
**Daniel Michelsanti, Zheng-Hua Tan, Shi-Xiong Zhang, Yong Xu et al.** · 2020-08-21

<details>
<summary>Abstract</summary>

Speech enhancement and speech separation are two related tasks, whose purpose is to extract either one or more target speech signals, respectively, from a mixture of sounds generated by several sources. Traditionally, these tasks have been tackled using signal processing and machine learning techniques applied to the available acoustic signals. Since the visual aspect of speech is essentially unaffected by the acoustic environment, visual information from the target speakers, such as lip movements and facial expressions, has also been used for speech enhancement and speech separation systems. In order to efficiently fuse acoustic and visual information, researchers have exploited the flexibility of data-driven approaches, specifically deep learning, achieving strong performance. The ceaseless proposal of a large number of techniques to extract features and fuse multimodal information has highlighted the need for an overview that comprehensively describes and discusses audio-visual speech enhancement and separation based on deep learning. In this paper, we provide a systematic survey of this research topic, focusing on the main elements that characterise the systems in the literature: acoustic features; visual features; deep learning methods; fusion techniques; training targets and objective functions. In addition, we review deep-learning-based methods for speech reconstruction from silent videos and audio-visual sound source separation for non-speech signals, since these methods can be more or less directly applied to audio-visual speech enhancement and separation. Finally, we survey commonly employed audio-visual speech datasets, given their central role in the development of data-driven approaches, and evaluation methods, because they are generally used to compare different systems and determine their performance.

</details>

### [Deep Variational Generative Models for Audio-visual Speech Separation](2008.07191.md)
**Viet-Nhat Nguyen, Mostafa Sadeghi, Elisa Ricci, Xavier Alameda-Pineda** · 2020-08-17

<details>
<summary>Abstract</summary>

In this paper, we are interested in audio-visual speech separation given a single-channel audio recording as well as visual information (lips movements) associated with each speaker. We propose an unsupervised technique based on audio-visual generative modeling of clean speech. More specifically, during training, a latent variable generative model is learned from clean speech spectrograms using a variational auto-encoder (VAE). To better utilize the visual information, the posteriors of the latent variables are inferred from mixed speech (instead of clean speech) as well as the visual data. The visual modality also serves as a prior for latent variables, through a visual network. At test time, the learned generative model (both for speaker-independent and speaker-dependent scenarios) is combined with an unsupervised non-negative matrix factorization (NMF) variance model for background noise. All the latent variables and noise parameters are then estimated by a Monte Carlo expectation-maximization algorithm. Our experiments show that the proposed unsupervised VAE-based method yields better separation performance than NMF-based approaches as well as a supervised deep learning-based technique.

</details>

### [Audiovisual Speech Synthesis using Tacotron2](2008.00620.md)
**Ahmed Hussen Abdelaziz, Anushree Prasanna Kumar, Chloe Seivwright, Gabriele Fanelli et al.** · 2020-08-03

<details>
<summary>Abstract</summary>

Audiovisual speech synthesis is the problem of synthesizing a talking face while maximizing the coherency of the acoustic and visual speech. In this paper, we propose and compare two audiovisual speech synthesis systems for 3D face models. The first system is the AVTacotron2, which is an end-to-end text-to-audiovisual speech synthesizer based on the Tacotron2 architecture. AVTacotron2 converts a sequence of phonemes representing the sentence to synthesize into a sequence of acoustic features and the corresponding controllers of a face model. The output acoustic features are used to condition a WaveRNN to reconstruct the speech waveform, and the output facial controllers are used to generate the corresponding video of the talking face. The second audiovisual speech synthesis system is modular, where acoustic speech is synthesized from text using the traditional Tacotron2. The reconstructed acoustic speech signal is then used to drive the facial controls of the face model using an independently trained audio-to-facial-animation neural network. We further condition both the end-to-end and modular approaches on emotion embeddings that encode the required prosody to generate emotional audiovisual speech. We analyze the performance of the two systems and compare them to the ground truth videos using subjective evaluation tests. The end-to-end and modular systems are able to synthesize close to human-like audiovisual speech with mean opinion scores (MOS) of 4.1 and 3.9, respectively, compared to a MOS of 4.1 for the ground truth generated from professionally recorded videos. While the end-to-end system gives a better overall quality, the modular approach is more flexible and the quality of acoustic speech and visual speech synthesis is almost independent of each other.

</details>

### [Deep Multi-modality Soft-decoding of Very Low Bit-rate Face Videos](2008.01652.md)
**Yanhui Guo, Xi Zhang, Xiaolin Wu** · 2020-08-02

<details>
<summary>Abstract</summary>

We propose a novel deep multi-modality neural network for restoring very low bit rate videos of talking heads. Such video contents are very common in social media, teleconferencing, distance education, tele-medicine, etc., and often need to be transmitted with limited bandwidth. The proposed CNN method exploits the correlations among three modalities, video, audio and emotion state of the speaker, to remove the video compression artifacts caused by spatial down sampling and quantization. The deep learning approach turns out to be ideally suited for the video restoration task, as the complex non-linear cross-modality correlations are very difficult to model analytically and explicitly. The new method is a video post processor that can significantly boost the perceptual quality of aggressively compressed talking head videos, while being fully compatible with all existing video compression standards.

</details>

### [Talking-head Generation with Rhythmic Head Motion](2007.08547.md)
**Lele Chen, Guofeng Cui, Celong Liu, Zhong Li et al.** · 2020-07-16

<details>
<summary>Abstract</summary>

When people deliver a speech, they naturally move heads, and this rhythmic head motion conveys prosodic information. However, generating a lip-synced video while moving head naturally is challenging. While remarkably successful, existing works either generate still talkingface videos or rely on landmark/video frames as sparse/dense mapping guidance to generate head movements, which leads to unrealistic or uncontrollable video synthesis. To overcome the limitations, we propose a 3D-aware generative network along with a hybrid embedding module and a non-linear composition module. Through modeling the head motion and facial expressions1 explicitly, manipulating 3D animation carefully, and embedding reference images dynamically, our approach achieves controllable, photo-realistic, and temporally coherent talking-head videos with natural head movements. Thoughtful experiments on several standard benchmarks demonstrate that our method achieves significantly better results than the state-of-the-art methods in both quantitative and qualitative comparisons. The code is available on https://github.com/ lelechen63/Talking-head-Generation-with-Rhythmic-Head-Motion.

</details>

### [Learning Speech Representations from Raw Audio by Joint Audiovisual Self-Supervision](2007.04134.md)
**Abhinav Shukla, Stavros Petridis, Maja Pantic** · 2020-07-08

<details>
<summary>Abstract</summary>

The intuitive interaction between the audio and visual modalities is valuable for cross-modal self-supervised learning. This concept has been demonstrated for generic audiovisual tasks like video action recognition and acoustic scene classification. However, self-supervision remains under-explored for audiovisual speech. We propose a method to learn self-supervised speech representations from the raw audio waveform. We train a raw audio encoder by combining audio-only self-supervision (by predicting informative audio attributes) with visual self-supervision (by generating talking faces from audio). The visual pretext task drives the audio representations to capture information related to lip movements. This enriches the audio encoder with visual information and the encoder can be used for evaluation without the visual modality. Our method attains competitive performance with respect to existing self-supervised audio features on established isolated word classification benchmarks, and significantly outperforms other methods at learning from fewer labels. Notably, our method also outperforms fully supervised training, thus providing a strong initialization for speech related tasks. Our results demonstrate the potential of multimodal self-supervision in audiovisual speech for learning good audio representations.

</details>

### [Modality Dropout for Improved Performance-driven Talking Faces](2005.13616.md)
**Ahmed Hussen Abdelaziz, Barry-John Theobald, Paul Dixon, Reinhard Knothe et al.** · 2020-05-27

<details>
<summary>Abstract</summary>

We describe our novel deep learning approach for driving animated faces using both acoustic and visual information. In particular, speech-related facial movements are generated using audiovisual information, and non-speech facial movements are generated using only visual information. To ensure that our model exploits both modalities during training, batches are generated that contain audio-only, video-only, and audiovisual input features. The probability of dropping a modality allows control over the degree to which the model exploits audio and visual information during training. Our trained model runs in real-time on resource limited hardware (e.g.\ a smart phone), it is user agnostic, and it is not dependent on a potentially error-prone transcription of the speech. We use subjective testing to demonstrate: 1) the improvement of audiovisual-driven animation over the equivalent video-only approach, and 2) the improvement in the animation of speech-related facial movements after introducing modality dropout. Before introducing dropout, viewers prefer audiovisual-driven animation in 51% of the test sequences compared with only 18% for video-driven. After introducing dropout viewer preference for audiovisual-driven animation increases to 74%, but decreases to 8% for video-only.

</details>

### [Identity-Preserving Realistic Talking Face Generation](2005.12318.md)
**Sanjana Sinha, Sandika Biswas, Brojeshwar Bhowmick** · 2020-05-25

<details>
<summary>Abstract</summary>

Speech-driven facial animation is useful for a variety of applications such as telepresence, chatbots, etc. The necessary attributes of having a realistic face animation are 1) audio-visual synchronization (2) identity preservation of the target individual (3) plausible mouth movements (4) presence of natural eye blinks. The existing methods mostly address the audio-visual lip synchronization, and few recent works have addressed the synthesis of natural eye blinks for overall video realism. In this paper, we propose a method for identity-preserving realistic facial animation from speech. We first generate person-independent facial landmarks from audio using DeepSpeech features for invariance to different voices, accents, etc. To add realism, we impose eye blinks on facial landmarks using unsupervised learning and retargets the person-independent landmarks to person-specific landmarks to preserve the identity-related facial structure which helps in the generation of plausible mouth shapes of the target identity. Finally, we use LSGAN to generate the facial texture from person-specific facial landmarks, using an attention mechanism that helps to preserve identity-related texture. An extensive comparison of our proposed method with the current state-of-the-art methods demonstrates a significant improvement in terms of lip synchronization accuracy, image reconstruction quality, sharpness, and identity-preservation. A user study also reveals improved realism of our animation results over the state-of-the-art methods. To the best of our knowledge, this is the first work in speech-driven 2D facial animation that simultaneously addresses all the above-mentioned attributes of a realistic speech-driven face animation.

</details>

### [End-to-End Lip Synchronisation Based on Pattern Classification](2005.08606.md)
**You Jin Kim, Hee Soo Heo, Soo-Whan Chung, Bong-Jin Lee** · 2020-05-18

<details>
<summary>Abstract</summary>

The goal of this work is to synchronise audio and video of a talking face using deep neural network models. Existing works have trained networks on proxy tasks such as cross-modal similarity learning, and then computed similarities between audio and video frames using a sliding window approach. While these methods demonstrate satisfactory performance, the networks are not trained directly on the task. To this end, we propose an end-to-end trained network that can directly predict the offset between an audio stream and the corresponding video stream. The similarity matrix between the two modalities is first computed from the features, then the inference of the offset can be considered to be a pattern recognition problem where the matrix is considered equivalent to an image. The feature extractor and the classifier are trained jointly. We demonstrate that the proposed approach outperforms the previous work by a large margin on LRS2 and LRS3 datasets.

</details>

### [FaR-GAN for One-Shot Face Reenactment](2005.06402.md)
**Hanxiang Hao, Sriram Baireddy, Amy R. Reibman, Edward J. Delp** · 2020-05-13

<details>
<summary>Abstract</summary>

Animating a static face image with target facial expressions and movements is important in the area of image editing and movie production. This face reenactment process is challenging due to the complex geometry and movement of human faces. Previous work usually requires a large set of images from the same person to model the appearance. In this paper, we present a one-shot face reenactment model, FaR-GAN, that takes only one face image of any given source identity and a target expression as input, and then produces a face image of the same source identity but with the target expression. The proposed method makes no assumptions about the source identity, facial expression, head pose, or even image background. We evaluate our method on the VoxCeleb1 dataset and show that our method is able to generate a higher quality face image than the compared methods.

</details>

### [What comprises a good talking-head video generation?: A Survey and Benchmark](2005.03201.md)
**Lele Chen, Guofeng Cui, Ziyi Kou, Haitian Zheng et al.** · 2020-05-07

<details>
<summary>Abstract</summary>

Over the years, performance evaluation has become essential in computer vision, enabling tangible progress in many sub-fields. While talking-head video generation has become an emerging research topic, existing evaluations on this topic present many limitations. For example, most approaches use human subjects (e.g., via Amazon MTurk) to evaluate their research claims directly. This subjective evaluation is cumbersome, unreproducible, and may impend the evolution of new research. In this work, we present a carefully-designed benchmark for evaluating talking-head video generation with standardized dataset pre-processing strategies. As for evaluation, we either propose new metrics or select the most appropriate ones to evaluate results in what we consider as desired properties for a good talking-head video, namely, identity preserving, lip synchronization, high video quality, and natural-spontaneous motion. By conducting a thoughtful analysis across several state-of-the-art talking-head generation approaches, we aim to uncover the merits and drawbacks of current methods and point out promising directions for future work. All the evaluation code is available at: https://github.com/lelechen63/talking-head-generation-survey.

</details>

### [APB2Face: Audio-guided face reenactment with auxiliary pose and blink signals](2004.14569.md)
**Jiangning Zhang, Liang Liu, Zhucun Xue, Yong Liu** · 2020-04-30

<details>
<summary>Abstract</summary>

Audio-guided face reenactment aims at generating photorealistic faces using audio information while maintaining the same facial movement as when speaking to a real person. However, existing methods can not generate vivid face images or only reenact low-resolution faces, which limits the application value. To solve those problems, we propose a novel deep neural network named APB2Face, which consists of GeometryPredictor and FaceReenactor modules. GeometryPredictor uses extra head pose and blink state signals as well as audio to predict the latent landmark geometry information, while FaceReenactor inputs the face landmark image to reenact the photorealistic face. A new dataset AnnVI collected from YouTube is presented to support the approach, and experimental results indicate the superiority of our method than state-of-the-arts, whether in authenticity or controllability.

</details>

### [ActGAN: Flexible and Efficient One-shot Face Reenactment](2003.13840.md)
**Ivan Kosarevych, Marian Petruk, Markian Kostiv, Orest Kupyn et al.** · 2020-03-30

<details>
<summary>Abstract</summary>

This paper introduces ActGAN - a novel end-to-end generative adversarial network (GAN) for one-shot face reenactment. Given two images, the goal is to transfer the facial expression of the source actor onto a target person in a photo-realistic fashion. While existing methods require target identity to be predefined, we address this problem by introducing a "many-to-many" approach, which allows arbitrary persons both for source and target without additional retraining. To this end, we employ the Feature Pyramid Network (FPN) as a core generator building block - the first application of FPN in face reenactment, producing finer results. We also introduce a solution to preserve a person's identity between synthesized and target person by adopting the state-of-the-art approach in deep face recognition domain. The architecture readily supports reenactment in different scenarios: "many-to-many", "one-to-one", "one-to-another" in terms of expression accuracy, identity preservation, and overall image quality. We demonstrate that ActGAN achieves competitive performance against recent works concerning visual quality.

</details>

### [Realistic Face Reenactment via Self-Supervised Disentangling of Identity and Pose](2003.12957.md)
**Xianfang Zeng, Yusu Pan, Mengmeng Wang, Jiangning Zhang et al.** · 2020-03-29

<details>
<summary>Abstract</summary>

Recent works have shown how realistic talking face images can be obtained under the supervision of geometry guidance, e.g., facial landmark or boundary. To alleviate the demand for manual annotations, in this paper, we propose a novel self-supervised hybrid model (DAE-GAN) that learns how to reenact face naturally given large amounts of unlabeled videos. Our approach combines two deforming autoencoders with the latest advances in the conditional generation. On the one hand, we adopt the deforming autoencoder to disentangle identity and pose representations. A strong prior in talking face videos is that each frame can be encoded as two parts: one for video-specific identity and the other for various poses. Inspired by that, we utilize a multi-frame deforming autoencoder to learn a pose-invariant embedded face for each video. Meanwhile, a multi-scale deforming autoencoder is proposed to extract pose-related information for each frame. On the other hand, the conditional generator allows for enhancing fine details and overall reality. It leverages the disentangled features to generate photo-realistic and pose-alike face images. We evaluate our model on VoxCeleb1 and RaFD dataset. Experiment results demonstrate the superior quality of reenacted images and the flexibility of transferring facial movements between identities.

</details>

### [Audio-driven Talking Face Video Generation with Learning-based Personalized Head Pose](2002.10137.md)
**Ran Yi, Zipeng Ye, Juyong Zhang, Hujun Bao et al.** · 2020-02-24

<details>
<summary>Abstract</summary>

Real-world talking faces often accompany with natural head movement. However, most existing talking face video generation methods only consider facial animation with fixed head pose. In this paper, we address this problem by proposing a deep neural network model that takes an audio signal A of a source person and a very short video V of a target person as input, and outputs a synthesized high-quality talking face video with personalized head pose (making use of the visual information in V), expression and lip synchronization (by considering both A and V). The most challenging issue in our work is that natural poses often cause in-plane and out-of-plane head rotations, which makes synthesized talking face video far from realistic. To address this challenge, we reconstruct 3D face animation and re-render it into synthesized frames. To fine tune these frames into realistic ones with smooth background transition, we propose a novel memory-augmented GAN module. By first training a general mapping based on a publicly available dataset and fine-tuning the mapping using the input short video of target person, we develop an effective strategy that only requires a small number of frames (about 300 frames) to learn personalized talking behavior including head pose. Extensive experiments and two user studies show that our method can generate high-quality (i.e., personalized head movements, expressions and good lip synchronization) talking face videos, which are naturally looking with more distinguishing head movement effects than the state-of-the-art methods.

</details>

### [A Neural Lip-Sync Framework for Synthesizing Photorealistic Virtual News Anchors](2002.08700.md)
**Ruobing Zheng, Zhou Zhu, Bo Song, Changjiang Ji** · 2020-02-20

<details>
<summary>Abstract</summary>

Lip sync has emerged as a promising technique for generating mouth movements from audio signals. However, synthesizing a high-resolution and photorealistic virtual news anchor is still challenging. Lack of natural appearance, visual consistency, and processing efficiency are the main problems with existing methods. This paper presents a novel lip-sync framework specially designed for producing high-fidelity virtual news anchors. A pair of Temporal Convolutional Networks are used to learn the cross-modal sequential mapping from audio signals to mouth movements, followed by a neural rendering network that translates the synthetic facial map into a high-resolution and photorealistic appearance. This fully trainable framework provides end-to-end processing that outperforms traditional graphics-based methods in many low-delay applications. Experiments also show the framework has advantages over modern neural-based methods in both visual appearance and efficiency.

</details>

### [Disentangled Speech Embeddings using Cross-modal Self-supervision](2002.08742.md)
**Arsha Nagrani, Joon Son Chung, Samuel Albanie, Andrew Zisserman** · 2020-02-20

<details>
<summary>Abstract</summary>

The objective of this paper is to learn representations of speaker identity without access to manually annotated data. To do so, we develop a self-supervised learning objective that exploits the natural cross-modal synchrony between faces and audio in video. The key idea behind our approach is to tease apart--without annotation--the representations of linguistic content and speaker identity. We construct a two-stream architecture which: (1) shares low-level features common to both representations; and (2) provides a natural mechanism for explicitly disentangling these factors, offering the potential for greater generalisation to novel combinations of content and identity and ultimately producing speaker identity representations that are more robust. We train our method on a large-scale audio-visual dataset of talking heads `in the wild', and demonstrate its efficacy by evaluating the learned speaker representations for standard speaker recognition performance.

</details>

