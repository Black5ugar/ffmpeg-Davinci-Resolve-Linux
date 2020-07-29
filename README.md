# ffmpeg-Davinci-Resolve-Linux
A ffmpeg GUI Based on Tkinter, transcoding video, in order to be used in DaVinci resolve Linux

## preparation
To ensure that you can use this python script, plz make sure that ffmpeg is installed
on your operating system.  
+ for ubuntu:
　　`sudo apt-get install ffmpeg`
+ for archlinux:
　`sudo pacman -S ffmpeg`
  
Also, make sure that tkinter is installed on your system.
+ for ubuntu:　`sudo apt install python3-tkinter`
+ for archlinux:`sudo pacman -S python-pmw`

## what is this python script for
The graphical transcoder based on tkinter and ffmpeg is mainly used to use davinci resolve on Linux, this is because davinci resovle linux does not support most mainstream video encoding.  
The transcoder is currently only an initial version(0.1Beta?), video encoding can only use `mpeg4`, audio can only use `pcm_s8`, the output format is only `mov` now, but it's enough for personal use.(Davinci Linux version is just a disabled version)  
If you need another encoding format, you can add it inside the source code yourself.
## instructions 
`python trans.py`
