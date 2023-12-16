import gdown

weight_gdrive = "https://drive.google.com/uc?id=1fj1wAI1Xj7ykWtayKAIXZSZ4FkHoqGqU"
total_weight = "https://drive.google.com/uc?id=17rfov8knJC6TyXiBHI4HR4ks49YI7ew6"
dst_unzip = "/opt/app/"
dst_unzip_totalseg = "/opt/app/"
gdown.download(weight_gdrive, dst_unzip)
gdown.download(total_weight, dst_unzip_totalseg)
