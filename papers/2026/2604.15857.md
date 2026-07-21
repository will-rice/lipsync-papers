---
arxiv_id: "2604.15857"
title: "AHS: Adaptive Head Synthesis via Synthetic Data Augmentations"
authors:
  - Taewoong Kang
  - Hyojin Jang
  - Sohyun Jeong
  - Seunggi Moon
  - Gihwi Kim
  - Hoon Jin Jung
  - Jaegul choo
submitted: "2026-04-17"
categories:
  - cs.CV
arxiv_url: https://arxiv.org/abs/2604.15857
source: arxiv-html
converter: pandoc
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-21T00:10:00+00:00"
references_parsed: 0
arxiv_version: ""
---

# AHS: Adaptive Head Synthesis via Synthetic Data Augmentations

Taewoong Kang¹  Hyojin Jang¹¹¹footnotemark: 1  Sohyun Jeong¹¹¹footnotemark: 1  Seunggi Moon²\
 Gihwi Kim³  Hoon Jin Jung³  Jaegul Choo¹\
¹KAIST ² Korea University ³ FLIPTION\
{keh0t0, wkdgywlsrud, jsh0212, jchoo}@kaist.ac.kr Equal contribution

###### Abstract

Recent digital media advancements have created increasing demands for sophisticated portrait manipulation techniques, particularly head swapping, where one’s head is seamlessly integrated with another’s body. However, current approaches predominantly rely on face-centered cropped data with limited view angles, significantly restricting their real-world applicability. They struggle with diverse head expressions, varying hairstyles, and natural blending beyond facial regions. To address these limitations, we propose Adaptive Head Synthesis (AHS), which effectively handles full upper-body images with varied head poses and expressions. AHS incorporates a novel head reenacted synthetic data augmentation strategy to overcome self-supervised training constraints, enhancing generalization across diverse facial expressions and orientations without requiring paired training data. Comprehensive experiments demonstrate that AHS achieves superior performance in challenging real-world scenarios, producing visually coherent results that preserve identity and expression fidelity across various head orientations and hairstyles. Notably, AHS shows exceptional robustness in maintaining facial identity while drastic expression changes and faithfully preserving accessories while significant head pose variations.

![[Uncaptioned image]](https://arxiv.org/html/2604.15857v1/figures/teaser.png)

Figure 1: Head-swapped results comparison among the baselines. Our model outperforms on preserving identity, hairstyle and accessaries while reeancting target body image’s expression and head pose.

## 1 Introduction

Head swapping is a challenging task that seamlessly integrates a head of a source image with a body of a target image, while reenacting the head orientation and expression of the target image. Given its potential impact on industries such as fashion design, virtual character customization, and digital marketing, exploring this task holds considerable research value. Despite its potential, head swapping remains relatively underexplored due to its inherent challenges. One major challenge is the lack of ground truth data for head swapping. As a result, models only could rely on self-supervised training, which significantly weakens their generalization capabilities. Specifically, models trained solely on self-reconstruction often struggle to capture variations in facial expressions and head orientations, limiting their effectiveness in real-world applications. Another key challenge arises from the high variability in hair length and style, requiring the model to consider a broader spatial region. This makes head swapping more difficult than face swapping \[6, 17, 31\], a similar task that transfers the facial identity of a source to a target while preserving the target’s non-identity-related attributes, as it focuses exclusively on the facial region.

Existing head swapping approaches have attempted to address these challenges, but significant limitations still hinder their effectiveness in real-world applications. One approach restricts the editing region to the cropped face area to simplify the task by reducing spatial complexity \[40, 2, 20\]. However, this severely impacts practical applicability. Since head swapping inherently involves variations in hair shape, length, and overall head orientation, confining modifications to only the facial region prevents seamless integration. As a result, this approach falls short in applications that require full head synthesis. Another approach leverages few-shot training techniques \[50\] to reenact the head orientation from the target image. It often necessitates complex preprocessing, as it typically relies on video data to extract training samples. Additionally, it commonly consists of two separate models, one for reenactment and another for blending, further increasing computational complexity. Moreover, it is generally less effective than zero-shot methods, which need no prior data on specific individuals. Given these drawbacks, there is a growing need for more robust head swapping methods that can operate in a zero-shot setting using a single model while effectively handling variations in head orientation, hair structure, and expression without requiring extensive preprocessing or specialized training data. HID \[25\] tackles these issues and enables zero-shot head swapping. However, it still has difficulty capturing facial attributes such as expressions and relies solely on ControlNet \[58\]-OpenPose during inference to manage pose and head orientation, as its training phase lacks mechanisms for controlling these aspects. For a more natural and practical outcome, it is crucial to transfer the face ID, facial shape, skin tone, accessories, and hairstyle of the source image, while preserving the pose, expression, and head orientation of the target image, as shown in Fig. 2.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/definition3.png)

Figure 2: Problem definition of head swapping. The first row indicates the portion of the head from the source image that needs to be transferred, while the second row indicates the portion of the head in the target image that should be preserved.

Therefore, we propose Adaptive Head Synthesis (AHS), which designed to effectively handle diverse facial orientations, expressions, and hairstyles in challenging settings of full upper body images. To overcome the limitations of self-reconstruction training caused by the absence of ground-truth data, we introduce a synthetic data augmentation strategy using a state-of-the-art animatable head avatar model \[11\]. This augmentation enhances the zero-shot adaptability, making AHS a robust and practical solution for real-world head-swapping applications. Furthermore, we achieve precise control over expression, head orientation, and pose by simply merging two conditioning images, a densepose map \[19\] and a normal map.

Our main contributions are as follows:

- •
  We propose AHS, a novel approach that enables effective and high-quality head swapping with a single model on challenging datasets, while considering head orientation alignment and expression reenactment.
- •
  We present a synthetic data augmentation strategy using a head reenactment model, which mitigates the limitations of self-supervised training and enhances generalization capabilities across diverse facial expressions, head orientations, and hairstyles.
- •
  Through extensive experiments, we demonstrate that AHS achieves state-of-the-art head swapping performance in complex real-world scenarios.

## 2 Related Work

### 2.1 Head Swap

Although research on head swapping remains relatively underexplored, existing studies \[40, 20, 2, 53, 50, 18\] share a common limitation: they predominantly rely on face-centered cropped datasets, which primarily consist of front-facing views. This dataset constraint severely limits the diversity of head orientations and seamless head-body integration, which are crucial for real-world applications. More details for these works are provided in Sec. 6.

To overcome these dataset constraints, for example, in real-world cases where subjects have extremely long hair, recent work \[25\] leverages a real-world dataset and introduces a strategy to improve generalization by injecting hair and face ID information through text embeddings. However, this approach suffers from artifact generation and a decline in identity similarity, because it relies on embedding-level injection rather than feature-level injection. Additionally, it does not explicitly model facial expressions, limiting its effectiveness in capturing natural variations. These limitations highlight the need for a more robust head swapping approach that can generalize effectively to diverse head orientations, expressions, and hairstyles without being constrained by face-centered cropped datasets.

### 2.2 Diffusion-based Image Editing

Diffusion models \[46, 22, 51\] have achieved substantial advances in text-to-image synthesis \[26, 44, 45, 48\], drawing widespread interest in recent years. These developments have been propelled by the emergence of extensive and high-quality text-image datasets \[4, 49\], ongoing enhancements in foundational models \[5, 39\], improvements in conditioning encoders, and the introduction of sophisticated control mechanisms \[38, 34, 57, 58, 3\]. Recent research has increasingly focused on leveraging diffusion models for image editing under diverse conditions. Such methods include pose-guided generation \[24, 29\], reference-based editing  \[56, 7\], multi-view face synthesis  \[42\], and multi-conditional image manipulation  \[58, 30\], which incorporate depth and edge maps. In addition, diffusion-based techniques have been applied to various inpainting tasks using reference images, such as object inpainting \[56, 7\], hairstyle transformation \[12\], and virtual clothing synthesis \[28, 9, 60\]. Nevertheless, head inpainting poses distinct challenges compared to other inpainting tasks such as clothing synthesis. The wide range of hairstyles, facial orientations, and expressions leads to more complex inpainting regions, requiring precise control and making head manipulation particularly demanding. To bridge this gap, our work extends diffusion models to the head-swapping task, which involves transferring the head from a reference image onto a target body image. Our proposed approach effectively manages the complexities associated with head swapping while maintaining realistic and seamless integration.

## 3 Method

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/overall2.png)

Figure 3: Overview of training AHS. Our model encodes identity using dedicated Head and Face Encoders, while H-Net preserves fine-grained head details. To prevent reconstruction artifacts and improve robustness, the training process is enhanced with GAGAvatar, which generates augmented data with diverse head poses and expressions.

This section presents our proposed framework for effective head swapping and reenactment, which comprises a novel data augmentation strategy and a specialized network architecture. In Sec. 3.1, we introduce our model architecture, designed to preserve identity and accessories with high fidelity. Following this, in Sec. 3.2, we detail our data augmentation strategy, which relies on a synthetic dataset of randomly reenacted heads. Finally, we describe effective inference in Sec. 3.3 utilizing our trained model.

### 3.1 Model Architecture

Let $`I_{s}`$ and $`I_{t}`$ be the source and target images, respectively. Our goal is to generate an output image $`I_{o}`$ where the head from $`I_{s}`$ seamlessly replaces the head in $`I_{t}`$. The generated head must preserve the identity from $`I_{s}`$ while matching the pose and expression of $`I_{t}`$.

To achieve this alignment, we guide our model with $`I_{\text{normal}}`$. This is obtained by replacing the head region of the target’s dense pose map with a normal map extracted via the state-of-the-art head reconstruction model, EMOCA \[14\]. This simple additional input provides explicit geometric cues, enabling effective reenactment of the target’s head attributes. The model takes the following inputs:

```math
I_{o}=\Phi(\mathcal{E}(I_{t}),\mathcal{E}(I_{t}^{\mathcal{M}}),\mathcal{M},\mathcal{E}(I_{\text{normal}})),
```

where $`\mathcal{E}`$ represents a VAE encoder, $`\mathcal{M}`$ is the mask, $`I_{t}^{\mathcal{M}}`$ means masked $`I_{t}`$ and $`\Phi`$ denotes our full model.

To effectively integrate head identity, we employ both cross-attention and self-attention mechanisms within our primary U-Net, referred to as S-Net. For cross-attention, we leverage the face encoder and head encoder inspired by Photomaker \[35\] and IP-Adapter \[57\]. The face encoder extracts key-value matrices $`K_{f}\in\mathbb{R}^{N\times d}`$, $`V_{f}\in\mathbb{R}^{N\times d}`$ by fusing with text embeddings, while the head encoder computes $`K_{h}\in\mathbb{R}^{N\times d^{\prime}}`$, $`V_{h}\in\mathbb{R}^{N\times d^{\prime}}`$ from head embeddings $`h`$. The extracted information is incorporated into the model via the cross-attention layer:

```math
\texttt{Attention}(Q,K_{f},V_{f})+\texttt{Attention}(Q,K_{h},V_{h}).
```

This enables the model to capture high-level semantic features, ensuring identity preservation while allowing flexible pose adaptation. We further incorporate self-attention, following \[9\], to provide low-level features. Specifically, we extract key-value pairs $`K_{n}\in\mathbb{R}^{N\times d^{\prime\prime}}`$, $`V_{n}\in\mathbb{R}^{N\times d^{\prime\prime}}`$ from H-Net, the reference net, and concatenate them with those from S-Net. This allows the query to attend to both H-Net and S-Net features effectively referencing the source image features. By combining self-attention for low-level features with cross-attention for high-level semantic control, our model effectively synthesizes head-swapped images that are both perceptually realistic and preserve intricate details. Moreover, the face and head encoders accelerate model convergence and compensate for cases where H-Net is not explicitly trained, ensuring stable performance even without extensive fine-tuning.

### 3.2 Data Augmentation

While our model architecture excels at transferring reference features, it faces challenges in pose alignment and photorealistic inpainting when trained for the head swapping task in a self-supervised manner. For instance, in the case of in-the-wild images, the source and target images often exhibit significantly different head orientations and expressions, as they originate from different individuals. However, this alignment issue cannot be fully addressed within the constraints of self-supervised training. To improve robustness and performance across diverse scenarios, we incorporate a strategic data augmentation.

The primary challenge lies in the inability of the model to effectively capture both head orientation and facial expression information. To address this challenge, we devise a simple yet effective approach by strategically augmenting the training dataset. Specifically, we leverage the state-of-the-art head reenactment model, GAGAvatar \[11\]. By altering the head orientation and facial expression of randomly selected images while minimally compromising the original identity information, we enable our model to generalize more effectively across various real-world pose pairs. Through this augmentation, our model inherently learns head reenactment within a unified manner.

Additionally, to achieve photorealistic head swapping, the heterogeneous property among source and target’s head size and hairstyle must be solved. When $`I_{s}`$ and $`I_{t}`$ have significantly different head regions, directly placing the head of $`I_{s}`$ within the masked region of $`I_{t}`$ can result in unnatural artifacts, as shown in  Fig. 4. Therefore, our goal is to prevent the model from inferring the head size and hairstyle only from the target image’s mask contour. Specifically, we randomly replace the conventional segmentation-based head mask with a more adaptive masking strategy designed to facilitate seamless head integration. We apply various mask augmentation measures including dilation, widened bounding box creation, and merging with a random mask, as illustrated in Fig. 5, similar to \[31, 8\].

### 3.3 Inference

Our proposed AHS enables efficient inference by leveraging its head reenactment-based training regime. Simply providing the target body and source head images as input allows the model to generate a head-reenacted and swapped result, as illustrated in Fig. 6. However, due to the discrepancies between input for training and inference, certain techniques are incorporated to ensure optimal performance.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/artifacts_v2.png)

Figure 4: Examples of Copy-and-paste artifacts. These results are generated by the model that trained without applying our data augmentation methods, including head reenactment and masking. This copy-and-paste artifacts caused by not accounting for the pose and expression of the head in the target image.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/mask.png)

Figure 5: Mask augmentation strategy. Including dilation, widened bounding box creation, and merging with a random mask.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/inference4.png)

Figure 6: Inference overview. Our model takes source and target images and outputs head swapped results within an unified model.

#### Head parameter swapping.

During training, since $`I_{s}`$ and $`I_{t}`$ are images of the same person, the learning can be accomplished using only the head normal map of $`I_{t}`$. However, during inference, the model is required to process images of two different individuals. Therefore, the shape parameters of $`I_{s}`$ must be reflected in the head normal map of $`I_{t}`$. To achieve this, after obtaining the FLAME parameters of both $`I_{s}`$ and $`I_{t}`$ through EMOCA \[14\], we substitute the shape parameter of $`I_{s}`$ with the corresponding parameters of $`I_{t}`$ before generating the normal map.

```math
\text{FLAME}(\boldsymbol{\beta}_{s},\boldsymbol{\theta}_{t},\boldsymbol{\psi}_{t})\rightarrow(\textbf{V},\textbf{F}),
```

where FLAME \[33\] is a statistical 3D head model that outputs vertices V and faces F, given the head shape parameter $`\beta`$, pose parameter $`\theta`$, and facial expression parameter $`\psi`$. The head normal map is subsequently rendered based on the extracted geometry information.

#### Inference mask.

When $`I_{s}`$ and $`I_{t}`$ differ significantly, especially for hair length and head size, performing inpainting using only the head mask of $`I_{t}`$ can lead to unnatural artifacts. For instance, the head may be generated too small or the hair may appear truncated. To address this, we first perform inpainting by providing a wide bounding box that covers a larger area than the original head mask of $`I_{t}`$. We then mask the head and neck portions of the generated image, and merge them with the mask of $`I_{t}`$ before performing inpainting once again. This approach increases the degree of freedom in generation while preserving the details outside the head area with minimal degradation in quality.

## 4 Experiments

| Models                | CLIP-I (Head) $`\uparrow`$ | FID $`\downarrow`$ | FID (Crop) $`\downarrow`$ | ID sim $`\uparrow`$ | Head orientation $`\downarrow`$ | Expression $`\downarrow`$ |
| --------------------- | -------------------------- | ------------------ | ------------------------- | ------------------- | ------------------------------- | ------------------------- |
| REFace \[2\]          | 0.7859                     | 8.4491             | 24.31                     | 0.5239              | 5.57                            | 7.308                     |
| InstantID^(\*) \[54\] | 0.8223                     | 5.7882             | 11.43                     | 0.2829              | 7.52                            | 7.591                     |
| HID \[25\]            | 0.8577                     | 5.6306             | 6.83                      | 0.5555              | 11.51                           | 8.474                     |
| AHS (Ours)            | 0.9132                     | 5.7818             | 5.02                      | 0.6230              | 8.01                            | 6.204                     |

Table 1: Quantitative comparison. Best and second-best results are in bold and underlined, respectively. Our proposed method, AHS, outperforms existing methods in most metrics, excluding FID and head orientation.

To evaluate our method, we conduct experiments on the SHHQ \[16\] dataset. Following the experimental setup, we present quantitative and qualitative results with a user study to demonstrate state-of-the-art performance. Finally, we provide a comprehensive ablation study with analysis. Further details can be found in Sec. 7.

### 4.1 Experimental Setup

#### Implementation details.

To enhance the output quality, we adopt an alternative scheduler \[36\] and unfroze the S-Net. The H-Net remains frozen as its pretrained features are already effective, and unfreezing it would incur prohibitive memory and time costs. Similarly, we froze the face encoder to preserve its pretrained weights  \[35\] and unfroze the last layer the head encoder to enable residual detail enhancement from the input image. Training is implemented with data type casting to bfloat16 to enhance efficiency and is conducted on 4 H100 80GB GPUs over 70 epochs, using a batch size of 6 per GPU, which takes about 3 days.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/quali.png)

Figure 7: Qualitative comparison. The images in the Head column are combined with those in the Body column. The last four columns are the head-swapped results produced by each method. More results can be found in Sec. 10.

#### Baselines.

Due to the underexplored nature of the zero-shot head swapping task, there is a lack of established baselines for comparison. Among existing methods, HID \[25\] is a zero-shot head swapping approach specifically designed for upper body datasets, aligning most closely with our task. REFace \[2\], while not originally intended for head swapping, can also perform zero-shot head swapping. For a fair comparison, we utilize its weights trained for head swapping tasks. Due to the scarcity of high-performing, dedicated head-swapping baselines, we chose to compare our method against InstantID \[54\], a powerful and widely-used approach for identity-preserved generation. Although not originally designed for head swapping, incorporating IP-Adapter \[57\] and ControlNet \[58\] with its architecture makes it adaptable for this task. We achieve this adaptation by leveraging the SDXL Inpainting model \[41\] with Sapiens masks \[27\]. This setup allows the model to inpaint the head region to transfer identity, while concurrently using ControlNet to enforce the desired pose. Consequently, we compare our method against HID, REFace, and InstantID for comprehensive evaluation.

#### Evaluation.

For evaluation, we create test pairs by randomly selecting a source (head) image and a target (body) image from the dataset. We assess our method using a suite of quantitative metrics, following the protocol of our baseline HID \[25\], alongside a user study. The quantitative evaluation includes measuring the overall visual quality using the Fréchet Inception Distance (FID) \[21\]. We also assess more specific perceptual aspects with CLIP-I \[43\] similarity measured exclusively on the generated head region where the face and hair areas are segmented by SCHP \[32\] to isolate the quality. We further evaluate identity similarity with ArcFace \[15\], head orientation error with HopeNet \[47\], and expression similarity with FLAME \[33\]. To ensure a fair comparison against baselines that occasionally fail, the metrics are reported only on the common subset of samples where results are successfully generated across all methods. Consequently, scores for our more robust model may differ slightly between the main comparison and our ablation studies, where this filtering is not applied.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/userstudy_v2.png)\

Figure 8: Results of user study.

|                        |                            |                    |                     |                                 |                           |
| ---------------------- | -------------------------- | ------------------ | ------------------- | ------------------------------- | ------------------------- |
| Models                 | CLIP-I (Head) $`\uparrow`$ | FID $`\downarrow`$ | ID sim $`\uparrow`$ | Head orientation $`\downarrow`$ | Expression $`\downarrow`$ |
| w/o GAG Aug            | 0.7575                     | 10.94              | 0.8492              | 17.34                           | 6.8542                    |
| w/o Mask Aug           | 0.8637                     | 8.99               | 0.4098              | 7.27                            | 5.6719                    |
| w/o head encoder       | 0.8912                     | 9.29               | 0.5690              | 7.90                            | 8.8247                    |
| w/o face, head encoder | 0.9019                     | 9.66               | 0.6411              | 8.92                            | 8.4452                    |
| w/o decoupled CA       | 0.8050                     | 9.04               | 0.5124              | 8.27                            | 8.7458                    |
| AHS (Ours)             | 0.9122                     | 8.98               | 0.6237              | 8.72                            | 6.4273                    |

Table 2: Ablation study quantitative results. For each metric, the best and second-best performing results are denoted in bold and underlined formats, respectively.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/ablation10.png)

Figure 9: Ablation study qualitative results. Without the head and face encoders, identity preservation degrades under large head pose differences. Without augmentation, self-supervised learning causes copy-and-paste artifacts.

### 4.2 Results

#### Quantitative results.

As shown in Tab. 1, our proposed method, AHS, outperforms other methods across most metrics, achieving the best performance in identity similarity, FID (cropped), CLIP-I, and expression preservation. While methods like REFace \[2\] maintain head orientation well by directly inputting cropped faces and landmarks, they exhibit significant trade-offs, showing lower quality, identity similarity and expression. Similarly, InstantID \[54\] relies on a large ControlNet model, namely Identity Net, to inject head orientation information with landmark. In contrast, AHS achieves comparable orientation control simply by adding normal semantics to the input, demonstrating superior efficiency. Ultimately, although REFace scores well on full-image FID due to its crop-and-paste nature, our model, AHS, which generates the entire image holistically, not only achieves comparable results in those areas but also demonstrates superior overall performance.

#### Qualitative results.

Unlike baseline methods, AHS achieves high identity preservation while maintaining facial expressions. Baseline methods often suffer from a trade-off, where preserving expressions leads to identity degradation, or ensuring identity results in poor expression integration, as shown in Fig. 7 and Fig. 1. In contrast, AHS successfully maintains identity while accurately reflecting the expressions of $`I_{t}`$. Additionally, leveraging $`I_{normal}`$ input and mask augmentation training enables AHS to outperform other methods in cases where there are significant pose variations or hairstyle differences. While HID \[25\] demonstrates strong identity preservation under extreme conditions compared to existing methods, AHS achieves superior performance by more robustly retaining identity and hairstyle, faithfully transferring the target’s facial expressions, and robustly preserving accessories such as hats and sunglasses, even in highly challenging scenarios. We provide additional qualitative examples in Sec. 10 to further validate the robustness of the proposed approach.

#### User Study.

To validate the effectiveness of our method, AHS, we conduct a multiple-alternative forced-choice user study on 20 image pairs involving 19 participants. Each participant is asked to select the better result based on several key aspects: overall image quality, reenactment fidelity (pose, expression, and head orientation), hairstyle similarity and accessories preservation. As summarized in Fig. 8, AHS is consistently preferred across all criteria. It demonstrates a particularly significant lead in preserving identity features, as well as hairstyle and accessories.

### 4.3 Ablation Study

We perform an ablation study to analyze the impact of our key model architecture components (face encoder, head encoder, and decoupled CA) and data augmentation strategies (GAGAvatar \[11\] and mask). The results are presented in Table 2. First, we examine the model architecture. When both the face and head encoders are removed, the model’s performance relies heavily on the S-Net. While this leads to a high ID-sim score, the lack of detailed structural guidance yields a significant drop in FID and a failure to transfer expressions. As seen in Figure 9, this variant struggles to preserve identity, especially when handling large differences in head orientation and expression. Furthermore, removing the head encoder or the decoupled CA individually results in lower scores across most metrics, demonstrating that each component is necessary for optimal performance. Next, we evaluate the augmentation strategies. The model trained without the GAGAvatar augmentation achieves a high ID-sim score, but it learns a ”shortcut” by directly filling the masked area with conditional features. This approach results in prominent copy-and-paste artifacts, as shown in Figure 9, and indicates a failure to properly learn the reenactment task. Without mask augmentation, the model fails to learn background inpainting and generates images following the hair silhouette in the source image. These results reveal various trade-offs within the ablated models. However, they also validate that our final model achieves consistently superior performance across all metrics. This confirms that every component, the dual encoders for comprehensive guidance and our augmentation strategy for effective learning, is indispensable.

## 5 Conclusion

In this paper, we propose a novel head swapping approach, AHS, which effectively handles diverse head orientations, expressions, and hairstyles. AHS leverages a synthetic data augmentation strategy and a comprehensive conditioning approach using both cross- and self-attention. Experimental results demonstrate that AHS outperforms existing methods in identity preservation, expression transfer, and visual quality. However, head reenactment data augmentation using GAGAvatar \[11\] alone is insufficient to handle lighting variations. To address this, applying the same data augmentation strategy during the training using relighting models such as IC-Light \[59\] mitigates sensitivity to lighting changes. Detailed experiments are shown in Sec. 8.3. Despite these improvements, some limitations still remain, particularly in edge cases involving extreme facial structure differences or severe occlusions. These scenarios may lead to visual artifacts as the model struggles with geometric mismatches or missing information. Therefore, future work will focus on improving the robustness of the model for broader real-world applications.

## Acknowledgments

This work was supported by Institute for Information & communications Technology Planning & Evaluation(IITP) grant funded by the Korea government(MSIT) (RS-2019-II190075, Artificial Intelligence Graduate School Program(KAIST)) and the National Research Foundation of Korea(NRF) grant funded by the Korea government(MSIT) (No. RS-2025-00555621).

## References

- \[1\] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al. (2023) Gpt-4 technical report. arXiv preprint arXiv:2303.08774. Cited by: §7.1.
- \[2\] S. Baliah, Q. Lin, S. Liao, X. Liang, and M. H. Khan (2024) Realistic and efficient face swapping: a unified approach with diffusion models. arXiv preprint arXiv:2409.07269. Cited by: §1, §2.1, §4.1, §4.2, Table 1, §6.1, §8.1.
- \[3\] T. Brooks, A. Holynski, and A. A. Efros (2023) Instructpix2pix: learning to follow image editing instructions. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 18392–18402. Cited by: §2.2.
- \[4\] S. Changpinyo, P. Sharma, N. Ding, and R. Soricut (2021) Conceptual 12m: pushing web-scale image-text pre-training to recognize long-tail visual concepts. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 3558–3568. Cited by: §2.2.
- \[5\] J. Chen, J. Yu, C. Ge, L. Yao, E. Xie, Y. Wu, Z. Wang, J. Kwok, P. Luo, H. Lu, et al. (2023) Pixart-$`\alpha`$: fast training of diffusion transformer for photorealistic text-to-image synthesis. arXiv preprint arXiv:2310.00426. Cited by: §2.2.
- \[6\] R. Chen, X. Chen, B. Ni, and Y. Ge (2020) Simswap: an efficient framework for high fidelity face swapping. In Proceedings of the 28th ACM international conference on multimedia, pp. 2003–2011. Cited by: §1.
- \[7\] X. Chen, L. Huang, Y. Liu, Y. Shen, D. Zhao, and H. Zhao (2024) Anydoor: zero-shot object-level image customization. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 6593–6602. Cited by: §2.2.
- \[8\] S. Choi, S. Park, M. Lee, and J. Choo (2021) Viton-hd: high-resolution virtual try-on via misalignment-aware normalization. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 14131–14140. Cited by: §3.2.
- \[9\] Y. Choi, S. Kwak, K. Lee, H. Choi, and J. Shin (2024) Improving diffusion models for authentic virtual try-on in the wild. In European Conference on Computer Vision, pp. 206–235. Cited by: §2.2, §3.1.
- \[10\] F. Chollet (2017) Xception: deep learning with depthwise separable convolutions. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 1251–1258. Cited by: §7.
- \[11\] X. Chu and T. Harada (2025) Generalizable and animatable gaussian head avatar. Advances in Neural Information Processing Systems 37, pp. 57642–57670. Cited by: §1, §3.2, §4.3, §5, §7.3, §7.
- \[12\] C. Chung, S. Park, J. Kim, and J. Choo (2024) What to preserve and what to transfer: faithful, identity-preserving diffusion-based hairstyle transfer. arXiv preprint arXiv:2408.16450. Cited by: §2.2.
- \[13\] G. Comanici, E. Bieber, M. Schaekermann, I. Pasupat, N. Sachdeva, I. Dhillon, M. Blistein, O. Ram, D. Zhang, E. Rosen, et al. (2025) Gemini 2.5: pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. Cited by: Figure 11, §8.1.
- \[14\] R. Daněček, M. J. Black, and T. Bolkart (2022) Emoca: emotion driven monocular face capture and animation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 20311–20322. Cited by: §3.1, §3.3.
- \[15\] J. Deng, J. Guo, N. Xue, and S. Zafeiriou (2019) Arcface: additive angular margin loss for deep face recognition. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 4690–4699. Cited by: §4.1.
- \[16\] J. Fu, S. Li, Y. Jiang, K. Lin, C. Qian, C. Loy, W. Wu, and Z. Liu (2022) StyleGAN-human: a data-centric odyssey of human generation. arXiv preprint arXiv:2204.11823. Cited by: §4, §7.1, §7.
- \[17\] G. Gao, H. Huang, C. Fu, Z. Li, and R. He (2021) Information bottleneck disentanglement for identity swapping. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 3404–3413. Cited by: §1.
- \[18\] A. Groshev, A. Iashchenko, P. Paramonov, D. Dimitrov, and A. Kuznetsov (2025) GHOST 2.0: generative high-fidelity one shot transfer of heads. arXiv preprint arXiv:2502.18417. Cited by: §2.1, §6.1, §8.1.
- \[19\] R. A. Güler, N. Neverova, and I. Kokkinos (2018) Densepose: dense human pose estimation in the wild. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 7297–7306. Cited by: §1.
- \[20\] Y. Han, J. Zhang, J. Zhu, X. Li, Y. Ge, W. Li, C. Wang, Y. Liu, X. Liu, and Y. Tai (2023) A generalist facex via learning unified facial representation. arXiv preprint arXiv:2401.00551. Cited by: §1, §2.1, §6.1.
- \[21\] M. Heusel, H. Ramsauer, T. Unterthiner, B. Nessler, and S. Hochreiter (2017) GANs trained by a two time-scale update rule converge to a local nash equilibrium. In Advances in Neural Information Processing Systems, I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett (Eds.), Vol. 30, pp. . External Links: [Link](https://proceedings.neurips.cc/paper_files/paper/2017/file/8a1d694707eb0fefe65871369074926d-Paper.pdf) Cited by: §4.1.
- \[22\] J. Ho, A. Jain, and P. Abbeel (2020) Denoising diffusion probabilistic models. Advances in neural information processing systems 33, pp. 6840–6851. Cited by: §2.2.
- \[23\] J. Ho and T. Salimans (2022) Classifier-free diffusion guidance. arXiv preprint arXiv:2207.12598. Cited by: §7.
- \[24\] L. Hu (2024) Animate anyone: consistent and controllable image-to-video synthesis for character animation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 8153–8163. Cited by: §2.2.
- \[25\] T. Kang, S. Jeong, H. Jang, and J. Choo (2025-06) Zero-shot head swapping in real-world scenarios. In Proceedings of the Computer Vision and Pattern Recognition Conference (CVPR), pp. 10805–10814. Cited by: §1, §2.1, §4.1, §4.1, §4.2, Table 1, §7.1, §7.
- \[26\] B. Kawar, S. Zada, O. Lang, O. Tov, H. Chang, T. Dekel, I. Mosseri, and M. Irani (2023) Imagic: text-based real image editing with diffusion models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 6007–6017. Cited by: §2.2.
- \[27\] R. Khirodkar, T. Bagautdinov, J. Martinez, S. Zhaoen, A. James, P. Selednik, S. Anderson, and S. Saito (2024) Sapiens: foundation for human vision models. In European Conference on Computer Vision, pp. 206–228. Cited by: §4.1.
- \[28\] J. Kim, G. Gu, M. Park, S. Park, and J. Choo (2024) Stableviton: learning semantic correspondence with latent diffusion model for virtual try-on. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 8176–8185. Cited by: §2.2.
- \[29\] J. Kim, M. Kim, J. Lee, and J. Choo (2024) Tcan: animating human images with temporally consistent pose guidance using diffusion models. In European Conference on Computer Vision, pp. 326–342. Cited by: §2.2.
- \[30\] K. Kim, S. Park, J. Lee, and J. Choo (2023) Reference-based image composition with sketch via structure-aware diffusion model. arXiv preprint arXiv:2304.09748. Cited by: §2.2.
- \[31\] J. Lee, J. Hyung, S. Jung, and J. Choo (2024) Selfswapper: self-supervised face swapping via shape agnostic masked autoencoder. In European Conference on Computer Vision, pp. 383–400. Cited by: §1, §3.2.
- \[32\] P. Li, Y. Xu, Y. Wei, and Y. Yang (2019) Self-correction for human parsing. External Links: 1910.09777, [Link](https://arxiv.org/abs/1910.09777) Cited by: §4.1.
- \[33\] T. Li, T. Bolkart, M. J. Black, H. Li, and J. Romero (2017) Learning a model of facial shape and expression from 4d scans.. ACM Trans. Graph. 36 (6), pp. 194–1. Cited by: §3.3, §4.1.
- \[34\] Y. Li, H. Liu, Q. Wu, F. Mu, J. Yang, J. Gao, C. Li, and Y. J. Lee (2023) Gligen: open-set grounded text-to-image generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 22511–22521. Cited by: §2.2.
- \[35\] Z. Li, M. Cao, X. Wang, Z. Qi, M. Cheng, and Y. Shan (2024) Photomaker: customizing realistic human photos via stacked id embedding. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 8640–8650. Cited by: §3.1, §4.1, §7.
- \[36\] S. Lin, B. Liu, J. Li, and X. Yang (2024) Common diffusion noise schedules and sample steps are flawed. In Proceedings of the IEEE/CVF winter conference on applications of computer vision, pp. 5404–5411. Cited by: §4.1.
- \[37\] I. Loshchilov and F. Hutter (2019) Decoupled weight decay regularization. In International Conference on Learning Representations, External Links: [Link](https://openreview.net/forum?id=Bkg6RiCqY7) Cited by: §7.
- \[38\] C. Mou, X. Wang, L. Xie, Y. Wu, J. Zhang, Z. Qi, and Y. Shan (2024) T2i-adapter: learning adapters to dig out more controllable ability for text-to-image diffusion models. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 38, pp. 4296–4304. Cited by: §2.2.
- \[39\] W. Peebles and S. Xie (2023) Scalable diffusion models with transformers. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 4195–4205. Cited by: §2.2.
- \[40\] I. Perov, D. Gao, N. Chervoniy, K. Liu, S. Marangonda, C. Umé, Dpfks, C. S. Facenheim, L. RP, J. Jiang, S. Zhang, P. Wu, B. Zhou, and W. Zhang (2021) DeepFaceLab: integrated, flexible and extensible face-swapping framework. External Links: 2005.05535, [Link](https://arxiv.org/abs/2005.05535) Cited by: §1, §2.1, §6.1.
- \[41\] D. Podell, Z. English, K. Lacey, A. Blattmann, T. Dockhorn, J. Müller, J. Penna, and R. Rombach (2023) Sdxl: improving latent diffusion models for high-resolution image synthesis. arXiv preprint arXiv:2307.01952. Cited by: §4.1, §7.
- \[42\] M. Prinzler, E. Zakharov, V. Sklyarova, B. Kabadayi, and J. Thies (2024) Joker: conditional 3d head synthesis with extreme facial expressions. arXiv preprint arXiv:2410.16395. Cited by: §2.2.
- \[43\] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. (2021) Learning transferable visual models from natural language supervision. In International conference on machine learning, pp. 8748–8763. Cited by: §4.1.
- \[44\] A. Ramesh, P. Dhariwal, A. Nichol, C. Chu, and M. Chen (2022) Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:2204.06125 1 (2), pp. 3. Cited by: §2.2.
- \[45\] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer (2022) High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 10684–10695. Cited by: §2.2.
- \[46\] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer (2022) High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 10684–10695. Cited by: §2.2.
- \[47\] N. Ruiz, E. Chong, and J. M. Rehg (2018-06) Fine-grained head pose estimation without keypoints. In The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops, Cited by: §4.1.
- \[48\] C. Saharia, W. Chan, S. Saxena, L. Li, J. Whang, E. L. Denton, K. Ghasemipour, R. Gontijo Lopes, B. Karagol Ayan, T. Salimans, et al. (2022) Photorealistic text-to-image diffusion models with deep language understanding. Advances in neural information processing systems 35, pp. 36479–36494. Cited by: §2.2.
- \[49\] C. Schuhmann, R. Beaumont, R. Vencu, C. Gordon, R. Wightman, M. Cherti, T. Coombes, A. Katta, C. Mullis, M. Wortsman, et al. (2022) Laion-5b: an open large-scale dataset for training next generation image-text models. Advances in Neural Information Processing Systems 35, pp. 25278–25294. Cited by: §2.2.
- \[50\] C. Shu, H. Wu, H. Zhou, J. Liu, Z. Hong, C. Ding, J. Han, J. Liu, E. Ding, and J. Wang (2022) Few-shot head swapping in the wild. External Links: 2204.13100, [Link](https://arxiv.org/abs/2204.13100) Cited by: §1, §2.1, §6.1, Figure 11, §8.1.
- \[51\] J. Song, C. Meng, and S. Ermon (2020) Denoising diffusion implicit models. arXiv preprint arXiv:2010.02502. Cited by: §2.2.
- \[52\] Stability AI and Hugging Face (2023) Stable Diffusion XL 1.0 Inpainting 0.1. Hugging Face. Note: [https://huggingface.co/diffusers/stable-diffusion-xl-1.0-inpainting-0.1](https://huggingface.co/diffusers/stable-diffusion-xl-1.0-inpainting-0.1)Accessed: 2025-07-28 Cited by: §7.
- \[53\] Q. Wang, L. Liu, M. Hua, P. Zhu, W. Zuo, Q. Hu, H. Lu, and B. Cao (2023) HS-diffusion: semantic-mixing diffusion for head swapping. External Links: 2212.06458, [Link](https://arxiv.org/abs/2212.06458) Cited by: §2.1, §6.1.
- \[54\] Q. Wang, X. Bai, H. Wang, Z. Qin, A. Chen, H. Li, X. Tang, and Y. Hu (2024) Instantid: zero-shot identity-preserving generation in seconds. arXiv preprint arXiv:2401.07519. Cited by: §4.1, §4.2, Table 1.
- \[55\] C. Wu, J. Li, J. Zhou, J. Lin, K. Gao, K. Yan, S. Yin, S. Bai, X. Xu, Y. Chen, Y. Chen, Z. Tang, Z. Zhang, Z. Wang, A. Yang, B. Yu, C. Cheng, D. Liu, D. Li, H. Zhang, H. Meng, H. Wei, J. Ni, K. Chen, K. Cao, L. Peng, L. Qu, M. Wu, P. Wang, S. Yu, T. Wen, W. Feng, X. Xu, Y. Wang, Y. Zhang, Y. Zhu, Y. Wu, Y. Cai, and Z. Liu (2025) Qwen-image technical report. External Links: 2508.02324, [Link](https://arxiv.org/abs/2508.02324) Cited by: Figure 11, §8.1.
- \[56\] B. Yang, S. Gu, B. Zhang, T. Zhang, X. Chen, X. Sun, D. Chen, and F. Wen (2023) Paint by example: exemplar-based image editing with diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 18381–18391. Cited by: §2.2.
- \[57\] H. Ye, J. Zhang, S. Liu, X. Han, and W. Yang (2023) Ip-adapter: text compatible image prompt adapter for text-to-image diffusion models. arXiv preprint arXiv:2308.06721. Cited by: §2.2, §3.1, §4.1, §7.
- \[58\] L. Zhang, A. Rao, and M. Agrawala (2023) Adding conditional control to text-to-image diffusion models. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 3836–3847. Cited by: §1, §2.2, §4.1.
- \[59\] L. Zhang, A. Rao, and M. Agrawala (2025) Scaling in-the-wild training for diffusion-based illumination harmonization and editing by imposing consistent light transport. In The Thirteenth International Conference on Learning Representations, Cited by: §5, §8.3.
- \[60\] L. Zhu, D. Yang, T. Zhu, F. Reda, W. Chan, C. Saharia, M. Norouzi, and I. Kemelmacher-Shlizerman (2023) Tryondiffusion: a tale of two unets. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 4606–4615. Cited by: §2.2.

## 6 Additional Related Work

### 6.1 Head Swap

Many existing methods, such as those proposed in \[40, 20, 2\], optimize their approaches based on these cropped datasets, leading to inherent limitations in handling cases where the full head or surrounding region should be harmonized with the body. Consequently, these methods struggle with occlusions, head orientations beyond a narrow frontal distribution, and varying hair structures. While FaceX \[20\] and REFace \[2\] leverage diffusion models for head swapping, they still rely on face-centered training data, inheriting the same dataset-induced weaknesses. HSDiffusion \[53\], although diffusion-based, assumes a simple alignment mechanism where the center points of the head and body images are matched before compositing. However, without explicit modeling of head orientation differences, this approach often results in unnatural compositions when the source and target images have misaligned orientations. In contrast, HeSer \[50\] attempts to address these limitations by incorporating more varied head orientations. However, it operates under a few-shot learning paradigm, making it less flexible and scalable compared to zero-shot approaches. Additionally, the recent method GHOST 2.0 \[18\] adopts HeSer’s blending technique, requiring precise image alignment similar to HeSer. This introduces more complex data preprocessing steps. Furthermore, due to dataset limitations, it struggles to handle cases where the subject has extremely long hair.

## 7 Implementation Details

Our model is composed of three key components: the H-Net, which utilizes an SDXL inpainting model \[52\]; the S-Net, which employs the UNet from the original SDXL \[41\]; and a pretrained IP-Adapter \[57\] and a pretrained face encoder from PhotoMaker \[35\]. We train our model on the SHHQ dataset \[16\], adopting the data handling procedures from HID \[25\] with modified captions as detailed in Sec. 7.1. For data augmentation, we apply GAGAvatar \[11\] to 70% of the images. The corresponding masks are augmented through dilation (with a 90% probability), concatenation (50%), and conversion to bounding boxes (50%). The model is trained for 70 epochs using the AdamW optimizer \[37\] with a learning rate of $`1\times 10^{-5}`$ and a batch size of 6 per GPU. For reproducibility, we fix the random seed to 42 for both training and inference. During inference, we use a classifier-free guidance (CFG) \[23\] scale of 2.0 with 30 denoising steps and generate images at a resolution of $`1024\times 1024`$. In addition, for simplicity and efficiency, we employ the DeepXception model \[10\] to generate the segmentation mask during inference.

### 7.1 Datasets

We leverage the SHHQ dataset \[16\] following the approach in HID \[25\], but modify the captions. By replacing the original text embedding of ’hairstyle’ with a fused embedding from the hair image and text ’hairstyle’, HID eliminates the need for hairstyle descriptions in the prompt.Instead, we generate image captions about the hairstyle using the multi-modal large language model, GPT-4o \[1\] and add the generated captions to each original caption used in HID after removing ”with hairstyle”. To explicitly indicate the hair region, we provide both the input image and the cropped hair portion of the input image to the model.

### 7.2 Loss

To train our model, we use a composite loss function that balances overall image fidelity with accuracy in the specific head region. Our final loss, $`\mathcal{L}_{\text{total}}`$, is formulated as a weighted sum of two Mean Squared Error terms:

```math
\mathcal{L}_{\text{total}}=\lambda_{1}\mathcal{L}_{\text{global}}+\lambda_{2}\mathcal{L}_{\text{head}}
```

Here, $`\mathcal{L}_{\text{global}}`$ is the standard MSE loss between the prediction and the ground truth over the entire image. $`\mathcal{L}_{\text{head}}`$ is an MSE loss computed exclusively on the head region, isolated using a mask $`M`$. For all experiments, we set the balancing hyperparameters $`\lambda_{1}`$ and $`\lambda_{2}`$ to 1.0.

### 7.3 GAGAvatar Augmentation

For GAGAvatar \[11\] augmentation, we employ a balanced sampling strategy to ensure robustness. Head pose differences are distributed as $`5^{\circ}`$ (37%), $`5\text{--}10^{\circ}`$ (31%), and $`>15^{\circ}`$ (32%). For expression variations, we sample across a wide range of $`[-0.52,0.99]`$, achieving a mean cosine similarity of $`0.67`$ ($`\sigma=0.18`$). This diverse distribution allows the model to generalize across various motion scales. Our pipeline is fully automatic and does not require manual alignment between the source and target. Since the model generates the head within the target bounding box while centering the head using a normal map, it remains robust to large pose disparities.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/sup_additional_baselines.png)

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/sup_additional_abl_qual.png)

|                        |                           |                    |                          |                    |                                |                           |
| ---------------------- | ------------------------- | ------------------ | ------------------------ | ------------------ | ------------------------------ | ------------------------- |
| Method                 | CLIP-I(Head) $`\uparrow`$ | FID $`\downarrow`$ | FID(Crop) $`\downarrow`$ | ID sim$`\uparrow`$ | Head orientation$`\downarrow`$ | Expression $`\downarrow`$ |
| Ghost 2.0              | 0.8487                    | 7.968              | 19.749                   | 0.483              | 4.831                          | 10.626                    |
| HeSer \[50\]           | 0.8507                    | 6.444              | 15.221                   | 0.503              | 8.734                          | 11.022                    |
| Nano Banana \[13\]     | 0.8634                    | 4.241              | 2.809                    | 0.474              | 10.725                         | 7.449                     |
| Qwen-Image-Edit \[55\] | 0.8789                    | 4.377              | 4.422                    | 0.536              | 15.504                         | 7.522                     |
| Ours                   | 0.9139                    | 9.613              | 6.719                    | 0.625              | 8.427                          | 6.887                     |
| Ours w/o normal        | 0.9238                    | 10.055             | 5.944                    | 0.729              | 17.472                         | 10.799                    |
| Ours stage1            | 0.9157                    | 9.073              | 6.221                    | 0.631              | 9.000                          | 6.761                     |

Table 3: Quantitative Results.

Figure 10: Qualitative comparison with additional baselines.

Figure 11: Qualitative results of additional ablation study.

## 8 Additional Experiments

### 8.1 Comparisons with Additional Baselines

We further compare our AHS with four additional baselines: Nano Banana \[13\], Qwen-Image-Edit \[55\], HeSer \[50\], and Ghost 2.0 \[18\]. As shown in Fig. 11 and Tab. 3, while Nano Banana and Qwen-Image-Edit prioritize consistency, they often produce images identical to the input or suffer from severe copy-and-paste artifacts, which paradoxically leads to a high FID score. Similar to REFace \[2\], both HeSer and Ghost 2.0 rely on a conventional face-swap paradigm based on a crop-and-align pipeline. This approach is inherently unsuitable for head swapping as it is unable to handle regions outside the fixed facial crop, such as long hair. As a result, all three methods suffer from prominent bounding box artifacts and degradation in structural completeness compared to our method.

### 8.2 Additional Ablation Study

As shown in Fig. 11 and Tab. 3, omitting surface normals degrades head orientation and expression accuracy, as they provide essential geometric guidance for motion-identity decoupling. Furthermore, while bounding-box-only inference lacks boundary constraints leading to background flickering and deformation.

### 8.3 Lighting Condition Augmentation

Regarding lighting variations and complex occlusions, we realize that GAGAvatar alone is insufficient to handle these factors. To address this, we apply a data augmentation strategy using relighting models such as IC-Light \[59\]. Specifically, during training, we further augment 70% of the images augmented by GAGAvatar by applying IC-Light. As qualitatively shown in Fig. 12, this approach mitigates sensitivity to lighting changes and further enhances overall lighting consistency.

### 8.4 Inference Mask

As detailed in Section 3.3, this section elaborates on our inference methodology. Generating realistic hair presents a unique challenge, as the target area requires significant creative flexibility. To accommodate this, we employ a two-step inference process. Initially, we perform inference using a simple bounding box as the mask. While this approach provides ample space for hair synthesis, its broad nature can lead to undesirable artifacts, such as the deformation of clothing or the background outside the primary head region. To address this, we refine the mask in a second step. First, we extract a precise head region mask from the intermediate output. We then create a new, more accurate mask by computing the union of this mask and a mask from the body image. This refined mask is used to perform a second round of inference. This strategy ensures that the inpainting process is precisely focused on the desired areas, preventing modifications to irrelevant regions. As illustrated in Figure 13, the intermediate result, while plausible, exhibits clothing distortion. In contrast, the final output is cleanly reconstructed because the refined mask correctly excludes the clothing area from the inpainting process.

## 9 Failure Cases

Despite robust normal estimation in profile views, Fig. 14, our method faces three main challenges: (1) identity preservation under extreme poses, (2) restoration of masked-out facial occlusions, and (3) maintaining consistent facial scales when aligning with the body geometry. These cases arise from the inherent difficulty of hallucinating out-of-distribution spatial and structural information.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/sup_ic_light.png)

Figure 12: Results of IC-light Augmentation.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/sup_inference_mask.png)

Figure 13: Inference mask results.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/sup_failure_case.png)

Figure 14: Failure Cases.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/sup_additional_qual_1.png)

Figure 15: Qualitative comparison. The images in the Head column are combined with those in the Body column. The last four columns are the head-swapped results produced by each method.

![Refer to caption](https://arxiv.org/html/2604.15857v1/figures/sup_additional_qual_2.png)

Figure 16: Qualitative comparison. The images in the Head column are combined with those in the Body column. The last four columns are the head-swapped results produced by each method.

## 10 Additional Qualitative Results

We provide additional qualitative results in Fig. 15 and Fig. 16 generated by our proposed approach.
