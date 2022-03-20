from pytube import YouTube
import os

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)

    print("\nDownloading...")
    yt.download(path)
    print("Download Completed")


def main():
    link = input("Enter the YouTube link : ")
    
    downloadYouTube(link, "C:\\Users\\Adithiyaa\\OneDrive\\Desktop\\")

if __name__ == '__main__':
    main()
