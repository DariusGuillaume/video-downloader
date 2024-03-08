
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

import certifi
import os

os.environ['SSL_CERT_FILE'] = certifi.where()

def download_video():
    url = entry_url.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if stream:
            stream.download()
            messagebox.showinfo("Success", "Download completed successfully!")
        else:
            messagebox.showerror("Error", "No compatible MP4 format available for download.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create a label and entry for the URL
label_url = tk.Label(root, text="Enter YouTube URL:")
label_url.pack()

entry_url = tk.Entry(root, width=50)
entry_url.pack()

# Create a download button
button_download = tk.Button(root, text="Download", command=download_video)
button_download.pack()

# Run the Tkinter event loop
root.mainloop()
