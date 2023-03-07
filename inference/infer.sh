#!/bin/bash -eux
#SBATCH --job-name=captioning-blip
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=<MAIL>
#SBATCH --partition=<PARTITION_NAME> # -p
#SBATCH --account=<ACCOUNT_NAME> # -A
#SBATCH --mem-per-cpu=<NUMBER>G
#SBATCH --gpus=<NUMBER>

eval "$(conda shell.bash hook)"
set +eu
source activate blip
set +eu

cd LAVIS

# add optional arguments: --max_length=<int>, --num_captions=<int>, --model_type=<str>, --use_nucleus_sampling=<bool>
python predict.py --image_path=<str> -force_words <multiple str>
