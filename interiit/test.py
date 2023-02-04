from bing_image_downloader import downloader
downloader.download("Plastic Kitchen Knife", limit=10,  output_dir='test', 
adult_filter_off=True, force_replace=True, timeout=60,verbose=True)