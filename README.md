# python-opencv
Playground OpenCV

## ffmpeg
- The simplest solution in Windows OS, is placing ffmpeg.exe in the same folder as the Python script.

- The reason you are getting the error, is that ffmpeg.exe is not in the execution path of your operating system.
- Note: Executing **pip install ffmpeg-python** does not download FFmpeg application (but the Python package requires FFmpeg executable for functioning).

- Assuming you are using Windows:
```
Download the latest stable release from https://github.com/BtbN/FFmpeg-Builds/releases.
Static build in preferred (static build applies single executable file).
You may download a GPL licensed version (GPL versus LGPL is not relevant for executables).
The latest stable release up to date (Jan 23 2021) is 4.3.1
Assuming you are using Windows x64, download: ffmpeg-n4.3.1-29-g89daac5fe2-win64-gpl-4.3.zip 
Extract the ZIP file, and copy ffmpeg.exe to the same folder as your Python script.
In case it's working, you may also put ffmpeg.exe someplace else (like C:\ffmpeg\bin\), and update the Windows path.
Update:
There is an option to execute ffmpeg.exe, without adding it to the system path.

The method ffmpeg.run() accepts the optional argument cmd.
The default value of cmd is ffmpeg.
You can set the value of cmd to the full execution path.

Example:

(
    ffmpeg
    .concat(input_video, merged_audio, v=1, a=1)
    .output("mix_delayed_audio.mp4")
    .run(overwrite_output=True, cmd=r'c:\FFmpeg\bin\ffmpeg.exe')
)
```
