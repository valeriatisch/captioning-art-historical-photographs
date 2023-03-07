#!/bin/bash -eux
#SBATCH --job-name=eval
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=<EMAIL>
#SBATCH --partition=<PARTITION_NAME> # -p
#SBATCH --gpus=<NUMBER>
#SBATCH --account=<ACCOUNT_NAME> # -A
#SBATCH --mem=<NUMBER>G

# Initialize conda:
eval "$(conda shell.bash hook)"
set +eu
conda activate <ENV>
set +eu
cd LAVIS
python evaluate.py --cfg-path lavis/projects/blip/eval/caption_artpedia_eval.yaml
