from pytube import YouTube
link = input("Enter the link of the video:")
video = YouTube(link)
print("Title:", video.title)
print("Description:", video.description)
print("Date:",video.publish_date)
print("Channel Name:", video.author)
print("Views:", video.views)
print("keywords:", video.keywords)
