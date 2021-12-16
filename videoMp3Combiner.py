def videomp3combiner(videoName: str, audioName: str, outputName: str):
    import moviepy.editor as mpe
    clip = mpe.VideoFileClip(videoName)

    final_clip = clip.set_audio(mpe.AudioFileClip(audioName))
    final_clip.write_videofile(outputName, codec='libx264',
                               audio_codec='aac',
                               temp_audiofile='temp-audio.m4a',
                               remove_temp=True)


# videomp3combiner("output.mp4", "theaudio.mp3", "combined.mp4")
