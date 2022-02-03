from youtube_comment_scraper_python import *
youtube.open("https://www.youtube.com/watch?v=dBIr3DaWu0A")
all_data=[]
for i in range(0,1):
	response=youtube.video_comments()
	data=response['body']
	all_data.extend(data)
print(type(all_data))