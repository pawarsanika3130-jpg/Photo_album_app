import tkinter as tk
import time
from PIL import Image, ImageTk

#main application window
root=tk.Tk()
root.title("My Photo Album")
root.geometry("900x900")

#List of image paths
image_path=[
    r"C:/Users/amolj/OneDrive/Desktop/Album/car3.jpg",
    r"C:/Users/amolj/OneDrive/Desktop/Album/cars.jpeg",
    r"C:/Users/amolj/OneDrive/Desktop/Album/cars2.jpg",
    r"C:/Users/amolj/OneDrive/Desktop/Album/CRT_7130.jpg",
    r"C:/Users/amolj/OneDrive/Desktop/Album/download.jpeg"
]
image_size=(700,700)
images=[]
for path in image_path:
    img=Image.open(path)
    img=img.resize(image_size)
    images.append(img)#adding each image in the list
    
#convert PIL images into Tkinter readable image
final_images=[]
for img in images:
    photo= ImageTk.PhotoImage(img)
    final_images.append(photo)
    
#label widget to keep photo
image_label=tk.Label(root)
image_label.pack(pady=30)#it helps to show the label widget

#Slideshow
def starts_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)
        
#button
play_button=tk.Button(
    root,
    text="Play the Slideshow",
    font=("Arial",17),
    command=starts_slideshow
    
    )
play_button.pack(pady=40)

root.mainloop()