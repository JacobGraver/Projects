import pytube

import tkinter
import customtkinter

# Download function
def download():
    try:
        ytLink = 

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=40, textvariable=url_var) # origionally 350
link.pack()

# Download button
download = customtkinter.CTkButton(app, text="Download", command=download)

app.mainloop()
