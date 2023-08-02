# Docker Packaging and Model Inference for Task1 of SegRap Challenge 2023 (OARs)

To build the segrap2023_oar_segmentationcontainer Docker Image:

```shell
docker build . -t segrap2023_oar_segmentationcontainer
```

To run the prediction on new data:

```shell
docker run --rm --gpus <GPU NUM> --network none --memory="32g" -v <PATH/TO/LOCAL/INPUT_FOLDER>:/input/images/ -v </PATH/TO/LOCAL/OUTPUT_FOLDER>:/output/images/ --shm-size 2g segrap2023_oar_segmentationcontainer
```
Input folder must contain two subdirectories standing for two modalitites (CT and enhanced CT).
