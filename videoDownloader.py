import os
username = os.getlogin()
def finish():
    print('Download Completed, Enjoy My Friend\n -----------------------------------')

def downloading(resolution):
    print(f'Video Quality is : {resolution}\n -----------------------------------')
    print('Video is Downloading....\n -----------------------------------')

def playListDownloading(count,res):
    print(f'Video Quality is : {res}\n -----------------------------------')
    print(f'Video Number {count} is Downloading....\n -----------------------------------')

# Download from Playlist
ask = input('v For One Video, p For Playlist videos, n For Nothing : ')

if ask == 'v':
    # --------------------------- Download Single Video
    from pytube import YouTube
    link = input('Please enter the video URL : ')
    video = YouTube(link)
    stuff_in_string = f"C:\Users\maham\Downloads"
    video.streams.get_lowest_resolution().download(output_path=stuff_in_string)
    video.register_on_progress_callback(downloading(video.streams.get_lowest_resolution().resolution))
    video.register_on_complete_callback(finish())
elif ask == 'p':
    # --------------------------- Download from Playlist
    from pytube import Playlist
    link = input('Please enter the Playlist URL : ')
    playlist = Playlist(link)
    count = 2
    quality = input('Please Enter the Quality you want - h for High Qualiy, l for Low Qualiy : ')
    if quality == 'h':
        for videos in playlist.videos:
            # print(videos.streams.get_lowest_resolution())
            videos.streams.get_highest_resolution().download(output_path='F:\A WebDevelopment\Wordpress Stuff\Wordpress Course')
            print(f'Video Number 1 is Downloading....\n -----------------------------------')
            videos.register_on_progress_callback(playListDownloading(count,videos.streams.get_highest_resolution().resolution))
            count += 1
    elif quality == 'l':
        for videos in playlist.videos:
            # print(videos.streams.get_lowest_resolution())
            videos.streams.get_lowest_resolution().download(output_path='F:\A WebDevelopment\Wordpress Stuff\Wordpress Course')
            print(f'Video Number 1 is Downloading....\n -----------------------------------')
            videos.register_on_progress_callback(playListDownloading(count,videos.streams.get_lowest_resolution().resolution))
            count += 1
    else:
        print("Don't forget to Choose the Quality You want")
    finish()
else:
    # ---------------------------- Nothing
    print("Thank you so much, Have a nice day :-)")