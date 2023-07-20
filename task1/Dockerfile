#FROM pytorch/pytorch:1.13.0-cuda11.6-cudnn8-devel
FROM python:3.10-slim

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install unzip

RUN groupadd -r user && useradd -m --no-log-init -r -g user user
RUN python -m pip install --user -U pip && python -m pip install --user pip-tools

RUN mkdir -p /opt/app /input /output /opt/nnUNet_trained_models/nnUNet/3d_fullres \
    /opt/nnUNet_raw_data_base /opt/nnUNet_preprocessed && chown user:user /opt/app /input /output /opt/nnUNet_trained_models/nnUNet/3d_fullres \
    /opt/nnUNet_raw_data_base /opt/nnUNet_preprocessed
    

WORKDIR /opt/app
ENV PATH="/home/app/.local/bin:${PATH}"

RUN python -m pip install --user -U pip
COPY --chown=app:app requirements.txt /opt/app/requirements.txt
COPY --chown=app:app tools /opt/app/tools 
COPY --chown=app:app main.py /opt/app/main.py
COPY --chown=app:app weight_dl.py /opt/app/weight_dl.py

RUN python -m pip install --user torch==1.12.0+cu116 torchvision==0.13.0+cu116 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu116
RUN pip install -e /opt/app/tools/nnUNet
RUN python -m pip install --user -r requirements.txt
RUN python -m weight_dl
RUN unzip Task606_SegRap1.zip -d /opt/nnUNet_trained_models/nnUNet/3d_fullres
RUN chown user:user /opt/nnUNet_trained_models/nnUNet/3d_fullres/Task606_SegRap1/
RUN rm Task606_SegRap1.zip
ENV RESULTS_FOLDER="/opt/nnUNet_trained_models:${RESULTS_FOLDER}"

CMD ["python","main.py"]
