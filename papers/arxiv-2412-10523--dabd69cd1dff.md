---
identifier: arxiv:2412.10523
title: "The Language of Motion: Unifying Verbal and Non-verbal Language of 3D Human Motion"
authors:
  - Changan Chen
  - Juze Zhang
  - Shrinidhi K. Lakshmikanth
  - Yusu Fang
  - Ruizhi Shao
  - Gordon Wetzstein
  - Li Fei-Fei
  - Ehsan Adeli
published: "2024-12-13T00:00:00+00:00"
url: https://arxiv.org/abs/2412.10523
source: arxiv
doi: null
arxiv_id: "2412.10523"
categories:
  - cs.CV
---

# The Language of Motion: Unifying Verbal and Non-verbal Language of 3D Human Motion

Changan Chen^(\*)    Juze Zhang^(\*)    Shrinidhi K. Lakshmikanth^(\*)
   Yusu Fang    Ruizhi Shao    Gordon Wetzstein    Li Fei-Fei    Ehsan
Adeli    Stanford University

###### Abstract

Human communication is inherently multimodal, involving a combination of
verbal and non-verbal cues such as speech, facial expressions, and body
gestures. Modeling these behaviors is essential for understanding human
interaction and for creating virtual characters that can communicate
naturally in applications like games, films, and virtual reality.
However, existing motion generation models are typically limited to
specific input modalities—either speech, text, or motion data—and cannot
fully leverage the diversity of available data. In this paper, we
propose a novel framework that unifies verbal and non-verbal language
using multimodal language models for human motion understanding and
generation. This model is flexible in taking text, speech, and motion or
any combination of them as input. Coupled with our novel pre-training
strategy, our model not only achieves state-of-the-art performance on
co-speech gesture generation but also requires much less data for
training. Our model also unlocks an array of novel tasks such as
editable gesture generation and emotion prediction from motion. We
believe unifying the verbal and non-verbal language of human motion is
essential for real-world applications, and language models offer a
powerful approach to achieving this goal. Project page:
[languageofmotion.github.io](https://languageofmotion.github.io).

^(\*)^(\*)footnotetext: indicates equal contribution

## 1 Introduction

Human communication is multimodal. We use spoken and body language,
including hand gestures, facial expressions, body postures and emotional
expressions to interact with each other effectively. For example, people
use linguistic cues along with body language, including hand gestures,
facial expressions, overall body posture, and even emotional expressions
to interact with the environment effectively. Modeling these multimodal
behaviors is essential for understanding and generating human motion,
enabling a wide range of applications for virtual characters in games,
movies, and virtual reality—areas that have recently received
substantial attention.

Existing work has been focused on modeling human motion from different
modalities, such as speech \[43, 71, 49\], text \[76, 23, 65\],
egocentric vision \[30, 34\], or the surrounding environment \[25, 64,
78, 75, 5\]. These models only take specific modalities as input, whose
performance is thus limited to the data available for their downstream
task. For example, co-speech gesture generation work typically trains
speaker-dependent models \[19, 71, 43, 3\], which requires high-quality
speech–motion capture of a person. While gesture style varies from
person to person, many gestures are shared across people as well as
non-speech-driven motion, such as walking or waving hands. Existing work
has yet to leverage motion priors from all forms of motion data.

One of the promising ways to unify different tasks is multimodal
language models, where a single language model can take different
modalities as input and output target modalities. These models have
shown promising results in a wide range of multimodal tasks, such as
visual question answering \[42, 33, 2\], audio understanding and
generation \[6, 15, 74\], and text-to-motion generation \[83, 9, 76, 62,
10\]. While language models have been widely applied, it has not been
explored in the speech-text–motion generation setting.

We argue language models play a crucial role in unifying the verbal and
non-verbal language of human motion for three reasons: 1) language
models naturally connect different modalities, 2) speech is highly
semantic, and tasks like modeling laughter in response to a joke require
strong semantic reasoning capabilities and 3) language models are
equipped with strong semantic understanding from extensive pre-training.

Towards this goal, we propose a novel multimodal language model for
expressional motion generation and understanding (see Fig. ). To
leverage language models to model motion, we first tokenize motion
separately for different body parts (face, hand, upper-body,
lower-body). Such compositionality has shown to be more beneficial to
model the expressive human expressions \[49, 43\]. Along with
off-the-shelf tokenizers for text and speech \[28\], we can represent
any given modality inputs as a sequence of tokens, which are consumed by
language models. To train the language models, we design a two-stage
training pipeline. The model is first pre-trained to align various
modalities with compositional body motion alignment and audio–text
alignment. After pre-training, we compile downstream tasks into
instructions and train the model on these instructions to allow the
model to follow various task instructions.

We first validate our model on the BEATv2 co-speech gesture generation
benchmark \[43\] and show that our model strongly outperforms
state-of-the-art models. We then conduct a thorough evaluation to
demonstrate the effectiveness of our pre-training tasks. We also show
that our pre-training strategy is more powerful when under severe data
scarcity. While never seeing speech–motion data during pre-training, our
model reaches competitive performance with a relatively small amount of
data for a novel speaker, showing remarkable generalization. By
performing post-training on both speech–motion and text–motion tasks, we
show that our model not only follows audio and text prompts but also
unlocks novel tasks such as predicting emotion from motion data. Please
watch the Supp. video for the qualitative examples. To the best of our
knowledge, this is the first work to build multimodal language models to
unify the verbal and non-verbal language of 3D human motions.

## 2 Related Work

![](arxiv-2412-10523--dabd69cd1dff.figures/figure-1.webp)

Figure 2: Method overview. We employ modality-specific tokenizers to
process various input modalities. Specifically, we train a compositional
body motion VQ-VAE to tokenize face, hands, upper body, and lower body
motions into discrete tokens, combining these modality-specific
vocabularies(audio and text) into a unified multimodal vocabulary.
During training, mixed tokens from different modalities are used as
input, and the output is generated through an encoder-decoder language
model. The mixed tokens are fed into the transformer encoder, while the
decoder predicts the probability distribution of the next token in an
autoregressive manner at each step.

### 2.1 Speech-Driven Motion Generation

Human communication is multimodal and we use our speech, facial
expressions, and body gestures to communicate with each other. Given
this complimentary nature, recent work \[1, 31\] explores cross-modal
generation of human motion from speech in different forms. These models
are trained and evaluated on specific upper body joints, full body
joints, and even facial expressions. Recent work in co-speech gesture
generation often utilizes generative models to create gestures from
audio conditions \[12, 70, 8, 43\]. Other work also explores the
possibility of generating the listener’s motion \[47, 48, 60\]. Another
area of research focuses on generating speech-driven co-speech facial
expressions, with notable works including ViCO \[86\] and
CodeTalker \[68\]. However, these works are limited in that they only
take speech as input and do not utilize other forms of motion data,
making it challenging to follow both speech and textual cues. To tackle
this, we propose to unify input/output modalities with a language model
framework.

### 2.2 Text to Motion Generation

Humans communicate with spoken language and non-verbal means such as
emotions and interactions with surrounding environment \[25, 64\], among
other cues. Recent work has explored generating human motion from text
descriptions \[18, 44, 77, 24, 63, 16, 53, 57, 67, 26, 84, 77, 4, 13,
17\]. Some work attempts to generate human motion using diffusion
models \[58, 11, 79, 79, 59, 87, 73, 80\] while other work exploring
language models for generating human motion \[76, 23, 65, 83, 9, 62, 38,
81, 65\]. While these works have shown promising results in generating
human motion from text instructions, they fall short in capturing the
underlying meaning of the motion language itself. This limitation makes
it challenging to develop a model capable of generating human motion
from both verbal and non-verbal language. In this work, we propose a
novel framework to capture patterns in body language and subtle
expressive gestures inherently present in human communication.

### 2.3 Multimodal Language Models

Recent years have witnessed the rise of language models \[85, 14, 7, 55,
66, 54\], primarily leveraging transformer architectures \[61\] that
process text tokens as input and generate text tokens. Building upon
these advancements, substantial efforts have expanded into multimodal
language models capable of handling various types of input and output,
with notable examples including BLIP-2 \[32\], LLaVA \[42\], and
VideoChat \[35\]. Furthermore, the scope of multimodal language models
(MM-LLMs) has broadened to include modality-specific outputs, as
demonstrated by models like GILL \[27\] and SpeechGPT \[74\]. Efforts
such as LLaVA \[42\] and AudioGPT \[22\] are advancing towards seamless
any-to-any modality conversion, with the goal of emulating human-like
cognitive abilities in multimodal contexts. Inspired by this line of
work, we propose a new framework aimed at unifying verbal and non-verbal
language within language models. Our framework takes text, speech, and
motion data as input and generates human motion or text as output,
further exploring the potential synergy between different tasks and
modalities to enhance the performance of human motion generation.

## 3 Multimodal Language Model for Motion Generation and Understanding

In this section, we present a multimodal language model for motion
generation and understanding, which is illustrated in Fig. 2. We first
describe the tokenization of different modalities (Sec. 3.2), then we
introduce our generative pre-training for modality alignment (Sec. 3.3),
and finally, we detail post-training for instructions
following(Sec. 3.4).

### 3.1 Preliminaries

We use the neutral SMPL-X \[52\] body model including FLAME \[37\] face
model. This model is parameterized by per-person body shape
$`\mathbf{\beta}\in\mathbb{R}^{T\times 300}`$, 55 joint pose
$`\mathbf{g}\in\mathbb{R}^{T\times 55\times 3}`$, facial expression
$`\mathbf{\psi}\in\mathbb{R}^{T\times 100}`$, and global body
translation $`\mathbf{\gamma}\in\mathbb{R}^{T\times 3}`$, where $`T`$ is
the frame number.

### 3.2 Tokenization

In order for our modelt take various modalities as input (audio, tex,t
and motion), we first tokenize different modalities with
modality-specific tokenizers, and then combine them into a multimodal
vocabulary.

Compositional body motion tokenization. Following the motion
representation approach in EMAGE \[43\], we divide the body into four
parts with 6D rotation representation: 9 joints forming the lower-body
$`\mathbf{g}_{l}\in\mathbb{R}^{T\times 54}`$, 13 joints forming the
upper-body $`\mathbf{g}_{u}\in\mathbb{R}^{T\times 78}`$, 30 joints
forming the hands $`\mathbf{g}_{h}\in\mathbb{R}^{T\times 180}`$ and
1-joint along with 100 expression parameters representing the face
$`\mathbf{g}_{f}\in\mathbb{R}^{T\times 106}`$. Collectively, the motion
space is represented as
$`G=\{\mathbf{g}_{f},\mathbf{g}_{h},\mathbf{g}_{u},\mathbf{g}_{l}\}`$.
Notably, we avoid using the commonly adopted HumanML3D representation
\[16\] (H3D-Format) in text-to-motion tasks, as it predominantly focuses
on skeletal movement, emphasizing swinging motions while overlooking
twisting rotations of body parts—an essential aspect for effectively
conveying body language. With this compositional representation, we
train four separate VQ-VAEs to tokenize the body pose for each part.
Each VQ-VAE encoder $`\mathcal{E}`$ applies a four-layer temporal
convolutional network (TCN) to extract continuous latent motion features
$`{\mathbf{z}}^{1:T}=\mathcal{E}(\mathbf{g}^{1:T})`$. This encoded
representation $`\mathbf{z}^{1:T}`$ is quantized using:

```math
\displaystyle\begin{split}\mathbf{q}^{t}=\mathcal{Q}(\mathbf{z}^{t}):=\arg\min_{\mathbf{q}^{k}\in Q}\|\mathbf{z}^{t}-\mathbf{q}^{k}\|^{2}\end{split} \tag{1}
```

where $`\mathbf{q}^{t}`$ is the discrete code in the codebook
representing the encoded $`\mathbf{z}^{t}`$. Collectively, the quantized
motion latent space is
$`Q=\{\mathbf{q}_{f},\mathbf{q}_{h},\mathbf{q}_{u},\mathbf{q}_{l}\}`$.
Each VQ-VAE decoder $`\mathcal{D}`$ decodes the quantized motion
$`\mathbf{q}^{t}`$ back into the motion space
$`\mathbf{\hat{g}}^{1:T}=\mathcal{D}(\mathbf{q}^{1:T})`$ and applies the
following reconstruction losses:

```math
\displaystyle\begin{split}\mathcal{L}_{total}=&\mathcal{L}_{\text{rec}}(\mathbf{g},\mathbf{\hat{g}})+\mathcal{L}_{\text{vel}}(\mathbf{g^{\prime}},\mathbf{\hat{g}^{\prime}})+\\
&\mathcal{L}_{\text{acc}}(\mathbf{g^{\prime\prime}},\mathbf{\hat{g}^{\prime\prime}})+\mathcal{L}_{\text{mrec}}(\mathbf{g},\mathbf{\hat{g}})+\\
&\mathcal{L}_{\text{mvel}}(\mathbf{g^{\prime}},\mathbf{\hat{g}^{\prime}})+\mathcal{L}_{\text{macc}}(\mathbf{g^{\prime\prime}},\mathbf{\hat{g}^{\prime\prime}})+\\
&\mathcal{L}_{\text{comm}}(\mathbf{g},\mathbf{{q}}),\end{split} \tag{2}
```

where $`\mathbf{\hat{g}^{\prime}}`$ represent the reconstructed motion,
$`\mathbf{\hat{g}^{\prime}}`$ and $`\mathbf{g^{\prime}}`$ represent the
velocity of $`\mathbf{\hat{g}}`$ and $`\mathbf{g}`$, while
$`\mathbf{\hat{g}^{\prime\prime}}`$ and $`\mathbf{g^{\prime\prime}}`$
represent their acceleration. For lower-body, upper-body and hands
VQ-VAEs, pose reconstruction loss $`\mathcal{L}_{rec}`$ is a Geodesic
loss. For face VQ-VAE, $`\mathcal{L}_{rec}`$ is $`\ell_{2}`$ loss. Pose
velocity/acceleration losses $`\mathcal{L}_{vel}`$ and
$`\mathcal{L}_{acc}`$ are $`\ell_{1}`$ losses. Mesh reconstruction loss
$`\mathcal{L}_{mrec}`$ is $`\ell_{2}`$ loss. Mesh velocity/acceleration
losses $`\mathcal{L}_{mvel}`$ and $`\mathcal{L}_{macc}`$ are
$`\ell_{1}`$ losses. Codebook commitment loss $`\mathcal{L}_{comm}`$ is
$`\ell_{2}`$ loss. Vertices of the SMPLX-2020 mesh computed from the
pose $`\mathbf{g}`$ and $`\mathbf{\hat{g}}`$ are used to compute mesh
losses.

Speech tokenization. Similar to the motion modality, speech data is also
continuous by nature. To facilitate speech training within a language
model, we used HuBERT \[20\] to represent audio streams as discrete
tokens. In this work, audio input is sampled at 16 kHz, resulting in
$`\mathbf{a}\in\mathbb{R}^{T\times s}`$, where $`s`$ represents the
audio frame rate after quantization. HuBERT further downsamples audio by
a factor of 320, resulting in $`s=50`$. This frame rate, compared to the
typical motion frame rate of 30 fps, provides an acceptable input token
length for language models. The resulting audio token space is noted as
$`A=\{\mathbf{a}\}`$.

Text tokenization. Following previous work \[23, 55\], we use
SentencePiece \[28\] to tokenize text inputs and outputs into WordPiece
tokens \[56, 29\] for the language model, with a vocabulary of 32,000
wordpieces inherited from the T5 \[55\] language model, which can be
represented as $`W=\{\mathbf{w}\}`$. This vocabulary enables the model
to process a fixed set of predetermined languages. Additionally, we
extend the vocabulary with several multimodal tokens to support
multi-modal inputs.

Figure 3: Illustration of pre-training. We pre-train our language model
by translating one modality to another using paired data.

Multimodal vocabulary. Altogether, we have a combined token space
defined as
$`M:=Q\cup A\cup W\cup C=\{\mathbf{q}_{f},\mathbf{q}_{u},\mathbf{q}_{h},\mathbf{q}_{l},\mathbf{a},\mathbf{w}\}`$.
Each modality-specific tokenizer outputs its modality-specific
vocabulary. To build a unified language model that can process these
different modalities, we need to combine these vocabularies into a joint
vocabulary. Since the language model is pre-trained with the text
modality, we choose to extend the original text vocabulary
$`V_{t}=\{v_{t}^{i}\}_{i=1}^{K_{t}}`$ with vocabularies from other
modalities, including audio $`V_{a}=\{v_{a}^{i}\}_{i=1}^{K_{a}}`$, face
$`V_{f}=\{v_{f}^{i}\}_{i=1}^{K_{f}}`$, hands
$`V_{h}=\{v_{h}^{i}\}_{i=1}^{K_{h}}`$, upper body
$`V_{u}=\{v_{u}^{i}\}_{i=1}^{K_{u}}`$, and lower body
$`V_{l}=\{v_{l}^{i}\}_{i=1}^{K_{l}}`$, following previous work \[23\].
In particular, the motion vocabulary is defined as a combination of four
body-part vocabularies:
$`V_{m}=\{v_{f}^{i},v_{h}^{i},v_{u}^{i},v_{l}^{i}\}_{i=1}^{K_{m}}`$.
Additionally, each modality-specific vocabulary includes special tokens
for boundary recognition, such as $`<`$/soa$`>`$ and $`<`$/eoa$`>`$ to
indicate the start and end of an audio sequence. As a result, all
modalities can be represented in a unified format with one joint
multimodal vocabulary $`V=\{V_{t},V_{a},V_{f},V_{h},V_{u},V_{l}\}`$.

### 3.3 Pre-training for Modality Alignment

Existing motion generation models rely heavily on paired data to train
downstream tasks. Yet, collecting high-quality paired motion data is
both costly and time consuming while there exists a large amount of
unpaired data of each modality that can be explored. Inspired by this,
we introduce our generative pre-training strategy, as shown in Fig. 3.
More specifically, we implement two types of modality alignment during
the pre-training stage: compositional motion alignment and audio–text
alignment that are detailed below.

Compositional body motion alignment. Our body motion is inherently
compositional, i.e., different body parts move in accordance. For
example, when we are happy, our faces express smiles and our gestures
tend to become more positive. The correlation between different body
part motions is universal, transcending cultural boundaries. This shared
prior forms the basis of our approach. To explore this correspondence,
we consider two types of motion alignment tasks: spatial and temporal.

Spatial. To model the correlation between these different body parts, we
train the model to take in a randomly selected combination of body parts
(e.g., upper or upper + face) and predict another randomly selected
combination of other body parts (e.g., lower or lower + hand). This
helps our model learn the spatial relations between body parts. Below is
one example template that defines task prompts, conditions, and answers.
The model takes both prompts and conditions as input and is expected to
output the answer.

Task Prompts: Translate upper to lower body.  
Conditions: Upper Body Tokens
$`V_{\text{condition}}=\{v_{u}^{i}\in V_{u}\mid i\in\{\text{sequence token index}\}\}`$  
Answer: Lower Body Tokens
$`V_{\text{Answer}}=\{v_{l}^{i}\in V_{l}\mid i\in\{\text{sequence token index}\}\}`$

Temporal. Predicting how motion changes as a function of time is also an
important self-supervision, which enables the model to capture the
temporal evolution of motion. We model this by randomly masking off
certain motion frames to help the model learn the temporal priors of
motion.

Task Prompts: Translate mask to unmasked motion.  
Conditions: Masked Tokens
$`V_{\text{condition}}=\{v_{m}^{i}\in V_{m}\mid i\in\{\text{masked sequence token index}\}\}.`$  
Answer: Unmasked Motion Tokens
$`V_{\text{Answer}}=\{v_{m}^{i}\in V\mid i\in\{\text{unmasked sequence token index}\}\}`$

Audio-text alignment. In addition to the motion modality, we also design
translation tasks between audio and text modalities, leveraging the
abundance of available data. These tasks follow the format of
“predicting modality Y from modality X”. For example, “predicting text
from audio” should help the model’s performance in “predicting motion
from audio” by mapping the audio embeddings into the well-pre-trained
text embedding space.

### 3.4 Post-training with Instruction Following

After pre-training, the model gains an understanding of the underlying
grammar and syntax within motion modality’s vocabulary and good
alignment between audio and text modalities. We then fine-tune the model
with paired data on downstream tasks such as co-speech gesture
generation or text-to-motion generation. To enable the model to perform
desired downstream tasks while following natural human instructions, we
construct a multi-task instruction-following template by formatting
several key tasks such as audio-to-motion, text-to-motion, and
emotion-to-motion into instructions. Specifically, for each task, we
compose dozens of different instruction templates, resulting in more
than one thousand different tasks, each having a unique instruction
prompt. An example of our instruction template is shown below. See Supp.
for more examples.

Task Prompts: Based on $`<\text{Audio}\_\text{Placeholder}>`$, generate
a full-body movement sequence involving face, hands, upper body, and
lower body that matches the audio’s rhythm.  
Conditions: Audio Tokens
$`V_{\text{condition}}=\{v_{a}^{i}\in V_{a}\mid i\in\{\text{audio sequence token index}\}\}`$  
Answer: Unmasked Motion Tokens
$`V_{\text{Answer}}=\{v_{m}^{i}\in V\mid i\in\{\text{ motion sequence token index}\}\}`$

|                                  |                    |                |                       |                     |
| -------------------------------- | ------------------ | -------------- | --------------------- | ------------------- |
|                                  | FGD $`\downarrow`$ | BC$`\uparrow`$ | Diversity$`\uparrow`$ | Condition Signal    |
| DisCo \[40\]                     | 9.417              | 6.439          | 9.912                 | audio               |
| CaMN \[41\]                      | 6.644              | 6.769          | 10.86                 | audio, text, facial |
| DiffStyleGesture \[69\]          | 8.811              | 7.241          | 11.49                 | audio, style        |
| Habibie et al. \[19\]            | 9.040              | 7.716          | 8.213                 | audio, text         |
| TalkSHOW \[71\]                  | 6.209              | 6.947          | 13.47                 | audio               |
| SynTalker \[8\]                  | 6.413              | 7.971          | 12.721                | audio, text         |
| EMAGE \[43\]                     | 5.512              | 7.724          | 13.06                 | audio, text         |
| Ours w/o language pre-training   | 7.470              | 6.148          | 14.162                | audio               |
| Ours w/o multimodal pre-training | 5.408              | 7.742          | 14.418                | audio               |
| Ours                             | 5.301              | 7.780          | 15.167                | audio               |

Table 1: Co-speech gesture generation results on BEATv2 benchmark. We
report FGD $`\times 10^{-1}`$, BC $`\times 10^{-1}`$, Diversity, which
measures realism, speech-motion synchronization, and diversity
respectively. Our model outperforms state-of-the-art methods on this
benchmark.

### 3.5 Language Model Training Details

Our model leverages 220M pre-trained Flan-T5-Base model \[55\] with an
encoder–decoder transformer structure to address the conditional
generation task. Through our shared multimodal vocabulary $`V`$, every
input modality is represented as “text” tokens, allowing us to fully
leverage the original T5 model for each conditional generation task.
Specifically, with constructed modality latent codebook indices—such as
index 8 of the upper body codebook—the upper body can be formatted as
“$`<\text{upper}\_8>`$”. Thus, the input can be converted into a
sequence of tokens $`S_{i}=\{s_{i}^{k}\}_{k=1}^{L}`$, where
$`s_{i}\in V`$ and $`L`$ represents the input length. Similarly, the
model outputs a sequence of tokens $`S_{o}=\{s_{o}^{k}\}_{k=1}^{L}`$,
with a fixed input/output token length and $`s_{o}\in V`$.

Since our model is encoder-decoder architecture, we set a maximum input
length of 512. We specify modalities with start and stop tokens.
Following the original T5 implementation, the sequence of tokens is sent
to the encoder, and the decoder then performs next-token predictions in
an auto-regressive manner at each step. The training objective can be
formulated as follows:

```math
\mathcal{L}_{LM}=-\sum_{k=0}^{L_{t}-1}\log p_{\theta}(s_{t}^{k}|s_{t}^{<k},s_{i}), \tag{3}
```

where $`s_{t}`$ represents each token within the sequence, serving as
the index in our unified vocabulary $`V`$. Through next-token
prediction, our model learns the underlying distribution of each
modality, enabling the accurate and meaningful generation of target
“words”. For both pre-training and post-training, we finetune the
model’s entire weights instead of performing low-rank adaptation
(LORA \[21\]) since our goal is to maximally align each modality.

|                  |                    |                |                       |
| ---------------- | ------------------ | -------------- | --------------------- |
|                  | FGD $`\downarrow`$ | BC$`\uparrow`$ | Diversity$`\uparrow`$ |
| W/o pre-training | 5.501              | 7.721          | 14.281                |
| W/o A2T          | 5.443              | 7.721          | 14.499                |
| W/o spatial      | 6.336              | 7.381          | 14.173                |
| W/o temporal     | 6.800              | 7.341          | 13.810                |
| W/o motion       | 7.776              | 7.344          | 14.640                |
| Ours             | 5.301              | 7.780          | 15.165                |

Table 2: Ablations of pre-training.

## 4 Experiments

In this section, we first evaluate our model on the co-speech gesture
generation benchmark, then investigate the generalization enabled by
generative multimodal pre-training, demonstrate our model’s capability
in following both audio and text prompts, and lastly our novel ability
to predict emotion from motion.

### 4.1 Co-Speech Gesture Generation

To evaluate our model’s audio-to-motion generation ability, we choose to
benchmark on co-speech gesture generation on the BEATv2 dataset \[43\],
where the goal is to generate body gesture motion for a given speech of
a speaker. Existing co-speech generation work typically models
speaker-dependent gestures \[71, 48, 43\]. During the pre-training
stage, our model utilizes large-scale unpaired data in a self-supervised
setup, drawing from two primary datasets, BEATv2 and Librispeech \[50\].
Together, these datasets provide approximately 1,000 hours of
audio-to-text data and 60 hours of motion data. During the
post-training, to ensure a fair comparison with baselines, we adopt the
same evaluation protocol as \[43\], i.e., training and testing on
speaker-2 and using their motion tokenizer. For pre-training, we ensure
the model does not see any audio-to-motion data. Following prior
work \[43\], we adopt Frechet Gesture Distance (FGD) \[72\] to evaluate
the realism of the body gestures, Beat Correlation (BC) \[36\] to assess
speech-motion synchrony and Diversity \[31\], which is calculated with
the $`\ell_{1}`$ distance between multiple body gesture clips.

The results are shown in Table 1. Compared with the state-of-the-art
methods on this benchmark, our model achieves better performance across
all metrics, indicating that our model generates more realistic, and
diverse motion that is synchronized with the speech. Existing work often
supplies additional signals to the model to boost the model’s
performance such as the text transcribed from the speech \[41, 19, 43\]
or onset/amplitudes \[43\], partially due to the lack of semantic
understanding of speech. In our model, since we use a pre-trained
language model, the model naturally has a strong semantic understanding,
allowing our model to show competitive performance without heavy
reliance on hand-crafting features. If we use randomly initialized model
weights, we can see that the model’s performance drops drastically,
indicating that language pre-training is vital for co-speech gesture
generation. If we remove our multimodal pre-training stage, the model’s
performance also deteriorates, showing that our model benefits from the
generative pre-training.

To further understand our model’s performance, we show some qualitative
results of our model in Fig. 4. We can see that our model generates
gestures that are synchronized with the speech. See Supp. video for more
examples.

![](arxiv-2412-10523--dabd69cd1dff.figures/figure-2.webp)

Figure 4: Qualitative example on co-speech gesture generation. Given a
speech, we visualize the ground truth 3D motion accompanying the audio,
the motion generated by the baseline EMAGE \[43\], SynTalker \[8\] and
our method. Our model generates more diverse and expressive motion
compared to the baseline, especially when the speaker emphasizes on
certain words such as “tired” and “because”.

Figure 5: Generation performance vs. the amount of post-training data.
Our model learns a stronger motion prior from pre-training and thus
shows much better under data scarcity.

### 4.2 Effect of Generative Pre-training

Generating gesture motion for a new speaker requires collecting
high-quality motion data, typically from motion capture systems.
Collecting such data is time-consuming. In this section, we first
validate the importance of each pre-training task and then investigate
whether our generative pre-training leads to better generalization on
new speakers and thus reduces the amount of data required for training.

Validating pre-training tasks. To understand how different pre-training
objectives contribute to the performance, we ablate the audio-to-text
alignment task (“w/o A2T”), the spatial body motion alignment task (“w/o
spatial”), the temporal body motion alignment task (“w/o temporal”) and
the whole body alignment task (“w/o motion”).

![](arxiv-2412-10523--dabd69cd1dff.figures/figure-3.webp)

Figure 6: Editable gesture generation. We prompt the language with text
and audio information and it outputs motions that are both expressional
gesture motion as well as general movement motion.

The results are shown in Table 1. “w/o A2T” lowers the model’s
performance, indicating that aligning the audio embedding space with
text helps with semantic understanding and also the downstream gesture
generation task. Removing either spatial motion prediction, temporal
motion prediction or them altogether hurts the performance, showing that
learning spatial-temporal motion priors in the pre-training stage is
important for the downstream tasks.

Effect on the training data. We hypothesize that our pre-training
strategy captures strong multimodal correlation and motion priors, which
could reduce the reliance on the amount of paired data for downstream
tasks. To validate this hypothesis, we follow the setting in Sec. 4.1
and limit the amount of training data available to the model during the
pre-training stage. Note that the model has never seen audio2motion data
during pre-training. We set the amount of the data to
$`\frac{1}{2^{n}},n\in[1...5]`$. We train our full model, our model
without pre-training and EMAGE to convergence under each setting and
evaluate on the same test set.

The results are shown in Figure 5. We can see that our full model starts
with much lower FGD compared with the model without pre-training even
when only using 1/32 of the paired training. As expected, as the amount
of paired fine-tuning data increases, the performance reduces but our
full model always outperforms the w/o pre-training ablation and EMAGE,
showing that our model benefits pre-training and shows greater
generalization under extreme data scarcity.

### 4.3 Unifying Audio-to-Motion and Text-to-Motion for Editable Generation

By taking a language model-driven approach, our model is capable of
following both audio and text prompts. We first train the motion
tokenizer on both BEATv2 and AMASS \[46\] datasets since the range of
motion in these two datasets is very different. We use the same tasks
for pre-training. For post-training, we combine Audio2Motion and
Text2Motion with various instructions, in which text-to-motion with
HumanML3D \[16\] text annotations. See Supp. for details.

![](arxiv-2412-10523--dabd69cd1dff.figures/figure-4.webp)

Figure 7: Qualitative example of emotion prediction.

By training on both text-to-motion and audio-to-motion data, our model
supports joint audio-text prompts, enabling what we call editable
gesture generation. This approach facilitates the generation of
synergistic full-body motions conditioned on both speech and flexibly
chosen prompts. For instance, the model can generate the motion of a
person walking while talking. In this work, we demonstrate this
capability by prompting the model separately for specific body part
motions and then combining them seamlessly. Combining conversation
gestures with daily motions is extremely useful for applications such as
gaming or VR. We show several qualitative examples in Fig. 6. We can see
that the model can generate human motion that follows both audio and
text prompts, showing the emergent capabilities of our model. See Supp.
video for more examples.

### 4.4 Predicting Emotion from Motion

Our model’s flexibility in the input/output modality also unlocks an
array of new tasks such as translation between different body parts or
modalities. In this section, we propose a novel task that predicts
emotion from motion.

Reading someone’s body language, i.e., predicting emotion from motion is
important for applications such as mental health or psychiatry, however,
existing audio2motion or motion2text do not have this capability. We
extract the emotion labels (neutral, anger, happiness, fear, disgust,
sadness, contempt, and surprise) on BEATv2 and convert them into
instructions for training. To be compatible with arbitrary language
output from MotionGPT, we evaluate the model performance by measuring
the BLEU \[51\], Rouge Cider \[39\], and BERTScore \[82\] between the
prediction and the ground truth, which measures the semantic distances
between texts. See more details in Supp.

The results are shown in Table 3. MotionGPT entirely fails this task
with a performance similar to a random baseline because it was only
trained to caption general motion rather than subtle gesture movement
and body language. Our model outperforms the random and MotionGPT by a
large margin, showing our model’s ability to predict the emotion from
motion. We also show one qualitative example in Fig. 7.

|           |                    |                         |                       |
| --------- | ------------------ | ----------------------- | --------------------- |
|           | Bleu@1$`\uparrow`$ | Rouge Cider$`\uparrow`$ | BertScore$`\uparrow`$ |
| GT        | 100                | 100                     | 99.9                  |
| Random    | 2.45               | 4.44                    | 0.19                  |
| MotionGPT | 1.68               | 10.67                   | 2.31                  |
| Ours      | 14.71              | 26.67                   | 16.94                 |

Table 3: Motion to emotion. We prompt our model to predict emotion given
a motion sequence.

## 5 Discussion

In this work, we propose a novel multimodal language model to unify
verbal and non-verbal language with a novel pre-training objective. Our
model not only shows state-of-the-art performance on co-speech gestures
but also unlocks an array of novel tasks.

While promising, the model sometimes fails to produce coherent motion
potentially due to discrete motion tokenization. Moving forward, we
believe incorporating continuous tokenization is an important step to
improve the quality of the generated motion.

We believe unifying verbal and non-verbal language of human motion
generation and understanding is crucial for real-world applications, and
language models provide a powerful framework to approach that goal.

#### Acknowledgments:

This project was partially funded by NIH grant R01AG089169 and UST. The
authors would also like to thank Georgios Pavlakos for his valuable
discussion, Chaitanya Patel, Jingyan Zhang, and Bin Li for their
feedback on the paper.

## References

- \[1\] Chaitanya Ahuja, Dong Won Lee, Yukiko I Nakano, and
  Louis-Philippe Morency. Style transfer for co-speech gesture
  animation: A multi-speaker conditional-mixture approach. In _ECCV_,
  pages 248–265. Springer, 2020.
- \[2\] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech,
  Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katherine Millican,
  Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda
  Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob Menick,
  Sebastian Borgeaud, Andrew Brock, Aida Nematzadeh, Sahand Sharifzadeh,
  Mikolaj Binkowski, Ricardo Barreira, Oriol Vinyals, Andrew Zisserman,
  and Karen Simonyan. Flamingo: a visual language model for few-shot
  learning. In _Advances in Neural Information Processing
  Systems_, 2022.
- \[3\] Tenglong Ao, Zeyi Zhang, and Libin Liu. Gesturediffuclip:
  Gesture diffusion model with clip latents. _ACM Transactions on
  Graphics (TOG)_, 42(4):1–18, 2023.
- \[4\] Nikos Athanasiou, Alpár Ceske, Markos Diomataris, Michael J
  Black, and Gül Varol. Motionfix: Text-driven 3d human motion editing.
  _arXiv preprint arXiv:2408.00712_, 2024.
- \[5\] Bharat Lal Bhatnagar, Xianghui Xie, Ilya A Petrov, Cristian
  Sminchisescu, Christian Theobalt, and Gerard Pons-Moll. Behave:
  Dataset and method for tracking human object interactions. In _CVPR_,
  pages 15935–15946, 2022.
- \[6\] Zalán Borsos, Raphaël Marinier, Damien Vincent, Eugene
  Kharitonov, Olivier Pietquin, Matt Sharifi, Dominik Roblek, Olivier
  Teboul, David Grangier, Marco Tagliasacchi, and Neil Zeghidour.
  Audiolm: a language modeling approach to audio generation, 2023.
- \[7\] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared
  Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish
  Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen
  Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler,
  Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler,
  Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher
  Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario
  Amodei. Language models are few-shot learners, 2020.
- \[8\] Bohong Chen, Yumeng Li, Yao-Xiang Ding, Tianjia Shao, and Kun
  Zhou. Enabling synergistic full-body control in prompt-based co-speech
  motion generation. In _Proceedings of the 32nd ACM International
  Conference on Multimedia_, pages 6774–6783, 2024a.
- \[9\] Ling-Hao Chen, Shunlin Lu, Ailing Zeng, Hao Zhang, Benyou Wang,
  Ruimao Zhang, and Lei Zhang. Motionllm: Understanding human behaviors
  from human motions and videos, 2024b.
- \[10\] Xin Chen, Biao Jiang, Wen Liu, Zilong Huang, Bin Fu, Tao Chen,
  and Gang Yu. Executing your commands via motion diffusion in latent
  space. In _CVPR_, pages 18000–18010, 2023a.
- \[11\] Xin Chen, Biao Jiang, Wen Liu, Zilong Huang, Bin Fu, Tao Chen,
  Jingyi Yu, and Gang Yu. Executing your commands via motion diffusion
  in latent space. In _CVPR_, 2023b.
- \[12\] Kiran Chhatre, Radek Daněček, Nikos Athanasiou, Giorgio
  Becherini, Christopher Peters, Michael J. Black, and Timo Bolkart.
  AMUSE: Emotional speech-driven 3D body animation via disentangled
  latent diffusion. In _CVPR_, pages 1942–1953, 2024.
- \[13\] Seunggeun Chi, Hyung-gun Chi, Hengbo Ma, Nakul Agarwal, Faizan
  Siddiqui, Karthik Ramani, and Kwonjoon Lee. M2d2m: Multi-motion
  generation from text with discrete diffusion models. _arXiv preprint
  arXiv:2407.14502_, 2024.
- \[14\] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina
  Toutanova. Bert: Pre-training of deep bidirectional transformers for
  language understanding, 2019.
- \[15\] Yuan Gong, Hongyin Luo, Alexander H Liu, Leonid Karlinsky, and
  James Glass. Listen, think, and understand. _arXiv preprint
  arXiv:2305.10790_, 2023.
- \[16\] Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, Wei Ji, Xingyu Li,
  and Li Cheng. Generating diverse and natural 3d human motions from
  text. In _CVPR_, pages 5152–5161, 2022a.
- \[17\] Chuan Guo, Xinxin Zuo, Sen Wang, and Li Cheng. Tm2t: Stochastic
  and tokenized modeling for the reciprocal generation of 3d human
  motions and texts. In _ECCV_, pages 580–597. Springer, 2022b.
- \[18\] Chuan Guo, Yuxuan Mu, Muhammad Gohar Javed, Sen Wang, and Li
  Cheng. Momask: Generative masked modeling of 3d human motions. In
  _CVPR_, pages 1900–1910, 2024.
- \[19\] Ikhsanul Habibie, Weipeng Xu, Dushyant Mehta, Lingjie Liu,
  Hans-Peter Seidel, Gerard Pons-Moll, Mohamed Elgharib, and Christian
  Theobalt. Learning speech-driven 3d conversational gestures from
  video, 2021.
- \[20\] Wei-Ning Hsu, Benjamin Bolte, Yao-Hung Hubert Tsai, Kushal
  Lakhotia, Ruslan Salakhutdinov, and Abdelrahman Mohamed. Hubert:
  Self-supervised speech representation learning by masked prediction of
  hidden units. _IEEE/ACM transactions on audio, speech, and language
  processing_, 29:3451–3460, 2021.
- \[21\] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu,
  Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. Lora: Low-rank
  adaptation of large language models. _arXiv preprint
  arXiv:2106.09685_, 2021.
- \[22\] Rongjie Huang, Mingze Li, Dongchao Yang, Jiatong Shi, Xuankai
  Chang, Zhenhui Ye, Yuning Wu, Zhiqing Hong, Jiawei Huang, Jinglin Liu,
  et al. Audiogpt: Understanding and generating speech, music, sound,
  and talking head. In _AAAI_, pages 23802–23804, 2024.
- \[23\] Biao Jiang, Xin Chen, Wen Liu, Jingyi Yu, Gang Yu, and Tao
  Chen. Motiongpt: Human motion as a foreign language. In
  _NeurIPS_, 2023.
- \[24\] Biao Jiang, Xin Chen, Chi Zhang, Fukun Yin, Zhuoyuan Li, Gang
  Yu, and Jiayuan Fan. Motionchain: Conversational motion controllers
  via multimodal prompts. In _ECCV_, pages 54–74. Springer, 2025.
- \[25\] Nan Jiang, Zhiyuan Zhang, Hongjie Li, Xiaoxuan Ma, Zan Wang,
  Yixin Chen, Tengyu Liu, Yixin Zhu, and Siyuan Huang. Scaling up
  dynamic human-scene interaction modeling. In _Proceedings of the
  IEEE/CVF Conference on Computer Vision and Pattern Recognition_, pages
  1737–1747, 2024.
- \[26\] Korrawe Karunratanakul, Konpat Preechakul, Supasorn
  Suwajanakorn, and Siyu Tang. Guided motion diffusion for controllable
  human motion synthesis. In _ICCV_, pages 2151–2162, 2023.
- \[27\] Jing Yu Koh, Daniel Fried, and Russ R Salakhutdinov. Generating
  images with multimodal language models. _Advances in Neural
  Information Processing Systems_, 36, 2024.
- \[28\] T Kudo. Sentencepiece: A simple and language independent
  subword tokenizer and detokenizer for neural text processing. _arXiv
  preprint arXiv:1808.06226_, 2018a.
- \[29\] Taku Kudo. Subword regularization: Improving neural network
  translation models with multiple subword candidates. _arXiv preprint
  arXiv:1804.10959_, 2018b.
- \[30\] Gen Li, Kaifeng Zhao, Siwei Zhang, Xiaozhong Lyu, Mihai
  Dusmanu, Yan Zhang, Marc Pollefeys, and Siyu Tang. EgoGen: An
  Egocentric Synthetic Data Generator. In _IEEE Conference on Computer
  Vision and Pattern Recognition (CVPR)_, 2024.
- \[31\] Jing Li, Di Kang, Wenjie Pei, Xuefei Zhe, Ying Zhang, Zhenyu
  He, and Linchao Bao. Audio2gestures: Generating diverse gestures from
  speech audio with conditional variational autoencoders. In
  _Proceedings of the IEEE/CVF International Conference on Computer
  Vision_, pages 11293–11302, 2021a.
- \[32\] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. Blip-2:
  Bootstrapping language-image pre-training with frozen image encoders
  and large language models. In _International conference on machine
  learning_, pages 19730–19742. PMLR, 2023a.
- \[33\] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. BLIP-2:
  bootstrapping language-image pre-training with frozen image encoders
  and large language models. In _ICML_, 2023b.
- \[34\] Jiaman Li, Karen Liu, and Jiajun Wu. Ego-body pose estimation
  via ego-head pose estimation. In _Proceedings of the IEEE/CVF
  Conference on Computer Vision and Pattern Recognition_, pages
  17142–17151, 2023c.
- \[35\] KunChang Li, Yinan He, Yi Wang, Yizhuo Li, Wenhai Wang, Ping
  Luo, Yali Wang, Limin Wang, and Yu Qiao. Videochat: Chat-centric video
  understanding. _arXiv preprint arXiv:2305.06355_, 2023d.
- \[36\] Ruilong Li, Shan Yang, David A. Ross, and Angjoo Kanazawa. Ai
  choreographer: Music conditioned 3d dance generation with aist++,
  2021b.
- \[37\] Tianye Li, Timo Bolkart, Michael J Black, Hao Li, and Javier
  Romero. Learning a model of facial shape and expression from 4d scans.
  _ACM Trans. Graph._, 36(6):194–1, 2017.
- \[38\] Han Liang, Jiacheng Bao, Ruichi Zhang, Sihan Ren, Yuecheng Xu,
  Sibei Yang, Xin Chen, Jingyi Yu, and Lan Xu. Omg: Towards
  open-vocabulary motion generation via mixture of controllers. In
  _CVPR_, pages 482–493, 2024.
- \[39\] Chin-Yew Lin. Rouge: A package for automatic evaluation of
  summaries. In _Text summarization branches out_, pages 74–81, 2004.
- \[40\] Haiyang Liu, Naoya Iwamoto, Zihao Zhu, Zhengqing Li, You Zhou,
  Elif Bozkurt, and Bo Zheng. Disco: Disentangled implicit content and
  rhythm learning for diverse co-speech gestures synthesis. In
  _Proceedings of the 30th ACM International Conference on Multimedia_,
  pages 3764–3773, 2022a.
- \[41\] Haiyang Liu, Zihao Zhu, Naoya Iwamoto, Yichen Peng, Zhengqing
  Li, You Zhou, Elif Bozkurt, and Bo Zheng. Beat: A large-scale semantic
  and emotional multi-modal dataset for conversational gestures
  synthesis. In _ECCV_, 2022b.
- \[42\] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual
  instruction tuning, 2023a.
- \[43\] Haiyang Liu, Zihao Zhu, Giorgio Becherini, Yichen Peng,
  Mingyang Su, You Zhou, Xuefei Zhe, Naoya Iwamoto, Bo Zheng, and
  Michael J. Black. Emage: Towards unified holistic co-speech gesture
  generation via expressive masked audio gesture modeling. In
  _CVPR_, 2024.
- \[44\] Jinpeng Liu, Wenxun Dai, Chunyu Wang, Yiji Cheng, Yansong Tang,
  and Xin Tong. Plan, posture and go: Towards open-world text-to-motion
  generation. _arXiv preprint arXiv:2312.14828_, 2023b.
- \[45\] Naureen Mahmood, Nima Ghorbani, Nikolaus F. Troje, Gerard
  Pons-Moll, and Michael J. Black. Amass: Archive of motion capture as
  surface shapes. In _ICCV_, 2019a.
- \[46\] Naureen Mahmood, Nima Ghorbani, Nikolaus F Troje, Gerard
  Pons-Moll, and Michael J Black. Amass: Archive of motion capture as
  surface shapes. In _ICCV_, pages 5442–5451, 2019b.
- \[47\] Evonne Ng, Hanbyul Joo, Liwen Hu, Hao Li, Trevor Darrell,
  Angjoo Kanazawa, and Shiry Ginosar. Learning to listen: Modeling
  non-deterministic dyadic facial motion. In _CVPR_, 2022.
- \[48\] Evonne Ng, Sanjay Subramanian, Dan Klein, Angjoo Kanazawa,
  Trevor Darrell, and Shiry Ginosar. Can language models learn to
  listen? In _ICCV_, 2023.
- \[49\] Evonne Ng, Javier Romero, Timur Bagautdinov, Shaojie Bai,
  Trevor Darrell, Angjoo Kanazawa, and Alexander Richard. From audio to
  photoreal embodiment: Synthesizing humans in conversations, 2024.
- \[50\] Vassil Panayotov, Guoguo Chen, Daniel Povey, and Sanjeev
  Khudanpur. Librispeech: an asr corpus based on public domain audio
  books. In _2015 IEEE international conference on acoustics, speech and
  signal processing (ICASSP)_, pages 5206–5210. IEEE, 2015.
- \[51\] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu.
  Bleu: a method for automatic evaluation of machine translation. In
  _Proceedings of the 40th annual meeting of the Association for
  Computational Linguistics_, pages 311–318, 2002.
- \[52\] Georgios Pavlakos, Vasileios Choutas, Nima Ghorbani, Timo
  Bolkart, Ahmed AA Osman, Dimitrios Tzionas, and Michael J Black.
  Expressive body capture: 3d hands, face, and body from a single image.
  In _CVPR_, pages 10975–10985, 2019.
- \[53\] Mathis Petrovich, Michael J Black, and Gül Varol. Temos:
  Generating diverse human motions from textual descriptions. In
  _European Conference on Computer Vision_, pages 480–497.
  Springer, 2022.
- \[54\] Ryan Po, Wang Yifan, Vladislav Golyanik, Kfir Aberman,
  Jonathan T Barron, Amit Bermano, Eric Chan, Tali Dekel, Aleksander
  Holynski, Angjoo Kanazawa, et al. State of the art on diffusion models
  for visual computing. In _Computer Graphics Forum_, page e15063. Wiley
  Online Library, 2024.
- \[55\] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan
  Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu.
  Exploring the limits of transfer learning with a unified text-to-text
  transformer, 2023.
- \[56\] Rico Sennrich. Neural machine translation of rare words with
  subword units. _arXiv preprint arXiv:1508.07909_, 2015.
- \[57\] Yonatan Shafir, Guy Tevet, Roy Kapon, and Amit H Bermano. Human
  motion diffusion as a generative prior. _arXiv preprint
  arXiv:2303.01418_, 2023.
- \[58\] Guy Tevet, Sigal Raab, Brian Gordon, Yonatan Shafir, Daniel
  Cohen-Or, and Amit H. Bermano. Human motion diffusion model. In
  _ICLR_, 2022.
- \[59\] Guy Tevet, Sigal Raab, Brian Gordon, Yoni Shafir, Daniel
  Cohen-or, and Amit Haim Bermano. Human motion diffusion model. In _The
  Eleventh International Conference on Learning Representations_, 2023.
- \[60\] Minh Tran, Di Chang, Maksim Siniukov, and Mohammad Soleymani.
  Dyadic interaction modeling for social behavior generation. In
  _ECCV_, 2024.
- \[61\] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit,
  Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin.
  Attention is all you need. In _Advances in Neural Information
  Processing Systems_, 2017.
- \[62\] Yuan Wang, Di Huang, Yaqi Zhang, Wanli Ouyang, Jile Jiao,
  Xuetao Feng, Yan Zhou, Pengfei Wan, Shixiang Tang, and Dan Xu.
  Motiongpt-2: A general-purpose motion-language model for motion
  generation and understanding. _arXiv_, 2024a.
- \[63\] Zhenzhi Wang, Jingbo Wang, Dahua Lin, and Bo Dai. Intercontrol:
  Generate human motion interactions by controlling every joint. _arXiv
  preprint arXiv:2311.15864_, 2023.
- \[64\] Zan Wang, Yixin Chen, Baoxiong Jia, Puhao Li, Jinlu Zhang,
  Jingze Zhang, Tengyu Liu, Yixin Zhu, Wei Liang, and Siyuan Huang. Move
  as you say, interact as you can: Language-guided human motion
  generation with scene affordance. In _Proceedings of the IEEE/CVF
  Conference on Computer Vision and Pattern Recognition (CVPR)_, 2024b.
- \[65\] Qi Wu, Yubo Zhao, Yifan Wang, Yu-Wing Tai, and Chi-Keung Tang.
  Motionllm: Multimodal motion-language learning with large language
  models, 2024a.
- \[66\] Yecheng Wu, Zhuoyang Zhang, Junyu Chen, Haotian Tang, Dacheng
  Li, Yunhao Fang, Ligeng Zhu, Enze Xie, Hongxu Yin, Li Yi, et al.
  Vila-u: a unified foundation model integrating visual understanding
  and generation. _arXiv preprint arXiv:2409.04429_, 2024b.
- \[67\] Yiming Xie, Varun Jampani, Lei Zhong, Deqing Sun, and Huaizu
  Jiang. Omnicontrol: Control any joint at any time for human motion
  generation. _arXiv preprint arXiv:2310.08580_, 2023.
- \[68\] Jinbo Xing, Menghan Xia, Yuechen Zhang, Xiaodong Cun, Jue Wang,
  and Tien-Tsin Wong. Codetalker: Speech-driven 3d facial animation with
  discrete motion prior. In _CVPR_, pages 12780–12790, 2023.
- \[69\] Sicheng Yang, Zhiyong Wu, Minglei Li, Zhensong Zhang, Lei Hao,
  Weihong Bao, Ming Cheng, and Long Xiao. Diffusestylegesture: Stylized
  audio-driven co-speech gesture generation with diffusion models. In
  _Proceedings of the Thirty-Second International Joint Conference on
  Artificial Intelligence, IJCAI-23_, pages 5860–5868. International
  Joint Conferences on Artificial Intelligence Organization, 2023.
- \[70\] Hongwei Yi, Hualin Liang, Yifei Liu, Qiong Cao, Yandong Wen,
  Timo Bolkart, Dacheng Tao, and Michael J Black. Generating holistic 3d
  human motion from speech. In _CVPR_, pages 469–480, 2023a.
- \[71\] Hongwei Yi, Hualin Liang, Yifei Liu, Qiong Cao, Yandong Wen,
  Timo Bolkart, Dacheng Tao, and Michael J. Black. Generating holistic
  3d human motion from speech. In _CVPR_, 2023b.
- \[72\] Youngwoo Yoon, Bok Cha, Joo-Haeng Lee, Minsu Jang, Jaeyeon Lee,
  Jaehong Kim, and Geehyuk Lee. Speech gesture generation from the
  trimodal context of text, audio, and speaker identity. _ACM
  Transactions on Graphics_, 39(6), 2020.
- \[73\] Ye Yuan, Jiaming Song, Umar Iqbal, Arash Vahdat, and Jan Kautz.
  Physdiff: Physics-guided human motion diffusion model. In _ICCV_,
  pages 16010–16021, 2023.
- \[74\] Dong Zhang, Shimin Li, Xin Zhang, Jun Zhan, Pengyu Wang, Yaqian
  Zhou, and Xipeng Qiu. Speechgpt: Empowering large language models with
  intrinsic cross-modal conversational abilities, 2023a.
- \[75\] Juze Zhang, Haimin Luo, Hongdi Yang, Xinru Xu, Qianyang Wu, Ye
  Shi, Jingyi Yu, Lan Xu, and Jingya Wang. Neuraldome: A neural modeling
  pipeline on multi-view human-object interactions. In _Proceedings of
  the IEEE/CVF Conference on Computer Vision and Pattern Recognition_,
  pages 8834–8845, 2023b.
- \[76\] Jianrong Zhang, Yangsong Zhang, Xiaodong Cun, Shaoli Huang,
  Yong Zhang, Hongwei Zhao, Hongtao Lu, and Xi Shen. T2m-gpt: Generating
  human motion from textual descriptions with discrete representations.
  In _CVPR_, 2023c.
- \[77\] Jianrong Zhang, Yangsong Zhang, Xiaodong Cun, Yong Zhang,
  Hongwei Zhao, Hongtao Lu, Xi Shen, and Ying Shan. Generating human
  motion from textual descriptions with discrete representations. In
  _CVPR_, pages 14730–14740, 2023d.
- \[78\] Juze Zhang, Jingyan Zhang, Zining Song, Zhanhe Shi, Chengfeng
  Zhao, Ye Shi, Jingyi Yu, Lan Xu, and Jingya Wang. Hoi-mˆ 3: Capture
  multiple humans and objects interaction within contextual environment.
  In _CVPR_, pages 516–526, 2024a.
- \[79\] Mingyuan Zhang, Zhongang Cai, Liang Pan, Fangzhou Hong, Xinying
  Guo, Lei Yang, and Ziwei Liu. Motiondiffuse: Text-driven human motion
  generation with diffusion model. _arXiv preprint
  arXiv:2208.15001_, 2022.
- \[80\] Mingyuan Zhang, Xinying Guo, Liang Pan, Zhongang Cai, Fangzhou
  Hong, Huirong Li, Lei Yang, and Ziwei Liu. Remodiffuse:
  Retrieval-augmented motion diffusion model. In _ICCV_, pages 364–373,
  2023e.
- \[81\] Mingyuan Zhang, Daisheng Jin, Chenyang Gu, Fangzhou Hong,
  Zhongang Cai, Jingfang Huang, Chongzhi Zhang, Xinying Guo, Lei Yang,
  Ying He, et al. Large motion model for unified multi-modal motion
  generation. _arXiv_, 2024b.
- \[82\] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q Weinberger,
  and Yoav Artzi. Bertscore: Evaluating text generation with bert.
  _arXiv preprint arXiv:1904.09675_, 2019.
- \[83\] Yaqi Zhang, Di Huang, Bin Liu, Shixiang Tang, Yan Lu, Lu Chen,
  Lei Bai, Qi Chu, Nenghai Yu, and Wanli Ouyang. Motiongpt: Finetuned
  llms are general-purpose motion generators. In _AAAI_, 2024c.
- \[84\] Zhikai Zhang, Yitang Li, Haofeng Huang, Mingxian Lin, and Li
  Yi. Freemotion: Mocap-free human motion synthesis with multimodal
  large language models. In _ECCV_, pages 403–421. Springer, 2025.
- \[85\] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang,
  Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong,
  Yifan Du, Chen Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, Ruiyang
  Ren, Yifan Li, Xinyu Tang, Zikang Liu, Peiyu Liu, Jian-Yun Nie, and
  Ji-Rong Wen. A survey of large language models, 2024.
- \[86\] Mohan Zhou, Yalong Bai, Wei Zhang, Ting Yao, Tiejun Zhao, and
  Tao Mei. Responsive listening head generation: A benchmark dataset and
  baseline. In _ECCV_, 2022.
- \[87\] Wenyang Zhou, Zhiyang Dou, Zeyu Cao, Zhouyingcheng Liao, Jingbo
  Wang, Wenjia Wang, Yuan Liu, Taku Komura, Wenping Wang, and Lingjie
  Liu. Emdm: Efficient motion diffusion model for fast and high-quality
  motion generation. In _ECCV_, pages 18–38. Springer, 2025.

|                                 |                                                                                                                                                                                                                                                                       |                                      |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| Task                            | Input                                                                                                                                                                                                                                                                 | Output                               |
| Audio-to-Full Motion            | Based on \[audio\], generate a synchronized movement sequence involving both face, hands, upper and lower body. Listen to \[audio\] and produce movements that involve both the upper and lower body in harmony.                                                      | \[face\]\[hands\] \[upper\]\[lower\] |
| Audio-to-Full Motion            | Based on \[audio\], generate a synchronized movement sequence involving both face, hands, upper and lower body. Listen to \[audio\] and produce movements that involve both the upper and lower body in harmony.                                                      | \[face\]\[hands\] \[upper\]\[lower\] |
| Audio&Transcript-to-Full Motion | Generate a set of movements for face, hand, upper, and lower body that correspond to the timestamped alignment in \[audio&transcript\] Using the precise timestamp match in \[audio&transcript\], generate corresponding face, hand, upper, and lower body movements. | \[face\]\[hands\] \[upper\]\[lower\] |
| Audio-to-Upper Body Motion      | Using \[audio\], produce upper body movements that capture the tone and energy. From \[audio\], create a series of gestures that use the upper body to reflect its flow.                                                                                              | \[upper\]                            |
| Audio-to-Lower Body Motion      | Interpret \[audio\] with lower body gestures that reflect its tempo. Create leg and foot movements that align with the intensity shifts in \[audio\].                                                                                                                 | \[lower\]                            |
| Audio-to-Hands Body Motion      | Develop a set of hand movements that respond dynamically to \[audio\]. Generate expressive hand gestures that reflect the cues in \[audio\].                                                                                                                          | \[hand\]                             |
| Audio-to-Face Body Motion       | Create expressions that correspond to the varying sentiments in \[audio\]. Listen to \[audio\] and generate a sequence of facial expressions that match its energy.                                                                                                   | \[face\]                             |
| Emotion-to-Motion               | Generate a movement sequence that fully embodies the emotion of \[emotion\] using the face, hands, upper body, and lower body. Express the emotion \[emotion\] through a series of actions involving the face, hands, upper, and lower body.”                         | \[face\]\[hands\] \[upper\]\[lower\] |
| Motion-to-Emotion               | What emotion is conveyed by the movements in the face, hands, upper body, and lower body within \[face\]\[hands\]\[upper\]\[lower\]? Examine the face, hand, upper, and lower body movements in \[face\]\[hands\] \[upper\]\[lower\] to interpret the emotional tone. | \[emotion\]                          |
| Text-to-Full Motion             | Give me gestures involving the face, hands, upper body, and lower body that correspond to \[caption\] Show me gestures involving the face, hands, upper body, and lower body that capture the essence of Input: \[caption\].                                          | \[face\]\[hands\] \[upper\]\[lower\] |
| Text-to-Upper Body Motion       | Create an upper body gesture that aligns with the sentiment of \[caption\]. Develop an upper body action sequence that mirrors the tone in \[caption\].                                                                                                               | \[upper\]                            |
| Text-to-Lower Body Motion       | Illustrate the message in \[caption\] with lower body motions. Translate \[caption\] into a lower body movement sequence.                                                                                                                                             | \[lower\]                            |
| Text-to-Lower Body Motion       | Describe the motion represented by \[upper\]\[lower\] using plain English. What does the \[upper\]\[lower\] communicate? Please describe it in words.                                                                                                                 | \[caption\]                          |

Table 4: Examples of instruction prompt templates during post-training.
For each task, we show two examples of the input prompts and the output
format.

![](arxiv-2412-10523--dabd69cd1dff.figures/figure-5.webp)

Figure 8: Qualitative examples for text-to-motion generation. Given a
text caption, we compare the 3D motion generated by our method with
those generated by state-of-the-art methods, including MDM \[59\],
T2M-GPT \[77\], and MotionGPT \[23\]. Our model produces smooth,
natural, and sometimes better motion in comparison with existing
methods, which do not model the audio modality.

## 7 Supplementary

In this supplementary material, we provide additional details about:

1.  1.  Supplementary video for qualitative examples (referenced in Sec. 1).
2.  2.  Additional details on post-training (referenced in Sec. 3.4).
3.  3.  Additional details on editable generation (referenced in Sec. 4.3).
4.  4.  Additional details on emotion prediction (referenced in Sec. 4.4).
5.  5.  Results for text-to-motion.
6.  6.  Additional implementation details.
7.  7.  Additional qualitative example of co-speech gesture generation.

### 7.1 Supplementary Video

We provide a supplemental video to illustrate our results. In the video,
we present: 1) an overview of our overall framework, 2) detailed
qualitative comparisons across four tasks: co-speech gesture generation,
editable gesture generation, text-to-motion generation, and emotion
understanding, and 3) examples of failure cases to inspire further
research. We recommend watching this video with your headphone, as video
results provide a more comprehensive understanding of our approach.

### 7.2 Additional Details on Post-training

Existing datasets primarily provide pair-wise motion data but lack
corresponding instructions. Following \[23\], we construct paired data
for downstream tasks such as co-speech gesture generation and
text-to-motion generation, equipping the model with
instruction-following capabilities. Building upon existing
datasets \[41, 43, 45, 50\], we develop an instructional multi-modal
dataset comprising several core tasks. Unlike previous work \[23\], our
approach explicitly distinguishes each body part by introducing specific
part-specific keywords. As illustrated in Tab. 4, each core task
includes dozens of carefully designed instruction prompts.

### 7.3 Additional Details on Editable Gesture Generation

As shown in Tab. 4, we prompt the model with part-specific keywords,
enabling it to generate any body part based on either audio or text
inputs. This approach allows us to easily edit specific body parts. In
this paper, we demonstrate this by prompting the model twice: once to
generate the upper body from audio and once to generate the lower body
from a text description. We anticipate that with further training on
larger datasets, the model will be able to simultaneously follow input
prompts from multiple sources.

### 7.4 Additional Details on Emotion Understanding

Since we perform instruction tuning during the post-training stage, the
model does not always guarantee precise single-emotion label
predictions. Instead of using a classification accuracy metric, we adopt
text embedding distance metrics to evaluate the similarity between the
predicted emotion and the ground truth labels. Specifically, we use
BLEU \[51\], ROUGE, CIDEr \[39\], and BERTScore \[82\] to assess the
semantic distances between the predicted and reference texts.

### 7.5 Results for Text-to-motion Generation

In the main paper, we focused on demonstrating our model’s capability in
co-speech gesture generation as well as editable gesture generation.
Another task that our model is naturally good at is text-to-motion
generation. To understand how good our model is at generating motion
from instructions, we investigate the quality of generated motion given
text descriptions.

We show some qualitative examples of our text-to-motion generation in
Fig. 8, where we also compare with existing work \[59, 77, 23\]. We can
see that our model produces smooth, natural, and sometimes better
motions in comparison with other generation methods. We encourage
watching the supplementary video to get a more comprehensive
understanding of our model’s text-following ability.

While our model shows strong text-to-motion generation on par or even
better than existing models, we observe that the common text-to-motion
metrics (e.g., FID \[16\]) are strongly coupled with the motion
representation that existing work adopts, i.e., HumanML3D \[16\]
(H3D-Format), because the VAEs are trained using that format. While the
H3D-Format focuses predominantly on skeletal movements, such as swinging
motions, it under-represents twisting rotations and other nuanced body
dynamics. In contrast, our method prioritizes expressive motion with a
compositional representation, capturing a broader range of movements.
Because these metrics are heavily entangled with specific motion
representations, we find them not suitable to evaluate our method. We
encourage readers to refer to the qualitative results in Fig. 8 and the
supplementary video for a more comprehensive understanding. Future work
is necessary to develop evaluation approaches that assess the quality of
generated motion independently of the motion representation used.

### 7.6 Additional Implementation Details

Model training. Our model employs a two-stage training process:
Generative Pre-training and Post-training. During the first stage of
modality alignment, we trained the full model using 8 $`\times`$ NVIDIA
H100-80GB GPUs and the AdamW optimizer with a learning rate of 2e-4.
Each configuration of the pre-trained model was trained until
convergence. For the post-training stage, we used 8 $`\times`$ NVIDIA
3090-24G GPUs with the AdamW optimizer and a learning rate of 1e-4. To
ensure fair comparisons in ablation studies, each configuration of the
post-trained model was trained for a fixed 350 epochs.

Global Translation Prediction. Benefiting from the compositional body
representation, our approach generates high-quality expressive motions,
particularly for gestures and emotion understanding. However, the
holistic motion is divided into several body parts for local frames, as
noted in \[43\]. To address this, we follow  \[43\] and train a VAE
module with a 4-layer TCN structure. This module takes the lower body as
input and estimates the global translations
$`T_{trans}\in\mathbb{R}^{T\times 3}`$.

### 7.7 Additional Qualitative Example of Co-speech Gesture Generation

To show the effectiveness of our model on co-speech gesture generation,
we provide one more qualitative example in Fig. 9. We can see that our
model generates gestures that are synchronized with the speech and
expressive of the emotion, outperforming two state-of-the-art methods.

![](arxiv-2412-10523--dabd69cd1dff.figures/figure-6.webp)

Figure 9: Additional qualitative example on co-speech gesture
generation. Given an input speech, we visualize the ground truth 3D
motion accompanying the audio, the motion generated by two baselines:
EMAGE \[43\], SynTalker \[8\], and our method. Our model generates more
diverse and expressive motion compared to existing methods, especially
when the speaker emphasizes on words such as “angered” and “upset”.
