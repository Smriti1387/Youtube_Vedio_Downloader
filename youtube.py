from pytube import YouTube 
print("Provide the link of the youtube video here !! \n")
yt = YouTube(input()) 

try:
 print(yt.title) 
 stream = yt.streams.first() 
 stream.download()
except:
 print("Connection Error!")