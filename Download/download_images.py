from simple_image_download import simple_image_download as sid
response = sid.simple_image_download
#Provide comma separated keywords to download other images.
keywords= {"beercan"}

for kw in keywords:
    response().download(kw, 15)
