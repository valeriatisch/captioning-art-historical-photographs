================
ARTPEDIA DATASET
================

Artpedia contains a collection of 2,930 painting images, each associated to a variable number of textual descriptions. Each sentence is labelled either as a visual sentence or as a contextual sentence, if does not describe the visual content of the artwork. Contextual sentences can describe the historical context of the artwork, its author, the artistic influence or the place where the painting is exhibited. As in standard cross-modal datasets, the association between sentences and painting is also provided. Overall, the dataset contains a total of 28,212 sentences, 9,173 labelled as visual sentences and the remaining 19,039 as contextual sentences.


JSON FILE
=========
Each item of the json file contains the following attributes:
- title: title of the painting 
- img_url: url of the image painting
- year: year of the painting
- visual_sentences: list of visual sentences associated to the painting
- contextual_sentences: list of contextual sentences associated to the painting
- split: dataset split of the painting (train/val/test)


DATASET EXAMPLE
===============
{
	"title": "Wanderer above the Sea of Fog", 
	"img_url": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg", 
	"year": 1818, 
	"visual_sentences": ["In the foreground, a young man stands upon a rocky precipice with his back to the viewer.", "He is wrapped in a dark green overcoat, and grips a walking stick in his right hand.", "His hair caught in a wind, the wanderer gazes out on a landscape covered in a thick sea of fog.", "Through the wreaths of fog, forests of trees can be perceived atop these escarpments.", "In the far distance, faded mountains rise in the left, gently levelling off into lowland plains in the east.", "Beyond here, the pervading fog stretches out indefinitely, eventually commingling with the horizon and becoming indistinguishable from the cloud-filled sky."], 
	"contextual_sentences": ["Wanderer above the Sea of Fog (German:", "Der Wanderer \u00fcber dem Nebelmeer), also known as Wanderer above the Mist or Mountaineer in a Misty Landscape, is an oil painting", "c.\u20091818 by the German Romantic artist Caspar David Friedrich.", "It has been considered one of the masterpieces of Romanticism and one of its most representative works.", "It currently resides in the Kunsthalle Hamburg in Hamburg, Germany.", "In the middle ground, several other ridges, perhaps not unlike the ones the wanderer himself stands upon, jut out from the mass.", "The painting is composed of various elements from the Elbe Sandstone Mountains in Saxony and Bohemia, sketched in the field but in accordance with his usual practice, rearranged by Friedrich himself in the studio for the painting.", "In the background to the right is the Zirkelstein.", "The mountain in the background to the left could be either the Rosenberg or the Kaltenberg.", "The group of rocks in front of it represent the Gamrig near Rathen.", "The rocks on which the traveller stands are a group on the Kaiserkrone."], 
	"split": "train"
}


CITATION
========
If you use this dataset, please cite the following paper:

@inproceedings{stefanini2019artpedia,
  	  title={{Artpedia: A New Visual-Semantic Dataset with Visual and Contextual Sentences}},
  	  author={Stefanini, Matteo and Cornia, Marcella and Baraldi, Lorenzo and Corsini, Massimiliano and Cucchiara, Rita},
  	  booktitle={Proceedings of the International Conference on Image Analysis and Processing},
  	  year={2019}
} 


CONTACT
=======
If you have any question, drop us an e-mail at matteo.stefanini@unimore.it or marcella.cornia@unimore.it.