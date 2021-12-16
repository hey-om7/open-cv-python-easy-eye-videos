import moviepy.editor as mp


def convertToMp3(videoName: str):
    clip = mp.VideoFileClip(videoName)
    clip.audio.write_audiofile("theaudio.mp3")
    return "Converted"


# print(convertToMp3("vid.mp4"))
