# Winning submission to the SegRap 2023 MICCAI challenge
## Inference models for tasks 1 (OAR segmentation) and 2 (GTV segmentation) of SegRap Challenge 2023.
## The submitted model won the first rank for task 2 and 6th rank for task 1 in the final(test) phase of the challenge.

This repo contains the codes and pre-trained weights for the winning submission to the SegRap 2023 MICCAI challenge.
The code was developed based on [nnUNet](https://github.com/MIC-DKFZ/nnUNet) and [TotalSegmentator](https://github.com/wasserth/TotalSegmentator).

Inference codes for tasks one and two are separated into `./task1` and `./task2` subdirs.

To build the segrap2023_oar_segmentationcontainer (task1) Docker Image:

```shell
docker build . -t segrap2023_oar_segmentationcontainer
```

To run the prediction on new data:

```shell
docker run --rm --gpus <GPU NUM> --network none --memory="32g" -v <PATH/TO/LOCAL/INPUT_FOLDER>:/input/images/ -v </PATH/TO/LOCAL/OUTPUT_FOLDER>:/output/images/ --shm-size 2g segrap2023_oar_segmentationcontainer
```
Likewise, to build the segrap2023_gtv_segmentationcontainer (task2) Docker Image:

```shell
docker build . -t segrap2023_gtv_segmentationcontainer 
```

To run the prediction on new data:

```shell
docker run --rm --gpus <GPU NUM> -v <PATH/TO/LOCAL/INPUT_FOLDER>:/input/images/ -v </PATH/TO/LOCAL/OUTPUT_FOLDER>:/output/images/ --shm-size 2g segrap2023_gtv_segmentationcontainer
```
