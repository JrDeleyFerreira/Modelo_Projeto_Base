from pytubefix import YouTube

url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
yt = YouTube(url)

stram = yt.streams.get_highest_resolution()
stram.download(skip_existing=True, max_retries=1, output_path="downloads")


def main():
    print("Hello from modelo-projeto-base!")


if __name__ == "__main__":
    main()
