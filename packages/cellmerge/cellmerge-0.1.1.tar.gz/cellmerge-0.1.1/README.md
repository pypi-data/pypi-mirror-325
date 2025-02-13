# MergeSegmentations

## Repository overview
This repository contains the file and scripts that support the study titled ***"Efficient integration and validation of deep learning-based nuclei segmentations in H&E slides from multiple models"***

1)  [Merging segmentations](#Merging-segmentations-using-our-package)
2)  [Recreating Figures in manuscript](#Script-to-recreate-plots-as-demonstrated-in-manuscript)
3)  [Linear mixed models for assessing variance explained in bulk-RNA gene expression data](#Script-to-build-mixed-linear-models)
4)  [Pathway analysis for genes explained by high variance](#Pathway-analysis-script)

All the data and files required to run the scripts are located in the [data](https://github.com/jagadhesh89/MergeSegmentations/tree/main/data) directory. 

The study overview is illustrated here:

![Study overview](https://github.com/jagadhesh89/MergeSegmentations/blob/main/Overview_final.jpeg)

## Merging segmentations using our package
Usage:  
```
pip install cellmerge==0.1.0
cellmerge -m <method1_predictions> -p <method2_predictions> -o outdir
```

Sample files for the -m and -p options are in the data directory under monusac and pannuke sub-directories. 

The input to the scripts are prediction files from the monusac and pannuke models. This can be tweaked to take inputs from any similar models as long as the outputs follow a datastructure that is similar to the format described as follows:

The file is a pickle dump with underlying datastructure as a dictionary. Where each key corresponds to a unique nuclei id. 

For example:
{
  'id1':{'box':[],'centroid':[],'contour':[], 'prob':[], 'type':[]},  
  'id2':{'box':[],'centroid':[],'contour':[], 'prob':[], 'type':[]}  
}

The box describes the bounding box of the nuclei
The centroid describes the centroid x,y coordinates of the nuclei
The countour describes the boundary of the nuclei in coordinates
The prob details the probability of the prediction of nuclei
The type details the type of the nuclei, i.e epithelial etc. 

The primary function of this code is the "merge_coordinates" function in the script that uses [Annoy](https://github.com/spotify/annoy) to merge the predictions.

The output is a ".dat" file which is a pickle file, which has all the combined/integrated/merged predictions in a datastructure described in the example above. 


## Script to recreate plots as demonstrated in manuscript
The Jupyter notebook titled **[paper_plots_final.ipynb](https://github.com/jagadhesh89/MergeSegmentations/blob/main/paper_plots_final.ipynb)** has the analyses scripts that created the plots. Associated files to run this jupyter notebook have also been uploaded to the repository. 

## Script to build mixed linear models
The script titled **[pca_script.R](https://github.com/jagadhesh89/MergeSegmentations/blob/main/pca_script.R)** that performs this analysis uses the variancePartition package in R to build the mixed models to assess the variance contributed by the individual models. 

## Pathway analysis script
The script titled **[pathway.R](https://github.com/jagadhesh89/MergeSegmentations/blob/main/pathway.R)** that performs this analysis uses the WebGestaltR package to perform the analysis. 
