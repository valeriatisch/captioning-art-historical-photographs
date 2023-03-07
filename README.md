# Captioning Art-Historical Photographs

## Table of Contents 📋
1. [Overview](#overview-)
2. [Report](#report-)
3. [Repo Structure](#repo-structure-)
4. [Setup](#setup-)
5. [Datasets](#datasets-)
   1. [Artpedia Dataset](#artpedia-dataset)
   2. [Wildenstein Plattner Institute (WPI) Dataset](#wildenstein-plattner-institute-wpi-dataset)
6. [Models](#models-)
7. [Experiments](#experiments-)
   1. [Finetuning BLIP on Artpedia](#finetuning-blip-on-artpedia-)
      1. [Training](#training-)
      2. [Evaluation](#evaluation-)
   2. [Finetuning with Grayscale Images](#finetuning-with-grayscale-images-)
   3. [Finetuning on Filtered Artpedia Dataset](#finetuning-on-filtered-artpedia-dataset-)
   4. [Constrained Caption Generation](#constrained-caption-generation-)
   5. [Artists](#artists-)
8. [Contribution](#want-to-contribute-)
9. [Credits](#credits-)

## Overview 🌃
The [Wildenstein Plattner Institut](https://wpi.art/) owns a vast collection of art-historical photographs.
To make them more accessible, captions are required, especially for visually impaired individuals.
Because manually creating captions would be too time-consuming an automatic solution is needed.
We present an approach, that is specifically adapted to art images. We work with the language-image pre-training
framework [BLIP](https://github.com/salesforce/BLIP). For that, we leverage the
[LAVIS](https://github.com/salesforce/LAVIS) library, which provides an interface for applying BLIP.
We finetune BLIP's pre-trained base model on the art image dataset
[Artpedia](https://aimagelab.ing.unimore.it/imagelab/page.asp?IdPage=35)
and investigate methods to improve the training dataset and caption generation. In all approaches, the finetuned models show
better results than the pre-trained ones. The captions become more detailed and sometimes contain art-specific
content like painting styles.

## Report 📄
If you are interested in the details of our project, please have a look at our [report](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/report.pdf).
There, you will find our motivation behind this project, a detailed explanation of the methods used,
specifically the BLIP model and the evaluation metrics.
All of our experiments and results are presented and discussed in depth, including qualitative and quantitative analysis. 
We also talk about possible future work, in case you'd like to enhance our work.

## Repo Structure 🗂

| Folder / File                                                                                                        | Description                                                                                       |
|:---------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| [LAVIS](https://github.com/valeriatisch/LAVIS)                                                                       | Forked LAVIS submodule                                                                            |
| [artists](https://github.com/valeriatisch/captioning-art-photographs-blip/tree/main/artists)                         | Evaluation of the artist experiment & querying of artists                                         |
| [artpedia](https://github.com/valeriatisch/captioning-art-photographs-blip/tree/main/artpedia)                       | Artpedia dataset, formatting, analysis, training & evaluation                                     |
| [grayscaled_artpedia](https://github.com/valeriatisch/captioning-art-photographs-blip/tree/main/grayscale)           | Converting Artpedia images to grayscale, training & evaluation                                    |
| [inference](https://github.com/valeriatisch/captioning-art-photographs-blip/tree/main/inference)                     | Constrained caption generation                                                                    |
| [plot](https://github.com/valeriatisch/captioning-art-photographs-blip/tree/main/plot)                               | Script for plotting the evaluation results                                                        |
| [results](https://github.com/valeriatisch/captioning-art-photographs-blip/tree/main/output)                          | Evaluation results (finetuned vs. base model)                                                     |
| [wpi](https://github.com/valeriatisch/captioning-art-photographs-blip/tree/main/wpi)                                 | WPI dataset, analysis & evaluation                                                                |
| [lavis_example.ipynb](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/lavis_example.ipynb) | Google Colab Jupyter notebook with examples for using LAVIS to generate captions & attention maps |
| [*report*](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/report.pdf)                     | Our extensive report of the project                                                               |

## Setup 🛠

[Python](https://www.python.org/downloads/) and a package manager like [pip](https://pip.pypa.io/en/stable/installation/)
and/or [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) need to be installed on your system.

1. Open your terminal and clone the **repository**, including the submodules.
```shell
git clone --recurse-submodules  https://github.com/valeriatisch/captioning-art-photographs-blip.git
```

If cloned the repo without the submodules, you can run:
```shell
git submodule update --init
```

To update the repo with the submodules, you can run:
```shell
git pull --recurse-submodules
```

2. We recommend creating a virtual **environment**.
You can create and activate a new environment with [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
or another package manager of your preference.
```shell
conda create -n captioning_art pip python=3.8
conda activate captioning_art
```

To deactivate the environment, run:
```shell
conda deactivate
```

To remove the environment, run:
```shell
conda remove -n captioning_art --all
```

3. To set up the `LAVIS` **submodule**, please follow this [guide](https://github.com/valeriatisch/LAVIS#installation).
You can also use our [installs.sh](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/installs.sh)
script for installation or take a look at it in case you run into installation problems. 
You might need to install another PyTorch and CUDA versions to match your systems requirements.
```shell
chmod +x installs.sh
./installs.sh
```

4. Install the remaining **requirements**. It might happen that some requirements will already be satisfied through the previous installation, but that shouldn't be a problem.
```shell
pip install -r requirements.txt
```

5. To **run** the code on your local machine, you can simply do as follows:
```shell
python path_to_file/file.py <args>
```
You will also find many shell scripts in the repo, equally named as the corresponding python scripts.
The shell scripts are used to submit a batch job on an HPC cluster using the slurm workload manager.
The script sets various Slurm directives, such as job name, email notifications, partition to run the job, GPUs needed, memory, and time limit.
If you want to use the shell scripts, you need to adjust the settings inside them. <br>
To run a job, execute:
```shell
sbatch path_to_file/file.sh
```

To **train** a model, run:
```shell
cd LAVIS
python train.py --cfg-path lavis/projects/blip/train/<CONFIG>.yaml
```

To **generate** captions, run:
```
cd LAVIS
python predict.py --image_path=<PATH_TO_IMAGE>
```
Please take a look into the script for more options.

To **evaluate** a model, run:
```
cd LAVIS
python evaluate.py --cfg-path lavis/projects/blip/eval/<CONFIG>.yaml
```

Please **_notice_**, that you need to adjust the YAML configs and fill in the right paths,
or you might want to create your own. You also need to adjust the paths in [`LAVIS/lavis/tasks/captioning.py`]().

Please refer to the [LAVIS readme](https://github.com/valeriatisch/LAVIS#readme) and the
[LAVIS documentation](https://opensource.salesforce.com/LAVIS//latest/index.html#) for more information and advanced usage.

How to get the datasets used for our experiments, is described in the [Datasets](#datasets-) section.

How to run the individual experiments, is described in more detail in the [Experiments](#experiments-) section.

6. To run the Jupyter **notebooks**, please make sure [Jupyter](https://docs.jupyter.org/en/latest/install.html#new-to-python-and-jupyter) is installed on your system. 
```
jupyter --version
pip install jupyter
```
Navigate to the directory containing the notebook you'd like to open and launch it:
```shell
cd path_to_directory_with_notebook
jupyter the_notebook.ipynb
```

The notebook will be opened in your default browser.

There is [one notebook](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/lavis_example.ipynb) that needs to be run in a **Google Colab** environment. If you are not familiar with Google Colab,
please look up this [guide](https://medium.com/lean-in-women-in-tech-india/google-colab-the-beginners-guide-5ad3b417dfa).

## Datasets 📚

### Artpedia Dataset
The Artpedia Dataset and the corresponding paper can be found [here](https://aimagelab.ing.unimore.it/imagelab/page.asp?IdPage=35). <br>
To download the images you can execute the beginning cells of this [Jupyter Notebook](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/artpedia/artpedia.ipynb)
to initiate the download of the images. <br>
In the same notebook, we also provide an analysis of the Artpedia dataset. <br>
All plots regarding the Artpedia dataset are saved in [artpedia/plots](https://github.com/valeriatisch/captioning-art-photographs-blip/tree/main/artpedia/plots).

We enhanced the Artpedia dataset, so that in the end each image has the following attributes:

| Attribute               | Description                                                                                                                             | Source    |
|:------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|:----------|
| `title`                 | the title of the painting                                                                                                               | original  |
| `img_url`               | the wikimedia url to the image where to download it                                                                                     | original  |
| `year`                  | the year the painting was created                                                                                                       | original  |
| `visual_sentences`      | a list of visual sentences describing the painting                                                                                      | original  |
| `contextual_sentences`  | a list of contextual sentences describing the painting                                                                                  | original  |
| `split`                 | training (`train`), validation (`val`) and test (`test`) split                                                                          | original  |
| `got_img`               | `yes` or `no`, depending on whether the image could be downloaded                                                                       | new       |
| `matching_scores`       | a list of matching scores between the image and each visual sentence in the same order the sentences are stored `visual_sentences`      | new       |
| `cosine_similarities`   | a list of cosine similarities between the image and each visual sentence in the same order the sentences are stored `visual_sentences`  | new       |
| `visual_sentences`      | the artist of the painting                                                                                                              | new       |

The enhanced dataset can be found [here](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/artpedia/new_artpedia.json).

### Wildenstein Plattner Institute (WPI) Dataset

The Annotations of the WPI dataset can be found in this [JSON file](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/wpi/wpi_annotations.json).<br>
You can execute the beginning cells of this [Jupyter Notebook](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/wpi/wpi.ipynb)
to initiate the download of the images. <br>
In the same notebook, we also provide an analysis of the WPI dataset. <br>
All plots regarding the WPI dataset are saved in [wpi/plots](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/wpi/plots).

The WPI dataset contains the following attributes for an image:

| Attribute    | Description                                                | Present    |
|:-------------|:-----------------------------------------------------------|:-----------|
| `img_urls`   | the url to the image where to download it                  | always     |
| `Title`      | the title of the image                                     | always     |
| `img_path`   | the path to the downloaded image                           | always     |
| `Genres`     | a list of genres the image belongs to                      | sometimes  |
| `Topics`     | a list of topics the image contains                        | sometimes  |
| `Names`      | a list of names like the publisher or author of the image  | sometimes  |
| `Places`     | a list of places the image displays                        | sometimes  |

## Models 🧠
You can find the models we finetuned under this [link](https://nextcloud.hpi.de/s/ExEkDePEXCtq2G9).
The password is `blip_models`.

## Experiments 🧪
Do you want to recreate our experiments or use our scripts on other images?
Here, we try to guide you through the process of preparing the datasets, finetuning, and evaluating the BLIP model as best we can. <br>
In general, you just need to run the corresponding scripts as described in the [Setup](#setup-) section.

### Finetuning BLIP on Artpedia 🖼️
We finetune the BLIP base model on the Artpedia dataset.
We use the training, validation, and test split provided by Artpedia.

#### Training 🏋️‍♀️
First, adjust the config file [`lavis/projects/blip/train/artpedia.yaml`](https://github.com/valeriatisch/LAVIS/blob/main/lavis/projects/blip/train/artpedia.yaml). <br>
To train the model, adjust the shell script and then run:
```shell
sbatch artpedia/train_artpedia.sh
```
Or run the python script directly from the `LAVIS` directory specifying the path to the right config file:
```shell
cd LAVIS
python train.py --cfg-path lavis/projects/blip/train/artpedia.yaml
```

#### Evaluation 📊
Again, adjust [`lavis/projects/blip/eval/caption_artpedia_eval.yaml`](https://github.com/valeriatisch/LAVIS/blob/main/lavis/projects/blip/eval/caption_artpedia_eval.yaml) first. <br>
To evaluate the model, adjust the shell script too, and run:
```shell
sbatch artpedia/eval_artpedia.sh
```
Or:
```shell
cd LAVIS
python evaluate.py --cfg-path lavis/projects/blip/eval/caption_artpedia_eval.yaml
```

### Finetuning on Grayscale Images 🖤
We transform the images of the Artpedia dataset to grayscale and finetune the BLIP base model on them.
Again, we use the training, validation, and test split provided by Artpedia.

To transform the images to grayscale, run:
```shell
sbatch grayscaled_artpedia/convert_bw.sh
```
Or run the python script directly specifying the input and output directory:
```shell
python grayscaled_artpedia/convert_bw.py artpedia/images/ artpedia/images/bw/
```

### Finetuning on Filtered Artpedia Dataset 🔍
We apply BLIP's filter to calculate matching scores for the images and visual sentences of the Artpedia dataset.
We filter out the image-text pairs having a score below a threshold of 80%.

To generate matching scores for the dataset, run:
```shell
cd LAVIS
sbatch match.sh
```
Or run the python script directly specifying the args:
```shell
cd LAVIS
python caption_matching.py ../artpedia/imgs ../artpedia/artpedia_res.json ../artpedia/artpedia_scored.json
```

To train with a filtered version of the Artpedia dataset use [`LAVIS/lavis/projects/blip/train/artpedia_filtered.yaml`](https://github.com/valeriatisch/LAVIS/blob/main/lavis/projects/blip/train/artpedia_filtered.yaml).
You can define your threshold in this config as well.

### Constrained Caption Generation 🤖
We explore the potential of constrained caption generation by forcing tags or other words to be included in generated captions.

To generate captions with a constraint, you can run [`LAVIS/predict.py`](https://github.com/valeriatisch/LAVIS/blob/main/predict.py)
and pass the words to include with `--forcewords`.

### Artists 👩‍🎨
We investigate the model's ability to recognize the artists of given artworks.

Unfortunately, the original Artpedia dataset does not provide the artists.
You can run [`artists/query_artpedia_artists.py`](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/artists/query_artpedia_artists.py)
or [`artists/query_artpedia_artists.sh`](https://github.com/valeriatisch/captioning-art-photographs-blip/blob/main/artists/query_artpedia_artists.sh) to get the artists.
Don't forget to specify the input and output paths.

For evaluation, use [`lavis/projects/blip/eval/caption_artists_eval.yaml`](https://github.com/valeriatisch/LAVIS/blob/main/lavis/projects/blip/eval/caption_artists_eval.yaml).

## Contribution 🤝
You are more than welcome to contribute to this project. <br>
Please feel free to open an [issue](https://github.com/valeriatisch/captioning-art-photographs-blip/issues),
create a [pull request](https://github.com/valeriatisch/captioning-art-photographs-blip/pulls) or just share an idea.

## Credits 🙏
This project makes use of the following two libraries and a dataset:
- [Artpedia](https://aimagelab.ing.unimore.it/imagelab/page.asp?IdPage=35) - _"A New Visual-Semantic Dataset with Visual and Contextual Sentences"_ by Matteo Stefanini, Marcella Cornia, Lorenzo Baraldi, Massimiliano Corsini, Rita Cucchiara
- [BLIP](https://github.com/salesforce/BLIP) - _"Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation"_ by Junnan Li, Dongxu Li, Caiming Xiong, Steven Hoi
- [LAVIS](https://github.com/salesforce/LAVIS) - _"A Library for Language-Vision Intelligence"_ by Dongxu Li, Junnan Li, Hung Le, Guangsen Wang, Silvio Savarese, Steven C. H. Hoi

We want to say a special thank you to the developers for their hard work and for making their code publicly available for others to use.
