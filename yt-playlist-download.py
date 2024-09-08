import os
from pytubefix import Playlist, YouTube

def downloadMp3s(links):
    for l in links:
        # converts the link to a YouTube object
        video = YouTube(l, use_oauth=True, allow_oauth_cache=True)
        print(video.title, "downloading audio...")
        
        # changes: added filter to download mp3 only
        music = video.streams.filter(only_audio=True).first()
        out_file = music.download(output_path=f"downloads\\{playlist.title}")
        
        # save the file 
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        print(video.title, "audio downloaded")
        
def downloadMp4s(links):
    for l in links:
        # converts the link to a YouTube object
        video = YouTube(l, use_oauth=True, allow_oauth_cache=True)
        print(video.title, "downloading video...")
        
        # changes: added filter to download mp4 only
        video_opts = video.streams.filter(progressive=True, file_extension='mp4').first()
        video_opts.download(output_path=f"downloads\\{playlist.title}")
            
        print(video.title, "video downloaded")

def run(playlist, download_extension):
    # get linked list of links in the playlist
    links = playlist.video_urls
    # download each item in the list
    if (download_extension == 'mp3'):
        downloadMp3s(links)
    else:
        downloadMp4s(links)

    print(f"{playlist.title} downloaded")

if __name__ == "__main__":
    download_extension = input("Set file_extension to download:\n mp3 - to download only audio\n mp4 - to download video\n")
    file = open('playlists-urls-to-download.txt')
    urls = file.readlines()    
    
    for url in urls:        
        playlist = Playlist(url)
        run(playlist, download_extension)
