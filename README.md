# Awesome_Micro_Gesture [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This is the official repository of `Micro-Gesture Recognition: A Survey of Datasets, Methods, and Challenges`.

> **[Taorui Wang](https://scholar.google.com/citations?user=k1fJCkIAAAAJ&hl=zh-CN)**<sup>1,2\*</sup>, **Xun Lin**<sup>2,\*</sup>, [Zitong Yu](https://zitong-yu.github.io/yzt/)<sup>2,†</sup>, [Qilang Ye](https://rikeilong.github.io/)<sup>3,4</sup>, [Dan Guo](https://faculty.hfut.edu.cn/gd/en/index.htm)<sup>5</sup>, [Sergio Escalera](https://sergioescalera.com/)<sup>6</sup>, [Ghada Khoriba](https://nu.edu.eg/academic-staff/dr-ghada-khoriba)<sup>7</sup>, [Yong Xu](https://faculty.hitsz.edu.cn/xuyong)<sup>1,†</sup>  

> <sup>1</sup>Harbin Institute of Technology, Shenzhen, China; 
<sup>2</sup>Great Bay University, China; 
<sup>3</sup>Nankai University, China; 
<sup>4</sup>Zhongguancun Academy, China; 
<sup>5</sup>Hefei University of Technology, China; 
<sup>6</sup>Universitat de Barcelona and Computer Vision Center, Spain; 
<sup>7</sup>Center for Informatics Science (CIS), School of Information Technology and Computer Science, Nile University, Egypt.  
> (\*Equal Contribution, †Corresponding Authors)
<h5 align="center">  

 ****[Paper](https://www.mi-research.net/article/doi/10.1007/s11633-025-1629-x)**** | **[ArXiv](https://ArXiv.org/)** | **[Github Page](https://github.com/timwang2001/Awesome_Micro_Gesture)**

</h5>

![Comparison of Gestures and Micro-Gestures](image/comparison.png)

## 📢 News

> [!WARNING]
> **2026-04-21 · Correction on Table 1**
>
> We identified a typo in the **MA-52** entry of **Table 1**.
> The correct number of samples is **22,422**, not **3,712**.
>
> This issue has now been corrected. We apologize for the mistake.
> Please refer to the official [MA-52 dataset](https://huggingface.co/datasets/kunli-cs/MA-52) for the source information.

> [!TIP]
> **2026-04-07 · Congratulations!**
>
> Our survey has been accepted by *Machine Intelligence Research*
> (**Impact Factor: 8.7, JCR Q1**).
>
> Congratulations to all collaborators!

> [!NOTE]
> **2025-07-23 · Repository Released**
>
> We released our survey,
> **_Micro-Gesture Recognition: A Survey of Datasets, Methods, and Challenges_**.
>
> This repository serves as a living companion to the paper and continuously
> organizes datasets, methods, and related resources for the community.
>
> If you notice any missing work or incorrect entry, please feel free to open
> an issue or contact us.


## Timeline of MGR Method Evolution
This timeline highlights how micro-gesture recognition has evolved, from early dataset creation to today's multimodal and MLLM-driven methods, and offers a quick view of the field's growth trajectory.
![Micro Gesture Trend](image/MGs_trend.png)

## 💎Datasets constructed for MGR
This section summarizes publicly available datasets for micro-gesture recognition and related affective understanding tasks. We list release time, source institute, publication venue, and available project links to support quick comparison and dataset selection.

| Date         | Institute | Paper                                                                                                                                                                                   | Publication | Others |
|----------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|--------|
| 2026/03 | UAEU | [MA-Bench: Towards Fine-grained Micro-Action Understanding](https://arxiv.org/pdf/2603.26586)| CVPR | - |
| 2026/02 | Univ. of Oulu | [iMiGUE-Speech: A Spontaneous Speech Dataset for Affective Analysis](https://arxiv.org/abs/2602.21464) | Speech Prosody | - |
| 2025/04  | LUT             | [DEEMO: De-identity Multimodal Emotion Recognition and Reasoning](https://ArXiv.org/pdf/2504.19549)                                                        | ArXiv       | -      |
| 2024/05 | LUT          | [EALD-MLLM: Emotion Analysis in Long-sequential and De-identity videos with Multi-modal Large Language Model](https://ArXiv.org/abs/2405.00574)                            | ArXiv  | -      |
| 2024/03 | HFUT      | [Benchmarking Micro-action Recognition: Dataset, Methods, and Applications](https://ArXiv.org/abs/2403.05234)                 | TCSVT       | -      |
| 2023/02 | Univ. of Oulu    | [SMG: A Micro-gesture Dataset Towards Spontaneous Body Gestures for Emotional Stress State Analysis](https://link.springer.com/article/10.1007/s11263/023/01761-6)                       | IJCV        | [Github](https://github.com/mikecheninoulu/SMG) |
| 2021/07 | TJU             | [iMiGUE: An Identity-free Video Dataset for Micro-Gesture Understanding and Emotion Analysis](https://ArXiv.org/abs/2107.00285)                                                    | CVPR       | [Github](https://github.com/linuxsino/iMiGUE) |
| 2019/05 | Univ. of Oulu    | [Analyze Spontaneous Gestures for Emotional Stress State Recognition:  A Micro-gesture Dataset and Analysis with Deep Learning](https://ieeexplore.ieee.org/abstract/document/8756513)         | FG          | -      |

## 🔨Methods
This section tracks representative MGR methods in chronological order, covering supervised, self-supervised/unsupervised, multimodal fusion, and efficiency-oriented designs. It is updated to reflect both peer-reviewed publications and influential preprints.

| Date    | Institute | Paper                                                                                                                                                                                   | Publication | Others |
|---------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|--------|
| 2026/04/17 | - | [Cross-Modal Generation: From Commodity WiFi to High-Fidelity mmWave and RFID Sensing](https://arxiv.org/abs/2604.16558)<br>Authors: Zhixiong Yang, Long Jing, Yao Li, Shuli Cheng, Guoxuan Chi, Chenyu Wen<br>arXiv: 2604.16558 | ArXiv | - |
| 2026/04/16 | - | [Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953)<br>Authors: Hassan Ali, Doreen Jirak, Luca Müller, Stefan Wermter<br>arXiv: 2604.14953 | ArXiv | - |
| 2026/04/15 | - | [EMGFlow: Robust and Efficient Surface Electromyography Synthesis via Flow Matching](https://arxiv.org/abs/2604.13685)<br>Authors: Boxuan Jiang, Chenyun Dai, Can Han<br>arXiv: 2604.13685 | ArXiv | - |
| 2026/04/13 | - | [From Multimodal Signals to Adaptive XR Experiences for De-escalation Training](https://arxiv.org/abs/2604.11570)<br>Authors: Birgit Nierula, Karam Tomotaki-Dawoud, Daniel Johannes Meyer, Iryna Ignatieva, Mina Mottahedin, Thomas Koch, Sebastian Bosse<br>arXiv: 2604.11570 | ArXiv | - |
| 2026/04/06 | - | [On Optimizing Electrode Configuration for Wrist-Worn sEMG-Based Thumb Gesture Recognition](https://arxiv.org/abs/2604.04623)<br>Authors: Wenjuan Zhong, Chenfei Ma, Kianoush Nazarpour<br>arXiv: 2604.04623 | ArXiv | - |
| 2026/04/01 | - | [Semantically Annotated Multimodal Dataset for RF Interpretation and Prediction](https://arxiv.org/abs/2604.01433)<br>Authors: Steve Blandino, Jelena Senic, Raied Caromi, Samuel Berweger, Anuraag Bodi, Camillo Gentile, Nada Golmie<br>arXiv: 2604.01433 | ArXiv | - |
| 2026/03/30 | - | [TinyGaze: Lightweight Gaze-Gesture Recognition on Commodity Mobile Devices](https://arxiv.org/abs/2604.09658)<br>Authors: Yaxiong Lei, Hyochan Cho, Fergus Buchanan, Shijing He, Xinya Gong, Yuheng Wang, Juan Ye<br>arXiv: 2604.09658 | ArXiv | - |
| 2026/03/27 | - | [SHANDS: A Multi-View Dataset and Benchmark for Surgical Hand-Gesture and Error Recognition Toward Medical Training](https://arxiv.org/abs/2603.26400)<br>Authors: Le Ma, Thiago Freitas dos Santos, Nadia Magnenat-Thalmann, Katarzyna Wac<br>arXiv: 2603.26400 | ArXiv | - |
| 2026/03 | INRIA | [B-MoE: A Body-Part-Aware Mixture-of-Experts "All Parts Matter" Approach to Micro-Action Recognition](https://arxiv.org/abs/2603.24245) | ArXiv | - |
| 2026/03 | NUPT | [FG-SGL: Fine-Grained Semantic Guidance Learning via Motion Process Decomposition for Micro-Gesture Recognition](https://arxiv.org/abs/2603.16269) | ArXiv | - |
|2026/01| NUPT | [Adaptive Spatiotemporal Graph Network with Cross-Stream Interaction for Micro-Gesture Recognition](https://ieeexplore.ieee.org/abstract/document/11399839) | ICCECE | - |
|2025/10| LUT             | [MSF-Mamba: Motion-aware State Fusion Mamba for Efficient Micro-Gesture Recognition](https://arxiv.org/abs/2510.10478)                                                        | IEEE TMM       | -      |
|2025/07| NPU             | [Hybrid-supervised Hypergraph-enhanced Transformer for Micro-gesture Based Emotion Recognition](https://ArXiv.org/pdf/2507.14867)                                                        | ArXiv       | -      |
|2025/07| HFUT | [Online Micro-gesture Recognition Using Data Augmentation and Spatial-Temporal Attention](https://ArXiv.org/abs/2507.09512)| MiGA@IJCAI |-
|2025/06| Goertek          | [DCSNN: An Efficient and High-speed sEMG-based Transient-state Micro-gesture Recognition Method on Wearable Devices](https://dl.acm.org/doi/10.1145/3729494)                            | PACM IMWUT  | -      |
|2025/06|HFUT | [Towards Fine-Grained Emotion Understanding via Skeleton-Based Micro-Gesture Recognition](https://ArXiv.org/abs/2506.12848)|MiGA@IJCAI| [Github](https://github.com/EGO-False-Sleep/Miga25_track1)
|2025/06| Cyrion Labs      | [CLIP-MG: Guiding Semantic Attention with Skeletal Pose Features and RGB Data for Micro-Gesture Recognition on the iMiGUE Dataset](https://www.ArXiv.org/pdf/2506.16385)                 | ArXiv       | -      |
|2025/05| LUT | [Micro-gesture recognition using Mamba](https://lutpub.lut.fi/handle/10024/170090) | ArXiv | - 
|2025/02| HFUT              | [Prototypical Calibrating Ambiguous Samples for Micro-Action Recognition](https://ojs.aaai.org/index.php/AAAI/article/view/32509)                                                                    | AAAI       | [Github](https://github.com/kunli-cs/pcan) |
|2025/02| LUT              | [Identity-free Artificial Emotional Intelligence via Micro-Gesture Understanding](https://ArXiv.org/pdf/2405.13206)                                                                    | ArXiv       | [Github](https://github.com/ErichG/MG-based-Emotion-Understanding) |
|2025/01| UCL              | [MM-Gesture: Towards Precise Micro-Gesture Recognition through Multimodal Fusion](https://ArXiv.org/pdf/2507.08344)                                                                     | MiGA@IJCAI       | [Github](https://github.com/momiji-bit/MM-Gesture) |
|2024/08| HFUT | [Prototype Learning for Micro-gesture Classification](https://ArXiv.org/abs/2408.03097) | MiGA@IJCAI | - |
|2024/07| Univ. of Oulu    | [Naive Data Augmentation Might Be Toxic: Data-Prior Guided Self-Supervised Representation Learning for Micro-Gesture Recognition](https://ieeexplore.ieee.org/document/10581907)         | FG          | -      |
|2024/07| HFUT              | [Micro-gesture Online Recognition using Learnable Query Points](https://ArXiv.org/abs/2407.04490)                                    | MiGA@IJCAI       | -      |
|2024/05| LUT              | [Enhancing Micro Gesture Recognition for Emotion Understanding via Context-Aware Visual-Text Contrastive Learning](https://ArXiv.org/pdf/2405.01885)                                    | ArXiv       | -      |
|2024/01| BUAA             | [BeyondVision: An EMG-driven Micro Hand Gesture Recognition Based on Dynamic Segmentation](https://www.MiGA@IJCAI.org/proceedings/2024/668)                                                    | MiGA@IJCAI       | [Github](https://github.com/tyc333/NoBarriers) |
|2023/07|HFUT |[Joint Skeletal and Semantic Embedding Loss for Micro-gesture Classification](https://ArXiv.org/abs/2307.10624)|ArXiv|-|
|2023/02| Univ. of Oulu    | [SMG: A Micro-gesture Dataset Towards Spontaneous Body Gestures for Emotional Stress State Analysis](https://link.springer.com/article/10.1007/s11263/023/01761-6)                       | IJCV        | [Github](https://github.com/mikecheninoulu/SMG) |
|2022/12| TJU | [CdCLR: Clip-Driven Contrastive Learning for Skeleton-Based Action Recognition](https://ieeexplore.ieee.org/document/10008837)| VCIP | -|
|2022/08| Univ. of Oulu | [Efficient dense-graph convolutional network with inductive prior augmentations for unsupervised micro-gesture recognition](https://ieeexplore.ieee.org/document/9956565/authors#authors) | ICPR |-|
|2021/07| TJU             | [iMiGUE: An Identity-free Video Dataset for Micro-Gesture Understanding and Emotion Analysis](https://ArXiv.org/abs/2107.00285)                                                    | CVPR       | [Github](https://github.com/linuxsino/iMiGUE) |
## ♥️Contributing

We warmly welcome contributions from the community. You can submit pull requests to add new papers, datasets, projects, or to fix incorrect entries. Please format each new row as `"Date|Institute|Paper|Publication|Project link"` to keep the table consistent. Thank you for helping improve this repository.

## 🗒️Citation

If you find our survey useful for your research, please cite us:

```bibtex
@Article{MIR-2025-09-543,
title = {Micro-gesture Recognition: A Comprehensive Survey of Datasets, Methods, and Challenges},
journal = {Machine Intelligence Research},
volume = {23},
number = {2},
pages = {308-330},
year = {2026},
issn = {2731-538X},
doi = {10.1007/s11633-025-1629-x},	
url = {https://www.mi-research.net/en/article/doi/10.1007/s11633-025-1629-x},
author = {Taorui Wang and Xun Lin and Yong Xu and Qilang Ye and Dan Guo and Sergio Escalera and Ghada Khoriba and Zitong Yu}
}
```
