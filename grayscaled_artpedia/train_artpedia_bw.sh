#!/bin/bash -eux
#SBATCH --job-name=bw_train_captioning
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=<MAIL>
#SBATCH --partition=sorcery # -p
#SBATCH --gpus=1
#SBATCH --account=naumann # -A
#SBATCH --mem=48G
#SBATCH --time=20:00:00
 
# Initialize conda:
eval "$(conda shell.bash hook)"
set +eu
conda activate blip
set +eu
cd LAVIS
python train.py --cfg-path lavis/projects/blip/train/artpedia_bw.yaml

