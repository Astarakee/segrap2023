# Docker Packaging and Model Inference

To build the SegRap Docker Image:

```shell
docker build . -t segrap2023_oar_segmentationcontainer
```

To run the prediction on new data:

```shell
docker run --rm --gpus <GPU NUM> -v <PATH/TO/LOCAL/INPUT_FOLDER>:/input/images/ -v </PATH/TO/LOCAL/OUTPUT_FOLDER>:/output/images/ --shm-size 2g segrap2023_oar_segmentationcontainer
```
Input folder must contains two subdirectories standing for two modalitites.