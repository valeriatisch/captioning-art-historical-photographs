#!/bin/bash -eux
#SBATCH --job-name=crawl_artists
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=<EMAIL>
#SBATCH --partition=<PARTITION_NAME> # -p
#SBATCH --gpus=<NUMBER>
#SBATCH --account=<ACCOUNT_NAME> # -A
#SBATCH --time=04:00:00

eval "$(conda shell.bash hook)"
set +eu
source activate <ENV>
set +eu

python query_artpedia_artists.py --input=../artpedia/artpedia.json --output=artpedia_artists_mapping_clean
