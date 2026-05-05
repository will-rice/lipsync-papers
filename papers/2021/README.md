# 2021

28 papers in this year.

### [Initiative Defense against Facial Manipulation](2112.10098.md)
**Qidong Huang, Jie Zhang, Wenbo Zhou, WeimingZhang et al.** · 2021-12-19

<details>
<summary>Abstract</summary>

Benefiting from the development of generative adversarial networks (GAN), facial manipulation has achieved significant progress in both academia and industry recently. It inspires an increasing number of entertainment applications but also incurs severe threats to individual privacy and even political security meanwhile. To mitigate such risks, many countermeasures have been proposed. However, the great majority methods are designed in a passive manner, which is to detect whether the facial images or videos are tampered after their wide propagation. These detection-based methods have a fatal limitation, that is, they only work for ex-post forensics but can not prevent the engendering of malicious behavior. To address the limitation, in this paper, we propose a novel framework of initiative defense to degrade the performance of facial manipulation models controlled by malicious users. The basic idea is to actively inject imperceptible venom into target facial data before manipulation. To this end, we first imitate the target manipulation model with a surrogate model, and then devise a poison perturbation generator to obtain the desired venom. An alternating training strategy are further leveraged to train both the surrogate model and the perturbation generator. Two typical facial manipulation tasks: face attribute editing and face reenactment, are considered in our initiative defense framework. Extensive experiments demonstrate the effectiveness and robustness of our framework in different settings. Finally, we hope this work can shed some light on initiative countermeasures against more adversarial scenarios.

</details>

### [Towards Robust Real-time Audio-Visual Speech Enhancement](2112.09060.md)
**Mandar Gogate, Kia Dashtipour, Amir Hussain** · 2021-12-16

<details>
<summary>Abstract</summary>

The human brain contextually exploits heterogeneous sensory information to efficiently perform cognitive tasks including vision and hearing. For example, during the cocktail party situation, the human auditory cortex contextually integrates audio-visual (AV) cues in order to better perceive speech. Recent studies have shown that AV speech enhancement (SE) models can significantly improve speech quality and intelligibility in very low signal to noise ratio (SNR) environments as compared to audio-only SE models. However, despite significant research in the area of AV SE, development of real-time processing models with low latency remains a formidable technical challenge. In this paper, we present a novel framework for low latency speaker-independent AV SE that can generalise on a range of visual and acoustic noises. In particular, a generative adversarial networks (GAN) is proposed to address the practical issue of visual imperfections in AV SE. In addition, we propose a deep neural network based real-time AV SE model that takes into account the cleaned visual speech output from GAN to deliver more robust SE. The proposed framework is evaluated on synthetic and real noisy AV corpora using objective speech quality and intelligibility metrics and subjective listing tests. Comparative simulation results show that our real time AV SE framework outperforms state-of-the-art SE approaches, including recent DNN based SE models.

</details>

### [One-shot Talking Face Generation from Single-speaker Audio-Visual Correlation Learning](2112.02749.md)
**Suzhen Wang, Lincheng Li, Yu Ding, Xin Yu** · 2021-12-06

<details>
<summary>Abstract</summary>

Audio-driven one-shot talking face generation methods are usually trained on video resources of various persons. However, their created videos often suffer unnatural mouth shapes and asynchronous lips because those methods struggle to learn a consistent speech style from different speakers. We observe that it would be much easier to learn a consistent speech style from a specific speaker, which leads to authentic mouth movements. Hence, we propose a novel one-shot talking face generation framework by exploring consistent correlations between audio and visual motions from a specific speaker and then transferring audio-driven motion fields to a reference image. Specifically, we develop an Audio-Visual Correlation Transformer (AVCT) that aims to infer talking motions represented by keypoint based dense motion fields from an input audio. In particular, considering audio may come from different identities in deployment, we incorporate phonemes to represent audio signals. In this manner, our AVCT can inherently generalize to audio spoken by other identities. Moreover, as face keypoints are used to represent speakers, AVCT is agnostic against appearances of the training speaker, and thus allows us to manipulate face images of different identities readily. Considering different face shapes lead to different motions, a motion field transfer module is exploited to reduce the audio-driven dense motion field gap between the training identity and the one-shot reference. Once we obtained the dense motion field of the reference image, we employ an image renderer to generate its talking face videos from an audio clip. Thanks to our learned consistent speaking style, our method generates authentic mouth shapes and vivid movements. Extensive experiments demonstrate that our synthesized videos outperform the state-of-the-art in terms of visual quality and lip-sync.

</details>

### [Towards Intelligibility-Oriented Audio-Visual Speech Enhancement](2111.09642.md)
**Tassadaq Hussain, Mandar Gogate, Kia Dashtipour, Amir Hussain** · 2021-11-18

<details>
<summary>Abstract</summary>

Existing deep learning (DL) based speech enhancement approaches are generally optimised to minimise the distance between clean and enhanced speech features. These often result in improved speech quality however they suffer from a lack of generalisation and may not deliver the required speech intelligibility in real noisy situations. In an attempt to address these challenges, researchers have explored intelligibility-oriented (I-O) loss functions and integration of audio-visual (AV) information for more robust speech enhancement (SE). In this paper, we introduce DL based I-O SE algorithms exploiting AV information, which is a novel and previously unexplored research direction. Specifically, we present a fully convolutional AV SE model that uses a modified short-time objective intelligibility (STOI) metric as a training cost function. To the best of our knowledge, this is the first work that exploits the integration of AV modalities with an I-O based loss function for SE. Comparative experimental results demonstrate that our proposed I-O AV SE framework outperforms audio-only (AO) and AV models trained with conventional distance-based loss functions, in terms of standard objective evaluation measures when dealing with unseen speakers and noises.

</details>

### [Talking Head Generation with Audio and Speech Related Facial Action Units](2110.09951.md)
**Sen Chen, Zhilei Liu, Jiaxing Liu, Zhengxiang Yan et al.** · 2021-10-19

<details>
<summary>Abstract</summary>

The task of talking head generation is to synthesize a lip synchronized talking head video by inputting an arbitrary face image and audio clips. Most existing methods ignore the local driving information of the mouth muscles. In this paper, we propose a novel recurrent generative network that uses both audio and speech-related facial action units (AUs) as the driving information. AU information related to the mouth can guide the movement of the mouth more accurately. Since speech is highly correlated with speech-related AUs, we propose an Audio-to-AU module in our system to predict the speech-related AU information from speech. In addition, we use AU classifier to ensure that the generated images contain correct AU information. Frame discriminator is also constructed for adversarial training to improve the realism of the generated face. We verify the effectiveness of our model on the GRID dataset and TCD-TIMIT dataset. We also conduct an ablation study to verify the contribution of each component in our model. Quantitative and qualitative experiments demonstrate that our method outperforms existing methods in both image quality and lip-sync accuracy.

</details>

### [FACIAL: Synthesizing Dynamic Talking Face with Implicit Attribute Learning](2108.07938.md)
**Chenxu Zhang, Yifan Zhao, Yifei Huang, Ming Zeng et al.** · 2021-08-18

<details>
<summary>Abstract</summary>

In this paper, we propose a talking face generation method that takes an audio signal as input and a short target video clip as reference, and synthesizes a photo-realistic video of the target face with natural lip motions, head poses, and eye blinks that are in-sync with the input audio signal. We note that the synthetic face attributes include not only explicit ones such as lip motions that have high correlations with speech, but also implicit ones such as head poses and eye blinks that have only weak correlation with the input audio. To model such complicated relationships among different face attributes with input audio, we propose a FACe Implicit Attribute Learning Generative Adversarial Network (FACIAL-GAN), which integrates the phonetics-aware, context-aware, and identity-aware information to synthesize the 3D face animation with realistic motions of lips, head poses, and eye blinks. Then, our Rendering-to-Video network takes the rendered face images and the attention map of eye blinks as input to generate the photo-realistic output video frames. Experimental results and user studies show our method can generate realistic talking face videos with not only synchronized lip motions, but also natural head movements and eye blinks, with better qualities than the results of state-of-the-art methods.

</details>

### [UniFaceGAN: A Unified Framework for Temporally Consistent Facial Video Editing](2108.05650.md)
**Meng Cao, Haozhi Huang, Hao Wang, Xuan Wang et al.** · 2021-08-12

<details>
<summary>Abstract</summary>

Recent research has witnessed advances in facial image editing tasks including face swapping and face reenactment. However, these methods are confined to dealing with one specific task at a time. In addition, for video facial editing, previous methods either simply apply transformations frame by frame or utilize multiple frames in a concatenated or iterative fashion, which leads to noticeable visual flickers. In this paper, we propose a unified temporally consistent facial video editing framework termed UniFaceGAN. Based on a 3D reconstruction model and a simple yet efficient dynamic training sample selection mechanism, our framework is designed to handle face swapping and face reenactment simultaneously. To enforce the temporal consistency, a novel 3D temporal loss constraint is introduced based on the barycentric coordinate interpolation. Besides, we propose a region-aware conditional normalization layer to replace the traditional AdaIN or SPADE to synthesize more context-harmonious results. Compared with the state-of-the-art facial image editing methods, our framework generates video portraits that are more photo-realistic and temporally smooth.

</details>

### [FakeAVCeleb: A Novel Audio-Video Multimodal Deepfake Dataset](2108.05080.md)
**Hasam Khalid, Shahroz Tariq, Minha Kim, Simon S. Woo** · 2021-08-11

<details>
<summary>Abstract</summary>

While the significant advancements have made in the generation of deepfakes using deep learning technologies, its misuse is a well-known issue now. Deepfakes can cause severe security and privacy issues as they can be used to impersonate a person's identity in a video by replacing his/her face with another person's face. Recently, a new problem of generating synthesized human voice of a person is emerging, where AI-based deep learning models can synthesize any person's voice requiring just a few seconds of audio. With the emerging threat of impersonation attacks using deepfake audios and videos, a new generation of deepfake detectors is needed to focus on both video and audio collectively. To develop a competent deepfake detector, a large amount of high-quality data is typically required to capture real-world (or practical) scenarios. Existing deepfake datasets either contain deepfake videos or audios, which are racially biased as well. As a result, it is critical to develop a high-quality video and audio deepfake dataset that can be used to detect both audio and video deepfakes simultaneously. To fill this gap, we propose a novel Audio-Video Deepfake dataset, FakeAVCeleb, which contains not only deepfake videos but also respective synthesized lip-synced fake audios. We generate this dataset using the most popular deepfake generation methods. We selected real YouTube videos of celebrities with four ethnic backgrounds to develop a more realistic multimodal dataset that addresses racial bias, and further help develop multimodal deepfake detectors. We performed several experiments using state-of-the-art detection methods to evaluate our deepfake dataset and demonstrate the challenges and usefulness of our multimodal Audio-Video deepfake dataset.

</details>

### [Audio2Head: Audio-driven One-shot Talking-head Generation with Natural Head Motion](2107.09293.md)
**Suzhen Wang, Lincheng Li, Yu Ding, Changjie Fan et al.** · 2021-07-20

<details>
<summary>Abstract</summary>

We propose an audio-driven talking-head method to generate photo-realistic talking-head videos from a single reference image. In this work, we tackle two key challenges: (i) producing natural head motions that match speech prosody, and (ii) maintaining the appearance of a speaker in a large head motion while stabilizing the non-face regions. We first design a head pose predictor by modeling rigid 6D head movements with a motion-aware recurrent neural network (RNN). In this way, the predicted head poses act as the low-frequency holistic movements of a talking head, thus allowing our latter network to focus on detailed facial movement generation. To depict the entire image motions arising from audio, we exploit a keypoint based dense motion field representation. Then, we develop a motion field generator to produce the dense motion fields from input audio, head poses, and a reference image. As this keypoint based representation models the motions of facial regions, head, and backgrounds integrally, our method can better constrain the spatial and temporal consistency of the generated videos. Finally, an image generation network is employed to render photo-realistic talking-head videos from the estimated keypoint based motion fields and the input reference image. Extensive experiments demonstrate that our method produces videos with plausible head motions, synchronized facial expressions, and stable backgrounds and outperforms the state-of-the-art.

</details>

### [Speech2Video: Cross-Modal Distillation for Speech to Video Generation](2107.04806.md)
**Shijing Si, Jianzong Wang, Xiaoyang Qu, Ning Cheng et al.** · 2021-07-10

<details>
<summary>Abstract</summary>

This paper investigates a novel task of talking face video generation solely from speeches. The speech-to-video generation technique can spark interesting applications in entertainment, customer service, and human-computer-interaction industries. Indeed, the timbre, accent and speed in speeches could contain rich information relevant to speakers' appearance. The challenge mainly lies in disentangling the distinct visual attributes from audio signals. In this article, we propose a light-weight, cross-modal distillation method to extract disentangled emotional and identity information from unlabelled video inputs. The extracted features are then integrated by a generative adversarial network into talking face video clips. With carefully crafted discriminators, the proposed framework achieves realistic generation results. Experiments with observed individuals demonstrated that the proposed framework captures the emotional expressions solely from speeches, and produces spontaneous facial motion in the video output. Compared to the baseline method where speeches are combined with a static image of the speaker, the results of the proposed framework is almost indistinguishable. User studies also show that the proposed method outperforms the existing algorithms in terms of emotion expression in the generated videos.

</details>

### [Multi-modality Deep Restoration of Extremely Compressed Face Videos](2107.05548.md)
**Xi Zhang, Xiaolin Wu** · 2021-07-05

<details>
<summary>Abstract</summary>

Arguably the most common and salient object in daily video communications is the talking head, as encountered in social media, virtual classrooms, teleconferences, news broadcasting, talk shows, etc. When communication bandwidth is limited by network congestions or cost effectiveness, compression artifacts in talking head videos are inevitable. The resulting video quality degradation is highly visible and objectionable due to high acuity of human visual system to faces. To solve this problem, we develop a multi-modality deep convolutional neural network method for restoring face videos that are aggressively compressed. The main innovation is a new DCNN architecture that incorporates known priors of multiple modalities: the video-synchronized speech signal and semantic elements of the compression code stream, including motion vectors, code partition map and quantization parameters. These priors strongly correlate with the latent video and hence they are able to enhance the capability of deep learning to remove compression artifacts. Ample empirical evidences are presented to validate the superior performance of the proposed DCNN method on face videos over the existing state-of-the-art methods.

</details>

### [Txt2Vid: Ultra-Low Bitrate Compression of Talking-Head Videos via Text](2106.14014.md)
**Pulkit Tandon, Shubham Chandak, Pat Pataranutaporn, Yimeng Liu et al.** · 2021-06-26

<details>
<summary>Abstract</summary>

Video represents the majority of internet traffic today, driving a continual race between the generation of higher quality content, transmission of larger file sizes, and the development of network infrastructure. In addition, the recent COVID-19 pandemic fueled a surge in the use of video conferencing tools. Since videos take up considerable bandwidth (~100 Kbps to a few Mbps), improved video compression can have a substantial impact on network performance for live and pre-recorded content, providing broader access to multimedia content worldwide. We present a novel video compression pipeline, called Txt2Vid, which dramatically reduces data transmission rates by compressing webcam videos ("talking-head videos") to a text transcript. The text is transmitted and decoded into a realistic reconstruction of the original video using recent advances in deep learning based voice cloning and lip syncing models. Our generative pipeline achieves two to three orders of magnitude reduction in the bitrate as compared to the standard audio-video codecs (encoders-decoders), while maintaining equivalent Quality-of-Experience based on a subjective evaluation by users (n = 242) in an online study. The Txt2Vid framework opens up the potential for creating novel applications such as enabling audio-video communication during poor internet connectivity, or in remote terrains with limited bandwidth. The code for this work is available at https://github.com/tpulkit/txt2vid.git.

</details>

### [Selective Listening by Synchronizing Speech with Lips](2106.07150.md)
**Zexu Pan, Ruijie Tao, Chenglin Xu, Haizhou Li** · 2021-06-14

<details>
<summary>Abstract</summary>

A speaker extraction algorithm seeks to extract the speech of a target speaker from a multi-talker speech mixture when given a cue that represents the target speaker, such as a pre-enrolled speech utterance, or an accompanying video track. Visual cues are particularly useful when a pre-enrolled speech is not available. In this work, we don't rely on the target speaker's pre-enrolled speech, but rather use the target speaker's face track as the speaker cue, that is referred to as the auxiliary reference, to form an attractor towards the target speaker. We advocate that the temporal synchronization between the speech and its accompanying lip movements is a direct and dominant audio-visual cue. Therefore, we propose a self-supervised pre-training strategy, to exploit the speech-lip synchronization cue for target speaker extraction, which allows us to leverage abundant unlabeled in-domain data. We transfer the knowledge from the pre-trained model to the attractor encoder of the speaker extraction network. We show that the proposed speaker extraction network outperforms various competitive baselines in terms of signal quality, perceptual quality, and intelligibility, achieving state-of-the-art performance.

</details>

### [Learning Pose-Adaptive Lip Sync with Cascaded Temporal Convolutional Network](s2:81ff564e6318ff01b00f9480ba1456798692201c.md)
**Ruobing Zheng, Bo Song, Changjiang Ji** · 2021-06-06

<details>
<summary>Abstract</summary>

Speech-driven lip sync has become a promising technique for generating and editing talking-head videos. These studies mainly use 3D morphable models or 2D facial landmarks as the intermediate face representations. However, 2D-based methods have been stagnant recently due to their inability to handle out-of-plane rotations, even though the 2D landmarks have the advantage of fast and accurate extraction. In this paper, we design a cascaded temporal convolutional network to successively generate mouth shapes and corresponding jawlines based on audio signals and template headposes. Instead of explicitly calibrating the rotation between the predicted mouth and the template face, we employ neural networks to learn the pose-adaptive mapping implicitly. We also propose an image-to-image translation-based neural rendering method for producing high-resolution and photo-realistic videos. Experiments show our solution improves both the mapping accuracy and visual performance than baselines. This work could benefit many real-world applications like virtual anchors, telepresence, and conversational agents.

</details>

### [Text2Video: Text-driven Talking-head Video Synthesis with Personalized Phoneme-Pose Dictionary](2104.14631.md)
**Sibo Zhang, Jiahong Yuan, Miao Liao, Liangjun Zhang** · 2021-04-29

<details>
<summary>Abstract</summary>

With the advance of deep learning technology, automatic video generation from audio or text has become an emerging and promising research topic. In this paper, we present a novel approach to synthesize video from the text. The method builds a phoneme-pose dictionary and trains a generative adversarial network (GAN) to generate video from interpolated phoneme poses. Compared to audio-driven video generation algorithms, our approach has a number of advantages: 1) It only needs a fraction of the training data used by an audio-driven approach; 2) It is more flexible and not subject to vulnerability due to speaker variation; 3) It significantly reduces the preprocessing, training and inference time. We perform extensive experiments to compare the proposed method with state-of-the-art talking face generation methods on a benchmark dataset and datasets of our own. The results demonstrate the effectiveness and superiority of our approach.

</details>

### [Learned Spatial Representations for Few-shot Talking-Head Synthesis](2104.14557.md)
**Moustafa Meshry, Saksham Suri, Larry S. Davis, Abhinav Shrivastava** · 2021-04-29

<details>
<summary>Abstract</summary>

We propose a novel approach for few-shot talking-head synthesis. While recent works in neural talking heads have produced promising results, they can still produce images that do not preserve the identity of the subject in source images. We posit this is a result of the entangled representation of each subject in a single latent code that models 3D shape information, identity cues, colors, lighting and even background details. In contrast, we propose to factorize the representation of a subject into its spatial and style components. Our method generates a target frame in two steps. First, it predicts a dense spatial layout for the target image. Second, an image generator utilizes the predicted layout for spatial denormalization and synthesizes the target frame. We experimentally show that this disentangled representation leads to a significant improvement over previous methods, both quantitatively and qualitatively.

</details>

### [3D-TalkEmo: Learning to Synthesize 3D Emotional Talking Head](2104.12051.md)
**Qianyun Wang, Zhenfeng Fan, Shihong Xia** · 2021-04-25

<details>
<summary>Abstract</summary>

Impressive progress has been made in audio-driven 3D facial animation recently, but synthesizing 3D talking-head with rich emotion is still unsolved. This is due to the lack of 3D generative models and available 3D emotional dataset with synchronized audios. To address this, we introduce 3D-TalkEmo, a deep neural network that generates 3D talking head animation with various emotions. We also create a large 3D dataset with synchronized audios and videos, rich corpus, as well as various emotion states of different persons with the sophisticated 3D face reconstruction methods. In the emotion generation network, we propose a novel 3D face representation structure - geometry map by classical multi-dimensional scaling analysis. It maps the coordinates of vertices on a 3D face to a canonical image plane, while preserving the vertex-to-vertex geodesic distance metric in a least-square sense. This maintains the adjacency relationship of each vertex and holds the effective convolutional structure for the 3D facial surface. Taking a neutral 3D mesh and a speech signal as inputs, the 3D-TalkEmo is able to generate vivid facial animations. Moreover, it provides access to change the emotion state of the animated speaker. We present extensive quantitative and qualitative evaluation of our method, in addition to user studies, demonstrating the generated talking-heads of significantly higher quality compared to previous state-of-the-art methods.

</details>

### [A cappella: Audio-visual Singing Voice Separation](2104.09946.md)
**Juan F. Montesinos, Venkatesh S. Kadandale, Gloria Haro** · 2021-04-20

<details>
<summary>Abstract</summary>

The task of isolating a target singing voice in music videos has useful applications. In this work, we explore the single-channel singing voice separation problem from a multimodal perspective, by jointly learning from audio and visual modalities. To do so, we present Acappella, a dataset spanning around 46 hours of a cappella solo singing videos sourced from YouTube. We also propose an audio-visual convolutional network based on graphs which achieves state-of-the-art singing voice separation results on our dataset and compare it against its audio-only counterpart, U-Net, and a state-of-the-art audio-visual speech separation model. We evaluate the models in the following challenging setups: i) presence of overlapping voices in the audio mixtures, ii) the target voice set to lower volume levels in the mix, and iii) combination of i) and ii). The third one being the most challenging evaluation setup. We demonstrate that our model outperforms the baseline models in the singing voice separation task in the most challenging evaluation setup. The code, the pre-trained models, and the dataset are publicly available at https://ipcv.github.io/Acappella/able at https://ipcv.github.io/Acappella/

</details>

### [Single Source One Shot Reenactment using Weighted motion From Paired Feature Points](2104.03117.md)
**Soumya Tripathy, Juho Kannala, Esa Rahtu** · 2021-04-07

<details>
<summary>Abstract</summary>

Image reenactment is a task where the target object in the source image imitates the motion represented in the driving image. One of the most common reenactment tasks is face image animation. The major challenge in the current face reenactment approaches is to distinguish between facial motion and identity. For this reason, the previous models struggle to produce high-quality animations if the driving and source identities are different (cross-person reenactment). We propose a new (face) reenactment model that learns shape-independent motion features in a self-supervised setup. The motion is represented using a set of paired feature points extracted from the source and driving images simultaneously. The model is generalised to multiple reenactment tasks including faces and non-face objects using only a single source image. The extensive experiments show that the model faithfully transfers the driving motion to the source while retaining the source identity intact.

</details>

### [LI-Net: Large-Pose Identity-Preserving Face Reenactment Network](2104.02850.md)
**Jin Liu, Peng Chen, Tao Liang, Zhaoxing Li et al.** · 2021-04-07

<details>
<summary>Abstract</summary>

Face reenactment is a challenging task, as it is difficult to maintain accurate expression, pose and identity simultaneously. Most existing methods directly apply driving facial landmarks to reenact source faces and ignore the intrinsic gap between two identities, resulting in the identity mismatch issue. Besides, they neglect the entanglement of expression and pose features when encoding driving faces, leading to inaccurate expressions and visual artifacts on large-pose reenacted faces. To address these problems, we propose a Large-pose Identity-preserving face reenactment network, LI-Net. Specifically, the Landmark Transformer is adopted to adjust driving landmark images, which aims to narrow the identity gap between driving and source landmark images. Then the Face Rotation Module and the Expression Enhancing Generator decouple the transformed landmark image into pose and expression features, and reenact those attributes separately to generate identity-preserving faces with accurate expressions and poses. Both qualitative and quantitative experimental results demonstrate the superiority of our method.

</details>

### [Looking into Your Speech: Learning Cross-modal Affinity for Audio-visual Speech Separation](2104.02775.md)
**Jiyoung Lee, Soo-Whan Chung, Sunok Kim, Hong-Goo Kang et al.** · 2021-03-25

<details>
<summary>Abstract</summary>

In this paper, we address the problem of separating individual speech signals from videos using audio-visual neural processing. Most conventional approaches utilize frame-wise matching criteria to extract shared information between co-occurring audio and video. Thus, their performance heavily depends on the accuracy of audio-visual synchronization and the effectiveness of their representations. To overcome the frame discontinuity problem between two modalities due to transmission delay mismatch or jitter, we propose a cross-modal affinity network (CaffNet) that learns global correspondence as well as locally-varying affinities between audio and visual streams. Given that the global term provides stability over a temporal sequence at the utterance-level, this resolves the label permutation problem characterized by inconsistent assignments. By extending the proposed cross-modal affinity on the complex network, we further improve the separation performance in the complex spectral domain. Experimental results verify that the proposed methods outperform conventional ones on various datasets, demonstrating their advantages in real-world scenarios.

</details>

### [AD-NeRF: Audio Driven Neural Radiance Fields for Talking Head Synthesis](2103.11078.md)
**Yudong Guo, Keyu Chen, Sen Liang, Yong-Jin Liu et al.** · 2021-03-20

<details>
<summary>Abstract</summary>

Generating high-fidelity talking head video by fitting with the input audio sequence is a challenging problem that receives considerable attentions recently. In this paper, we address this problem with the aid of neural scene representation networks. Our method is completely different from existing methods that rely on intermediate representations like 2D landmarks or 3D face models to bridge the gap between audio input and video output. Specifically, the feature of input audio signal is directly fed into a conditional implicit function to generate a dynamic neural radiance field, from which a high-fidelity talking-head video corresponding to the audio signal is synthesized using volume rendering. Another advantage of our framework is that not only the head (with hair) region is synthesized as previous methods did, but also the upper body is generated via two individual neural radiance fields. Experimental results demonstrate that our novel framework can (1) produce high-fidelity and natural results, and (2) support free adjustment of audio signals, viewing directions, and background images. Code is available at https://github.com/YudongGuo/AD-NeRF.

</details>

### [One Shot Audio to Animated Video Generation](2102.09737.md)
**Neeraj Kumar, Srishti Goel, Ankur Narang, Brejesh Lall et al.** · 2021-02-19

<details>
<summary>Abstract</summary>

We consider the challenging problem of audio to animated video generation. We propose a novel method OneShotAu2AV to generate an animated video of arbitrary length using an audio clip and a single unseen image of a person as an input. The proposed method consists of two stages. In the first stage, OneShotAu2AV generates the talking-head video in the human domain given an audio and a person's image. In the second stage, the talking-head video from the human domain is converted to the animated domain. The model architecture of the first stage consists of spatially adaptive normalization based multi-level generator and multiple multilevel discriminators along with multiple adversarial and non-adversarial losses. The second stage leverages attention based normalization driven GAN architecture along with temporal predictor based recycle loss and blink loss coupled with lipsync loss, for unsupervised generation of animated video. In our approach, the input audio clip is not restricted to any specific language, which gives the method multilingual applicability. OneShotAu2AV can generate animated videos that have: (a) lip movements that are in sync with the audio, (b) natural facial expressions such as blinks and eyebrow movements, (c) head movements. Experimental evaluation demonstrates superior performance of OneShotAu2AV as compared to U-GAT-IT and RecycleGan on multiple quantitative metrics including KID(Kernel Inception Distance), Word error rate, blinks/sec

</details>

### [Switching Variational Auto-Encoders for Noise-Agnostic Audio-visual Speech Enhancement](2102.04144.md)
**Mostafa Sadeghi, Xavier Alameda-Pineda** · 2021-02-08

<details>
<summary>Abstract</summary>

Recently, audio-visual speech enhancement has been tackled in the unsupervised settings based on variational auto-encoders (VAEs), where during training only clean data is used to train a generative model for speech, which at test time is combined with a noise model, e.g. nonnegative matrix factorization (NMF), whose parameters are learned without supervision. Consequently, the proposed model is agnostic to the noise type. When visual data are clean, audio-visual VAE-based architectures usually outperform the audio-only counterpart. The opposite happens when the visual data are corrupted by clutter, e.g. the speaker not facing the camera. In this paper, we propose to find the optimal combination of these two architectures through time. More precisely, we introduce the use of a latent sequential variable with Markovian dependencies to switch between different VAE architectures through time in an unsupervised manner: leading to switching variational auto-encoder (SwVAE). We propose a variational factorization to approximate the computationally intractable posterior distribution. We also derive the corresponding variational expectation-maximization algorithm to estimate the parameters of the model and enhance the speech signal. Our experiments demonstrate the promising performance of SwVAE.

</details>

### [One-shot Face Reenactment Using Appearance Adaptive Normalization](2102.03984.md)
**Guangming Yao, Yi Yuan, Tianjia Shao, Shuang Li et al.** · 2021-02-08

<details>
<summary>Abstract</summary>

The paper proposes a novel generative adversarial network for one-shot face reenactment, which can animate a single face image to a different pose-and-expression (provided by a driving image) while keeping its original appearance. The core of our network is a novel mechanism called appearance adaptive normalization, which can effectively integrate the appearance information from the input image into our face generator by modulating the feature maps of the generator using the learned adaptive parameters. Furthermore, we specially design a local net to reenact the local facial components (i.e., eyes, nose and mouth) first, which is a much easier task for the network to learn and can in turn provide explicit anchors to guide our face generator to learn the global appearance and pose-and-expression. Extensive quantitative and qualitative experiments demonstrate the significant efficacy of our model compared with prior one-shot methods.

</details>

### [AMFFCN: Attentional Multi-layer Feature Fusion Convolution Network for Audio-visual Speech Enhancement](2101.06268.md)
**Xinmeng Xu, Jianjun Hao** · 2021-01-15

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement system is regarded to be one of promising solutions for isolating and enhancing speech of desired speaker. Conventional methods focus on predicting clean speech spectrum via a naive convolution neural network based encoder-decoder architecture, and these methods a) not adequate to use data fully and effectively, b) cannot process features selectively. The proposed model addresses these drawbacks, by a) applying a model that fuses audio and visual features layer by layer in encoding phase, and that feeds fused audio-visual features to each corresponding decoder layer, and more importantly, b) introducing soft threshold attention into the model to select the informative modality softly. This paper proposes attentional audio-visual multi-layer feature fusion model, in which soft threshold attention unit are applied on feature mapping at every layer of decoder. The proposed model demonstrates the superior performance of the network against the state-of-the-art models.

</details>

### [Multi-layer Feature Fusion Convolution Network for Audio-visual Speech Enhancement](2101.05975.md)
**Xinmeng Xu, Jianjun Hao** · 2021-01-15

<details>
<summary>Abstract</summary>

Speech enhancement can potentially benefit from the visual information from the target speaker, such as lip movement and facial expressions, because the visual aspect of speech is essentially unaffected by acoustic environment. In this paper, we address the problem of enhancing corrupted speech signal from videos by using audio-visual (AV) neural processing. Most of recent AV speech enhancement approaches separately process the acoustic and visual features and fuse them via a simple concatenation operation. Although this strategy is convenient and easy to implement, it comes with two major drawbacks: 1) evidence in speech perception suggests that in humans the AV integration occurs at a very early stage, in contrast to previous models that process the two modalities separately at early stage and combine them only at a later stage, thus making the system less robust, and 2) a simple concatenation does not allow to control how the information from the acoustic and the visual modalities is treated. To overcome these drawbacks, we propose a multi-layer feature fusion convolution network (MFFCN), which separately process acoustic and visual modalities for preserving each modality features while fusing both modalities' features layer by layer in encoding phase for enjoying the human AV speech perception. In addition, considering the balance between the two modalities, we design channel and spectral attention mechanisms to provide additional flexibility in dealing with different types of information expanding the representational ability of the convolution neural network. Experimental results show that the proposed MFFCN demonstrates the performance of the network superior to the state-of-the-art models.

</details>

### [Fast Facial Landmark Detection and Applications: A Survey](2101.10808.md)
**Kostiantyn Khabarlak, Larysa Koriashkina** · 2021-01-12

<details>
<summary>Abstract</summary>

Dense facial landmark detection is one of the key elements of face processing pipeline. It is used in virtual face reenactment, emotion recognition, driver status tracking, etc. Early approaches were suitable for facial landmark detection in controlled environments only, which is clearly insufficient. Neural networks have shown an astonishing qualitative improvement for in-the-wild face landmark detection problem, and are now being studied by many researchers in the field. Numerous bright ideas are proposed, often complimentary to each other. However, exploration of the whole volume of novel approaches is quite challenging. Therefore, we present this survey, where we summarize state-of-the-art algorithms into categories, provide a comparison of recently introduced in-the-wild datasets (e.g., 300W, AFLW, COFW, WFLW) that contain images with large pose, face occlusion, taken in unconstrained conditions. In addition to quality, applications require fast inference, and preferably on mobile devices. Hence, we include information about algorithm inference speed both on desktop and mobile hardware, which is rarely studied. Importantly, we highlight problems of algorithms, their applications, vulnerabilities, and briefly touch on established methods. We hope that the reader will find many novel ideas, will see how the algorithms are used in applications, which will enable further research.

</details>

