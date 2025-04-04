# Rethinking Large-scale Dataset Compression: Shifting Focus From Labels to Images
[[`Paper`]() | [`BibTex`](#citation) | [`🤗Dataset`](https://huggingface.co/collections/he-yang/rethinking-large-scale-dataset-compression-67a4634cb4ed419d3a6d2720) | [`📂Logs`](https://drive.google.com/drive/folders/17tearagY46nDj1D-MfegzM9kNAOAK8SR?usp=drive_link)]

---

Official Implementation for "[Rethinking Large-scale Dataset Compression: Shifting Focus From Labels to Images]()".

[Lingao Xiao](https://scholar.google.com/citations?user=MlNI5YYAAAAJ),&nbsp;
[Songhua Liu](https://scholar.google.com/citations?user=AnYh2rAAAAAJ),&nbsp;
[Yang He*](https://scholar.google.com/citations?user=vvnFsIIAAAAJ),&nbsp;
[Xinchao Wang](https://scholar.google.com/citations?user=w69Buq0AAAAJ)


> **Abstract**: Dataset distillation and dataset pruning aim to compress datasets to improve computational and storage efficiency. However, due to differing applications, they are typically not compared directly, creating uncertainty about their relative performance. Additionally, inconsistencies in evaluation settings among dataset distillation studies prevent fair comparisons and hinder reproducibility. Therefore, there is an urgent need for a benchmark that can equitably evaluate methodologies across both distillation and pruning literature.
Notably, our benchmark has demonstrated the effectiveness of soft labels in evaluations, even for randomly selected subsets.
This advantage has shifted researchers' focus away from the images themselves, but soft labels are cumbersome to store and use. To address these concerns, we propose a framework, *Prune, Combine, and Augment (PCA)*, which prioritizes image data and relies solely on hard labels for evaluation. Our benchmark and framework aim to refocus attention on image data in dataset compression research, paving the way for more balanced and accessible techniques.

## TODOs
- [x] release large-scale benchmark
- [x] release SOTA datasets
- [ ] release PCA framework
- [ ] release PCA datasets

*Note: for soft label benchmark, we use [fast evaluation code without relabeling](https://github.com/VILA-Lab/SRe2L/tree/main/SRe2L/validate#alternative-validation).

## Datasets ([🤗Hugging Face](https://huggingface.co/collections/he-yang/rethinking-large-scale-dataset-compression-67a4634cb4ed419d3a6d2720))

SOTA datasets used in our experiments are available at [🤗Hugging Face](https://huggingface.co/collections/he-yang/rethinking-large-scale-dataset-compression-67a4634cb4ed419d3a6d2720).
We have preprocessed all images into fixed 224x224 resolutioins and creates the datasets for a fair storage comparison.

| Method                                         | Type | Venue      | Dataset Key                                            | Avaiable IPCs          |
| ---------------------------------------------- | ---- | ---------- | ------------------------------------------------------ | ---------------------- |
| random                                         | -    | -          | he-yang/2025-rethinkdc-imagenet-random-ipc-`[IPC]`     | `[1,10,20,50,100,200]` |
| [SRe2L](https://arxiv.org/abs/2306.13092)      | `D`  | NeurIPS'23 | he-yang/2025-rethinkdc-imagenet-sre2l-ipc-`[IPC]`      | `[10,50,100]`          |
| [CDA](https://arxiv.org/abs/2311.18838)        | `D`  | TMLR'24    | he-yang/2025-rethinkdc-imagenet-cda-ipc-`[IPC]`        | `[10,50,100]`          |
| [G-VBSM](https://arxiv.org/abs/2311.17950)     | `D`  | CVPR'24    | he-yang/2025-rethinkdc-imagenet-gvbsm-ipc-`[IPC]`      | `[10,50,100]`          |
| [LPLD](https://arxiv.org/abs/2410.15919)       | `D`  | NeurIPS'24 | he-yang/2025-rethinkdc-imagenet-lpld-ipc-`[IPC]`       | `[10,50,100]`          |
| [RDED](https://arxiv.org/abs/2312.03526)       | `D`  | CVPR'24    | he-yang/2025-rethinkdc-imagenet-rded-ipc-`[IPC]`       | `[10,50,100]`          |
| [DWA](https://arxiv.org/abs/2409.17612)        | `D`  | NeurIPS'24 | he-yang/2025-rethinkdc-imagenet-dwa-ipc-`[IPC]`        | `[10,50,100]`          |
| [Forgetting](https://arxiv.org/abs/1812.05159) | `P`  | ICLR'19    | he-yang/2025-rethinkdc-imagenet-forgetting-ipc-`[IPC]` | `[10,50,100]`          |
| [EL2N](https://arxiv.org/abs/2107.07075)       | `P`  | NeurIPS'21 | he-yang/2025-rethinkdc-imagenet-el2n-ipc-`[IPC]`       | `[10,50,100]`          |
| [AUM](https://arxiv.org/abs/2001.10528)        | `P`  | NeurIPS'20 | he-yang/2025-rethinkdc-imagenet-aum-ipc-`[IPC]`        | `[10,50,100]`          |
| [CCS](https://arxiv.org/abs/2210.15809)        | `P`  | ICLR'23    | he-yang/2025-rethinkdc-imagenet-ccs-ipc-`[IPC]`        | `[10,50,100]`          |
- `D` denotes dataset distillation literatures, and `P` is dataset pruning.

To use it, you do **NOT** need to download them manually:
```python
from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("[Dataset-Key]")
```

Or, simply install our package and put the dataset-key as training directory. For more details, please follow [Package Usage](#usage).


## Installation

Install from pip (tested on python=3.12)
```sh
pip install rethinkdc
```


<details>
<summary>Install from source</summary>

**Step 1**: Clone Repo,
```sh
git clone https://github.com/ArmandXiao/Rethinking-Dataset-Compression.git
cd Rethinking-Dataset-Compression
```

**Step 2**: Create Environment,
```sh
conda env create -f environment.yml
conda activate rethinkdc
```

**Step 3**: Install Benchmark,
```sh
make build
make install
```
</details>

## Usage
Prepare:
```
export IMAGENET_VAL_DIR=[YOUR_PATH_TO_IMAGENET_VALIDATION_DIR]

# example
export IMAGENET_VAL_DIR="./imagenet/val"
```

General Usage:
```sh
rethinkdc --help
```

Example Usage:
```sh
# use default soft/hard standard evaluation setting
rethinkdc [YOUR_PATH_TO_DATASET] [*ARGS]

# change training dataset (test random dataset)
rethinkdc he-yang/2025-rethinkdc-imagenet-random-ipc-10 --soft --ipc 10 --output-dir ./random_ipc10_soft
```
- more examples can be found in folder [script](script)

## Main Table Result ([📂Google Drive](https://drive.google.com/drive/folders/17tearagY46nDj1D-MfegzM9kNAOAK8SR?usp=drive_link))

Logs for main tables are results provided in [google drive](https://drive.google.com/drive/folders/17tearagY46nDj1D-MfegzM9kNAOAK8SR?usp=drive_link) for reference.

| Table                                                                                                          | Explanation                                                     |
| -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| [Table 3](https://drive.google.com/drive/folders/1ZlqoLPmMV235F4G3NyCMM1af_VTHPjA7?usp=drive_link)             | Random baselines in soft label setting with standard evaluation |
| [Table 4 & Table 18](https://drive.google.com/drive/folders/1Zs25THv54VNYcJ72KeyABjMZYL7hFbxT?usp=drive_link)  | SOTA methods in soft label setting with std                     |
| [Table 5 & Table 19](https://drive.google.com/drive/folders/1T1xsCWA9ahhICAeTBiVLlYX-G0-bw6gy?usp=drive_link)  | SOTA methods in hard label setting with std                     |
| [Table 6](https://drive.google.com/drive/folders/1rtEnoO8TUteg5E5wS1vLazuix-B0r3ph?usp=drive_link)             | SOTA Pruning Rules                                              |
| [Table 7](https://drive.google.com/drive/folders/13OBiPnBA8y2iCu-9C63d0iR6jdEKKrTB?usp=drive_link)             | Ablation Study of PCA                                           |
| [Table 8](https://drive.google.com/drive/folders/1-QTCzBEgQDw_RtyYXSy0zYOZcvAG7BCo?usp=drive_link)             | Cross-architecture Performance of PCA                           |
| [Table 12 & Table 22](https://drive.google.com/drive/folders/1YKFPAtmnoFAQipLd2YNlSsoNColf46aU?usp=drive_link) | Regularization-based Data Augmentation                          |
| [Table 20](https://drive.google.com/drive/folders/1O4dt67os89kHvVROcjYgNSLtMHQU4V6K?usp=drive_link)            | Pure Noise as Input                                             |
| [Table 24](https://drive.google.com/drive/folders/1PW2Pf8o7f_3ZvCIvyU6-Rd-9mFMdxetn?usp=drive_link)            | PCA using Different Pruning Methods                             |


## Related Repos
Our repo is either build upon the following repos:
- [https://github.com/VILA-Lab/SRe2L](https://github.com/VILA-Lab/SRe2L)
- [https://github.com/he-y/soft-label-pruning-for-dataset-distillation](https://github.com/he-y/soft-label-pruning-for-dataset-distillation)
- [https://github.com/haizhongzheng/Coverage-centric-coreset-selection](https://github.com/haizhongzheng/Coverage-centric-coreset-selection)

Similar Repos:
- [https://github.com/NUS-HPC-AI-Lab/DD-Ranking](https://github.com/NUS-HPC-AI-Lab/DD-Ranking)


## Citation
```
```