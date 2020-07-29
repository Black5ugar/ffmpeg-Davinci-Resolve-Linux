"""
this is a script for me to change the video's
format in oreder to be used in Davinci Resolve
created by blacksugar

default video encoder: mpeg4
default audio encoder: pcm_s8

an example for the command:
ffmpeg -i <input_file> -c:v mpeg4 -c:a pcm_s8 -q:v 0 -q:a 0 <output_file>

if you don't have the module named 'tkinter'
try:
sudo apt-get install python3-tkinter on ubuntu
sudo pacman -S python-pmw on archlinux
"""
import os


import tkinter as tk
import tkinter.filedialog

from tkinter import ttk
root = tk.Tk()


# set a title
root.title('ffmpeg')

# set the window size
root.geometry('850x150')

# 1.the Combobox for setting the video encoding format
video_lable = tk.Label(root, text='video encoder', width=15, font=30)
video_lable.grid(row=1)

video_cmb = ttk.Combobox(root, width=15)
video_cmb.grid(row=2, column=0)
video_cmb['value'] = ('mpeg4')
video_cmb.current(0)

# 2.the Combobox for setting the audio encoding format
audio_lable = tk.Label(root, text='audio encoder', width=15, font=30)
audio_lable.grid(row=1, column=1)

audio_cmb = ttk.Combobox(root, width=15)
audio_cmb['value'] = ('pcm_s8')
audio_cmb.current(0)
audio_cmb.grid(row=2, column=1)

# 3.the output file settings
# the output file entry
output_lable = tk.Label(root, text='output filename', width=15, font=30)
output_lable.grid(row=1, column=2)

output_entry = tk.Entry(root, width=15)
output_entry.grid(row=2, column=2)

# the output file format
outputformat_lable = tk.Label(root, text="format", width=15, font=30)
outputformat_lable.grid(row=1, column=3)

outputformat_cmb = ttk.Combobox(root, width=15)
outputformat_cmb['value'] = ('.mov')
outputformat_cmb.current(0)
outputformat_cmb.grid(row=2, column=3)


def transformat():
    """
    the button of trans format
    """
    outputfilename = output_entry.get()
    outputfileformat = outputformat_cmb.get()
    inputfilename = inputfile_entry.get()
    audioencoder = audio_cmb.get()
    videoencoder = video_cmb.get()
    outputfile = outputfilename + outputfileformat

    os.popen(f'ffmpeg -i {inputfilename} -c:v {videoencoder} -c:a {audioencoder} -q:v 0 -q:a 0 {outputfile}')


trans_btn = tk.Button(root, text='transfor', width=10, command=transformat)
trans_btn.grid(row=2, column=4)


# 4.choose a file
# the input file entry
inputfile_entry = tk.Entry(root, width=73)
inputfile_entry.grid(row=3, column=0, columnspan=4, padx=10, pady=25)

# the button of choosing file dialog
def choose_inputfile():
    inputfilename = tkinter.filedialog.askopenfilename()
    inputfile_entry.insert('end', inputfilename)


choose_btn = tk.Button(root, text='select', width=10, command=choose_inputfile)
choose_btn.grid(row=3, column=4)


root.mainloop()
