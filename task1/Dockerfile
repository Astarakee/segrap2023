FROM nvcr.io/nvidia/pytorch:22.04-py3

RUN apt-get update -y
RUN apt-get install unzip
WORKDIR /opt

## Clone and Install totalsegmentor(and nnUNet v1)
RUN pip install TotalSegmentator


RUN mkdir SegRap23
WORKDIR /opt/SegRap23

## Copy SegRap Code
COPY requirements.txt .
COPY weight_dl.py .
COPY main.py .
COPY tools tools/
## Install requirements
RUN pip install -r requirements.txt

## Download Trained Model and store it in /opt/nnUNet_trained_models/nnUNet/3d_fullres
RUN python weight_dl.py
RUN mkdir -p /opt/nnUNet_trained_models/nnUNet/3d_fullres
RUN unzip /opt/app/Task606_SegRap1 -d /opt/nnUNet_trained_models/nnUNet/3d_fullres
ENV RESULTS_FOLDER=/opt/nnUNet_trained_models

CMD ["python","main.py", "-i", "/input","-o","/output"]
