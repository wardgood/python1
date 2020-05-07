from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=nVQFaK0Pq2I')

video=yt.streams.filter(file_extension='mp4', res='1080p').first()

video.download(r'E:\\')