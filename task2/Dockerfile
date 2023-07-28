FROM nvcr.io/nvidia/pytorch:22.04-py3

RUN apt-get update -y
RUN apt-get install unzip
WORKDIR /opt

RUN mkdir SegRap23
RUN mkdir -p /opt/nnUNet_trained_models/nnUNet/3d_fullres
RUN mkdir /opt/app/

RUN chmod -R 777 SegRap23
RUN chmod -R 777 /opt/nnUNet_trained_models/nnUNet/3d_fullres
RUN chmod -R 777 /opt/app

## Clone and Install totalsegmentor(and nnUNet v1)
RUN pip install TotalSegmentator

RUN adduser user
USER user

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
RUN unzip /opt/app/Task609_SegRapTumor -d /opt/nnUNet_trained_models/nnUNet/3d_fullres
ENV RESULTS_FOLDER=/opt/nnUNet_trained_models

CMD ["python","main.py", "-i", "/input","-o","/output"]
