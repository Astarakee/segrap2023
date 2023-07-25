import gdown

weight_gdrive = "https://drive.google.com/uc?id=1XmlBpqqkocbHeraHmi69KpppFzI2TRcG"
dst_unzip = "/opt/app/"
gdown.download(weight_gdrive, dst_unzip)
