import requests,os
dir_path = os.path.join(os.getcwd(),'data')
if not os.path.exists(dir_path):
    os.mkdir(dir_path,0o666)
s="GPCQ5"
url="https://aims.iith.ac.in/aims/captcha/getCaptchaByString/"+s
print(f'Downloading...')
response = requests.get(url,stream = True)
if response.status_code == 200:
    with open(os.path.join(dir_path,'2.jpg'), 'wb') as image:
        for block in response.iter_content(chunk_size=1024):
            image.write(block)
    print('successfully downloaded')