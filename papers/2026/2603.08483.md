---
arxiv_id: "2603.08483"
title: "X-AVDT: Audio-Visual Cross-Attention for Robust Deepfake Detection"
authors:
  - Youngseo Kim
  - Kwan Yun
  - Seokhyeon Hong
  - Sihun Cha
  - Colette Suhjung Koo
  - Junyong Noh
submitted: "2026-03-09"
categories: []
arxiv_url: https://arxiv.org/abs/2603.08483
source: arxiv-html
converter: pandoc
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-21T00:10:35+00:00"
references_parsed: 0
arxiv_version: ""
---

# X-AVDT: Audio-Visual Cross-Attention for Robust Deepfake Detection

Youngseo Kim Kwan Yun Seokhyeon Hong Sihun Cha Colette Suhjung Koo Junyong Noh \
Visual Media Lab, KAIST

###### Abstract

The surge of highly realistic synthetic videos produced by contemporary generative systems has significantly increased the risk of malicious use, challenging both humans and existing detectors. Against this backdrop, we take a generator-side view and observe that internal cross-attention mechanisms in these models encode fine-grained speech–motion alignment, offering useful correspondence cues for forgery detection. Building on this insight, we propose X-AVDT, a robust and generalizable deepfake detector that probes generator-internal audio-visual signals accessed via DDIM inversion to expose these cues. X-AVDT extracts two complementary signals: (i) a video composite capturing inversion-induced discrepancies, and (ii) audio–visual cross-attention feature reflecting modality alignment enforced during generation. To enable faithful, cross-generator evaluation, we further introduce MMDF, a new multi-modal deepfake dataset spanning diverse manipulation types and rapidly evolving synthesis paradigms, including GANs, diffusion, and flow-matching. Extensive experiments demonstrate that X-AVDT achieves leading performance on MMDF and generalizes strongly to external benchmarks and unseen generators, outperforming existing methods with accuracy improved by +13.1%. Our findings highlight the importance of leveraging internal audio–visual consistency cues for robustness to future generators in deepfake detection. Code is available at [X-AVDT](https://youngseo0526.github.io/X-AVDT/).

## 1 Introduction

Deepfakes, synthetic or edited portrait videos that manipulate identity, speech, or motion, have become feasible with advances in generative video models. These models have evolved from Generative Adversarial Networks (GANs) \[26\] to diffusion-based models \[70, 33\], which push fidelity to unprecedented levels. Recent systems \[17, 87, 32\] can synthesize photorealistic digital humans from minimal input, lowering production costs for creative media and assistants. However, when misused, the same advances heighten societal and security risks, including targeted disinformation, real-time impersonation, identity theft, and financial fraud \[15, 81, 19, 22, 6, 27\]. These concerns have motivated the research community to develop deepfake detection, which aims to reliably authenticate media under rapidly evolving generators.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/0_av_attn_map.png)

Figure 1: Temporally averaged cross-attention maps. For each video, we extract audio–visual cross-attention during DDIM inversion and average the maps over all frames to obtain a single heatmap. Real vs. fake samples exhibit consistent disparities.

Diffusion models have become central to recent facial forgery generation. Many video generators employ cross-attention \[83\] to condition visual features on external signals such as text, motion, or audio \[4, 84, 13\]. Among these external signals, audio is especially useful as it provides frame synchronous, densely informative supervision aligned with facial dynamics. In audio-driven diffusion models, this conditioning often takes the form of audio–visual cross-attention, which ties phonetic content to facial motion and expressiveness. Such architectures are explicitly designed to promote audio-visual alignment via cross-attention in the diffusion U-Net, making their internal features a natural source of correspondence cues for deepfake detection. Figure 1 presents examples of extracted audio-visual cross attention features, using Hallo \[90\], an audio-driven talking head diffusion model pretrained on a large corpus of speech videos. It is observed that similar attention patterns recur across different generator frameworks. This indicates that internal audio–visual cross-attention features from diffusion models provide a robust, generator-agnostic discriminative signal for deepfake detection, reinforcing this generality.

|                        |          |        |     |     |       |     |     |
| ---------------------- | -------- | ------ | --- | --- | ----- | --- | --- |
| Dataset                | Modality | Method |     |     | Model |     |     |
|                        |          | FS     | RE  | TH  | GAN   | DF  | FM  |
| Celeb-DF \[48\]        | V        | ✓      | ✗   | ✗   | ✓     | ✗   | ✗   |
| DF-Platter \[60\]      | V        | ✓      | ✓   | ✗   | ✓     | ✗   | ✗   |
| KoDF \[40\]            | AV       | ✓      | ✓   | ✓   | ✓     | ✗   | ✗   |
| FaceForensics++ \[71\] | AV       | ✓      | ✓   | ✗   | ✓     | ✗   | ✗   |
| DFDC \[21 dataset")\]  | AV       | ✓      | ✗   | ✗   | ✓     | ✗   | ✗   |
| FakeAVCeleb \[38\]     | AV       | ✓      | ✗   | ✓   | ✓     | ✗   | ✗   |
| AV-Deepfake1M \[8\]    | AV       | ✗      | ✗   | ✓   | ✓     | ✗   | ✗   |
| MMDF (Ours)            | AV       | ✓      | ✓   | ✓   | ✓     | ✓   | ✓   |

Table 1: Comparison of deepfake video datasets. FS:Face swapping, RE: Self-reenactment, TH: Talking-head generation, DF: Diffusion model, FM: Flow-matching.

Building on this observation, we propose X-AVDT, an Audio-Visual Cross-Attention framework for robust Deepfake deTection. Our framework leverages the cross-modal interaction of videos by utilizing fine-grained audio-visual diffusion features to generalize across manipulation types and synthesis models. To extract internal signals, we employ an inversion scheme that maps input videos into the diffusion model’s latent space and reconstructs them under the model prior. We further incorporate a latent noise map, reconstructed video, and input-reconstruction residual as complementary spatial cues, motivated by findings that pretrained diffusion models more faithfully reconstruct diffusion-generated content than real content \[86, 9\]. While fully synthetic videos often expose global inconsistencies, face-centric manipulations are confined to the facial region, preserve identity, and yield subtle artifacts that are easily obscured, thereby challenging residual-only detectors \[86, 9\]. By augmenting inversion-based discrepancies with audio-visual cross-attention and fusing them into a unified representation, X-AVDT provides complementary global and localized evidence that can improve detection reliability.

Existing datasets \[44, 48, 21 dataset")\] are largely composed of earlier GAN-generated forgeries, offering limited coverage of contemporary models and manipulation types. As a result, they fail to capture the diversity and realism of continuously updated diffusion or flow-based methods, constraining progress toward building detectors that generalize beyond legacy benchmarks. To further facilitate robust detection of rapidly evolving deepfakes, we introduce MMDF, a curated Multi-modal, Multi-generator DeepFake dataset. It is a high-quality dataset of paired real videos and corresponding fakes generated by a diverse suite of recent synthesis models. MMDF is the first dataset to cover contemporary diffusion (both U-Net \[70\] based and transformer \[63\] based) and flow-matching \[51\] generators, and it includes audio–visual pairs. The dataset also spans manipulation paradigms such as talking-head generation \[17, 13\], self-reenactment \[29, 91\], and face swapping \[32\], making it suitable for real-world, unconstrained deepfake detection. A comparison of MMDF with prior deepfake datasets is provided in Table 1.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/1_input.png)

Figure 2: Input representations with complementary features. (a) video composite $`\boldsymbol{\phi}`$ is obtained from video $`x`$ and audio $`c`$ by running DDIM inversion and reconstruction, decoding both the noisy and clean latents, and computing the residual. We then concatenate four components channel-wise: $`x`$, $`D(\hat{z}_{T})`$, $`D(\hat{z}_{0})`$, and $`\lvert x-D(\hat{z}_{0})\rvert`$. (b) AV cross-attention feature $`\boldsymbol{\psi}`$ is extracted during DDIM inversion from the diffusion U-Net and summarized as a frame-aligned tensor. These complementary cues (a) and (b) capture appearance information and modality alignment, respectively. For clarity, all visual elements shown ($`D(\hat{z}_{T})`$, $`D(\hat{z}_{0})`$, and $`\lvert x-D(\hat{z}_{0})\rvert`$) are decoded images.

## 2 Related Work

Deepfake Video Generation. The synthesis and editing of human faces in video, with high realism and temporal coherence, have been extensively studied. Early innovations in generative modeling were driven by GANs \[26\] with gains in stability, resolution, and controllability \[68, 36, 37\], along with basic conditional setups \[59, 35, 98\]. More recently, diffusion and flow-matching models \[70, 33, 13\] have shown remarkable success in portrait video manipulation for deepfakes. In parallel, control signals such as audio \[17, 87\], textual prompts \[88, 4\], facial landmarks \[94, 84\], dense motion flow \[94\], and 3D face priors \[64, 50\] have significantly enhanced the realism of synthetic videos. Moreover, current manipulation techniques include talking-head generation \[17, 13\], face reenactment \[29, 91\], face swapping \[32\], lip-sync/dubbing \[65, 96\], and appearance editing \[7\].

Artifact-based Deepfake Detection. Detection methods have evolved alongside deepfake video generation. Early attempts relied on hand-crafted forensic features, including blink detection \[46\], facial warping artifacts \[47\], or color inconsistencies \[58, 42\]. CNN-based classifiers trained on real and fake examples became dominant. Prior studies have demonstrated the effectiveness of deep learning for detecting subtle synthesis artifacts \[71, 1, 45, 28, 66, 76, 72, 85\]. Frequency-domain and fingerprint-based detectors further improved generalization across different GAN architectures \[25, 57\]. However, these methods often struggle to generalize beyond their training datasets and remain vulnerable to newer, more sophisticated forgeries.

Generalizable Deepfake Detection. A principal goal is generalization across unseen generators, manipulation types, and domains. To this end, recent work investigates the semantic characteristics of generated images. DIRE \[86\] proposes a reconstruction-based detector grounded in the hypothesis that images produced by diffusion models can be more accurately reconstructed by a pretrained diffusion model than real images. DRCT \[11\] extends this idea by synthesizing hard examples via diffusion reconstruction and applying contrastive learning to the resulting residuals. FakeInversion \[9\] leverages features obtained via latent inversion of Stable Diffusion \[70\]. These methods are built on prior observations that CLIP \[67\] embeddings can be predictive of image authenticity \[61, 74\].

Audio-Visual Inconsistencies. Several studies \[97, 23, 77, 39\] adopt a late-fusion design in which RGB images and audio are encoded separately and combined only at the classification head. While this preserves strong per-modality features, the resulting embeddings occupy different latent spaces and are not directly aligned across modalities. Other approaches \[30, 62, 49\] learn audio–visual representations in a self-supervised way, implicitly fusing the modalities by pulling their embeddings together. Such implicit fusion can miss fine-grained semantic misalignment and offers limited interpretability of the cross-modal evidence. In contrast, we focus on internal features from large generative models as explicit, interpretable signals of persistent audio-visual inconsistency.

## 3 Preliminaries

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/1_overview.png)

Figure 3: The overall framework of X-AVDT. From each audio-visual pair, we form two inputs $`\boldsymbol{\phi}`$ and $`\boldsymbol{\psi}`$. Two 3D encoders map them to features that are concatenated and passed through the Feature Fusion Decoder to produce a fused feature. A classification head outputs the real/fake score, while an embedding head is trained with a triplet objective to improve robustness.

Diffusion models \[20, 33, 70\] are probabilistic generative models that learn a data distribution by progressively denoising samples. They consist of two complementary processes. In the forward process, Gaussian noise is gradually injected into a clean image $`x_{0}`$, given by

```math
x_{t}\;=\;\sqrt{\bar{\alpha}_{t}}\,x_{0}\;+\;\sqrt{1-\bar{\alpha}_{t}}\,\epsilon,\qquad\epsilon\sim\mathcal{N}(0,\mathbf{I})
```

which maps $`x_{0}`$ to increasingly noisy latents $`x_{t}`$, where $`t=0,\ldots,T`$ and $`\bar{\alpha}_{t}=\prod_{k=1}^{t}\alpha_{k}`$. The reverse process starts from a noisy sample $`x_{T}`$ and iteratively produces cleaner states conditioned on an auxiliary vector $`c`$ (e.g., audio), using a noise predictor $`\epsilon_{\theta}(x_{t},t,c)`$. Given the current estimate of the clean image,

```math
\hat{x}_{0}(x_{t},t,c)=\frac{x_{t}-\sqrt{1-\bar{\alpha}_{t}}\,\epsilon_{\theta}(x_{t},t,c)}{\sqrt{\bar{\alpha}_{t}}},
```

the conditional reverse update can be written as

```math
x_{t-1}=\sqrt{\bar{\alpha}_{t-1}}\,\hat{x}_{0}(x_{t},t,c)+\sqrt{1-\bar{\alpha}_{t-1}}\,\epsilon_{\theta}(x_{t},t,c).
```

In this work, we rely on a pre-trained audio-conditioned Latent Diffusion Model (LDM) \[70\], where the diffusion process operates in the latent space of a VAE: $`z_{0}=E(x_{0})`$ and $`x_{0}\approx D(z_{0})`$. The denoiser is a 3D U-Net conditioned on external signals and composed of residual blocks, spatial self-attention, temporal self-attention, and cross-attention. Let $`f^{l}_{n}`$ be the video features at layer $`l`$ and video frame $`n`$, projected to queries $`q_{n}^{l}`$, keys $`k_{n}^{l}`$, and values $`v_{n}^{l}`$. The attention output is given by

```math
\tilde{f}^{\,l}_{n}\;=\;A_{n}^{l}\,v_{n}^{l},\qquad A_{n}^{l}\;=\;\mathrm{Softmax}\!\left(\frac{q_{n}^{l}(k_{n}^{l})^{\!\top}}{\sqrt{d}}\right),
```

where $`d`$ is the query/key embedding dimension. This enables the model to capture global dependencies across space and time in the video. In parallel, cross-attention is computed between video queries and the conditioning audio embedding, thereby guiding the denoising process toward the target reconstruction.

## 4 Method

### 4.1 Problem Definition

We train a binary deepfake detector on audio–visual pairs $`\mathcal{D}_{\text{train}}=\{(x_{m},c_{m},y_{m})\}_{m=1}^{M}`$, where each example consists of a face video clip $`x_{m}`$, its paired audio condition $`c_{m}`$, and a label $`y_{m}\in\{0,1\}`$ that indicates whether the video is real or fake. The training set contains $`M`$ videos. From each input pair, an audio-conditioned LDM extracts two types of features, video composite $`\boldsymbol{\phi}(x,c)`$ and an AV cross-attention feature $`\boldsymbol{\psi}(x,c)`$, as illustrated in Figure 2 and discussed in Sec. 4.2. We fuse $`\boldsymbol{\phi}`$ and $`\boldsymbol{\psi}`$ and train a detector $`G_{\theta}`$ to estimate $`p_{\theta}(y=1\mid x,c)=\sigma(G_{\theta}(\cdot))`$ by optimizing a weighted sum of a binary cross-entropy term and a metric-learning term, which will be defined in Sec. 4.3.

### 4.2 Input Representation

#### 4.2.1 Diffusion Inversion & Reconstruction

As shown in Figure 2a, given a video $`x\in\mathbb{R}^{N\times 3\times H\times W}`$, where $`N`$ denotes the number of frames in the clip and $`H`$ and $`W`$ denote the height and width, respectively, and a paired audio condition $`c`$, we operate in the VAE latent space with encoder $`E`$ and decoder $`D`$. We first encode the input video frame to $`z_{0}=E(x)`$ while conditioning on the wav2vec 2.0 \[3\] audio embedding c (omitted in the figure for brevity). We then obtain the corresponding latent noise map using the DDIM inversion process $`\hat{z}_{T}=F_{\theta}(z_{0},c)`$. Subsequently, starting from $`\hat{z}_{T}`$, we run the conditional reverse diffusion to obtain a clean latent $`\hat{z}_{0}=R_{\theta}(\hat{z}_{T},c)`$. We then decode $`\hat{z}_{0}`$ to the pixel space to obtain the reconstructed video $`D(\hat{z}_{0})`$ and compute the residual between the input and the reconstruction $`r=\lvert x-D(\hat{z}_{0})\rvert`$.

To construct the video composite $`\boldsymbol{\phi}`$ for the detector, we use an input formed by channel-wise concatenation of the image $`x`$, the decoded latent DDIM noise map $`D(\hat{z}_{T})`$, the image $`D(\hat{z}_{0})`$ reconstructed from the reverse DDIM process, and the reconstruction residual $`r=\lvert x-D(\hat{z}_{0})\rvert`$:

```math
\boldsymbol{\phi}(x,c)=\mathrm{concat}\big[\,x,\;D(\hat{z}_{T}),\;D(\hat{z}_{0}),\;r\,\big]\in\mathbb{R}^{N\times 12\times H\times W},
```

Because DDIM inversion uses a finite number of steps, the mismatch after a forward-reverse pass reflects discretization error, whereas manipulated samples tend to produce smaller discrepancies and thus higher likelihood of forgery under the diffusion model \[9\]. We use the pattern of this gap as an inversion-induced discrepancy measure for detecting manipulation.

#### 4.2.2 Audio-Visual Cross-Attention Feature

As illustrated in Figure 2b, DDIM inversion is performed with a 3D U-Net composed of multiple blocks organized into down, mid and up stages. Each block contains an audio-visual cross-attention layer in which video hidden states serve as queries while the audio encoder’s hidden states provide keys and values. We extract the cross-attention from an up block at a chosen diffusion timestep $`t`$, conditioned on the input audio. This attention is taken from the same conditioned LDM used to construct the video composite $`\boldsymbol{\phi}`$.

Let $`H(t)`$ be the 3D U-Net hidden state at timestep $`t`$. Using the attention output projection, we aggregate the multi-head outputs, reduce the head dimension to $`C`$ channels, and reshape the result into the per-frame latent grid, yielding a temporally aligned feature $`\boldsymbol{\psi}(x,c)`$, which is defined as:

```math
\boldsymbol{\psi}(x,c)=\mathrm{CrossAttn}\!\left(H(t),\,c\right)\in\mathbb{R}^{N\times C\times h\times w},
```

Here, $`h\times w`$ is the latent-space resolution (e.g., $`64\times 64`$ for $`512\times 512`$ inputs with an 8x downsampling). In our setup, we extract the attention from the last up block at timestep $`t=24`$ and reshape it to a per-frame. The resulting $`\boldsymbol{\psi}`$ provides a compact, temporally aligned descriptor of audio–visual correspondence that the detector can exploit to distinguish authentic from manipulated content. Because it captures speech–motion synchrony enforced by the denoiser instead of appearance alone, it is less sensitive to purely visual artifacts and thus offers a complementary, model-internal cue that improves robustness. Ablation on input representations and attention features appear in Sec. 6.4.

### 4.3 Detector Architecture

Figure 3 presents the X-AVDT framework. X-AVDT pairs two signals extracted from different parts of the conditioned LDM pipeline to improve robustness. Accordingly, the detector takes two inputs. Two 3D encoders, $`E_{v}`$ for $`\boldsymbol{\phi}`$ and $`E_{a}`$ for $`\boldsymbol{\psi}`$, produce feature volumes that are aligned in space and time and then fused by a Feature Fusion Decoder (FFD) to yield a logit and an embedding:

```math
\mathbf{v}^{\prime}=E_{v}(\boldsymbol{\phi}),\qquad\mathbf{a}^{\prime}=E_{a}(\boldsymbol{\psi}).
```

The tensors $`\mathbf{v}^{\prime}`$ and $`\mathbf{a}^{\prime}`$ are concatenated along the channel dimension and projected to a shared embedding with a $`1{\times}1`$ convolution to obtain $`\mathbf{p}_{i}`$. The FFD then applies a self-attention layer over spatial tokens, followed by a series of $`L`$ 3D ResNeXt \[89\] layers. Then global average pooling (GAP) produces a fused feature vector $`\mathbf{g}_{i}`$ for the $`i`$-th sample:

$`\displaystyle\mathbf{p}_{i}`$$`\displaystyle=\mathrm{Proj}\!\left(\mathrm{concat}\!\left[\mathbf{v}^{\prime}_{i},\mathbf{a}^{\prime}_{i}\right]\right),`$$`\displaystyle\mathbf{g}_{i}`$$`\displaystyle=\mathrm{GAP}\!\left(\mathrm{Conv3D}^{L}\!\big(\mathrm{SelfAttn}(\mathbf{p}_{i})\big)\right).`$

From $`\mathbf{g}_{i}`$ we form two branches: a fully connected layer maps $`\mathbf{g}_{i}`$ to a scalar logit $`s_{i}`$ for the binary classification loss, and an embedding head outputs an $`\ell_{2}`$-normalized vector $`\mathbf{u}^{(i)}`$ for metric learning. With ground-truth labels $`y_{i}\in\{0,1\}`$ (real=0, fake=1) and sigmoid $`\sigma(\cdot)`$, the binary cross-entropy loss over a mini-batch of size $`B`$ is defined as follows:

```math
\mathcal{L}_{\text{bce}}=-\frac{1}{B}\sum_{i=1}^{B}\Big[y_{i}\log\sigma(s_{i})+(1-y_{i})\log\bigl(1-\sigma(s_{i})\bigr)\Big].
```

Let $`\mathbf{u}_{a}^{(i)}`$, $`\mathbf{u}_{p}^{(i)}`$, and $`\mathbf{u}_{n}^{(i)}`$ denote anchor, positive, and negative embeddings for the $`i`$-th triplet, respectively. It tightens same class embeddings and separates different classes. Using the squared $`\ell_{2}`$ distance and a margin $`m>0`$, the triplet loss is

```math
\mathcal{L}_{\text{tri}}=\frac{1}{B}\sum_{i=1}^{B}\max\bigl(0,\;\left\|\mathbf{u}_{a}^{(i)}-\mathbf{u}_{p}^{(i)}\right\|_{2}^{2}-\left\|\mathbf{u}_{a}^{(i)}-\mathbf{u}_{n}^{(i)}\right\|_{2}^{2}+m\bigr).
```

The overall objective minimizes a weighted sum of the two terms, controlled by a balancing parameter $`\lambda\in[0,1]`$:

```math
\mathcal{L}_{\text{total}}=(1-\lambda)\,\mathcal{L}_{\text{bce}}+\lambda\,\mathcal{L}_{\text{tri}}.
```

This joint objective allows the model to learn discriminative and mutually informative representations that generalize across manipulation patterns. Further analysis is provided in Sec. 6.4.

## 5 Dataset

The MMDF dataset was constructed from curated real clips paired with their corresponding manipulated versions, resulting in a collection of 28.8k clips with a total duration of 41.67 hours. Using Hallo3 dataset \[18\] as our source, we applied each video clip duration, resolution, and face-presence filters with MediaPipe \[55\] to retain single-person, frontal-to-quarter views with stable lip motion and speech. We removed clips with scene cuts, strong camera motion, excessive facial motion, or long side facing poses. These videos contain individuals of diverse ages, ethnicities, and genders in close-up shots across varied indoor and outdoor backgrounds. MMDF covers three manipulation types, such as talking-head generation, self-reenactment, and face swapping, produced using GAN, diffusion, and flow-matching generators. Comparative networks were trained on a diverse set of data obtained from commonly used generators and evaluated on unseen ones to assess cross-generator generalization. See Table 2 for details.

|       |                            |                       |                  |                     |
| ----- | -------------------------- | --------------------- | ---------------- | ------------------- |
| Split | Generator                  | Model                 | Method           | \#Clips (real/fake) |
| Train | Hallo2 \[17\]              | Diffusion             | Talking-Head     | 4k/4k               |
|       | LivePortrait \[29\]        | GAN                   | Self-Reenactment | 4k/4k               |
|       | FaceAdapter \[32\]         | Diffusion             | Face Swapping    | 4k/4k               |
| Test  | HunyuanAvatar \[13\]       | Flow Matching         | Talking-Head     | 0.8k/0.8k           |
|       | MegActor-$`\Sigma`$ \[91\] | Diffusion Transformer | Self-Reenactment | 0.8k/0.8k           |
|       | AniPortrait \[87\]         | Diffusion             | Talking-Head     | 0.8k/0.8k           |

Table 2: Composition of the dataset. This coverage better reflects current synthesis trends than outdated datasets that focus primarily on GANs, and permits assessing cross-generator generalization.

|                        |                     |                       |                      |                    |                   |
| ---------------------- | ------------------- | --------------------- | -------------------- | ------------------ | ----------------- |
| Dataset                | Sync-C $`\uparrow`$ | Sync-D $`\downarrow`$ | LPIPS $`\downarrow`$ | FVD $`\downarrow`$ | HFAR $`\uparrow`$ |
| FaceForensics++ \[71\] | 3.32                | 11.06                 | 0.27                 | 370.23             | 0.22              |
| FakeAVCeleb \[38\]     | 5.87                | 8.38                  | 0.19                 | 170.61             | 0.34              |
| MMDF (Ours)            | 7.36                | 7.35                  | 0.07                 | 121.39             | 0.41              |

Table 3: Audio-visual quality of manipulated videos. Sync-C, Sync-D, LPIPS, and FVD are computational metrics, whereas HFAR denotes the human false acceptance rate measured in a user study.

To quantify the realism of the manipulated videos, we report several metrics values. As shown in Table 3, MMDF exhibits stronger audio–visual synchronization and more favorable perceptual and video statistics than FaceForensics++ \[71\] and FakeAVCeleb \[38\], indicating temporally coherent, high-quality manipulations suitable for the detection task. In addition, we report Human False Acceptance Rate (HFAR), defined as the proportion of fake clips judged to be real by human evaluators (i.e., False Positive Rate, FPR). A higher HFAR indicates that humans are more likely to perceive fake clips as real, suggesting that the dataset contains more challenging and realistic negative samples. Metric definitions are provided in Sec. 6.1 and MMDF details are in the supplementary material.

|                                           |                    |       |         |       |                            |       |         |       |                      |       |         |       |         |       |         |       |
| ----------------------------------------- | ------------------ | ----- | ------- | ----- | -------------------------- | ----- | ------- | ----- | -------------------- | ----- | ------- | ----- | ------- | ----- | ------- | ----- |
|                                           | AniPortrait \[87\] |       |         |       | MegActor-$`\Sigma`$ \[91\] |       |         |       | HunyuanAvatar \[13\] |       |         |       | Average |       |         |       |
| Model                                     | AUROC              | AP    | Acc@EER | Acc   | AUROC                      | AP    | Acc@EER | Acc   | AUROC                | AP    | Acc@EER | Acc   | AUROC   | AP    | Acc@EER | Acc   |
| Official-pretrained                       |                    |       |         |       |                            |       |         |       |                      |       |         |       |         |       |         |       |
| LipForensics \[31\]                       | 79.49              | 81.45 | 73.25   | 74.50 | 72.17                      | 73.56 | 65.85   | 67.11 | 63.66                | 56.50 | 59.91   | 60.66 | 74.24   | 74.54 | 71.91   | 72.38 |
| RealForensics \[30\]                      | 86.31              | 85.23 | 78.65   | 77.56 | 62.93                      | 61.60 | 58.79   | 58.71 | 64.90                | 60.30 | 61.40   | 60.85 | 77.65   | 75.71 | 72.15   | 65.70 |
| AVAD \[23\]                               | 73.25              | 74.98 | 66.05   | 67.49 | 50.87                      | 56.96 | 51.26   | 51.18 | 75.37                | 74.54 | 74.14   | 74.39 | 67.47   | 67.29 | 64.75   | 65.29 |
| FACTOR \[69\]                             | 94.21              | 93.54 | 86.29   | 86.55 | 75.44                      | 72.83 | 68.82   | 69.33 | 36.69                | 46.18 | 38.27   | 56.15 | 68.78   | 70.85 | 64.46   | 70.68 |
| LipFD \[53\]                              | 52.55              | 50.60 | 51.74   | 51.90 | 51.45                      | 49.89 | 50.80   | 50.93 | 60.38                | 53.85 | 57.78   | 58.30 | 57.64   | 51.83 | 55.37   | 55.82 |
| AVH-Align \[77\]                          | 74.88              | 73.94 | 68.82   | 70.03 | 51.20                      | 47.81 | 50.86   | 50.93 | 34.53                | 39.96 | 37.50   | 36.91 | 50.34   | 50.95 | 49.89   | 49.98 |
| MMDF-retrained (cross-dataset evaluation) |                    |       |         |       |                            |       |         |       |                      |       |         |       |         |       |         |       |
| RealForensics \[30\]                      | 97.47              | 97.22 | 90.99   | 90.28 | 97.60                      | 96.70 | 92.68   | 92.45 | 74.89                | 72.09 | 68.38   | 61.12 | 92.42   | 91.39 | 84.01   | 81.28 |
| LipFD \[53\]                              | 49.59              | 50.26 | 49.79   | 49.75 | 50.32                      | 50.82 | 50.14   | 50.18 | 48.39                | 50.26 | 49.10   | 48.96 | 53.75   | 51.29 | 52.65   | 52.87 |
| AVH-Align \[77\]                          | 98.94              | 98.53 | 95.94   | 96.54 | 67.92                      | 62.36 | 62.24   | 63.38 | 75.92                | 65.87 | 69.70   | 70.94 | 81.44   | 76.52 | 75.59   | 76.76 |
| Human Evaluation                          | –                  | –     | –       | 83.75 | –                          | –     | –       | 74.17 | –                    | –     | –       | 58.33 | –       | –     | –       | 71.88 |
| X-AVDT (Ours)                             | 99.10              | 98.89 | 96.54   | 97.05 | 90.17                      | 88.05 | 83.11   | 84.52 | 97.79                | 97.44 | 97.69   | 97.91 | 95.29   | 94.03 | 91.15   | 91.98 |

Table 4: Quantitative comparison on the MMDF dataset. Detectors are evaluated using the official pretrained checkpoint (first panel) and after retrained on the MMDF training set (Hallo2 \[17\], LivePortrait \[29\], and FaceAdapter \[32\]) (second panel). Best in bold; second-best underlined. ^(\*)Note: FACTOR is a zero-shot method, while AVAD and AVH-Align are unsupervised methods.

FakeAVCeleb \[38\] FaceForensics++ \[71\] Model AUROC AP Acc@EER Acc AUROC AP Acc@EER Acc Official pretrained LipForensics \[31\] 98.40 98.37 95.00 95.80 98.14^(†) 97.93^(†) 97.00^(†) 98.50^(†) RealForensics \[30\] 95.80 96.20 85.99 85.46 99.47^(†) 99.42^(†) 95.49^(†) 95.22^(†) AVAD \[23\] 74.96 75.88 66.00 66.79 55.38 53.92 51.50 52.16 FACTOR \[69\] 88.44 88.22 76.00 80.00 76.33 76.08 68.50 71.00 LipFD \[53\] 73.17 64.39 66.36 67.16 52.84^(†) 51.01^(†) 50.96^(†) 59.31^(†) AVH-Align \[77\] 93.52 93.48 83.00 83.90 37.07 40.43 40.50 41.62 MMDF-trained (cross-dataset evaluation) RealForensics \[30\] 83.67 85.56 71.42 71.42 88.85 87.65 79.39 78.54 LipFD \[53\] 53.59 51.09 52.37 53.67 52.92 50.21 52.08 51.89 AVH-Align \[77\] 54.20 53.74 52.00 52.80 36.66 40.03 37.00 39.64 Human Evaluation – – – 78.75 – – – 71.25 X-AVDT (Ours) 99.69 99.74 97.85 98.65 89.55 89.17 87.55 89.77

Table 5: Quantitative comparison on the benchmark dataset. Detectors are trained on the MMDF training set and evaluated on FakeAVCeleb and FaceForensics++, respectively. ^(†)Indicates that the corresponding benchmark was used during the method’s original training (train–test overlap).

## 6 Experiments

### 6.1 Implementation Details

X-AVDT is implemented and trained with the same configuration across all evaluation datasets. Training requires 14 hours on a single NVIDIA RTX 3090 GPU.

Architecture. Hallo \[90\] is employed as our audio-conditioned latent diffusion backbone, initialized from Stable Diffusion \[70\]. While we choose Hallo because it provides high-fidelity synthesis and rich internal audio–visual signals that our detector can exploit, other choices can also be possible \[52, 87, 14\]. See the supplementary material for details. Audio conditioning is provided by wav2vec 2.0 \[3\] features projected to the U-Net cross-attention embedding dimension. We do not use classifier-free guidance during either DDIM inversion or reconstruction to preserve bijectivity and conditioning fidelity. Unless otherwise stated, we extract the audio–visual cross-attention from the last up block of the U-Net at diffusion timestep $`t=24`$. Both the image encoder $`E_{v}(\cdot)`$ and the feature encoder $`E_{a}(\cdot)`$ use 3D ResNeXt \[89\]. The FFD uses an $`L`$-layer 3D ResNeXt stack. We fix $`L=3`$ in Eq. (8). In our setup, the video composite $`\boldsymbol{\phi}`$ has 12 channels ($`x`$, $`D(\hat{z}_{T})`$, $`D(\hat{z}_{0})`$, residual), and the AV cross-attention feature $`\boldsymbol{\psi}`$ uses $`C=320`$ channels after collapsing the multi-head dimension and is reshaped with a latent resolution of $`64\times 64`$.

Training Details. We train the detector for 2 epochs on frames of size $`512\times 512`$ using AdamW \[54\] with a learning rate of $`1\times 10^{-4}`$, weight decay of $`0.05`$, and a batch size of $`8`$. For the triplet loss Eq. (11), we set the margin $`m`$ to $`0.3`$, and the balancing parameter $`\lambda`$ in the overall objective Eq. (12) is also set to $`0.3`$.

Automatic Metrics. We report the values measured by four detection metrics, AUROC, Average Precision (AP), Accuracy at Equal Error Rate (Acc@EER), and Accuracy. We obtain Acc@EER by computing the EER threshold from the ROC curve and evaluating accuracy at that threshold. To assess the proposed MMDF dataset, we also report values measured by generation quality metrics including Lip Sync scores (Sync-C and Sync-D) from SyncNet for lip-speech alignment \[16\], LPIPS for perceptual distance \[95\], and Fréchet Video Distance (FVD) for distributional distance between generated and ground-truth videos \[82\]. Lower is better for LPIPS and FVD, higher Sync-C and lower Sync-D indicate better synchronization.

|                |                 |       |         |                    |       |         |                   |       |         |
| -------------- | --------------- | ----- | ------- | ------------------ | ----- | ------- | ----------------- | ----- | ------- |
|                | Cross-Attention |       |         | Temporal-Attention |       |         | Spatial-Attention |       |         |
| Timestep $`t`$ | AUROC           | AP    | Acc@EER | AUROC              | AP    | Acc@EER | AUROC             | AP    | Acc@EER |
| $`t=24`$       | 91.56           | 86.90 | 81.51   | 83.92              | 87.08 | 75.01   | 64.57             | 68.00 | 61.82   |
| $`t=249`$      | 81.30           | 69.52 | 77.13   | 68.25              | 71.94 | 64.10   | 57.42             | 52.00 | 56.04   |
| $`t=499`$      | 68.11           | 57.97 | 67.44   | 66.29              | 66.29 | 59.30   | 52.38             | 53.14 | 50.02   |

Table 6: Ablation results for different attention features and diffusion timesteps. As the diffusion timestep $`t`$ grows, the latent becomes noisier and conditioning weakens. Results at $`t\in\{24,249,499\}`$ show that cross-attention performs best, and performance degrades as $`t`$ increases.

Baselines. We evaluated X-AVDT against open-source baselines, including the video-only LipForensics \[31\], and audio–visual methods RealForensics \[30\], AVAD \[23\], LipFD \[53\], FACTOR \[69\], and AVH-Align \[77\]. We used two variants: (i) the official checkpoint and (ii) models retrained from scratch on our training sets using the official code. This protocol enables a fair cross-dataset transfer comparison against our MMDF-trained model. Further details are in the supplementary material.

### 6.2 Comparison with State-of-the-art

#### 6.2.1 Comparison on MMDF Dataset

Table 4 comprises two panels. Official-pretrained reports results from publicly released checkpoints of prior methods, and MMDF-retrained reports the same baselines retrained on our MMDF for cross-dataset evaluation. Baselines are evaluated in both settings, whereas X-AVDT values are reported in the MMDF-retrained panel. As the training code for LipForensics \[53\] and AVAD \[23\] is unavailable, we report results obtained by their official pretrained model only. The pretrained baselines presented in the first panel tended to overfit to earlier synthesis methods and showed limited domain adaptation capability, resulting in poor transfer ability to unseen manipulations and a persistent generalization gap across datasets. As shown in the bottom row, X-AVDT achieved the highest average AUROC of 95.29, exceeding the performance of the strongest retrained baseline (RealForensics \[30\] 92.42). The margin over prior methods remained broadly consistent across generators, resulting in a clear overall lead despite MMDF retraining.

#### 6.2.2 Comparison on Benchmark Dataset

We further evaluate X-AVDT on the GAN-based benchmarks FakeAVCeleb \[38\] and FaceForensics++ \[71\], following the same setup as in Table 4. As summarized in Tables 4 and 5, models trained on MMDF transfer well to these benchmarks. Notably, several pretrained detectors are marked with ^(†), indicating train-test overlap. Even under this favorable condition for the baselines, X-AVDT achieved the best scores on both benchmarks with an AUROC of 99.69 on FakeAVCeleb and 89.55 on FaceForensics++.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/2_ablation_attn.png)

Figure 4: Comparison of attention features across diffusion timesteps. Red box denote the configuration used in our method.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/5_abl_perturbation.png)

Figure 5: Robustness against unseen corruptions. AUROC (%) across five severity levels. Per corruption scales are shown on the $`x`$–axes. Average denotes the mean AUROC across all corruptions at each severity level.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/4-1_grad_cam.png)

Figure 6: Grad-CAM visualizations. Red activation indicates regions where our model focuses most (i.e., pixels that make a strong positive contribution to the predicted class), while cooler colors denote weak or no contribution.

### 6.3 Human Evaluation

For human evaluation studies, we use two metrics: Human Evaluation (HE) in Table 4 and Table 5, and HFAR in Table 3. Both HE and HFAR were obtained from the same user study with 24 participants (balanced in gender, aged between their 20s and 30s), where each participant viewed the videos with audio and answered whether it was real or fake. Across datasets, HE was consistently lower than our detector, indicating the task is challenging for humans, whereas our model remains robust.

|                                                  |       |       |         |
| ------------------------------------------------ | ----- | ----- | ------- |
| Method                                           | AUROC | AP    | Acc@EER |
| (a) Ablation on Input Representations            |       |       |         |
| w/o AV Cross-Attn ($`\boldsymbol{\psi}`$)        | 88.22 | 87.25 | 83.70   |
| w/o Video Composite ($`\boldsymbol{\phi}`$)      | 90.21 | 90.57 | 84.32   |
| w/o Residual ($`\lvert x-D(\hat{z}_{0})\rvert`$) | 93.82 | 92.25 | 89.00   |
| (b) Ablation on Loss Design                      |       |       |         |
| w/o $`\mathcal{L}_{\text{tri}}`$                 | 92.64 | 92.26 | 86.32   |
| X-AVDT (full)                                    | 95.29 | 94.03 | 91.15   |

(b) adding the triplet term improves the results across all metrics.

Table 7: Ablation on input representations and loss design. (a) removing any of the input representation degrades performance,

### 6.4 Ablation Study

Choice of Attention Type and Timestep. We analyze how the choice of attention feature and the diffusion timestep affect detection. Table 6 shows that, among attention features extracted from the 3D U-Net in Hallo \[90\], the audio-conditioned cross-attention was consistently the most informative, as it explicitly regularizes the representation toward audio–visual alignment. Figure 4 further illustrates that temporal coherence and spatial appearance tend to capture global motion and pose changes, making them less discriminative. By contrast, cross-attention highlights articulators while suppressing background and is inherently less sensitive to scene changes. Moreover, features from earlier diffusion steps were more discriminative than those from later steps, because early denoising retains stronger conditioning signals before texture refinement dominates, leaving modality-consistency cues less degraded.

Complementary Effect of Input Representations. The video composite $`\boldsymbol{\phi}`$ encodes inversion-induced discrepancies, while the AV cross-attention feature $`\boldsymbol{\psi}`$ provides cross-modal consistency cues derived from the diffusion model’s internal alignment. Motivated by their complementary nature, we combine $`\boldsymbol{\phi}`$ and $`\boldsymbol{\psi}`$ and assess their contributions via an ablation study that removes each component individually. The combined model yields the highest overall performance, indicating that the two representations reinforce each other. Table 7a corroborates this with quantitative results across all three metrics.

Effect of Loss Design. To assess the effect of loss formulation, we compared models trained with only the binary cross-entropy loss $`\mathcal{L}_{\text{bce}}`$ against those using the combined objective $`\mathcal{L}_{\text{bce}}+\mathcal{L}_{\text{tri}}`$. The triplet loss $`\mathcal{L}_{\text{tri}}`$ serves as an auxiliary metric-learning loss, providing an inductive bias toward a more discriminative class structure in the embedding space that complements the classification signal. See Table 7b for quantitative results.

Robustness of In-the-Wild Perturbation Attack. We trained X-AVDT on MMDF without augmentation and evaluated robustness on unseen corruptions with five severity levels. For comparison, all baselines used their official pretrained checkpoints. We report AUROC (%) values in Figure 5. X-AVDT outperformed prior detectors across severity levels, with smaller performance decay than comparative methods under high-frequency suppressing distortions (JPEG/Blur), additive noise, and scale changes due to resizing, as well as under temporal disruptions from frame dropping. Detailed information can be found in the supplementary material.

### 6.5 Discussion

To understand how our detector treats real versus forged videos, we applied Grad-CAM \[73\] to our detector and visualized activation maps on samples from three representative generators (Figure 6). Grad-CAM highlights where the model grounds its decision in each frame, and these activation maps make the effect of our design explicit. Our method concentrated activation on articulatory regions and maintained this focus across frames in real videos. In contrast, forgeries elicited scattered, multi-focal responses, revealing the absence of consistent audio–visual cues. This behavior was consistent across all generators, indicating that our detector exploits audio–visual consistency as a general cue, which in turn explains its generalization beyond any single model’s artifacts. See the supplementary material for details.

## 7 Conclusion

We introduce X-AVDT, a simple, robust, and generalizable detector that probes internal audio–visual signals in pretrained diffusion models via DDIM inversion. Our approach fuses two complementary representations: a video composite $`\boldsymbol{\phi}`$ that surfaces reconstruction-based discrepancies and an AV cross-attention feature $`\boldsymbol{\psi}`$ that encodes speech–motion synchrony. Empirically, we demonstrate that probing intermediate diffusion features during inversion yields more discriminative and better calibrated signals than relying solely on end point reconstructions. Evaluated on MMDF and external benchmarks, X-AVDT delivers consistent improvements over prior methods and transfers well to unseen generators, achieving superior performance on standard datasets and under perturbed image conditions. We also present MMDF, an audio–visual deepfake benchmark curated for cross-generator generalization and robustness studies. We hope MMDF serves as a strong benchmark suite for advancing detector generalization and real-world robustness, while X-AVDT provides a solid baseline and diagnostic probe for future work on audio–visual, generator-internal cues.

Limitations and Future Work Despite strong accuracy and cross-dataset robustness, our method incurs a high computational cost, reflecting the inherent expense of inversion. For a 16 frame clip, a full DDIM inversion and reconstruction process with a 40 timestep schedule requires approximately one minute end-to-end. Current detectors also remain imperfect in non-speech segments or multi-speaker scenes, because the approach relies on speech-driven features. A few promising directions include supplementing our representation with unimodal back-off strategies for weak or missing speech and with speech-agnostic correspondence cues beyond phonetics, and pursuing lightweight inversion via distillation.

## Acknowledgement

This work was supported by the Institute of Information & Communications Technology Planning & Evaluation (IITP) grant funded by the Korea government (MSIT) (No. RS-2024-00439499, Generating Hyper-Realistic to Extremely-stylized Face Avatar with Varied Speech Speed and Context-based Emotional Expression) (50%), and by the Culture, Sports and Tourism R&D Program through the Korea Creative Content Agency (KOCCA) grant funded by the Ministry of Culture, Sports and Tourism in 2024 (RS-2024-00440434) (50%).

## References

- \[1\] D. Afchar, V. Nozick, J. Yamagishi, and I. Echizen (2018) Mesonet: a compact facial video forgery detection network. In 2018 IEEE international workshop on information forensics and security (WIFS), pp. 1–7. Cited by: §2.
- \[2\] T. Afouras, J. S. Chung, and A. Zisserman (2018) LRS3-ted: a large-scale dataset for visual speech recognition. arXiv preprint arXiv:1809.00496. Cited by: §A.2.5.
- \[3\] A. Baevski, Y. Zhou, A. Mohamed, and M. Auli (2020) Wav2vec 2.0: a framework for self-supervised learning of speech representations. Advances in neural information processing systems 33, pp. 12449–12460. Cited by: §A.1.2, §4.2.1, §6.1.
- \[4\] O. Bar-Tal, H. Chefer, O. Tov, C. Herrmann, R. Paiss, S. Zada, A. Ephrat, J. Hur, G. Liu, A. Raj, et al. (2024) Lumiere: a space-time diffusion model for video generation. In SIGGRAPH Asia 2024 Conference Papers, pp. 1–11. Cited by: §1, §2.
- \[5\] S. Barrington, M. Bohacek, and H. Farid (2024) The deepspeak dataset. arXiv preprint arXiv:2408.05366. Cited by: §B.2, Table B.2.2.
- \[6\] (2024) Behind the deepfake: 8% create; 90% concerned. Technical report The Alan Turing Institute. External Links: [Link](https://www.turing.ac.uk/sites/default/files/2024-07/behind_the_deepfake_full_publication.pdf) Cited by: §1.
- \[7\] T. Brooks, A. Holynski, and A. A. Efros (2023) InstructPix2Pix: learning to follow image editing instructions. In CVPR, Cited by: §2.
- \[8\] Z. Cai, S. Ghosh, A. P. Adatia, M. Hayat, A. Dhall, T. Gedeon, and K. Stefanov (2024) AV-deepfake1m: a large-scale llm-driven audio-visual deepfake dataset. In Proceedings of the 32nd ACM International Conference on Multimedia, pp. 7414–7423. Cited by: Table 1.
- \[9\] G. Cazenavette, A. Sud, T. Leung, and B. Usman (2024) Fakeinversion: learning to detect images from unseen text-to-image models by inverting stable diffusion. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 10759–10769. Cited by: §D.1, Appendix D, §1, §2, §4.2.1.
- \[10\] N. A. Chandra, R. Murtfeldt, L. Qiu, A. Karmakar, H. Lee, E. Tanumihardja, K. Farhat, B. Caffee, S. Paik, C. Lee, et al. (2025) Deepfake-eval-2024: a multi-modal in-the-wild benchmark of deepfakes circulated in 2024. arXiv preprint arXiv:2503.02857. Cited by: Table B.2.2.
- \[11\] B. Chen, J. Zeng, J. Yang, and R. Yang (2024) Drct: diffusion reconstruction contrastive training towards universal detection of diffusion generated images. In Forty-first International Conference on Machine Learning, Cited by: §2.
- \[12\] H. Chen, W. Xie, T. Afouras, A. Nagrani, A. Vedaldi, and A. Zisserman (2021) Audio-visual synchronisation in the wild. arXiv preprint arXiv:2112.04432. Cited by: §A.2.3.
- \[13\] Y. Chen, S. Liang, Z. Zhou, Z. Huang, Y. Ma, J. Tang, Q. Lin, Y. Zhou, and Q. Lu (2025) HunyuanVideo-avatar: high-fidelity audio-driven human animation for multiple characters. arXiv preprint arXiv:2505.20156. Cited by: Table B.2.1, Table C.1, §D.3, §E.2.4, Figure D.3.4, Figure D.3.4, §1, §1, §2, Table 2, Table 4.
- \[14\] Z. Chen, J. Cao, Z. Chen, Y. Li, and C. Ma (2025) Echomimic: lifelike audio-driven portrait animations through editable landmark conditions. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 39, pp. 2403–2410. Cited by: §D.2, §6.1.
- \[15\] R. Chesney and D. K. Citron (2019) Deep fakes: a looming challenge for privacy, democracy, and national security. California Law Review 107, pp. 1753–1819. Cited by: §1.
- \[16\] J. S. Chung and A. Zisserman (2016) Out of time: automated lip sync in the wild. In Asian conference on computer vision, pp. 251–263. Cited by: §6.1.
- \[17\] J. Cui, H. Li, Y. Yao, H. Zhu, H. Shang, K. Cheng, H. Zhou, S. Zhu, and J. Wang (2024) Hallo2: long-duration and high-resolution audio-driven portrait image animation. arXiv preprint arXiv:2410.07718. Cited by: §E.2.1, Figure D.3.1, Figure D.3.1, §1, §1, §2, Table 2, Table 4, Table 4.
- \[18\] J. Cui, H. Li, Y. Zhan, H. Shang, K. Cheng, Y. Ma, S. Mu, H. Zhou, J. Wang, and S. Zhu (2025) Hallo3: highly dynamic and realistic portrait image animation with video diffusion transformer. In Proceedings of the Computer Vision and Pattern Recognition Conference, pp. 21086–21095. Cited by: §E.2, §E.4, §5.
- \[19\] (2024) Deepfakes: a human challenge. Technical report WeProtect Global Alliance. External Links: [Link](https://www.weprotect.org/wp-content/uploads/Deepfakes_A-Human-Challenge_PA-Report_v3.pdf) Cited by: §1.
- \[20\] P. Dhariwal and A. Nichol (2021) Diffusion models beat gans on image synthesis. Advances in neural information processing systems 34, pp. 8780–8794. Cited by: §3.
- \[21\] B. Dolhansky, J. Bitton, B. Pflaum, J. Lu, R. Howes, M. Wang, and C. C. Ferrer (2020) The deepfake detection challenge (dfdc) dataset. arXiv preprint arXiv:2006.07397. Cited by: §A.2.5, Table 1, §1.
- \[22\] Federal Communications Commission (2024) FCC proposes \$6 million fine for deepfake robocalls around nh primary. Note: [https://www.fcc.gov/document/fcc-proposes-6-million-fine-deepfake-robocalls-around-nh-primary](https://www.fcc.gov/document/fcc-proposes-6-million-fine-deepfake-robocalls-around-nh-primary) Cited by: §1.
- \[23\] C. Feng, Z. Chen, and A. Owens (2023) Self-supervised video forensics by audio-visual anomaly detection. In proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 10491–10503. Cited by: §A.2.3, §2, Table 4, Table 5, §6.1, §6.2.1.
- \[24\] R. A. Fisher (1936) The use of multiple measurements in taxonomic problems. Annals of eugenics 7 (2), pp. 179–188. Cited by: §D.1.
- \[25\] J. Frank, T. Eisenhofer, L. Schönherr, A. Fischer, D. Kolossa, and T. Holz (2020) Leveraging frequency analysis for deep fake image recognition. In International conference on machine learning, pp. 3247–3258. Cited by: §2.
- \[26\] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio (2014) Generative adversarial nets. Advances in neural information processing systems 27. Cited by: §1, §2.
- \[27\] H. Guan, J. Horan, and A. Zhang (2025) Evaluating analytic systems against ai-generated deepfakes. Note: [https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=959128](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=959128) Cited by: §B.2, §1.
- \[28\] D. Güera and E. J. Delp (2018) Deepfake video detection using recurrent neural networks. In 2018 15th IEEE international conference on advanced video and signal based surveillance (AVSS), pp. 1–6. Cited by: §2.
- \[29\] J. Guo, D. Zhang, X. Liu, Z. Zhong, Y. Zhang, P. Wan, and D. Zhang (2024) Liveportrait: efficient portrait animation with stitching and retargeting control. arXiv preprint arXiv:2407.03168. Cited by: §D.3, §E.2.2, Figure D.3.2, Figure D.3.2, §1, §2, Table 2, Table 4, Table 4.
- \[30\] A. Haliassos, R. Mira, S. Petridis, and M. Pantic (2022) Leveraging real talking faces via self-supervision for robust forgery detection. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 14950–14962. Cited by: §A.2.2, §C.2, §C.2, §2, Table 4, Table 4, Table 5, Table 5, §6.1, §6.2.1.
- \[31\] A. Haliassos, K. Vougioukas, S. Petridis, and M. Pantic (2021) Lips don’t lie: a generalisable and robust approach to face forgery detection. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 5039–5049. Cited by: §A.2.1, §C.2, §C.2, Table 4, Table 5, §6.1.
- \[32\] Y. Han, J. Zhu, K. He, X. Chen, Y. Ge, W. Li, X. Li, J. Zhang, C. Wang, and Y. Liu (2024) Face-adapter for pre-trained diffusion models with fine-grained id and attribute control. In European Conference on Computer Vision, pp. 20–36. Cited by: §E.2.3, Figure D.3.3, Figure D.3.3, §1, §1, §2, Table 2, Table 4, Table 4.
- \[33\] J. Ho, A. Jain, and P. Abbeel (2020) Denoising diffusion probabilistic models. Advances in neural information processing systems 33, pp. 6840–6851. Cited by: §1, §2, §3.
- \[34\] L. Hu (2024) Animate anyone: consistent and controllable image-to-video synthesis for character animation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 8153–8163. Cited by: §A.1.1.
- \[35\] P. Isola, J. Zhu, T. Zhou, and A. A. Efros (2017) Image-to-image translation with conditional adversarial networks. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 1125–1134. Cited by: §2.
- \[36\] T. Karras, T. Aila, S. Laine, and J. Lehtinen (2017) Progressive growing of gans for improved quality, stability, and variation. arXiv preprint arXiv:1710.10196. Cited by: §2.
- \[37\] T. Karras, S. Laine, and T. Aila (2019) A style-based generator architecture for generative adversarial networks. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 4401–4410. Cited by: §2.
- \[38\] H. Khalid, S. Tariq, M. Kim, and S. S. Woo (2021) FakeAVCeleb: a novel audio-video multimodal deepfake dataset. arXiv preprint arXiv:2108.05080. Cited by: Table B.1, §B.1, Table 1, Table 3, Table 5, §5, §6.2.2.
- \[39\] M. Klemt, C. Segna, and A. Rohrbach (2025) DeepFake doctor: diagnosing and treating audio-video fake detection. arXiv preprint arXiv:2506.05851. Cited by: §2.
- \[40\] P. Kwon, J. You, G. Nam, S. Park, and G. Chae (2021) Kodf: a large-scale korean deepfake detection dataset. In Proceedings of the IEEE/CVF international conference on computer vision, pp. 10744–10753. Cited by: §B.2, Table B.2.2, Table 1.
- \[41\] S. Lee, K. Yun, and J. Noh (2025) StyleMM: stylized 3d morphable face model via text-driven aligned image translation. In Computer Graphics Forum, pp. e70234. Cited by: §C.3.
- \[42\] H. Li, B. Li, S. Tan, and J. Huang (2020) Identification of deep network generated images using disparities in color components. Signal Processing 174, pp. 107616. Cited by: §2.
- \[43\] J. Li, D. Li, S. Savarese, and S. Hoi (2023) Blip-2: bootstrapping language-image pre-training with frozen image encoders and large language models. In International conference on machine learning, pp. 19730–19742. Cited by: §C.1.
- \[44\] L. Li, J. Bao, H. Yang, D. Chen, and F. Wen (2019) Faceshifter: towards high fidelity and occlusion aware face swapping. arXiv preprint arXiv:1912.13457. Cited by: §1.
- \[45\] L. Li, J. Bao, T. Zhang, H. Yang, D. Chen, F. Wen, and B. Guo (2020) Face x-ray for more general face forgery detection. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 5001–5010. Cited by: §2.
- \[46\] Y. Li, M. Chang, and S. Lyu (2018) In ictu oculi: exposing ai created fake videos by detecting eye blinking. In 2018 IEEE International workshop on information forensics and security (WIFS), pp. 1–7. Cited by: §2.
- \[47\] Y. Li and S. Lyu (2018) Exposing deepfake videos by detecting face warping artifacts. arXiv preprint arXiv:1811.00656. Cited by: §2.
- \[48\] Y. Li, X. Yang, P. Sun, H. Qi, and S. Lyu (2020) Celeb-df: a large-scale challenging dataset for deepfake forensics. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 3207–3216. Cited by: Table 1, §1.
- \[49\] Y. Liang, M. Yu, G. Li, J. Jiang, B. Li, F. Yu, N. Zhang, X. Meng, and W. Huang (2024) SpeechForensics: audio-visual speech representation learning for face forgery detection. Advances in Neural Information Processing Systems 37, pp. 86124–86144. Cited by: §B.2, Table B.2.1, §2.
- \[50\] C. Lin, J. Gao, L. Tang, T. Takikawa, X. Zeng, X. Huang, K. Kreis, S. Fidler, M. Liu, and T. Lin (2023) Magic3d: high-resolution text-to-3d content creation. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 300–309. Cited by: §2.
- \[51\] Y. Lipman, R. T. Chen, H. Ben-Hamu, M. Nickel, and M. Le (2022) Flow matching for generative modeling. arXiv preprint arXiv:2210.02747. Cited by: §1.
- \[52\] H. Liu, W. Sun, D. Di, S. Sun, J. Yang, C. Zou, and H. Bao (2025) Moee: mixture of emotion experts for audio-driven portrait animation. In Proceedings of the Computer Vision and Pattern Recognition Conference, pp. 26222–26231. Cited by: §6.1.
- \[53\] W. Liu, T. She, J. Liu, B. Li, D. Yao, and R. Wang (2024) Lips are lying: spotting the temporal inconsistency between audio and visual in lip-syncing deepfakes. Advances in Neural Information Processing Systems 37, pp. 91131–91155. Cited by: §A.2.5, Table 4, Table 4, Table 5, Table 5, §6.1, §6.2.1.
- \[54\] I. Loshchilov and F. Hutter (2017) Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101. Cited by: §6.1.
- \[55\] C. Lugaresi, J. Tang, H. Nash, C. McClanahan, E. Uboweja, M. Hays, F. Zhang, C. Chang, M. G. Yong, J. Lee, et al. (2019) Mediapipe: a framework for building perception pipelines. arXiv preprint arXiv:1906.08172. Cited by: §E.1, §5.
- \[56\] G. Luo, L. Dunlap, D. H. Park, A. Holynski, and T. Darrell (2023) Diffusion hyperfeatures: searching through time and space for semantic correspondence. Advances in Neural Information Processing Systems 36, pp. 47500–47510. Cited by: §C.3.
- \[57\] F. Marra, D. Gragnaniello, L. Verdoliva, and G. Poggi (2019) Do gans leave artificial fingerprints?. In 2019 IEEE conference on multimedia information processing and retrieval (MIPR), pp. 506–511. Cited by: §2.
- \[58\] S. McCloskey and M. Albright (2018) Detecting gan-generated imagery using color cues. arXiv preprint arXiv:1812.08247. Cited by: §2.
- \[59\] M. Mirza and S. Osindero (2014) Conditional generative adversarial nets. arXiv preprint arXiv:1411.1784. Cited by: §2.
- \[60\] K. Narayan, H. Agarwal, K. Thakral, S. Mittal, M. Vatsa, and R. Singh (2023) Df-platter: multi-face heterogeneous deepfake dataset. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 9739–9748. Cited by: Table 1.
- \[61\] U. Ojha, Y. Li, and Y. J. Lee (2023) Towards universal fake image detectors that generalize across generative models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 24480–24489. Cited by: §2.
- \[62\] T. Oorloff, S. Koppisetti, N. Bonettini, D. Solanki, B. Colman, Y. Yacoob, A. Shahriyari, and G. Bharaj (2024) Avff: audio-visual feature fusion for video deepfake detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 27102–27112. Cited by: §2.
- \[63\] W. Peebles and S. Xie (2023) Scalable diffusion models with transformers. In Proceedings of the IEEE/CVF international conference on computer vision, pp. 4195–4205. Cited by: §1.
- \[64\] B. Poole, A. Jain, J. T. Barron, and B. Mildenhall (2022) Dreamfusion: text-to-3d using 2d diffusion. arXiv preprint arXiv:2209.14988. Cited by: §2.
- \[65\] K. Prajwal, R. Mukhopadhyay, V. P. Namboodiri, and C. Jawahar (2020) A lip sync expert is all you need for speech to lip generation in the wild. In Proceedings of the 28th ACM international conference on multimedia, pp. 484–492. Cited by: §2.
- \[66\] Y. Qian, G. Yin, L. Sheng, Z. Chen, and J. Shao (2020) Thinking in frequency: face forgery detection by mining frequency-aware clues. In European conference on computer vision, pp. 86–103. Cited by: §2.
- \[67\] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. (2021) Learning transferable visual models from natural language supervision. In International conference on machine learning, pp. 8748–8763. Cited by: §2.
- \[68\] A. Radford, L. Metz, and S. Chintala (2015) Unsupervised representation learning with deep convolutional generative adversarial networks. arXiv preprint arXiv:1511.06434. Cited by: §2.
- \[69\] T. Reiss, B. Cavia, and Y. Hoshen (2023) Detecting deepfakes without seeing any. arXiv preprint arXiv:2311.01458. Cited by: §A.2.4, Table 4, Table 5, §6.1.
- \[70\] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer (2022) High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 10684–10695. Cited by: §C.1, §1, §1, §2, §2, §3, §3, §6.1.
- \[71\] A. Rossler, D. Cozzolino, L. Verdoliva, C. Riess, J. Thies, and M. Nießner (2019) Faceforensics++: learning to detect manipulated facial images. In Proceedings of the IEEE/CVF international conference on computer vision, pp. 1–11. Cited by: Table B.1, §B.1, Table 1, §2, Table 3, Table 5, §5, §6.2.2.
- \[72\] E. Sabir, J. Cheng, A. Jaiswal, W. AbdAlmageed, I. Masi, and P. Natarajan (2019) Recurrent convolutional strategies for face manipulation detection in videos. Interfaces (GUI) 3 (1), pp. 80–87. Cited by: §2.
- \[73\] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra (2017) Grad-cam: visual explanations from deep networks via gradient-based localization. In Proceedings of the IEEE international conference on computer vision, pp. 618–626. Cited by: §6.5.
- \[74\] Z. Sha, Z. Li, N. Yu, and Y. Zhang (2023) De-fake: detection and attribution of fake images generated by text-to-image generation models. In Proceedings of the 2023 ACM SIGSAC conference on computer and communications security, pp. 3418–3432. Cited by: §2.
- \[75\] B. Shi, W. Hsu, K. Lakhotia, and A. Mohamed (2022) Learning audio-visual speech representation by masked multimodal cluster prediction. arXiv preprint arXiv:2201.02184. Cited by: §A.2.6.
- \[76\] K. Shiohara and T. Yamasaki (2022) Detecting deepfakes with self-blended images. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 18720–18729. Cited by: §2.
- \[77\] S. Smeu, D. Boldisor, D. Oneata, and E. Oneata (2025) Circumventing shortcuts in audio-visual deepfake detection datasets with unsupervised learning. In Proceedings of the Computer Vision and Pattern Recognition Conference, pp. 18815–18825. Cited by: §A.2.6, §C.2, §C.2, §2, Table 4, Table 4, Table 5, Table 5, §6.1.
- \[78\] J. Son Chung, A. Senior, O. Vinyals, and A. Zisserman (2017) Lip reading sentences in the wild. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 6447–6456. Cited by: §A.2.3.
- \[79\] N. Stracke, S. A. Baumann, K. Bauer, F. Fundel, and B. Ommer (2025) Cleandift: diffusion features without noise. In Proceedings of the Computer Vision and Pattern Recognition Conference, pp. 117–127. Cited by: §C.3.
- \[80\] L. Tang, M. Jia, Q. Wang, C. P. Phoo, and B. Hariharan (2023) Emergent correspondence from image diffusion. Advances in Neural Information Processing Systems 36, pp. 1363–1389. Cited by: §C.3.
- \[81\] (2019) The state of deepfakes. Technical report Deeptrace (Sensity). External Links: [Link](https://regmedia.co.uk/2019/10/08/deepfake_report.pdf) Cited by: §1.
- \[82\] T. Unterthiner, S. Van Steenkiste, K. Kurach, R. Marinier, M. Michalski, and S. Gelly (2018) Towards accurate generative models of video: a new metric & challenges. arXiv preprint arXiv:1812.01717. Cited by: §6.1.
- \[83\] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin (2017) Attention is all you need. Advances in neural information processing systems 30. Cited by: §1.
- \[84\] Q. Wang, X. Bai, H. Wang, Z. Qin, A. Chen, H. Li, X. Tang, and Y. Hu (2024) Instantid: zero-shot identity-preserving generation in seconds. arXiv preprint arXiv:2401.07519. Cited by: §1, §2.
- \[85\] S. Wang, O. Wang, R. Zhang, A. Owens, and A. A. Efros (2020) CNN-generated images are surprisingly easy to spot… for now. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 8695–8704. Cited by: §2.
- \[86\] Z. Wang, J. Bao, W. Zhou, W. Wang, H. Hu, H. Chen, and H. Li (2023) Dire for diffusion-generated image detection. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 22445–22455. Cited by: §1, §2.
- \[87\] H. Wei, Z. Yang, and Z. Wang (2024) Aniportrait: audio-driven synthesis of photorealistic portrait animation. arXiv preprint arXiv:2403.17694. Cited by: Table B.2.1, Table C.1, §D.3, §E.2.6, Figure D.3.6, Figure D.3.6, §1, §2, Table 2, Table 4, §6.1.
- \[88\] J. Z. Wu, Y. Ge, X. Wang, S. W. Lei, Y. Gu, Y. Shi, W. Hsu, Y. Shan, X. Qie, and M. Z. Shou (2023) Tune-a-video: one-shot tuning of image diffusion models for text-to-video generation. In Proceedings of the IEEE/CVF international conference on computer vision, pp. 7623–7633. Cited by: §2.
- \[89\] S. Xie, R. Girshick, P. Dollár, Z. Tu, and K. He (2017) Aggregated residual transformations for deep neural networks. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 1492–1500. Cited by: §A.1.3, §4.3, §6.1.
- \[90\] M. Xu, H. Li, Q. Su, H. Shang, L. Zhang, C. Liu, J. Wang, Y. Yao, and S. Zhu (2024) Hallo: hierarchical audio-driven visual synthesis for portrait image animation. arXiv preprint arXiv:2406.08801. Cited by: §A.1.1, §D.2, §1, §6.1, §6.4.
- \[91\] S. Yang, H. Li, J. Wu, M. Jing, L. Li, R. Ji, J. Liang, H. Fan, and J. Wang (2025) Megactor-sigma: unlocking flexible mixed-modal control in portrait animation with diffusion transformer. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 39, pp. 9256–9264. Cited by: Table B.2.1, Table C.1, §E.2.5, Figure D.3.5, Figure D.3.5, §1, §2, Table 2, Table 4.
- \[92\] K. Yun, Y. Kim, K. Seo, C. W. Seo, and J. Noh (2024) Representative feature extraction during diffusion process for sketch extraction with one example. arXiv preprint arXiv:2401.04362. Cited by: §C.3.
- \[93\] J. Zhang, C. Herrmann, J. Hur, L. Polania Cabrera, V. Jampani, D. Sun, and M. Yang (2023) A tale of two features: stable diffusion complements dino for zero-shot semantic correspondence. Advances in Neural Information Processing Systems 36, pp. 45533–45547. Cited by: §C.3.
- \[94\] L. Zhang, A. Rao, and M. Agrawala (2023) Adding conditional control to text-to-image diffusion models. In Proceedings of the IEEE/CVF international conference on computer vision, pp. 3836–3847. Cited by: §2.
- \[95\] R. Zhang, P. Isola, A. A. Efros, E. Shechtman, and O. Wang (2018) The unreasonable effectiveness of deep features as a perceptual metric. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 586–595. Cited by: §6.1.
- \[96\] W. Zhang, X. Cun, X. Wang, Y. Zhang, X. Shen, Y. Guo, Y. Shan, and F. Wang (2023) Sadtalker: learning realistic 3d motion coefficients for stylized audio-driven single image talking face animation. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 8652–8661. Cited by: §2.
- \[97\] Y. Zhou and S. Lim (2021) Joint audio-visual deepfake detection. In Proceedings of the IEEE/CVF international conference on computer vision, pp. 14800–14809. Cited by: §2.
- \[98\] J. Zhu, T. Park, P. Isola, and A. A. Efros (2017) Unpaired image-to-image translation using cycle-consistent adversarial networks. In Proceedings of the IEEE international conference on computer vision, pp. 2223–2232. Cited by: §2.

\thetitle\

Supplementary Material\

In this supplementary material, we provide expanded details on the proposed model and the data, an extended ablation study, a class separability analysis, and additional visualizations:

- •
  In Section A, we present additional technical details of our training setup, including the inversion procedure, attention feature extraction and the model architecture. We also describe how the baselines were trained, and detail the human evaluation.
- •
  In Section B, we report the results of experiments on broader deepfake benchmarks, and provide comparative analyses with representative audio-visual baselines.
- •
  In Section C, we (i) report the results of an extended ablation study that compares inversion conditions (audio-driven, text-driven, and withou inversion), (ii) provide detailed results under perturbation attacks, and (iii) analyze attention types and diffusion timesteps.
- •
  In Section D, we conduct a class separability analysis using Fisher SNR and LDA margin to quantify the discriminability of the learned representations. We also present extended cross-attention robustness analyses, along with attention map visualizations that support these findings.
- •
  In Section E, we describe how the MMDF training and evaluation data were obtained and present qualitative examples, including our model’s input representations and sample dataset visualizations.
- •
  In Section F, we discuss the limitations of our system.

## Appendix A Additional Experimental Details

### A.1 Implementation Details of X-AVDT

#### A.1.1 Input Representation

The full procedure of input representation extraction is summarized in Algorithm 1. We follow Hallo \[90\] with a paired ReferenceNet \[34\] to encode identity features from the source portrait frame. During DDIM inversion, the denoising U-Net reads these features via cross-attention. For the cross-attention feature in our detector, we sample at an early diffusion step, setting $`t^{\star}\!=\!24`$ out of a 1000 step schedule during inversion. We adopt Hallo’s hierarchical audio-visual cross-attention mechanism to handle regional masking. We compute lip, expression, and pose masks, apply them as element-wise gates to the cross-attention features and then aggregate the gated features with learned weights. We operate clip-wise on non-overlapping 16 frame segments. If the video length is not divisible by 16, we repeat the last frame to pad to the nearest multiple before feature extraction, and concatenate the per-clip outputs along time. This extraction pipeline is applied identically across all datasets for both training and evaluation.

Input: Video $`x`$, Reference frame $`x_{\mathrm{ref}}`$, Audio $`c`$,

         Masks $`\mathcal{M}=\{\mathcal{M}_{\mathrm{full}},\mathcal{M}_{\mathrm{face}},\mathcal{M}_{\mathrm{lip}}\}`$

Output: Video composite $`\boldsymbol{\phi}=[x,D(\hat{z}_{T}),D(\hat{z}_{0}),r]`$,

         AV cross-attention feature $`\boldsymbol{\psi}=\mathrm{CrossAttn}(H(t),\,c)`$

1. Encode. $`z_{0}\leftarrow\mathrm{VAE_{\mathrm{enc}}}(x)`$,   $`e_{a}\leftarrow\mathrm{Audio_{\mathrm{enc}}}(c)`$

2. Reference pass. $`\mathrm{RefFeat}\leftarrow\mathrm{ReferenceNet}(x_{\mathrm{ref}})`$

3. DDIM Inversion. Run the inverse scheduler $`z_{0}\rightarrow z_{T}`$.

for _$`t\in T`$ (fine $`\rightarrow`$ coarse)_ do

    $`\bigl(\hat{\epsilon}_{t},\ {\boldsymbol{\psi}}_{t}\bigr)\leftarrow\mathrm{UNetFwd}\!\left(z_{t},\ e_{a},\ \mathcal{M};\ \mathrm{RefFeat}\right)`$

   

   $`z_{t+1}\leftarrow\mathrm{DDIMInverseScheduler}(z_{t},\hat{\epsilon}_{t})`$

   

   if _$`t=t^{\star}`$_ then

       $`\tilde{\boldsymbol{\psi}}\leftarrow\mathrm{HeadProj}(\psi_{t})`$

      $`\boldsymbol{\psi}\leftarrow\sum_{k\in\{\mathrm{full,face,lip}\}}w_{k}\,(\tilde{\boldsymbol{\psi}}\odot\mathcal{M}_{k})`$

    end if

   

end for

4. DDIM Reconstruction. Run the forward scheduler $`z_{T}\rightarrow z_{0}`$. for _$`t\in T`$ (coarse $`\rightarrow`$ fine)_ do

    $`\hat{\epsilon}_{t}\leftarrow\mathrm{UNetFwd}(\tilde{z}_{t},\,e_{a},\,\mathcal{M};\,\mathrm{RefFeat})`$

   $`\tilde{z}_{t-1}\leftarrow\mathrm{DDIMScheduler}(\tilde{z}_{t},\,\hat{\epsilon}_{t})`$

end for

$`\hat{z}_{0}\leftarrow\tilde{z}_{0}`$,   $`\hat{x}\leftarrow D(\hat{z}_{0})`$,   $`u\leftarrow D(\hat{z}_{T})`$,   $`r\leftarrow|x-\hat{x}|`$,  

$`\boldsymbol{\phi}\leftarrow[x,\,u,\,\hat{x},\,r]`$

Return $`(\boldsymbol{\phi},\ \boldsymbol{\psi})`$

Algorithm 1 Audio-driven inversion & reconstruction.

#### A.1.2 Conditioning

We use wav2vec 2.0 \[3\] as the audio feature encoder to condition our videos. To capture rich semantics information across different audio layers, we concatenate the audio embeddings from the last 12 layers of wav2vec 2.0 network. Given the sequential nature of audio, we aggregate a 5-frame local context (t$`-`$2…t$`+`$2) for each video frame before projection.

#### A.1.3 Training

To fuse the video composite $`\boldsymbol{\phi}`$ and AV cross-attention feature $`\boldsymbol{\psi}`$ during training, we proceed as follows. We concatenate $`\mathbf{v}^{\prime}`$ and $`\mathbf{a}^{\prime}`$ along the channel dimension and apply a $`1{\times}1`$ convolution, reducing the channels from $`2048`$ to $`1024`$ to obtain $`p_{i}`$. We add fixed 2D positional encodings to $`p_{i}`$ and apply an 8-head self-attention over the $`H\!W`$ tokens, with LayerNorm and a residual connection. We feed the self-attention outputs into three 3D ResNeXt \[89\] layers, followed by global average pooling, which yields $`g_{i}\in\mathbb{R}^{1024}`$. We train for 2 epochs by default, as our inputs are structured internal representations extracted from a pretrained diffusion model, enabling faster convergence than raw RGB. Table A.1.3 reports an ablation result showing that performance quickly converges after a few epochs.

|        |       |          |       |       |       |
| ------ | ----- | -------- | ----- | ----- | ----- |
| Epochs | 1     | 2 (Ours) | 5     | 10    | 20    |
| AUROC  | 93.24 | 95.29    | 95.01 | 95.19 | 95.13 |

Table A.1.3: Effect of training epochs on X-AVDT.

### A.2 Details of Baseline Detectors

#### A.2.1 LipForensics \[31\]

LipForensics is a video-only deepfake detector that operates on mouth crops, targeting the lip region and modeling temporal inconsistencies in mouth movements to identify manipulation-specific irregularities. We evaluated LipForensics using the official pretrained model that has been trained on FaceForensics++. In addition, we did not retrain it because the training code is not available.

#### A.2.2 RealForensics \[30\]

RealForensics uses audio-visual pretraining, in which audio and visuals exclusively from real samples are used to learn representations that help a classifier discriminate between real and fake videos. We evaluated RealForensics using the official pretrained model that has been trained on FaceForensics++, and we also retrained it on MMDF using the same hyperparameters.

#### A.2.3 AVAD \[23\]

AVAD first pretrains an audio–visual synchronization model following Chen et al. \[12\] to learn temporal alignment between speech and mouth motion. They then use the inferred features to train an anomaly detector, producing a fully unsupervised multi-modal deepfake detector. As an unsupervised method, AVAD is not trained with labels or fake examples. We evaluated AVAD using the official pretrained model that was trained on LRS \[78\] and did not retrain it because the training code is not available.

#### A.2.4 FACTOR \[69\]

FACTOR is a training-free deepfake detector that frames detection as fact checking. It uses audio-visual encoders to extract modality-specific features and computes a truth score (cosine similarity) that quantifies the consistency between observed audio-visual evidence and an asserted attribute. FACTOR operates in a zero-shot, label-free setting and does not use fake examples. We evaluated FACTOR using the official implementation and pretrained feature extractors.

#### A.2.5 LipFD \[53\]

LipFD targets lip-syncing forgeries by enforcing audio-visual temporal consistency between lip movements and audio signals. The method operates on mouth crops and combines a global video branch with a lip-region branch in a dual-head design. We evaluated LipFD using the model pretrained on Lip Reading Sentences 3 (LRS3) \[2\], FaceForensics++, and the Deepfake Detection Challenge Dataset (DFDC) \[21 dataset")\]. For retraining on MMDF, we trained LipFD for 25 epochs and otherwise keep the original hyperparameters.

#### A.2.6 AVH-Align \[77\]

AVH-Align addresses dataset shortcuts such as leading silence by training only on real data and learning a frame-level audio-video alignment score from AV-HuBERT features \[75\]. The training is self-supervised and label-free on real pairs, with no fake examples used. We evaluated AVH-Align using the official pretrained model that has been trained on FakeAVCeleb and AV-Deepfake1M. In addition, we retrained it on MMDF using the same hyperparameters.

|                    |          |         |     |                        |          |           |
| ------------------ | -------- | ------- | --- | ---------------------- | -------- | --------- |
| FakeAVCeleb \[38\] |          |         |     | FaceForensics++ \[71\] |          |           |
| FSGAN              | FaceSwap | Wav2Lip |     | Deepfakes              | FaceSwap | Face2Face |
| 99.73              | 99.79    | 99.92   |     | 99.62                  | 99.24    | 99.63     |

Table B.1: In-domain AUROC on the benchmark dataset. Cross-manipulation generalization is evaluated by training on two manipulation methods and testing on the remaining one (e.g., train on the first two columns and test on the third columns).

### A.3 Human Evaluation

We conducted a human evaluation study to assess deepfake detection accuracy and to quantify the realism of manipulated videos in MMDF, comparing results against FaceForensics++ and FakeAVCeleb. For each clip, participants responded to two following questions: (i) _“Is the video real or fake?”_ (binary choice), and (ii) _”What did you focus on when deciding whether the video was real or fake?”_. For question (ii), 80% of comments cited audio-visual synchronization as the primary cue, while the remainder pointed to background artifacts, expression dynamics, and intraoral details, etc. We used 80 videos (60 from the MMDF dataset, 10 from the FakeAVCeleb, and 10 from FaceForensics++), with 24 participants providing responses. We aggregated answers to compute Human Evaluation (HE) accuracy and Human False Acceptance Rate (HFAR), with both metrics derive from the same study.

## Appendix B Additional Experiments

### B.1 In-domain Evaluation

Table B.1 summarizes the in-domain performance of X-AVDT on each benchmark dataset (FakeAVCeleb \[38\] and FaceForensics++ \[71\]), where the model is trained and tested on the same dataset ($`\sim`$ Official-pretrained). X-AVDT achieved high AUROC across manipulation types (higher than the scores obtained by the prior methods presented in Table 5). Note that Table 5 reports the results for cross-dataset robustness (MMDF $`\rightarrow`$ benchmark); while the performances of many MMDF-trained baselines dropped due to domain mismatch, X-AVDT remained strong.

|                        |                    |       |         |                            |       |         |                      |       |         |         |       |         |
| ---------------------- | ------------------ | ----- | ------- | -------------------------- | ----- | ------- | -------------------- | ----- | ------- | ------- | ----- | ------- |
|                        | AniPortrait \[87\] |       |         | MegActor-$`\Sigma`$ \[91\] |       |         | HunyuanAvatar \[13\] |       |         | Average |       |         |
| Model                  | AUROC              | AP    | Acc@EER | AUROC                      | AP    | Acc@EER | AUROC                | AP    | Acc@EER | AUROC   | AP    | Acc@EER |
| SpeechForensics \[49\] | 99.99              | 99.99 | 99.88   | 98.69                      | 98.82 | 94.46   | 92.12                | 91.98 | 82.90   | 96.93   | 96.93 | 92.41   |
| X-AVDT (Ours)          | 99.10              | 98.89 | 96.54   | 90.17                      | 88.05 | 83.11   | 97.79                | 97.44 | 97.69   | 95.29   | 94.03 | 91.15   |

Table B.2.1: Additional quantitative comparison results on the MMDF dataset.

|                          |       |       |         |       |
| ------------------------ | ----- | ----- | ------- | ----- |
| Dataset                  | AUROC | AP    | Acc@EER | Acc   |
| DeepSpeak v1.0 \[5\]     | 94.29 | 95.06 | 95.39   | 94.94 |
| KoDF \[40\]              | 93.07 | 92.88 | 91.13   | 91.87 |
| Deepfake-Eval2024 \[10\] | 75.02 | 72.73 | 71.68   | 71.36 |

Table B.2.2: Additional quantitative results for X-AVDT.

### B.2 Additional Experiments

In addition to Table 4 in the main paper, we report additional quantitative results to further evaluate the generalization of SpeechForensics \[49\]. Table B.2.1 compares X-AVDT with SpeechForensics using representative audio-visual baselines on the MMDF dataset. Although X-AVDT performed worse than SpeechForensics on AniPortrait and MegActor-$`\Sigma`$, it yielded a clear improvement on HunyuanAvatar, where SpeechForensics attained comparatively lower scores. Overall, the results indicate complementary strengths of the two methods across generators and suggest that generator-internal audio-visual consistency cues can be particularly helpful in challenging settings such as HunyuanAvatar, whose high-fidelity, temporally coherent, audio-driven synthesis can suppress overt artifact-based cues. Table B.2.2 summarizes results on additional in-the-wild deepfake benchmarks, such as DeepSpeak v1.0 \[5\], KoDF \[40\], and Deepfake-Eval2024 \[27\]. X-AVDT maintained high performance on DeepSpeak v1.0 and KoDF, but its performance dropped on Deepfake-Eval2024, due to a challenging domain shift in content and compression conditions. Nevertheless, the method remained well above chance across all three datasets, indicating non-trivial generalization in settings with MMDF.

## Appendix C Additional Ablation Study

|                     |                    |       |         |                            |       |         |                      |       |         |         |       |         |
| ------------------- | ------------------ | ----- | ------- | -------------------------- | ----- | ------- | -------------------- | ----- | ------- | ------- | ----- | ------- |
|                     | AniPortrait \[87\] |       |         | MegActor-$`\Sigma`$ \[91\] |       |         | HunyuanAvatar \[13\] |       |         | Average |       |         |
| Method              | AUROC              | AP    | Acc@EER | AUROC                      | AP    | Acc@EER | AUROC                | AP    | Acc@EER | AUROC   | AP    | Acc@EER |
| w/o Inversion       | 73.55              | 67.56 | 69.95   | 63.18                      | 63.69 | 59.81   | 41.81                | 46.36 | 43.55   | 62.22   | 61.07 | 56.69   |
| Text-driven         | 90.22              | 90.85 | 81.56   | 76.15                      | 75.25 | 69.91   | 49.01                | 49.00 | 50.51   | 74.48   | 76.94 | 65.75   |
| Audio-driven (Ours) | 96.55              | 98.83 | 90.20   | 89.87                      | 89.25 | 83.86   | 97.71                | 97.04 | 90.94   | 94.71   | 95.04 | 88.33   |

Table C.1: Ablation on video composite $`\boldsymbol{\phi}`$. When training, we fix the backbone and vary only the conditioning signal used during inversion. Audio-driven setting ranked first across datasets, while removing inversion cues yielded the weakest composite.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/b2_abl_perturbation.png)

Figure C.2.1: Robustness to unseen corruptions. AP (%) is shown in the first row and Acc@EER (%) is shown in the second row across five severity levels. Per corruption scales are shown on the $`x`$–axes. Average denotes the mean AP in the top row and Acc@EER in the bottom row, respectively, across all corruptions at each severity level.

|         |                         |       |          |                       |       |       |
| ------- | ----------------------- | ----- | -------- | --------------------- | ----- | ----- |
|         | Audio Desynchronizaiton |       |          | Audio Codec Artifacts |       |       |
| Metric  | -0.5 sec                | 0     | +0.5 sec | 0                     | 8k    | 32k   |
| AUROC   | 90.90                   | 93.70 | 91.31    | 93.70                 | 91.80 | 90.17 |
| AP      | 91.10                   | 94.30 | 91.74    | 94.30                 | 88.80 | 86.51 |
| Acc@EER | 83.40                   | 86.40 | 83.97    | 86.40                 | 85.90 | 81.56 |

Table C.2.2: Robustness to unseen audio perturbations. Performance under audio desynchronization (temporal offsets) and audio codec artifacts (low-bitrate re-encoding) at varying severity levels.

### C.1 Inversion Condition

In Table C.1, we compare three input settings for the video composite $`\boldsymbol{\phi}`$. The settings are: text-driven conditioning; original-frame only, which uses only the original RGB frames without the decoded latent DDIM noise map $`D(\hat{z}_{T})`$, the reconstruction $`D(\hat{z}_{0})`$, the residual $`r=\lvert x-D(\hat{z}_{0})\rvert`$, or attention features; and audio-driven conditioning (Ours). For text-driven conditioning, we use the BLIP-2, OPT-2.7b \[43\] model to caption frames before inversion. The text-conditioned inversion is based on Stable Diffusion 1.5 \[70\], the same backbone as Hallo. This ablation represents the core designing principle of X-AVDT leveraging internal features of large generative models, specifically audio-visual cross-attention features for deepfake detection. The audio-driven setting consistently yielded the strongest results, validating that audio conditioned cross-attention offers richer, temporally aligned cues than text conditioning. Such alignment is particularly important for facial-editing videos that hinge on subtle mouth and expression edits.

### C.2 Robustness of Perturbation Attack

We conducted an additional ablation study to evaluate the robustness of X-AVDT exploiting audio–visual alignment signals against diverse image perturbations. We assessed performance under five scenarios, with severity 0 denoting the unmodified original. All experiments were run on a subset of MMDF. The baselines (LipForensics \[31\], RealForensics \[30\], and AVH-Align \[77\]) were evaluated with their official pretrained checkpoints.

- •
  JPEG Compression: Lossy re-encoding is applied with quality levels of 90, 70, 50, and 30. Lower quality yields stronger high-frequency suppression.
- •
  Blur: Gaussian blur with radius of 0.5, 1.0, 2.0, and 3.0, modeling defocus and motion smoothing.
- •
  Noise: Additive Gaussian noise with standard deviation (pixel scale) of 5, 10, 20, and 35.
- •
  Resizing: Downscale and then upscale using bilinear interpolation with percentage of 75%, 60%, 50%, and 40%. The frame is reduced and then upsampled back to the original size, simulating resolution loss.
- •
  Frame Drop: Randomly remove frames with probabilities of 0.05, 0.10, 0.20, and 0.30, creating temporal discontinuities. We do not duplicate frames in this setting.

These experiments were conducted with the same dataset used in Table 4 and Table 5. The quantitative results for AP (%) and Acc@EER (%) are presented in Figure C.2.1. As shown in the results, X-AVDT caused only minor performance degradation across various perturbation methods, while consistently surpassed competing baselines \[31, 30, 77\], demonstrating strong robustness.

Audio Perturbation Attack. We evaluates the robustness of X-AVDT under two audio perturbations: Audio Desynchronization and Audio Codec Artifacts. For desynchronization, we apply a temporal offset $`\tau\in\{-0.5,+0.5\}`$ seconds, where a positive offset delays speech by prefixing $`|\tau|`$ seconds of silence, while a negative offset advances audio by trimming the first $`|\tau|`$ seconds. For codec artifacts, we re-encode audio with a bitrate cap $`b\in\{8,32\}`$ kbps to introduce compression distortions. As shown in Table C.2.2, compared to the clean setting ($`\tau=0`$, original audio), desynchronization induced only modest performance drops (within 2.4-3.2 points across metrics) at $`\tau=\pm 0.5`$s. Similarly, compared to no re-encoding, codec artifacts caused limited degradation (within 0.5-7.8 points across metrics) under $`b\in\{8,32\}`$ kbps. These results suggest that the learned audio-visual consistency cues remain stable under temporal misalignment and compression-induced distortions.

![[Uncaptioned image]](https://arxiv.org/html/2603.08483v1/figs/b3_abl_cross.png)

![[Uncaptioned image]](https://arxiv.org/html/2603.08483v1/figs/b3_abl_temporal.png)

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/b3_abl_spatial.png)

Figure C.3: Visualization of attention features across diffusion timesteps.

### C.3 Choice of Attention Type and Timestep

We present additional visual examples across different attention types and DDIM inversion timesteps $`t`$ in Figure C.3. In a diffusion model trained with $`T=1000`$ steps, we perform inversion with a 40 step sampling schedule and conducted an ablation study over cross-attention, spatial-attention, and temporal-attention, comparing three representative timesteps at $`t\in\{24,249,499\}`$. Audio-visual cross-attention consistently concentrated on articulators (e.g., lips, jaw), while suppressing the background. Furthermore, as $`t`$ increased, cross-attention maintained the highest performance at every timestep, outperforming both temporal and spatial attention, indicating that it is the most robust component (see Table 6).

Analysis on Chosen Timestep. As reported in Table 6 of the main paper, the performance of X-AVDT consistently improved as the timestep decreased, across cross-attention, temporal-attention, and spatial-attention. This tendency likely arises because features become more informative in earlier diffusion steps (i.e., as $`t\rightarrow 0`$), while features in later steps are more heavily corrupted by noise and thus less discriminative. This observation aligns with prior findings \[80, 93, 92, 56, 41, 79\], which show that mid-to-early diffusion features provide stronger signals for correspondence, stylization, and segmentation due to reduced noise perturbation and richer structural detail. Therefore we did not conducted experiments on $`t>500`$, following the previous research.

## Appendix D Analysis

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/0_snr.png)

Figure D.1: PCA embeddings with a shared LDA decision boundary. Embeddings are extracted from the baseline and from the independently trained X-AVDT, without any fine-tuning.

This section complements our method by analyzing the overall detection pipeline, and visualizing the internal audio-visual cross-attention maps from the diffusion backbone. We compared our method against a visual-only baseline \[9\]. For the visualization, we present attention heatmaps for the source and representative generators.

### D.1 Fisher SNR and LDA Margin

We hypothesize that internal audio-visual cross-attention features from large generative models provide a strong discriminative signal for deepfake detection. As shown in Figure D.1, our method produced noticeably better real/fake separation than a visual only baseline \[9\]. For a fair comparison, we fit a single linear discriminant analysis (LDA) classifier in the embedding space and project both methods to two dimensions, using the same decision boundary across panels. Measured by Fisher signal-to-noise ratio (SNR) \[24\] and the LDA margin, performance improves from 1.95dB and 5.29 (baseline) to 7.53dB and 8.75 (ours). This gap suggests that cross-attention captures stable audio-visual correspondence and exposes inconsistencies that generative models fail to reproduce.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/c2_attention_robustness.png)

Figure D.2: Top-$`q`$ Attention Mass Coverage within the Face ROI (Left) and $`\Delta`$ Cross-Attention Maps (Right). In the $`\Delta`$ maps, red indicates regions with higher fake cross-attention than real ($`\Delta>0`$), and blue indicates the opposite ($`\Delta<0`$).

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/c3_av_attn_map2.png)

Figure D.3: Temporally averaged cross-attention heatmaps.

### D.2 Cross-Attention Robustness

Figure D.2 quantifies the top-$`q`$ attention mass coverage within the face ROI: real videos concentrate the top-$`q`$ mass in a smaller ROI, whereas synthesized videos consistently require coverage of a larger ROI coverage (left). Moreover, the $`\Delta`$ attention maps reveal a coherent spatial contrast pattern: attention for real videos is concentrated on the mouth and background, while attention for fake videos is more broadly distributed along the face boundary (right). This pattern persists across two different inversion sources, Hallo \[90\], our backbone generator, and Echomimic \[14\].

### D.3 Attention Map Visualization

To complement our quantitative results, we visualize internal audio-visual cross-attention maps from the diffusion backbone. As shown in Figure D.3, for each video we extract cross-attention during DDIM inversion, normalize the weights per frame, and average them over time to obtain a single heatmap. We compare the source clip deepfake results from with three representative generators that span different synthesis frameworks: LivePortrait (GAN-based) \[29\], AniPortrait (diffusion-based) \[87\], and HunyuanAvatar (flow-matching-based) \[13\]. Empirically, similar cross-attention patterns are observed across the results from different generator frameworks, indicating that large generative models already provide strong and efficient self-supervised representations well suited for detection. Note that our detector is trained and evaluated on attention features, not on visualized maps, which are provided solely for interpretability. Averaging and normalization for display can introduce information loss, whereas feature vectors are stable.

## Appendix E MMDF Dataset

### E.1 MMDF Construction and Split Protocol

The filtering in MMDF construction corresponds to standard face-detection preprocessing \[55\] that is widely adopted across facial video datasets and generation pipelines. We only removed clips with inaccurate face tracking to ensure reliable ground-truth pairs, thereby reducing confounding failure cases across all compared detectors rather than favoring X-AVDT. This reduced the candidate set by 6.93% (2,001 clips removed). MMDF is intentionally designed as a strict cross-generator generalization benchmark. Because our goal is to detect forgeries from unseen generation mechanisms, we enforce disjoint generation methods between train and test to avoid overfitting to generator-specific artifacts. We also incorporate a variety of generators, model families, and synthesis methods to maximize the diversity of train-test combinations under this cross-setting.

### E.2 Details of Fake Generators

As mentioned in the main paper, we adopt the Hallo3 dataset released by its authors \[18\] as the source corpus and employ a curated subset as our real set (see Figure E.1). Then the generators described below synthesize the paired fakes. During preprocessing, all videos are sampled at 25fps to obtain the reference images, and the generated sequences are temporally aligned to their sources for one-to-one pairing, and resized to $`512\times 512`$. All fakes are produced by inference only, without any additional training, using the authors’ default parameters.

#### E.2.1 Hallo2 \[17\]

Hallo2 is a diffusion-based, audio-driven portrait image animation model. For the fake samples in the MMDF training set, we use the first video frame as the single reference image and feed the clip’s corresponding audio as the driving signal to generate an audio-synchronized talking-head sequence.

#### E.2.2 LivePortrait \[29\]

LivePortrait is a GAN-based portrait animation method that warps a single reference image according to a driving signal to perform self-reenactment. For the fake samples in the MMDF training set, we use the first frame as the reference image and animate it using the remaining frames as driving images. Note that LivePortrait operates as an image-to-video model without audio driving (i.e., motion is driven solely by image frames).

#### E.2.3 FaceAdapter \[32\]

FaceAdapter is a face-editing adapter for pretrained diffusion models, targeting face swapping. For the fake samples in the MMDF training set, we randomly select a source identity and a target identity. Leveraging its image-to-image design, we generate swapped frames for the target clip and then pair the synthesized frames with the source audio to produce the final video, thereby preserving the source identity and speech.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/d_dataset_distribution.png)

Figure E.1: Statistics of the MMDF dataset.

#### E.2.4 HunyuanAvatar \[13\]

HunyuanAvatar is a flow-matching-based audio-driven human animation method. For the fake samples in the MMDF evaluation set, we use the first frame as the source input. We then feed the clip’s corresponding audio together with a text prompt generated from the first frame by BLIP-2, OPT-2.7b model, producing an audio-synchronized, text-conditioned talking head sequence.

#### E.2.5 MegActor-$`\Sigma`$ \[91\]

MegActor-$`\Sigma`$ is a diffusion-transformer (DiT)–based portrait animation method with mixed-modal conditioning. For the fake samples in the MMDF evaluation set, we use the first frame as the source input, and feed the source video together with its corresponding audio to generate a self-reenactment sequence.

#### E.2.6 Aniportrait \[87\]

Aniportrait is a diffusion-based, audio-driven portrait animation method. For the fake samples in the MMDF evaluation set, we use the first video frame as the single reference image and feed the clip’s corresponding audio as the driving signal to generate an audio-synchronized talking-head sequence.

### E.3 Input Representation Visualization

Figure D.2.1 and Figure D.2.2 contain samples from our model’s input representation, video composite $`\boldsymbol{\psi}`$ and AV cross-attention feature $`\boldsymbol{\psi}`$ utilized by our detector. From top to bottom, we show the audio-visual cross-attention feature $`\boldsymbol{\psi}`$, the original video $`x`$, the decoded latent DDIM noise map $`D(\hat{z}_{T})`$, the reconstructed video $`D(\hat{z}_{0})`$, and the reconstruction residual $`r=\lvert x-D(\hat{z}_{0})\rvert`$ of the video composite $`\boldsymbol{\phi}`$. The supplementary video with audio further illustrates temporal dynamics and audio-visual synchronization patterns.

### E.4 MMDF Dataset Visualization

Figures D.3.1–D.3.6 present samples from the curated MMDF dataset used in our experiments. For each identity, the real frames were taken from the source dataset \[18\] and the fake videos were generated by respective generators. The supplementary video with audio further illustrates temporal dynamics and audio-visual synchronization patterns.

## Appendix F Limitations

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/rebuttal_tradeoff.png)

Figure F: Speed-accuracy trade-off with DDIM inversion steps.

Figure F indicates a potential limitation of our approach in real-world applications. Performance depends on the number of DDIM inversion timestep schedule $`k`$ used to extract $`\boldsymbol{\phi}`$ and $`\boldsymbol{\psi}`$. While larger $`k`$ yields more faithful inversion features and improves AUROC, it increases runtime and computational cost. Conversely, smaller $`k`$ reduces latency but degrades detection accuracy. The incurred cost can be mitigated in future work by adopting fewer step schedules or model distillation.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/d2_input1.png)

Figure D.2.1: Qualitative visualization of the input representations $`\boldsymbol{\phi}`$ and $`\boldsymbol{\psi}`$.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/d2_input2.png)

Figure D.2.2: Qualitative visualization of the input representations $`\boldsymbol{\phi}`$ and $`\boldsymbol{\psi}`$.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/d3_1_hallo2.png)

Figure D.3.1: Qualitative comparison of real and fake videos generated by Hallo2 \[17\] in the MMDF.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/d3_2_liveportrait.png)

Figure D.3.2: Qualitative comparison of real and fake videos generated by LivePortrait \[29\] in the MMDF.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/d3_3_faceadatper.png)

Figure D.3.3: Qualitative comparison of real and fake videos generated by FaceAdater \[32\] in the MMDF.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/d3_4_hunyuan.png)

Figure D.3.4: Qualitative comparison of real and fake videos generated by HunyuanAvatar \[13\] in the MMDF.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/d3_5_megactor.png)

Figure D.3.5: Qualitative comparison of real and fake videos generated by MegActor-$`\Sigma`$ \[91\] in the MMDF.

![Refer to caption](https://arxiv.org/html/2603.08483v1/figs/d3_6_aniportrait.png)

Figure D.3.6: Qualitative comparison of real and fake videos generated by AniPortrait \[87\] in the MMDF.
