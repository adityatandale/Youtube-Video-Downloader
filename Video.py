from tkinter import *
from tkinter import filedialog, messagebox
import yt_dlp

# Function to download video
def download_video():
    url = link.get()

    if url == "":
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    # Select folder
    folder = filedialog.askdirectory()

    if folder == "":
        return

    ydl_opts = {
        'outtmpl': folder + '/%(title)s.%(ext)s',
        'format': 'best'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Video Downloaded Successfully")

    except Exception as e:
        messagebox.showerror("Download Error", str(e))


# GUI Window
root = Tk()
root.geometry("500x300")
root.title("YouTube Video Downloader")
root.config(bg="#f2f2f2")

# Heading
heading = Label(
    root,
    text="YouTube Video Downloader",
    font=("Arial", 20, "bold"),
    bg="#f2f2f2",
    fg="red"
)
heading.pack(pady=20)

# URL Label
url_label = Label(
    root,
    text="Enter YouTube Video URL",
    font=("Arial", 12),
    bg="#f2f2f2"
)
url_label.pack()

# URL Entry
link = StringVar()

url_entry = Entry(
    root,
    textvariable=link,
    width=50,
    font=("Arial", 12)
)
url_entry.pack(pady=10)

# Download Button
download_btn = Button(
    root,
    text="Download Video",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    padx=10,
    pady=5,
    command=download_video
)
download_btn.pack(pady=20)

# Run App
root.mainloop()