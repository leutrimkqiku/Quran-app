import tkinter as tk
from PIL import ImageTk, Image
import pygame
from tkinter import ttk

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Create a list of MP3 file paths and PNG image paths
mp3_files = [
    ("Quran app/elif.mp3", "PNG/ELIF.png"),
    ("Quran app/ba.mp3", "PNG/BA.png"),
    ("Quran app/te.mp3", "PNG/TE.png"),
    ("Quran app/the.mp3", "PNG/THE.png"),
    ("Quran app/gjim.mp3", "PNG/GJIM.png"),
    ("Quran app/ha.mp3", "PNG/HA.png"),
    ("Quran app/haa.mp3", "PNG/HAA.png"),
    ("Quran app/del.mp3", "PNG/DEL.png"),
    ("Quran app/dhel.mp3", "PNG/DHEL.png"),
    ("Quran app/ra.mp3", "PNG/RA.png"),
    ("Quran app/ze.mp3", "PNG/ZE.png"),
    ("Quran app/sin.mp3", "PNG/SIN.png"),
    ("Quran app/shin.mp3", "PNG/SHIN.png"),
    ("Quran app/sad.mp3", "PNG/SAD.png"),
    ("Quran app/dad.mp3", "PNG/DAD.png"),
    ("Quran app/ta.mp3", "PNG/TA.png"),
    ("Quran app/dha.mp3", "PNG/DHA.png"),
    ("Quran app/ain.mp3", "PNG/AIN.png"),
    ("Quran app/gain.mp3", "PNG/GAIN.png"),
    ("Quran app/fil.mp3", "PNG/FIL.png"),
    ("Quran app/kaf.mp3", "PNG/KAF.png"),
    ("Quran app/kef.mp3", "PNG/KEF.png"),
    ("Quran app/lam.mp3", "PNG/LAM.png"),
    ("Quran app/mim.mp3", "PNG/MIM.png"),
    ("Quran app/nun.mp3", "PNG/NUN.png"),
    ("Quran app/he.mp3", "PNG/HE.png"),
    ("Quran app/uau.mp3", "PNG/UAU.png"),
    ("Quran app/je.mp3", "PNG/JE.png"),





]

# Create a new Tkinter window
window = tk.Tk()
# Set the window title
window.title("MP3 Player")
# Create buttons for each MP3 file
buttons = []
x=0
for mp3_path, png_path in mp3_files:
    

    # Load the PNG image and create a button with the image\

    img = Image.open(png_path)
    img = img.resize((100, 100))
    img = ImageTk.PhotoImage(img)

    button = tk.Button(window, image=img, command=lambda path=mp3_path: play_mp3(path))
    button.image = img  # Save a reference to the image to avoid garbage collection
    if x < 7:
        button.grid(column=x,row=0 , padx=5,pady=5)
        buttons.append(button)
    elif x < 14:
        button.grid(column=x-7,row=1 , padx=5,pady=5)
        buttons.append(button)
    elif x < 21:
        button.grid(column=x-14,row=2 , padx=5,pady=5)
        buttons.append(button)
    else:
        button.grid(column=x-21,row=3 , padx=5,pady=5)
        buttons.append(button)
    x=x+1
notebook = ttk.Notebook(window)
 


# Start the Tkinter event loop
window.mainloop()