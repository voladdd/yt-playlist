import os
from pytube import Playlist, YouTube

def run(playlist):
    # get linked list of links in the playlist
    links = playlist.video_urls
    # download each item in the list
    for l in links:
        # converts the link to a YouTube object
        video = YouTube(l, use_oauth=True, allow_oauth_cache=True)
        print(video.title, "downloading...")
        
        # changes: added filter to download mp3 only
        music = video.streams.filter(only_audio=True).first()
        out_file = music.download(output_path=f"downloads\\{playlist.title}")
        
        # save the file 
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
         
        print(video.title, "downloaded")
    print(f"{playlist.title} downloaded")

if __name__ == "__main__":
    file = open('playlists-urls-to-download.txt')
    urls = file.readlines()    
    
    for url in urls:        
        playlist = Playlist(url)
        run(playlist)
