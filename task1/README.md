# Docker Packaging and Model Inference

To build the SegRap Docker Image:

```shell
docker build . -t seg_crop
```

To run the prediction on new data:

```shell
docker run --rm --gpus <GPU NUM> -v <PATH/TO/LOCAL/HEAD-NECK_CT_FOLDER>:/input/images/head-neck-ct -v <PATH/TO/LOCAL/HEAD-NECK_CE_CT_FOLDER>:/input/images/head-neck-contrast-enhanced-ct -v </PATH/TO/LOCAL/OUTPUT_FOLDER>:/output/images/head-neck-segmentation --shm-size 2g seg_crop
```