# Docker Packaging and Model Inference

To build the SegRap Docker Image:

```shell
docker build . -t seg_crop
```

To run the prediction on new data:

```shell
docker run --rm --gpus <GPU NUM> -v <PATH/TO/LOCAL/INPUT_FOLDER>:/input/images/ -v </PATH/TO/LOCAL/OUTPUT_FOLDER>:/output/images/ --shm-size 2g seg_crop
```
Input folder must contains two subdirectories standing for two modalitites.