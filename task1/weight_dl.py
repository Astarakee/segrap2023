import gdown

weight_gdrive = "https://drive.google.com/uc?id=1HcoyD74deen1jcOPyYB0z8iMxhD4b50y"
dst_unzip = "/opt/app/"
gdown.download(weight_gdrive, dst_unzip)
