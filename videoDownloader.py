import os
def finish():
    print('Download Completed😊, Enjoy My Friend, You will find it in Downloads❤️\n -----------------------------------')

def downloading(resolution):
    print('\n -----------------------------------')
    print(f'Video Quality is : {resolution}\n -----------------------------------')

def playListDownloading(count,res):
    print('\n -----------------------------------')
    print(f'Video Quality is : {res}\n -----------------------------------')
    print(f'Video Number {count} is Downloading....')

# Download from Video, Playlist, That's it ❤️🌹
ask = input('v For One Video, p For Playlist videos, n For Nothing : ')
if ask == 'v':
    # --------------------------- Download Single Video
    from pytube import YouTube
    link = input('Please enter the video URL : ')
    video = YouTube(link)
    path = "C:Downloads"
    quality = input('Please Enter the Quality you want - h for High Qualiy, l for Low Qualiy : ')
    if quality == 'h':
        print(f'Your Video {video.title} is Downloading ....\n -----------------------------------')
        print('Video is Downloading....\n -----------------------------------')    
        video.streams.get_highest_resolution().download(output_path=path)
        video.register_on_progress_callback(downloading(video.streams.get_lowest_resolution().resolution))
        video.register_on_complete_callback(finish())
    elif quality == 'l':
        print('Video is Downloading....\n -----------------------------------')
        video.streams.get_lowest_resolution().download(output_path=path)
        video.register_on_progress_callback(downloading(video.streams.get_lowest_resolution().resolution))
        video.register_on_complete_callback(finish())
    else:
                print("Don't forget to Choose the Quality You want")
elif ask == 'p':
    # --------------------------- Download from Playlist
    from pytube import Playlist
    link = input('Please enter the Playlist URL : ')
    playlist = Playlist(link)
    count = 2
    quality = input('Please Enter the Quality you want - h for High Qualiy, l for Low Qualiy : ')
    if quality == 'h':
        print(f'Your playlist {playlist.title} is Downloading ....\n -----------------------------------')
        print(f'Video Number 1 is Downloading....\n -----------------------------------')
        dir = os.path.join("C:","Downloads",f"{playlist.title}")
        if not os.path.exists(dir):
            os.mkdir(dir)
        for videos in playlist.videos:
            videos.streams.get_highest_resolution().download(output_path=f'C:Downloads\{playlist.title}')
            videos.register_on_progress_callback(playListDownloading(count,videos.streams.get_highest_resolution().resolution))
            count += 1
            
    elif quality == 'l':
        print(f'Your playlist {playlist.title} is Downloading😊 ....\n -----------------------------------')
        print(f'Video Number 1 is Downloading....\n -----------------------------------')
        dir = os.path.join("C:","Downloads",f"{playlist.title}")
        if not os.path.exists(dir):
            os.mkdir(dir)
        for videos in playlist.videos:
            videos.streams.get_lowest_resolution().download(output_path=f'C:Downloads\{playlist.title}')
            videos.register_on_progress_callback(playListDownloading(count,videos.streams.get_lowest_resolution().resolution))
            count += 1
    else:
        print("Don't forget to Choose the Quality You want")
    finish()
else:
    # ---------------------------- Nothing
    print("Thank you so much, Have a nice day :-)")