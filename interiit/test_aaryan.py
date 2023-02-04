# from simple_image_download import simple_image_download as simp
# response = simp.simple_image_download
# a = open("real.txt","r")
# data = a.read()
# a.close()
# data_li = data.split('\n')
# for i in data_li:
#     response().download(f"{i}", 15)

from bing_image_downloader import downloader
a = open("real.txt","r")
data = a.read()
a.close()
data_li = data.split('\n')
# downloader.download("A bowl", limit=7,  output_dir='data', 
#     adult_filter_off=True, force_replace=True, timeout=60,verbose=True)
for i in data_li:
    downloader.download(i, limit=7,  output_dir='data/', 
    adult_filter_off=True, force_replace=True, timeout=60,verbose=True)