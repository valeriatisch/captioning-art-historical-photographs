#!/bin/bash -eux
#SBATCH --job-name=evalCapWPI
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=<MAIL>
#SBATCH --partition=<PARTITION_NAME> # -p
#SBATCH --gpus=<NUMBER>
#SBATCH --account=<ACCOUNT_NAME> # -A
#SBATCH --mem=<NUMBER>G
#SBATCH --time=24:00:00
 
# Initialize conda:
eval "$(conda shell.bash hook)"
set +eu
conda activate blip
set +eu
cd LAVIS
python evaluate.py --cfg-path lavis/projects/blip/eval/wpi_eval.yaml
