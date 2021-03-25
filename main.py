from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import VideoPrivate
from pytube.extract import is_private, video_id, video_info_url

DOWNLOAD_DIR = 'C:\Music' #path for the downloaded files

#functions
def downloadVideo(url, audioOrVideo): 
    yt = YouTube(url)
    if audioOrVideo == "audio":
        incomingStream = yt.streams.get_audio_only()
    else : 
        incomingStream = yt.streams.get_highest_resolution()
    
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    print("Downloading...")
    incomingStream.download(DOWNLOAD_DIR)
    print("Download completed!!")


def downloadPlaylist(url, audioOrVideo):
    playlist = Playlist(url)
    print("Downloading...")
    for video in playlist.videos:
        try : #for some weird reason, shit hits the fan if there's private videos on the playlist, so be aware
                #tried pytube's 'is_private'-function combined with try&catch, didn't work, the problem might be on the youtube's end
            if audioOrVideo == "audio": 
                incomingStream = video.streams.get_audio_only()
            else : 
                incomingStream = video.streams.get_highest_resolution() #need to check out DASH /w FFMpeg

            incomingStream.download(output_path=DOWNLOAD_DIR)
            print(incomingStream.title, " downloaded...")
        except : 
            print("Private video, couldn't be downloaded")
    print("Download completed!!")

#asking for inputs & simple functionality
print("This program downloads YouTube Videos OR just the Audio in the highest possible quality, works with whole playlists too")
print()
videoOrPlaylist = input("Type in 'video' or 'playlist', whichever you want to be downloaded  :  ")
print()

if videoOrPlaylist == "video" :
    link = input("Enter the video's YouTube URL :  ")
    print()
    audioOrVideo = input("Type in 'video' to download in video format or 'audio' just for the audio  :  ")
    downloadVideo(link, audioOrVideo)

else : 
    link = input("Enter the YouTube playlists URL :  ")
    print()
    audioOrVideo = input("Type in 'video' to download in video format or 'audio' just for the audio  :  ")
    downloadPlaylist(link, audioOrVideo)

print("All done! :)")