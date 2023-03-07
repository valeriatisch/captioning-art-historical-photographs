#!/bin/bash -eux
#SBATCH --job-name=captioning
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=<EMAIL>
#SBATCH --partition=<PARTITION_NAME> # -p
#SBATCH --gpus=<NUMBER>
#SBATCH --account=<ACCOUNT_NAME> # -A
#SBATCH --mem=<NUMBER>G
#SBATCH --time=09:00:00
#SBATCH --exclude=<NODE_NAME> # if needed

# Initialize conda:
eval "$(conda shell.bash hook)"
set +eu
conda activate <ENV>
set +eu
cd LAVIS
python train.py --cfg-path lavis/projects/blip/train/artpedia.yaml

