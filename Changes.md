# Overview over changes in LAVIS
## Remove
artpedia folder

## Added files

| File                                                       | Changes                                                                                     |
|:-----------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| caption_matching.py                                        | calculate matching<br> scores and write into file                                           |
| predict.py                                                 | generate captions and <br> create attention maps                                            |
| dataset_card/artpedia.md                                   | dataset information                                                                         |
| lavis/configs/datasets/artpedia/bw_cap.yaml                | dataset configurations                                                                      |
| lavis/configs/datasets/artpedia/defaults_cap.yaml          | dataset configurations                                                                      |
| lavis/configs/datasets/artpedia/filtered.yaml              | dataset configurations                                                                      |
| lavis/configs/datasets/artpedia/artist.yaml                | dataset configurations                                                                      |
| lavis/configs/datasets/wpi/defaults_cap.yaml               | dataset configurations                                                                      |
| lavis/datasets/datasets/artpedia_filtered_dataset.py       | add filtered dataset                                                                        |
| lavis/datasets/datasets/caption_wpi_datasets.py            | add wpi dataset                                                                             |
| lavis/datasets/datasets/caption_wpi_datasets.py            | add wpi dataset                                                                             |
| lavis/projects/blip/eval/caption_artpedia_eval.yaml        | configuration file                                                                          |
| lavis/projects/blip/eval/<br>caption_artpedia_eval_bw.yaml | configuration file                                                                          |
| lavis/projects/blip/eval/wpi_eval.yaml                     | configuration file                                                                          |
| lavis/projects/blip/train/artpedia.yaml                    | configuration file                                                                          |
| lavis/projects/blip/train/artpedia_bw.yaml                 | configuration file                                                                          |
| lavis/projects/blip/train/artpedia_filter.yaml             | configuration file                                                                          |
| lavis/projects/blip/train/artpedia_filtered.yaml           | configuration file                                                                          |
| lavis/projects/blip/eval/caption_artists_eval.yaml         | configuration file                                                                          |
| run_scripts/blip/train/train_artpedia.sh                   | --remove--                                                                                  |
| lavis/tasks/captioning_artpedia.py                         | captioning task for<br> Artpedia to enable logging in tensorboard                           |
| lavis/tasks/captioning_wpi.py                              | captioning task for WPI<br> dataset with tag accuracy metric                                |
| lavis/tasks/captioning_artist.py                           | captioning task for Artpedia <br>dataset with accuracy for matching artists                 |


## Changed files
| File                                             | Changes                                                           |
|:-------------------------------------------------|:------------------------------------------------------------------|
| evaluate.py                                      | fix bug when using distributed_mode = False                       |
| lavis/common/utils.py                            | increase precision of datatime string for logging                 |
| lavis/datasets/builders/__init__.py              | added builder for our datasets                                    |
| lavis/datasets/builders/base_dataset_builder.py  | stop data from being downloaded                                   |
| lavis/datasets/builders/caption_builder.py       | added builders for our datasets                                   |
| lavis/datasets/datasets/caption_datasets.py      | fix for large images bug                                          |
| lavis/datasets/datasets/coco_caption_datasets.py | small change in  to be able to use our annotations for evaluation |
| lavis/models/blip_models/blip_caption.py         | enable using force_words in caption generation                    |
| lavis/models/med.py                              | enable using force_words in caption generation                    |
| lavis/runners/runner_base.py                     | fix bug when using distributed_mode = False                       |
| lavis/runners/runner_iter.py                     | fix bug when using distributed_mode = False                       |
| lavis/tasks/\__init\__.py                        | add tasks for Captioning Artpedia and WPI                         |
| lavis/tasks/captioning.py                        | adjust COCO evaluation, so it can be used for artpedia            |
| requirements-dev.txt                             | add requirements                                                  |
| train.py                                         | fix bug when using distributed_mode = False                       |
