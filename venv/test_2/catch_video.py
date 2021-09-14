from selenium import webdriver
import requests

url = 'https://video.pearvideo.com/mp4/adshort/20210909/cont-1741262-15764285_adpkg-ad_hd.mp4'

# url = 'https://ericsson-my.sharepoint.com/2b927ab7-85f7-44c4-83a9-a2b1ce00fdb1'
r = requests.get(url)
print(r.content)
with open('video.mp4','wb') as f:
    f.write(r.content)