# Winning submission to the [SegRap 2023](https://segrap2023.grand-challenge.org/segrap2023/) MICCAI challenge
### Inference models for tasks 1 (OAR segmentation) and 2 (GTV segmentation) of SegRap Challenge 2023. The submitted model won the first rank for task 2 and 6th rank for task 1 in the final(test) phase of the challenge.

This repo contains the codes and pre-trained weights for the winning submission to the SegRap 2023 MICCAI challenge.
The code was developed based on [nnUNet](https://github.com/MIC-DKFZ/nnUNet) and [TotalSegmentator](https://github.com/wasserth/TotalSegmentator).

### Run the inference via docker
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
Please note that the `Input Path` must contain two subdirectories inclduing `./images/head-neck-ct/` (non-contrast-ct images) and `images/head-neck-contrast-enhanced-ct/` (contrast-ct images)
with volumetric images in `.mha` file format.
More details regarding the data structure and formats can be found in [SegRap official repo](https://github.com/HiLab-git/SegRap2023)

### Citation
If you found this work useful for your research, please consider citing:

arXiv{Astaraki2023, title = { Fully Automatic Segmentation of Gross Target Volume and Organs-at-Risk for Radiotherapy Planning of Nasopharyngeal Carcinoma }, <br> author = {Astaraki, Mehdi and Bendazzoli, Simone and Toma-Dasu, Iuliana}, <br/> url = {https://doi.org/10.48550/arXiv.2310.02972}, year = {2023}}

### Acknowledgment
This model was developed, evaluated, and submitted by Mehdi Astaraki, and [Simone Bendazzoli](https://github.com/SimoneBendazzoli93).

