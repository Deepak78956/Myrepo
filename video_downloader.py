from pytube import YouTube
import pprint


print("Welcome to YouTube video downloader utility\n")
yurl = input("Enter URL of the youtube video you wants to download\n")
yt = YouTube(yurl)
title = yt.title
print(f'{title} is the title of your youtube video url\n')
dstream = yt.streams.all()
pprint.pprint(dstream)
while True:
    try:
        num = int(input("Choose from above streams"))
        break
    except:
        print("Enter valid integer")
stream = dstream[num-1]
stream.download()
print("Download Succesful\n")
   
    



