# Docker Packaging and Model Inference

To build the SegRap Docker Image:

```shell
docker build . -t seg_rap_2023
```

To run the prediction on new data:

```shell
docker run -v <PATH/TO/LOCAL/HEAD-NECK_CT_FOLDER>:/input/images/head-neck-ct -v <PATH/TO/LOCAL/HEAD-NECK_CE_CT_FOLDER>:/input/images/head-neck-contrast-enhanced-ct -v </PATH/TO/LOCAL/OUTPUT_FOLDER>:/output/images/head-neck-segmentation --shm-size 2g seg_rap_2023
```