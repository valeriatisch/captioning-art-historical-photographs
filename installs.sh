#!/bin/bash
conda install -y pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch
pip install -r LAVIS/requirements-dev.txt
conda install -y -c "bioconda/label/cf201901" java-jdk
bash get_stanford_model.sh
pip install -U setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm