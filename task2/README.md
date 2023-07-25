# Docker Packaging and Model Inference for Task2 of SegRap Challenge 2023 (GTVs)

To build the segrap2023_gtv_segmentationcontainer Docker Image:

```shell
docker build . -t segrap2023_gtv_segmentationcontainer 
```

To run the prediction on new data:

```shell
docker run --rm --gpus <GPU NUM> -v <PATH/TO/LOCAL/INPUT_FOLDER>:/input/images/ -v </PATH/TO/LOCAL/OUTPUT_FOLDER>:/output/images/ --shm-size 2g segrap2023_gtv_segmentationcontainer
```

Note that the INPUT_FOLDER must contain two subdirectories (CT, and contrast CT).
