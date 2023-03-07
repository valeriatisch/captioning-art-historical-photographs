#!/bin/bash -eux
#SBATCH --account=<ACCOUNT_NAME> # -A
#SBATCH --job-name=convert_bw
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=<MAIL>
#SBATCH --partition=<PARTITION_NAME> # -p
#SBATCH --gpus=<NUMBER>
#SBATCH --mem=<NUMBER>G
# Initialize conda:
eval "$(conda shell.bash hook)"
set +eu
conda activate <ENV>
set +eu
python convert_bw.py artpedia/imgs/ artpedia/imgs/bw/