# lipsync-papers

A curated, automatically-updated collection of papers on **lip sync**, talking-head synthesis, audio-driven face animation, and related topics — starting from [Wav2Lip](https://arxiv.org/abs/2008.10010) (2020) and growing every week.

## How it works

* Papers are sourced from [arXiv](https://arxiv.org/) via its public API.
* A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs every **Monday at 06:00 UTC** to pull papers submitted in the previous week.
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

The following keyword queries are used against arXiv title and abstract fields:

`lip sync` · `lip synchronization` · `wav2lip` · `talking head` · `talking face` · `audio-driven face` · `speech-driven face` · `audio visual speech` · `face reenactment` · `neural dubbing`

## Papers

<!-- PAPERS_TABLE_START -->
### 2026

| Date | Title | Authors |
|------|-------|---------|
| 2026-03-09 | [Talking Together: Synthesizing Co-Located 3D Conversations from Audio](https://arxiv.org/abs/2603.08674) | Mengyi Shan, Shouchieh Chang, Ziqian Bai, Shichen Liu et al. |
| 2026-03-08 | [EmbedTalk: Triplane-Free Talking Head Synthesis using Embedding-Driven Gaussian Deformation](https://arxiv.org/abs/2603.07604) | Arpita Saggar, Jonathan C. Darling, Duygu Sarikaya, David C. Hogg |
| 2026-03-06 | [TempoSyncDiff: Distilled Temporally-Consistent Diffusion for Low-Latency Audio-Driven Talking Head Generation](https://arxiv.org/abs/2603.06057) | Soumya Mazumdar, Vineet Kumar Rakesh |
| 2026-03-06 | [Text-Driven Emotionally Continuous Talking Face Generation](https://arxiv.org/abs/2603.06071) | Hao Yang, Yanyan Zhao, Tian Zheng, Hongbo Zhang et al. |
| 2026-03-04 | [UniSync: Towards Generalizable and High-Fidelity Lip Synchronization for Challenging Scenarios](https://arxiv.org/abs/2603.03882) | Ruidi Fan, Yang Zhou, Siyuan Wang, Tian Yu et al. |
| 2026-03-02 | [UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](https://arxiv.org/abs/2603.01418) | Hebeizi Li, Zihao Liang, Benyuan Sun, Zihao Yin et al. |
| 2026-02-25 | [FlowPortrait: Reinforcement Learning for Audio-Driven Portrait Video Generation](https://arxiv.org/abs/2603.00159) | Weiting Tan, Andy T. Liu, Ming Tu, Xinghua Qu et al. |
| 2026-02-20 | [Narrating For You: Prompt-guided Audio-visual Narrating Face Generation Employing Multi-entangled Latent Space](https://arxiv.org/abs/2602.18618) | Aashish Chandra, Aashutosh A, Abhijit Das |
| 2026-02-14 | [EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](https://arxiv.org/abs/2602.13669) | Rang Meng, Yingjie Yin, Yuming Li, Chenguang Ma |
| 2026-02-13 | [VineetVC: Adaptive Video Conferencing Under Severe Bandwidth Constraints Using Audio-Driven Talking-Head Reconstruction](https://arxiv.org/abs/2602.12758) | Vineet Kumar Rakesh, Soumya Mazumdar, Tapas Samanta, Hemendra Kumar Pandey et al. |
| 2026-02-11 | [3DXTalker: Unifying Identity, Lip Sync, Emotion, and Spatial Dynamics in Expressive 3D Talking Avatars](https://arxiv.org/abs/2602.10516) | Zhongju Wang, Zhenhong Sun, Beier Wang, Yifu Wang et al. |
| 2026-02-10 | [Toward Fine-Grained Facial Control in 3D Talking Head Generation](https://arxiv.org/abs/2602.09736) | Shaoyang Xie, Xiaofeng Cong, Baosheng Yu, Zhipeng Gui et al. |
| 2026-02-10 | [AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534) | Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang et al. |
| 2026-02-09 | [MOVA: Towards Scalable and Synchronized Video-Audio Generation](https://arxiv.org/abs/2602.08794) | SII-OpenMOSS Team, :, Donghua Yu, Mingshu Chen et al. |
| 2026-02-09 | [VedicTHG: Symbolic Vedic Computation for Low-Resource Talking-Head Generation in Educational Avatars](https://arxiv.org/abs/2602.08775) | Vineet Kumar Rakesh, Ahana Bhattacharjee, Soumya Mazumdar, Tapas Samanta et al. |
| 2026-02-07 | [SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads](https://arxiv.org/abs/2602.07449) | Tan Yu, Qian Qiao, Le Shen, Ke Zhou et al. |
| 2026-02-05 | [From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122) | Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro et al. |
| 2026-02-04 | [A$^2$-LLM: An End-to-end Conversational Audio Avatar Large Language Model](https://arxiv.org/abs/2602.04913) | Xiaolin Hu, Hang Yuan, Xinzhu Sang, Binbin Yan et al. |
| 2026-02-03 | [Asymmetric Hierarchical Anchoring for Audio-Visual Joint Representation: Resolving Information Allocation Ambiguity for Robust Cross-Modal Generalization](https://arxiv.org/abs/2602.03570) | Bixing Wu, Yuhong Zhao, Zongli Ye, Jiachen Lian et al. |
| 2026-01-31 | [JoyAvatar: Unlocking Highly Expressive Avatars via Harmonized Text-Audio Conditioning](https://arxiv.org/abs/2602.00702) | Ruikui Wang, Jinheng Feng, Lang Tian, Huaishao Luo et al. |
| 2026-01-30 | [MIRRORTALK: Forging Personalized Avatars Via Disentangled Style and Hierarchical Motion Control](https://arxiv.org/abs/2601.22501) | Renjie Lu, Xulong Zhang, Xiaoyang Qu, Jianzong Wang, Shangfei Wang |
| 2026-01-30 | [LPIPS-AttnWav2Lip: Generic Audio-Driven lip synchronization for Talking Head Generation in the Wild](https://arxiv.org/abs/2602.00189) | Zhipeng Chen, Xinheng Wang, Lun Xie, Haijie Yuan, Hang Pan |
| 2026-01-29 | [JUST-DUB-IT: Video Dubbing via Joint Audio-Visual Diffusion](https://arxiv.org/abs/2601.22143) | Anthony Chen, Naomi Ken Korem, Tavi Halperin, Matan Ben Yosef et al. |
| 2026-01-29 | [EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers](https://arxiv.org/abs/2601.22127) | John Flynn, Wolfgang Paier, Dimitar Dinev, Sam Nhut Nguyen et al. |
| 2026-01-29 | [Lightweight High-Fidelity Low-Bitrate Talking Face Compression for 3D Video Conference](https://arxiv.org/abs/2601.21269) | Jianglong Li, Jun Xu, Bingcong Lu, Zhengxue Cheng et al. |
| 2026-01-28 | [SFQA: A Comprehensive Perceptual Quality Assessment Dataset for Singing Face Generation](https://arxiv.org/abs/2601.20385) | Zhilin Gao, Yunhao Li, Sijing Wu, Yucheng Zhu et al. |
| 2026-01-27 | [Uncertainty-Aware 3D Emotional Talking Face Synthesis with Emotion Prior Distillation](https://arxiv.org/abs/2601.19112) | Nanhan Shen, Zhilei Liu |
| 2026-01-26 | [Splat-Portrait: Generalizing Talking Heads with Gaussian Splatting](https://arxiv.org/abs/2601.18633) | Tong Shi, Melonie de Almeida, Daniela Ivanova, Nicolas Pugeault, Paul Henderson |
| 2026-01-26 | [Audio-Driven Talking Face Generation with Blink Embedding and Hash Grid Landmarks Encoding](https://arxiv.org/abs/2601.18849) | Yuhui Zhang, Hui Yu, Wei Liang, Sunjie Zhang |
| 2026-01-21 | [FunCineForge: A Unified Dataset Toolkit and Model for Zero-Shot Movie Dubbing in Diverse Cinematic Scenes](https://arxiv.org/abs/2601.14777) | Jiaxuan Liu, Yang Xiang, Han Zhao, Xiangang Li, Zhenhua Ling |
| 2026-01-20 | [HoverAI: An Embodied Aerial Agent for Natural Human-Drone Interaction](https://arxiv.org/abs/2601.13801) | Yuhua Jin, Nikita Kuzmin, Georgii Demianchuk, Mariya Lezina et al. |
| 2026-01-19 | [Exploring Talking Head Models With Adjacent Frame Prior for Speech-Preserving Facial Expression Manipulation](https://arxiv.org/abs/2601.12876) | Zhenxuan Lu, Zhihua Xu, Zhijing Yang, Feng Gao et al. |
| 2026-01-15 | [EditEmoTalk: Controllable Speech-Driven 3D Facial Animation with Continuous Expression Editing](https://arxiv.org/abs/2601.10000) | Diqiong Jiang, Kai Zhu, Dan Song, Jian Chang et al. |
| 2026-01-15 | [RSATalker: Realistic Socially-Aware Talking Head Generation for Multi-Turn Conversation](https://arxiv.org/abs/2601.10606) | Peng Chen, Xiaobao Wei, Yi Yang, Naiming Yao et al. |
| 2026-01-14 | [Now You See Me, Now You Don't: A Unified Framework for Expression Consistent Anonymization in Talking Head Videos](https://arxiv.org/abs/2601.11635) | Anil Egin, Andrea Tangherloni, Antitza Dantcheva |
| 2026-01-05 | [ESGaussianFace: Emotional and Stylized Audio-Driven Facial Animation via 3D Gaussian Splatting](https://arxiv.org/abs/2601.01847) | Chuhang Ma, Shuai Tan, Ye Pan, Jiaolong Yang, Xin Tong |
| 2026-01-05 | [MANGO:Natural Multi-speaker 3D Talking Head Generation via 2D-Lifted Enhancement](https://arxiv.org/abs/2601.01749) | Lei Zhu, Lijian Lin, Ye Zhu, Jiahao Wu et al. |
| 2026-01-04 | [MM-Sonate: Multimodal Controllable Audio-Video Generation with Zero-Shot Voice Cloning](https://arxiv.org/abs/2601.01568) | Chunyu Qiang, Jun Wang, Xiaopeng Wang, Kang Yin, Yuxin Guo |
| 2026-01-02 | [Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation](https://arxiv.org/abs/2601.00664) | Taekyung Ki, Sangwon Jang, Jaehyeong Jo, Jaehong Yoon, Sung Ju Hwang |

### 2025

| Date | Title | Authors |
|------|-------|---------|
| 2025-12-31 | [From Inpainting to Editing: A Self-Bootstrapping Framework for Context-Rich Visual Dubbing](https://arxiv.org/abs/2512.25066) | Xu He, Haoxian Zhang, Hejia Chen, Changyuan Zheng et al. |
| 2025-12-30 | [DyStream: Streaming Dyadic Talking Heads Generation via Flow Matching-based Autoregressive Model](https://arxiv.org/abs/2512.24408) | Bohong Chen, Haiyang Liu |
| 2025-12-27 | [PTalker: Personalized Speech-Driven 3D Talking Head Animation via Style Disentanglement and Modality Alignment](https://arxiv.org/abs/2512.22602) | Bin Wang, Yang Xu, Huan Zhao, Hao Zhang, Zixing Zhang |
| 2025-12-25 | [SyncAnyone: Implicit Disentanglement via Progressive Self-Correction for Lip-Syncing in the wild](https://arxiv.org/abs/2512.21736) | Xindi Zhang, Dechao Meng, Steven Xiao, Qi Wang et al. |
| 2025-12-24 | [ALIVE: An Avatar-Lecture Interactive Video Engine with Content-Aware Retrieval for Real-Time Interaction](https://arxiv.org/abs/2512.20858) | Md Zabirul Islam, Md Motaleb Hossen Manik, Ge Wang |
| 2025-12-24 | [Efficient and Robust Video Defense Framework against 3D-field Personalized Talking Face](https://arxiv.org/abs/2512.21019) | Rui-qing Sun, Xingshan Yao, Tian Lan, Jia-Ling Shi et al. |
| 2025-12-23 | [FlashLips: 100-FPS Mask-Free Latent Lip-Sync using Reconstruction Instead of Diffusion or GANs](https://arxiv.org/abs/2512.20033) | Andreas Zinonos, Michał Stypułkowski, Antoni Bigata, Stavros Petridis et al. |
| 2025-12-23 | [TAVID: Text-Driven Audio-Visual Interactive Dialogue Generation](https://arxiv.org/abs/2512.20296) | Ji-Hoon Kim, Junseok Ahn, Doyeop Kwak, Joon Son Chung, Shinji Watanabe |
| 2025-12-21 | [In-Context Audio Control of Video Diffusion Transformers](https://arxiv.org/abs/2512.18772) | Wenze Liu, Weicai Ye, Minghong Cai, Quande Liu et al. |
| 2025-12-20 | [Asynchronous Pipeline Parallelism for Real-Time Multilingual Lip Synchronization in Video Communication Systems](https://arxiv.org/abs/2512.18318) | Eren Caglar, Amirkia Rafiei Oskooei, Mehmet Kutanoglu, Mustafa Keles, Mehmet S. Aktas |
| 2025-12-20 | [MACE-Dance: Motion-Appearance Cascaded Experts for Music-Driven Dance Video Generation](https://arxiv.org/abs/2512.18181) | Kaixing Yang, Jiashu Zhu, Xulong Tang, Ziqiao Peng et al. |
| 2025-12-19 | [InstructDubber: Instruction-based Alignment for Zero-shot Movie Dubbing](https://arxiv.org/abs/2512.17154) | Zhedong Zhang, Liang Li, Gaoxiang Cong, Chunshan Liu et al. |
| 2025-12-19 | [SynergyWarpNet: Attention-Guided Cooperative Warping for Neural Portrait Animation](https://arxiv.org/abs/2512.17331) | Shihang Li, Zhiqiang Gong, Minming Ye, Yue Gao, Wen Yao |
| 2025-12-16 | [TalkVerse: Democratizing Minute-Long Audio-Driven Video Generation](https://arxiv.org/abs/2512.14938) | Zhenzhi Wang, Jian Wang, Ke Ma, Dahua Lin, Bing Zhou |
| 2025-12-16 | [FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling](https://arxiv.org/abs/2512.14056) | Kim Sung-Bin, Joohyun Chang, David Harwath, Tae-Hyun Oh |
| 2025-12-16 | [VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image](https://arxiv.org/abs/2512.14677) | Sicheng Xu, Guojun Chen, Jiaolong Yang, Yizhong Zhang et al. |
| 2025-12-15 | [JoVA: Unified Multimodal Learning for Joint Video-Audio Generation](https://arxiv.org/abs/2512.13677) | Xiaohu Huang, Hao Zhou, Qiangpeng Yang, Shilei Wen, Kai Han |
| 2025-12-15 | [Seedance 1.5 pro: A Native Audio-Visual Joint Generation Foundation Model](https://arxiv.org/abs/2512.13507) | Team Seedance, Heyi Chen, Siyan Chen, Xin Chen et al. |
| 2025-12-15 | [Soul: Breathe Life into Digital Human for High-fidelity Long-term Multimodal Animation](https://arxiv.org/abs/2512.13495) | Jiangning Zhang, Junwei Zhu, Zhenye Gan, Donghao Luo et al. |
| 2025-12-15 | [KlingAvatar 2.0 Technical Report](https://arxiv.org/abs/2512.13313) | Kling Team, Jialu Chen, Yikang Ding, Zhixue Fang et al. |
| 2025-12-12 | [JoyAvatar-Flash: Real-time and Infinite Audio-Driven Avatar Generation with Autoregressive Diffusion](https://arxiv.org/abs/2512.11423) | Chaochao Li, Ruikui Wang, Liangbo Zhou, Jinheng Feng et al. |
| 2025-12-12 | [REST: Diffusion-based Real-time End-to-end Streaming Talking Head Generation via ID-Context Caching and Asynchronous Streaming Distillation](https://arxiv.org/abs/2512.11229) | Haotian Wang, Yuzhe Weng, Jun Du, Haoran Xu et al. |
| 2025-12-11 | [GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939) | Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh |
| 2025-11-30 | [EmoDiffTalk:Emotion-aware Diffusion for Editable 3D Gaussian Talking Head](https://arxiv.org/abs/2512.05991) | Chang Liu, Tianjiao Jing, Chengcheng Ma, Xuanqi Zhou et al. |
| 2025-11-28 | [AnyTalker: Scaling Multi-Person Talking Video Generation with Interactivity Refinement](https://arxiv.org/abs/2511.23475) | Zhizhou Zhong, Yicheng Ji, Zhe Kong, Yiying Liu et al. |
| 2025-11-27 | [VSpeechLM: A Visual Speech Language Model for Visual Text-to-Speech Task](https://arxiv.org/abs/2511.22229) | Yuyue Wang, Xin Cheng, Yihan Wu, Xihua Wang et al. |
| 2025-11-27 | [IMTalker: Efficient Audio-driven Talking Face Generation with Implicit Motion Transfer](https://arxiv.org/abs/2511.22167) | Bo Chen, Tao Liu, Qi Chen, Xie Chen, Zilong Zheng |
| 2025-11-27 | [AI killed the video star. Audio-driven diffusion model for expressive talking head generation](https://arxiv.org/abs/2511.22488) | Baptiste Chopin, Tashvik Dhamija, Pranav Balaji, Yaohui Wang, Antitza Dantcheva |
| 2025-11-24 | [AuViRe: Audio-visual Speech Representation Reconstruction for Deepfake Temporal Localization](https://arxiv.org/abs/2511.18993) | Christos Koutlis, Symeon Papadopoulos |
| 2025-11-22 | [A superpersuasive autonomous policy debating system](https://arxiv.org/abs/2511.17854) | Allen Roush, Devin Gonier, John Hines, Judah Goldfeder et al. |
| 2025-11-18 | [Towards Authentic Movie Dubbing with Retrieve-Augmented Director-Actor Interaction Learning](https://arxiv.org/abs/2511.14249) | Rui Liu, Yuan Zhao, Zhenqi Jia |
| 2025-11-17 | [Passive Dementia Screening via Facial Temporal Micro-Dynamics Analysis of In-the-Wild Talking-Head Video](https://arxiv.org/abs/2511.13802) | Filippo Cenacchi, Longbing Cao, Mitchell McEwan, Deborah Richards |
| 2025-11-12 | [GRACE: Designing Generative Face Video Codec via Agile Hardware-Centric Workflow](https://arxiv.org/abs/2511.09272) | Rui Wan, Qi Zheng, Ruoyu Zhang, Bu Chen et al. |
| 2025-11-11 | [Is It Truly Necessary to Process and Fit Minutes-Long Reference Videos for Personalized Talking Face Generation?](https://arxiv.org/abs/2511.07940) | Rui-Qing Sun, Ang Li, Zhijing Wu, Tian Lan et al. |
| 2025-11-10 | [ConsistTalk: Intensity Controllable Temporally Consistent Talking Head Generation with Diffusion Noise Search](https://arxiv.org/abs/2511.06833) | Zhenjie Liu, Jianzhang Lu, Renjie Lu, Cong Liang, Shangfei Wang |
| 2025-11-07 | [Shared Latent Representation for Joint Text-to-Audio-Visual Synthesis](https://arxiv.org/abs/2511.05432) | Dogucan Yaman, Seymanur Akti, Fevziye Irem Eyiokur, Alexander Waibel |
| 2025-11-06 | [THEval. Evaluation Framework for Talking Head Video Generation](https://arxiv.org/abs/2511.04520) | Nabyl Quignon, Baptiste Chopin, Yaohui Wang, Antitza Dantcheva |
| 2025-11-05 | [Assessing Identity Leakage in Talking Face Generation: Metrics and Evaluation Framework](https://arxiv.org/abs/2511.08613) | Dogucan Yaman, Fevziye Irem Eyiokur, Hazım Kemal Ekenel, Alexander Waibel |
| 2025-11-05 | [UniAVGen: Unified Audio and Video Generation with Asymmetric Cross-Modal Interactions](https://arxiv.org/abs/2511.03334) | Guozhen Zhang, Zixiang Zhou, Teng Hu, Ziqiao Peng et al. |
| 2025-11-04 | [Densemarks: Learning Canonical Embeddings for Human Heads Images via Point Tracks](https://arxiv.org/abs/2511.02830) | Dmitrii Pozdeev, Alexey Artemov, Ananta R. Bhattarai, Artem Sevastopolsky |
| 2025-10-29 | [Learning Disentangled Speech- and Expression-Driven Blendshapes for 3D Talking Face Animation](https://arxiv.org/abs/2510.25234) | Yuxiang Mao, Zhijie Zhang, Zhiheng Zhang, Jiawei Liu et al. |
| 2025-10-29 | [Audio-Visual Speech Enhancement In Complex Scenarios With Separation And Dereverberation Joint Modeling](https://arxiv.org/abs/2510.26825) | Jiarong Du, Zhan Jin, Peijun Yang, Juan Liu et al. |
| 2025-10-28 | [See the Speaker: Crafting High-Resolution Talking Faces from Speech with Prior Guidance and Region Refinement](https://arxiv.org/abs/2510.26819) | Jinting Wang, Jun Wang, Hei Victor Cheng, Li Liu |
| 2025-10-27 | [Lookahead Anchoring: Preserving Character Identity in Audio-Driven Human Animation](https://arxiv.org/abs/2510.23581) | Junyoung Seo, Rodrigo Mira, Alexandros Haliassos, Stella Bounareli et al. |
| 2025-10-26 | [MAGIC-Talk: Motion-aware Audio-Driven Talking Face Generation with Customizable Identity Control](https://arxiv.org/abs/2510.22810) | Fatemeh Nazarieh, Zhenhua Feng, Diptesh Kanojia, Muhammad Awais, Josef Kittler |
| 2025-10-26 | [DeepfakeBench-MM: A Comprehensive Benchmark for Multimodal Deepfake Detection](https://arxiv.org/abs/2510.22622) | Kangran Zhao, Yupeng Chen, Xiaoyu Zhang, Yize Chen et al. |
| 2025-10-18 | [Audio-Visual Speech Enhancement for Spatial Audio - Spatial-VisualVoice and the MAVE Database](https://arxiv.org/abs/2510.16437) | Danielle Yaffe, Ferdinand Campe, Prachi Sharma, Dorothea Kolossa, Boaz Rafaely |
| 2025-10-16 | [PIA: Deepfake Detection Using Phoneme-Temporal and Identity-Dynamic Analysis](https://arxiv.org/abs/2510.14241) | Soumyya Kanti Datta, Tanvi Ranga, Chengzhe Sun, Siwei Lyu |
| 2025-10-14 | [Playmate2: Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback](https://arxiv.org/abs/2510.12089) | Xingpei Ma, Shenneng Huang, Jiaran Cai, Yuansheng Guan et al. |
| 2025-10-12 | [DEMO: Disentangled Motion Latent Flow Matching for Fine-Grained Controllable Talking Portrait Synthesis](https://arxiv.org/abs/2510.10650) | Peiyin Chen, Zhuowei Yang, Hui Feng, Sheng Jiang, Rui Yan |
| 2025-10-11 | [VividAnimator: An End-to-End Audio and Pose-driven Half-Body Human Animation Framework](https://arxiv.org/abs/2510.10269) | Donglin Huang, Yongyuan Li, Tianhang Liu, Junming Huang et al. |
| 2025-10-08 | [A Bridge from Audio to Video: Phoneme-Viseme Alignment Allows Every Face to Speak Multiple Languages](https://arxiv.org/abs/2510.06612) | Zibo Su, Kun Wei, Jiahua Li, Xu Yang, Cheng Deng |
| 2025-10-06 | [Paper2Video: Automatic Video Generation from Scientific Papers](https://arxiv.org/abs/2510.05096) | Zeyu Zhu, Kevin Qinghong Lin, Mike Zheng Shou |
| 2025-10-06 | [AUREXA-SE: Audio-Visual Unified Representation Exchange Architecture with Cross-Attention and Squeezeformer for Speech Enhancement](https://arxiv.org/abs/2510.05295) | M. Sajid, Deepanshu Gupta, Yash Modi, Sanskriti Jain et al. |
| 2025-10-03 | [EGSTalker: Real-Time Audio-Driven Talking Head Generation with Efficient Gaussian Deformation](https://arxiv.org/abs/2510.08587) | Tianheng Zhu, Yinfeng Yu, Liejun Wang, Fuchun Sun, Wendong Zheng |
| 2025-10-03 | [Unmasking Puppeteers: Leveraging Biometric Leakage to Disarm Impersonation in AI-based Videoconferencing](https://arxiv.org/abs/2510.03548) | Danial Samadi Vahdati, Tai Duc Nguyen, Ekta Prashnani, Koki Nagano et al. |
| 2025-10-02 | [Input-Aware Sparse Attention for Real-Time Co-Speech Video Generation](https://arxiv.org/abs/2510.02617) | Beijia Lu, Ziyi Chen, Jing Xiao, Jun-Yan Zhu |
| 2025-09-28 | [Efficient Audio-Visual Speech Separation with Discrete Lip Semantics and Multi-Scale Global-Local Attention](https://arxiv.org/abs/2509.23610) | Kai Li, Kejun Gao, Xiaolin Hu |
| 2025-09-26 | [StableDub: Taming Diffusion Prior for Generalized and Efficient Visual Dubbing](https://arxiv.org/abs/2509.21887) | Liyang Chen, Tianze Zhou, Xu He, Boshi Tang et al. |
| 2025-09-24 | [Talking Head Generation via AU-Guided Landmark Prediction](https://arxiv.org/abs/2509.19749) | Shao-Yu Chang, Jingyi Xu, Hieu Le, Dimitris Samaras |
| 2025-09-24 | [KSDiff: Keyframe-Augmented Speech-Aware Dual-Path Diffusion for Facial Animation](https://arxiv.org/abs/2509.20128) | Tianle Lyu, Junchuan Zhao, Ye Wang |
| 2025-09-24 | [SynchroRaMa : Lip-Synchronized and Emotion-Aware Talking Face Generation via Multi-Modal Emotion Embedding](https://arxiv.org/abs/2509.19965) | Phyo Thet Yee, Dimitrios Kollias, Sudeepta Mishra, Abhinav Dhall |
| 2025-09-24 | [Comparative Study of Subjective Video Quality Assessment Test Methods in Crowdsourcing for Varied Use Cases](https://arxiv.org/abs/2509.20118) | Babak Naderi, Ross Cutler |
| 2025-09-23 | [Audio-Driven Universal Gaussian Head Avatars](https://arxiv.org/abs/2509.18924) | Kartik Teotia, Helge Rhodin, Mohit Mendiratta, Hyeongwoo Kim et al. |
| 2025-09-21 | [PGSTalker: Real-Time Audio-Driven Talking Head Generation via 3D Gaussian Splatting with Pixel-Aware Density Control](https://arxiv.org/abs/2509.16922) | Tianheng Zhu, Yinfeng Yu, Liejun Wang, Fuchun Sun, Wendong Zheng |
| 2025-09-17 | [Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior](https://arxiv.org/abs/2509.14379) | Yochai Yemini, Rami Ben-Ari, Sharon Gannot, Ethan Fetaya |
| 2025-09-16 | [A Lightweight Pipeline for Noisy Speech Voice Cloning and Accurate Lip Sync Synthesis](https://arxiv.org/abs/2509.12831) | Javeria Amir, Farwa Attaria, Mah Jabeen, Umara Noor, Zahid Rashid |
| 2025-09-16 | [Robust Audio-Visual Target Speaker Extraction with Emotion-Aware Multiple Enrollment Fusion](https://arxiv.org/abs/2509.12583) | Zhan Jin, Bang Zeng, Peijun Yang, Jiarong Du et al. |
| 2025-09-15 | [AvatarSync: Rethinking Talking-Head Animation through Phoneme-Guided Autoregressive Perspective](https://arxiv.org/abs/2509.12052) | Yuchen Deng, Xiuyang Wu, Hai-Tao Zheng, Suiyang Zhang et al. |
| 2025-09-11 | [Kling-Avatar: Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis](https://arxiv.org/abs/2509.09595) | Yikang Ding, Jiwen Liu, Wenyuan Zhang, Zekun Wang et al. |
| 2025-09-10 | [Bitrate-Controlled Diffusion for Disentangling Motion and Content in Video](https://arxiv.org/abs/2509.08376) | Xiao Li, Qi Chen, Xiulian Peng, Kai Yu et al. |
| 2025-08-28 | [EmoCAST: Emotional Talking Portrait via Emotive Text Description](https://arxiv.org/abs/2508.20615) | Yiguo Jiang, Xiaodong Cun, Yong Zhang, Yudian Zheng et al. |
| 2025-08-27 | [InfinityHuman: Towards Long-Term Audio-Driven Human](https://arxiv.org/abs/2508.20210) | Xiaodi Li, Pan Xie, Yi Ren, Qijun Gan et al. |
| 2025-08-27 | [Improving Generalization in Deepfake Detection with Face Foundation Models and Metric Learning](https://arxiv.org/abs/2508.19730) | Stelios Mylonas, Symeon Papadopoulos |
| 2025-08-26 | [OmniHuman-1.5: Instilling an Active Mind in Avatars via Cognitive Simulation](https://arxiv.org/abs/2508.19209) | Jianwen Jiang, Weihong Zeng, Zerong Zheng, Jiaqi Yang et al. |
| 2025-08-26 | [Wan-S2V: Audio-Driven Cinematic Video Generation](https://arxiv.org/abs/2508.18621) | Xin Gao, Li Hu, Siqi Hu, Mingyang Huang et al. |
| 2025-08-25 | [Warm Chat: Diffuse Emotion-aware Interactive Talking Head Avatar with Tree-Structured Guidance](https://arxiv.org/abs/2508.18337) | Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian, Jian Yang |
| 2025-08-25 | [Lightning Fast Caching-based Parallel Denoising Prediction for Accelerating Talking Head Generation](https://arxiv.org/abs/2509.00052) | Jianzhi Long, Wenhao Sun, Rongcheng Tu, Dacheng Tao |
| 2025-08-20 | [D^3-Talker: Dual-Branch Decoupled Deformation Fields for Few-Shot 3D Talking Head Synthesis](https://arxiv.org/abs/2508.14449) | Yuhang Guo, Kaijun Deng, Siyang Song, Jindong Xie et al. |
| 2025-08-20 | [Taming Transformer for Emotion-Controllable Talking Face Generation](https://arxiv.org/abs/2508.14359) | Ziqi Zhang, Cheng Deng |
| 2025-08-19 | [TalkVid: A Large-Scale Diversified Dataset for Audio-Driven Talking Head Synthesis](https://arxiv.org/abs/2508.13618) | Shunian Chen, Hejin Huang, Yexin Liu, Zihan Ye et al. |
| 2025-08-19 | [EDTalk++: Full Disentanglement for Controllable Talking Head Synthesis](https://arxiv.org/abs/2508.13442) | Shuai Tan, Bin Ji |
| 2025-08-19 | [Leveraging Mamba with Full-Face Vision for Audio-Visual Speech Enhancement](https://arxiv.org/abs/2508.13624) | Rong Chao, Wenze Ren, You-Jin Li, Kuo-Hsuan Hung et al. |
| 2025-08-19 | [End-to-end audio-visual learning for cochlear implant sound coding simulations in noisy environments](https://arxiv.org/abs/2508.13576) | Meng-Ping Lin, Enoch Hsin-Ho Huang, Shao-Yi Chien, Yu Tsao |
| 2025-08-17 | [CEM-Net: Cross-Emotion Memory Network for Emotional Talking Face Generation](https://arxiv.org/abs/2508.12368) | Kangyi Wu, Pengna Li, Jingwen Fu, Yang Wu et al. |
| 2025-08-16 | [RealTalk: Realistic Emotion-Aware Lifelike Talking-Head Synthesis](https://arxiv.org/abs/2508.12163) | Wenqing Wang, Yun Fu |
| 2025-08-15 | [FantasyTalking2: Timestep-Layer Adaptive Preference Optimization for Audio-Driven Portrait Animation](https://arxiv.org/abs/2508.11255) | MengChao Wang, Qiang Wang, Fan Jiang, Mu Xu |
| 2025-08-14 | [HM-Talker: Hybrid Motion Modeling for High-Fidelity Talking Head Synthesis](https://arxiv.org/abs/2508.10566) | Shiyu Liu, Kui Jiang, Xianming Liu, Hongxun Yao, Xiaocheng Feng |
| 2025-08-13 | [SpeechForensics: Audio-Visual Speech Representation Learning for Face Forgery Detection](https://arxiv.org/abs/2508.09913) | Yachao Liang, Min Yu, Gang Li, Jianguo Jiang et al. |
| 2025-08-11 | [Audio-Visual Speech Enhancement: Architectural Design and Deployment Strategies](https://arxiv.org/abs/2508.08468) | Anis Hamadouche, Haifeng Luo, Mathini Sellathurai, Tharm Ratnarajah |
| 2025-08-10 | [KLASSify to Verify: Audio-Visual Deepfake Detection Using SSL-based Audio and Handcrafted Visual Features](https://arxiv.org/abs/2508.07337) | Ivan Kukanov, Jun Wah Ng |
| 2025-08-08 | [MotionSwap](https://arxiv.org/abs/2508.06430) | Om Patil, Jinesh Modi, Suryabha Mukhopadhyay, Meghaditya Giri, Chhavi Malhotra |
| 2025-08-07 | [RAP: Real-time Audio-driven Portrait Animation with Video Diffusion Transformer](https://arxiv.org/abs/2508.05115) | Fangyu Du, Taiqing Li, Qian Qiao, Tan Yu et al. |
| 2025-08-06 | [UniTalker: Conversational Speech-Visual Synthesis](https://arxiv.org/abs/2508.04585) | Yifan Hu, Rui Liu, Yi Ren, Xiang Yin, Haizhou Li |
| 2025-08-05 | [READ: Real-time and Efficient Asynchronous Diffusion for Audio-driven Talking Head Generation](https://arxiv.org/abs/2508.03457) | Haotian Wang, Yuzhe Weng, Jun Du, Haoran Xu et al. |
| 2025-08-04 | [Text2Lip: Progressive Lip-Synced Talking Face Generation from Text via Viseme-Guided Rendering](https://arxiv.org/abs/2508.02362) | Xu Wang, Shengeng Tang, Fei Wang, Lechao Cheng et al. |
| 2025-08-04 | [X-Actor: Emotional and Expressive Long-Range Portrait Acting from Audio](https://arxiv.org/abs/2508.02944) | Chenxu Zhang, Zenan Li, Hongyi Xu, You Xie et al. |
| 2025-08-01 | [AudioGen-Omni: A Unified Multimodal Diffusion Transformer for Video-Synchronized Audio, Speech, and Song Generation](https://arxiv.org/abs/2508.00733) | Le Wang, Jun Wang, Chunyu Qiang, Feng Deng et al. |
| 2025-08-01 | [Is It Really You? Exploring Biometric Verification Scenarios in Photorealistic Talking-Head Avatar Videos](https://arxiv.org/abs/2508.00748) | Laura Pedrouzo-Rodriguez, Pedro Delgado-DeRobles, Luis F. Gomez, Ruben Tolosana et al. |
| 2025-07-31 | [Who is a Better Talker: Subjective and Objective Quality Assessment for AI-Generated Talking Heads](https://arxiv.org/abs/2507.23343) | Yingjie Zhou, Jiezhang Cao, Zicheng Zhang, Farong Wen et al. |
| 2025-07-30 | [Robust Deepfake Detection for Electronic Know Your Customer Systems Using Registered Images](https://arxiv.org/abs/2507.22601) | Takuma Amada, Kazuya Kakizaki, Taiki Miyagawa, Akinori F. Ebihara et al. |
| 2025-07-29 | [DiTalker: A Unified DiT-based Framework for High-Quality and Speaking Styles Controllable Portrait Animation](https://arxiv.org/abs/2508.06511) | He Feng, Yongjia Ma, Donglin Di, Lei Fan et al. |
| 2025-07-28 | [JOLT3D: Joint Learning of Talking Heads and 3DMM Parameters with Application to Lip-Sync](https://arxiv.org/abs/2507.20452) | Sungjoon Park, Minsik Park, Haneol Lee, Jaesub Yun, Donggeon Lee |
| 2025-07-28 | [Mask-Free Audio-driven Talking Face Generation for Enhanced Visual Quality and Identity Preservation](https://arxiv.org/abs/2507.20953) | Dogucan Yaman, Fevziye Irem Eyiokur, Leonard Bärmann, Hazım Kemal Ekenel, Alexander Waibel |
| 2025-07-27 | [MagicAnime: A Hierarchically Annotated, Multimodal and Multitasking Dataset with Benchmarks for Cartoon Animation Generation](https://arxiv.org/abs/2507.20368) | Shuolin Xu, Bingyuan Wang, Zeyu Cai, Fangteng Fu et al. |
| 2025-07-25 | [Face2VoiceSync: Lightweight Face-Voice Consistency for Text-Driven Talking Face Generation](https://arxiv.org/abs/2507.19225) | Fang Kang, Yin Cao, Haoyu Chen |
| 2025-07-24 | [Celeb-DF++: A Large-scale Challenging Video DeepFake Benchmark for Generalizable Forensics](https://arxiv.org/abs/2507.18015) | Yuezun Li, Delong Zhu, Xinjie Cui, Siwei Lyu |
| 2025-07-22 | [Livatar-1: Real-Time Talking Heads Generation with Tailored Flow Matching](https://arxiv.org/abs/2507.18649) | Haiyang Liu, Xiaolin Hong, Xuancheng Yang, Yudi Ruan et al. |
| 2025-07-22 | [Navigating Large-Pose Challenge for High-Fidelity Face Reenactment with Video Diffusion Model](https://arxiv.org/abs/2507.16341) | Mingtao Guo, Guanyu Xing, Yanci Zhang, Yanli Liu |
| 2025-07-17 | [Cross-Modal Watermarking for Authentic Audio Recovery and Tamper Localization in Synthesized Audiovisual Forgeries](https://arxiv.org/abs/2507.12723) | Minyoung Kim, Sehwan Park, Sungmin Cha, Paul Hongsuck Seo |
| 2025-07-17 | [ATL-Diff: Audio-Driven Talking Head Generation with Early Landmarks-Guide Noise Diffusion](https://arxiv.org/abs/2507.12804) | Hoang-Son Vo, Quang-Vinh Nguyen, Seungwon Kim, Hyung-Jeong Yang et al. |
| 2025-07-17 | [Think-Before-Draw: Decomposing Emotion Semantics & Fine-Grained Controllable Expressive Talking Head Generation](https://arxiv.org/abs/2507.12761) | Hanlei Shi, Leyuan Qu, Yu Liu, Di Gao et al. |
| 2025-07-17 | [AVFSNet: Audio-Visual Speech Separation for Flexible Number of Speakers with Multi-Scale and Multi-Task Learning](https://arxiv.org/abs/2507.12972) | Daning Zhang, Ying Wei |
| 2025-07-11 | [Detecting Deepfake Talking Heads from Facial Biometric Anomalies](https://arxiv.org/abs/2507.08917) | Justin D. Norman, Hany Farid |
| 2025-07-11 | [M2DAO-Talker: Harmonizing Multi-granular Motion Decoupling and Alternating Optimization for Talking-head Generation](https://arxiv.org/abs/2507.08307) | Kui Jiang, Shiyu Liu, Junjun Jiang, Hongxun Yao, Xiaopeng Fan |
| 2025-07-09 | [Audio-Visual Speech Separation via Bottleneck Iterative Network](https://arxiv.org/abs/2507.07270) | Sidong Zhang, Shiv Shankar, Trang Nguyen, Andrea Fanelli, Madalina Fiterau |
| 2025-07-08 | [MEDTalk: Multimodal Controlled 3D Facial Animation with Dynamic Emotions by Disentangled Embedding](https://arxiv.org/abs/2507.06071) | Chang Liu, Ye Pan, Chenyang Ding, Susanto Rahardja, Xiaokang Yang |
| 2025-07-07 | [MoDiT: Learning Highly Consistent 3D Motion Coefficients with Diffusion Transformer for Talking Head Generation](https://arxiv.org/abs/2507.05092) | Yucheng Wang, Dan Xu |
| 2025-07-04 | [MoDA: Multi-modal Diffusion Architecture for Talking Head Generation](https://arxiv.org/abs/2507.03256) | Xinyang Li, Gen Li, Zhihui Lin, Yichen Qian et al. |
| 2025-07-03 | [CanonSwap: High-Fidelity and Consistent Video Face Swapping via Canonical Space Modulation](https://arxiv.org/abs/2507.02691) | Xiangyang Luo, Ye Zhu, Yunfei Liu, Lijian Lin et al. |
| 2025-07-02 | [FixTalk: Taming Identity Leakage for High-Quality Talking Head Generation in Extreme Cases](https://arxiv.org/abs/2507.01390) | Shuai Tan, Bill Gong, Bin Ji, Ye Pan |
| 2025-06-30 | [JAM-Flow: Joint Audio-Motion Synthesis with Flow Matching](https://arxiv.org/abs/2506.23552) | Mingi Kwon, Joonghyuk Shin, Jaeseok Jung, Jaesik Park, Youngjung Uh |
| 2025-06-27 | [MirrorMe: Towards Realtime and High Fidelity Audio-Driven Halfbody Animation](https://arxiv.org/abs/2506.22065) | Dechao Meng, Steven Xiao, Xindi Zhang, Guangyuan Wang et al. |
| 2025-06-27 | [Few-Shot Identity Adaptation for 3D Talking Heads via Global Gaussian Field](https://arxiv.org/abs/2506.22044) | Hong Nie, Fuyuan Cao, Lu Chen, Fengxin Chen et al. |
| 2025-06-27 | [RiverEcho: Real-Time Interactive Digital System for Ancient Yellow River Culture](https://arxiv.org/abs/2506.21865) | Haofeng Wang, Yilin Guo, Zehao Li, Tong Yue et al. |
| 2025-06-26 | [GGTalker: Talking Head Systhesis with Generalizable Gaussian Priors and Identity-Specific Adaptation](https://arxiv.org/abs/2506.21513) | Wentao Hu, Shunkai Li, Ziqiao Peng, Haoxian Zhang et al. |
| 2025-06-24 | [Bind-Your-Avatar: Multi-Talking-Character Video Generation with Dynamic 3D-mask-based Embedding Router](https://arxiv.org/abs/2506.19833) | Yubo Huang, Weiqiang Wang, Sirui Zhao, Tong Xu et al. |
| 2025-06-23 | [OmniAvatar: Efficient Audio-Driven Avatar Video Generation with Adaptive Body Animation](https://arxiv.org/abs/2506.18866) | Qijun Gan, Ruizi Yang, Jianke Zhu, Shaofei Xue, Steven Hoi |
| 2025-06-23 | [Advancing Talking Head Generation: A Comprehensive Survey of Multi-Modal Methodologies, Datasets, Evaluation Metrics, and Loss Functions](https://arxiv.org/abs/2507.02900) | Vineet Kumar Rakesh, Soumya Mazumdar, Research Pratim Maity, Sarbajit Pal et al. |
| 2025-06-17 | [SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742) | Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu et al. |
| 2025-06-17 | [Compressed Video Super-Resolution based on Hierarchical Encoding](https://arxiv.org/abs/2506.14381) | Yuxuan Jiang, Siyue Teng, Qiang Zhu, Chen Feng et al. |
| 2025-06-16 | [Audio-Visual Driven Compression for Low-Bitrate Talking Head Videos](https://arxiv.org/abs/2506.13419) | Riku Takahashi, Ryugo Morita, Jinjia Zhou |
| 2025-06-15 | [iDiT-HOI: Inpainting-based Hand Object Interaction Reenactment via Video Diffusion Transformer](https://arxiv.org/abs/2506.12847) | Zhelun Shen, Chenming Wu, Junsheng Zhou, Chen Zhao et al. |
| 2025-06-13 | [ICME 2025 Grand Challenge on Video Super-Resolution for Video Conferencing](https://arxiv.org/abs/2506.12269) | Babak Naderi, Ross Cutler, Juhee Cho, Nabakumar Khongbantabam, Dejan Ivkovic |
| 2025-06-10 | [HunyuanVideo-HOMA: Generic Human-Object Interaction in Multimodal Driven Human Animation](https://arxiv.org/abs/2506.08797) | Ziyao Huang, Zixiang Zhou, Juan Cao, Yifeng Ma et al. |
| 2025-06-07 | [A Fast and Lightweight Model for Causal Audio-Visual Speech Separation](https://arxiv.org/abs/2506.06689) | Wendi Sang, Kai Li, Runxuan Yang, Jianqiang Huang, Xiaolin Hu |
| 2025-06-03 | [NTIRE 2025 XGC Quality Assessment Challenge: Methods and Results](https://arxiv.org/abs/2506.02875) | Xiaohong Liu, Xiongkuo Min, Qiang Hu, Xiaoyun Zhang et al. |
| 2025-06-02 | [Silence is Golden: Leveraging Adversarial Examples to Nullify Audio Control in LDM-based Talking-Head Generation](https://arxiv.org/abs/2506.01591) | Yuan Gan, Jiaxu Miao, Yunze Wang, Yi Yang |
| 2025-06-01 | [SkyReels-Audio: Omni Audio-Conditioned Talking Portraits in Video Diffusion Transformers](https://arxiv.org/abs/2506.00830) | Zhengcong Fei, Hao Jiang, Di Qiu, Baoxuan Gu et al. |
| 2025-05-30 | [TalkingHeadBench: A Multi-Modal Benchmark & Analysis of Talking-Head DeepFake Detection](https://arxiv.org/abs/2505.24866) | Xinqi Xiong, Prakrut Patel, Qingyuan Fan, Amisha Wadhwa et al. |
| 2025-05-29 | [MMGT: Motion Mask Guided Two-Stage Network for Co-Speech Gesture Video Generation](https://arxiv.org/abs/2505.23120) | Siyuan Wang, Jiawei Liu, Wei Wang, Yeying Jin et al. |
| 2025-05-29 | [Hallo4: High-Fidelity Dynamic Portrait Animation via Direct Preference Optimization](https://arxiv.org/abs/2505.23525) | Jiahao Cui, Yan Chen, Mingwang Xu, Hanlin Shang et al. |
| 2025-05-29 | [Video Editing for Audio-Visual Dubbing](https://arxiv.org/abs/2505.23406) | Binyamin Manela, Sharon Gannot, Ethan Fetyaya |
| 2025-05-28 | [Tell me Habibi, is it Real or Fake?](https://arxiv.org/abs/2505.22581) | Kartik Kuckreja, Parul Gupta, Injy Hamed, Thamar Solorio et al. |
| 2025-05-28 | [FaceEditTalker: Controllable Talking Head Generation with Facial Attribute Editing](https://arxiv.org/abs/2505.22141) | Guanwen Feng, Zhiyuan Ma, Yunan Li, Jiahao Yang et al. |
| 2025-05-28 | [Let Them Talk: Audio-Driven Multi-Person Conversational Video Generation](https://arxiv.org/abs/2505.22647) | Zhe Kong, Feng Gao, Yong Zhang, Zhuoliang Kang et al. |
| 2025-05-28 | [RESOUND: Speech Reconstruction from Silent Videos via Acoustic-Semantic Decomposed Modeling](https://arxiv.org/abs/2505.22024) | Long-Khanh Pham, Thanh V. T. Tran, Minh-Tan Pham, Van Nguyen |
| 2025-05-27 | [OmniSync: Towards Universal Lip Synchronization via Diffusion Transformers](https://arxiv.org/abs/2505.21448) | Ziqiao Peng, Jiwen Liu, Haoxian Zhang, Xiaoqiang Liu et al. |
| 2025-05-26 | [Total-Editing: Head Avatar with Editable Appearance, Motion, and Lighting](https://arxiv.org/abs/2505.20582) | Yizhou Zhao, Chunjiang Liu, Haoyu Chen, Bhiksha Raj et al. |
| 2025-05-25 | [Revival with Voice: Multi-modal Controllable Text-to-Speech Synthesis](https://arxiv.org/abs/2505.18972) | Minsu Kim, Pingchuan Ma, Honglie Chen, Stavros Petridis, Maja Pantic |
| 2025-05-23 | [DualTalk: Dual-Speaker Interaction for 3D Talking Head Conversations](https://arxiv.org/abs/2505.18096) | Ziqiao Peng, Yanbo Fan, Haoyu Wu, Xuan Wang et al. |
| 2025-05-23 | [Watch and Listen: Understanding Audio-Visual-Speech Moments with Multimodal LLM](https://arxiv.org/abs/2505.18110) | Zinuo Li, Xian Zhang, Yongxin Guo, Mohammed Bennamoun et al. |
| 2025-05-10 | [VTutor: An Animated Pedagogical Agent SDK that Provide Real Time Multi-Model Feedback](https://arxiv.org/abs/2505.06676) | Eason Chen, Chenyu Lin, Yu-Kai Huang, Xinyi Tang et al. |
| 2025-05-08 | [OXSeg: Multidimensional attention UNet-based lip segmentation using semi-supervised lip contours](https://arxiv.org/abs/2505.05531) | Hanie Moghaddasi, Christina Chambers, Sarah N. Mattson, Jeffrey R. Wozniak et al. |
| 2025-05-03 | [OT-Talk: Animating 3D Talking Head with Optimal Transportation](https://arxiv.org/abs/2505.01932) | Xinmu Wang, Xiang Gao, Xiyun Song, Heather Yu et al. |
| 2025-05-03 | [GenSync: A Generalized Talking Head Framework for Audio-driven Multi-Subject Lip-Sync using 3D Gaussian Splatting](https://arxiv.org/abs/2505.01928) | Anushka Agarwal, Muhammad Yusuf Hassan, Talha Chafekar |
| 2025-05-02 | [FlowDubber: Movie Dubbing with LLM-based Semantic-aware Learning and Flow Matching based Voice Enhancing](https://arxiv.org/abs/2505.01263) | Gaoxiang Cong, Liang Li, Jiadong Pan, Zhedong Zhang et al. |
| 2025-05-02 | [Model See Model Do: Speech-Driven Facial Animation with Style Control](https://arxiv.org/abs/2505.01319) | Yifang Pan, Karan Singh, Luiz Gustavo Hafemann |
| 2025-05-01 | [KeySync: A Robust Approach for Leakage-free Lip Synchronization in High Resolution](https://arxiv.org/abs/2505.00497) | Antoni Bigata, Rodrigo Mira, Stella Bounareli, Michał Stypułkowski et al. |
| 2025-04-30 | [MagicPortrait: Temporally Consistent Face Reenactment with 3D Geometric Guidance](https://arxiv.org/abs/2504.21497) | Mengting Wei, Yante Li, Tuomas Varanka, Yan Jiang, Guoying Zhao |
| 2025-04-27 | [IM-Portrait: Learning 3D-aware Video Diffusion for Photorealistic Talking Heads from Monocular Videos](https://arxiv.org/abs/2504.19165) | Yuan Li, Ziqian Bai, Feitong Tan, Zhaopeng Cui et al. |
| 2025-04-26 | [Audio-Driven Talking Face Video Generation with Joint Uncertainty Learning](https://arxiv.org/abs/2504.18810) | Yifan Xie, Fei Ma, Yi Bin, Ying He, Fei Yu |
| 2025-04-25 | [Disentangle Identity, Cooperate Emotion: Correlation-Aware Emotional Talking Portrait Generation](https://arxiv.org/abs/2504.18087) | Weipeng Tan, Chuming Lin, Chengming Xu, FeiFan Xu et al. |
| 2025-04-18 | [Supervising 3D Talking Head Avatars with Analysis-by-Audio-Synthesis](https://arxiv.org/abs/2504.13386) | Radek Daněček, Carolin Schmitt, Senya Polikovsky, Michael J. Black |
| 2025-04-08 | [PASE: Phoneme-Aware Speech Encoder to Improve Lip Sync Accuracy for Talking Head Synthesis](https://arxiv.org/abs/2504.05803) | Yihuan Huang, Jiajun Liu, Yanzhen Ren, Jun Xue et al. |
| 2025-04-08 | [Contrastive Decoupled Representation Learning and Regularization for Speech-Preserving Facial Expression Manipulation](https://arxiv.org/abs/2504.05672) | Tianshui Chen, Jianman Lin, Zhijing Yang, Chumei Qing et al. |
| 2025-04-08 | [VideoSPatS: Video SPatiotemporal Splines for Disentangled Occlusion, Appearance and Motion Modeling and Editing](https://arxiv.org/abs/2504.07146) | Juan Luis Gonzalez Bello, Xu Yao, Alex Whelan, Kyle Olszewski et al. |
| 2025-04-08 | [Exploiting Temporal Audio-Visual Correlation Embedding for Audio-Driven One-Shot Talking Head Animation](https://arxiv.org/abs/2504.05746) | Zhihua Xu, Tianshui Chen, Zhijing Yang, Siyuan Peng et al. |
| 2025-04-06 | [FluentLip: A Phonemes-Based Two-stage Approach for Audio-Driven Lip Synthesis with Optical Flow Consistency](https://arxiv.org/abs/2504.04427) | Shiyan Liu, Rui Qu, Yan Jin |
| 2025-04-03 | [VoiceCraft-Dub: Automated Video Dubbing with Neural Codec Language Models](https://arxiv.org/abs/2504.02386) | Kim Sung-Bin, Jeongsoo Choi, Puyuan Peng, Joon Son Chung et al. |
| 2025-04-03 | [Audio-visual Controlled Video Diffusion with Masked Selective State Spaces Modeling for Natural Talking Head Generation](https://arxiv.org/abs/2504.02542) | Fa-Ting Hong, Zunnan Xu, Zixiang Zhou, Jun Zhou et al. |
| 2025-04-03 | [OmniTalker: One-shot Real-time Text-Driven Talking Audio-Video Generation With Multimodal Style Mimicking](https://arxiv.org/abs/2504.02433) | Zhongjian Wang, Peng Zhang, Jinwei Qi, Guangyuan Wang et al. |
| 2025-04-02 | [Detecting Lip-Syncing Deepfakes: Vision Temporal Transformer for Analyzing Mouth Inconsistencies](https://arxiv.org/abs/2504.01470) | Soumyya Kanti Datta, Shan Jia, Siwei Lyu |
| 2025-04-01 | [Monocular and Generalizable Gaussian Talking Head Animation](https://arxiv.org/abs/2504.00665) | Shengjie Gong, Haojie Li, Jiapeng Tang, Dongming Hu et al. |
| 2025-03-30 | [MoCha: Towards Movie-Grade Talking Character Synthesis](https://arxiv.org/abs/2503.23307) | Cong Wei, Bo Sun, Haoyu Ma, Ji Hou et al. |
| 2025-03-28 | [Audio-Plane: Audio Factorization Plane Gaussian Splatting for Real-Time Talking Head Synthesis](https://arxiv.org/abs/2503.22605) | Shuai Shen, Wanhua Li, Yunpeng Zhang, Yap-Peng Tan, Jiwen Lu |
| 2025-03-28 | [Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](https://arxiv.org/abs/2503.22225) | Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian, Jian Yang |
| 2025-03-27 | [ChatAnyone: Stylized Real-time Portrait Video Generation with Hierarchical Motion Diffusion Model](https://arxiv.org/abs/2503.21144) | Jinwei Qi, Chaonan Ji, Sheng Xu, Peng Zhang et al. |
| 2025-03-26 | [Perceptually Accurate 3D Talking Head Generation: New Definitions, Speech-Mesh Representation, and Evaluation Metrics](https://arxiv.org/abs/2503.20308) | Lee Chae-Yeon, Oh Hyun-Bin, Han EunGi, Kim Sung-Bin et al. |
| 2025-03-26 | [Dual Audio-Centric Modality Coupling for Talking Head Generation](https://arxiv.org/abs/2503.22728) | Ao Fu, Ziqi Ni, Yi Zhou |
| 2025-03-25 | [AudCast: Audio-Driven Human Video Generation by Cascaded Diffusion Transformers](https://arxiv.org/abs/2503.19824) | Jiazhi Guan, Kaisiyuan Wang, Zhiliang Xu, Quanwei Yang et al. |
| 2025-03-25 | [MVPortrait: Text-Guided Motion and Emotion Control for Multi-view Vivid Portrait Animation](https://arxiv.org/abs/2503.19383) | Yukang Lin, Hokit Fung, Jianjin Xu, Zeping Ren et al. |
| 2025-03-25 | [EmoHead: Emotional Talking Head via Manipulating Semantic Expression Parameters](https://arxiv.org/abs/2503.19416) | Xuli Shen, Hua Cai, Dingding Yu, Weilin Shen et al. |
| 2025-03-24 | [DisentTalk: Cross-lingual Talking Face Generation via Semantic Disentangled Diffusion Model](https://arxiv.org/abs/2503.19001) | Kangwei Liu, Junwu Liu, Yun Cao, Jinlin Guo, Xiaowei Yi |
| 2025-03-24 | [Teller: Real-Time Streaming Audio-Driven Portrait Animation with Autoregressive Motion Generation](https://arxiv.org/abs/2503.18429) | Dingcheng Zhen, Shunshun Yin, Shiyang Qin, Hou Yi et al. |
| 2025-03-23 | [DiffusionTalker: Efficient and Compact Speech-Driven 3D Talking Head via Personalizer-Guided Distillation](https://arxiv.org/abs/2503.18159) | Peng Chen, Xiaobao Wei, Ming Lu, Hui Chen, Feng Tian |
| 2025-03-21 | [Re-HOLD: Video Hand Object Interaction Reenactment via adaptive Layout-instructed Diffusion Model](https://arxiv.org/abs/2503.16942) | Yingying Fan, Quanwei Yang, Kaisiyuan Wang, Hang Zhou et al. |
| 2025-03-21 | [From Faces to Voices: Learning Hierarchical Representations for High-quality Video-to-Speech](https://arxiv.org/abs/2503.16956) | Ji-Hoon Kim, Jeongsoo Choi, Jaehun Kim, Chaeyoung Jung, Joon Son Chung |
| 2025-03-20 | [UniSync: A Unified Framework for Audio-Visual Synchronization](https://arxiv.org/abs/2503.16357) | Tao Feng, Yifan Xie, Xun Guan, Jiyuan Song et al. |
| 2025-03-18 | [PC-Talk: Precise Facial Animation Control for Audio-Driven Talking Face Generation](https://arxiv.org/abs/2503.14295) | Baiqin Wang, Xiangyu Zhu, Fan Shen, Hao Xu, Zhen Lei |
| 2025-03-17 | [Unlock Pose Diversity: Accurate and Efficient Implicit Keypoint-based Spatiotemporal Diffusion for Audio-driven Talking Portrait](https://arxiv.org/abs/2503.12963) | Chaolong Yang, Kai Yao, Yuyao Yan, Chenru Jiang et al. |
| 2025-03-17 | [SyncDiff: Diffusion-based Talking Head Synthesis with Bottlenecked Temporal Visual Prior for Improved Synchronization](https://arxiv.org/abs/2503.13371) | Xulin Fan, Heting Gao, Ziyi Chen, Peng Chang et al. |
| 2025-03-14 | [Cafe-Talk: Generating 3D Talking Face Animation with Multimodal Coarse- and Fine-grained Control](https://arxiv.org/abs/2503.14517) | Hejia Chen, Haoxian Zhang, Shoulong Zhang, Xiaoqiang Liu et al. |
| 2025-03-14 | [EmoDiffusion: Enhancing Emotional 3D Facial Animation with Latent Diffusion Models](https://arxiv.org/abs/2503.11028) | Yixuan Zhang, Qing Chang, Yuxi Wang, Guang Chen et al. |
| 2025-03-12 | [Bidirectional Learned Facial Animation Codec for Low Bitrate Talking Head Videos](https://arxiv.org/abs/2503.09787) | Riku Takahashi, Ryugo Morita, Fuma Kimishima, Kosuke Iwama, Jinjia Zhou |
| 2025-03-10 | [Versatile Multimodal Controls for Expressive Talking Human Animation](https://arxiv.org/abs/2503.08714) | Zheng Qin, Ruobing Zheng, Yabing Wang, Tianqi Li et al. |
| 2025-03-09 | [Removing Averaging: Personalized Lip-Sync Driven Characters Based on Identity Adapter](https://arxiv.org/abs/2503.06397) | Yanyu Zhu, Lichen Bai, Jintao Xu, Hai-tao Zheng |
| 2025-03-07 | [MagicInfinite: Generating Infinite Talking Videos with Your Words and Voice](https://arxiv.org/abs/2503.05978) | Hongwei Yi, Tian Ye, Shitong Shao, Xuancheng Yang et al. |
| 2025-03-06 | [FREAK: Frequency-modulated High-fidelity and Real-time Audio-driven Talking Portrait Synthesis](https://arxiv.org/abs/2503.04067) | Ziqi Ni, Ao Fu, Yi Zhou |
| 2025-03-03 | [KeyFace: Expressive Audio-Driven Facial Animation for Long Sequences via KeyFrame Interpolation](https://arxiv.org/abs/2503.01715) | Antoni Bigata, Michał Stypułkowski, Rodrigo Mira, Stella Bounareli et al. |
| 2025-02-28 | [Two-Stream Spatial-Temporal Transformer Framework for Person Identification via Natural Conversational Keypoints](https://arxiv.org/abs/2502.20803) | Masoumeh Chapariniya, Hossein Ranjbar, Teodora Vukovic, Sarah Ebling, Volker Dellwo |
| 2025-02-27 | [ARTalk: Speech-Driven 3D Head Animation via Autoregressive Model](https://arxiv.org/abs/2502.20323) | Xuangeng Chu, Nabarun Goswami, Ziteng Cui, Hanqin Wang, Tatsuya Harada |
| 2025-02-27 | [InsTaG: Learning Personalized 3D Talking Head from Few-Second Video](https://arxiv.org/abs/2502.20387) | Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng et al. |
| 2025-02-26 | [FLAP: Fully-controllable Audio-driven Portrait Video Generation through 3D head conditioned diffusion model](https://arxiv.org/abs/2502.19455) | Lingzhou Mu, Baiji Liu, Ruonan Zhang, Guiming Mo et al. |
| 2025-02-24 | [Dimitra: Audio-driven Diffusion model for Expressive Talking Head Generation](https://arxiv.org/abs/2502.17198) | Baptiste Chopin, Tashvik Dhamija, Pranav Balaji, Yaohui Wang, Antitza Dantcheva |
| 2025-02-20 | [NeRF-3DTalker: Neural Radiance Field with 3D Prior Aided Audio Disentanglement for Talking Head Synthesis](https://arxiv.org/abs/2502.14178) | Xiaoxing Liu, Zhilei Liu, Chongke Bi |
| 2025-02-17 | [SayAnything: Audio-Driven Lip Synchronization with Conditional Video Diffusion](https://arxiv.org/abs/2502.11515) | Junxian Ma, Shiwen Wang, Jian Yang, Junyi Hu et al. |
| 2025-02-13 | [Long-Term TalkingFace Generation via Motion-Prior Conditional Diffusion Model](https://arxiv.org/abs/2502.09533) | Fei Shen, Cong Wang, Junyao Gao, Qin Guo et al. |
| 2025-02-11 | [Playmate: Flexible Control of Portrait Animation via 3D-Implicit Space Guided Diffusion](https://arxiv.org/abs/2502.07203) | Xingpei Ma, Jiaran Cai, Yuansheng Guan, Shenneng Huang et al. |
| 2025-02-07 | [Towards Multimodal Empathetic Response Generation: A Rich Text-Speech-Vision Avatar-based Benchmark](https://arxiv.org/abs/2502.04976) | Han Zhang, Zixiang Meng, Meng Luo, Hong Han et al. |
| 2025-02-06 | [VTutor: An Open-Source SDK for Generative AI-Powered Animated Pedagogical Agents with Multi-Media Output](https://arxiv.org/abs/2502.04103) | Eason Chen, Chenyu Lin, Xinyi Tang, Aprille Xi et al. |
| 2025-02-02 | [EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](https://arxiv.org/abs/2502.00654) | Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond, Seungryul Baek |
| 2025-01-24 | [SyncAnimation: A Real-Time End-to-End Framework for Audio-Driven Human Pose and Talking Head Animation](https://arxiv.org/abs/2501.14646) | Yujian Liu, Shidang Xu, Jing Guo, Dingbin Wang et al. |
| 2025-01-23 | [Bridging The Multi-Modality Gaps of Audio, Visual and Linguistic for Speech Enhancement](https://arxiv.org/abs/2501.13375) | Meng-Ping Lin, Jen-Cheng Hou, Chia-Wei Chen, Shao-Yi Chien et al. |
| 2025-01-21 | [A Lightweight and Interpretable Deepfakes Detection Framework](https://arxiv.org/abs/2501.11927) | Muhammad Umar Farooq, Ali Javed, Khalid Mahmood Malik, Muhammad Anas Raza |
| 2025-01-18 | [EMO2: End-Effector Guided Audio-Driven Avatar Video Generation](https://arxiv.org/abs/2501.10687) | Linrui Tian, Siqi Hu, Qi Wang, Bang Zhang, Liefeng Bo |
| 2025-01-15 | [Joint Learning of Depth and Appearance for Portrait Image Animation](https://arxiv.org/abs/2501.08649) | Xinya Ji, Gaspard Zoss, Prashanth Chandran, Lingchen Yang et al. |
| 2025-01-14 | [Neural Speech Tracking in a Virtual Acoustic Environment: Audio-Visual Benefit for Unscripted Continuous Speech](https://arxiv.org/abs/2501.08124) | Mareike Daeglau, Juergen Otten, Giso Grimm, Bojana Mirkovic et al. |
| 2025-01-09 | [Towards Dynamic Neural Communication and Speech Neuroprosthesis Based on Viseme Decoding](https://arxiv.org/abs/2501.14790) | Ji-Ha Park, Seo-Hyun Lee, Soowon Kim, Seong-Whan Lee |
| 2025-01-08 | [Identity-Preserving Video Dubbing Using Motion Warping](https://arxiv.org/abs/2501.04586) | Runzhen Liu, Qinjie Lin, Yunfei Liu, Lijian Lin et al. |
| 2025-01-07 | [Generating and Detecting Various Types of Fake Image and Audio Content: A Review of Modern Deep Learning Technologies and Tools](https://arxiv.org/abs/2501.06227) | Arash Dehghani, Hossein Saberi |
| 2025-01-06 | [RDD4D: 4D Attention-Guided Road Damage Detection And Classification](https://arxiv.org/abs/2501.02822) | Asma Alkalbani, Muhammad Saqib, Ahmed Salim Alrawahi, Abbas Anwar et al. |
| 2025-01-03 | [MoEE: Mixture of Emotion Experts for Audio-Driven Portrait Animation](https://arxiv.org/abs/2501.01808) | Huaize Liu, Wenzhang Sun, Donglin Di, Shibo Sun et al. |
| 2025-01-03 | [JoyGen: Audio-Driven 3D Depth-Aware Talking-Face Video Editing](https://arxiv.org/abs/2501.01798) | Qili Wang, Dajiang Wu, Zihang Xu, Junshi Huang, Jun Lv |
| 2025-01-02 | [VideoAnydoor: High-fidelity Video Object Insertion with Precise Motion Control](https://arxiv.org/abs/2501.01427) | Yuanpeng Tu, Hao Luo, Xi Chen, Sihui Ji et al. |

### 2024

| Date | Title | Authors |
|------|-------|---------|
| 2024-12-28 | [DEGSTalk: Decomposed Per-Embedding Gaussian Fields for Hair-Preserving Talking Face Synthesis](https://arxiv.org/abs/2412.20148) | Kaijun Deng, Dezhi Zheng, Jindong Xie, Jinbao Wang et al. |
| 2024-12-26 | [UniAvatar: Taming Lifelike Audio-Driven Talking Head Generation with Comprehensive Motion and Lighting Control](https://arxiv.org/abs/2412.19860) | Wenzhang Sun, Xiang Li, Donglin Di, Zhuding Liang et al. |
| 2024-12-21 | [Improving Lip-synchrony in Direct Audio-Visual Speech-to-Speech Translation](https://arxiv.org/abs/2412.16530) | Lucas Goncalves, Prashant Mathur, Xing Niu, Brady Houston et al. |
| 2024-12-18 | [Real-time One-Step Diffusion-based Expressive Portrait Videos Generation](https://arxiv.org/abs/2412.13479) | Hanzhong Guo, Hongwei Yi, Daquan Zhou, Alexander William Bergman et al. |
| 2024-12-18 | [Joint Co-Speech Gesture and Expressive Talking Face Generation using Diffusion with Adapters](https://arxiv.org/abs/2412.14333) | Steven Hogue, Chenxu Zhang, Yapeng Tian, Xiaohu Guo |
| 2024-12-18 | [GLCF: A Global-Local Multimodal Coherence Analysis Framework for Talking Face Generation Detection](https://arxiv.org/abs/2412.13656) | Xiaocan Chen, Qilin Yin, Jiarui Liu, Wei Lu et al. |
| 2024-12-16 | [Towards a Universal Synthetic Video Detector: From Face or Background Manipulations to Fully AI-Generated Content](https://arxiv.org/abs/2412.12278) | Rohit Kundu, Hao Xiong, Vishal Mohanty, Athula Balachandran, Amit K. Roy-Chowdhury |
| 2024-12-13 | [VQTalker: Towards Multilingual Talking Avatars through Facial Motion Tokenization](https://arxiv.org/abs/2412.09892) | Tao Liu, Ziyang Ma, Qi Chen, Feilong Chen et al. |
| 2024-12-12 | [LatentSync: Taming Audio-Conditioned Latent Diffusion Models for Lip Sync with SyncNet Supervision](https://arxiv.org/abs/2412.09262) | Chunyu Li, Chao Zhang, Weikai Xu, Jingyu Lin et al. |
| 2024-12-12 | [EmoDubber: Towards High Quality and Emotion Controllable Movie Dubbing](https://arxiv.org/abs/2412.08988) | Gaoxiang Cong, Jiadong Pan, Liang Li, Yuankai Qi et al. |
| 2024-12-12 | [GoHD: Gaze-oriented and Highly Disentangled Portrait Animation with Rhythmic Poses and Realistic Expression](https://arxiv.org/abs/2412.09296) | Ziqi Zhou, Weize Quan, Hailin Shi, Wei Li et al. |
| 2024-12-11 | [PointTalk: Audio-Driven Dynamic Lip Point Cloud for 3D Gaussian-based Talking Head Synthesis](https://arxiv.org/abs/2412.08504) | Yifan Xie, Tao Feng, Xin Zhang, Xiangyang Luo et al. |
| 2024-12-10 | [PortraitTalk: Towards Customizable One-Shot Audio-to-Talking Face Generation](https://arxiv.org/abs/2412.07754) | Fatemeh Nazarieh, Zhenhua Feng, Diptesh Kanojia, Muhammad Awais, Josef Kittler |
| 2024-12-05 | [MEMO: Memory-Guided Diffusion for Expressive Talking Video Generation](https://arxiv.org/abs/2412.04448) | Longtao Zheng, Yifan Zhang, Hanzhong Guo, Jiachun Pan et al. |
| 2024-12-05 | [IF-MDM: Implicit Face Motion Diffusion Model for High-Fidelity Realtime Talking Head Generation](https://arxiv.org/abs/2412.04000) | Sejong Yang, Seoung Wug Oh, Yang Zhou, Seon Joo Kim |
| 2024-12-04 | [SINGER: Vivid Audio-driven Singing Video Generation with Multi-scale Spectral Diffusion Model](https://arxiv.org/abs/2412.03430) | Yan Li, Ziya Zhou, Zhiqiang Wang, Wei Xue et al. |
| 2024-12-03 | [When Words Smile: Generating Diverse Emotional Facial Expressions from Text](https://arxiv.org/abs/2412.02508) | Haidong Xu, Meishan Zhang, Hao Ju, Zhedong Zheng et al. |
| 2024-12-01 | [Synergizing Motion and Appearance: Multi-Scale Compensatory Codebooks for Talking Head Video Generation](https://arxiv.org/abs/2412.00719) | Shuling Zhao, Fa-Ting Hong, Xiaoshui Huang, Dan Xu |
| 2024-11-29 | [LokiTalk: Learning Fine-Grained and Generalizable Correspondences to Enhance NeRF-based Talking Head Synthesis](https://arxiv.org/abs/2411.19525) | Tianqi Li, Ruobing Zheng, Bonan Li, Zicheng Zhang et al. |
| 2024-11-29 | [Ditto: Motion-Space Diffusion for Controllable Realtime Talking Head Synthesis](https://arxiv.org/abs/2411.19509) | Tianqi Li, Ruobing Zheng, Minghui Yang, Jingdong Chen, Ming Yang |
| 2024-11-29 | [V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow](https://arxiv.org/abs/2411.19486) | Jeongsoo Choi, Ji-Hoon Kim, Jinyu Li, Joon Son Chung, Shujie Liu |
| 2024-11-25 | [Sonic: Shifting Focus to Global Audio Perception in Portrait Animation](https://arxiv.org/abs/2411.16331) | Xiaozhong Ji, Xiaobin Hu, Zhihong Xu, Junwei Zhu et al. |
| 2024-11-23 | [EmotiveTalk: Expressive Talking Head Generation through Audio Information Decoupling and Emotional Video Diffusion](https://arxiv.org/abs/2411.16726) | Haotian Wang, Yuzhe Weng, Yueyan Li, Zilu Guo et al. |
| 2024-11-23 | [ConsistentAvatar: Learning to Diffuse Fully Consistent Talking Head Avatar with Temporal Guidance](https://arxiv.org/abs/2411.15436) | Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian, Jian Yang |
| 2024-11-20 | [Comparative Analysis of Audio Feature Extraction for Real-Time Talking Portrait Synthesis](https://arxiv.org/abs/2411.13209) | Pegah Salehi, Sajad Amouei Sheshkal, Vajira Thambawita, Sushant Gautam et al. |
| 2024-11-14 | [LES-Talker: Fine-Grained Emotion Editing for Talking Head Generation in Linear Emotion Space](https://arxiv.org/abs/2411.09268) | Guanwen Feng, Zhihao Qian, Yunan Li, Siyu Jin et al. |
| 2024-11-12 | [SAV-SE: Scene-aware Audio-Visual Speech Enhancement with Selective State Space Model](https://arxiv.org/abs/2411.07751) | Xinyuan Qian, Jiaran Gao, Yaodan Zhang, Qiquan Zhang et al. |
| 2024-11-06 | [Large Generative Model-assisted Talking-face Semantic Communication System](https://arxiv.org/abs/2411.03876) | Feibo Jiang, Siwei Tu, Li Dong, Cunhua Pan et al. |
| 2024-10-31 | [Stereo-Talker: Audio-driven 3D Human Synthesis with Prior-Guided Mixture-of-Experts](https://arxiv.org/abs/2410.23836) | Xiang Deng, Youxin Pang, Xiaochen Zhao, Chao Xu et al. |
| 2024-10-29 | [Multimodal Semantic Communication for Generative Audio-Driven Video Conferencing](https://arxiv.org/abs/2410.22112) | Haonan Tong, Haopeng Li, Hongyang Du, Zhaohui Yang et al. |
| 2024-10-24 | [Real-time 3D-aware Portrait Video Relighting](https://arxiv.org/abs/2410.18355) | Ziqi Cai, Kaiwen Jiang, Shu-Yu Chen, Yu-Kun Lai et al. |
| 2024-10-18 | [Takin-ADA: Emotion Controllable Audio-Driven Animation with Canonical and Landmark Loss Optimization](https://arxiv.org/abs/2410.14283) | Bin Lin, Yanzhen Yu, Jianhao Ye, Ruitao Lv et al. |
| 2024-10-17 | [DAWN: Dynamic Frame Avatar with Non-autoregressive Diffusion Framework for Talking Head Video Generation](https://arxiv.org/abs/2410.13726) | Hanbo Cheng, Limin Lin, Chenyu Liu, Pengcheng Xia et al. |
| 2024-10-15 | [Titanic Calling: Low Bandwidth Video Conference from the Titanic Wreck](https://arxiv.org/abs/2410.11434) | Fevziye Irem Eyiokur, Christian Huber, Thai-Binh Nguyen, Tuan-Nam Nguyen et al. |
| 2024-10-14 | [Beyond Fixed Topologies: Unregistered Training and Comprehensive Evaluation Metrics for 3D Talking Heads](https://arxiv.org/abs/2410.11041) | Federico Nocentini, Thomas Besnier, Claudio Ferrari, Sylvain Arguillere et al. |
| 2024-10-14 | [MuseTalk: Real-Time High-Fidelity Video Dubbing via Spatio-Temporal Sampling](https://arxiv.org/abs/2410.10122) | Yue Zhang, Zhizhou Zhong, Minhao Liu, Zhaokang Chen et al. |
| 2024-10-14 | [Generative Human Video Compression with Multi-granularity Temporal Trajectory Factorization](https://arxiv.org/abs/2410.10171) | Shanzhi Yin, Bolin Chen, Shiqi Wang, Yan Ye |
| 2024-10-13 | [Tokenizing Motion: A Generative Approach for Scene Dynamics Compression](https://arxiv.org/abs/2410.09768) | Shanzhi Yin, Zihan Zhang, Bolin Chen, Shiqi Wang, Yan Ye |
| 2024-10-10 | [MMHead: Towards Fine-grained Multi-modal 3D Facial Animation](https://arxiv.org/abs/2410.07757) | Sijing Wu, Yunhao Li, Yichao Yan, Huiyu Duan et al. |
| 2024-10-09 | [MimicTalk: Mimicking a personalized and expressive 3D talking face in minutes](https://arxiv.org/abs/2410.06734) | Zhenhui Ye, Tianyun Zhong, Yi Ren, Ziyue Jiang et al. |
| 2024-10-07 | [EmoGene: Audio-Driven Emotional 3D Talking-Head Generation](https://arxiv.org/abs/2410.17262) | Wenqing Wang, Yun Fu |
| 2024-10-04 | [Diffusion-based Unsupervised Audio-visual Speech Enhancement](https://arxiv.org/abs/2410.05301) | Jean-Eudes Ayilo, Mostafa Sadeghi, Romain Serizel, Xavier Alameda-Pineda |
| 2024-10-01 | [Lipschitz-Driven Noise Robustness in VQ-AE for High-Frequency Texture Repair in ID-Specific Talking Heads](https://arxiv.org/abs/2410.00990) | Jian Yang, Xukun Wang, Wentao Wang, Guoming Li et al. |
| 2024-09-29 | [Learning Frame-Wise Emotion Intensity for Audio-Driven Talking-Head Generation](https://arxiv.org/abs/2409.19501) | Jingyi Xu, Hieu Le, Zhixin Shu, Yang Wang et al. |
| 2024-09-27 | [Diverse Code Query Learning for Speech-Driven Facial Animation](https://arxiv.org/abs/2409.19143) | Chunzhi Gu, Shigeru Kuriyama, Katsuya Hotta |
| 2024-09-26 | [Stable Video Portraits](https://arxiv.org/abs/2409.18083) | Mirela Ostrek, Justus Thies |
| 2024-09-23 | [DH-FaceVid-1K: A Large-Scale High-Quality Dataset for Face Video Generation](https://arxiv.org/abs/2410.07151) | Donglin Di, He Feng, Wenzhang Sun, Yongjia Ma et al. |
| 2024-09-22 | [Robust Audio-Visual Speech Enhancement: Correcting Misassignments in Complex Environments with Advanced Post-Processing](https://arxiv.org/abs/2409.14554) | Wenze Ren, Kuo-Hsuan Hung, Rong Chao, YouJin Li et al. |
| 2024-09-18 | [JEAN: Joint Expression and Audio-guided NeRF-based Talking Face Generation](https://arxiv.org/abs/2409.12156) | Sai Tanmay Reddy Chakkera, Aggelina Chatziagapi, Dimitris Samaras |
| 2024-09-16 | [DreamHead: Learning Spatial-Temporal Correspondence via Hierarchical Diffusion for Audio-driven Talking Head Synthesis](https://arxiv.org/abs/2409.10281) | Fa-Ting Hong, Yunfei Liu, Yu Li, Changyin Zhou et al. |
| 2024-09-14 | [StyleTalk++: A Unified Framework for Controlling the Speaking Styles of Talking Heads](https://arxiv.org/abs/2409.09292) | Suzhen Wang, Yifeng Ma, Yu Ding, Zhipeng Hu et al. |
| 2024-09-12 | [ProbTalk3D: Non-Deterministic Emotion Controllable Speech-Driven 3D Facial Animation Synthesis Using VQ-VAE](https://arxiv.org/abs/2409.07966) | Sichun Wu, Kazi Injamamul Haque, Zerrin Yumak |
| 2024-09-11 | [EMOdiffhead: Continuously Emotional Control in Talking Head Generation via Diffusion](https://arxiv.org/abs/2409.07255) | Jian Zhang, Weijian Mai, Zhijun Zhang |
| 2024-09-11 | [DiffTED: One-shot Audio-driven TED Talk Video Generation with Diffusion-based Co-speech Gestures](https://arxiv.org/abs/2409.07649) | Steven Hogue, Chenxu Zhang, Hamza Daruger, Yapeng Tian, Xiaohu Guo |
| 2024-09-09 | [PersonaTalk: Bring Attention to Your Persona in Visual Dubbing](https://arxiv.org/abs/2409.05379) | Longhao Zhang, Shuang Liang, Zhipeng Ge, Tianshu Hu |
| 2024-09-09 | [KAN-Based Fusion of Dual-Domain for Audio-Driven Facial Landmarks Generation](https://arxiv.org/abs/2409.05330) | Hoang-Son Vo-Thanh, Quang-Vinh Nguyen, Soo-Hyung Kim |
| 2024-09-05 | [SegTalker: Segmentation-based Talking Face Generation with Mask-guided Local Editing](https://arxiv.org/abs/2409.03605) | Lingyu Xiong, Xize Cheng, Jintao Tan, Xianjia Wu et al. |
| 2024-09-05 | [SVP: Style-Enhanced Vivid Portrait Talking Head Diffusion Model](https://arxiv.org/abs/2409.03270) | Weipeng Tan, Chuming Lin, Chengming Xu, Xiaozhong Ji et al. |
| 2024-09-04 | [PoseTalk: Text-and-Audio-based Pose Control and Motion Refinement for One-Shot Talking Head Generation](https://arxiv.org/abs/2409.02657) | Jun Ling, Yiwen Wang, Han Xue, Rong Xie, Li Song |
| 2024-09-03 | [LSTMSE-Net: Long Short Term Speech Enhancement Network for Audio-visual Speech Enhancement](https://arxiv.org/abs/2409.02266) | Arnav Jain, Jasmer Singh Sanjotra, Harshvardhan Choudhary, Krish Agrawal et al. |
| 2024-09-02 | [KMTalk: Speech-Driven 3D Facial Animation with Key Motion Embedding](https://arxiv.org/abs/2409.01113) | Zhihao Xu, Shengjie Gong, Jiapeng Tang, Lingyu Liang et al. |
| 2024-08-23 | [G3FA: Geometry-guided GAN for Face Animation](https://arxiv.org/abs/2408.13049) | Alireza Javanmardi, Alain Pagani, Didier Stricker |
| 2024-08-21 | [AutoDirector: Online Auto-scheduling Agents for Multi-sensory Composition](https://arxiv.org/abs/2408.11564) | Minheng Ni, Chenfei Wu, Huaying Yuan, Zhengyuan Yang et al. |
| 2024-08-21 | [EmoFace: Emotion-Content Disentangled Speech-Driven 3D Talking Face Animation](https://arxiv.org/abs/2408.11518) | Yihong Lin, Liang Peng, Zhaoxin Fan, Xianjia Wu et al. |
| 2024-08-20 | [DEGAS: Detailed Expressions on Full-Body Gaussian Avatars](https://arxiv.org/abs/2408.10588) | Zhijing Shao, Duotun Wang, Qing-Yao Tian, Yao-Dong Yang et al. |
| 2024-08-18 | [S^3D-NeRF: Single-Shot Speech-Driven Neural Radiance Field for High Fidelity Talking Head Synthesis](https://arxiv.org/abs/2408.09347) | Dongze Li, Kang Zhao, Wei Wang, Yifeng Ma et al. |
| 2024-08-18 | [FD2Talk: Towards Generalized Talking Head Generation with Facial Decoupled Diffusion Model](https://arxiv.org/abs/2408.09384) | Ziyu Yao, Xuxin Cheng, Zhiqi Huang |
| 2024-08-18 | [Meta-Learning Empowered Meta-Face: Personalized Speaking Style Adaptation for Audio-Driven 3D Talking Face Animation](https://arxiv.org/abs/2408.09357) | Xukun Zhou, Fengxin Li, Ziqiao Peng, Kejian Wu et al. |
| 2024-08-12 | [DEEPTalk: Dynamic Emotion Embedding for Probabilistic Speech-Driven 3D Face Animation](https://arxiv.org/abs/2408.06010) | Jisoo Kim, Jungbin Cho, Joonho Park, Soonmin Hwang et al. |
| 2024-08-10 | [High-fidelity and Lip-synced Talking Face Synthesis via Landmark-based Diffusion Model](https://arxiv.org/abs/2408.05416) | Weizhi Zhong, Junfan Lin, Peixin Chen, Liang Lin, Guanbin Li |
| 2024-08-10 | [Style-Preserving Lip Sync via Audio-Aware Style Reference](https://arxiv.org/abs/2408.05412) | Weizhi Zhong, Jichang Li, Yinqi Cai, Ming Li et al. |
| 2024-08-06 | [ReSyncer: Rewiring Style-based Generator for Unified Audio-Visually Synced Facial Performer](https://arxiv.org/abs/2408.03284) | Jiazhi Guan, Zhiliang Xu, Hang Zhou, Kaisiyuan Wang et al. |
| 2024-08-03 | [GLDiTalker: Speech-Driven 3D Facial Animation with Graph Latent Diffusion Transformer](https://arxiv.org/abs/2408.01826) | Yihong Lin, Zhaoxin Fan, Xianjia Wu, Lingyu Xiong et al. |
| 2024-08-03 | [JambaTalk: Speech-Driven 3D Talking Head Generation Based on Hybrid Transformer-Mamba Model](https://arxiv.org/abs/2408.01627) | Farzaneh Jafari, Stefano Berretti, Anup Basu |
| 2024-08-03 | [Landmark-guided Diffusion Model for High-fidelity and Temporally Coherent Talking Head Generation](https://arxiv.org/abs/2408.01732) | Jintao Tan, Xize Cheng, Lingyu Xiong, Lei Zhu et al. |
| 2024-08-01 | [EmoTalk3D: High-Fidelity Free-View Synthesis of Emotional 3D Talking Head](https://arxiv.org/abs/2408.00297) | Qianyun He, Xinya Ji, Yicheng Gong, Yuanxun Lu et al. |
| 2024-08-01 | [Reenact Anything: Semantic Video Motion Transfer Using Motion-Textual Inversion](https://arxiv.org/abs/2408.00458) | Manuel Kansy, Jacek Naruniec, Christopher Schroers, Markus Gross, Romann M. Weber |
| 2024-07-27 | [RAVSS: Robust Audio-Visual Speech Separation in Multi-Speaker Scenarios with Missing Visual Cues](https://arxiv.org/abs/2407.19224) | Tianrui Pan, Jie Liu, Bohan Wang, Jie Tang, Gangshan Wu |
| 2024-07-26 | [LinguaLinker: Audio-Driven Portraits Animation with Implicit Facial Control Enhancement](https://arxiv.org/abs/2407.18595) | Rui Zhang, Yixiao Fang, Zhengnan Lu, Pei Cheng et al. |
| 2024-07-22 | [PAV: Personalized Head Avatar from Unstructured Video Collection](https://arxiv.org/abs/2407.21047) | Akin Caliskan, Berkay Kicanaoglu, Hyeongwoo Kim |
| 2024-07-21 | [Anchored Diffusion for Video Face Reenactment](https://arxiv.org/abs/2407.15153) | Idan Kligvasser, Regev Cohen, George Leifman, Ehud Rivlin, Michael Elad |
| 2024-07-20 | [Text-based Talking Video Editing with Cascaded Conditional Diffusion](https://arxiv.org/abs/2407.14841) | Bo Han, Heqing Zou, Haoyang Li, Guangcong Wang, Chng Eng Siong |
| 2024-07-17 | [EmoFace: Audio-driven Emotional 3D Face Animation](https://arxiv.org/abs/2407.12501) | Chang Liu, Qunfen Lin, Zijiao Zeng, Ye Pan |
| 2024-07-13 | [Learning Online Scale Transformation for Talking Head Video Generation](https://arxiv.org/abs/2407.09965) | Fa-Ting Hong, Dan Xu |
| 2024-07-12 | [One-Shot Pose-Driving Face Animation Platform](https://arxiv.org/abs/2407.08949) | He Feng, Donglin Di, Yongjia Ma, Wei Chen, Tonghua Su |
| 2024-07-10 | [RT-LA-VocE: Real-Time Low-SNR Audio-Visual Speech Enhancement](https://arxiv.org/abs/2407.07825) | Honglie Chen, Rodrigo Mira, Stavros Petridis, Maja Pantic |
| 2024-07-08 | [Audio-driven High-resolution Seamless Talking Head Video Editing via StyleGAN](https://arxiv.org/abs/2407.05577) | Jiacheng Su, Kunhong Liu, Liyan Chen, Junfeng Yao et al. |
| 2024-07-01 | [Enhancing Speech-Driven 3D Facial Animation with Audio-Visual Guidance from Lip Reading Expert](https://arxiv.org/abs/2407.01034) | Han EunGi, Oh Hyun-Bin, Kim Sung-Bin, Corentin Nivelet Etcheberry et al. |
| 2024-06-26 | [RealTalk: Real-time and Realistic Audio-driven Face Generation with 3D Facial Prior-guided Identity Alignment Network](https://arxiv.org/abs/2406.18284) | Xiaozhong Ji, Chuming Lin, Zhonggan Ding, Ying Tai et al. |
| 2024-06-21 | [EmpathyEar: An Open-source Avatar Multimodal Empathetic Chatbot](https://arxiv.org/abs/2406.15177) | Hao Fei, Han Zhang, Bin Wang, Lizi Liao et al. |
| 2024-06-20 | [MultiTalk: Enhancing 3D Talking Head Generation Across Languages with Multilingual Video Dataset](https://arxiv.org/abs/2406.14272) | Kim Sung-Bin, Lee Chae-Yeon, Gihun Son, Oh Hyun-Bin et al. |
| 2024-06-17 | [NLDF: Neural Light Dynamic Fields for Efficient 3D Talking Head Generation](https://arxiv.org/abs/2406.11259) | Niu Guanchen |
| 2024-06-15 | [A Comprehensive Taxonomy and Analysis of Talking Head Synthesis: Techniques for Portrait Generation, Driving Mechanisms, and Editing](https://arxiv.org/abs/2406.10553) | Ming Meng, Yufei Zhao, Bo Zhang, Yonggui Zhu et al. |
| 2024-06-13 | [DubWise: Video-Guided Speech Duration Control in Multimodal LLM-based Text-to-Speech for Dubbing](https://arxiv.org/abs/2406.08802) | Neha Sahipjohn, Ashishkumar Gudmalwar, Nirmesh Shah, Pankaj Wasnik, Rajiv Ratn Shah |
| 2024-06-13 | [Hallo: Hierarchical Audio-Driven Visual Synthesis for Portrait Image Animation](https://arxiv.org/abs/2406.08801) | Mingwang Xu, Hui Li, Qingkun Su, Hanlin Shang et al. |
| 2024-06-13 | [Talking Heads: Understanding Inter-layer Communication in Transformer Language Models](https://arxiv.org/abs/2406.09519) | Jack Merullo, Carsten Eickhoff, Ellie Pavlick |
| 2024-06-13 | [FlowAVSE: Efficient Audio-Visual Speech Enhancement with Conditional Flow Matching](https://arxiv.org/abs/2406.09286) | Chaeyoung Jung, Suyeon Lee, Ji-Hoon Kim, Joon Son Chung |
| 2024-06-12 | [Make Your Actor Talk: Generalizable and High-Fidelity Lip Sync with Motion and Appearance Disentanglement](https://arxiv.org/abs/2406.08096) | Runyi Yu, Tianyu He, Ailing Zhang, Yuchi Wang et al. |
| 2024-06-12 | [Emotional Conversation: Empowering Talking Faces with Cohesive Expression, Gaze and Pose Generation](https://arxiv.org/abs/2406.07895) | Jiadong Liang, Feng Lu |
| 2024-06-12 | [Let's Go Real Talk: Spoken Dialogue Model for Face-to-Face Conversation](https://arxiv.org/abs/2406.07867) | Se Jin Park, Chae Won Kim, Hyeongseop Rha, Minsu Kim et al. |
| 2024-06-05 | [Controllable Talking Face Generation by Implicit Facial Keypoints Editing](https://arxiv.org/abs/2406.02880) | Dong Zhao, Jiaying Shi, Wenjun Li, Shudong Wang et al. |
| 2024-05-31 | [MunchSonic: Tracking Fine-grained Dietary Actions through Active Acoustic Sensing on Eyeglasses](https://arxiv.org/abs/2405.21004) | Saif Mahmud, Devansh Agarwal, Ashwin Ajit, Qikang Liang et al. |
| 2024-05-30 | [Audio2Rig: Artist-oriented deep learning tool for facial animation](https://arxiv.org/abs/2405.20412) | Bastien Arcelin, Nicolas Chaverou |
| 2024-05-24 | [InstructAvatar: Text-Guided Emotion and Motion Control for Avatar Generation](https://arxiv.org/abs/2405.15758) | Yuchi Wang, Junliang Guo, Jianhong Bai, Runyi Yu et al. |
| 2024-05-23 | [OpFlowTalker: Realistic and Natural Talking Face Generation via Optical Flow Guidance](https://arxiv.org/abs/2405.14709) | Shuheng Ge, Haoyu Xing, Li Zhang, Xiangqian Wu |
| 2024-05-21 | [Face Adapter for Pre-Trained Diffusion Models with Fine-Grained ID and Attribute Control](https://arxiv.org/abs/2405.12970) | Yue Han, Junwei Zhu, Keke He, Xu Chen et al. |
| 2024-05-16 | [Faces that Speak: Jointly Synthesising Talking Face and Speech from Text](https://arxiv.org/abs/2405.10272) | Youngjoon Jang, Ji-Hoon Kim, Junseok Ahn, Doyeop Kwak et al. |
| 2024-05-14 | [PolyGlotFake: A Novel Multilingual and Multimodal DeepFake Dataset](https://arxiv.org/abs/2405.08838) | Yang Hou, Haitao Fu, Chuankai Chen, Zida Li et al. |
| 2024-05-12 | [SPEAK: Speech-Driven Pose and Emotion-Adjustable Talking Head Generation](https://arxiv.org/abs/2405.07257) | Changpeng Cai, Guinan Guo, Jiao Li, Junhao Su et al. |
| 2024-05-09 | [SwapTalk: Audio-Driven Talking Face Generation with One-Shot Customization in Latent Space](https://arxiv.org/abs/2405.05636) | Zeren Zhang, Haibo Qin, Jiayu Huang, Yixin Li et al. |
| 2024-05-09 | [NeRFFaceSpeech: One-shot Audio-driven 3D Talking Head Synthesis via Generative Prior](https://arxiv.org/abs/2405.05749) | Gihoon Kim, Kwanggyoon Seo, Sihun Cha, Junyong Noh |
| 2024-05-07 | [Audio-Visual Speech Representation Expert for Enhanced Talking Face Video Generation and Evaluation](https://arxiv.org/abs/2405.04327) | Dogucan Yaman, Fevziye Irem Eyiokur, Leonard Bärmann, Seymanur Aktı et al. |
| 2024-05-06 | [AniTalker: Animate Vivid and Diverse Talking Faces through Identity-Decoupled Facial Motion Encoding](https://arxiv.org/abs/2405.03121) | Tao Liu, Feilong Chen, Shuai Fan, Chenpeng Du et al. |
| 2024-04-29 | [GSTalker: Real-time Audio-Driven Talking Face Generation via Deformable Gaussian Splatting](https://arxiv.org/abs/2404.19040) | Bo Chen, Shoukang Hu, Qi Chen, Chenpeng Du et al. |
| 2024-04-29 | [Audio-Visual Target Speaker Extraction with Reverse Selective Auditory Attention](https://arxiv.org/abs/2404.18501) | Ruijie Tao, Xinyuan Qian, Yidi Jiang, Junjie Li et al. |
| 2024-04-29 | [Embedded Representation Learning Network for Animating Styled Video Portrait](https://arxiv.org/abs/2404.19038) | Tianyong Wang, Xiangyu Liang, Wangguandong Zheng, Dan Niu et al. |
| 2024-04-24 | [GaussianTalker: Real-Time High-Fidelity Talking Head Synthesis with Audio-Driven 3D Gaussian Splatting](https://arxiv.org/abs/2404.16012) | Kyusun Cho, Joungbin Lee, Heeji Yoon, Yeobin Hong et al. |
| 2024-04-23 | [TalkingGaussian: Structure-Persistent 3D Talking Head Synthesis via Gaussian Splatting](https://arxiv.org/abs/2404.15264) | Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng et al. |
| 2024-04-22 | [GaussianTalker: Speaker-specific Talking Head Synthesis via 3D Gaussian Splatting](https://arxiv.org/abs/2404.14037) | Hongyun Yu, Zhan Qu, Qihang Yu, Jianchuan Chen et al. |
| 2024-04-16 | [VASA-1: Lifelike Audio-Driven Talking Faces Generated in Real Time](https://arxiv.org/abs/2404.10667) | Sicheng Xu, Guojun Chen, Yu-Xiao Guo, Jiaolong Yang et al. |
| 2024-04-15 | [FSRT: Facial Scene Representation Transformer for Face Reenactment from Factorized Appearance, Head-pose, and Facial Expression Features](https://arxiv.org/abs/2404.09736) | Andre Rochow, Max Schwarz, Sven Behnke |
| 2024-04-13 | [THQA: A Perceptual Quality Assessment Database for Talking Heads](https://arxiv.org/abs/2404.09003) | Yingjie Zhou, Zicheng Zhang, Wei Sun, Xiaohong Liu et al. |
| 2024-04-07 | [GvT: A Graph-based Vision Transformer with Talking-Heads Utilizing Sparsity, Trained from Scratch on Small Datasets](https://arxiv.org/abs/2404.04924) | Dongjing Shan, guiqiang chen |
| 2024-04-02 | [EDTalk: Efficient Disentanglement for Emotional Talking Head Synthesis](https://arxiv.org/abs/2404.01647) | Shuai Tan, Bin Ji, Mengxiao Bi, Ye Pan |
| 2024-03-29 | [Talk3D: High-Fidelity Talking Portrait Synthesis via Personalized 3D Generative Prior](https://arxiv.org/abs/2403.20153) | Jaehoon Ko, Kyusun Cho, Joungbin Lee, Heeji Yoon et al. |
| 2024-03-29 | [MI-NeRF: Learning a Single Face NeRF from Multiple Identities](https://arxiv.org/abs/2403.19920) | Aggelina Chatziagapi, Grigorios G. Chrysos, Dimitris Samaras |
| 2024-03-28 | [MoDiTalker: Motion-Disentangled Diffusion Model for High-Fidelity Talking Head Generation](https://arxiv.org/abs/2403.19144) | Seyeon Kim, Siyoon Jin, Jihye Park, Kihong Kim et al. |
| 2024-03-27 | [Robust Active Speaker Detection in Noisy Environments](https://arxiv.org/abs/2403.19002) | Siva Sai Nagender Vasireddy, Chenxu Zhang, Xiaohu Guo, Yapeng Tian |
| 2024-03-26 | [Superior and Pragmatic Talking Face Generation with Teacher-Student Framework](https://arxiv.org/abs/2403.17883) | Chao Liang, Jianwen Jiang, Tianyun Zhong, Gaojie Lin et al. |
| 2024-03-26 | [Deepfake Generation and Detection: A Benchmark and Survey](https://arxiv.org/abs/2403.17881) | Gan Pei, Jiangning Zhang, Menghan Hu, Zhenyu Zhang et al. |
| 2024-03-26 | [AniPortrait: Audio-Driven Synthesis of Photorealistic Portrait Animation](https://arxiv.org/abs/2403.17694) | Huawei Wei, Zejun Yang, Zhisheng Wang |
| 2024-03-25 | [Make-Your-Anchor: A Diffusion-based 2D Avatar Generation Framework](https://arxiv.org/abs/2403.16510) | Ziyao Huang, Fan Tang, Yong Zhang, Xiaodong Cun et al. |
| 2024-03-25 | [DiffusionAct: Controllable Diffusion Autoencoder for One-shot Face Reenactment](https://arxiv.org/abs/2403.17217) | Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras, Georgios Tzimiropoulos |
| 2024-03-23 | [Adaptive Super Resolution For One-Shot Talking-Head Generation](https://arxiv.org/abs/2403.15944) | Luchuan Song, Pinxin Liu, Guojun Yin, Chenliang Xu |
| 2024-03-19 | [EmoVOCA: Speech-Driven Emotional 3D Talking Heads](https://arxiv.org/abs/2403.12886) | Federico Nocentini, Claudio Ferrari, Stefano Berretti |
| 2024-03-16 | [ScanTalk: 3D Talking Heads from Unregistered Scans](https://arxiv.org/abs/2403.10942) | Federico Nocentini, Thomas Besnier, Claudio Ferrari, Sylvain Arguillere et al. |
| 2024-03-11 | [FlowVQTalker: High-Quality Emotional Talking Face Generation through Normalizing Flow and Quantization](https://arxiv.org/abs/2403.06375) | Shuai Tan, Bin Ji, Ye Pan |
| 2024-03-11 | [Style2Talker: High-Resolution Talking Head Generation with Emotion Style and Art Style](https://arxiv.org/abs/2403.06365) | Shuai Tan, Bin Ji, Ye Pan |
| 2024-03-11 | [Say Anything with Any Style](https://arxiv.org/abs/2403.06363) | Shuai Tan, Bin Ji, Yu Ding, Ye Pan |
| 2024-03-11 | [A Comparative Study of Perceptual Quality Metrics for Audio-driven Talking Head Videos](https://arxiv.org/abs/2403.06421) | Weixia Zhang, Chengguang Zhu, Jingnan Gao, Yichao Yan et al. |
| 2024-03-04 | [FaceChain-ImagineID: Freely Crafting High-Fidelity Diverse Talking Faces from Disentangled Audio](https://arxiv.org/abs/2403.01901) | Chao Xu, Yang Liu, Jiazheng Xing, Weida Wang et al. |
| 2024-02-28 | [G4G:A Generic Framework for High Fidelity Talking Face Generation with Fine-grained Intra-modal Alignment](https://arxiv.org/abs/2402.18122) | Juan Zhang, Jiahao Chen, Cheng Wang, Zhiwang Yu et al. |
| 2024-02-28 | [Context-aware Talking Face Video Generation](https://arxiv.org/abs/2402.18092) | Meidai Xuanyuan, Yuwang Wang, Honglei Guo, Qionghai Dai |
| 2024-02-27 | [Learning Dynamic Tetrahedra for High-Quality Talking Head Synthesis](https://arxiv.org/abs/2402.17364) | Zicheng Zhang, Ruobing Zheng, Ziwen Liu, Congying Han et al. |
| 2024-02-27 | [EMO: Emote Portrait Alive -- Generating Expressive Portrait Videos with Audio2Video Diffusion Model under Weak Conditions](https://arxiv.org/abs/2402.17485) | Linrui Tian, Qi Wang, Bang Zhang, Liefeng Bo |
| 2024-02-26 | [Resolution-Agnostic Neural Compression for High-Fidelity Portrait Video Conferencing via Implicit Radiance Fields](https://arxiv.org/abs/2402.16599) | Yifei Li, Xiaohong Liu, Yicong Peng, Guangtao Zhai, Jun Zhou |
| 2024-02-26 | [Audio-Visual Speech Enhancement in Noisy Environments via Emotion-Based Contextual Cues](https://arxiv.org/abs/2402.16394) | Tassadaq Hussain, Kia Dashtipour, Yu Tsao, Amir Hussain |
| 2024-02-25 | [AVI-Talking: Learning Audio-Visual Instructions for Expressive 3D Talking Face Generation](https://arxiv.org/abs/2402.16124) | Yasheng Sun, Wenqing Chu, Hang Zhou, Kaisiyuan Wang, Hideki Koike |
| 2024-02-20 | [StyleDubber: Towards Multi-Scale Style Learning for Movie Dubbing](https://arxiv.org/abs/2402.12636) | Gaoxiang Cong, Yuankai Qi, Liang Li, Amin Beheshti et al. |
| 2024-02-20 | [AnnoTheia: A Semi-Automatic Annotation Toolkit for Audio-Visual Speech Technologies](https://arxiv.org/abs/2402.13152) | José-M. Acosta-Triana, David Gimeno-Gómez, Carlos-D. Martínez-Hinarejos |
| 2024-02-08 | [DiffSpeaker: Speech-Driven 3D Facial Animation with Diffusion Transformer](https://arxiv.org/abs/2402.05712) | Zhiyuan Ma, Xiangyu Zhu, Guojun Qi, Chen Qian et al. |
| 2024-02-05 | [One-shot Neural Face Reenactment via Finding Directions in GAN's Latent Space](https://arxiv.org/abs/2402.03553) | Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras, Georgios Tzimiropoulos |
| 2024-02-02 | [EmoSpeaker: One-shot Fine-grained Emotion-Controlled Talking Face Generation](https://arxiv.org/abs/2402.01422) | Guanwen Feng, Haoran Cheng, Yunan Li, Zhiyuan Ma et al. |
| 2024-01-28 | [Lips Are Lying: Spotting the Temporal Inconsistency between Audio and Visual in Lip-Syncing DeepFakes](https://arxiv.org/abs/2401.15668) | Weifeng Liu, Tianyi She, Jiawei Liu, Boheng Li et al. |
| 2024-01-23 | [NeRF-AD: Neural Radiance Field with Attention-based Disentanglement for Talking Face Synthesis](https://arxiv.org/abs/2401.12568) | Chongke Bi, Xiaoxing Liu, Zhilei Liu |
| 2024-01-18 | [Exposing Lip-syncing Deepfakes from Mouth Inconsistencies](https://arxiv.org/abs/2401.10113) | Soumyya Kanti Datta, Shan Jia, Siwei Lyu |
| 2024-01-16 | [Real3D-Portrait: One-shot Realistic 3D Talking Portrait Synthesis](https://arxiv.org/abs/2401.08503) | Zhenhui Ye, Tianyun Zhong, Yi Ren, Jiaqi Yang et al. |
| 2024-01-16 | [EmoTalker: Emotionally Editable Talking Face Generation via Diffusion Model](https://arxiv.org/abs/2401.08049) | Bingyuan Zhang, Xulong Zhang, Ning Cheng, Jun Yu et al. |
| 2024-01-09 | [Jump Cut Smoothing for Talking Heads](https://arxiv.org/abs/2401.04718) | Xiaojuan Wang, Taesung Park, Yang Zhou, Eli Shechtman, Richard Zhang |
| 2024-01-02 | [Towards a Simultaneous and Granular Identity-Expression Control in Personalized Face Generation](https://arxiv.org/abs/2401.01207) | Renshuai Liu, Bowen Ma, Wei Zhang, Zhipeng Hu et al. |

### 2023

| Date | Title | Authors |
|------|-------|---------|
| 2023-12-28 | [EFHQ: Multi-purpose ExtremePose-Face-HQ dataset](https://arxiv.org/abs/2312.17205) | Trung Tuan Dao, Duc Hong Vu, Cuong Pham, Anh Tran |
| 2023-12-25 | [SAiD: Speech-driven Blendshape Facial Animation with Diffusion](https://arxiv.org/abs/2401.08655) | Inkyu Park, Jaewoong Cho |
| 2023-12-23 | [TransFace: Unit-Based Audio-Visual Speech Synthesizer for Talking Head Translation](https://arxiv.org/abs/2312.15197) | Xize Cheng, Rongjie Huang, Linjun Li, Tao Jin et al. |
| 2023-12-21 | [DREAM-Talk: Diffusion-based Realistic Emotional Audio-driven Method for Single Image Talking Face Generation](https://arxiv.org/abs/2312.13578) | Chenxu Zhang, Chao Wang, Jianfeng Zhang, Hongyi Xu et al. |
| 2023-12-18 | [AE-NeRF: Audio Enhanced Neural Radiance Field for Few Shot Talking Head Synthesis](https://arxiv.org/abs/2312.10921) | Dongze Li, Kang Zhao, Wei Wang, Bo Peng et al. |
| 2023-12-18 | [Mimic: Speaking Style Disentanglement for Speech-Driven 3D Facial Animation](https://arxiv.org/abs/2312.10877) | Hui Fu, Zeqing Wang, Ke Gong, Keze Wang et al. |
| 2023-12-18 | [VectorTalker: SVG Talking Face Generation with Progressive Vectorisation](https://arxiv.org/abs/2312.11568) | Hao Hu, Xuan Wang, Jingxiang Sun, Yanbo Fan et al. |
| 2023-12-17 | [MM-TTS: Multi-modal Prompt based Style Transfer for Expressive Text-to-Speech Synthesis](https://arxiv.org/abs/2312.10687) | Wenhao Guan, Yishuang Li, Tao Li, Hukai Huang et al. |
| 2023-12-16 | [Learning Dense Correspondence for NeRF-Based Face Reenactment](https://arxiv.org/abs/2312.10422) | Songlin Yang, Wei Wang, Yushi Lan, Xiangyu Fan et al. |
| 2023-12-15 | [DreamTalk: When Emotional Talking Head Generation Meets Diffusion Probabilistic Models](https://arxiv.org/abs/2312.09767) | Yifeng Ma, Shiwei Zhang, Jiayu Wang, Xiang Wang et al. |
| 2023-12-12 | [GMTalker: Gaussian Mixture-based Audio-Driven Emotional Talking Video Portraits](https://arxiv.org/abs/2312.07669) | Yibo Xia, Lizhen Wang, Xiang Deng, Xiaoyan Luo et al. |
| 2023-12-12 | [GSmoothFace: Generalized Smooth Talking Face Generation via Fine Grained 3D Face Guidance](https://arxiv.org/abs/2312.07385) | Haiming Zhang, Zhihao Yuan, Chaoda Zheng, Xu Yan et al. |
| 2023-12-11 | [Neural Text to Articulate Talk: Deep Text to Audiovisual Speech Synthesis achieving both Auditory and Photo-realism](https://arxiv.org/abs/2312.06613) | Georgios Milis, Panagiotis P. Filntisis, Anastasios Roussos, Petros Maragos |
| 2023-12-11 | [DiT-Head: High-Resolution Talking Head Synthesis using Diffusion Transformers](https://arxiv.org/abs/2312.06400) | Aaron Mir, Eduardo Alonso, Esther Mondragón |
| 2023-12-09 | [R2-Talker: Realistic Real-Time Talking Head Synthesis with Hash Grid Landmarks Encoding and Progressive Multilayer Conditioning](https://arxiv.org/abs/2312.05572) | Zhiling Ye, LiangGuo Zhang, Dingheng Zeng, Quan Lu, Ning Jiang |
| 2023-12-09 | [FT2TF: First-Person Statement Text-To-Talking Face Generation](https://arxiv.org/abs/2312.05430) | Xingjian Diao, Ming Cheng, Wayner Barrios, SouYoung Jin |
| 2023-12-07 | [SingingHead: A Large-scale 4D Dataset for Singing Head Animation](https://arxiv.org/abs/2312.04369) | Sijing Wu, Yunhao Li, Weitian Zhang, Jun Jia et al. |
| 2023-12-05 | [MyPortrait: Morphable Prior-Guided Personalized Portrait Generation](https://arxiv.org/abs/2312.02703) | Bo Ding, Zhenfeng Fan, Shuang Yang, Shihong Xia |
| 2023-12-05 | [AV2AV: Direct Audio-Visual Speech to Audio-Visual Speech Translation with Unified Audio-Visual Speech Representation](https://arxiv.org/abs/2312.02512) | Jeongsoo Choi, Se Jin Park, Minsu Kim, Yong Man Ro |
| 2023-12-04 | [VividTalk: One-Shot Audio-Driven Talking Head Generation Based on 3D Hybrid Prior](https://arxiv.org/abs/2312.01841) | Xusen Sun, Longhao Zhang, Hao Zhu, Peng Zhang et al. |
| 2023-11-29 | [SyncTalk: The Devil is in the Synchronization for Talking Head Synthesis](https://arxiv.org/abs/2311.17590) | Ziqiao Peng, Wentao Hu, Yue Shi, Xiangyu Zhu et al. |
| 2023-11-29 | [Talking Head(?) Anime from a Single Image 4: Improved Model and Its Distillation](https://arxiv.org/abs/2311.17409) | Pramook Khungurn |
| 2023-11-28 | [THInImg: Cross-modal Steganography for Presenting Talking Heads in Images](https://arxiv.org/abs/2311.17177) | Lin Zhao, Hongxuan Li, Xuefei Ning, Xinru Jiang |
| 2023-11-26 | [GAIA: Zero-shot Talking Avatar Generation](https://arxiv.org/abs/2311.15230) | Tianyu He, Junliang Guo, Runyi Yu, Yuchi Wang et al. |
| 2023-11-24 | [Cooperative Dual Attention for Audio-Visual Speech Enhancement with Facial Cues](https://arxiv.org/abs/2311.14275) | Feixiang Wang, Shuang Yang, Shiguang Shan, Xilin Chen |
| 2023-11-20 | [MemoryCompanion: A Smart Healthcare Solution to Empower Efficient Alzheimer's Care Via Unleashing Generative AI](https://arxiv.org/abs/2311.14730) | Lifei Zheng, Yeonie Heo, Yi Fang |
| 2023-11-15 | [CP-EB: Talking Face Generation with Controllable Pose and Eye Blinking Embedding](https://arxiv.org/abs/2311.08673) | Jianzong Wang, Yimin Deng, Ziqi Liang, Xulong Zhang et al. |
| 2023-11-12 | [ChatAnything: Facetime Chat with LLM-Enhanced Personas](https://arxiv.org/abs/2311.06772) | Yilin Zhao, Xinbin Yuan, Shanghua Gao, Zhijie Lin et al. |
| 2023-11-09 | [BakedAvatar: Baking Neural Fields for Real-Time Head Avatar Synthesis](https://arxiv.org/abs/2311.05521) | Hao-Bin Duan, Miao Wang, Jin-Chuan Shi, Xu-Chuan Chen, Yan-Pei Cao |
| 2023-11-08 | [Synthetic Speaking Children -- Why We Need Them and How to Make Them](https://arxiv.org/abs/2311.06307) | Muhammad Ali Farooq, Dan Bigioi, Rishabh Jain, Wang Yao et al. |
| 2023-11-05 | [AV-Lip-Sync+: Leveraging AV-HuBERT to Exploit Multimodal Inconsistency for Deepfake Detection of Frontal Face Videos](https://arxiv.org/abs/2311.02733) | Sahibzada Adil Shahzad, Ammarah Hashmi, Yan-Tsung Peng, Yu Tsao, Hsin-Min Wang |
| 2023-11-05 | [3D-Aware Talking-Head Video Motion Transfer](https://arxiv.org/abs/2311.02549) | Haomiao Ni, Jiachen Liu, Yuan Xue, Sharon X. Huang |
| 2023-11-03 | [DiffDub: Person-generic Visual Dubbing Using Inpainting Renderer with Diffusion Auto-encoder](https://arxiv.org/abs/2311.01811) | Tao Liu, Chenpeng Du, Shuai Fan, Feilong Chen, Kai Yu |
| 2023-11-02 | [LaughTalk: Expressive 3D Talking Head Generation with Laughter](https://arxiv.org/abs/2311.00994) | Kim Sung-Bin, Lee Hyun, Da Hye Hong, Suekyeong Nam et al. |
| 2023-10-30 | [Scenario-Aware Audio-Visual TF-GridNet for Target Speech Extraction](https://arxiv.org/abs/2310.19644) | Zexu Pan, Gordon Wichern, Yoshiki Masuyama, Francois G. Germain et al. |
| 2023-10-30 | [Seeing Through the Conversation: Audio-Visual Speech Separation based on Diffusion Model](https://arxiv.org/abs/2310.19581) | Suyeon Lee, Chaeyoung Jung, Youngjoon Jang, Jaehun Kim, Joon Son Chung |
| 2023-10-23 | [Learning Through AI-Clones: Enhancing Self-Perception and Presentation Performance](https://arxiv.org/abs/2310.15112) | Qingxiao Zheng, Zhuoer Chen, Yun Huang |
| 2023-10-17 | [CorrTalk: Correlation Between Hierarchical Speech and Facial Activity Variances for 3D Animation](https://arxiv.org/abs/2310.11295) | Zhaojie Chu, Kailing Guo, Xiaofen Xing, Yilin Lan et al. |
| 2023-10-09 | [HyperLips: Hyper Control Lips with High Resolution Decoder for Talking Face Generation](https://arxiv.org/abs/2310.05720) | Yaosen Chen, Yu Yao, Zhiqiang Li, Wei Wang et al. |
| 2023-10-08 | [GestSync: Determining who is speaking without a talking head](https://arxiv.org/abs/2310.05304) | Sindhu B Hegde, Andrew Zisserman |
| 2023-10-08 | [Learning Separable Hidden Unit Contributions for Speaker-Adaptive Lip-Reading](https://arxiv.org/abs/2310.05058) | Songtao Luo, Shuang Yang, Shiguang Shan, Xilin Chen |
| 2023-10-04 | [uTalk: Bridging the Gap Between Humans and AI](https://arxiv.org/abs/2310.02739) | Hussam Azzuni, Sharim Jamal, Abdulmotaleb Elsaddik |
| 2023-09-30 | [DiffPoseTalk: Speech-Driven Stylistic 3D Facial Animation and Head Pose Generation via Diffusion Models](https://arxiv.org/abs/2310.00434) | Zhiyao Sun, Tian Lv, Sheng Ye, Matthieu Lin et al. |
| 2023-09-28 | [OSM-Net: One-to-Many One-shot Talking Head Generation with Spontaneous Head Motions](https://arxiv.org/abs/2309.16148) | Jin Liu, Xi Wang, Xiaomeng Fu, Yesheng Chai et al. |
| 2023-09-20 | [Deep Complex U-Net with Conformer for Audio-Visual Speech Enhancement](https://arxiv.org/abs/2309.11059) | Shafique Ahmed, Chia-Wei Chen, Wenze Ren, Chin-Jou Li et al. |
| 2023-09-15 | [Audio-Visual Active Speaker Extraction for Sparsely Overlapped Multi-talker Speech](https://arxiv.org/abs/2309.08408) | Junjie Li, Ruijie Tao, Zexu Pan, Meng Ge et al. |
| 2023-09-14 | [HDTR-Net: A Real-Time High-Definition Teeth Restoration Network for Arbitrary Talking Face Generation Methods](https://arxiv.org/abs/2309.07495) | Yongyuan Li, Xiuyuan Qin, Chao Liang, Mingqiang Wei |
| 2023-09-14 | [DT-NeRF: Decomposed Triplane-Hash Neural Radiance Fields for High-Fidelity Talking Portrait Synthesis](https://arxiv.org/abs/2309.07752) | Yaoyu Su, Shaohui Wang, Haoqian Wang |
| 2023-09-14 | [DiffTalker: Co-driven audio-image diffusion for talking faces via intermediate landmarks](https://arxiv.org/abs/2309.07509) | Zipeng Qi, Xulong Zhang, Ning Cheng, Jing Xiao, Jianzong Wang |
| 2023-09-14 | [AV2Wav: Diffusion-Based Re-synthesis from Continuous Self-supervised Features for Audio-Visual Speech Enhancement](https://arxiv.org/abs/2309.08030) | Ju-Chieh Chou, Chung-Ming Chien, Karen Livescu |
| 2023-09-13 | [PIAVE: A Pose-Invariant Audio-Visual Speaker Extraction Network](https://arxiv.org/abs/2309.06723) | Qinghua Liu, Meng Ge, Zhizheng Wu, Haizhou Li |
| 2023-09-12 | [DF-TransFusion: Multimodal Deepfake Detection via Lip-Audio Cross-Attention and Facial Self-Attention](https://arxiv.org/abs/2309.06511) | Aaditya Kharel, Manas Paranjape, Aniket Bera |
| 2023-09-10 | [Efficient Emotional Adaptation for Audio-Driven Talking-Head Generation](https://arxiv.org/abs/2309.04946) | Yuan Gan, Zongxin Yang, Xihang Yue, Lingyun Sun, Yi Yang |
| 2023-09-10 | [MaskRenderer: 3D-Infused Multi-Mask Realistic Face Reenactment](https://arxiv.org/abs/2309.05095) | Tina Behrouzi, Atefeh Shahroudnejad, Payam Mousavi |
| 2023-09-05 | [RADIO: Reference-Agnostic Dubbing Video Synthesis](https://arxiv.org/abs/2309.01950) | Dongyeun Lee, Chaewon Kim, Sangjoon Yu, Jaejun Yoo, Gyeong-Moon Park |
| 2023-08-30 | [From Pixels to Portraits: A Comprehensive Survey of Talking Head Generation Techniques and Applications](https://arxiv.org/abs/2308.16041) | Shreyank N Gowda, Dheeraj Pandey, Shashank Narayana Gowda |
| 2023-08-28 | [FaceChain: A Playground for Human-centric Artificial Intelligence Generated Content](https://arxiv.org/abs/2308.14256) | Yang Liu, Cheng Yu, Lei Shang, Yongyi He et al. |
| 2023-08-24 | [ToonTalker: Cross-Domain Face Reenactment](https://arxiv.org/abs/2308.12866) | Yuan Gong, Yong Zhang, Xiaodong Cun, Fei Yin et al. |
| 2023-08-18 | [Diff2Lip: Audio Conditioned Diffusion Models for Lip-Synchronization](https://arxiv.org/abs/2308.09716) | Soumik Mukhopadhyay, Saksham Suri, Ravi Teja Gadde, Abhinav Shrivastava |
| 2023-08-17 | [A Survey on Deep Multi-modal Learning for Body Language Recognition and Generation](https://arxiv.org/abs/2308.08849) | Li Liu, Lufei Gao, Wentao Lei, Fengji Ma et al. |
| 2023-08-16 | [IIANet: An Intra- and Inter-Modality Attention Network for Audio-Visual Speech Separation](https://arxiv.org/abs/2308.08143) | Kai Li, Runxuan Yang, Fuchun Sun, Xiaolin Hu |
| 2023-08-12 | [Text-to-Video: a Two-stage Framework for Zero-shot Identity-agnostic Talking-head Generation](https://arxiv.org/abs/2308.06457) | Zhichao Wang, Mengyu Dai, Keld Lundgaard |
| 2023-08-09 | [VAST: Vivify Your Talking Avatar via Zero-Shot Expressive Facial Style Transfer](https://arxiv.org/abs/2308.04830) | Liyang Chen, Zhiyong Wu, Runnan Li, Weihong Bao et al. |
| 2023-08-01 | [Context-Aware Talking-Head Video Editing](https://arxiv.org/abs/2308.00462) | Songlin Yang, Wei Wang, Jun Ling, Bo Peng et al. |
| 2023-07-20 | [HyperReenact: One-Shot Reenactment via Jointly Learning to Refine and Retarget Faces](https://arxiv.org/abs/2307.10797) | Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras, Georgios Tzimiropoulos |
| 2023-07-19 | [MODA: Mapping-Once Audio-driven Portrait Animation with Dual Attentions](https://arxiv.org/abs/2307.10008) | Yunfei Liu, Lijian Lin, Fei Yu, Changyin Zhou, Yu Li |
| 2023-07-19 | [Implicit Identity Representation Conditioned Memory Compensation Network for Talking Head video Generation](https://arxiv.org/abs/2307.09906) | Fa-Ting Hong, Dan Xu |
| 2023-07-19 | [Hierarchical Semantic Perceptual Listener Head Video Generation: A High-performance Pipeline](https://arxiv.org/abs/2307.09821) | Zhigang Chang, Weitai Hu, Qing Yang, Shibao Zheng |
| 2023-07-18 | [FACTS: Facial Animation Creation using the Transfer of Styles](https://arxiv.org/abs/2307.09480) | Jack Saunders, Steven Caulkin, Vinay Namboodiri |
| 2023-07-18 | [Audio-driven Talking Face Generation with Stabilized Synchronization Loss](https://arxiv.org/abs/2307.09368) | Dogucan Yaman, Fevziye Irem Eyiokur, Leonard Bärmann, Hazim Kemal Ekenel, Alexander Waibel |
| 2023-07-18 | [Efficient Region-Aware Neural Radiance Fields for High-Fidelity Talking Portrait Synthesis](https://arxiv.org/abs/2307.09323) | Jiahe Li, Jiawei Zhang, Xiao Bai, Jun Zhou, Lin Gu |
| 2023-07-18 | [OPHAvatars: One-shot Photo-realistic Head Avatars](https://arxiv.org/abs/2307.09153) | Shaoxu Li |
| 2023-07-15 | [Leveraging Self-Supervised Audio-Visual Pretrained Models to Improve Vocoded Speech Intelligibility in Cochlear Implant Simulation](https://arxiv.org/abs/2307.07748) | Richard Lee Lai, Jen-Cheng Hou, I-Chun Chern, Kuo-Hsuan Hung et al. |
| 2023-07-11 | [On the Vulnerability of DeepFake Detectors to Attacks Generated by Denoising Diffusion Models](https://arxiv.org/abs/2307.05397) | Marija Ivanovska, Vitomir Štruc |
| 2023-07-09 | [Predictive Coding For Animation-Based Video Compression](https://arxiv.org/abs/2307.04187) | Goluck Konuko, Stéphane Lathuilière, Giuseppe Valenzise |
| 2023-07-08 | [FTFDNet: Learning to Detect Talking Face Video Manipulation with Tri-Modality Interaction](https://arxiv.org/abs/2307.03990) | Ganglai Wang, Peng Zhang, Junwen Xiong, Feihan Yang et al. |
| 2023-07-05 | [Interactive Conversational Head Generation](https://arxiv.org/abs/2307.02090) | Mohan Zhou, Yalong Bai, Wei Zhang, Ting Yao, Tiejun Zhao |
| 2023-07-04 | [A Comprehensive Multi-scale Approach for Speech and Dynamics Synchrony in Talking Head Generation](https://arxiv.org/abs/2307.03270) | Louis Airale, Dominique Vaufreydaz, Xavier Alameda-Pineda |
| 2023-07-03 | [RobustL2S: Speaker-Specific Lip-to-Speech Synthesis exploiting Self-Supervised Representations](https://arxiv.org/abs/2307.01233) | Neha Sahipjohn, Neil Shah, Vishal Tambrahalli, Vineet Gandhi |
| 2023-06-28 | [Text-driven Talking Face Synthesis by Reprogramming Audio-driven Models](https://arxiv.org/abs/2306.16003) | Jeongsoo Choi, Minsu Kim, Se Jin Park, Yong Man Ro |
| 2023-06-20 | [Audio-Driven 3D Facial Animation from In-the-Wild Videos](https://arxiv.org/abs/2306.11541) | Liying Lu, Tianke Zhang, Yunfei Liu, Xuangeng Chu, Yu Li |
| 2023-06-19 | [Instruct-NeuralTalker: Editing Audio-Driven Talking Radiance Fields with Instructions](https://arxiv.org/abs/2306.10813) | Yuqi Sun, Ruian He, Weimin Tan, Bo Yan |
| 2023-06-19 | [SelfTalk: A Self-Supervised Commutative Training Diagram to Comprehend 3D Talking Faces](https://arxiv.org/abs/2306.10799) | Ziqiao Peng, Yihao Luo, Yue Shi, Hao Xu et al. |
| 2023-06-15 | [Emotional Speech-Driven Animation with Content-Emotion Disentanglement](https://arxiv.org/abs/2306.08990) | Radek Daněček, Kiran Chhatre, Shashank Tripathi, Yandong Wen et al. |
| 2023-06-13 | [Parametric Implicit Face Representation for Audio-Driven Facial Reenactment](https://arxiv.org/abs/2306.07579) | Ricong Huang, Peiwen Lai, Yipeng Qin, Guanbin Li |
| 2023-06-12 | [NPVForensics: Jointing Non-critical Phonemes and Visemes for Deepfake Detection](https://arxiv.org/abs/2306.06885) | Yu Chen, Yang Yu, Rongrong Ni, Yao Zhao, Haoliang Li |
| 2023-06-10 | [Audio-Visual Speech Enhancement With Selective Off-Screen Speech Extraction](https://arxiv.org/abs/2306.06495) | Tomoya Yoshinaga, Keitaro Tanaka, Shigeo Morishima |
| 2023-06-08 | [ReliableSwap: Boosting General Face Swapping Via Reliable Supervision](https://arxiv.org/abs/2306.05356) | Ge Yuan, Maomao Li, Yong Zhang, Huicheng Zheng |
| 2023-06-06 | [Ada-TTA: Towards Adaptive High-Quality Text-to-Talking Avatar Synthesis](https://arxiv.org/abs/2306.03504) | Zhenhui Ye, Ziyue Jiang, Yi Ren, Jinglin Liu et al. |
| 2023-06-06 | [Emotional Talking Head Generation based on Memory-Sharing and Attention-Augmented Networks](https://arxiv.org/abs/2306.03594) | Jianrong Wang, Yaxin Zhao, Li Liu, Tianyi Xu et al. |
| 2023-06-02 | [Learning Landmarks Motion from Speech for Speaker-Agnostic 3D Talking Heads Generation](https://arxiv.org/abs/2306.01415) | Federico Nocentini, Claudio Ferrari, Stefano Berretti |
| 2023-05-31 | [Exploring Phonetic Context-Aware Lip-Sync For Talking Face Generation](https://arxiv.org/abs/2305.19556) | Se Jin Park, Minsu Kim, Jeongsoo Choi, Yong Man Ro |
| 2023-05-31 | [Audio-Visual Speech Separation in Noisy Environments with a Lightweight Iterative Model](https://arxiv.org/abs/2306.00160) | Héctor Martel, Julius Richter, Kai Li, Xiaolin Hu, Timo Gerkmann |
| 2023-05-24 | [AV-TranSpeech: Audio-Visual Robust Speech-to-Speech Translation](https://arxiv.org/abs/2305.15403) | Rongjie Huang, Huadai Liu, Xize Cheng, Yi Ren et al. |
| 2023-05-23 | [CPNet: Exploiting CLIP-based Attention Condenser and Probability Map Guidance for High-fidelity Talking Face Generation](https://arxiv.org/abs/2305.13962) | Jingning Xu, Benlai Tang, Mingjie Wang, Minghao Li, Meirong Ma |
| 2023-05-22 | [RenderMe-360: A Large Digital Asset Library and Benchmarks Towards High-fidelity Head Avatars](https://arxiv.org/abs/2305.13353) | Dongwei Pan, Long Zhuo, Jingtan Piao, Huiwen Luo et al. |
| 2023-05-18 | [An Android Robot Head as Embodied Conversational Agent](https://arxiv.org/abs/2305.10945) | Marcel Heisler, Christian Becker-Asano |
| 2023-05-17 | [LPMM: Intuitive Pose Control for Neural Talking-Head Model via Landmark-Parameter Morphable Model](https://arxiv.org/abs/2305.10456) | Kwangho Lee, Patrick Kwon, Myung Ki Lee, Namhyuk Ahn, Junsoo Lee |
| 2023-05-15 | [Identity-Preserving Talking Face Generation with Landmark and Appearance Priors](https://arxiv.org/abs/2305.08293) | Weizhi Zhong, Chaowei Fang, Yinqi Cai, Pengxu Wei et al. |
| 2023-05-10 | [DaGAN++: Depth-Aware Generative Adversarial Network for Talking Head Video Generation](https://arxiv.org/abs/2305.06225) | Fa-Ting Hong, Li Shen, Dan Xu |
| 2023-05-09 | [StyleSync: High-Fidelity Generalized and Personalized Lip Sync in Style-based Generator](https://arxiv.org/abs/2305.05445) | Jiazhi Guan, Zhanwang Zhang, Hang Zhou, Tianshu Hu et al. |
| 2023-05-09 | [Zero-shot personalized lip-to-speech synthesis with face image based voice control](https://arxiv.org/abs/2305.14359) | Zheng-Yan Sheng, Yang Ai, Zhen-Hua Ling |
| 2023-05-05 | [Avatar Fingerprinting for Authorized Use of Synthetic Talking-Head Videos](https://arxiv.org/abs/2305.03713) | Ekta Prashnani, Koki Nagano, Shalini De Mello, David Luebke, Orazio Gallo |
| 2023-05-05 | [A multimodal dynamical variational autoencoder for audiovisual speech representation learning](https://arxiv.org/abs/2305.03582) | Samir Sadok, Simon Leglaive, Laurent Girin, Xavier Alameda-Pineda, Renaud Séguier |
| 2023-05-04 | [Multimodal-driven Talking Face Generation via a Unified Diffusion-based Generator](https://arxiv.org/abs/2305.02594) | Chao Xu, Shaoting Zhu, Junwei Zhu, Tianxin Huang et al. |
| 2023-05-04 | [High-fidelity Generalized Emotional Talking Face Generation with Multi-modal Emotion Space Learning](https://arxiv.org/abs/2305.02572) | Chao Xu, Junwei Zhu, Jiangning Zhang, Yue Han et al. |
| 2023-05-01 | [GeneFace++: Generalized and Stable Real-Time Audio-Driven 3D Talking Face Generation](https://arxiv.org/abs/2305.00787) | Zhenhui Ye, Jinzheng He, Ziyue Jiang, Rongjie Huang et al. |
| 2023-05-01 | [StyleAvatar: Real-time Photo-realistic Portrait Avatar from a Single Video](https://arxiv.org/abs/2305.00942) | Lizhen Wang, Xiaochen Zhao, Jingxiang Sun, Yuxiang Zhang et al. |
| 2023-04-30 | [StyleLipSync: Style-based Personalized Lip-sync Video Generation](https://arxiv.org/abs/2305.00521) | Taekyung Ki, Dongchan Min |
| 2023-04-27 | [Controllable One-Shot Face Video Synthesis With Semantic Aware Prior](https://arxiv.org/abs/2304.14471) | Kangning Liu, Yu-Chuan Su, Wei, Hong et al. |
| 2023-04-25 | [AudioGPT: Understanding and Generating Speech, Music, Sound, and Talking Head](https://arxiv.org/abs/2304.12995) | Rongjie Huang, Mingze Li, Dongchao Yang, Jiatong Shi et al. |
| 2023-04-20 | [High-Fidelity and Freely Controllable Talking Head Video Generation](https://arxiv.org/abs/2304.10168) | Yue Gao, Yuan Zhou, Jinglu Wang, Xiao Li et al. |
| 2023-04-18 | [Audio-Driven Talking Face Generation with Diverse yet Realistic Facial Animations](https://arxiv.org/abs/2304.08945) | Rongliang Wu, Yingchen Yu, Fangneng Zhan, Jiahui Zhang et al. |
| 2023-04-11 | [One-Shot High-Fidelity Talking-Head Synthesis with Deformable Neural Radiance Field](https://arxiv.org/abs/2304.05097) | Weichuang Li, Longhao Zhang, Dong Wang, Bin Zhao et al. |
| 2023-04-06 | [That's What I Said: Fully-Controllable Talking Face Generation](https://arxiv.org/abs/2304.03275) | Youngjoon Jang, Kyeongha Rho, Jong-Bin Woo, Hyeongkeun Lee et al. |
| 2023-04-06 | [Face Animation with an Attribute-Guided Diffusion Model](https://arxiv.org/abs/2304.03199) | Bohan Zeng, Xuhui Liu, Sicheng Gao, Boyu Liu et al. |
| 2023-04-02 | [A Unified Compression Framework for Efficient Speech-Driven Talking-Face Generation](https://arxiv.org/abs/2304.00471) | Bo-Kyeong Kim, Jaemin Kang, Daeun Seo, Hancheol Park et al. |
| 2023-04-01 | [TalkCLIP: Talking Head Generation with Text-Guided Expressive Speaking Styles](https://arxiv.org/abs/2304.00334) | Yifeng Ma, Suzhen Wang, Yu Ding, Bowen Ma et al. |
| 2023-03-31 | [FONT: Flow-guided One-shot Talking Head Generation with Natural Head Motions](https://arxiv.org/abs/2303.17789) | Jin Liu, Xi Wang, Xiaomeng Fu, Yesheng Chai et al. |
| 2023-03-30 | [DAE-Talker: High Fidelity Speech-Driven Talking Face Generation with Diffusion Autoencoder](https://arxiv.org/abs/2303.17550) | Chenpeng Du, Qi Chen, Tianyu He, Xu Tan et al. |
| 2023-03-29 | [Seeing What You Said: Talking Face Generation Guided by a Lip Reading Expert](https://arxiv.org/abs/2303.17480) | Jiadong Wang, Xinyuan Qian, Malu Zhang, Robby T. Tan, Haizhou Li |
| 2023-03-26 | [OTAvatar: One-shot Talking Face Avatar with Controllable Tri-plane Rendering](https://arxiv.org/abs/2303.14662) | Zhiyuan Ma, Xiangyu Zhu, Guojun Qi, Zhen Lei, Lei Zhang |
| 2023-03-21 | [Emotionally Enhanced Talking Face Generation](https://arxiv.org/abs/2303.11548) | Sahil Goyal, Shagun Uppal, Sarthak Bhagat, Yi Yu et al. |
| 2023-03-20 | [EmoTalk: Speech-Driven Emotional Disentanglement for 3D Face Animation](https://arxiv.org/abs/2303.11089) | Ziqiao Peng, Haoyu Wu, Zhenbo Song, Hao Xu et al. |
| 2023-03-17 | [Style Transfer for 2D Talking Head Animation](https://arxiv.org/abs/2303.09799) | Trong-Thang Pham, Nhat Le, Tuong Do, Hung Nguyen et al. |
| 2023-03-17 | [MMFace4D: A Large-Scale Multi-Modal 4D Face Dataset for Audio-Driven 3D Face Animation](https://arxiv.org/abs/2303.09797) | Haozhe Wu, Jia Jia, Junliang Xing, Hongwei Xu et al. |
| 2023-03-14 | [DisCoHead: Audio-and-Video-Driven Talking Head Generation by Disentangled Control of Head Pose and Facial Expressions](https://arxiv.org/abs/2303.07697) | Geumbyeol Hwang, Sunwon Hong, Seunghyun Lee, Sungwoo Park, Gyeongsu Chae |
| 2023-03-14 | [Learning Cross-lingual Visual Speech Representations](https://arxiv.org/abs/2303.09455) | Andreas Zinonos, Alexandros Haliassos, Pingchuan Ma, Stavros Petridis, Maja Pantic |
| 2023-03-13 | [Real-Time Audio-Visual End-to-End Speech Enhancement](https://arxiv.org/abs/2303.07005) | Zirun Zhu, Hemin Yang, Min Tang, Ziyi Yang et al. |
| 2023-03-09 | [Improving Few-Shot Learning for Talking Face System with TTS Data Augmentation](https://arxiv.org/abs/2303.05322) | Qi Chen, Ziyang Ma, Tao Liu, Xu Tan et al. |
| 2023-03-05 | [Cyber Vaccine for Deepfake Immunity](https://arxiv.org/abs/2303.02659) | Ching-Chun Chang, Huy Hong Nguyen, Junichi Yamagishi, Isao Echizen |
| 2023-02-28 | [UniFLG: Unified Facial Landmark Generator from Text or Speech](https://arxiv.org/abs/2302.14337) | Kentaro Mitsui, Yukiya Hono, Kei Sawada |
| 2023-02-27 | [Memory-augmented Contrastive Learning for Talking Head Generation](https://arxiv.org/abs/2302.13469) | Jianrong Wang, Yaxin Zhao, Li Liu, Hongkai Fan et al. |
| 2023-02-24 | [Pose-Controllable 3D Facial Animation Synthesis using Hierarchical Audio-Vertex Attention](https://arxiv.org/abs/2302.12532) | Bin Liu, Xiaolin Wei, Bo Li, Junjie Cao, Yu-Kun Lai |
| 2023-02-16 | [OPT: One-shot Pose-Controllable Talking Head Generation](https://arxiv.org/abs/2302.08197) | Jin Liu, Xi Wang, Xiaomeng Fu, Yesheng Chai et al. |
| 2023-01-31 | [GeneFace: Generalized and High-Fidelity Audio-Driven 3D Talking Face Synthesis](https://arxiv.org/abs/2301.13430) | Zhenhui Ye, Ziyue Jiang, Yi Ren, Jinglin Liu et al. |
| 2023-01-16 | [DPE: Disentanglement of Pose and Expression for General Video Portrait Editing](https://arxiv.org/abs/2301.06281) | Youxin Pang, Yong Zhang, Weize Quan, Yanbo Fan et al. |
| 2023-01-15 | [Learning Audio-Driven Viseme Dynamics for 3D Face Animation](https://arxiv.org/abs/2301.06059) | Linchao Bao, Haoxian Zhang, Yue Qian, Tangli Xue et al. |
| 2023-01-10 | [DiffTalk: Crafting Diffusion Models for Generalized Audio-Driven Portraits Animation](https://arxiv.org/abs/2301.03786) | Shuai Shen, Wenliang Zhao, Zibin Meng, Wanhua Li et al. |
| 2023-01-06 | [CodeTalker: Speech-Driven 3D Facial Animation with Discrete Motion Prior](https://arxiv.org/abs/2301.02379) | Jinbo Xing, Menghan Xia, Yuechen Zhang, Xiaodong Cun et al. |
| 2023-01-06 | [Diffused Heads: Diffusion Models Beat GANs on Talking-Face Generation](https://arxiv.org/abs/2301.03396) | Michał Stypułkowski, Konstantinos Vougioukas, Sen He, Maciej Zięba et al. |
| 2023-01-05 | [Expressive Speech-driven Facial Animation with controllable emotions](https://arxiv.org/abs/2301.02008) | Yutong Chen, Junhong Zhao, Wei-Qiang Zhang |
| 2023-01-03 | [StyleTalk: One-shot Talking Head Generation with Controllable Speaking Styles](https://arxiv.org/abs/2301.01081) | Yifeng Ma, Suzhen Wang, Zhipeng Hu, Changjie Fan et al. |

### 2022

| Date | Title | Authors |
|------|-------|---------|
| 2022-12-28 | [All's well that FID's well? Result quality and metric scores in GAN models for lip-sychronization tasks](https://arxiv.org/abs/2212.13810) | Carina Geldhauser, Johan Liljegren, Pontus Nordqvist |
| 2022-12-23 | [Dubbing in Practice: A Large Scale Study of Human Localization With Insights for Automatic Dubbing](https://arxiv.org/abs/2212.12137) | William Brannon, Yogesh Virkar, Brian Thompson |
| 2022-12-21 | [An Audio-Visual Speech Separation Model Inspired by Cortico-Thalamo-Cortical Circuits](https://arxiv.org/abs/2212.10744) | Kai Li, Fenghua Xie, Hang Chen, Kexin Yuan, Xiaolin Hu |
| 2022-12-15 | [MetaPortrait: Identity-Preserving Talking Head Generation with Fast Personalized Adaptation](https://arxiv.org/abs/2212.08062) | Bowen Zhang, Chenyang Qi, Pan Zhang, Bo Zhang et al. |
| 2022-12-09 | [Masked Lip-Sync Prediction by Audio-Visual Contextual Exploitation in Transformers](https://arxiv.org/abs/2212.04970) | Yasheng Sun, Hang Zhou, Kaisiyuan Wang, Qianyi Wu et al. |
| 2022-12-09 | [Memories are One-to-Many Mapping Alleviators in Talking Face Generation](https://arxiv.org/abs/2212.05005) | Anni Tang, Tianyu He, Xu Tan, Jun Ling, Li Song |
| 2022-12-07 | [Talking Head Generation with Probabilistic Audio-to-Visual Diffusion Priors](https://arxiv.org/abs/2212.04248) | Zhentao Yu, Zixin Yin, Deyu Zhou, Duomin Wang et al. |
| 2022-12-06 | [Self-Supervised Audio-Visual Speech Representations Learning By Multimodal Self-Distillation](https://arxiv.org/abs/2212.02782) | Jing-Xuan Zhang, Genshun Wan, Zhen-Hua Ling, Jia Pan et al. |
| 2022-11-28 | [High-fidelity Facial Avatar Reconstruction from Monocular Video with Generative Priors](https://arxiv.org/abs/2211.15064) | Yunpeng Bai, Yanbo Fan, Xuan Wang, Yong Zhang et al. |
| 2022-11-27 | [VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild](https://arxiv.org/abs/2211.14758) | Kun Cheng, Xiaodong Cun, Yong Zhang, Menghan Xia et al. |
| 2022-11-26 | [Progressive Disentangled Representation Learning for Fine-Grained Controllable Talking Head Synthesis](https://arxiv.org/abs/2211.14506) | Duomin Wang, Yu Deng, Zixin Yin, Heung-Yeung Shum, Baoyuan Wang |
| 2022-11-22 | [Real-time Neural Radiance Talking Portrait Synthesis via Audio-spatial Decomposition](https://arxiv.org/abs/2211.12368) | Jiaxiang Tang, Kaisiyuan Wang, Hang Zhou, Xiaokang Chen et al. |
| 2022-11-22 | [SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation](https://arxiv.org/abs/2211.12194) | Wenxuan Zhang, Xiaodong Cun, Xuan Wang, Yong Zhang et al. |
| 2022-11-20 | [LA-VocE: Low-SNR Audio-visual Speech Enhancement using Neural Vocoders](https://arxiv.org/abs/2211.10999) | Rodrigo Mira, Buye Xu, Jacob Donley, Anurag Kumar et al. |
| 2022-11-17 | [SPACE: Speech-driven Portrait Animation with Controllable Expression](https://arxiv.org/abs/2211.09809) | Siddharth Gururani, Arun Mallya, Ting-Chun Wang, Rafael Valle, Ming-Yu Liu |
| 2022-11-12 | [MARLIN: Masked Autoencoder for facial video Representation LearnINg](https://arxiv.org/abs/2211.06627) | Zhixi Cai, Shreya Ghosh, Kalin Stefanov, Abhinav Dhall et al. |
| 2022-11-07 | [Egocentric Audio-Visual Noise Suppression](https://arxiv.org/abs/2211.03643) | Roshan Sharma, Weipeng He, Ju Lin, Egor Lakomkin et al. |
| 2022-11-02 | [SyncTalkFace: Talking Face Generation with Precise Lip-Syncing via Audio-Lip Memory](https://arxiv.org/abs/2211.00924) | Se Jin Park, Minsu Kim, Joanna Hong, Jeongsoo Choi, Yong Man Ro |
| 2022-11-02 | [Autoregressive GAN for Semantic Unconditional Head Motion Generation](https://arxiv.org/abs/2211.00987) | Louis Airale, Xavier Alameda-Pineda, Stéphane Lathuilière, Dominique Vaufreydaz |
| 2022-11-02 | [Audio-visual speech enhancement with a deep Kalman filter generative model](https://arxiv.org/abs/2211.00988) | Ali Golmakani, Mostafa Sadeghi, Romain Serizel |
| 2022-10-24 | [A Novel Frame Structure for Cloud-Based Audio-Visual Speech Enhancement in Multimodal Hearing-aids](https://arxiv.org/abs/2210.13127) | Abhijeet Bishnu, Ankit Gupta, Mandar Gogate, Kia Dashtipour et al. |
| 2022-10-13 | [Sparse in Space and Time: Audio-visual Synchronisation with Trainable Selectors](https://arxiv.org/abs/2210.07055) | Vladimir Iashin, Weidi Xie, Esa Rahtu, Andrew Zisserman |
| 2022-10-13 | [Pre-Avatar: An Automatic Presentation Generation Framework Leveraging Talking Avatar](https://arxiv.org/abs/2210.06877) | Aolan Sun, Xulong Zhang, Tiandong Ling, Jianzong Wang et al. |
| 2022-10-12 | [GOTCHA: Real-Time Video Deepfake Detection via Challenge-Response](https://arxiv.org/abs/2210.06186) | Govind Mittal, Chinmay Hegde, Nasir Memon |
| 2022-10-07 | [A Keypoint Based Enhancement Method for Audio Driven Free View Talking Head Synthesis](https://arxiv.org/abs/2210.03335) | Yichen Han, Ya Li, Yingming Gao, Jinlong Xue et al. |
| 2022-10-07 | [Compressing Video Calls using Synthetic Talking Heads](https://arxiv.org/abs/2210.03692) | Madhav Agarwal, Anchit Gupta, Rudrabha Mukhopadhyay, Vinay P. Namboodiri, C V Jawahar |
| 2022-10-06 | [Audio-Visual Face Reenactment](https://arxiv.org/abs/2210.02755) | Madhav Agarwal, Rudrabha Mukhopadhyay, Vinay Namboodiri, C V Jawahar |
| 2022-09-27 | [StyleMask: Disentangling the Style Space of StyleGAN2 for Neural Face Reenactment](https://arxiv.org/abs/2209.13375) | Stella Bounareli, Christos Tzelepis, Vasileios Argyriou, Ioannis Patras, Georgios Tzimiropoulos |
| 2022-09-21 | [Gemino: Practical and Robust Neural Compression for Video Conferencing](https://arxiv.org/abs/2209.10507) | Vibhaalakshmi Sivaraman, Pantea Karimi, Vedantha Venkatapathy, Mehrdad Khani et al. |
| 2022-09-21 | [FNeVR: Neural Volume Rendering for Face Animation](https://arxiv.org/abs/2209.10340) | Bohan Zeng, Boyu Liu, Hong Li, Xuhui Liu et al. |
| 2022-09-19 | [AutoLV: Automatic Lecture Video Generator](https://arxiv.org/abs/2209.08795) | Wenbin Wang, Yang Song, Sanjay Jha |
| 2022-09-17 | [Continuously Controllable Facial Expression Editing in Talking Face Videos](https://arxiv.org/abs/2209.08289) | Zhiyao Sun, Yu-Hui Wen, Tian Lv, Yanan Sun et al. |
| 2022-09-09 | [Talking Head from Speech Audio using a Pre-trained Image Generator](https://arxiv.org/abs/2209.04252) | Mohammed M. Alghamdi, He Wang, Andrew J. Bulpitt, David C. Hogg |
| 2022-09-07 | [Multimodal Speech Enhancement Using Burst Propagation](https://arxiv.org/abs/2209.03275) | Mohsin Raza, Leandro A. Passos, Ahmed Khubaib, Ahsan Adeel |
| 2022-09-03 | [Synthesizing Photorealistic Virtual Humans Through Cross-modal Disentanglement](https://arxiv.org/abs/2209.01320) | Siddarth Ravichandran, Ondřej Texler, Dimitar Dinev, Hyun Jae Kang |
| 2022-08-29 | [StableFace: Analyzing and Improving Motion Stability for Talking Face Generation](https://arxiv.org/abs/2208.13717) | Jun Ling, Xu Tan, Liyang Chen, Runnan Li et al. |
| 2022-08-23 | [StyleTalker: One-shot Style-based Audio-driven Talking Head Video Generation](https://arxiv.org/abs/2208.10922) | Dongchan Min, Minyoung Song, Eunji Ko, Sung Ju Hwang |
| 2022-08-21 | [Towards MOOCs for Lipreading: Using Synthetic Talking Heads to Train Humans in Lipreading at Scale](https://arxiv.org/abs/2208.09796) | Aditya Agarwal, Bipasha Sen, Rudrabha Mukhopadhyay, Vinay Namboodiri, C. V Jawahar |
| 2022-08-17 | [Extreme-scale Talking-Face Video Upsampling with Audio-Visual Priors](https://arxiv.org/abs/2208.08118) | Sindhu B Hegde, Rudrabha Mukhopadhyay, Vinay P Namboodiri, C. V. Jawahar |
| 2022-08-03 | [Free-HeadGAN: Neural Talking Head Synthesis with Explicit Gaze Control](https://arxiv.org/abs/2208.02210) | Michail Christos Doukas, Evangelos Ververas, Viktoriia Sharmanska, Stefanos Zafeiriou |
| 2022-07-24 | [Learning Dynamic Facial Radiance Fields for Few-Shot Talking Head Synthesis](https://arxiv.org/abs/2207.11770) | Shuai Shen, Wanhua Li, Zheng Zhu, Yueqi Duan et al. |
| 2022-07-22 | [Visual Speech-Aware Perceptual 3D Facial Expression Reconstruction from Videos](https://arxiv.org/abs/2207.11094) | Panagiotis P. Filntisis, George Retsinas, Foivos Paraperas-Papantoniou, Athanasios Katsamanis et al. |
| 2022-07-09 | [Dual-Path Cross-Modal Attention for better Audio-Visual Speech Extraction](https://arxiv.org/abs/2207.04213) | Zhongweiyang Xu, Xulin Fan, Mark Hasegawa-Johnson |
| 2022-07-08 | [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](https://arxiv.org/abs/2207.03800) | Yongqi Wang, Zhou Zhao |
| 2022-07-04 | [Multi-Modal Multi-Correlation Learning for Audio-Visual Speech Separation](https://arxiv.org/abs/2207.01197) | Xiaoyu Wang, Xiangyu Kong, Xiulian Peng, Yan Lu |
| 2022-06-30 | [Improving Visual Speech Enhancement Network by Learning Audio-visual Affinity with Multi-head Attention](https://arxiv.org/abs/2206.14964) | Xinmeng Xu, Yang Wang, Jie Jia, Binbin Chen, Dejun Li |
| 2022-06-29 | [Cut Inner Layers: A Structured Pruning Strategy for Efficient U-Net GANs](https://arxiv.org/abs/2206.14658) | Bo-Kyeong Kim, Shinkook Choi, Hancheol Park |
| 2022-06-26 | [Perceptual Conversational Head Generation with Regularized Driver and Enhanced Renderer](https://arxiv.org/abs/2206.12837) | Ailin Huang, Zhewei Huang, Shuchang Zhou |
| 2022-06-15 | [VisageSynTalk: Unseen Speaker Video-to-Speech Synthesis via Speech-Visage Feature Selection](https://arxiv.org/abs/2206.07458) | Joanna Hong, Minsu Kim, Yong Man Ro |
| 2022-06-06 | [Canonical Cortical Graph Neural Networks and its Application for Speech Enhancement in Audio-Visual Hearing Aids](https://arxiv.org/abs/2206.02671) | Leandro A. Passos, João Paulo Papa, Amir Hussain, Ahsan Adeel |
| 2022-05-30 | [EAMM: One-Shot Emotional Talking Face via Audio-Based Emotion-Aware Motion Model](https://arxiv.org/abs/2205.15278) | Xinya Ji, Hang Zhou, Kaisiyuan Wang, Qianyi Wu et al. |
| 2022-05-26 | [One-Shot Face Reenactment on Megapixels](https://arxiv.org/abs/2205.13368) | Wonjun Kang, Geonsu Lee, Hyung Il Koo, Nam Ik Cho |
| 2022-05-24 | [Merkel Podcast Corpus: A Multimodal Dataset Compiled from 16 Years of Angela Merkel's Weekly Video Podcasts](https://arxiv.org/abs/2205.12194) | Debjoy Saha, Shravan Nayak, Timo Baumann |
| 2022-05-15 | [Learning Lip-Based Audio-Visual Speaker Embeddings with AV-HuBERT](https://arxiv.org/abs/2205.07180) | Bowen Shi, Abdelrahman Mohamed, Wei-Ning Hsu |
| 2022-05-13 | [Talking Face Generation with Multilingual TTS](https://arxiv.org/abs/2205.06421) | Hyoung-Kyu Song, Sang Hoon Woo, Junhyeok Lee, Seungmin Yang et al. |
| 2022-05-02 | [Emotion-Controllable Generalized Talking Face Generation](https://arxiv.org/abs/2205.01155) | Sanjana Sinha, Sandika Biswas, Ravindra Yadav, Brojeshwar Bhowmick |
| 2022-04-28 | [Unsupervised Voice-Face Representation Learning by Cross-Modal Prototype Contrast](https://arxiv.org/abs/2204.14057) | Boqing Zhu, Kele Xu, Changjian Wang, Zheng Qin et al. |
| 2022-04-27 | [Talking Head Generation Driven by Speech-Related Facial Action Units and Audio- Based on Multimodal Representation Fusion](https://arxiv.org/abs/2204.12756) | Sen Chen, Zhilei Liu, Jiaxing Liu, Longbiao Wang |
| 2022-04-13 | [Dynamic Neural Textures: Generating Talking-Face Videos with Continuously Controllable Expressions](https://arxiv.org/abs/2204.06180) | Zipeng Ye, Zhiyao Sun, Yu-Hui Wen, Yanan Sun et al. |
| 2022-04-06 | [Audio-Visual Person-of-Interest DeepFake Detection](https://arxiv.org/abs/2204.03083) | Davide Cozzolino, Alessandro Pianese, Matthias Nießner, Luisa Verdoliva |
| 2022-03-31 | [Audio-Visual Speech Codecs: Rethinking Audio-Visual Speech Enhancement by Re-Synthesis](https://arxiv.org/abs/2203.17263) | Karren Yang, Dejan Markovic, Steven Krenn, Vasu Agrawal, Alexander Richard |
| 2022-03-30 | [End to End Lip Synchronization with a Temporal AutoEncoder](https://arxiv.org/abs/2203.16224) | Yoav Shalev, Lior Wolf |
| 2022-03-28 | [Expressive Talking Head Video Encoding in StyleGAN2 Latent-Space](https://arxiv.org/abs/2203.14512) | Trevine Oorloff, Yaser Yacoob |
| 2022-03-27 | [Thin-Plate Spline Motion Model for Image Animation](https://arxiv.org/abs/2203.14367) | Jian Zhao, Hui Zhang |
| 2022-03-18 | [On the role of Lip Articulation in Visual Speech Perception](https://arxiv.org/abs/2203.10117) | Zakaria Aldeneh, Masha Fedzechkina, Skyler Seto, Katherine Metcalf et al. |
| 2022-03-15 | [DialogueNeRF: Towards Realistic Avatar Face-to-Face Conversation Video Generation](https://arxiv.org/abs/2203.07931) | Yichao Yan, Zanwei Zhou, Zi Wang, Jingnan Gao, Xiaokang Yang |
| 2022-03-13 | [Depth-Aware Generative Adversarial Network for Talking Head Video Generation](https://arxiv.org/abs/2203.06605) | Fa-Ting Hong, Longhao Zhang, Li Shen, Dan Xu |
| 2022-03-10 | [An Audio-Visual Attention Based Multimodal Network for Fake Talking Face Videos Detection](https://arxiv.org/abs/2203.05178) | Ganglai Wang, Peng Zhang, Lei Xie, Wei Huang et al. |
| 2022-03-08 | [Attention-Based Lip Audio-Visual Synthesis for Talking Face Generation in the Wild](https://arxiv.org/abs/2203.03984) | Ganglai Wang, Peng Zhang, Lei Xie, Wei Huang, Yufei Zha |
| 2022-03-08 | [StyleHEAT: One-Shot High-Resolution Editable Talking Face Generation via Pre-trained StyleGAN](https://arxiv.org/abs/2203.04036) | Fei Yin, Yong Zhang, Xiaodong Cun, Mingdeng Cao et al. |
| 2022-03-05 | [Audio-visual speech separation based on joint feature representation with cross-modal attention](https://arxiv.org/abs/2203.02655) | Junwen Xiong, Peng Zhang, Lei Xie, Wei Huang et al. |
| 2022-02-25 | [FSGANv2: Improved Subject Agnostic Face Swapping and Reenactment](https://arxiv.org/abs/2202.12972) | Yuval Nirkin, Yosi Keller, Tal Hassner |
| 2022-02-22 | [Thinking the Fusion Strategy of Multi-reference Face Reenactment](https://arxiv.org/abs/2202.10758) | Takuya Yashima, Takuya Narihira, Tamaki Kojima |
| 2022-02-13 | [Data standardization for robust lip sync](https://arxiv.org/abs/2202.06198) | Chun Wang |
| 2022-02-01 | [The impact of removing head movements on audio-visual speech enhancement](https://arxiv.org/abs/2202.00538) | Zhiqi Kang, Mostafa Sadeghi, Radu Horaud, Xavier Alameda-Pineda et al. |
| 2022-01-31 | [Finding Directions in GAN's Latent Space for Neural Face Reenactment](https://arxiv.org/abs/2202.00046) | Stella Bounareli, Vasileios Argyriou, Georgios Tzimiropoulos |
| 2022-01-20 | [Stitch it in Time: GAN-Based Facial Editing of Real Videos](https://arxiv.org/abs/2201.08361) | Rotem Tzaban, Ron Mokady, Rinon Gal, Amit H. Bermano, Daniel Cohen-Or |
| 2022-01-18 | [Leveraging Real Talking Faces via Self-Supervision for Robust Forgery Detection](https://arxiv.org/abs/2201.07131) | Alexandros Haliassos, Rodrigo Mira, Stavros Petridis, Maja Pantic |
| 2022-01-17 | [Towards Realistic Visual Dubbing with Heterogeneous Sources](https://arxiv.org/abs/2201.06260) | Tianyi Xie, Liucheng Liao, Cheng Bi, Benlai Tang et al. |
| 2022-01-16 | [Audio-Driven Talking Face Video Generation with Dynamic Convolution Kernels](https://arxiv.org/abs/2201.05986) | Zipeng Ye, Mengfei Xia, Ran Yi, Juyong Zhang et al. |
| 2022-01-03 | [DFA-NeRF: Personalized Talking Head Generation via Disentangled Face Attributes Neural Rendering](https://arxiv.org/abs/2201.00791) | Shunyu Yao, RuiZhe Zhong, Yichao Yan, Guangtao Zhai, Xiaokang Yang |

### 2021

| Date | Title | Authors |
|------|-------|---------|
| 2021-12-27 | [Responsive Listening Head Generation: A Benchmark Dataset and Baseline](https://arxiv.org/abs/2112.13548) | Mohan Zhou, Yalong Bai, Wei Zhang, Ting Yao et al. |
| 2021-12-19 | [Initiative Defense against Facial Manipulation](https://arxiv.org/abs/2112.10098) | Qidong Huang, Jie Zhang, Wenbo Zhou, WeimingZhang, Nenghai Yu |
| 2021-12-16 | [Towards Robust Real-time Audio-Visual Speech Enhancement](https://arxiv.org/abs/2112.09060) | Mandar Gogate, Kia Dashtipour, Amir Hussain |
| 2021-12-06 | [One-shot Talking Face Generation from Single-speaker Audio-Visual Correlation Learning](https://arxiv.org/abs/2112.02749) | Suzhen Wang, Lincheng Li, Yu Ding, Xin Yu |
| 2021-12-04 | [Joint Audio-Text Model for Expressive Speech-Driven 3D Facial Animation](https://arxiv.org/abs/2112.02214) | Yingruo Fan, Zhaojiang Lin, Jun Saito, Wenping Wang, Taku Komura |
| 2021-11-18 | [Towards Intelligibility-Oriented Audio-Visual Speech Enhancement](https://arxiv.org/abs/2111.09642) | Tassadaq Hussain, Mandar Gogate, Kia Dashtipour, Amir Hussain |
| 2021-11-02 | [BiosecurID: a multimodal biometric database](https://arxiv.org/abs/2111.03472) | Julian Fierrez, Javier Galbally, Javier Ortega-Garcia, Manuel R Freire et al. |
| 2021-10-30 | [Imitating Arbitrary Talking Style for Realistic Audio-DrivenTalking Face Synthesis](https://arxiv.org/abs/2111.00203) | Haozhe Wu, Jia Jia, Haoyu Wang, Yishun Dou et al. |
| 2021-10-26 | [Emotion recognition in talking-face videos using persistent entropy and neural networks](https://arxiv.org/abs/2110.13571) | Eduardo Paluzo-Hidalgo, Guillermo Aguirre-Carrazana, Rocio Gonzalez-Diaz |
| 2021-10-19 | [Talking Head Generation with Audio and Speech Related Facial Action Units](https://arxiv.org/abs/2110.09951) | Sen Chen, Zhilei Liu, Jiaxing Liu, Zhengxiang Yan, Longbiao Wang |
| 2021-10-16 | [Intelligent Video Editing: Incorporating Modern Talking Face Generation Algorithms in a Video Editor](https://arxiv.org/abs/2110.08580) | Anchit Gupta, Faizan Farooq Khan, Rudrabha Mukhopadhyay, Vinay P. Namboodiri, C. V. Jawahar |
| 2021-10-10 | [Fine-grained Identity Preserving Landmark Synthesis for Face Reenactment](https://arxiv.org/abs/2110.04708) | Haichao Zhang, Youcheng Ben, Weixi Zhang, Tao Chen et al. |
| 2021-09-22 | [Live Speech Portraits: Real-Time Photorealistic Talking-Head Animation](https://arxiv.org/abs/2109.10595) | Yuanxun Lu, Jinxiang Chai, Xun Cao |
| 2021-09-16 | [Invertible Frowns: Video-to-Video Facial Emotion Translation](https://arxiv.org/abs/2109.08061) | Ian Magnusson, Aruna Sankaranarayanan, Andrew Lippman |
| 2021-09-10 | [Detection of GAN-synthesized street videos](https://arxiv.org/abs/2109.04991) | Omran Alamayreh, Mauro Barni |
| 2021-09-05 | [Deep Person Generation: A Survey from the Perspective of Face, Pose and Cloth Synthesis](https://arxiv.org/abs/2109.02081) | Tong Sha, Wei Zhang, Tong Shen, Zhoujun Li, Tao Mei |
| 2021-08-18 | [Speech Drives Templates: Co-Speech Gesture Synthesis with Learned Templates](https://arxiv.org/abs/2108.08020) | Shenhan Qian, Zhi Tu, Yihao Zhi, Wen Liu, Shenghua Gao |
| 2021-08-18 | [FACIAL: Synthesizing Dynamic Talking Face with Implicit Attribute Learning](https://arxiv.org/abs/2108.07938) | Chenxu Zhang, Yifan Zhao, Yifei Huang, Ming Zeng et al. |
| 2021-08-12 | [UniFaceGAN: A Unified Framework for Temporally Consistent Facial Video Editing](https://arxiv.org/abs/2108.05650) | Meng Cao, Haozhi Huang, Hao Wang, Xuan Wang et al. |
| 2021-08-11 | [FakeAVCeleb: A Novel Audio-Video Multimodal Deepfake Dataset](https://arxiv.org/abs/2108.05080) | Hasam Khalid, Shahroz Tariq, Minha Kim, Simon S. Woo |
| 2021-08-09 | [AnyoneNet: Synchronized Speech and Talking Head Generation for Arbitrary Person](https://arxiv.org/abs/2108.04325) | Xinsheng Wang, Qicong Xie, Jihua Zhu, Lei Xie, Scharenborg |
| 2021-07-26 | [Beyond Voice Identity Conversion: Manipulating Voice Attributes by Adversarial Learning of Structured Disentangled Representations](https://arxiv.org/abs/2107.12346) | Laurent Benaroya, Nicolas Obin, Axel Roebel |
| 2021-07-20 | [Audio2Head: Audio-driven One-shot Talking-head Generation with Natural Head Motion](https://arxiv.org/abs/2107.09293) | Suzhen Wang, Lincheng Li, Yu Ding, Changjie Fan, Xin Yu |
| 2021-07-14 | [Parallel and High-Fidelity Text-to-Lip Generation](https://arxiv.org/abs/2107.06831) | Jinglin Liu, Zhiying Zhu, Yi Ren, Wencan Huang et al. |
| 2021-07-10 | [Speech2Video: Cross-Modal Distillation for Speech to Video Generation](https://arxiv.org/abs/2107.04806) | Shijing Si, Jianzong Wang, Xiaoyang Qu, Ning Cheng et al. |
| 2021-07-07 | [Egocentric Videoconferencing](https://arxiv.org/abs/2107.03109) | Mohamed Elgharib, Mohit Mendiratta, Justus Thies, Matthias Nießner et al. |
| 2021-07-05 | [Multi-modality Deep Restoration of Extremely Compressed Face Videos](https://arxiv.org/abs/2107.05548) | Xi Zhang, Xiaolin Wu |
| 2021-06-26 | [Txt2Vid: Ultra-Low Bitrate Compression of Talking-Head Videos via Text](https://arxiv.org/abs/2106.14014) | Pulkit Tandon, Shubham Chandak, Pat Pataranutaporn, Yimeng Liu et al. |
| 2021-06-14 | [Selective Listening by Synchronizing Speech with Lips](https://arxiv.org/abs/2106.07150) | Zexu Pan, Ruijie Tao, Chenglin Xu, Haizhou Li |
| 2021-06-08 | [LipSync3D: Data-Efficient Learning of Personalized 3D Talking Faces from Video using Pose and Lighting Normalization](https://arxiv.org/abs/2106.04185) | Avisek Lahiri, Vivek Kwatra, Christian Frueh, John Lewis, Chris Bregler |
| 2021-05-19 | [Disentanglement Learning for Variational Autoencoders Applied to Audio-Visual Speech Enhancement](https://arxiv.org/abs/2105.08970) | Guillaume Carbajal, Julius Richter, Timo Gerkmann |
| 2021-04-29 | [Text2Video: Text-driven Talking-head Video Synthesis with Personalized Phoneme-Pose Dictionary](https://arxiv.org/abs/2104.14631) | Sibo Zhang, Jiahong Yuan, Miao Liao, Liangjun Zhang |
| 2021-04-29 | [Learned Spatial Representations for Few-shot Talking-Head Synthesis](https://arxiv.org/abs/2104.14557) | Moustafa Meshry, Saksham Suri, Larry S. Davis, Abhinav Shrivastava |
| 2021-04-25 | [3D-TalkEmo: Learning to Synthesize 3D Emotional Talking Head](https://arxiv.org/abs/2104.12051) | Qianyun Wang, Zhenfeng Fan, Shihong Xia |
| 2021-04-22 | [Pose-Controllable Talking Face Generation by Implicitly Modularized Audio-Visual Representation](https://arxiv.org/abs/2104.11116) | Hang Zhou, Yasheng Sun, Wayne Wu, Chen Change Loy et al. |
| 2021-04-20 | [A cappella: Audio-visual Singing Voice Separation](https://arxiv.org/abs/2104.09946) | Juan F. Montesinos, Venkatesh S. Kadandale, Gloria Haro |
| 2021-04-16 | [Write-a-speaker: Text-based Emotional and Rhythmic Talking-head Generation](https://arxiv.org/abs/2104.07995) | Lincheng Li, Suzhen Wang, Zhimeng Zhang, Yu Ding et al. |
| 2021-04-15 | [Audio-Driven Emotional Video Portraits](https://arxiv.org/abs/2104.07452) | Xinya Ji, Hang Zhou, Kaisiyuan Wang, Wayne Wu et al. |
| 2021-04-07 | [Single Source One Shot Reenactment using Weighted motion From Paired Feature Points](https://arxiv.org/abs/2104.03117) | Soumya Tripathy, Juho Kannala, Esa Rahtu |
| 2021-04-07 | [Everything's Talkin': Pareidolia Face Reenactment](https://arxiv.org/abs/2104.03061) | Linsen Song, Wayne Wu, Chaoyou Fu, Chen Qian et al. |
| 2021-04-07 | [LI-Net: Large-Pose Identity-Preserving Face Reenactment Network](https://arxiv.org/abs/2104.02850) | Jin Liu, Peng Chen, Tao Liang, Zhaoxing Li et al. |
| 2021-03-25 | [Looking into Your Speech: Learning Cross-modal Affinity for Audio-visual Speech Separation](https://arxiv.org/abs/2104.02775) | Jiyoung Lee, Soo-Whan Chung, Sunok Kim, Hong-Goo Kang, Kwanghoon Sohn |
| 2021-03-20 | [AD-NeRF: Audio Driven Neural Radiance Fields for Talking Head Synthesis](https://arxiv.org/abs/2103.11078) | Yudong Guo, Keyu Chen, Sen Liang, Yong-Jin Liu et al. |
| 2021-03-18 | [KoDF: A Large-scale Korean DeepFake Detection Dataset](https://arxiv.org/abs/2103.10094) | Patrick Kwon, Jaeseong You, Gyuhyeon Nam, Sungwoo Park, Gyeongsu Chae |
| 2021-03-05 | [Real-time RGBD-based Extended Body Pose Estimation](https://arxiv.org/abs/2103.03663) | Renat Bashirov, Anastasia Ianina, Karim Iskakov, Yevgeniy Kononenko et al. |
| 2021-03-02 | [Audio-Visual Speech Separation Using Cross-Modal Correspondence Loss](https://arxiv.org/abs/2103.01463) | Naoki Makishima, Mana Ihori, Akihiko Takashima, Tomohiro Tanaka et al. |
| 2021-02-19 | [One Shot Audio to Animated Video Generation](https://arxiv.org/abs/2102.09737) | Neeraj Kumar, Srishti Goel, Ankur Narang, Brejesh Lall et al. |
| 2021-02-18 | [AudioVisual Speech Synthesis: A brief literature review](https://arxiv.org/abs/2103.03927) | Efthymios Georgiou, Athanasios Katsamanis |
| 2021-02-08 | [Switching Variational Auto-Encoders for Noise-Agnostic Audio-visual Speech Enhancement](https://arxiv.org/abs/2102.04144) | Mostafa Sadeghi, Xavier Alameda-Pineda |
| 2021-02-08 | [One-shot Face Reenactment Using Appearance Adaptive Normalization](https://arxiv.org/abs/2102.03984) | Guangming Yao, Yi Yuan, Tianjia Shao, Shuang Li et al. |
| 2021-01-15 | [AMFFCN: Attentional Multi-layer Feature Fusion Convolution Network for Audio-visual Speech Enhancement](https://arxiv.org/abs/2101.06268) | Xinmeng Xu, Jianjun Hao |
| 2021-01-15 | [Multi-layer Feature Fusion Convolution Network for Audio-visual Speech Enhancement](https://arxiv.org/abs/2101.05975) | Xinmeng Xu, Jianjun Hao |
| 2021-01-12 | [Fast Facial Landmark Detection and Applications: A Survey](https://arxiv.org/abs/2101.10808) | Kostiantyn Khabarlak, Larysa Koriashkina |
| 2021-01-08 | [VisualVoice: Audio-Visual Speech Separation with Cross-Modal Consistency](https://arxiv.org/abs/2101.03149) | Ruohan Gao, Kristen Grauman |

### 2020

| Date | Title | Authors |
|------|-------|---------|
| 2020-12-14 | [Multi Modal Adaptive Normalization for Audio to Video Generation](https://arxiv.org/abs/2012.07304) | Neeraj Kumar, Srishti Goel, Ankur Narang, Brejesh Lall |
| 2020-12-14 | [Robust One Shot Audio to Video Generation](https://arxiv.org/abs/2012.07842) | Neeraj Kumar, Srishti Goel, Ankur Narang, Mujtaba Hasan |
| 2020-11-30 | [One-Shot Free-View Neural Talking-Head Synthesis for Video Conferencing](https://arxiv.org/abs/2011.15126) | Ting-Chun Wang, Arun Mallya, Ming-Yu Liu |
| 2020-11-30 | [Adaptive Compact Attention For Few-shot Video-to-video Translation](https://arxiv.org/abs/2011.14695) | Risheng Huang, Li Shen, Xuan Wang, Cheng Lin, Hao-Zhi Huang |
| 2020-11-29 | [Audio-visual Speech Separation with Adversarially Disentangled Visual Representation](https://arxiv.org/abs/2011.14334) | Peng Zhang, Jiaming Xu, Jing shi, Yunzhe Hao, Bo Xu |
| 2020-11-21 | [Stochastic Talking Face Generation Using Latent Distribution Matching](https://arxiv.org/abs/2011.10727) | Ravindra Yadav, Ashish Sardana, Vinay P Namboodiri, Rajesh M Hegde |
| 2020-11-21 | [Iterative Text-based Editing of Talking-heads Using Neural Retargeting](https://arxiv.org/abs/2011.10688) | Xinwei Yao, Ohad Fried, Kayvon Fatahalian, Maneesh Agrawala |
| 2020-11-09 | [An Empirical Study of Visual Features for DNN based Audio-Visual Speech Enhancement in Multi-talker Environments](https://arxiv.org/abs/2011.04359) | Shrishti Saha Shetu, Soumitro Chakrabarty, Emanuël A. P. Habets |
| 2020-11-09 | [FACEGAN: Facial Attribute Controllable rEenactment GAN](https://arxiv.org/abs/2011.04439) | Soumya Tripathy, Juho Kannala, Esa Rahtu |
| 2020-11-02 | [Facial Keypoint Sequence Generation from Audio](https://arxiv.org/abs/2011.01114) | Prateek Manocha, Prithwijit Guha |
| 2020-10-25 | [APB2FaceV2: Real-Time Audio-Guided Multi-Face Reenactment](https://arxiv.org/abs/2010.13017) | Jiangning Zhang, Xianfang Zeng, Chao Xu, Jun Chen et al. |
| 2020-10-09 | [Audio-Visual Speech Inpainting with Deep Learning](https://arxiv.org/abs/2010.04556) | Giovanni Morrone, Daniel Michelsanti, Zheng-Hua Tan, Jesper Jensen |
| 2020-10-05 | [SMILE: Semantically-guided Multi-attribute Image and Layout Editing](https://arxiv.org/abs/2010.02315) | Andrés Romero, Luc Van Gool, Radu Timofte |
| 2020-09-21 | [Correlating Subword Articulation with Lip Shapes for Embedding Aware Audio-Visual Speech Enhancement](https://arxiv.org/abs/2009.09561) | Hang Chen, Jun Du, Yu Hu, Li-Rong Dai et al. |
| 2020-09-12 | [DualLip: A System for Joint Lip Reading and Generation](https://arxiv.org/abs/2009.05784) | Weicong Chen, Xu Tan, Yingce Xia, Tao Qin et al. |
| 2020-09-02 | [Seeing wake words: Audio-visual Keyword Spotting](https://arxiv.org/abs/2009.01225) | Liliane Momeni, Triantafyllos Afouras, Themos Stafylakis, Samuel Albanie, Andrew Zisserman |
| 2020-08-30 | [Improved Lite Audio-Visual Speech Enhancement](https://arxiv.org/abs/2008.13222) | Shang-Yi Chuang, Hsin-Min Wang, Yu Tsao |
| 2020-08-29 | ["It took me almost 30 minutes to practice this". Performance and Production Practices in Dance Challenge Videos on TikTok](https://arxiv.org/abs/2008.13040) | Daniel Klug |
| 2020-08-23 | [A Lip Sync Expert Is All You Need for Speech to Lip Generation In The Wild](https://arxiv.org/abs/2008.10010) | K R Prajwal, Rudrabha Mukhopadhyay, Vinay Namboodiri, C V Jawahar |
| 2020-08-21 | [An Overview of Deep-Learning-Based Audio-Visual Speech Enhancement and Separation](https://arxiv.org/abs/2008.09586) | Daniel Michelsanti, Zheng-Hua Tan, Shi-Xiong Zhang, Yong Xu et al. |
| 2020-08-18 | [Mesh Guided One-shot Face Reenactment using Graph Convolutional Networks](https://arxiv.org/abs/2008.07783) | Guangming Yao, Yi Yuan, Tianjia Shao, Kun Zhou |
| 2020-08-17 | [Deep Variational Generative Models for Audio-visual Speech Separation](https://arxiv.org/abs/2008.07191) | Viet-Nhat Nguyen, Mostafa Sadeghi, Elisa Ricci, Xavier Alameda-Pineda |
| 2020-08-08 | [Speech Driven Talking Face Generation from a Single Image and an Emotion Condition](https://arxiv.org/abs/2008.03592) | Sefik Emre Eskimez, You Zhang, Zhiyao Duan |
| 2020-08-03 | [Audiovisual Speech Synthesis using Tacotron2](https://arxiv.org/abs/2008.00620) | Ahmed Hussen Abdelaziz, Anushree Prasanna Kumar, Chloe Seivwright, Gabriele Fanelli et al. |
| 2020-08-02 | [Deep Multi-modality Soft-decoding of Very Low Bit-rate Face Videos](https://arxiv.org/abs/2008.01652) | Yanhui Guo, Xi Zhang, Xiaolin Wu |
| 2020-07-21 | [CSLNSpeech: solving extended speech separation problem with the help of Chinese sign language](https://arxiv.org/abs/2007.10629) | Jiasong Wu, Xuan Li, Taotao Li, Fanman Meng et al. |
| 2020-07-16 | [Talking-head Generation with Rhythmic Head Motion](https://arxiv.org/abs/2007.08547) | Lele Chen, Guofeng Cui, Celong Liu, Zhong Li et al. |
| 2020-07-08 | [Learning Speech Representations from Raw Audio by Joint Audiovisual Self-Supervision](https://arxiv.org/abs/2007.04134) | Abhinav Shukla, Stavros Petridis, Maja Pantic |
| 2020-06-20 | [Speaker Independent and Multilingual/Mixlingual Speech-Driven Talking Head Generation Using Phonetic Posteriorgrams](https://arxiv.org/abs/2006.11610) | Huirong Huang, Zhiyong Wu, Shiyin Kang, Dongyang Dai et al. |
| 2020-05-29 | [Not made for each other- Audio-Visual Dissonance-based Deepfake Detection and Localization](https://arxiv.org/abs/2005.14405) | Komal Chugh, Parul Gupta, Abhinav Dhall, Ramanathan Subramanian |
| 2020-05-27 | [Modality Dropout for Improved Performance-driven Talking Faces](https://arxiv.org/abs/2005.13616) | Ahmed Hussen Abdelaziz, Barry-John Theobald, Paul Dixon, Reinhard Knothe et al. |
| 2020-05-25 | [Identity-Preserving Realistic Talking Face Generation](https://arxiv.org/abs/2005.12318) | Sanjana Sinha, Sandika Biswas, Brojeshwar Bhowmick |
| 2020-05-24 | [Lite Audio-Visual Speech Enhancement](https://arxiv.org/abs/2005.11769) | Shang-Yi Chuang, Yu Tsao, Chen-Chou Lo, Hsin-Min Wang |
| 2020-05-18 | [End-to-End Lip Synchronisation Based on Pattern Classification](https://arxiv.org/abs/2005.08606) | You Jin Kim, Hee Soo Heo, Soo-Whan Chung, Bong-Jin Lee |
| 2020-05-14 | [FaceFilter: Audio-visual speech separation using still images](https://arxiv.org/abs/2005.07074) | Soo-Whan Chung, Soyeon Choe, Joon Son Chung, Hong-Goo Kang |
| 2020-05-13 | [FaR-GAN for One-Shot Face Reenactment](https://arxiv.org/abs/2005.06402) | Hanxiang Hao, Sriram Baireddy, Amy R. Reibman, Edward J. Delp |
| 2020-05-07 | [What comprises a good talking-head video generation?: A Survey and Benchmark](https://arxiv.org/abs/2005.03201) | Lele Chen, Guofeng Cui, Ziyi Kou, Haitian Zheng, Chenliang Xu |
| 2020-04-30 | [APB2Face: Audio-guided face reenactment with auxiliary pose and blink signals](https://arxiv.org/abs/2004.14569) | Jiangning Zhang, Liang Liu, Zhucun Xue, Yong Liu |
| 2020-04-27 | [MakeItTalk: Speaker-Aware Talking-Head Animation](https://arxiv.org/abs/2004.12992) | Yang Zhou, Xintong Han, Eli Shechtman, Jose Echevarria et al. |
| 2020-04-11 | [Dancing to the Partisan Beat: A First Analysis of Political Communication on TikTok](https://arxiv.org/abs/2004.05478) | Juan Carlos Medina Serrano, Orestis Papakyriakopoulos, Simon Hegelich |
| 2020-03-30 | [ActGAN: Flexible and Efficient One-shot Face Reenactment](https://arxiv.org/abs/2003.13840) | Ivan Kosarevych, Marian Petruk, Markian Kostiv, Orest Kupyn et al. |
| 2020-03-29 | [Realistic Face Reenactment via Self-Supervised Disentangling of Identity and Pose](https://arxiv.org/abs/2003.12957) | Xianfang Zeng, Yusu Pan, Mengmeng Wang, Jiangning Zhang, Yong Liu |
| 2020-03-05 | [Talking-Heads Attention](https://arxiv.org/abs/2003.02436) | Noam Shazeer, Zhenzhong Lan, Youlong Cheng, Nan Ding, Le Hou |
| 2020-03-01 | [Towards Automatic Face-to-Face Translation](https://arxiv.org/abs/2003.00418) | Prajwal K R, Rudrabha Mukhopadhyay, Jerin Philip, Abhishek Jha et al. |
| 2020-02-24 | [Audio-driven Talking Face Video Generation with Learning-based Personalized Head Pose](https://arxiv.org/abs/2002.10137) | Ran Yi, Zipeng Ye, Juyong Zhang, Hujun Bao, Yong-Jin Liu |
| 2020-02-20 | [A Neural Lip-Sync Framework for Synthesizing Photorealistic Virtual News Anchors](https://arxiv.org/abs/2002.08700) | Ruobing Zheng, Zhou Zhu, Bo Song, Changjiang Ji |
| 2020-02-20 | [Disentangled Speech Embeddings using Cross-modal Self-supervision](https://arxiv.org/abs/2002.08742) | Arsha Nagrani, Joon Son Chung, Samuel Albanie, Andrew Zisserman |
<!-- PAPERS_TABLE_END -->
