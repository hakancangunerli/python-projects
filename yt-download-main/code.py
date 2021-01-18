from pytube import Youtube

link = input("pass the link") #tres simple, mais i get errors a veces 
yt = YouTube(link) 

print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download()
print("Download completed!!")